---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
genre: reference
title: slsa LinkML schema
description: "The modular LinkML schema of the SLSA specification v1.2 (schema id `https://w3id.org/lmodel/slsa`): `slsa.yaml` imports a core module and one module per track, predicate or study, covering the Build, Source, Dependency and Build Environment tracks and the in-toto statement layer; its `lokf adapt` copy in `.lokf/slsa.yaml` is the bundle's domain schema."
resource: src/slsa/schema/slsa.yaml
version: 1.2.0
license: Apache-2.0
distribution:
  - name: slsa.yaml
    access_url: https://github.com/lmodel/slsa/blob/main/src/slsa/schema/slsa.yaml
    media_type: application/yaml
  - name: Documentation site
    access_url: https://lmodel.github.io/slsa
    media_type: text/html
derivedFrom:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
  - https://w3id.org/lmodel/slsa/knowledge/references/secure-software-factory
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-adoption-study
relatedTo:
  - https://w3id.org/lmodel/slsa/knowledge/references/openssf-supply-chain
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:17:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-23T22:22:59Z"
sources:
  - resource: src/slsa/schema/README.md
    title: the table of modules
  - resource: src/slsa/schema/slsa_core.yaml
    title: the core module and the six subsets
  - resource: src/slsa/schema/slsa_build.yaml
    title: the Build track's provenance predicate
  - resource: src/slsa/schema/slsa_verification.yaml
    title: the Verification Summary Attestation predicate
  - resource: src/slsa/schema/slsa_source.yaml
    title: the Source track
  - resource: src/slsa/schema/slsa_dependency.yaml
    title: the Dependency track
  - resource: src/slsa/schema/slsa_build_environment.yaml
    title: the Build Environment track
  - resource: src/slsa/schema/slsa_adoption.yaml
    title: the adoption study's themes
  - resource: docs/about.md
    title: the naming paragraph
  - resource: .linkmllint.yaml
    title: the lint rule for permissible values
  - resource: project.justfile
    title: the lokf-adapt recipes and their root classes
  - resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
---

# slsa LinkML schema

`src/slsa/schema/slsa.yaml` is the umbrella schema. Its header gives `version: 1.2.0` and `source: https://slsa.dev/spec/v1.2`, and a comment says that the version is the SLSA specification version the model renders. It declares the prefix `slsa:` as `https://w3id.org/lmodel/slsa/`, imports the seven modules below, and adds only the tree root, `SlsaDocument`. That class holds attestations and the parties, platforms, packages, repositories and images they concern.

## Modules

`src/slsa/schema/README.md` lists the modules. Each module imports the core and lints alone, and no module imports the umbrella, so an importer can take one module.

- **`slsa_core.yaml`** holds what every track shares. That is the in-toto statement layer (`InTotoStatement`, `InTotoResourceDescriptor`, `InTotoDigestSet` and `InTotoAnnotation`) and the roles (`SlsaParty` and its subclasses `SlsaProducer`, `SlsaConsumer`, `SlsaVerifier` and `SlsaInfrastructureProvider`). It is also the build platform and its control plane, the package model, the `SlsaBuildLevel` enum and the six subsets. It imports only `linkml:types`.
- **`slsa_build.yaml`** holds the Build track's provenance predicate, `SlsaBuildProvenance`, with `SlsaBuildDefinition`, `SlsaRunDetails`, `SlsaBuildMetadata` and `SlsaBuildParameter`.
- **`slsa_verification.yaml`** holds the Verification Summary Attestation predicate, `SlsaVerificationSummary`, and the `SlsaResult` and `SlsaVerificationResult` enums.
- **`slsa_source.yaml`** holds the Source track: source control systems, repositories, revisions, branches and tags, and source provenance.
- **`slsa_dependency.yaml`** holds the Dependency track (working draft) and its `SlsaDependencyInventory`.
- **`slsa_build_environment.yaml`** holds the Build Environment track (working draft): `SlsaBuildImage`, its producer, its measurements and the build environment attestation. It also imports `slsa_build` for the image's provenance.
- **`slsa_adoption.yaml`** holds the adoption study's challenge and strategy themes on `SlsaAdoptionMetadata`.

Together, the modules hold 36 classes, 9 enums and 6 subsets.

## Names

`docs/about.md` says that classes carry a prefix (`InTotoStatement`, `SlsaPackage`) so that they can be imported beside other vocabularies, that slots are snake_case, and that permissible values keep the strings SLSA defines, such as `SLSA_BUILD_LEVEL_3`. `.linkmllint.yaml` makes UPPER_CASE permissible values the lint rule, because the SLSA-defined values are the strings that appear in attestations and policies.

## Enums

`SlsaBuildLevel`, `SlsaSourceLevel`, `SlsaDependencyLevel` and `SlsaBuildEnvironmentLevel` name each track's levels. `SlsaResult` and `SlsaVerificationResult` carry verification results, and `SlsaReviewType` names the forms of review that may approve a revision. `SlsaAdoptionChallenge` and `SlsaAdoptionStrategy` encode the adoption study's themes.

## Subsets

Each element is tagged with the subsets it belongs to; [Schema subsets](../explanations/schema-subsets.md) explains them.

The merged copies in `docs/schema/`, the Python data models, the `project/` artifacts and `.lokf/slsa.yaml` are generated from these files: see [Generated artifacts](generated-artefacts.md).

## As the bundle's domain schema

A domain schema adds a host's own classes and keys to the LOKF vocabulary. The README says that the bundle's domain schema is `.lokf/slsa.yaml`, a copy that `lokf adapt` wrote from `src/slsa/schema/slsa.yaml`. Edit the source, never the copy. `just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` fails when the copy is stale.

`project.justfile` passes nine root classes to `lokf adapt`: `SlsaParty`, `SlsaBuildPlatform`, `SlsaControlPlane`, `SlsaPackage`, `SlsaPackageRegistry`, `SlsaSourceControlSystem`, `SlsaSourceRepository`, `SlsaSourceRevision` and `SlsaBuildImage`. A concept may name any of them, or a subclass, as its `type`. The README lists thirteen classes for Obsidian users of the KTL Registrar and KTL Curator plugins to add to the *Known LOKF types* setting: `SlsaProducer`, `SlsaConsumer`, `SlsaVerifier`, `SlsaInfrastructureProvider`, `SlsaBuildImageProducer`, `SlsaBuildPlatform`, `SlsaControlPlane`, `SlsaPackage`, `SlsaPackageRegistry`, `SlsaSourceControlSystem`, `SlsaSourceRepository`, `SlsaSourceRevision` and `SlsaBuildImage`. `SlsaParty`, which the schema marks abstract, is not in that list.

`project.justfile` says that `lokf adapt` is in lokf's main branch but not yet in a release. Until it is, set `LOKF_CMD` to run it from a lokf checkout, for example `LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt`.

The README says that in the copy, LOKF's `id` stands in for each class's own identifier (`builder_id`, `repository_uri` and the like), so a concept writes `id`. No SLSA key shares a name with a LOKF key, so none is renamed.
