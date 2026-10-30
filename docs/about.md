# About slsa

This project is a [LinkML](https://linkml.io) model of the
[SLSA specification](https://slsa.dev/spec/v1.2/), version 1.2. It renders
the specification's Build and Source tracks, the build provenance and
Verification Summary Attestation predicates, and the roles, build platform
and package model the specification defines. The in-toto statement layer they
sit in comes from lmodel/in-toto's core module, which
`src/slsa/schema/in_toto/in_toto_core.yaml` vendors, and `SlsaStatement` adds
SLSA's fields to its statement. The Dependency and Build Environment tracks
follow the working draft at version 1.2, which the release does not include.
A copy of the specification's pages sits beside the schema in
`src/slsa/schema/spec/`.

Element names carry a prefix (`SlsaStatement`, `SlsaPackage`, and
`InTotoStatement` in the in-toto layer) so they can be imported beside other
vocabularies, slots are snake_case, and permissible values keep the strings
SLSA defines, such as `SLSA_BUILD_LEVEL_3`. Every element links to the page it
renders. The in-toto layer's elements live under `in_toto_linkml:`
(`https://w3id.org/lmodel/in-toto/`), except `media_type` and `algorithm`,
which take the IRIs LOKF gives them, and every other element lives under
`slsa:` (`https://w3id.org/lmodel/slsa/`).

## Beyond the specification

Two sources add elements that are not SLSA's, each in a subset of its own.

### Secure Software Factory (`slsa_ssf`)

The [Secure Software Factory whitepaper](Secure_Software_Factory_Whitepaper.pdf)
(CNCF TAG-Security, 2022) describes a pipeline of version control, build
service, artifact registry, signing service and policy engine. From it the
schema takes `pipeline_orchestrator` on a build definition, `signing_tool` and
`transparency_log_entry` on `SlsaStatement`, and `guac_uri` and
`security_insights_uri` on a package, which point at the
[OpenSSF](https://openssf.org/technical-initiatives/software-supply-chain/)
projects GUAC and Security Insights.

### Adoption study (`slsa_adoption_study`)

Tamanna et al. (2024), *Analyzing Challenges in Deployment of the SLSA
Framework for Software Supply Chain Security*
([arXiv:2409.05014](https://arxiv.org/abs/2409.05014)),
analysed 1,523 SLSA-related GitHub issues. The `slsa_adoption` module encodes
its four challenge themes and five strategy themes as enums on
`SlsaAdoptionMetadata`; `hermetic`, `provenance_generation_tool`,
`attestation_storage_uri` and `review_type` record the practices the study
discusses; and a comment on the element concerned cites the study's theme.
