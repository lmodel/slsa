---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
genre: reference
title: slsa LinkML schema
description: "The modular LinkML schema of the SLSA specification v1.2 (schema id `https://w3id.org/lmodel/slsa`): `slsa.yaml` imports a core module and one module per track, predicate or study, covering the Build, Source, Dependency and Build Environment tracks; the core imports the in-toto statement layer from lmodel/in-toto's vendored core module and adds SlsaStatement; its `lokf adapt` copy in `.lokf/slsa.yaml` is the bundle's domain schema."
resource: src/slsa/schema/slsa.yaml
version: 1.2.0
license: Apache-2.0
distribution:
  - name: slsa.yaml
    access_url: https://github.com/lmodel/slsa/blob/main/src/slsa/schema/slsa.yaml
    media_type: application/yaml
  - name: Schema pages
    access_url: https://lmodel.github.io/slsa/schema/
    media_type: text/html
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
  - https://w3id.org/lmodel/slsa/knowledge/references/in-toto-attestation
  - https://w3id.org/lmodel/slsa/knowledge/references/secure-software-factory
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-adoption-study
relatedTo:
  - https://w3id.org/lmodel/slsa/knowledge/references/openssf-supply-chain
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:18:36Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T22:22:59Z"
sources:
  - resource: src/slsa/schema/slsa.yaml
    id: schema-slsa.yaml
    title: the umbrella schema, its header and SlsaDocument
  - resource: src/slsa/schema/README.md
    id: schema-readme.md
    title: the table of modules and the rule on module imports
  - resource: src/slsa/schema/slsa_core.yaml
    id: slsa_core.yaml
    title: the core module, SlsaStatement, SlsaPredicate and the six subsets
  - resource: src/slsa/schema/in_toto/in_toto_core.yaml
    id: in_toto_core.yaml
    title: lmodel/in-toto's core module as vendored
  - resource: NOTICE
    id: notice
    title: the lmodel/in-toto section
  - resource: src/slsa/schema/slsa_build.yaml
    id: slsa_build.yaml
    title: the Build track's provenance predicate and its typed fields
  - resource: src/slsa/schema/slsa_verification.yaml
    id: slsa_verification.yaml
    title: the Verification Summary Attestation predicate, time_verified and the slsa_result_value type
  - resource: src/slsa/schema/slsa_source.yaml
    id: slsa_source.yaml
    title: the Source track and authored_at
  - resource: src/slsa/schema/slsa_dependency.yaml
    title: the Dependency track
  - resource: src/slsa/schema/slsa_build_environment.yaml
    title: the Build Environment track
  - resource: src/slsa/schema/slsa_adoption.yaml
    title: the adoption study's themes
  - resource: docs/about.md
    id: docs-about.md
    title: the naming paragraph
  - resource: docs/index.md
    id: index.md
    title: the Validating data section
  - resource: .linkmllint.yaml
    title: the lint rule for permissible values
  - resource: project.justfile
    id: project.justfile
    title: the lokf-adapt recipes, their root classes and the LOKF_CMD note
  - resource: README.md
    id: readme.md
    title: the Mappings and Knowledge Trust Ladder (KTL) sections
---

# slsa LinkML schema

`src/slsa/schema/slsa.yaml` is the umbrella schema. Its header gives `version: 1.2.0` and `source: https://slsa.dev/spec/v1.2`, which [SLSA specification](../references/slsa-specification.md) explains. It declares the prefix `slsa:` as `https://w3id.org/lmodel/slsa/`, imports the seven `slsa_*` modules below, and adds only the tree root, `SlsaDocument`. That class holds attestations as `SlsaStatement`s, and the parties, platforms, packages, repositories and images they concern.[^schema-slsa.yaml]

## Modules

`src/slsa/schema/README.md` says that each `slsa_*` module imports the core and lints alone, and that no module imports the umbrella, so an importer can take one module.[^schema-readme.md]

