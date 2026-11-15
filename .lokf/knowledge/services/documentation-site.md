---
type: Service
id: https://w3id.org/lmodel/slsa/knowledge/services/documentation-site
genre: reference
title: slsa documentation site
description: The Hugo site in `website/`, built from the README, `docs/`, the schema's gen-doc pages and the knowledge bundle by the Knowledge website workflow, which publishes it at `https://lmodel.github.io/slsa/` once `KNOWLEDGE_WEBSITE_ENABLED` is true. It sends the retired mkdocs site's page addresses, such as `/elements/<name>`, on to the new pages.
resource: website/site.toml
endpoint: https://lmodel.github.io/slsa/
documentation: https://lmodel.github.io/slsa/
sources:
  - resource: .github/workflows/knowledge-website.yaml
    title: the build and deploy workflow
  - resource: website/README.md
    title: what each page is built from, and how to preview the site
  - resource: website/site.toml
    title: the site's address, title and redirects
  - resource: website/layouts/_partials/route.html
    title: where a link to a file under `docs/` that is no page goes
  - resource: docs/
    title: the site's hand-written pages
dependsOn:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:01:34Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-27T12:57:54Z"
---

# Documentation site

`website/` holds a Hugo site that the ktl-website skill laid down. `website/README.md` says what each page is built from:

- the README is the home page;
- each page under `docs/` is a page under `docs/`;
- each concept in `.lokf/knowledge/` is a page under `knowledge/`, with its trust label;
- `CHANGELOG.md` is a page per release under `changelog/`;
- the schema's `gen-doc` pages are pages under `schema/`, each also at `elements/<Name>/`.

The site also serves the four files `lokf export` writes under `knowledge/`.

`.github/workflows/knowledge-website.yaml` builds the site, with a check of every link between its pages:

- on each push to the default branch that touches its inputs;
- on each pull request that touches its inputs;
- on a run by hand;
- every Monday.

It deploys the default branch's build to GitHub Pages only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`, and deploys nothing for a pull request.

`website/site.toml` names no docs groups, so the pages at the top of `docs/` form one group. The site leaves `docs/templates-linkml/` and `docs/elements/` out.

The home page has the same five buttons on every site: the schema, the bundle, the architecture page, the glossary and the quick start. A button whose page is not there is greyed.

`website/site.toml` sends `/about` on to the page built from `docs/about.md`, and each `/schema/<name>/` address on to that element's page. The site itself sends each `/elements/<name>/` address, which the retired mkdocs site gave a schema page, on to the element's page.

A link from a docs page to a file under `docs/` that is no page of the site opens that file on GitHub. Such files are `schema/slsa_merged.yaml` (the schema with no imports) and `Secure_Software_Factory_Whitepaper.pdf`.

To preview the site, run `scripts/build.sh serve` in `website/`. It needs bash, git and uv, and takes Hugo and Pagefind from PyPI.
