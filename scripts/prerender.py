#!/usr/bin/env python3
"""Pre-render client-side React pages so crawlers and AI agents can read them.

The ConsumIQ page builds its DOM in the browser (React + Babel via CDN), so
anything that doesn't run JavaScript sees an empty <div id="root">. This script
renders the page in headless Chrome, takes the rendered #root markup and writes
it back into the source file between prerender markers. React's createRoot()
replaces that markup on load, so visitors get the same live app.

Re-run after editing the JSX:  python3 scripts/prerender.py
"""
import functools
import http.server
import pathlib
import re
import subprocess
import sys
import threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ["archive/ConsumIQ.html"]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
START, END = "<!-- prerender:start -->", "<!-- prerender:end -->"
ROOT_RE = re.compile(r'(<div id="root">)(.*?)(</div>\s*\n\s*<script type="text/babel">)', re.S)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def render(url):
    out = subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=15000",
         "--window-size=1440,900", "--dump-dom", url],
        capture_output=True, text=True, timeout=120, check=True,
    ).stdout
    m = re.search(r'<div id="root">(.*)</div>\s*<script type="text/babel"', out, re.S)
    if not m or len(m.group(1)) < 1000:
        sys.exit(f"render of {url} produced no #root content; is the CDN reachable?")
    return re.sub(r"\s*<!-- prerender:(start|end) -->\s*", "", m.group(1)).strip()


def main():
    srv = serve()
    try:
        for page in PAGES:
            path = ROOT / page
            src = path.read_text()
            html = render(f"http://127.0.0.1:{srv.server_port}/{page}")
            new, n = ROOT_RE.subn(lambda m: f"{m.group(1)}{START}{html}{END}{m.group(3)}", src, count=1)
            if n != 1:
                sys.exit(f"could not find <div id=\"root\"> followed by the babel script in {page}")
            path.write_text(new)
            print(f"{page}: {len(html):,} chars pre-rendered")
    finally:
        srv.shutdown()


if __name__ == "__main__":
    main()
