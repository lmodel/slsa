---
type: Explanation
id: https://w3id.org/lmodel/slsa/knowledge/explanations/schema-subsets
genre: explanation
title: Schema subsets
description: Why the slsa schema tags its elements with six subsets (one per SLSA track, plus slsa_ssf and slsa_adoption_study), and what each subset covers.
resource: src/slsa/schema/slsa.yaml
isPartOf:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:14:46Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-22T18:46:59Z"
---

# Schema subsets

The schema tags its classes, slots and enums with `in_subset`. Each subset's description says which part of SLSA or which outside source it covers. An element can belong to several subsets.

- **`slsa_build_track`**: the trustworthiness of the build process and the resulting provenance.
- **`slsa_source_track`**: the trustworthiness of how source revisions are created and managed.
- **`slsa_dependency_track`**: a producer's ability to manage risk from third-party dependencies.
- **`slsa_build_env_track`**: the integrity of the compute environment that runs builds.
- **`slsa_ssf`**: the CNCF Secure Software Factory reference architecture and the OpenSSF Supply Chain Integrity ecosystem. It tags five slots and no class.
- **`slsa_adoption_study`**: the challenge and strategy themes of the adoption study by Tamanna et al. (2024), for documenting adoption status alongside attestation payloads.

The four track subsets follow the [SLSA tracks](../glossary/slsa-track.md). The other two follow the [Secure Software Factory whitepaper](../references/secure-software-factory.md) and the [adoption study](../references/slsa-adoption-study.md).
