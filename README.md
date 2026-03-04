# Jaynes Archive

Minimal Hugo site for the E.T. Jaynes paper archive.

## What remains in this repo
- `content/papers`: paper pages (Markdown front matter + content)
- `data/clusters.json`: landing page grouping
- `data/summaries.json`: short summary text for landing cards
- `static/pdfs/raw` and `static/pdfs/clean`: downloadable PDFs
- `layouts/*` and `static/js/search.js`: site UI and client-side search
- `scripts/workbench_server.py` + `scripts/workbench`: local audit workbench UI/API

## Run locally
1. Install Hugo.
2. Run the site:
   `make app`
3. Run the workbench (expects Hugo on `http://localhost:1313`):
   `make workbench`

Workbench Python deps:
`pip install fastapi uvicorn pymupdf httpx`

## Deploy on Netlify
- This repo includes [netlify.toml](/home/dave/Projects/jaynes-archive/netlify.toml).
- Netlify should auto-detect:
  - Build command: `hugo --gc --minify`
  - Publish directory: `public`

If you still see Netlify "Page not found", check:
1. Site settings -> Build & deploy -> Publish directory is exactly `public`.
2. Deploy log shows Hugo build succeeded (not skipped/failed).
3. The deployed branch is the one containing this repo content (`master` or `main`).
