---
type: Explanation
id: https://w3id.org/lmodel/slsa/knowledge/explanations/schema-subsets
genre: explanation
title: Schema subsets
description: "Why the slsa schema tags its elements with six subsets (one per SLSA track: Build, Source, Dependency and Build Environment, plus slsa_ssf and slsa_adoption_study for what two outside sources add), and what each subset covers."
resource: src/slsa/schema/slsa_core.yaml
isPartOf:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:17:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T22:22:59Z"
sources:
  - resource: docs/about.md
    title: the Beyond the specification section
---

# Schema subsets

`slsa_core.yaml` defines six subsets, and the schema tags its classes, slots and enums with them through `in_subset`. Each subset's description says which part of SLSA or which outside source it covers. An element can belong to several subsets.

- **`slsa_build_track`**: the SLSA Build track, which measures the trustworthiness of a build and its provenance.
- **`slsa_source_track`**: the SLSA Source track, which measures how source revisions are created and managed.
- **`slsa_dependency_track`**: the SLSA Dependency track, a working-draft track for managing risk from third-party dependencies.
- **`slsa_build_environment_track`**: the SLSA Build Environment track, a working-draft track for the integrity of the compute environment that runs builds.
- **`slsa_ssf`**: elements the schema adds from the CNCF TAG-Security Secure Software Factory reference architecture and the OpenSSF supply-chain projects. It tags five slots and no class.
- **`slsa_adoption_study`**: elements the schema adds from the adoption study by Tamanna et al. (2024).

The descriptions of `slsa_ssf` and `slsa_adoption_study` say that their elements are not part of the SLSA specification. `docs/about.md` says the same: two sources add elements that are not SLSA's, each in a subset of its own.

The four track subsets follow the [SLSA tracks](../glossary/slsa-track.md). The other two follow the [Secure Software Factory whitepaper](../references/secure-software-factory.md) and the [adoption study](../references/slsa-adoption-study.md).
