# Change Log

## 2026-10-21

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
