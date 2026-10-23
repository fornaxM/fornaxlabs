# Fornax Labs

Fornax Labs is an agentic AI platform for small and mid-sized businesses: AI agents that pick up requests from email, WhatsApp, web forms and business tools, do the routine work, and keep people in control.

This repository is the website at **[fornaxlabs.xyz](https://fornaxlabs.xyz/)**, served by Netlify.

## Pages

| Path | What it is |
|---|---|
| `index.html` | Fornax Labs homepage: the agentic platform, use cases (client servicing, finance operations, marketing), tracking, Sugamkar and FAQ |
| `site/sugamkar.html` | Sugamkar, our first product: turns client requests from email, WhatsApp and web forms into one worklist for advisors and service firms (served at `/site/sugamkar`) |

## Archive

`archive/` holds pages that are no longer part of the public site. They are marked `noindex`, excluded in `robots.txt`, left out of `sitemap.xml` and `llms.txt`, and not linked from any live page.

| Path | What it is |
|---|---|
| `archive/ConsumIQ.html` | ConsumIQ, the metering and billing platform for AI-native SaaS (archived 2026-10-23) |
| `archive/docs.html` | ConsumIQ documentation (archived 2026-10-23) |
| `archive/index_backup.html` | Previous billing-led homepage built around ConsumIQ (archived 2026-10-23) |

`_redirects` (Netlify) sends the old public URLs `/site/consumiq`, `/site/docs` and `/index_backup.html` to the homepage.

## Discoverability

- `robots.txt` allows search engines and AI crawlers, except `/archive/`; `sitemap.xml` lists the indexable pages.
- `llms.txt` is a plain-text summary of the company and its pages for AI tools.
- `archive/ConsumIQ.html` is a client-side React page. Its rendered markup is saved inside `#root` so crawlers that don't run JavaScript can read it. After editing the page's JSX, regenerate it with:

  ```sh
  python3 scripts/prerender.py
  ```

## Brand

The Forge mark, lockups, colours, product accents and favicons are in [`brand-assets/`](brand-assets/README.md).
