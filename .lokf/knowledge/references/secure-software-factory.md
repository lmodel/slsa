---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/secure-software-factory
genre: reference
title: CNCF Secure Software Factory whitepaper
description: The CNCF TAG-Security Secure Software Factory whitepaper (2022), a reference architecture for an end-to-end SLSA pipeline; the schema's slsa_ssf subset draws on it.
resource: docs/Secure_Software_Factory_Whitepaper.pdf
sources:
  - resource: docs/about.md
    title: the CNCF TAG-Security Secure Software Factory section
  - resource: src/slsa/schema/slsa.yaml
    title: the slsa_ssf subset
  - resource: https://github.com/cncf/tag-security/blob/main/community/working-groups/supply-chain-security/secure-software-factory/Secure_Software_Factory_Whitepaper.pdf
    title: the upstream copy of the whitepaper
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:14:46Z"
status: draft
author:
  - type: Organization
    id: https://w3id.org/lmodel/slsa/knowledge/org/cncf-tag-security
    name: CNCF TAG-Security
license: https://creativecommons.org/licenses/by/4.0/
verified:
  - by: process:ktl-librarian
    at: "2026-10-22T18:46:59Z"
---

# CNCF Secure Software Factory whitepaper

The whitepaper is kept in the repository as `docs/Secure_Software_Factory_Whitepaper.pdf`. `docs/about.md` describes it as CNCF TAG-Security's 2022 reference architecture for end-to-end SLSA implementation, composed of six pipeline stages:

- Version Control System;
- CI Build Service;
- Artifact Registry;
- Signing Service (Sigstore, Cosign, Fulcio);
- Policy Engine (OPA, Gatekeeper, Kyverno);
- Runtime Security.

Schema elements drawn from this architecture are tagged with the `slsa_ssf` subset. `docs/about.md` names `pipelineOrchestrator`, `signingTool`, `sigstoreLogEntry`, `guacUri` and `securityInsightsUri`. The subset's description in the schema points at <https://github.com/cncf/tag-security/tree/main/community/working-groups/supply-chain-security/secure-software-factory>.

## Upstream copy

The file is byte-identical to `community/working-groups/supply-chain-security/secure-software-factory/Secure_Software_Factory_Whitepaper.pdf` in the archived `cncf/tag-security` repository: both have the git blob hash `c3c6b99f8444fa1d78fef15ace5baba12d37d1bf`. That repository licenses its documentation under CC BY 4.0.
