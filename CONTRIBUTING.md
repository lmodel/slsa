# Contributing to slsa

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives: a code comment, a workflow header, or a linked page. `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

Thanks for your interest in improving this LinkML schema for SLSA.

## What this project is

A LinkML schema for the SLSA specification's tracks, levels and attestation formats, with elements from the CNCF Secure Software Factory whitepaper and the SLSA adoption study, published to PyPI as `slsa-linkml`.

| Path | Holds |
| --- | --- |
| `src/slsa/schema/*.yaml` | The LinkML schema and its modules. Edit these. |
| `src/slsa/schema/spec/` | A copy of the SLSA specification's pages. Never edit. |
| `src/slsa/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `docs/` | The documentation site's pages and the whitepaper. |
| `tests/`, `tests/data/` | Python tests; valid and invalid example data. |
| `.lokf/knowledge/` | This repository's own knowledge bundle. |

## Development setup

Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just) are required.

```bash
git clone https://github.com/lmodel/slsa.git
cd slsa
uv sync --group dev
just --list
```

`just gen-project` regenerates `project/` and the Python datamodel; `just gen-doc` and `just gen-merged` regenerate `docs/schema/` and the site's element pages.

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**; CI installs the librarian skill at run time, pinned to a release. Nothing in the schema depends on them. [The install page](https://w3id.org/ktl/docs/install/) lists every route; with npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Edit the schema, then regenerate.** Edit `src/slsa/schema/`, run `just gen-project`, `just gen-doc`, `just gen-merged` and `just lokf-adapt`, and commit the output; `project/`, `src/slsa/datamodel/`, `docs/schema/` and `.lokf/slsa.yaml` are generated.
- **Cite the passage a description renders.** A class, slot or enum value says what the SLSA specification, the whitepaper or the study says; name the page in the pull request. [AI_COVENANT.md](AI_COVENANT.md) says why.
- **Leave `src/slsa/schema/spec/` as upstream wrote it.** Replace it from a SLSA release instead; [NOTICE](NOTICE) records which release, and `upstream-watch.yaml` checks it.
- **Run the tests**: `just test` (schema generation, `pytest`, and the examples under `tests/data/`). Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-###.yaml`.
- **Follow the schema's conventions**: prefixed UpperCamelCase classes and enums (`SlsaPackage`), snake_case slots, UPPER_CASE values (`.linkmllint.yaml` says why), attributes unless two classes share a field, a short description on every element. `just lint` checks.
- **Run the pre-commit hooks** on what you staged (`uvx pre-commit run`): ruff, yamllint, codespell, typos and the `uv.lock` check.
- **Lock files are part of the change.** CI installs with `uv sync --locked`; a dependency edit that does not update `uv.lock` (or `.lokf/uv.lock`) fails the run.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml` is easy to trip locally**: ShellCheck, actionlint, markdownlint against `.markdownlint-cli2.jsonc`, link-checking against `lychee.toml`, and codespell over every `*.md`.
- **Actions are pinned to commit SHAs**, the version in a trailing comment, and bumped by Dependabot, never by hand to a tag.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour** (not just wording), add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
- Keep changes focused, reference the issue they close, and fill in the PR template's checklist.

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

AI assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike. You are the author of what you submit, and a claim about what SLSA requires must be checked against the specification.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/slsa/issues) for problems with the schema and requests for new elements. A problem with SLSA itself belongs [upstream](https://github.com/slsa-framework/slsa/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go; the release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:` and `security:` cut a release; other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. `uv-dynamic-versioning` reads the version from the tag, so no file is bumped. It then dispatches [`pypi-publish.yaml`](.github/workflows/pypi-publish.yaml) and `.github/workflows/knowledge-release.yaml` for the tag, each once its repository variable, `PYPI_RELEASE_ENABLED` or `KNOWLEDGE_RELEASE_ENABLED`, is `true`.
- Those steps run behind the `release` and `pypi-release` GitHub Environments; configure required reviewers on both in Settings → Environments, or every qualifying merge ships unattended. `pypi-release` must allow deployments from `v*` tags.
- Before the first release, register a pending trusted publisher for `slsa-linkml` on PyPI: workflow `pypi-publish.yaml`, environment `pypi-release`.
- Below 1.0.0: push the `v0.1.0` baseline tag on `main` before the first releasing merge; both release jobs refuse to run without it, as semantic-release would otherwise start at 1.0.0. `.releaserc.json` maps `breaking: true` to `minor`; reaching 1.0.0 means removing that rule in its own PR.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`; leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). The SLSA specification copy and the whitepaper are third-party work under their own terms; [NOTICE](NOTICE) lists them, so update it when you add something new from elsewhere.
