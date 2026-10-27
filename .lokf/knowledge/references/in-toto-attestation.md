---
type: Reference
id: https://w3id.org/lmodel/slsa/knowledge/references/in-toto-attestation
genre: reference
title: in-toto attestation framework
description: The in-toto attestation framework (spec v1), whose Statement, ResourceDescriptor and DigestSet layers carry SLSA provenance and verification summaries; the schema's InToto classes model them, with every digest algorithm the DigestSet page lists.
resource: https://github.com/in-toto/attestation/tree/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1
relatedTo:
  - https://w3id.org/lmodel/slsa/knowledge/references/slsa-specification
sources:
  - resource: src/slsa/schema/slsa_core.yaml
    title: the in-toto statement layer
  - resource: src/slsa/schema/spec/verification_summary.md
    title: the links to the in-toto pages at commit 7aefca3
  - resource: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/statement.md
    title: the Statement layer
  - resource: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md
    title: the ResourceDescriptor field type
  - resource: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/digest_set.md
    title: the DigestSet field type and its supported algorithms
generated:
  by: process:ktl-librarian
  at: "2026-10-27T12:57:54Z"
status: draft
---

# in-toto attestation framework

The in-toto attestation framework defines the layers of a software attestation. Its Statement page says that the Statement is the middle layer of an attestation: it binds the attestation to its subjects and names the type of its predicate. A ResourceDescriptor describes one software artifact or other resource, and a DigestSet maps algorithm names to the digests of one artifact.

The SLSA specification copy links these pages at commit `7aefca35a0f74a6e0cb397a8c4a76558f54de571` of the in-toto/attestation repository, for example in `verification_summary.md`.

## What the schema models

`slsa_core.yaml` models the statement layer in six classes:

- `InTotoStatement`: the statement, whose `statement_type` is always `https://in-toto.io/Statement/v1`.
- `InTotoStatementSubject`: one subject of a statement, which must carry a digest, as the Statement page requires.
- `InTotoResourceDescriptor`: a descriptor that carries at least one of a URI, a digest or its content, as the ResourceDescriptor page requires.
- `InTotoDigestSet`: the digests of one artifact. It names the 19 hash algorithms the DigestSet page lists, `dirHash` and the four git object types.
- `InTotoAdditionalDigest`: one digest under an algorithm the digest set does not name, such as a source control system's own revision type.
- `InTotoAnnotation`: one annotation on a descriptor.

The DigestSet page says that a consumer must accept only the algorithms it considers secure and ignore the rest, and that most applications should not accept `md5`.
