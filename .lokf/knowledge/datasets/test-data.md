---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/test-data
genre: reference
title: Test data
description: Example YAML instances of the slsa schema in tests/data/, valid and invalid, named after the class they instantiate; pytest and linkml-run-examples check them.
resource: tests/data/
sources:
  - resource: tests/test_data.py
    title: the pytest data test
  - resource: justfile
    title: the _test-examples recipe
dependsOn:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T20:08:09Z"
---

# Test data

`tests/data/README.md` says each file is named `classname-###.yaml`, where the part before the first `-` is a class of the schema. The folder has three subfolders:

- `valid/`: data that conforms to the schema, one or more files for `AdoptionMetadata`, `BuildDefinition`, `BuildProvenance`, `DependencyInventory`, `DigestSet`, `ResourceDescriptor`, `SourceProvenanceAttestation`, `SourceRevision` and `VerificationSummaryAttestation`;
- `invalid/`: data that must fail, for `BuildProvenance` and `VerificationSummaryAttestation` with required fields missing;
- `problem/`: data the current schema does not handle correctly yet, split into `valid/` and `invalid/` (empty today).

`tests/test_data.py` loads every file in `valid/` with the generated dataclass model. `just test` also runs `linkml-run-examples` over `valid/` and `invalid/`, writing its output to the git-ignored `examples/output/`.
