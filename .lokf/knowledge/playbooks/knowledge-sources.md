---
type: Playbook
id: https://w3id.org/lmodel/slsa/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external URL this bundle derives concepts from, and how to re-verify each on a refresh run."
resource: https://github.com/lmodel/slsa
sources:
  - resource: README.md
  - resource: .copier-answers.yml
  - resource: NOTICE
  - resource: LICENSE
  - resource: pyproject.toml
  - resource: docs/
  - resource: src/slsa/schema/
  - resource: src/slsa/datamodel/
  - resource: project/
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: justfile
  - resource: project.justfile
  - resource: tests/
  - resource: website/
  - resource: .github/workflows/main.yaml
  - resource: .github/workflows/knowledge-website.yaml
  - resource: .github/workflows/knowledge-release.yaml
  - resource: .github/workflows/pypi-publish.yaml
  - resource: .github/workflows/semantic-release.yml
  - resource: .github/workflows/upstream-watch.yaml
  - resource: .releaserc.json
  - resource: .github/scripts/changelog-release.mjs
  - resource: scripts/check_upstream_release.py
  - resource: CONTRIBUTING.md
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:20:11Z"
status: draft
---

# Knowledge sources

Steady-state refresh runs re-verify these sources instead of discovering them again. Update this map whenever the repository's knowledge geography changes.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a URL, so re-read the external sources this table names on every refresh.