- **`slsa_core.yaml`** holds what every track shares: `SlsaStatement` and `SlsaPredicate`, the roles, the build platform and its control plane, the package model, the `SlsaBuildLevel` enum and the six subsets. The roles are `SlsaParty` and its subclasses `SlsaProducer`, `SlsaConsumer`, `SlsaVerifier` and `SlsaInfrastructureProvider`. The module imports `linkml:types` and lmodel/in-toto's core module, `./in_toto/in_toto_core`.[^slsa_core.yaml]
- **`in_toto/in_toto_core.yaml`** is that core module, copied unchanged from lmodel/in-toto at v0.1.1.[^notice] It holds the in-toto statement layer: the six `InToto` classes, the abstract `InTotoPredicate` and three field types.[^in_toto_core.yaml] The README's table says that it imports only `linkml:types` and is never edited here, and that `tests/test_in_toto_import.py` pins it.[^schema-readme.md] [in-toto attestation framework](../references/in-toto-attestation.md) describes it.
- **`slsa_build.yaml`** holds the Build track's provenance predicate, `SlsaBuildProvenance`, with `SlsaBuildDefinition`, `SlsaRunDetails`, `SlsaBuildMetadata` and `SlsaBuildParameter`.
- **`slsa_verification.yaml`** holds the Verification Summary Attestation (VSA) predicate, `SlsaVerificationSummary`, with the classes for its policy, its input attestations and its dependency counts. It also holds the `SlsaResult` and `SlsaVerificationResult` enums and the `slsa_result_value` type.
- **`slsa_source.yaml`** holds the Source track: source control systems, repositories, revisions, branches and tags, and source provenance.
- **`slsa_dependency.yaml`** holds the Dependency track (working draft) and its `SlsaDependencyInventory`.
- **`slsa_build_environment.yaml`** holds the Build Environment track (working draft): `SlsaBuildImage`, its producer, its measurements and the build environment attestation. It also imports `slsa_build` for the image's provenance.
- **`slsa_adoption.yaml`** holds the adoption study's challenge and strategy themes on `SlsaAdoptionMetadata`.

Together, the modules hold 42 classes, 9 enums, 4 types and 6 subsets. The in-toto module holds 7 of the classes and 3 of the types.[^schema-slsa.yaml]

## On top of the in-toto layer

`SlsaStatement` extends `InTotoStatement` with `attestation_storage_uri`, `signing_tool` and `transparency_log_entry`, which the adoption study and the Secure Software Factory add and the in-toto specification does not define. A statement without them is a valid `SlsaStatement` too. `SlsaPredicate`, the abstract base of the schema's predicates, extends `InTotoPredicate` and takes its `predicate_kind`.[^slsa_core.yaml]

`build_type`, `builder_id` and `verifier_id` range over in-toto's `in_toto_type_uri`.[^slsa_build.yaml][^slsa_core.yaml] `started_on`, `finished_on` and `time_verified` range over `in_toto_timestamp`, so each ends in Z.[^slsa_build.yaml][^slsa_verification.yaml] `authored_at` on a source revision stays a `datetime`.[^slsa_source.yaml]

## Names and enums

`docs/about.md` says that element names carry a prefix (`SlsaStatement`, `SlsaPackage`, and `InTotoStatement` in the in-toto layer) so that they can be imported beside other vocabularies. It says that slots are snake_case, and that permissible values keep the strings SLSA defines, such as `SLSA_BUILD_LEVEL_3`. The in-toto layer's elements live under `in_toto_linkml:` (`https://w3id.org/lmodel/in-toto/`), except `media_type` and `algorithm`, which take the IRIs LOKF gives them. Every other element lives under `slsa:`.[^docs-about.md] `.linkmllint.yaml` makes UPPER_CASE permissible values the lint rule, because the SLSA-defined values are the strings that appear in attestations and policies.

`SlsaBuildLevel`, `SlsaSourceLevel`, `SlsaDependencyLevel` and `SlsaBuildEnvironmentLevel` name each track's [levels](../glossary/slsa-level.md). `SlsaResult` lists the verification results SLSA defines, and `SlsaVerificationResult` says whether a verification passed. A VSA's verified levels take the `slsa_result_value` type, which admits SLSA's results and an issuer's own. `SlsaReviewType` names the forms of review that may approve a revision. `SlsaAdoptionChallenge` and `SlsaAdoptionStrategy` encode the [adoption study](../references/slsa-adoption-study.md)'s themes.

