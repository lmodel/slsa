---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
genre: reference
title: SLSA specification
description: Supply-chain Levels for Software Artifacts (SLSA), the OpenSSF specification of tracks and levels for supply chain security that the slsa LinkML schema encodes; the schema's docs name v1.2 as the target.
resource: https://slsa.dev/spec/v1.2/
sources:
  - resource: docs/about.md
    title: the SLSA Specification section
  - resource: src/slsa/schema/slsa.yaml
    title: the schema header's source and see_also
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
---

# SLSA specification

SLSA (Supply-chain Levels for Software Artifacts) is a specification for describing and incrementally improving supply chain security. It is organized into tracks, and each track into levels that give increasing security guarantees. Its home is <https://slsa.dev>.

`docs/about.md` says the schema targets SLSA v1.2, "which defines the four tracks (Build, Source, Dependency, Build Environment) and the in-toto-based attestation model". The schema header in `src/slsa/schema/slsa.yaml` names `https://slsa.dev/spec/v1.0` as its `source` and lists `https://slsa.dev/spec/v1.2/` under `see_also`.

A copy of the specification's Markdown pages is kept in this repository: see [the SLSA specification copy](../datasets/slsa-spec-copy.md).

## Open questions

- 2026-10-21, process:ktl-librarian: `docs/about.md` says the schema targets SLSA v1.2, but the schema header in `src/slsa/schema/slsa.yaml` gives `source: https://slsa.dev/spec/v1.0` and `version: 1.0.0`. Which specification version does the schema follow, and should the header's `source` move to v1.2?
