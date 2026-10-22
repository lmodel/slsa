# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.1.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.2.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

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
