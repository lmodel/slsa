# Change Log

## 2026-10-27

* **Changed**: the documentation site follows `DOCS.exclude` and `REDIRECTS` in `website/site.config.mjs`, which replaced `MKDOCS` in 71dc33b; the schema files and the whitepaper under `docs/` are now linked on GitHub, not served by the site.
* **Changed**: the source map's documentation-site row checks `DOCS` and `REDIRECTS` and adds `website/scripts/routes.mjs`, since `MKDOCS` is gone from `website/site.config.mjs`.

## 2026-10-23

* **Changed**: the documentation site's list of page sources reads as a list.
* **Changed**: the documentation site is now the ktl-website Starlight site in `website/`, built by `knowledge-website.yaml`; the mkdocs workflows and `mkdocs.yml` are gone.
* **Changed**: the schema's HTML distribution names its pages at `schema/` on the documentation site, where `website/site.config.mjs` puts the schema's gen-doc pages.
* **Changed**: the site preview step names `npm run dev` in `website/`, since `just testdoc` needs mkdocs, which is no longer installed.
* **Changed**: the source map names `website/` and `knowledge-website.yaml` for the documentation site, in place of `mkdocs.yml` and the two mkdocs workflows.
* **Changed**: the adoption study concept quotes the title `docs/about.md` now cites, the arXiv record's current one (ab04158).
* **Resolved**: `docs/about.md` cites arXiv:2409.05014 by its current title since ab04158.
* **Changed**: the spec copy concept says that the upstream check lists no known differences, since 85c99e4 emptied `KNOWN_DIFFERENCES`.
* **Changed**: the source map's upstream-watch row also re-reads `KNOWN_DIFFERENCES`.
* **Prose**: reworded 10 concept bodies in plain English (generated-artefacts, license-and-attribution, openssf-supply-chain, secure-software-factory, slsa-adoption-study, slsa-level, slsa-linkml-schema, slsa-spec-copy, slsa-specification, test-data). No fact, link, number or frontmatter changed.
* **Rewrite**: the schema concept follows the modular schema at version 1.2.0: the umbrella and its seven modules, the prefixed class and enum names, and the nine `lokf adapt` roots and thirteen known types the README and `project.justfile` now give.
* **Rewrite**: the subsets explanation names the subsets as `slsa_core.yaml` now defines them, including the renamed `slsa_build_environment_track`, with their new descriptions.
* **Rewrite**: the specification copy now matches `docs/spec/draft/` at SLSA tag v1.2 file for file, as `NOTICE` says, since the three extra files were dropped and `build-requirements.md` restored.
* **Resolved**: the three files with no upstream match were removed and `build-requirements.md` restored in 57a4025; all 39 files now match SLSA tag v1.2 by git blob hash.
* **Rewrite**: the specification page follows the new `docs/about.md`, which names the tracks and predicates the schema renders, and the schema header, which now names v1.2.
* **Resolved**: the schema header gives `version: 1.2.0` and `source: https://slsa.dev/spec/v1.2` since 8695dc4, as `docs/about.md` does.
* **Rewrite**: the level term cites the track pages the specification copy now holds, since `levels.md` is gone, adds the Build Environment levels, and names the renamed enums.
* **Rewrite**: the track term cites `tracks.md` and `about.md`, since `levels.md` is gone from the specification copy, and names the renamed subsets and enums.
* **Rewrite**: the generated artifacts add `docs/schema/slsa_merged.yaml` from `just gen-merged` and `.lokf/slsa.yaml` from `just lokf-adapt`, which `project.justfile` and `CONTRIBUTING.md` now name.
* **Rewrite**: the test data follows the new example files, named after the prefixed classes, and the `ClassName-###.yaml` rule in `tests/data/README.md`.
* **Rewrite**: the regenerate playbook adds `just gen-merged` and `just lokf-adapt`, which `CONTRIBUTING.md` now asks for after a schema edit, and says the schema is a folder of modules.
* **Rewrite**: the attribution policy follows the README's shorter License section, which points to `NOTICE`; `NOTICE` now carries the specification's name, version and source, and says the copy is exact.
* **Rewrite**: the OpenSSF page now carries the working group's name and project list from openssf.org, since `docs/about.md` no longer describes the group, and names the two slots that point at its projects.
* **Rewrite**: the whitepaper page follows the new `docs/about.md`, which names five pipeline stages and the five snake_case slots the schema takes from the whitepaper.
* **Rewrite**: the adoption study takes its authors, numbers and titles from the arXiv record, and the module, enums and slots from the new `docs/about.md` and `slsa_adoption.yaml`.
* **Question**: the study's title in `docs/about.md` matches neither arXiv version.
* **Changed**: the documentation site names the two schema files the new home page links.
* **Changed**: the source map names the schema modules, `.linkmllint.yaml`, the `gen-merged` and `lokf-adapt` recipes, the specification pages that replace `levels.md`, and the openssf.org and arXiv records, and now counts `src/slsa/schema/README.md` as a source.
* **Prose**: reworded 2 concept bodies in plain English (regenerate-and-test, slsa-linkml-schema). No fact, link, number or frontmatter changed.
* **Changed**: the test playbook names the Python 3.10 to 3.14 matrix and the WSL2 `JUST_TEMPDIR` setting, from `main.yaml` and the `justfile` after the copier v0.5.0 update.
* **Changed**: the schema concept says its `lokf adapt` copy is the bundle's domain schema, which ten SLSA classes it adds as concept types and which keys it renames, from the README's KTL section.
* **Changed**: the source map adds the README's KTL section and `.copier-answers.yml` to its sources, and leaves out `src/README.md`, a short page from the project template.

## 2026-10-22

* **Changed**: the attribution policy's endorsement paragraph now says which claim the README makes and which `NOTICE` makes.
* **Prose**: reworded 2 concept bodies in plain English (license-and-attribution, release). No fact, link, number or frontmatter changed.
* **Added**: License and attribution, from the README's License and attribution section, `NOTICE` and `CONTRIBUTING.md`.
* **Rewrite**: the release playbook now follows `semantic-release.yml` and the reworked `pypi-publish.yaml`, which publishes `slsa-linkml` only when `PYPI_RELEASE_ENABLED` is `true`.
* **Changed**: the documentation site's preview runs only for pull requests from this repository's branches, as `test_pages_build.yaml` now says.
* **Changed**: the test playbook says CI also runs `just lint` on Python 3.13, as `main.yaml` now does.
* **Changed**: the specification copy names the weekly upstream watch, from `upstream-watch.yaml` and `scripts/check_upstream_release.py`.
* **Changed**: the source map adds the release, attribution and upstream-watch sources, and names the governance and lint files it leaves out.
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