| Source | Yields | Re-check by |
|--------|--------|-------------|
| `README.md`, `pyproject.toml`, `.copier-answers.yml`, `docs/about.md` | bundle metadata, four of the five `references/` | diff the manifest name, description and authors; re-read each section of `docs/about.md` |
| `src/slsa/schema/slsa.yaml`, the seven `src/slsa/schema/slsa_*.yaml` modules, the vendored `src/slsa/schema/in_toto/in_toto_core.yaml`, `src/slsa/schema/README.md`, `.linkmllint.yaml`, the Validating data section of `docs/index.md` | `datasets/slsa-linkml-schema`, `explanations/schema-subsets`, the level enums in `glossary/slsa-level` | load `slsa.yaml` with SchemaView and recount classes, enums, types and subsets per module; re-read the header's `version`, `source`, `see_also` and comments, and the subset descriptions in `slsa_core.yaml` |
| `src/slsa/schema/spec/` | `datasets/slsa-spec-copy`, the two `glossary/` terms | re-read `index.md`'s version line; re-list the pages; re-read `about.md`, `tracks.md`, `build-track-basics.md`, `source-requirements.md`, `dependency-track.md` and `build-env-track-basics.md` |
| `docs/Secure_Software_Factory_Whitepaper.pdf` | `references/secure-software-factory` | confirm the file is still there |
| `justfile`, `project.justfile`, `.linkml/generators.yaml`, `project/`, `src/slsa/datamodel/`, `docs/schema/` | `datasets/generated-artefacts`, `playbooks/regenerate-and-test` | re-read the `gen-project`, `gen-python`, `gen-doc`, `gen-merged`, `lokf-adapt`, `lokf-adapt-check` and `test` recipe chains; re-list `project/*/`; re-read the `excludes` in `.linkml/generators.yaml` |
| `project.justfile`, the README's Knowledge Trust Ladder (KTL) and Mappings sections | the domain-schema and mappings sections of `datasets/slsa-linkml-schema` | re-read the `--root` classes, the known-types list, the `LOKF_CMD` note, the renamed and kept keys, and whether the schema declares mappings |
| the comment on the adapted schema copy check in `.github/workflows/main.yaml`, the Compare with the last released bundle and Pack the domain schema steps of `.github/workflows/knowledge-release.yaml` | the release's schema asset in `datasets/generated-artefacts` | re-read the asset's name, its checksum file, what the comparison reads and which releases get it |
| `tests/data/`, `tests/test_data.py`, `tests/test_schema_rules.py` | `datasets/test-data` | re-list and count the files in `tests/data/valid/` and `tests/data/invalid/`; re-read the naming rule and the two tests |
| `website/site.config.mjs`, `website/scripts/routes.mjs`, `website/README.md`, `docs/index.md`, `.github/workflows/knowledge-website.yaml` | `services/documentation-site` | confirm the triggers and the deploy switch, the `DOCS`, `REDIRECTS` and `HOME` settings, and where a link to a file under `docs/` that is no page goes |
| `.github/workflows/main.yaml`, `CONTRIBUTING.md` | CI facts in `playbooks/regenerate-and-test` | confirm the Python matrix, the `just test`, `just lint` and `just lokf-adapt-check` steps and the regeneration steps |
| `.github/workflows/pypi-publish.yaml`, `.github/workflows/semantic-release.yml`, `.releaserc.json`, `.github/scripts/changelog-release.mjs`, the Releasing section of `CONTRIBUTING.md` | `playbooks/release` | re-read the triggers, the environments, the repository variables and the release rules |
| `README.md` (License section), `NOTICE`, `LICENSE`, the License section of `CONTRIBUTING.md` | `policies/license-and-attribution` | re-read each third-party entry in `NOTICE` and the README's License section |
| `.github/workflows/upstream-watch.yaml`, `scripts/check_upstream_release.py` | the upstream watch in `datasets/slsa-spec-copy` | re-read the schedule, `PINNED_TAG` and `KNOWN_DIFFERENCES` |
| `https://github.com/slsa-framework/slsa` (README, `LICENSE.md`, tag `v1.2`) | `org/slsa-project`, the license in `references/slsa-specification`, the upstream section of `datasets/slsa-spec-copy` | re-read the Governance and License sections; compare `git hash-object` of each copied file with the tree at the tag in use; watch for a release after v1.2 |
| `https://github.com/cncf/tag-security` (`LICENSE.md`, the whitepaper's folder) | `org/cncf-tag-security`, the upstream section of `references/secure-software-factory` | re-read the license; compare the PDF's blob hash |
| `https://openssf.org/technical-initiatives/software-supply-chain/` | `references/openssf-supply-chain` | re-read the working group's name and the project list |
| `https://arxiv.org/abs/2409.05014` | `references/slsa-adoption-study` | re-read the title, the authors and the abstract's numbers |
| `https://slsa.dev/spec/v1.2/` | `references/slsa-specification` | external authority: cite on change |
| `https://github.com/in-toto/attestation` (`spec/v1/` at commit `7aefca35a0f74a6e0cb397a8c4a76558f54de571`) | `references/in-toto-attestation` | re-read `statement.md`, `resource_descriptor.md` and `digest_set.md` at the commit the specification copy links to; when a newer SLSA release links another commit, compare the supported algorithms and the MUST rules |
| `src/slsa/schema/in_toto/in_toto_core.yaml`, `tests/test_in_toto_import.py`, the lmodel/in-toto section of `NOTICE`, `https://github.com/lmodel/in-toto/releases/tag/v0.1.0` | `references/in-toto-attestation`, the in-toto module in `datasets/slsa-linkml-schema`, the vendored-module step of `playbooks/regenerate-and-test` | compare `git hash-object` of the vendored file with the hash the test pins and with the file at the release tag; when the test pins a later release, re-read the module's classes, types and IRIs |

These are not knowledge sources, and are left out on purpose:

- `docs/elements/` and `examples/output/` (git-ignored build output);
- `docs/templates-linkml/` and `docs/js/` (site theming);
- `examples/README.md`, `src/README.md` and `tests/data/README.md` beyond the naming rule (short pages from the project template);
- `CODE_OF_CONDUCT.md`, `AI_COVENANT.md`, `SECURITY.md`, `CHANGELOG.md`, the rest of `CONTRIBUTING.md` and the issue and pull request templates (governance text);
- `uv.lock`, `.gitignore`, `.pre-commit-config.yaml`, `.yamllint.yaml`, `.editorconfig`, `config.public.mk`, `.github/dependabot.yml`, `.github/workflows/lint-and-docs.yaml`, `.markdownlint-cli2.jsonc`, `lychee.toml` and `.github/scripts/report-issue.sh` (tooling);
- `src/slsa/__init__.py`, `src/slsa/_version.py` and `tests/__init__.py` (package and test plumbing);
- `llms.txt` (the pointer that sends agents to this bundle);
- the `.lokf/` sidecar itself, including the `knowledge_bundle` link, `.github/workflows/knowledge-*.yaml` beyond `knowledge-website.yaml` and the comparison and domain-schema steps of `knowledge-release.yaml`, and `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md`.
