---
type: Service
id: https://w3id.org/lmodel/slsa/knowledge/services/documentation-site
genre: reference
title: slsa documentation site
description: The MkDocs site at `https://lmodel.github.io/slsa`, generated from the slsa schema and deployed to GitHub Pages on every push to main, with a preview built for each pull request.
resource: mkdocs.yml
endpoint: https://lmodel.github.io/slsa
documentation: https://lmodel.github.io/slsa
sources:
  - resource: .github/workflows/deploy-docs.yaml
    title: the deploy workflow
  - resource: .github/workflows/test_pages_build.yaml
    title: the pull request preview workflow
  - resource: docs/
    title: the site's hand-written pages
dependsOn:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-21T22:14:46Z"
---

# Documentation site

`.github/workflows/deploy-docs.yaml` runs on every push to `main` and by hand. It runs `just gen-doc`, which writes the per-element pages into the git-ignored `docs/elements/` and the merged schema into `docs/schema/`, and then `mkdocs gh-deploy`, which publishes the site to the `gh-pages` branch.

`.github/workflows/test_pages_build.yaml` builds the site with `mkdocs build` for each opened, reopened or updated pull request, and publishes a preview with `rossjrw/pr-preview-action`.

The hand-written pages are `docs/index.md` and `docs/about.md`. The about page links `docs/Secure_Software_Factory_Whitepaper.pdf`. `just testdoc` builds the site and serves it locally.
