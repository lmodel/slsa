---
type: Service
id: https://w3id.org/lmodel/slsa/knowledge/services/documentation-site
genre: reference
title: slsa documentation site
description: The Astro Starlight site in `website/`, built from the README, `docs/`, the schema's gen-doc pages and the knowledge bundle by the Knowledge website workflow, which publishes it at `https://lmodel.github.io/slsa/` once `KNOWLEDGE_WEBSITE_ENABLED` is true. Its `REDIRECTS` setting sends the retired mkdocs site's page addresses, such as `/elements/<name>`, on to the new pages.
resource: website/site.config.mjs
endpoint: https://lmodel.github.io/slsa/
documentation: https://lmodel.github.io/slsa/
sources:
  - resource: .github/workflows/knowledge-website.yaml
    title: the build and deploy workflow
  - resource: website/README.md
    title: what each page is built from, and how to preview the site
  - resource: website/scripts/routes.mjs
    title: where a link to a file under `docs/` that is no page goes
  - resource: docs/
    title: the site's hand-written pages
dependsOn:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-27T01:29:08Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-27T12:57:54Z"
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

`website/site.config.mjs` names `docs/` as the docs folder in `DOCS` and gives it no sidebar groups, so the Guide lists the docs pages by title with `docs/index.md` first as its Overview. `docs/about.md` is the only other docs page. `DOCS.exclude` keeps `docs/templates-linkml/` off the site.

`REDIRECTS` in the same file sends three addresses the retired mkdocs site gave its pages on to their new pages: `/elements` to `/schema/`, each `/elements/<name>` to `/schema/<name>/`, and `/about` to `/docs/about/`. Its `/elements/[...slug]` entry stands for one redirect per schema page.

A link from a docs page to a file under `docs/` that is no page of the site opens that file in the repository on GitHub. Such files are `schema/slsa.yaml`, `schema/slsa_merged.yaml` (the same schema with no imports) and `Secure_Software_Factory_Whitepaper.pdf`.

To preview the site, run `npm ci --ignore-scripts` and then `npm run dev` in `website/`. It needs Node.js 22.12 or later and uv.
