# Datasets

* [slsa LinkML schema](slsa-linkml-schema.md) - The LinkML schema for SLSA attestations and adoption metadata (schema id `https://w3id.org/lmodel/slsa`), covering the Build, Source, Dependency and Build Environment tracks, the in-toto Statement layer, and the SSF and adoption-study subsets; its `lokf adapt` copy in `.lokf/slsa.yaml` is the bundle's domain schema, with ten SLSA classes a concept may use as its type.
* [SLSA specification copy](slsa-spec-copy.md) - The SLSA specification's Markdown pages, images and provenance schemas (.proto, .cue) copied into `src/slsa/schema/spec/`; 38 of its 42 files match `docs/spec/draft/` at SLSA tag v1.2.
* [Generated artifacts](generated-artefacts.md) - Files generated from the slsa schema and never edited by hand, committed or git-ignored: the merged schema in docs/schema/, the Python data models, project/ (JSON Schema, OWL, SHACL, Java and more) and docs/elements/.
* [Test data](test-data.md) - Example YAML instances of the slsa schema in tests/data/, valid and invalid, named after the class they instantiate; pytest and linkml-run-examples check them.
