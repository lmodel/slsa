---
type: Dataset
id: https://w3id.org/lmodel/slsa/knowledge/datasets/slsa-linkml-schema
genre: reference
title: slsa LinkML schema
description: The LinkML schema for SLSA attestations and adoption metadata (schema id `https://w3id.org/lmodel/slsa`), covering the Build, Source, Dependency and Build Environment tracks, the in-toto Statement layer, and the SSF and adoption-study subsets; its `lokf adapt` copy in `.lokf/slsa.yaml` is the bundle's domain schema, with ten SLSA classes a concept may use as its type.
resource: src/slsa/schema/slsa.yaml
version: 1.0.0
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
  at: "2026-10-23T20:08:09Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-22T18:46:59Z"
sources:
  - resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
---

# slsa LinkML schema

`src/slsa/schema/slsa.yaml` is the one schema file, and the only file to edit by hand. It declares the prefix `slsa:` as `https://w3id.org/lmodel/slsa/`, imports `linkml:types`, and holds 24 classes, 72 slots, 9 enums and 6 subsets.

## Classes

- **Attestation model.** `SlsaDocument` is the tree root, a wrapper for any SLSA attestation payload. `Statement` is the in-toto Statement v1 layer, and four predicates extend it: `BuildProvenance`, `VerificationSummaryAttestation`, `SourceProvenanceAttestation` and `BuildEnvironmentAttestation`. `DigestSet` and `ResourceDescriptor` describe artifacts.
- **Build provenance parts.** `BuildDefinition`, `RunDetails`, `Builder` and `BuildMetadata`.
- **Roles and platforms.** `Producer`, `Consumer`, `InfrastructureProvider`, `Verifier`, `BuildPlatform` and `ControlPlane`.
- **Source, dependencies and environment.** `Package`, `SourceRepository`, `SourceRevision`, `DependencyInventory` and `BuildImage`.
- **Adoption.** `AdoptionMetadata`.

## Enums

`BuildLevelEnum`, `SourceLevelEnum`, `DependencyLevelEnum` and `BuildEnvLevelEnum` name each track's levels. `SlsaResultEnum` and `VerificationResultEnum` carry verification results, and `ReviewTypeEnum` names kinds of code review. `AdoptionChallengeEnum` and `AdoptionStrategyEnum` encode the adoption study's themes.

## Subsets

Each element is tagged with the subsets it belongs to; [Schema subsets](../explanations/schema-subsets.md) explains them.

The merged copy in `docs/schema/slsa.yaml`, the Python data models and the `project/` artifacts are generated from this file: see [Generated artifacts](generated-artefacts.md).

## As the bundle's domain schema

A domain schema adds a host's own classes and keys to the LOKF vocabulary. The README says the bundle's domain schema is `.lokf/slsa.yaml`, a copy that `lokf adapt` wrote from `src/slsa/schema/slsa.yaml`. Edit the source schema, never the copy.

A concept may name one of ten SLSA classes as its `type`: `Producer`, `Consumer`, `InfrastructureProvider`, `Verifier`, `Builder`, `BuildPlatform`, `ControlPlane`, `BuildImage`, `Package` and `SourceRepository`. The README says to add the same ten classes to the *Known LOKF types* setting of two Knowledge Trust Ladder (KTL) plugins, KTL Registrar and KTL Curator, after the built-in types, so that both plugins keep the same list.

The copy renames the SLSA keys that LOKF also uses, to `slsa_id`, `slsa_name`, `slsa_description`, `slsa_version`, `slsa_author`, `slsa_timestamp` and `slsa_predicate`. `slsa_name` and `slsa_description` mean the same as LOKF's `title` and `description`. So a concept sets `title` and `description`, and leaves the two SLSA keys empty.
