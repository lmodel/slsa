---
type: Policy
id: https://w3id.org/lmodel/slsa/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "Which license covers what in the slsa repository: Apache-2.0 for the schema and code, the SLSA specification copy under the Community Specification License 1.0 (older portions Apache-2.0) with its name, version and source given in NOTICE, the whitepaper under CC BY 4.0, lmodel/in-toto's vendored core module under Apache-2.0, and what else NOTICE lists."
resource: NOTICE
sources:
  - resource: README.md
    title: the License section
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
  - https://w3id.org/lmodel/slsa/knowledge/references/in-toto-attestation
  - https://w3id.org/lmodel/slsa/knowledge/org/slsa-project
  - https://w3id.org/lmodel/slsa/knowledge/org/cncf-tag-security
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:13:40Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-28T18:17:05Z"
---

# License and attribution

The README says that the schema and the code are under the Apache License 2.0 (`LICENSE`). It says that the repository also carries the specification's pages in `src/slsa/schema/spec/` and the CNCF Secure Software Factory whitepaper in `docs/`, each under its own license, and points to `NOTICE`. `NOTICE` lists the third-party work, and `pyproject.toml` names both files in `license-files`, so the package includes them.

## Third-party work

- **The SLSA specification copy.** `NOTICE` says that `src/slsa/schema/spec/` holds "Supply-chain Levels for Software Artifacts", the Working Draft as of version 1.2, by the SLSA Working Group (OpenSSF), retrieved from `docs/spec/draft` at SLSA tag v1.2. Content contributed after the group adopted the Community Specification governance model is under the Community Specification License 1.0. Older portions are Apache-2.0. That license asks every derivative work to name the material, its version and its source, and `NOTICE` names all three. `NOTICE` also says that every file is identical to its counterpart at that tag (commit `19e4e2f`), and that the copy holds nothing else.
- **The Secure Software Factory whitepaper.** `docs/Secure_Software_Factory_Whitepaper.pdf` is CNCF TAG-Security's whitepaper, copied unmodified from `cncf/tag-security`, whose documentation is under CC BY 4.0.
- **linkml-project-copier.** `NOTICE` says that the project was generated from linkml-project-copier, and that its justfile, configuration and documentation scaffolding derive from that template. `NOTICE` carries the template's MIT License text.
- **The knowledge bundle tooling.** `NOTICE` says that the scripts under `.lokf/scripts/` and `.lokf/m365/` and the knowledge-librarian, knowledge-registrar, knowledge-release and knowledge-sync workflows are copies of the ktl-sidecar templates in knowledge-trust-ladder. It says that the site under `website/` and the knowledge-website workflow derive from the ktl-website templates in the same repository, and that `website/NOTICE` lists the part adapted from the LOKF toolkit's site. All of them are under the Apache License 2.0.
- **lmodel/in-toto.** `NOTICE` says that `src/slsa/schema/in_toto/in_toto_core.yaml` is the core module of the in-toto Attestation Framework's LinkML schema from lmodel/in-toto at v0.1.0, under the Apache License 2.0, copied unchanged. It says that `tests/test_in_toto_import.py` pins its git object hash.

## Endorsement

`NOTICE` says that `src/slsa/schema/*.yaml`, `src/slsa/datamodel/`, `project/` and the slsa-linkml package are this project's rendering, not an official SLSA release, and that their use does not imply endorsement by the SLSA Working Group or OpenSSF. The README says that this is not an official SLSA release, and that its use does not imply endorsement by the SLSA Working Group, OpenSSF or the CNCF.

## Contributions

`CONTRIBUTING.md` says that contributions are licensed under the Apache License 2.0. It asks a contributor who adds something new from elsewhere to update `NOTICE`.
