---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/slsa-adoption-study
genre: reference
title: SLSA adoption study (Tamanna et al., 2024)
description: An empirical study of SLSA adoption in open source projects (arXiv:2409.05014), whose challenge and strategy themes the schema's slsa_adoption_study subset encodes as enums and slots.
resource: https://arxiv.org/abs/2409.05014
sources:
  - resource: docs/about.md
    title: the Adoption Study section
  - resource: src/slsa/schema/slsa.yaml
    title: the slsa_adoption_study subset and its enums
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-21T22:14:46Z"
---

# SLSA adoption study

Tamanna et al. (2024), "An Empirical Study on the Adoption of SLSA in Open Source Projects", performed a thematic analysis of 1,523 SLSA-related GitHub issues across 233 repositories. `docs/about.md` says the four challenge themes (CI, UC, LF, UR) and five strategy themes (S1 to S5) it identified are encoded as enums and slots in the `slsa_adoption_study` subset.

In `src/slsa/schema/slsa.yaml` they appear as `AdoptionChallengeEnum` (four values) and `AdoptionStrategyEnum` (five values), used by the `AdoptionMetadata` class.
