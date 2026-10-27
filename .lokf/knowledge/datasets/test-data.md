---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/test-data
genre: reference
title: Test data
description: Example YAML instances of the slsa schema in tests/data/, valid and invalid, named ClassName-###.yaml after the class they instantiate (InTotoStatement, SlsaBuildPlatform and the rest); pytest and linkml-run-examples check them.
resource: tests/data/
sources:
  - resource: tests/test_data.py
    title: the pytest data test
  - resource: tests/test_schema_rules.py
    title: the checks of rules the schema states twice
  - resource: justfile
    title: the _test-examples recipe
  - resource: CONTRIBUTING.md
    title: the naming rule for example data
dependsOn:
  - https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
generated:
  by: process:ktl-librarian
  at: "2026-10-27T12:57:54Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T20:08:09Z"
---

# Test data

`tests/data/README.md` says that each file is named `ClassName-###.yaml`, where the part before the first `-` is the name of a class as the schema writes it. The folder has three subfolders:

- `valid/`: data that conforms to the schema. It holds `InTotoStatement` files for each kind of predicate: build provenance, Tekton build provenance, verification summary, source provenance, source verification summaries for a git and an SVN revision, and a build environment attestation. It also holds files for `InTotoDigestSet`, `InTotoResourceDescriptor`, `SlsaDocument` and most of the `Slsa` classes a document holds.
- `invalid/`: data that must fail. The first line of each file says why it must fail. Examples are:
  - an `InTotoStatement` with no subject, a subject with no digest, the wrong statement type or a predicate of the wrong kind;
  - an `InTotoDigestSet` that is empty or whose SHA-256 digest is in uppercase hexadecimal;
  - an `InTotoResourceDescriptor` with no URI, digest or content;
  - a `SlsaBuildPlatform` with an unknown level;
  - a `SlsaVerificationSummary` with an unknown result or a policy with no URI.
- `problem/`: data the current schema does not handle correctly yet, split into `valid/` and `invalid/` (empty today).

`tests/test_data.py` loads every file in `valid/` with the generated dataclass model. `tests/test_schema_rules.py` checks rules the schema states in two places: the digest set's named algorithms against its at-least-one rule and its reserved names, and the `slsa_result_value` pattern against `SlsaResult`. `just test` also runs `linkml-run-examples` over `valid/` and `invalid/`, writing its output to the git-ignored `examples/output/`.