The slsa modules tag their elements with subsets, which [Schema subsets](../explanations/schema-subsets.md) explains. The merged copies in `docs/schema/`, the Python data models, the `project/` artifacts and `.lokf/slsa.yaml` are generated from these files: see [Generated artifacts](generated-artefacts.md). The README says that the schema declares no mappings to other vocabularies.[^readme.md]

## As the bundle's domain schema

A domain schema adds a host's own classes and keys to the LOKF vocabulary. The README says that the bundle's domain schema is `.lokf/slsa.yaml`, a copy that `lokf adapt` wrote from `src/slsa/schema/slsa.yaml`. Edit the source, never the copy. `just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` fails when the copy is stale.[^readme.md]

`project.justfile` passes nine root classes to `lokf adapt`: `SlsaParty`, `SlsaBuildPlatform`, `SlsaControlPlane`, `SlsaPackage`, `SlsaPackageRegistry`, `SlsaSourceControlSystem`, `SlsaSourceRepository`, `SlsaSourceRevision` and `SlsaBuildImage`. A concept may name any of them, or a subclass, as its `type`. The README lists thirteen classes for Obsidian users of the KTL Registrar and KTL Curator plugins to add to the *Known LOKF types* setting. They are the eight roots other than `SlsaParty`, which the schema marks abstract, and the five subclasses of `SlsaParty`: `SlsaProducer`, `SlsaConsumer`, `SlsaVerifier`, `SlsaInfrastructureProvider` and `SlsaBuildImageProducer`.

`project.justfile` says that the recipes run the sidecar's own `lokf`, version 0.9.0 or later. Set `LOKF_CMD` to run another `lokf`, such as one in a checkout: `LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt`.[^project.justfile]

The README says that in the copy, LOKF's `id` stands in for each class's own identifier (`builder_id`, `repository_uri` and the like), so a concept writes `id`. Two slots are renamed, because LOKF 0.9.0 defines slots of the same names: `revision` is `slsa_revision`, with its IRI still `slsa:revision`, and a statement's `predicate` is `slsa_predicate`, with in-toto's IRI. A slsa document keeps both keys. Every other key keeps its name, because no other top-level class, slot, enum or type in the schema has a name that `lokf.yaml` defines. `lokf adapt` does not compare class attributes, so `media_type` keeps the name it shares with a LOKF slot, and takes that slot's IRI, `dcat:mediaType`.[^readme.md]

## Validating data

`docs/index.md` says that `linkml-validate -s src/slsa/schema/slsa.yaml -C SlsaStatement statement.yaml` checks a file against the JSON Schema generated from the schema, and that the generated models check less. The dataclasses check required fields and enum values but no patterns. The Pydantic models also check patterns and list lengths, but they leave out the rules written as `any_of` or `none_of`, such as the rule that a resource descriptor carries a URI, a digest or its content. The same page says that no tool checks that a list never repeats a name, or that a VSA lists at most one level per track.[^index.md]

[^schema-slsa.yaml]: src/slsa/schema/slsa.yaml and its imports, counted with SchemaView
[^schema-readme.md]: src/slsa/schema/README.md, the table and the line under it
[^slsa_core.yaml]: src/slsa/schema/slsa_core.yaml, `imports` and `classes`
[^notice]: NOTICE, the lmodel/in-toto section
[^in_toto_core.yaml]: src/slsa/schema/in_toto/in_toto_core.yaml, `types` and `classes`
[^slsa_build.yaml]: src/slsa/schema/slsa_build.yaml, `classes`
[^slsa_verification.yaml]: src/slsa/schema/slsa_verification.yaml, `time_verified`
[^slsa_source.yaml]: src/slsa/schema/slsa_source.yaml, `authored_at`
[^docs-about.md]: docs/about.md, the naming paragraph
[^readme.md]: README.md, the Mappings and Knowledge Trust Ladder (KTL) sections
[^project.justfile]: project.justfile, the knowledge bundle section
[^index.md]: docs/index.md, the Validating data section
