# slsa

A LinkML model of [SLSA](https://slsa.dev), Supply-chain Levels for Software
Artifacts: its tracks and levels, the roles and systems in a software supply
chain, and the in-toto attestations that carry build provenance and
verification summaries.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): what the model renders and where its elements come from
- [`slsa.yaml`](schema/slsa.yaml): the schema with its modules' elements folded in, and
  [`slsa_merged.yaml`](schema/slsa_merged.yaml): the same with no imports, for
  vendoring or loading offline

The schema is modular. `slsa_core` holds what every track shares; `slsa_build`,
`slsa_verification`, `slsa_source`, `slsa_dependency` and
`slsa_build_environment` each hold one track or predicate; `slsa_adoption`
holds the adoption study's themes; and `slsa.yaml` imports them all and adds
the document root. An importer may take one module.

## Validating data

`linkml-validate -s src/slsa/schema/slsa.yaml -C SlsaStatement statement.yaml`
checks a file against the JSON Schema generated from the schema. The models in
`src/slsa/datamodel/` check less. The dataclasses check required fields and enum
values but no patterns. The Pydantic models also check patterns and list
lengths, but they
leave out the rules written as `any_of` or `none_of`: that a resource
descriptor carries a URI, a digest or its content, that a digest set holds at
least one digest, and that an additional digest does not reuse an algorithm
the set names. Validate a file before loading it into either model.

Two rules have no check at all: that a list never repeats a name, such as two
build parameters called `ref`, and that a VSA lists at most one level per
track. Python's regular expressions also let a value end in one line break, so
`linkml-validate` accepts a digest followed by a newline.
