# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.1.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.2.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Changed

- **The schema is rebuilt to LinkML conventions, and every data key changes.** Classes carry a prefix (`InTotoStatement`, `SlsaPackage`), and slots are snake_case attributes of their class. A statement nests its predicate as in-toto does, build parameters and component versions are lists of named values, references between classes go through identifiers, and the paper's citations move from descriptions into comments. Data written for the old schema does not validate.
- **The schema is modular.** `slsa_core` and one module per track or predicate sit under `slsa.yaml`, so an importer can take one module; `docs/schema/slsa.yaml` stays the merged file.
- **`.lokf/slsa.yaml` is regenerated**, and `just lokf-adapt` and `just lokf-adapt-check` write and check it. The README lists the classes a concept may use as its `type`.
- **The specification copy is exactly `docs/spec/draft/` at tag `v1.2`**: `build-requirements.md` is upstream's text again, and three pages that were not in that tree are gone.

### Removed

- **`Builder`** is folded into `SlsaBuildPlatform`, which the specification calls the same thing; **`versionTag`** goes with it. **`SlsaDocument.verifier`** and the other provenance fields on the root go too; the root holds attestations and entities.

## [0.3.1] - 2026-10-23

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.55.2](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.55.0...v0.55.2).** The release changed `.lokf/scripts/knowledge-preflight.sh` and `.lokf/scripts/knowledge-sync.sh` here.

## [0.3.0] - 2026-10-23

### Added

- **The knowledge bundle's domain schema is the SLSA schema.** `.lokf/slsa.yaml` is the copy `lokf adapt` wrote from `src/slsa/schema/slsa.yaml`, and `.lokf/justfile` validates the bundle against it, so a concept may name one of ten SLSA classes as its `type`.
- **A Knowledge Trust Ladder (KTL) section in the README** lists those classes for the plugins' *Known LOKF types* setting and the SLSA keys the copy renames.

## [0.2.0] - 2026-10-22

### Added

- **Governance files.** `AI_COVENANT.md`, `SECURITY.md`, `NOTICE`, this changelog, and issue and pull request templates.
- **Attribution for the SLSA specification copy and the Secure Software Factory whitepaper**, in the README and `NOTICE`, as their licenses ask.
- **`lint-and-docs.yaml`**: ShellCheck, actionlint, word budgets, markdownlint, link checks and codespell.
- **`upstream-watch.yaml`**: a weekly check that `src/slsa/schema/spec/` still matches SLSA's tag `v1.2` and that no newer version is tagged.
- **Releases through semantic-release**, from this changelog, dispatching the PyPI upload and the knowledge bundle zip behind repository variables.

### Changed

- **The distribution is `slsa-linkml`**; the import package stays `slsa`. PyPI publishing is off until `PYPI_RELEASE_ENABLED` is `true`.
- **`just lint` reports errors only**, as CI now runs it; the schema has no lint errors and 85 warnings.
- **`docs/schema/slsa.yaml` is regenerated** from the current schema; it still carried the description from before the last schema change.

### Security

- **Every workflow pins its actions to commit SHAs**, runs harden-runner in audit mode, and declares `permissions: {}` at the top; Dependabot groups the action and dependency updates.
