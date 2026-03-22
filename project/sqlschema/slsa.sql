-- # Class: SlsaDocument Description: Root wrapper for any SLSA attestation payload. Acts as the entry point for schema validation and tools.
--     * Slot: id
--     * Slot: verificationResult Description: Whether the artifact passed or failed policy verification.
--     * Slot: buildDefinition_id Description: All inputs to the build, sufficient to initialise and reproduce it. REQUIRED at SLSA Build L1.
--     * Slot: runDetails_id Description: Details specific to this particular execution of the build, including builder identity and metadata. REQUIRED at SLSA Build L1.
--     * Slot: verifier_uid Description: Identifies the entity that performed the verification.
--     * Slot: adoptionMetadata_id Description: Optional structured metadata recording the SLSA adoption challenges and mitigation strategies relevant to this attestation context. Derived from empirical analysis of SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Intended for use by framework authors, practitioners, and tooling that tracks adoption progress alongside attestation payloads.
-- # Class: DigestSet Description: A set of cryptographic digests for an artifact, keyed by algorithm name (e.g., "sha256", "gitCommit"). Provides enough information for consumers to verify artifact integrity using their preferred algorithm.
--     * Slot: id
--     * Slot: sha256 Description: Lowercase hex-encoded SHA-256 digest of the artifact.
--     * Slot: sha512 Description: Lowercase hex-encoded SHA-512 digest of the artifact.
--     * Slot: gitCommit Description: Git commit SHA identifying a source-backed artifact.
-- # Class: ResourceDescriptor Description: A reference to a software artifact including its location, digest, and optional metadata. Used throughout SLSA to describe inputs, outputs, and dependencies in provenance attestations.
--     * Slot: id
--     * Slot: uri Description: A URI uniquely identifying a resource, such as a package URL (purl), git repository URL, or OCI image reference.
--     * Slot: name Description: A local name for a resource within the context of an attestation, or the name of a package, producer, or party.
--     * Slot: downloadLocation Description: URI from which a resource can be downloaded, if different from its identifying URI.
--     * Slot: mediaType Description: IANA media type of a resource's content (e.g., "application/octet-stream", "application/vnd.oci.image.manifest.v1+json").
--     * Slot: Statement_id Description: Autocreated FK slot
--     * Slot: BuildProvenance_id Description: Autocreated FK slot
--     * Slot: BuildDefinition_id Description: Autocreated FK slot
--     * Slot: RunDetails_id Description: Autocreated FK slot
--     * Slot: Builder_uid Description: Autocreated FK slot
--     * Slot: VerificationSummaryAttestation_id Description: Autocreated FK slot
--     * Slot: SourceProvenanceAttestation_id Description: Autocreated FK slot
--     * Slot: DependencyInventory_id Description: Autocreated FK slot
--     * Slot: BuildEnvironmentAttestation_id Description: Autocreated FK slot
--     * Slot: digest_id Description: Set of cryptographic digests of a resource's content used for integrity verification.
-- # Abstract Class: Statement Description: The middle layer of an in-toto software attestation (Statement v1). Binds an authenticated predicate to one or more subject artifacts, allowing predicate-agnostic processing and storage.
--     * Slot: id
--     * Slot: _type Description: Always "https://in-toto.io/Statement/v1". Identifies the in-toto statement schema version and namespace.
--     * Slot: predicateType Description: URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).
--     * Slot: predicate Description: The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.
--     * Slot: attestationStorageUri Description: URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).
--     * Slot: signingTool Description: URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., "https://github.com/sigstore/cosign", "https://github.com/notaryproject/notation"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.
--     * Slot: sigstoreLogEntry Description: URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., "https://rekor.sigstore.dev/api/v1/log/entries/24296fb..."). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.
-- # Class: BuildProvenance Description: An attestation predicate (predicateType "https://slsa.dev/provenance/v1") that describes how a set of output artifacts was produced by a build platform. Consumers use this to verify artifact authenticity and trace artifacts back through the supply chain.
--     * Slot: id
--     * Slot: _type Description: Always "https://in-toto.io/Statement/v1". Identifies the in-toto statement schema version and namespace.
--     * Slot: predicateType Description: URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).
--     * Slot: predicate Description: The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.
--     * Slot: attestationStorageUri Description: URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).
--     * Slot: signingTool Description: URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., "https://github.com/sigstore/cosign", "https://github.com/notaryproject/notation"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.
--     * Slot: sigstoreLogEntry Description: URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., "https://rekor.sigstore.dev/api/v1/log/entries/24296fb..."). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.
--     * Slot: buildDefinition_id Description: All inputs to the build, sufficient to initialise and reproduce it. REQUIRED at SLSA Build L1.
--     * Slot: runDetails_id Description: Details specific to this particular execution of the build, including builder identity and metadata. REQUIRED at SLSA Build L1.
-- # Class: BuildDefinition Description: Describes all inputs to the build in enough detail to initialise and reproduce the build. The accuracy and completeness are implied by the builder identified in runDetails.
--     * Slot: id
--     * Slot: buildType Description: URI identifying the template for how to perform the build and how to interpret the parameters and dependencies. SHOULD resolve to a human-readable specification. REQUIRED at SLSA Build L1.
--     * Slot: externalParameters Description: Top-level, independent inputs under external (tenant or user) control. MUST be complete at SLSA Build L3. Stored as a JSON object. Verifiers SHOULD reject unrecognized fields.
--     * Slot: internalParameters Description: Parameters set internally by the build platform. Intended for debugging, incident response, and enabling reproducible builds. Stored as a JSON object; need not be verified by consumers.
--     * Slot: hermeticBuild Description: Whether all build inputs are fully isolated to the dependencies declared in resolvedDependencies, with no network access or filesystem references outside the explicit build graph. Hermetic builds are a stated requirement for SLSA Build L3; practitioners identified this as one of the most commonly cited implementation barriers, with over 50% of surveyed practitioners finding hermetic build requirements difficult to implement (Tamanna et al., 2024, CI.1).
--     * Slot: provenanceGenerationTool Description: URI or name of the tool used to generate provenance for this build (e.g., "https://github.com/slsa-framework/slsa-github-generator"). Standardizing this field across builds reduces confusion, supports reproducibility verification, and aligns with the recommended strategy of simplifying and standardizing provenance generation processes (Tamanna et al., 2024, S3.1).
--     * Slot: pipelineOrchestrator Description: URI or name of the CI/CD pipeline orchestration system that coordinated this build (e.g., "https://tekton.dev", "https://github.com/features/actions", "https://jenkins.io"). In the SSF reference architecture this is the Build Service layer that feeds the Artifact Registry. Providing this field helps distinguish the orchestrator from the provenance-generating builder identity (builder.id) in complex deployments where they differ (e.g., a Tekton Pipeline running on Google Cloud Pipelines).
-- # Class: RunDetails Description: Details specific to this particular execution of the build, including the trusted builder and optional run-level metadata.
--     * Slot: id
--     * Slot: builder_uid Description: Identifies the build platform that executed the build and is trusted to have correctly generated this provenance. REQUIRED at SLSA Build L1.
--     * Slot: buildMetadata_id Description: Metadata about this particular build execution.
-- # Class: Builder Description: Represents the transitive closure of all software, hardware, and entities trusted to faithfully execute the build and record provenance. The builder.id is the primary basis for determining SLSA Build Level.
--     * Slot: uid
--     * Slot: id Description: A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers.
--     * Slot: version Description: Map of component names to their version strings, represented as a JSON object (string → string).
--     * Slot: versionTag Description: A semantic version tag (e.g., "v1.2.3") assigned to the builder or the produced artifact at the time of the build. Practitioners recommended implementing versioning tagging early in SLSA framework deployment to facilitate progress tracking, reduce maintenance confusion from breaking changes, and enable more straightforward verification (Tamanna et al., 2024, S4.2).
-- # Class: BuildMetadata Description: Metadata about a specific invocation of the build, including timing information and a unique build identifier for log correlation.
--     * Slot: id
--     * Slot: invocationId Description: A globally unique identifier for a build invocation, useful for finding associated logs. Format defined by builder.id; treated as opaque and case-sensitive. The value SHOULD be globally unique.
--     * Slot: startedOn Description: Timestamp (RFC 3339) of when the build started.
--     * Slot: finishedOn Description: Timestamp (RFC 3339) of when the build completed.
-- # Class: VerificationSummaryAttestation Description: An attestation predicate (predicateType "https://slsa.dev/verification_summary/v1") issued by a trusted verifier stating that one or more artifacts were evaluated against a policy and the SLSA level at which they were verified. Allows consumers to trust the verifier's determination without needing access to all underlying provenance.
--     * Slot: id
--     * Slot: timeVerified Description: Timestamp (RFC 3339) indicating when the verification occurred.
--     * Slot: resourceUri Description: URI identifying the resource associated with the artifact being verified. SHOULD be the URI from which the consumer fetches the artifact.
--     * Slot: verificationResult Description: Whether the artifact passed or failed policy verification.
--     * Slot: dependencyLevels Description: Map from SlsaResult to count of transitive dependencies verified at that level (JSON object string). Allows policy engines to enforce minimum levels on the full dependency graph.
--     * Slot: slsaVersion Description: Version of the SLSA specification used during verification, in MAJOR.MINOR format (e.g., "1.0").
--     * Slot: _type Description: Always "https://in-toto.io/Statement/v1". Identifies the in-toto statement schema version and namespace.
--     * Slot: predicateType Description: URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).
--     * Slot: predicate Description: The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.
--     * Slot: attestationStorageUri Description: URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).
--     * Slot: signingTool Description: URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., "https://github.com/sigstore/cosign", "https://github.com/notaryproject/notation"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.
--     * Slot: sigstoreLogEntry Description: URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., "https://rekor.sigstore.dev/api/v1/log/entries/24296fb..."). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.
--     * Slot: verifier_uid Description: Identifies the entity that performed the verification.
--     * Slot: policy_id Description: The policy the subject was verified against. MUST contain a URI; SHOULD contain a digest identifying the exact policy version.
-- # Class: Verifier Description: The entity that performed verification of an artifact and issued a Verification Summary Attestation. Consumers MUST accept only specific (signer, verifier) pairs.
--     * Slot: uid
--     * Slot: id Description: A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers.
--     * Slot: version Description: Map of component names to their version strings, represented as a JSON object (string → string).
-- # Class: Producer Description: A party who creates software and provides it to others. Responsible for choosing an appropriate build platform, following a consistent build process, and distributing provenance to consumers.
--     * Slot: id
--     * Slot: name Description: A local name for a resource within the context of an attestation, or the name of a package, producer, or party.
--     * Slot: buildPlatformId Description: URI of the build platform chosen to produce artifacts.
-- # Class: Consumer Description: A party who uses software provided by a producer. May verify provenance directly or delegate that responsibility to a separate verifier.
--     * Slot: id
-- # Class: InfrastructureProvider Description: A party who provides software or services to other roles in the supply chain, such as a package registry maintainer or build platform operator.
--     * Slot: id
-- # Class: BuildPlatform Description: The infrastructure (software, hardware, people, and organizations) used to transform source code into package artifacts. Responsible for provenance generation and isolation between tenant builds. Often a hosted, multi-tenant build service.
--     * Slot: uid
--     * Slot: id Description: A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers.
--     * Slot: buildLevel Description: The SLSA Build Level this platform is capable of producing, as determined by its provenance generation and isolation guarantees.
--     * Slot: isHosted Description: True if this is a hosted (multi-tenant) platform running on shared or dedicated infrastructure, rather than an individual's workstation. Required for SLSA Build L2+.
-- # Class: ControlPlane Description: The build platform component that orchestrates each independent build execution and generates provenance. Managed by an admin and trusted to be outside of tenant control. Responsible for generating and signing provenance at SLSA Build L2+.
--     * Slot: id
-- # Class: Package Description: An identifiable unit of software intended for distribution. In the SLSA model, a package is always the output of a build process (which may be a no-op). The package name is the primary security boundary within a package ecosystem.
--     * Slot: id
--     * Slot: name Description: A local name for a resource within the context of an attestation, or the name of a package, producer, or party.
--     * Slot: ecosystem Description: The package ecosystem (e.g., "PyPA", "npm", "OCI", "cargo") governing distribution conventions for this package.
--     * Slot: registry Description: URI of the package registry where a package is published and from which consumers resolve the package name to an artifact.
--     * Slot: artifact_id Description: A specific immutable package artifact or the artifact whose dependency inventory is recorded.
-- # Class: SourceRepository Description: A self-contained unit that holds the content and complete revision history for a set of files, along with metadata such as branches and tags. Hosted and governed by a Source Control System.
--     * Slot: uid
--     * Slot: id Description: Canonical URI that uniquely identifies this source repository.
--     * Slot: description Description: Human-readable description of a repository's purpose or a resource.
--     * Slot: sourceLevel Description: The SLSA Source Level achieved or verified for a source repository or revision.
-- # Class: SourceRevision Description: A specific, logically immutable snapshot of a source repository's tracked files. Uniquely identified by a revision identifier such as a cryptographic hash (e.g., git commit SHA) or a path-qualified sequential number (e.g., SVN).
--     * Slot: id
--     * Slot: revisionId Description: Immutable identifier for a source revision (e.g., git commit SHA, path-qualified sequential number).
--     * Slot: author Description: Identity of the person or automation that authored this revision (e.g., an email address or platform username).
--     * Slot: timestamp Description: Timestamp (RFC 3339) of when this source revision was created.
--     * Slot: reviewType Description: The type of human or automated review process used to approve this source revision. Captures the contested forms of two-party review — including pair programming and mob programming — whose security equivalence to standard asynchronous two-party review is an open question identified in practitioner community discussions (Tamanna et al., 2024, LF.2). See ReviewTypeEnum for defined values.
--     * Slot: repository_uid Description: The source repository that contains this revision.
-- # Class: SourceProvenanceAttestation Description: An attestation describing how a source revision came to exist: where it was hosted, when it was generated, what process was used, who the contributors were, and which technical controls were enforced by the Source Control System.
--     * Slot: id
--     * Slot: sourceLevel Description: The SLSA Source Level achieved or verified for a source repository or revision.
--     * Slot: _type Description: Always "https://in-toto.io/Statement/v1". Identifies the in-toto statement schema version and namespace.
--     * Slot: predicateType Description: URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).
--     * Slot: predicate Description: The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.
--     * Slot: attestationStorageUri Description: URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).
--     * Slot: signingTool Description: URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., "https://github.com/sigstore/cosign", "https://github.com/notaryproject/notation"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.
--     * Slot: sigstoreLogEntry Description: URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., "https://rekor.sigstore.dev/api/v1/log/entries/24296fb..."). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.
--     * Slot: revision_id Description: The source revision that this attestation describes.
-- # Class: DependencyInventory Description: A comprehensive inventory of all third-party build dependencies for an artifact, capturing direct and transitive dependencies. Supports vulnerability management and incident response.
--     * Slot: id
--     * Slot: dependencyLevel Description: The SLSA Dependency Level that this inventory and associated triage process supports.
--     * Slot: artifact_id Description: A specific immutable package artifact or the artifact whose dependency inventory is recorded.
-- # Class: BuildImage Description: The template for a build environment, such as a VM or container image. Comprises the root filesystem, pre-installed guest OS and packages, the build executor, and the build agent. Created by a build image producer and consumed by the hosted build platform.
--     * Slot: uid
--     * Slot: id Description: URI uniquely identifying this build image version (e.g., an OCI image reference with digest).
--     * Slot: buildEnvLevel Description: The SLSA Build Environment Level supported or represented, reflecting the strength of the integrity guarantees provided.
--     * Slot: provenance_id Description: SLSA Build Provenance for a build image, describing how the image itself was produced. Required for SLSA Build Environment L1+.
-- # Class: BuildEnvironmentAttestation Description: An attestation describing the integrity of a build environment at the time a specific build was dispatched and executed. Used to verify that a build ran in the expected, untampered environment.
--     * Slot: id
--     * Slot: buildId Description: An immutable identifier uniquely assigned to a build execution (e.g., a UUID). Links a BuildEnvironmentAttestation to the corresponding build provenance.
--     * Slot: buildEnvLevel Description: The SLSA Build Environment Level supported or represented, reflecting the strength of the integrity guarantees provided.
--     * Slot: _type Description: Always "https://in-toto.io/Statement/v1". Identifies the in-toto statement schema version and namespace.
--     * Slot: predicateType Description: URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).
--     * Slot: predicate Description: The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.
--     * Slot: attestationStorageUri Description: URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).
--     * Slot: signingTool Description: URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., "https://github.com/sigstore/cosign", "https://github.com/notaryproject/notation"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.
--     * Slot: sigstoreLogEntry Description: URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., "https://rekor.sigstore.dev/api/v1/log/entries/24296fb..."). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.
--     * Slot: buildImage_uid Description: The build image from which the build environment was instantiated.
-- # Class: AdoptionMetadata Description: Optional structured metadata capturing the SLSA adoption challenges and mitigation strategies relevant to a given attestation or deployment context. Derived from empirical analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Use this class to document which challenge themes apply to the current deployment and which strategies are being employed or recommended. Attach via the adoptionMetadata slot on SlsaDocument.
--     * Slot: id
-- # Class: SlsaDocument_verifiedLevels
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
--     * Slot: verifiedLevels Description: The highest verified SLSA level for each applicable track (not including transitive dependencies). At most one level per track. Implies all levels below it within the same track.
-- # Class: ResourceDescriptor_annotations
--     * Slot: ResourceDescriptor_id Description: Autocreated FK slot
--     * Slot: annotations Description: Arbitrary vendor-specific key-value annotations.
-- # Class: VerificationSummaryAttestation_verifiedLevels
--     * Slot: VerificationSummaryAttestation_id Description: Autocreated FK slot
--     * Slot: verifiedLevels Description: The highest verified SLSA level for each applicable track (not including transitive dependencies). At most one level per track. Implies all levels below it within the same track.
-- # Class: SourceRevision_parentRevisions
--     * Slot: SourceRevision_id Description: Autocreated FK slot
--     * Slot: parentRevisions Description: Revision IDs of the parent revision(s), forming the directed acyclic graph of change history.
-- # Class: SourceProvenanceAttestation_controlsEnforced
--     * Slot: SourceProvenanceAttestation_id Description: Autocreated FK slot
--     * Slot: controlsEnforced Description: Technical controls actively enforced by the Source Control System when this revision was created (e.g., "two-party review", "branch protection", "status checks").
-- # Class: BuildEnvironmentAttestation_measurements
--     * Slot: BuildEnvironmentAttestation_id Description: Autocreated FK slot
--     * Slot: measurements Description: Cryptographic measurements (hashes) of build environment components captured during boot and initialization, used to verify integrity against known-good reference values.
-- # Class: AdoptionMetadata_challenges
--     * Slot: AdoptionMetadata_id Description: Autocreated FK slot
--     * Slot: challenges Description: The adoption challenge themes that apply to this attestation or deployment context, drawn from the empirically identified challenge taxonomy (Tamanna et al., 2024, arXiv:2409.05014).
-- # Class: AdoptionMetadata_strategies
--     * Slot: AdoptionMetadata_id Description: Autocreated FK slot
--     * Slot: strategies Description: The mitigation strategies being employed or recommended in this attestation or deployment context, drawn from the empirically identified strategy taxonomy (Tamanna et al., 2024, arXiv:2409.05014).

