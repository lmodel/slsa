---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
genre: reference
title: SLSA specification
description: Supply-chain Levels for Software Artifacts (SLSA), the OpenSSF specification of tracks and levels for supply chain security; the slsa LinkML schema renders version 1.2, its Build and Source tracks, and the working draft's Dependency and Build Environment tracks.
resource: https://slsa.dev/spec/v1.2/
sources:
  - resource: docs/about.md
    title: the opening paragraph
  - resource: src/slsa/schema/slsa.yaml
    title: the schema header's version, source, see_also and comments
  - resource: https://github.com/slsa-framework/slsa/blob/main/README.md
    title: the SLSA repository README, License section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:20:11Z"
status: draft
author:
  - type: Organization
    id: https://w3id.org/lmodel/slsa/knowledge/org/slsa-project
    name: SLSA project (OpenSSF)
verified:
  - by: process:ktl-librarian
    at: "2026-10-27T12:57:54Z"
---

# SLSA specification

SLSA (Supply-chain Levels for Software Artifacts) is a specification for describing and incrementally improving supply chain security, established by industry consensus. It is organized into a series of levels that describe increasing security guarantees, and [SLSA track](../glossary/slsa-track.md) says how the levels sit in tracks. Its home is <https://slsa.dev>.

`docs/about.md` says that the schema is a LinkML model of the SLSA specification, version 1.2. It renders the specification's Build and Source tracks, the build provenance and Verification Summary Attestation predicates, and the roles, build platform and package model the specification defines. The in-toto statement layer they sit in comes from lmodel/in-toto's core module, which `src/slsa/schema/in_toto/in_toto_core.yaml` vendors, and `SlsaStatement` adds SLSA's fields to its statement. [in-toto attestation framework](in-toto-attestation.md) describes that layer. The Dependency and Build Environment tracks follow the working draft at version 1.2, which the release does not include.

The schema header in `src/slsa/schema/slsa.yaml` agrees. It gives `version: 1.2.0` and `source: https://slsa.dev/spec/v1.2`, and lists `https://slsa.dev/spec/v1.2/` under `see_also`. A comment says that the version is the SLSA specification version the model renders.

A copy of the specification's pages is kept in this repository: see [the SLSA specification copy](../datasets/slsa-spec-copy.md).

## License

The SLSA repository's README gives two licenses. Content contributed under the Community Specification governance model is under the Community Specification License 1.0. Pre-existing portions from contributors who have not contributed again under that license are under the Apache License 2.0. Section 1.2 of the Community Specification License requires anyone who makes a derivative work to attribute it to the Working Group, naming at minimum the material's name, version number and source.
