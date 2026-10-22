---
type: Playbook
id: https://w3id.org/lmodel/slsa/knowledge/playbooks/release
genre: how-to
title: Release the slsa package
description: How a releasing commit merged to main makes semantic-release promote the changelog, tag vX.Y.Z and publish a GitHub Release, and how pypi-publish.yaml then publishes slsa-linkml to PyPI once PYPI_RELEASE_ENABLED is true.
resource: .github/workflows/pypi-publish.yaml
sources:
  - resource: .github/workflows/semantic-release.yml
    title: the plan and release jobs
  - resource: .releaserc.json
    title: the release rules and plugins
  - resource: .github/scripts/changelog-release.mjs
    title: the changelog check, notes and promote steps
  - resource: CONTRIBUTING.md
    title: the Releasing (maintainers) section
  - resource: pyproject.toml
    title: the package name and the uv-dynamic-versioning setup
generated:
  by: process:ktl-librarian
  at: "2026-10-22T18:46:59Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-21T22:14:46Z"
---

# Release the slsa package

The package is named `slsa-linkml` in `pyproject.toml`, and its import package stays `slsa`. Its version comes from git through `uv-dynamic-versioning`, so no file carries the version.

## Cut a release

1. Write the change under `## [Unreleased]` in `CHANGELOG.md` as you go. The release job refuses an empty section.
2. Type each commit with Conventional Commits. Only `feat:`, `fix:` and `security:` cut a release. A pull request that would release must carry a releasing type in its title too, because a squash merge takes its subject from the title.
3. Merge to `main`. The `release` job of `.github/workflows/semantic-release.yml` runs in the `release` GitHub Environment. It retitles the changelog section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release from the same text.

The `plan` job previews every pull request into `main` with `--dry-run`. It fails a pull request that would release with an empty changelog section, or with a title that has no releasing type.

The schema stays below 1.0.0. The `v0.1.0` baseline tag stops semantic-release from making a first release 1.0.0, and both jobs refuse to run without a `v*` tag. `.releaserc.json` maps a breaking change to a minor bump.

## Publish to PyPI

After a release, the `release` job dispatches `.github/workflows/pypi-publish.yaml` on the new tag when the `PYPI_RELEASE_ENABLED` repository variable is `true`. It dispatches `.github/workflows/knowledge-release.yaml` in the same way when `KNOWLEDGE_RELEASE_ENABLED` is `true`.

`pypi-publish.yaml` has two jobs, and both are skipped until `PYPI_RELEASE_ENABLED` is `true`:

- `build` refuses a dispatch from anything but a `v*` tag, runs `uv build` on Python 3.14, and stores `dist/` as an artifact.
- `pypi-publish` runs in the `pypi-release` environment with `id-token: write` for trusted publishing. A dispatch, or a release published by hand, publishes to PyPI. A version tag pushed by a person publishes to TestPyPI. A push of `v0.1.0` triggers nothing.

The environment's URL is `https://pypi.org/p/slsa-linkml`. `CONTRIBUTING.md` asks a maintainer to register a pending trusted publisher for `slsa-linkml` on PyPI before the first release, and to configure required reviewers on the `release` and `pypi-release` environments.
