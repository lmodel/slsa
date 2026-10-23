---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-spec-copy
genre: reference
title: SLSA specification copy
description: "The SLSA specification's Markdown pages, images and provenance schemas (.proto, .cue) copied into `src/slsa/schema/spec/`: all 39 files are identical to `docs/spec/draft/` at SLSA tag v1.2, and a weekly workflow watches for a newer release."
resource: src/slsa/schema/spec/
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:22:59Z"
status: draft
sources:
  - resource: https://github.com/slsa-framework/slsa/tree/v1.2/docs/spec/draft
    title: the SLSA repository's draft specification at tag v1.2 (commit 19e4e2f005f871270c4f555fc47afecfb37f3efe)
  - resource: .github/workflows/upstream-watch.yaml
    title: the weekly upstream watch
  - resource: scripts/check_upstream_release.py
    title: the comparison script and its pinned tag
  - resource: NOTICE
    title: the SLSA specification section
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T22:23:31Z"
---

# SLSA specification copy

`src/slsa/schema/spec/` holds a copy of the SLSA specification's pages as Markdown with Jekyll front matter: the tracks, the build, source, dependency and build environment track pages, threats, provenance and verification summary formats, and the terminology. `images/` holds the specification's SVG diagrams, and `schema/` holds `provenance.proto` and `provenance.cue`.

`index.md` says that this is "the Working Draft of what the next version of the SLSA specification might be" and "**Version 1.2** of the SLSA specification, which defines the SLSA Build and Source tracks". The copy also holds `dependency-track.md` and `build-env-track-basics.md` for the other two tracks. The pages keep their Jekyll template tags, for example the `{%- for section in site.data.nav.main %}` loop in `index.md`.

`CONTRIBUTING.md` says never to edit the copy in place, but to replace it from a SLSA release and update `NOTICE`.

## Upstream

`NOTICE` says that every file is identical to its counterpart in `docs/spec/draft/` in the SLSA repository at tag `v1.2` (commit `19e4e2f`), and that the copy holds nothing else. A comparison by git blob hash bears this out: all 39 files of the copy match the 39 files of that folder at that tag.

The [SLSA specification](../references/slsa-specification.md) page gives the license and its attribution condition.

## Upstream watch

`.github/workflows/upstream-watch.yaml` runs `scripts/check_upstream_release.py` every Monday at 07:00 UTC, and by hand. The script compares every copied file with its blob in the pinned tree, `PINNED_TAG = "v1.2"`, by git object hash, and checks whether the SLSA repository has tagged a newer version. It fails on a newer version or on a difference it does not list as known. Its `KNOWN_DIFFERENCES` list is empty, because the copy is exact. A failure opens an issue, or comments on the one already open.