CREATE TABLE "DigestSet" (
	id INTEGER NOT NULL,
	sha256 TEXT,
	sha512 TEXT,
	"gitCommit" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DigestSet_id" ON "DigestSet" (id);

CREATE TABLE "ResourceDescriptor" (
	id INTEGER NOT NULL,
	uri TEXT,
	name TEXT,
	"downloadLocation" TEXT,
	"mediaType" TEXT,
	"Statement_id" INTEGER,
	"BuildProvenance_id" INTEGER,
	"BuildDefinition_id" INTEGER,
	"RunDetails_id" INTEGER,
	"Builder_uid" INTEGER,
	"VerificationSummaryAttestation_id" INTEGER,
	"SourceProvenanceAttestation_id" INTEGER,
	"DependencyInventory_id" INTEGER,
	"BuildEnvironmentAttestation_id" INTEGER,
	digest_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Statement_id") REFERENCES "Statement" (id),
	FOREIGN KEY("BuildProvenance_id") REFERENCES "BuildProvenance" (id),
	FOREIGN KEY("BuildDefinition_id") REFERENCES "BuildDefinition" (id),
	FOREIGN KEY("RunDetails_id") REFERENCES "RunDetails" (id),
	FOREIGN KEY("Builder_uid") REFERENCES "Builder" (uid),
	FOREIGN KEY("VerificationSummaryAttestation_id") REFERENCES "VerificationSummaryAttestation" (id),
	FOREIGN KEY("SourceProvenanceAttestation_id") REFERENCES "SourceProvenanceAttestation" (id),
	FOREIGN KEY("DependencyInventory_id") REFERENCES "DependencyInventory" (id),
	FOREIGN KEY("BuildEnvironmentAttestation_id") REFERENCES "BuildEnvironmentAttestation" (id),
	FOREIGN KEY(digest_id) REFERENCES "DigestSet" (id)
);
CREATE INDEX "ix_ResourceDescriptor_id" ON "ResourceDescriptor" (id);

CREATE TABLE "Statement" (
	id INTEGER NOT NULL,
	_type TEXT NOT NULL,
	"predicateType" TEXT NOT NULL,
	predicate TEXT,
	"attestationStorageUri" TEXT,
	"signingTool" TEXT,
	"sigstoreLogEntry" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Statement_id" ON "Statement" (id);

CREATE TABLE "BuildDefinition" (
	id INTEGER NOT NULL,
	"buildType" TEXT NOT NULL,
	"externalParameters" TEXT,
	"internalParameters" TEXT,
	"hermeticBuild" BOOLEAN,
	"provenanceGenerationTool" TEXT,
	"pipelineOrchestrator" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BuildDefinition_id" ON "BuildDefinition" (id);

CREATE TABLE "Builder" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	version TEXT,
	"versionTag" TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Builder_uid" ON "Builder" (uid);

CREATE TABLE "BuildMetadata" (
	id INTEGER NOT NULL,
	"invocationId" TEXT,
	"startedOn" TEXT,
	"finishedOn" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BuildMetadata_id" ON "BuildMetadata" (id);

CREATE TABLE "VerificationSummaryAttestation" (
	id INTEGER NOT NULL,
	"timeVerified" TEXT,
	"resourceUri" TEXT NOT NULL,
	"verificationResult" VARCHAR(6) NOT NULL,
	"dependencyLevels" TEXT,
	"slsaVersion" TEXT,
	_type TEXT NOT NULL,
	"predicateType" TEXT NOT NULL,
	predicate TEXT,
	"attestationStorageUri" TEXT,
	"signingTool" TEXT,
	"sigstoreLogEntry" TEXT,
	verifier_uid INTEGER NOT NULL,
	policy_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(verifier_uid) REFERENCES "Verifier" (uid),
	FOREIGN KEY(policy_id) REFERENCES "ResourceDescriptor" (id)
);
CREATE INDEX "ix_VerificationSummaryAttestation_id" ON "VerificationSummaryAttestation" (id);

CREATE TABLE "Verifier" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	version TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Verifier_uid" ON "Verifier" (uid);

CREATE TABLE "Producer" (
	id INTEGER NOT NULL,
	name TEXT,
	"buildPlatformId" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Producer_id" ON "Producer" (id);

CREATE TABLE "Consumer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Consumer_id" ON "Consumer" (id);

CREATE TABLE "InfrastructureProvider" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InfrastructureProvider_id" ON "InfrastructureProvider" (id);

CREATE TABLE "BuildPlatform" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	"buildLevel" VARCHAR(18),
	"isHosted" BOOLEAN,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_BuildPlatform_uid" ON "BuildPlatform" (uid);

CREATE TABLE "ControlPlane" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ControlPlane_id" ON "ControlPlane" (id);

CREATE TABLE "SourceRepository" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	description TEXT,
	"sourceLevel" VARCHAR(19),
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_SourceRepository_uid" ON "SourceRepository" (uid);

CREATE TABLE "DependencyInventory" (
	id INTEGER NOT NULL,
	"dependencyLevel" VARCHAR(23),
	artifact_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(artifact_id) REFERENCES "ResourceDescriptor" (id)
);
CREATE INDEX "ix_DependencyInventory_id" ON "DependencyInventory" (id);

CREATE TABLE "AdoptionMetadata" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AdoptionMetadata_id" ON "AdoptionMetadata" (id);

CREATE TABLE "RunDetails" (
	id INTEGER NOT NULL,
	builder_uid INTEGER NOT NULL,
	"buildMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(builder_uid) REFERENCES "Builder" (uid),
	FOREIGN KEY("buildMetadata_id") REFERENCES "BuildMetadata" (id)
);
CREATE INDEX "ix_RunDetails_id" ON "RunDetails" (id);

CREATE TABLE "Package" (
	id INTEGER NOT NULL,
	name TEXT,
	ecosystem TEXT,
	registry TEXT,
	artifact_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(artifact_id) REFERENCES "ResourceDescriptor" (id)
);
CREATE INDEX "ix_Package_id" ON "Package" (id);

CREATE TABLE "SourceRevision" (
	id INTEGER NOT NULL,
	"revisionId" TEXT NOT NULL,
	author TEXT,
	timestamp TEXT,
	"reviewType" VARCHAR(16),
	repository_uid INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(repository_uid) REFERENCES "SourceRepository" (uid)
);
CREATE INDEX "ix_SourceRevision_id" ON "SourceRevision" (id);

CREATE TABLE "ResourceDescriptor_annotations" (
	"ResourceDescriptor_id" INTEGER,
	annotations TEXT,
	PRIMARY KEY ("ResourceDescriptor_id", annotations),
	FOREIGN KEY("ResourceDescriptor_id") REFERENCES "ResourceDescriptor" (id)
);
CREATE INDEX "ix_ResourceDescriptor_annotations_annotations" ON "ResourceDescriptor_annotations" (annotations);
CREATE INDEX "ix_ResourceDescriptor_annotations_ResourceDescriptor_id" ON "ResourceDescriptor_annotations" ("ResourceDescriptor_id");

CREATE TABLE "VerificationSummaryAttestation_verifiedLevels" (
	"VerificationSummaryAttestation_id" INTEGER,
	"verifiedLevels" VARCHAR(19) NOT NULL,
	PRIMARY KEY ("VerificationSummaryAttestation_id", "verifiedLevels"),
	FOREIGN KEY("VerificationSummaryAttestation_id") REFERENCES "VerificationSummaryAttestation" (id)
);
CREATE INDEX "ix_VerificationSummaryAttestation_verifiedLevels_verifiedLevels" ON "VerificationSummaryAttestation_verifiedLevels" ("verifiedLevels");
CREATE INDEX "ix_VerificationSummaryAttestation_verifiedLevels_VerificationSummaryAttestation_id" ON "VerificationSummaryAttestation_verifiedLevels" ("VerificationSummaryAttestation_id");

CREATE TABLE "AdoptionMetadata_challenges" (
	"AdoptionMetadata_id" INTEGER,
	challenges VARCHAR(22),
	PRIMARY KEY ("AdoptionMetadata_id", challenges),
	FOREIGN KEY("AdoptionMetadata_id") REFERENCES "AdoptionMetadata" (id)
);
CREATE INDEX "ix_AdoptionMetadata_challenges_challenges" ON "AdoptionMetadata_challenges" (challenges);
CREATE INDEX "ix_AdoptionMetadata_challenges_AdoptionMetadata_id" ON "AdoptionMetadata_challenges" ("AdoptionMetadata_id");

CREATE TABLE "AdoptionMetadata_strategies" (
	"AdoptionMetadata_id" INTEGER,
	strategies VARCHAR(32),
	PRIMARY KEY ("AdoptionMetadata_id", strategies),
	FOREIGN KEY("AdoptionMetadata_id") REFERENCES "AdoptionMetadata" (id)
);
CREATE INDEX "ix_AdoptionMetadata_strategies_AdoptionMetadata_id" ON "AdoptionMetadata_strategies" ("AdoptionMetadata_id");
CREATE INDEX "ix_AdoptionMetadata_strategies_strategies" ON "AdoptionMetadata_strategies" (strategies);

CREATE TABLE "SlsaDocument" (
	id INTEGER NOT NULL,
	"verificationResult" VARCHAR(6) NOT NULL,
	"buildDefinition_id" INTEGER NOT NULL,
	"runDetails_id" INTEGER NOT NULL,
	verifier_uid INTEGER NOT NULL,
	"adoptionMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("buildDefinition_id") REFERENCES "BuildDefinition" (id),
	FOREIGN KEY("runDetails_id") REFERENCES "RunDetails" (id),
	FOREIGN KEY(verifier_uid) REFERENCES "Verifier" (uid),
	FOREIGN KEY("adoptionMetadata_id") REFERENCES "AdoptionMetadata" (id)
);
CREATE INDEX "ix_SlsaDocument_id" ON "SlsaDocument" (id);

CREATE TABLE "BuildProvenance" (
	id INTEGER NOT NULL,
	_type TEXT NOT NULL,
	"predicateType" TEXT NOT NULL,
	predicate TEXT,
	"attestationStorageUri" TEXT,
	"signingTool" TEXT,
	"sigstoreLogEntry" TEXT,
	"buildDefinition_id" INTEGER NOT NULL,
	"runDetails_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("buildDefinition_id") REFERENCES "BuildDefinition" (id),
	FOREIGN KEY("runDetails_id") REFERENCES "RunDetails" (id)
);
CREATE INDEX "ix_BuildProvenance_id" ON "BuildProvenance" (id);

CREATE TABLE "SourceProvenanceAttestation" (
	id INTEGER NOT NULL,
	"sourceLevel" VARCHAR(19),
	_type TEXT NOT NULL,
	"predicateType" TEXT NOT NULL,
	predicate TEXT,
	"attestationStorageUri" TEXT,
	"signingTool" TEXT,
	"sigstoreLogEntry" TEXT,
	revision_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(revision_id) REFERENCES "SourceRevision" (id)
);
CREATE INDEX "ix_SourceProvenanceAttestation_id" ON "SourceProvenanceAttestation" (id);

CREATE TABLE "SourceRevision_parentRevisions" (
	"SourceRevision_id" INTEGER,
	"parentRevisions" TEXT,
	PRIMARY KEY ("SourceRevision_id", "parentRevisions"),
	FOREIGN KEY("SourceRevision_id") REFERENCES "SourceRevision" (id)
);
CREATE INDEX "ix_SourceRevision_parentRevisions_parentRevisions" ON "SourceRevision_parentRevisions" ("parentRevisions");
CREATE INDEX "ix_SourceRevision_parentRevisions_SourceRevision_id" ON "SourceRevision_parentRevisions" ("SourceRevision_id");

CREATE TABLE "BuildImage" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	"buildEnvLevel" VARCHAR(22),
	provenance_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(provenance_id) REFERENCES "BuildProvenance" (id)
);
CREATE INDEX "ix_BuildImage_uid" ON "BuildImage" (uid);

CREATE TABLE "SlsaDocument_verifiedLevels" (
	"SlsaDocument_id" INTEGER,
	"verifiedLevels" VARCHAR(19) NOT NULL,
	PRIMARY KEY ("SlsaDocument_id", "verifiedLevels"),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaDocument_verifiedLevels_SlsaDocument_id" ON "SlsaDocument_verifiedLevels" ("SlsaDocument_id");
CREATE INDEX "ix_SlsaDocument_verifiedLevels_verifiedLevels" ON "SlsaDocument_verifiedLevels" ("verifiedLevels");

CREATE TABLE "SourceProvenanceAttestation_controlsEnforced" (
	"SourceProvenanceAttestation_id" INTEGER,
	"controlsEnforced" TEXT,
	PRIMARY KEY ("SourceProvenanceAttestation_id", "controlsEnforced"),
	FOREIGN KEY("SourceProvenanceAttestation_id") REFERENCES "SourceProvenanceAttestation" (id)
);
CREATE INDEX "ix_SourceProvenanceAttestation_controlsEnforced_SourceProvenanceAttestation_id" ON "SourceProvenanceAttestation_controlsEnforced" ("SourceProvenanceAttestation_id");
CREATE INDEX "ix_SourceProvenanceAttestation_controlsEnforced_controlsEnforced" ON "SourceProvenanceAttestation_controlsEnforced" ("controlsEnforced");

CREATE TABLE "BuildEnvironmentAttestation" (
	id INTEGER NOT NULL,
	"buildId" TEXT NOT NULL,
	"buildEnvLevel" VARCHAR(22),
	_type TEXT NOT NULL,
	"predicateType" TEXT NOT NULL,
	predicate TEXT,
	"attestationStorageUri" TEXT,
	"signingTool" TEXT,
	"sigstoreLogEntry" TEXT,
	"buildImage_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("buildImage_uid") REFERENCES "BuildImage" (uid)
);
CREATE INDEX "ix_BuildEnvironmentAttestation_id" ON "BuildEnvironmentAttestation" (id);

CREATE TABLE "BuildEnvironmentAttestation_measurements" (
	"BuildEnvironmentAttestation_id" INTEGER,
	measurements TEXT,
	PRIMARY KEY ("BuildEnvironmentAttestation_id", measurements),
	FOREIGN KEY("BuildEnvironmentAttestation_id") REFERENCES "BuildEnvironmentAttestation" (id)
);
CREATE INDEX "ix_BuildEnvironmentAttestation_measurements_BuildEnvironmentAttestation_id" ON "BuildEnvironmentAttestation_measurements" ("BuildEnvironmentAttestation_id");
CREATE INDEX "ix_BuildEnvironmentAttestation_measurements_measurements" ON "BuildEnvironmentAttestation_measurements" (measurements);
