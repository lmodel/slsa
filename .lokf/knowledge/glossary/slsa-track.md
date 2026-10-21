---
type: GlossaryTerm
id: https://w3id.org/lmodel/slsa/knowledge/glossary/slsa-track
genre: reference
title: SLSA track
description: A track groups SLSA levels that measure one aspect of supply chain security (Build, Source, Dependency or Build Environment), so progress on one aspect is recognised without blocking on another.
resource: src/slsa/schema/spec/levels.md
sources:
  - resource: src/slsa/schema/spec/tracks.md
    title: the tracks overview
definedBy:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
generated:
  by: process:ktl-librarian
  at: "2026-10-21T22:03:37Z"
status: draft
---

# SLSA track

The specification copy's `levels.md` says that SLSA levels are split into tracks. Each track has its own set of levels that measure a particular aspect of supply chain security. Tracks let the specification recognise progress in one aspect without blocking on an unrelated one, and let it add tracks without invalidating earlier levels.

The schema models four tracks, each with a subset and a level enum: Build (`BuildLevelEnum`), Source (`SourceLevelEnum`), Dependency (`DependencyLevelEnum`) and Build Environment (`BuildEnvLevelEnum`). See [SLSA level](slsa-level.md).
