---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artifacts
description: "Files generated from the slsa schema and never edited by hand, committed or git-ignored: the merged schema in docs/schema/, the Python data models, project/ (JSON Schema, OWL, SHACL, Java and more) and docs/elements/."
resource: project/
sources:
  - resource: justfile
    title: the gen-project, gen-python and gen-doc recipes
  - resource: .linkml/generators.yaml
    title: the gen-project generator settings
  - resource: src/slsa/datamodel/
    title: the generated Python data models
  - resource: docs/schema/slsa.yaml
    title: the merged schema
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-22T09:13:59Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T20:08:09Z"
---

# Generated artifacts

The `justfile` recipes generate these from `src/slsa/schema/slsa.yaml`:

- **`project/`**, by `just gen-project`: Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, prefix map, Protobuf, SHACL, ShEx, SQL schema and TypeScript. `.linkml/generators.yaml`, which `config.public.mk` names, sets the generator options and excludes the Markdown generator.
- **`src/slsa/datamodel/slsa.py` and `slsa_pydantic.py`**, by `just gen-project` or `just gen-python`: the dataclass and Pydantic models.
- **`docs/schema/slsa.yaml`**, by `just gen-doc` through its `_gen-yaml` step: the merged schema, written by `gen-yaml`.
- **`docs/elements/*.md`**, by `just gen-doc`: the per-element documentation pages, which `.gitignore` excludes.

The README marks `project/` as auto-generated and not to be edited.
