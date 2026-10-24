---
type: GlossaryTerm
id: https://w3id.org/lmodel/slsa/knowledge/glossary/slsa-track
genre: reference
title: SLSA track
description: A SLSA track focuses on one aspect of a software supply chain (Build, Source, Dependency or Build Environment), with its own levels, threats and requirements; the schema gives each track a subset and a level enum.
resource: src/slsa/schema/spec/tracks.md
sources:
  - resource: src/slsa/schema/spec/about.md
    title: the How SLSA works section
  - resource: src/slsa/schema/slsa_core.yaml
    title: the four track subsets
definedBy:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
generated:
  by: process:ktl-librarian
  at: "2026-10-23T22:17:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-21T22:14:46Z"
---

# SLSA track

The specification copy's `about.md` says that a SLSA track focuses on a particular aspect of a supply chain, such as the Build Track. `tracks.md` says that each track is composed of multiple levels, addresses different threats, and has its own set of requirements and patterns of use. It describes four tracks: Build, Source, Build Environment and Dependency.

The schema models the four tracks, each with a subset and a level enum: Build (`slsa_build_track`, `SlsaBuildLevel`), Source (`slsa_source_track`, `SlsaSourceLevel`), Dependency (`slsa_dependency_track`, `SlsaDependencyLevel`) and Build Environment (`slsa_build_environment_track`, `SlsaBuildEnvironmentLevel`). See [SLSA level](slsa-level.md).
