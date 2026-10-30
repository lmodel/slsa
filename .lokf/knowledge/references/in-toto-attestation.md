---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/in-toto-attestation
genre: reference
title: in-toto attestation framework
description: The in-toto attestation framework (spec v1), whose Statement, ResourceDescriptor and DigestSet layers carry SLSA provenance and verification summaries; the schema takes its InToto classes, InTotoPredicate and three field types from lmodel/in-toto's core module at v0.1.0, vendored unchanged in src/slsa/schema/in_toto/, with every digest algorithm the DigestSet page lists.
resource: https://github.com/in-toto/attestation/tree/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1
relatedTo:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
sources:
  - resource: src/slsa/schema/in_toto/in_toto_core.yaml
    id: in_toto_core.yaml
    title: lmodel/in-toto's core module as vendored, its classes, types, IRIs and links
  - resource: https://github.com/lmodel/in-toto/releases/tag/v0.1.0
    id: v0.1.0
    title: the lmodel/in-toto release the module was copied from
  - resource: NOTICE
    id: notice
    title: the lmodel/in-toto section
  - resource: tests/test_in_toto_import.py
    id: test_in_toto_import.py
    title: the git object hash the vendored module must have
  - resource: src/slsa/schema/spec/verification_summary.md
    id: verification_summary.md
    title: the links to the in-toto pages at commit 7aefca3
  - resource: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/statement.md
    id: statement.md
    title: the Statement layer
  - resource: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md
    id: resource_descriptor.md
    title: the ResourceDescriptor field type
  - resource: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/digest_set.md
    id: digest_set.md
    title: the DigestSet field type and its supported algorithms
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:13:40Z"
status: draft
---

# in-toto attestation framework

The in-toto attestation framework defines the layers of a software attestation. Its Statement page says that the Statement is the middle layer of an attestation: it binds the attestation to its subjects and names the type of its predicate.[^statement.md] A ResourceDescriptor describes one software artifact or other resource, and a DigestSet maps algorithm names to the digests of one artifact.

The SLSA specification copy links these pages at commit `7aefca35a0f74a6e0cb397a8c4a76558f54de571` of the in-toto/attestation repository, for example in `verification_summary.md`.[^verification_summary.md]

## The schema's copy

`NOTICE` says that `src/slsa/schema/in_toto/in_toto_core.yaml` is the core module of the in-toto Attestation Framework's LinkML schema from lmodel/in-toto at v0.1.0, under the Apache License 2.0, copied unchanged.[^notice][^v0.1.0] `tests/test_in_toto_import.py` pins the copy to that file by its git object hash, `3ffd841743df241e2948a2150caa8b03a024762f`.[^test_in_toto_import.py]

The module links the framework's pages at in-toto/attestation's tag `v1.2.0`, not at the commit the SLSA copy links. Its classes and their keys take in-toto's IRIs, under `https://w3id.org/lmodel/in-toto/`, except `media_type`, which is `dcat:mediaType`, and `algorithm`, which is `spdx:algorithm`.[^in_toto_core.yaml]

The module holds seven classes:

- `InTotoStatement`: the statement, whose `statement_type` is always `https://in-toto.io/Statement/v1`.
- `InTotoStatementSubject`: one subject of a statement, which must carry a digest, as the Statement page requires.[^statement.md]
- `InTotoResourceDescriptor`: a descriptor that carries at least one of a URI, a digest or its content, as the ResourceDescriptor page requires.[^resource_descriptor.md]
- `InTotoDigestSet`: the digests of one artifact. It names the 19 hash algorithms the DigestSet page lists, `dirHash` and the four git object types.[^digest_set.md]
- `InTotoAdditionalDigest`: one digest under an algorithm the digest set does not name, such as a source control system's own revision type.
- `InTotoAnnotation`: one annotation on a descriptor.
- `InTotoPredicate`: the abstract base of every predicate a statement can carry, whose `predicate_kind` names the concrete kind.

It also holds three field types. `in_toto_resource_uri` and `in_toto_type_uri` are URIs with their scheme and authority in lowercase, and `in_toto_timestamp` is a time in RFC 3339 format in UTC, written with a trailing Z.[^in_toto_core.yaml]

The DigestSet page says that a consumer must accept only the algorithms it considers secure and ignore the rest, and that most applications should not accept `md5`.

[slsa LinkML schema](../datasets/slsa-linkml-schema.md) says how the schema imports the module and what it builds on it.

[^statement.md]: <https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/statement.md>, the opening and `subject`
[^verification_summary.md]: src/slsa/schema/spec/verification_summary.md, its in-toto links
[^notice]: NOTICE, the lmodel/in-toto section
[^v0.1.0]: <https://github.com/lmodel/in-toto/releases/tag/v0.1.0>, the release
[^test_in_toto_import.py]: tests/test_in_toto_import.py, `PINNED_BLOB`
[^in_toto_core.yaml]: src/slsa/schema/in_toto/in_toto_core.yaml, `see_also`, `slot_uri` and `types`
[^resource_descriptor.md]: <https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md>, Fields
[^digest_set.md]: <https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/digest_set.md>, the algorithms and the consumer guidelines
