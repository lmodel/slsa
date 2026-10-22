# Change Log

## 2026-10-22

* **Changed**: gen-project's settings moved from `config.yaml` to `.linkml/generators.yaml`, which `config.public.mk` now names, so the generated artifacts cite the new path.
* **Resolved**: the merged schema in `docs/schema/slsa.yaml` was regenerated and now carries the schema's new description.
* **Changed**: the source map names `.linkml/generators.yaml` where it named `config.yaml`.

## 2026-10-21

* **Added**: the SLSA project as an organization, from the SLSA repository README.
* **Added**: CNCF TAG-Security as an organization, from its repository's license file.
* **Changed**: the SLSA specification now names its publisher and its license, from the SLSA repository.
* **Changed**: the whitepaper now names its publisher, its upstream copy and its CC BY 4.0 license.
* **Rewrite**: the specification copy now records which upstream tree it matches, from a hash comparison with SLSA tag v1.2.
* **Resolved**: 38 of the 42 files match `docs/spec/draft/` at SLSA tag v1.2 by git blob hash.
* **Question**: three files of the specification copy have no match at SLSA tag v1.2.
* **Changed**: the subsets explanation no longer states a purpose the schema does not give.
* **Changed**: the source map now lists the SLSA and CNCF TAG-Security repositories.
* **Prose**: reworded 4 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Added**: the SLSA specification, from `docs/about.md` and the schema header.
* **Added**: the CNCF Secure Software Factory whitepaper, from `docs/about.md`.
* **Added**: the SLSA adoption study, from `docs/about.md`.
* **Added**: the OpenSSF Software Supply Chain working group, from `docs/about.md`.
* **Added**: the slsa LinkML schema, from `src/slsa/schema/slsa.yaml`.
* **Added**: the SLSA specification copy in `src/slsa/schema/spec/`.
* **Added**: an explanation of the schema's six subsets, from their descriptions in `src/slsa/schema/slsa.yaml`.
* **Added**: the glossary term SLSA track, from the specification copy.
* **Added**: the glossary term SLSA level, from the specification copy and the schema's level enums.
* **Added**: the generated artifacts, from the `justfile` and `config.yaml`.
* **Added**: the test data, from `tests/data/` and `tests/test_data.py`.
* **Added**: the documentation site, from `mkdocs.yml` and the two Pages workflows.
* **Added**: the regenerate-and-test playbook, from the `justfile` and the CI workflow.
* **Added**: the release playbook, from `pypi-publish.yaml` and `pyproject.toml`.
* **Added**: the knowledge sources map from the bootstrap discovery.
* **Question**: the schema header and `docs/about.md` name different SLSA versions.
* **Question**: the specification copy records no upstream commit.
* **Question**: the committed merged schema is older than the source schema.
* **Removal**: the sidecar's Example Service A, replaced by real concepts.
* **Removal**: the sidecar's Example Service B, replaced by real concepts.
* **Initialization**: Scaffolded the LOKF bundle for SLSA with placeholder
  services. Real concepts to follow.
