---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/secure-software-factory
genre: reference
title: CNCF Secure Software Factory whitepaper
description: The CNCF TAG-Security Secure Software Factory whitepaper (2022), which describes a pipeline of version control, build service, artifact registry, signing service and policy engine; the schema's slsa_ssf subset takes five slots from it.
resource: docs/Secure_Software_Factory_Whitepaper.pdf
sources:
  - resource: docs/about.md
    title: the Secure Software Factory section
  - resource: src/slsa/schema/slsa_core.yaml
    title: the slsa_ssf subset
  - resource: https://github.com/cncf/tag-security/blob/main/community/working-groups/supply-chain-security/secure-software-factory/Secure_Software_Factory_Whitepaper.pdf
    title: the upstream copy of the whitepaper
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:13:40Z"
status: draft
author:
  - type: Organization
    id: https://w3id.org/lmodel/slsa/knowledge/org/cncf-tag-security
    name: CNCF TAG-Security
license: https://creativecommons.org/licenses/by/4.0/
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T23:20:11Z"
---

# CNCF Secure Software Factory whitepaper

The whitepaper is kept in the repository as `docs/Secure_Software_Factory_Whitepaper.pdf`. `docs/about.md` says that the whitepaper, by CNCF TAG-Security (2022), describes a pipeline of version control, build service, artifact registry, signing service and policy engine.

`docs/about.md` names what the schema takes from it, each in the `slsa_ssf` subset:

- `pipeline_orchestrator` on a build definition;
- `signing_tool` and `transparency_log_entry` on `SlsaStatement`;
- `guac_uri` and `security_insights_uri` on a package, which point at the [OpenSSF](openssf-supply-chain.md) projects GUAC and Security Insights.

The subset's description says that these elements are not part of the SLSA specification.

## Upstream copy

The file is byte-identical to `community/working-groups/supply-chain-security/secure-software-factory/Secure_Software_Factory_Whitepaper.pdf` in the archived `cncf/tag-security` repository: both have the git blob hash `c3c6b99f8444fa1d78fef15ace5baba12d37d1bf`. That repository licenses its documentation under CC BY 4.0.
