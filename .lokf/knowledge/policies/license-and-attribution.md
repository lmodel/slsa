---
type: Policy
id: https://w3id.org/lmodel/slsa/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "Which license covers what in the slsa repository: Apache-2.0 for the schema and code, the SLSA specification copy under the Community Specification License 1.0 with its name, version and source attribution, the whitepaper under CC BY 4.0, and what NOTICE lists."
resource: NOTICE
sources:
  - resource: README.md
    title: the License and attribution section
  - resource: LICENSE
    title: the Apache License 2.0
  - resource: CONTRIBUTING.md
    title: the License section
  - resource: pyproject.toml
    title: the license and license-files keys
references:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-spec-copy
  - https://w3id.org/lmodel/slsa/knowledge/references/secure-software-factory
  - https://w3id.org/lmodel/slsa/knowledge/org/slsa-project
  - https://w3id.org/lmodel/slsa/knowledge/org/cncf-tag-security
generated:
  by: process:ktl-librarian
  at: "2026-10-22T18:54:27Z"
status: draft
---

# License and attribution

The README says the schema and the code in this repository are under the Apache License 2.0 (`LICENSE`). `NOTICE` lists the third-party work the repository carries, and `pyproject.toml` names both files in `license-files`, so the package includes them.

## Third-party work

- **The SLSA specification copy.** `src/slsa/schema/spec/` holds "Supply-chain Levels for Software Artifacts", the Working Draft as of version 1.2, by the SLSA Working Group (OpenSSF). It was retrieved from `docs/spec/draft` at SLSA tag v1.2. Content contributed after the group adopted the Community Specification governance model is under the Community Specification License 1.0. Older portions are Apache-2.0. That license asks every derivative work to name the material, its version and its source, and the README names all three. The copy is kept unmodified, and `NOTICE` says which files differ from that tree.
- **The Secure Software Factory whitepaper.** `docs/Secure_Software_Factory_Whitepaper.pdf` is CNCF TAG-Security's whitepaper, copied unmodified from `cncf/tag-security`, whose documentation is under CC BY 4.0.
- **linkml-project-copier.** `NOTICE` says the project was generated from linkml-project-copier, and that its justfile, configuration and documentation scaffolding derive from that template. `NOTICE` carries the template's MIT License text.
- **The knowledge bundle tooling.** `NOTICE` says the scripts under `.lokf/scripts/` and `.lokf/m365/` and the four `knowledge-*.yaml` workflows are copies of the ktl-sidecar templates in knowledge-trust-ladder, under the Apache License 2.0.

## Endorsement

`NOTICE` says that `src/slsa/schema/slsa.yaml`, `src/slsa/datamodel/`, `project/` and the slsa-linkml package are this project's rendering, not an official SLSA release, and that their use does not imply endorsement by the SLSA Working Group or OpenSSF. The README says that this is not an official SLSA release, and that its use does not imply endorsement by the SLSA Working Group, OpenSSF or the CNCF.

## Contributions

`CONTRIBUTING.md` says that contributions are licensed under the Apache License 2.0. It asks a contributor who adds something new from elsewhere to update `NOTICE`.
