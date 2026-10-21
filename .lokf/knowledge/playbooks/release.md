---
type: Playbook
id: https://w3id.org/lmodel/slsa/knowledge/playbooks/release
genre: how-to
title: Release the slsa package
description: How a version tag or a published GitHub release builds the slsa Python package and publishes it to TestPyPI or PyPI through trusted publishing in the pypi-release environment.
resource: .github/workflows/pypi-publish.yaml
sources:
  - resource: pyproject.toml
    title: the package name and the uv-dynamic-versioning setup
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
---

# Release the slsa package

The package version comes from git through `uv-dynamic-versioning`, with `0.0.0` as the fallback when no tag exists.

`.github/workflows/pypi-publish.yaml` has two jobs:

- `build` checks out the repository, runs `uv build` on Python 3.13, and stores `dist/` as an artifact.
- `pypi-publish` runs in the `pypi-release` environment with `id-token: write` for trusted publishing. On a pushed tag such as `v1.2.3`, it publishes to TestPyPI. On a published GitHub release, it publishes to PyPI.

The environment's URL is `https://pypi.org/p/slsa`, the PyPI project that matches the `name` in `pyproject.toml`.
