---
type: Service
id: https://w3id.org/lmodel/slsa/knowledge/services/documentation-site
genre: reference
title: slsa documentation site
description: The Astro Starlight site in `website/`, built from the README, `docs/`, the schema's gen-doc pages and the knowledge bundle by the Knowledge website workflow, which publishes it at `https://lmodel.github.io/slsa/` once `KNOWLEDGE_WEBSITE_ENABLED` is true. It keeps the addresses of the retired mkdocs site.
resource: website/site.config.mjs
endpoint: https://lmodel.github.io/slsa/
documentation: https://lmodel.github.io/slsa/
sources:
  - resource: .github/workflows/knowledge-website.yaml
    title: the build and deploy workflow
  - resource: website/README.md
    title: what each page is built from, and how to preview the site
  - resource: docs/
    title: the site's hand-written pages
dependsOn:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-23T23:25:14Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T22:22:59Z"
---

# Documentation site

`website/` holds an Astro Starlight site that the ktl-website skill laid down. `website/README.md` says what each page is built from:

- the README is the home page;
- each page under `docs/` is a page under `docs/`;
- each concept in `.lokf/knowledge/` is a page under `knowledge/`, with its trust label;
- `CHANGELOG.md` is a page per release;
- the schema's `gen-doc` pages are pages under `schema/`.

The site also serves the four files `lokf export` writes under `knowledge/`.

`.github/workflows/knowledge-website.yaml` builds the site, with a check of every link between its pages, on each push and pull request that touches its inputs, and every Monday. It deploys the default branch's build to GitHub Pages only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`, and deploys nothing for a pull request.

`website/site.config.mjs` keeps four settings of the retired mkdocs site under `MKDOCS`: its docs folder, its nav, its `exclude_docs` and its `site_url`. The nav orders the docs pages, so `docs/index.md` opens the Guide at `docs/` as its Overview and `docs/about.md` follows. `exclude_docs` keeps `docs/templates-linkml/` off the site. The files mkdocs served from `docs/` are served at the same addresses: `schema/slsa.yaml`, `schema/slsa_merged.yaml`, the same schema with no imports, and `Secure_Software_Factory_Whitepaper.pdf`. Each address mkdocs gave a page, such as `elements/<name>/`, sends the browser on to the page's new address, such as `schema/<name>/`.

To preview the site, run `npm ci --ignore-scripts` and then `npm run dev` in `website/`. It needs Node.js 22.12 or later and uv.
