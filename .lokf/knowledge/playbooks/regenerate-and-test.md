---
type: Playbook
id: https://w3id.org/lmodel/slsa/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test the schema
description: How to change the slsa schema and its modules, regenerate the artifacts, the docs and the bundle's domain schema with just (gen-project, gen-doc, gen-merged, lokf-adapt), then run the tests CI runs (just test) on Python 3.10 to 3.14.
resource: justfile
sources:
  - resource: .github/workflows/main.yaml
    title: the CI test workflow
  - resource: CONTRIBUTING.md
    title: the contribution guide
  - resource: project.justfile
    title: the gen-merged and lokf-adapt recipes
  - resource: website/README.md
    title: how to preview the site
references:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
  - https://w3id.org/lmodel/slsa/knowledge/datasets/generated-artefacts
  - https://w3id.org/lmodel/slsa/knowledge/datasets/test-data
generated:
  by: process:ktl-librarian
  at: "2026-10-27T12:57:54Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-21T22:14:46Z"
---

# Regenerate and test the schema

1. Install the dependencies with `just install`. `CONTRIBUTING.md` asks for Python 3.10 or later, uv and just.
2. Edit the schema in `src/slsa/schema/`: `slsa.yaml` and the modules it imports.
3. Run `just gen-project` to regenerate `project/` and the Python data models. After you rename or remove a class, run `just clean` first: `gen-java` writes one file per class into `project/java/` and deletes none.
4. Run `just gen-doc` to regenerate `docs/schema/slsa.yaml` and `docs/elements/`. To see them on the site, run `npm run dev` in `website/`, as `website/README.md` says. Then run `just gen-merged` to regenerate `docs/schema/slsa_merged.yaml`.
5. Run `just lokf-adapt` to regenerate `.lokf/slsa.yaml`, the bundle's domain schema. Until `lokf adapt` is in a lokf release, run it from a lokf checkout, as [slsa LinkML schema](../datasets/slsa-linkml-schema.md) says.
6. Run `just test`. It runs three steps:
    - `_test-schema` runs `gen-project` into a scratch `tmp/` folder.
    - `_test-python` regenerates the Python models and runs pytest.
    - `_test-examples` runs `linkml-run-examples` over `tests/data/`.
7. Run `just lint`, which runs `linkml-lint` over the schema folder and reports errors only. `.linkmllint.yaml` sets its rules.
8. Commit the regenerated files with the schema change.

`.github/workflows/main.yaml` runs `just test` on every push to `main` and on every pull request, on Python 3.10, 3.11, 3.12, 3.13 and 3.14. On Python 3.13 it runs `just lint` first.

On WSL2 (Windows Subsystem for Linux), run `export JUST_TEMPDIR=/tmp` before any recipe. Without `JUST_TEMPDIR`, shebang recipes fail with "Permission denied" errors, so the justfile prints a warning when the variable is missing.
