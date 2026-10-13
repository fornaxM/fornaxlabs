# Fornax Labs

Fornax Labs is an agentic AI company that builds and orchestrates AI agents for finance and marketing teams.

This repository is the website at **[fornaxlabs.xyz](https://fornaxlabs.xyz/)**, served by Netlify.

## Pages

| Path | What it is |
|---|---|
| `index.html` | Fornax Labs homepage: agent orchestration for finance and marketing teams, plus FAQ |
| `site/ConsumIQ.html` | ConsumIQ, our metering and billing platform for AI-native SaaS (served at `/site/consumiq`) |
| `site/docs.html` | ConsumIQ documentation (served at `/site/docs`) |
| `index_backup.html` | Previous billing-led homepage, kept as a backup and marked `noindex` |

## Discoverability

- `robots.txt` allows search engines and AI crawlers; `sitemap.xml` lists the indexable pages.
- `llms.txt` is a plain-text summary of the company and its pages for AI tools.
- `site/ConsumIQ.html` is a client-side React page. Its rendered markup is saved inside `#root` so crawlers that don't run JavaScript can read it. After editing the page's JSX, regenerate it with:

  ```sh
  python3 scripts/prerender.py
  ```

## Brand

The Forge mark, lockups, colours and favicons are in [`brand-assets/`](brand-assets/README.md).
