---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-spec-copy
genre: reference
title: SLSA specification copy
description: The SLSA specification's Markdown pages, images and provenance schemas (.proto, .cue) copied into `src/slsa/schema/spec/`; 38 of its 42 files match `docs/spec/draft/` at SLSA tag v1.2.
resource: src/slsa/schema/spec/
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
generated:
  by: process:ktl-librarian
  at: "2026-10-22T18:46:59Z"
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
---

# SLSA specification copy

`src/slsa/schema/spec/` holds a copy of the SLSA specification's pages as Markdown with Jekyll front matter: the levels and tracks, the build, source, dependency and build environment track pages, threats, provenance and verification summary formats, and the terminology. `images/` holds the specification's SVG diagrams, and `schema/` holds `provenance.proto` and `provenance.cue`.

`index.md` says this is "the Working Draft of what the next version of the SLSA specification might be" and "**Version 1.2** of the SLSA specification, which defines the SLSA Build and Source tracks". The copy also holds `dependency-track.md` and `build-env-track-basics.md` for the other two tracks. The pages keep their Jekyll template tags, for example the `{%- for section in site.data.nav.main %}` loop in `index.md`.

## Upstream

The copy was added in commit `eb37747` with the schema. Compared by git blob hash with `docs/spec/draft/` in the SLSA repository at tag `v1.2` (commit `19e4e2f`):

- 38 of the 42 files are byte-identical;
- `build-requirements.md` differs in one link, where the copy has `attestation-model#recommended-suite` and the upstream file has `../../attestation-model#recommended-suite`;
- `attested-build-env-levels.md`, `levels.md` and `verifying-systems.md` are not in that folder at that tag.

The [SLSA specification](../references/slsa-specification.md) page gives the license and its attribution condition.

## Upstream watch

`.github/workflows/upstream-watch.yaml` runs `scripts/check_upstream_release.py` every Monday at 07:00 UTC, and by hand. The script compares every copied file with its blob in the pinned tree, `PINNED_TAG = "v1.2"`, by git object hash, and checks whether the SLSA repository has tagged a newer version. It fails on a newer version or on a difference it does not list as known. A failure opens an issue, or comments on the one already open.

## Open questions

- 2026-10-21, process:ktl-librarian: `attested-build-env-levels.md`, `levels.md` and `verifying-systems.md` are not in `docs/spec/draft/` at SLSA tag v1.2, and `build-requirements.md` has one link changed. Where did those three files come from, and was the link changed on purpose?
