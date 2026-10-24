# slsa

A LinkML model of [SLSA](https://slsa.dev), Supply-chain Levels for Software
Artifacts: its tracks and levels, the roles and systems in a software supply
chain, and the in-toto attestations that carry build provenance and
verification summaries.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): what the model renders and where its elements come from
- [`slsa.yaml`](schema/slsa.yaml): the schema as the site serves it, and
  [`slsa_merged.yaml`](schema/slsa_merged.yaml): the same with no imports, for
  vendoring or loading offline

The schema is modular. `slsa_core` holds what every track shares; `slsa_build`,
`slsa_verification`, `slsa_source`, `slsa_dependency` and
`slsa_build_environment` each hold one track or predicate; `slsa_adoption`
holds the adoption study's themes; and `slsa.yaml` imports them all and adds
the document root. An importer may take one module.
