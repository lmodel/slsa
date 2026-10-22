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
  - resource: https://github.com/slsa-framework/slsa/blob/main/README.md
    title: the SLSA repository README, License section
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:14:46Z"
status: draft
author:
  - type: Organization
    id: https://w3id.org/lmodel/slsa/knowledge/org/slsa-project
    name: SLSA project (OpenSSF)
verified:
  - by: process:ktl-librarian
    at: "2026-10-22T18:46:59Z"
---

# SLSA specification

SLSA (Supply-chain Levels for Software Artifacts) is a specification for describing and incrementally improving supply chain security. It is organized into tracks, and each track into levels that give increasing security guarantees. Its home is <https://slsa.dev>.

`docs/about.md` says the schema targets SLSA v1.2, "which defines the four tracks (Build, Source, Dependency, Build Environment) and the in-toto-based attestation model". The schema header in `src/slsa/schema/slsa.yaml` names `https://slsa.dev/spec/v1.0` as its `source` and lists `https://slsa.dev/spec/v1.2/` under `see_also`.

A copy of the specification's Markdown pages is kept in this repository: see [the SLSA specification copy](../datasets/slsa-spec-copy.md).

## License

The SLSA repository's README puts content contributed under the Community Specification governance model under the Community Specification License 1.0, and pre-existing portions from contributors who have not contributed again under it under the Apache License 2.0. Section 1.2 of the Community Specification License requires anyone who makes a derivative work to attribute it to the Working Group, naming at minimum the material's name, version number and source.

## Open questions

- 2026-10-21, process:ktl-librarian: `docs/about.md` says the schema targets SLSA v1.2, but the schema header in `src/slsa/schema/slsa.yaml` gives `source: https://slsa.dev/spec/v1.0` and `version: 1.0.0`. Which specification version does the schema follow, and should the header's `source` move to v1.2?
