---
type: Playbook
id: https://w3id.org/lmodel/slsa/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test the schema
description: How to change the slsa schema and regenerate its artifacts and docs with just (gen-project, gen-doc), then run the tests CI runs (just test) on Python 3.9 to 3.13.
resource: justfile
sources:
  - resource: .github/workflows/main.yaml
    title: the CI test workflow
  - resource: CONTRIBUTING.md
    title: the contribution guide
references:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
  - https://w3id.org/lmodel/slsa/knowledge/datasets/generated-artefacts
  - https://w3id.org/lmodel/slsa/knowledge/datasets/test-data
generated:
  by: process:ktl-librarian
  at: "2026-10-22T18:46:59Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-21T22:14:46Z"
---

# Regenerate and test the schema

1. Install the dependencies with `just install`.
2. Edit `src/slsa/schema/slsa.yaml`, the only source file.
3. Run `just gen-project` to regenerate `project/` and the Python data models.
4. Run `just gen-doc` to regenerate `docs/schema/slsa.yaml` and `docs/elements/`, or `just testdoc` to build and serve the site.
5. Run `just test`. It runs three steps:
    - `_test-schema` runs `gen-project` into a scratch `tmp/` folder.
    - `_test-python` regenerates the Python models and runs pytest.
    - `_test-examples` runs `linkml-run-examples` over `tests/data/`.
6. Run `just lint` for the schema linter.
7. Commit the regenerated files with the schema change.

`.github/workflows/main.yaml` runs `just test` on every push to `main` and on every pull request, on Python 3.9, 3.10, 3.11, 3.12 and 3.13. On Python 3.13 it runs `just lint` first.
