# About slsa

Supply-chain Levels for Software Artifacts (LinkML)

This project provides a [LinkML](https://linkml.io) schema for the
[SLSA framework](https://slsa.dev), covering the Build, Source, Dependency,and Build Environment tracks, along with empirical adoption-study metadata and Secure Software Factory ecosystem annotations.

## References

### SLSA Specification

The schema targets [SLSA v1.2](https://slsa.dev/spec/v1.2/), which defines the four tracks (Build, Source, Dependency, Build Environment) and the in-toto-based attestation model.

### CNCF TAG-Security — Secure Software Factory

The [Secure Software Factory Whitepaper](Secure_Software_Factory_Whitepaper.pdf)
(CNCF TAG-Security, 2022) defines a reference architecture for end-to-end SLSA implementation composed of six pipeline stages: Version Control System, CI Build Service, Artifact Registry, Signing Service (Sigstore/Cosign/Fulcio),Policy Engine (OPA/Gatekeeper/Kyverno), and Runtime Security.

Schema elements drawn from the SSF architecture are tagged with the
`slsa_ssf` subset and include `pipelineOrchestrator`, `signingTool`,
`sigstoreLogEntry`, `guacUri`, and `securityInsightsUri`.

### OpenSSF Software Supply Chain Integrity

The [OpenSSF Software Supply Chain](https://openssf.org/technical-initiatives/software-supply-chain/)
working group coordinates SLSA, Sigstore, GUAC, gittuf, Security Insights, and related projects.  Cross-references to these projects are captured in `notes:` and `see_also:` annotations on the relevant schema classes and slots.

### Adoption Study

Tamanna et al. (2024), *"An Empirical Study on the Adoption of SLSA in Open Source Projects"* — [arXiv:2409.05014](https://arxiv.org/abs/2409.05014) — performed thematic analysis of 1,523 SLSA-related GitHub issues across 233 repositories.  The four challenge themes (CI, UC, LF, UR) and five strategy themes (S1–S5) they identified are encoded as enums and slots in the `slsa_adoption_study` subset.
