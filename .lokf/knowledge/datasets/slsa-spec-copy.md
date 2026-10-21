---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-spec-copy
genre: reference
title: SLSA specification copy
description: The SLSA specification's Markdown pages, images and provenance schemas (.proto, .cue) copied into `src/slsa/schema/spec/`; its index page calls itself the Working Draft and Version 1.2.
resource: src/slsa/schema/spec/
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
---

# SLSA specification copy

`src/slsa/schema/spec/` holds a copy of the SLSA specification's pages as Markdown with Jekyll front matter: the levels and tracks, the build, source, dependency and build environment track pages, threats, provenance and verification summary formats, and the terminology. `images/` holds the specification's SVG diagrams, and `schema/` holds `provenance.proto` and `provenance.cue`.

`index.md` says this is "the Working Draft of what the next version of the SLSA specification might be" and "**Version 1.2** of the SLSA specification, which defines the SLSA Build and Source tracks". The copy also holds `dependency-track.md` and `build-env-track-basics.md` for the other two tracks.

The pages keep their Jekyll template tags, so they render on <https://slsa.dev> and not in this repository's MkDocs site. The copy was added in commit `eb37747` with the schema; the repository does not record the upstream commit it came from.

## Open questions

- 2026-10-21, process:ktl-librarian: Which upstream commit or release of the SLSA specification was `src/slsa/schema/spec/` copied from? Its `index.md` calls itself both the Working Draft and Version 1.2, and says that version defines the Build and Source tracks, while the copy also carries Dependency and Build Environment track pages.
