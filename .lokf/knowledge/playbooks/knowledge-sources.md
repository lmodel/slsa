---
type: Playbook
id: https://w3id.org/lmodel/slsa/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external URL this bundle derives concepts from, and how to re-verify each on a refresh run."
resource: https://github.com/lmodel/slsa
sources:
  - resource: README.md
  - resource: pyproject.toml
  - resource: docs/
  - resource: src/slsa/schema/
  - resource: src/slsa/datamodel/
  - resource: project/
  - resource: config.yaml
  - resource: justfile
  - resource: project.justfile
  - resource: tests/
  - resource: mkdocs.yml
  - resource: .github/workflows/main.yaml
  - resource: .github/workflows/deploy-docs.yaml
  - resource: .github/workflows/test_pages_build.yaml
  - resource: .github/workflows/pypi-publish.yaml
  - resource: CONTRIBUTING.md
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
---

# Knowledge sources

Bootstrap discovery ran on 2026-10-21. Steady-state refresh runs re-verify these sources instead of discovering them again. Update this map whenever the repository's knowledge geography changes.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a URL, so re-read the external sources this table names on every refresh.

| Source | Yields | Re-check by |
|--------|--------|-------------|
| `README.md`, `pyproject.toml`, `.copier-answers.yml`, `docs/about.md` | bundle metadata, the four `references/` | diff the manifest name, description and authors; re-read each section of `docs/about.md` |
| `src/slsa/schema/slsa.yaml` | `datasets/slsa-linkml-schema`, `explanations/schema-subsets`, the level enums in `glossary/slsa-level` | reload it and recount classes, slots, enums and subsets; re-read the header's `version`, `source` and `see_also` |
| `src/slsa/schema/spec/` | `datasets/slsa-spec-copy`, the two `glossary/` terms | re-read `index.md`'s version line; re-list the pages; re-read `levels.md`, `tracks.md`, `source-requirements.md` and `dependency-track.md` |
| `docs/Secure_Software_Factory_Whitepaper.pdf` | `references/secure-software-factory` | confirm the file is still there |
| `justfile`, `project.justfile`, `config.yaml`, `project/`, `src/slsa/datamodel/`, `docs/schema/` | `datasets/generated-artefacts`, `playbooks/regenerate-and-test` | re-read the `gen-project`, `gen-python`, `gen-doc` and `test` recipe chains; re-list `project/*/`; re-read `config.yaml` excludes |
| `tests/data/`, `tests/test_data.py` | `datasets/test-data` | re-list `tests/data/`; re-read the test |
| `mkdocs.yml`, `docs/index.md`, `.github/workflows/deploy-docs.yaml`, `.github/workflows/test_pages_build.yaml` | `services/documentation-site` | confirm the triggers and the `gen-doc` plus `gh-deploy` and preview steps |
| `.github/workflows/main.yaml`, `CONTRIBUTING.md` | CI facts in `playbooks/regenerate-and-test` | confirm the Python matrix and the `just test` step |
| `.github/workflows/pypi-publish.yaml` | `playbooks/release` | re-read the triggers, the environment and the two publish steps |
| `https://slsa.dev/spec/v1.2/`, `https://arxiv.org/abs/2409.05014`, `https://openssf.org/technical-initiatives/software-supply-chain/` | the `references/` concepts | external authorities: cite on change |

These are not knowledge sources, and are left out on purpose:

- `docs/elements/` and `examples/output/` (git-ignored build output);
- `docs/templates-linkml/` and `docs/js/` (site theming);
- `examples/README.md`, `src/slsa/schema/README.md` and `tests/data/README.md` beyond the naming rule (short pages from the project template);
- `CODE_OF_CONDUCT.md`, `LICENSE` and the rest of `CONTRIBUTING.md` (governance text);
- `uv.lock`, `.gitignore`, `.pre-commit-config.yaml`, `.yamllint.yaml`, `.editorconfig`, `config.public.mk` and `.github/dependabot.yml` (tooling);
- `src/slsa/__init__.py`, `src/slsa/_version.py` and `tests/__init__.py` (package and test plumbing);
- `llms.txt` (the pointer that sends agents to this bundle);
- the `.lokf/` sidecar itself, including the `knowledge_bundle` link, `.github/workflows/knowledge-*.yaml` and `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md`.
