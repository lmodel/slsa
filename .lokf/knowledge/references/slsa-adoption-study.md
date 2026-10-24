---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/slsa-adoption-study
genre: reference
title: SLSA adoption study (Tamanna et al., 2024)
description: An empirical study by Tamanna et al. (2024, arXiv:2409.05014) of 1,523 SLSA-related GitHub issues from 233 repositories; the schema's slsa_adoption module encodes its four challenge and five strategy themes as enums on SlsaAdoptionMetadata.
resource: https://arxiv.org/abs/2409.05014
sources:
  - resource: docs/about.md
    title: the Adoption study section
  - resource: src/slsa/schema/slsa_adoption.yaml
    title: the adoption module and its enums
  - resource: https://arxiv.org/abs/2409.05014
    title: the arXiv record's title, authors and abstract
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:22:59Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-22T18:46:59Z"
---

# SLSA adoption study

The arXiv record for 2409.05014 names six authors: Mahzabin Tamanna, Sivana Hamer, Mindy Tran, Sascha Fahl, Yasemin Acar and Laurie Williams. Its abstract says that the study analyzed 1,523 SLSA-related issues extracted from 233 GitHub repositories. It used a topic-guided thematic analysis with Latent Dirichlet Allocation (LDA), and identified four challenges and five suggested adoption strategies.

The current version is titled "Analyzing Challenges in Deployment of the SLSA Framework for Software Supply Chain Security". Version 1, submitted on 8 September 2024, was titled "Unraveling Challenges with Supply-Chain Levels for Software Artifacts (SLSA) for Securing the Software Supply Chain".

`docs/about.md` cites the study as Tamanna et al. (2024), *Analyzing Challenges in Deployment of the SLSA Framework for Software Supply Chain Security*, the arXiv record's current title. It says that the `slsa_adoption` module encodes the four challenge themes and five strategy themes as enums on `SlsaAdoptionMetadata`. The slots `hermetic`, `provenance_generation_tool`, `attestation_storage_uri` and `review_type` record the practices the study discusses, and a comment on the element concerned cites the study's theme.

In the schema, `SlsaAdoptionChallenge` holds `COMPLEX_IMPLEMENTATION`, `UNCLEAR_COMMUNICATION`, `LIMITED_FEASIBILITY` and `UNCLEAR_RELEVANCE`. `SlsaAdoptionStrategy` holds `ENHANCE_ALIGNMENT_FLEXIBILITY`, `PROVIDE_DETAILED_DOCUMENTATION`, `STREAMLINE_PROVENANCE_GENERATION`, `IMPROVE_VERIFICATION_PROCESS` and `COLLABORATE_WITH_COMMUNITY`.
