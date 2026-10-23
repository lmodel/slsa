---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artifacts
description: "Files generated from the slsa schema and never edited by hand, committed or git-ignored: the two merged schemas in docs/schema/, the Python data models, project/ (JSON Schema, OWL, SHACL, Java and more), docs/elements/ and the bundle's domain schema .lokf/slsa.yaml."
resource: project/
sources:
  - resource: justfile
    title: the gen-project, gen-python and gen-doc recipes
  - resource: project.justfile
    title: the gen-merged and lokf-adapt recipes
  - resource: .linkml/generators.yaml
    title: the gen-project generator settings
  - resource: src/slsa/datamodel/
    title: the generated Python data models
  - resource: docs/schema/
    title: the merged schemas
  - resource: CONTRIBUTING.md
    title: the list of generated files
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:17:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T20:08:09Z"
---

# Generated artifacts

The recipes in `justfile` and `project.justfile` generate these from `src/slsa/schema/slsa.yaml` and the modules it imports:

- **`project/`**, by `just gen-project`: Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, prefix map, Protobuf, SHACL, ShEx, SQL schema and TypeScript. `.linkml/generators.yaml`, which `config.public.mk` names, sets the generator options and excludes the Markdown generator.
- **`src/slsa/datamodel/slsa.py` and `slsa_pydantic.py`**, by `just gen-project` or `just gen-python`: the dataclass and Pydantic models.
- **`docs/schema/slsa.yaml`**, by `just gen-doc` through its `_gen-yaml` step: the schema written by `gen-yaml`. `project.justfile` says that it holds the modules' elements folded in but keeps the `imports:` list, so a tool that loads it looks for the modules beside it.
- **`docs/schema/slsa_merged.yaml`**, by `just gen-merged`, run after `gen-doc`: the same schema with no imports, written by `gen-linkml --mergeimports`, for vendoring or loading offline.
- **`docs/elements/*.md`**, by `just gen-doc`: the per-element documentation pages, which `.gitignore` excludes.
- **`.lokf/slsa.yaml`**, by `just lokf-adapt`: the bundle's domain schema, which `lokf adapt` writes from the schema. See [slsa LinkML schema](slsa-linkml-schema.md).

The README marks `project/` as auto-generated and not to be edited. `CONTRIBUTING.md` names `project/`, `src/slsa/datamodel/`, `docs/schema/` and `.lokf/slsa.yaml` as generated.
