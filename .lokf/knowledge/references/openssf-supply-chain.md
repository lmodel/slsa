---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/openssf-supply-chain
genre: reference
title: OpenSSF Supply Chain Integrity Working Group
description: The OpenSSF Supply Chain Integrity Working Group, whose software supply chain projects include SLSA, Sigstore, GUAC, gittuf and Security Insights; the schema's guac_uri and security_insights_uri slots point at GUAC and Security Insights.
resource: https://openssf.org/technical-initiatives/software-supply-chain/
sources:
  - resource: docs/about.md
    title: the Secure Software Factory section
  - resource: src/slsa/schema/slsa_core.yaml
    title: the slsa_ssf subset and the guac_uri and security_insights_uri slots
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:17:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T22:22:59Z"
---

# OpenSSF Supply Chain Integrity Working Group

OpenSSF's Software Supply Chain page says that the Supply Chain Integrity Working Group provides a global community for collaborating to help individuals and organizations assess and improve the security of end-to-end supply chains for open source software. The page lists the projects in this area, among them SLSA, Sigstore, GUAC, gittuf, Security Insights, OSPS Baseline and Minder.

`docs/about.md` links this page where it names the slots the `slsa_ssf` subset adds to a package. `guac_uri` and `security_insights_uri` point at the OpenSSF projects GUAC and Security Insights. The `slsa_ssf` subset's description in `slsa_core.yaml` names "the OpenSSF supply-chain projects" as one of its two sources.
