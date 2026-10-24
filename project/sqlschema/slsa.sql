-- # Class: SlsaDocument Description: A document that holds SLSA attestations and the parties, platforms, packages, repositories and images they concern.
--     * Slot: id
--     * Slot: adoption_metadata_id Description: How the deployment the document describes fares against the adoption study's themes.
-- # Class: InTotoDigestSet Description: A set of digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
--     * Slot: id
--     * Slot: sha256 Description: The SHA-256 digest of the artifact.
--     * Slot: sha512 Description: The SHA-512 digest of the artifact.
--     * Slot: git_commit Description: The git commit id of a source revision.
--     * Slot: git_tree Description: The git tree id of a source revision's content.
--     * Slot: dir_hash Description: A digest over a directory's content, as the in-toto framework defines it.
-- # Class: InTotoAnnotation Description: One vendor-specific annotation on a resource descriptor, with a key and one or more values.
--     * Slot: id
--     * Slot: annotation_key Description: The annotation's key.
--     * Slot: InTotoResourceDescriptor_id Description: Autocreated FK slot
-- # Class: InTotoResourceDescriptor Description: A reference to a software artifact or other resource, by URI, by digest, or both, with optional metadata.
--     * Slot: id
--     * Slot: resource_uri Description: The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.
--     * Slot: resource_name Description: A name for the resource within the attestation that carries it.
--     * Slot: download_location Description: Where the resource can be fetched, when that differs from its identifying URI.
--     * Slot: media_type Description: The IANA media type of the resource's content.
--     * Slot: InTotoStatement_id Description: Autocreated FK slot
--     * Slot: SlsaBuildPlatform_builder_id Description: Autocreated FK slot
--     * Slot: SlsaPackage_id Description: Autocreated FK slot
--     * Slot: SlsaBuildDefinition_id Description: Autocreated FK slot
--     * Slot: SlsaRunDetails_id Description: Autocreated FK slot
--     * Slot: SlsaVerificationSummary_id Description: Autocreated FK slot
--     * Slot: SlsaDependencyInventory_id Description: Autocreated FK slot
--     * Slot: digest_id Description: The cryptographic digests of a resource's content, keyed by algorithm.
-- # Class: InTotoStatement Description: The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
--     * Slot: id
--     * Slot: statement_type Description: The in-toto statement type, always https://in-toto.io/Statement/v1.
--     * Slot: predicate_type Description: The URI that names the predicate's type and so its schema, such as https://slsa.dev/provenance/v1.
--     * Slot: attestation_storage_uri Description: Where the signed attestation is stored or can be fetched.
--     * Slot: signing_tool Description: The tool that signed the attestation, named by URI, such as Cosign or Notation.
--     * Slot: transparency_log_entry Description: The transparency log entry that records the signature, such as a Rekor entry.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
--     * Slot: predicate_id Description: The predicate, one of the kinds this schema models; predicate_kind names which.
-- # Abstract Class: SlsaPredicate Description: The base of every predicate this schema models; predicate_kind names the concrete kind.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Abstract Class: SlsaParty Description: A person or organization that takes part in a software supply chain, in one of the roles SLSA names.
--     * Slot: id
--     * Slot: party_type Description: The role the party acts in, one of this class's descendants.
--     * Slot: party_name Description: The party's name.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaProducer Description: A party that creates software and provides it to others, choosing a build platform and distributing provenance.
--     * Slot: id
--     * Slot: build_platform Description: The build platform this party or component belongs to or uses.
--     * Slot: party_type Description: The role the party acts in, one of this class's descendants.
--     * Slot: party_name Description: The party's name.
-- # Class: SlsaConsumer Description: A party that uses software a producer provides, verifying its provenance itself or through a verifier.
--     * Slot: id
--     * Slot: party_type Description: The role the party acts in, one of this class's descendants.
--     * Slot: party_name Description: The party's name.
-- # Class: SlsaVerifier Description: A party that inspects provenance or other attestations and decides whether an artifact is authentic.
--     * Slot: id
--     * Slot: verifier_id Description: The URI that identifies the verifier.
--     * Slot: party_type Description: The role the party acts in, one of this class's descendants.
--     * Slot: party_name Description: The party's name.
-- # Class: SlsaInfrastructureProvider Description: A party that provides software or services to the other roles, such as a package registry's or a build platform's maintainers.
--     * Slot: id
--     * Slot: party_type Description: The role the party acts in, one of this class's descendants.
--     * Slot: party_name Description: The party's name.
-- # Class: SlsaBuildPlatform Description: The system that runs builds and records their provenance: the transitive closure of software, hardware, people and organizations trusted to do so. Provenance names it as the builder.
--     * Slot: builder_id Description: The URI that identifies the platform and determines its SLSA Build level.
--     * Slot: build_level Description: The highest SLSA Build level the platform's provenance can meet.
--     * Slot: hosted Description: Whether the platform is a hosted service on shared or dedicated infrastructure rather than an individual's workstation.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaControlPlane Description: The component of a build platform that orchestrates each build and generates its provenance, outside the tenant's control.
--     * Slot: id
--     * Slot: build_platform Description: The build platform this party or component belongs to or uses.
-- # Class: SlsaComponentVersion Description: The version of one named component of a platform.
--     * Slot: id
--     * Slot: component Description: The component's name.
--     * Slot: component_version Description: The component's version string.
--     * Slot: SlsaVerifier_id Description: Autocreated FK slot
--     * Slot: SlsaBuildPlatform_builder_id Description: Autocreated FK slot
-- # Class: SlsaPackageRegistry Description: A distribution platform that resolves package names to immutable package artifacts within an ecosystem.
--     * Slot: ecosystem Description: The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI.
--     * Slot: registry_uri Description: The URI that identifies the registry.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaPackage Description: A unit of software distributed under a package name, which is the primary security boundary SLSA protects. Its artifacts are the outputs of builds.
--     * Slot: id
--     * Slot: ecosystem Description: The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI.
--     * Slot: package_name Description: The name consumers use to obtain the package within its ecosystem and registry.
--     * Slot: registry Description: The registry the package is published to.
--     * Slot: guac_uri Description: Where a GUAC instance answers queries about the package's dependency and provenance graph.
--     * Slot: security_insights_uri Description: The SECURITY-INSIGHTS.yml file of the project that produces the package.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaBuildProvenance Description: The predicate that says how a build platform produced a set of artifacts, so that consumers can verify the build met their expectations and others can rebuild it.
--     * Slot: id
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: build_definition_id Description: The inputs to the build; required at Build L1.
--     * Slot: run_details_id Description: What is specific to this execution of the build; required at Build L1.
-- # Class: SlsaBuildDefinition Description: The inputs to a build, in enough detail to initialize it and begin execution; the builder vouches for their accuracy.
--     * Slot: id
--     * Slot: build_type Description: The URI of the template that says how to run the build and read its parameters and dependencies; required at Build L1.
--     * Slot: hermetic Description: Whether the build could reach only the dependencies it declared, with no other network or filesystem access.
--     * Slot: provenance_generation_tool Description: The tool that generated this provenance, named by URI.
--     * Slot: pipeline_orchestrator Description: The CI/CD system that coordinated the build, named by URI, where it differs from the builder.
-- # Class: SlsaBuildParameter Description: One named input to a build, with a string value.
--     * Slot: id
--     * Slot: parameter_name Description: The parameter's name.
--     * Slot: parameter_value Description: The parameter's value.
--     * Slot: SlsaBuildDefinition_id Description: Autocreated FK slot
-- # Class: SlsaRunDetails Description: What is specific to one execution of a build: the platform that ran it, metadata about the run and its by-products.
--     * Slot: id
--     * Slot: builder_builder_id Description: The build platform that ran the build and is trusted to have written this provenance; required at Build L1.
--     * Slot: build_metadata_id Description: Metadata about this execution of the build.
-- # Class: SlsaBuildMetadata Description: Metadata about one execution of a build: its identifier and when it started and finished.
--     * Slot: id
--     * Slot: invocation_id Description: An identifier for this build invocation, in a format the builder defines; useful for finding its logs.
--     * Slot: started_on Description: When the build started.
--     * Slot: finished_on Description: When the build finished.
-- # Class: SlsaVerificationSummary Description: The predicate in which a verifier records that it evaluated artifacts against a policy and the SLSA levels they met, so consumers can rely on the verifier instead of reading every underlying attestation.
--     * Slot: id
--     * Slot: resource_uri Description: The URI consumers fetch the artifact from, which the verifier verified it as.
--     * Slot: time_verified Description: When the verification happened.
--     * Slot: verification_result Description: Whether the subject passed the policy.
--     * Slot: slsa_version Description: The SLSA specification version the verifier applied, as MAJOR.MINOR.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
--     * Slot: verifier_id Description: The verifier that made this determination.
--     * Slot: policy_id Description: The policy the subject was verified against, by URI and preferably by digest too.
-- # Class: SlsaDependencyLevelCount Description: The number of an artifact's transitive dependencies verified at one level, each counted once per track at its highest level.
--     * Slot: id
--     * Slot: verified_level Description: The level the dependencies were verified at.
--     * Slot: dependency_count Description: How many dependencies were verified at that level.
--     * Slot: SlsaVerificationSummary_id Description: Autocreated FK slot
-- # Class: SlsaSourceControlSystem Description: The platform or services that host a source repository and enforce its organization's policies on authentication, authorization and change management.
--     * Slot: scs_uri Description: The URI that identifies the source control system.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaSourceRepository Description: A self-contained unit that holds a set of files, their revision history and metadata such as branches and tags.
--     * Slot: repository_uri Description: The stable locator the SCS gives the repository.
--     * Slot: hosted_by Description: The source control system that hosts the repository.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaSourceRevision Description: A logically immutable snapshot of a repository's tracked files, with its version-control metadata: author, time and parent revisions.
--     * Slot: repository Description: The source repository this belongs to.
--     * Slot: revision_id Description: The revision identifier the SCS assigns, such as a git commit id or a path- qualified sequence number.
--     * Slot: authored_by Description: The identity of the person or automation that authored the revision.
--     * Slot: authored_at Description: When the revision was created.
--     * Slot: source_level Description: The SLSA Source level the SCS asserts for the revision.
--     * Slot: review_type Description: The form of review that approved the revision.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaNamedReference Description: A user-friendly name for a revision in a repository, such as main or v1.2.3; reference_type says whether it is a branch or a tag.
--     * Slot: id
--     * Slot: repository Description: The source repository this belongs to.
--     * Slot: revision Description: The source revision this refers to.
--     * Slot: reference_type Description: The kind of named reference, one of this class's descendants.
--     * Slot: reference_name Description: The reference's name, fully qualified in git, such as refs/heads/main.
--     * Slot: protected Description: Whether the organization has the SCS enforce its technical controls on this reference.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
-- # Class: SlsaBranch Description: A named reference that moves to track a line of development.
--     * Slot: id
--     * Slot: repository Description: The source repository this belongs to.
--     * Slot: revision Description: The source revision this refers to.
--     * Slot: reference_type Description: The kind of named reference, one of this class's descendants.
--     * Slot: reference_name Description: The reference's name, fully qualified in git, such as refs/heads/main.
--     * Slot: protected Description: Whether the organization has the SCS enforce its technical controls on this reference.
-- # Class: SlsaTag Description: A named reference meant never to move once created.
--     * Slot: id
--     * Slot: repository Description: The source repository this belongs to.
--     * Slot: revision Description: The source revision this refers to.
--     * Slot: reference_type Description: The kind of named reference, one of this class's descendants.
--     * Slot: reference_name Description: The reference's name, fully qualified in git, such as refs/heads/main.
--     * Slot: protected Description: Whether the organization has the SCS enforce its technical controls on this reference.
-- # Class: SlsaSourceProvenance Description: Evidence from an SCS of how a revision came to exist and which technical controls were enforced when it did.
--     * Slot: id
--     * Slot: revision Description: The source revision this refers to.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Class: SlsaDependencyInventory Description: The inventory of every third-party build dependency, direct and transitive, of one artifact version.
--     * Slot: id
--     * Slot: dependency_level Description: The SLSA Dependency level the producer's process meets for this artifact.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
--     * Slot: artifact_id Description: The artifact whose dependencies are inventoried.
-- # Class: SlsaBuildImageProducer Description: The party that creates and distributes build images; the hosted build platform itself, or a third party in a bring-your-own-image setting.
--     * Slot: id
--     * Slot: party_type Description: The role the party acts in, one of this class's descendants.
--     * Slot: party_name Description: The party's name.
-- # Class: SlsaBuildImage Description: The template a build environment is instantiated from, such as a VM or container image: root filesystem, guest OS and packages, build executor and build agent.
--     * Slot: build_env_level Description: The SLSA Build Environment level this meets.
--     * Slot: image_uri Description: The URI that identifies the image version, such as an OCI reference with its digest.
--     * Slot: SlsaDocument_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: The build provenance of the image itself, required at Build Environment L1.
--     * Slot: produced_by_id Description: The party that created and distributes the image.
-- # Class: SlsaMeasurement Description: The digest of one component or state of a build environment, to compare with its reference value.
--     * Slot: id
--     * Slot: measured_component Description: The component or state that was measured, such as the bootloader, guest kernel, build agent or root filesystem.
--     * Slot: SlsaBuildEnvironmentAttestation_id Description: Autocreated FK slot
--     * Slot: digest_id Description: The cryptographic digests of a resource's content, keyed by algorithm.
-- # Class: SlsaBuildEnvironmentAttestation Description: Evidence of the state of a build environment when a build was dispatched to it: the image it came from and the measurements taken at boot.
--     * Slot: id
--     * Slot: build_env_level Description: The SLSA Build Environment level this meets.
--     * Slot: build_id Description: The immutable identifier of the build execution the environment was assigned to.
--     * Slot: build_image Description: The image the environment was instantiated from.
--     * Slot: predicate_kind Description: The kind of predicate, one of this class's descendants.
-- # Class: SlsaAdoptionMetadata Description: The adoption challenges a deployment meets and the strategies it applies, from the study's taxonomy.
--     * Slot: id
-- # Class: InTotoAnnotation_annotation_values
--     * Slot: InTotoAnnotation_id Description: Autocreated FK slot
--     * Slot: annotation_values Description: The annotation's values.
-- # Class: SlsaVerificationSummary_verified_levels
--     * Slot: SlsaVerificationSummary_id Description: Autocreated FK slot
--     * Slot: verified_levels Description: The highest level verified in each track, and any verified property; a level implies the levels below it.
-- # Class: SlsaVerificationSummary_organization_properties
--     * Slot: SlsaVerificationSummary_id Description: Autocreated FK slot
--     * Slot: organization_properties Description: Properties an organization defines for its own consumers, each prefixed ORG_SOURCE_.
-- # Class: SlsaSourceRevision_parent_revisions
--     * Slot: SlsaSourceRevision_revision_id Description: Autocreated FK slot
--     * Slot: parent_revisions_revision_id Description: The revisions this one descends from, which together form the change history.
-- # Class: SlsaSourceProvenance_controls_enforced
--     * Slot: SlsaSourceProvenance_id Description: Autocreated FK slot
--     * Slot: controls_enforced Description: The technical controls the SCS enforced when the revision was created, as the organization documents them.
-- # Class: SlsaAdoptionMetadata_challenges
--     * Slot: SlsaAdoptionMetadata_id Description: Autocreated FK slot
--     * Slot: challenges Description: The challenge themes that apply.
-- # Class: SlsaAdoptionMetadata_strategies
--     * Slot: SlsaAdoptionMetadata_id Description: Autocreated FK slot
--     * Slot: strategies Description: The strategy themes applied or recommended.

CREATE TABLE "InTotoDigestSet" (
	id INTEGER NOT NULL,
	sha256 TEXT,
	sha512 TEXT,
	git_commit TEXT,
	git_tree TEXT,
	dir_hash TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InTotoDigestSet_id" ON "InTotoDigestSet" (id);

CREATE TABLE "InTotoResourceDescriptor" (
	id INTEGER NOT NULL,
	resource_uri TEXT,
	resource_name TEXT,
	download_location TEXT,
	media_type TEXT,
	"InTotoStatement_id" INTEGER,
	"SlsaBuildPlatform_builder_id" TEXT,
	"SlsaPackage_id" INTEGER,
	"SlsaBuildDefinition_id" INTEGER,
	"SlsaRunDetails_id" INTEGER,
	"SlsaVerificationSummary_id" INTEGER,
	"SlsaDependencyInventory_id" INTEGER,
	digest_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoStatement_id") REFERENCES "InTotoStatement" (id),
	FOREIGN KEY("SlsaBuildPlatform_builder_id") REFERENCES "SlsaBuildPlatform" (builder_id),
	FOREIGN KEY("SlsaPackage_id") REFERENCES "SlsaPackage" (id),
	FOREIGN KEY("SlsaBuildDefinition_id") REFERENCES "SlsaBuildDefinition" (id),
	FOREIGN KEY("SlsaRunDetails_id") REFERENCES "SlsaRunDetails" (id),
	FOREIGN KEY("SlsaVerificationSummary_id") REFERENCES "SlsaVerificationSummary" (id),
	FOREIGN KEY("SlsaDependencyInventory_id") REFERENCES "SlsaDependencyInventory" (id),
	FOREIGN KEY(digest_id) REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_InTotoResourceDescriptor_id" ON "InTotoResourceDescriptor" (id);

CREATE TABLE "SlsaPredicate" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaPredicate_id" ON "SlsaPredicate" (id);

CREATE TABLE "SlsaConsumer" (
	id INTEGER NOT NULL,
	party_type TEXT,
	party_name TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaConsumer_id" ON "SlsaConsumer" (id);

CREATE TABLE "SlsaVerifier" (
	id INTEGER NOT NULL,
	verifier_id TEXT NOT NULL,
	party_type TEXT,
	party_name TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaVerifier_id" ON "SlsaVerifier" (id);

CREATE TABLE "SlsaInfrastructureProvider" (
	id INTEGER NOT NULL,
	party_type TEXT,
	party_name TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaInfrastructureProvider_id" ON "SlsaInfrastructureProvider" (id);

CREATE TABLE "SlsaBuildDefinition" (
	id INTEGER NOT NULL,
	build_type TEXT NOT NULL,
	hermetic BOOLEAN,
	provenance_generation_tool TEXT,
	pipeline_orchestrator TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaBuildDefinition_id" ON "SlsaBuildDefinition" (id);

CREATE TABLE "SlsaBuildMetadata" (
	id INTEGER NOT NULL,
	invocation_id TEXT,
	started_on DATETIME,
	finished_on DATETIME,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaBuildMetadata_id" ON "SlsaBuildMetadata" (id);

CREATE TABLE "SlsaVerificationSummary" (
	id INTEGER NOT NULL,
	resource_uri TEXT NOT NULL,
	time_verified DATETIME,
	verification_result VARCHAR(6) NOT NULL,
	slsa_version TEXT,
	predicate_kind TEXT,
	verifier_id INTEGER NOT NULL,
	policy_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(verifier_id) REFERENCES "SlsaVerifier" (id),
	FOREIGN KEY(policy_id) REFERENCES "InTotoResourceDescriptor" (id)
);
CREATE INDEX "ix_SlsaVerificationSummary_id" ON "SlsaVerificationSummary" (id);

CREATE TABLE "SlsaDependencyInventory" (
	id INTEGER NOT NULL,
	dependency_level VARCHAR(23),
	"SlsaDocument_id" INTEGER,
	artifact_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id),
	FOREIGN KEY(artifact_id) REFERENCES "InTotoResourceDescriptor" (id)
);
CREATE INDEX "ix_SlsaDependencyInventory_id" ON "SlsaDependencyInventory" (id);

CREATE TABLE "SlsaBuildImageProducer" (
	id INTEGER NOT NULL,
	party_type TEXT,
	party_name TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaBuildImageProducer_id" ON "SlsaBuildImageProducer" (id);

CREATE TABLE "SlsaAdoptionMetadata" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SlsaAdoptionMetadata_id" ON "SlsaAdoptionMetadata" (id);

CREATE TABLE "SlsaDocument" (
	id INTEGER NOT NULL,
	adoption_metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(adoption_metadata_id) REFERENCES "SlsaAdoptionMetadata" (id)
);
CREATE INDEX "ix_SlsaDocument_id" ON "SlsaDocument" (id);

CREATE TABLE "InTotoAnnotation" (
	id INTEGER NOT NULL,
	annotation_key TEXT NOT NULL,
	"InTotoResourceDescriptor_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InTotoResourceDescriptor_id") REFERENCES "InTotoResourceDescriptor" (id)
);
CREATE INDEX "ix_InTotoAnnotation_id" ON "InTotoAnnotation" (id);

CREATE TABLE "SlsaBuildParameter" (
	id INTEGER NOT NULL,
	parameter_name TEXT NOT NULL,
	parameter_value TEXT,
	"SlsaBuildDefinition_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaBuildDefinition_id") REFERENCES "SlsaBuildDefinition" (id)
);
CREATE INDEX "ix_SlsaBuildParameter_id" ON "SlsaBuildParameter" (id);

CREATE TABLE "SlsaDependencyLevelCount" (
	id INTEGER NOT NULL,
	verified_level VARCHAR(30) NOT NULL,
	dependency_count INTEGER NOT NULL,
	"SlsaVerificationSummary_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaVerificationSummary_id") REFERENCES "SlsaVerificationSummary" (id)
);
CREATE INDEX "ix_SlsaDependencyLevelCount_id" ON "SlsaDependencyLevelCount" (id);

CREATE TABLE "SlsaVerificationSummary_verified_levels" (
	"SlsaVerificationSummary_id" INTEGER,
	verified_levels VARCHAR(30) NOT NULL,
	PRIMARY KEY ("SlsaVerificationSummary_id", verified_levels),
	FOREIGN KEY("SlsaVerificationSummary_id") REFERENCES "SlsaVerificationSummary" (id)
);
CREATE INDEX "ix_SlsaVerificationSummary_verified_levels_SlsaVerificationSummary_id" ON "SlsaVerificationSummary_verified_levels" ("SlsaVerificationSummary_id");
CREATE INDEX "ix_SlsaVerificationSummary_verified_levels_verified_levels" ON "SlsaVerificationSummary_verified_levels" (verified_levels);

CREATE TABLE "SlsaVerificationSummary_organization_properties" (
	"SlsaVerificationSummary_id" INTEGER,
	organization_properties TEXT,
	PRIMARY KEY ("SlsaVerificationSummary_id", organization_properties),
	FOREIGN KEY("SlsaVerificationSummary_id") REFERENCES "SlsaVerificationSummary" (id)
);
CREATE INDEX "ix_SlsaVerificationSummary_organization_properties_organization_properties" ON "SlsaVerificationSummary_organization_properties" (organization_properties);
CREATE INDEX "ix_SlsaVerificationSummary_organization_properties_SlsaVerificationSummary_id" ON "SlsaVerificationSummary_organization_properties" ("SlsaVerificationSummary_id");

CREATE TABLE "SlsaAdoptionMetadata_challenges" (
	"SlsaAdoptionMetadata_id" INTEGER,
	challenges VARCHAR(22),
	PRIMARY KEY ("SlsaAdoptionMetadata_id", challenges),
	FOREIGN KEY("SlsaAdoptionMetadata_id") REFERENCES "SlsaAdoptionMetadata" (id)
);
CREATE INDEX "ix_SlsaAdoptionMetadata_challenges_SlsaAdoptionMetadata_id" ON "SlsaAdoptionMetadata_challenges" ("SlsaAdoptionMetadata_id");
CREATE INDEX "ix_SlsaAdoptionMetadata_challenges_challenges" ON "SlsaAdoptionMetadata_challenges" (challenges);

CREATE TABLE "SlsaAdoptionMetadata_strategies" (
	"SlsaAdoptionMetadata_id" INTEGER,
	strategies VARCHAR(32),
	PRIMARY KEY ("SlsaAdoptionMetadata_id", strategies),
	FOREIGN KEY("SlsaAdoptionMetadata_id") REFERENCES "SlsaAdoptionMetadata" (id)
);
CREATE INDEX "ix_SlsaAdoptionMetadata_strategies_SlsaAdoptionMetadata_id" ON "SlsaAdoptionMetadata_strategies" ("SlsaAdoptionMetadata_id");
CREATE INDEX "ix_SlsaAdoptionMetadata_strategies_strategies" ON "SlsaAdoptionMetadata_strategies" (strategies);

CREATE TABLE "InTotoStatement" (
	id INTEGER NOT NULL,
	statement_type TEXT NOT NULL,
	predicate_type TEXT NOT NULL,
	attestation_storage_uri TEXT,
	signing_tool TEXT,
	transparency_log_entry TEXT,
	"SlsaDocument_id" INTEGER,
	predicate_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id),
	FOREIGN KEY(predicate_id) REFERENCES "SlsaPredicate" (id)
);
CREATE INDEX "ix_InTotoStatement_id" ON "InTotoStatement" (id);

CREATE TABLE "SlsaParty" (
	id INTEGER NOT NULL,
	party_type TEXT,
	party_name TEXT,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaParty_id" ON "SlsaParty" (id);

CREATE TABLE "SlsaBuildPlatform" (
	builder_id TEXT NOT NULL,
	build_level VARCHAR(18),
	hosted BOOLEAN,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (builder_id),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaBuildPlatform_builder_id" ON "SlsaBuildPlatform" (builder_id);

CREATE TABLE "SlsaPackageRegistry" (
	ecosystem TEXT,
	registry_uri TEXT NOT NULL,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (registry_uri),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaPackageRegistry_registry_uri" ON "SlsaPackageRegistry" (registry_uri);

CREATE TABLE "SlsaSourceControlSystem" (
	scs_uri TEXT NOT NULL,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (scs_uri),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaSourceControlSystem_scs_uri" ON "SlsaSourceControlSystem" (scs_uri);

CREATE TABLE "InTotoAnnotation_annotation_values" (
	"InTotoAnnotation_id" INTEGER,
	annotation_values TEXT,
	PRIMARY KEY ("InTotoAnnotation_id", annotation_values),
	FOREIGN KEY("InTotoAnnotation_id") REFERENCES "InTotoAnnotation" (id)
);
CREATE INDEX "ix_InTotoAnnotation_annotation_values_annotation_values" ON "InTotoAnnotation_annotation_values" (annotation_values);
CREATE INDEX "ix_InTotoAnnotation_annotation_values_InTotoAnnotation_id" ON "InTotoAnnotation_annotation_values" ("InTotoAnnotation_id");

CREATE TABLE "SlsaProducer" (
	id INTEGER NOT NULL,
	build_platform TEXT,
	party_type TEXT,
	party_name TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(build_platform) REFERENCES "SlsaBuildPlatform" (builder_id)
);
CREATE INDEX "ix_SlsaProducer_id" ON "SlsaProducer" (id);

CREATE TABLE "SlsaControlPlane" (
	id INTEGER NOT NULL,
	build_platform TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(build_platform) REFERENCES "SlsaBuildPlatform" (builder_id)
);
CREATE INDEX "ix_SlsaControlPlane_id" ON "SlsaControlPlane" (id);

CREATE TABLE "SlsaComponentVersion" (
	id INTEGER NOT NULL,
	component TEXT NOT NULL,
	component_version TEXT,
	"SlsaVerifier_id" INTEGER,
	"SlsaBuildPlatform_builder_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaVerifier_id") REFERENCES "SlsaVerifier" (id),
	FOREIGN KEY("SlsaBuildPlatform_builder_id") REFERENCES "SlsaBuildPlatform" (builder_id)
);
CREATE INDEX "ix_SlsaComponentVersion_id" ON "SlsaComponentVersion" (id);

CREATE TABLE "SlsaPackage" (
	id INTEGER NOT NULL,
	ecosystem TEXT,
	package_name TEXT NOT NULL,
	registry TEXT,
	guac_uri TEXT,
	security_insights_uri TEXT,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(registry) REFERENCES "SlsaPackageRegistry" (registry_uri),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaPackage_id" ON "SlsaPackage" (id);

CREATE TABLE "SlsaRunDetails" (
	id INTEGER NOT NULL,
	builder_builder_id TEXT NOT NULL,
	build_metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(builder_builder_id) REFERENCES "SlsaBuildPlatform" (builder_id),
	FOREIGN KEY(build_metadata_id) REFERENCES "SlsaBuildMetadata" (id)
);
CREATE INDEX "ix_SlsaRunDetails_id" ON "SlsaRunDetails" (id);

CREATE TABLE "SlsaSourceRepository" (
	repository_uri TEXT NOT NULL,
	hosted_by TEXT,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (repository_uri),
	FOREIGN KEY(hosted_by) REFERENCES "SlsaSourceControlSystem" (scs_uri),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaSourceRepository_repository_uri" ON "SlsaSourceRepository" (repository_uri);

CREATE TABLE "SlsaBuildProvenance" (
	id INTEGER NOT NULL,
	predicate_kind TEXT,
	build_definition_id INTEGER NOT NULL,
	run_details_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(build_definition_id) REFERENCES "SlsaBuildDefinition" (id),
	FOREIGN KEY(run_details_id) REFERENCES "SlsaRunDetails" (id)
);
CREATE INDEX "ix_SlsaBuildProvenance_id" ON "SlsaBuildProvenance" (id);

CREATE TABLE "SlsaSourceRevision" (
	repository TEXT,
	revision_id TEXT NOT NULL,
	authored_by TEXT,
	authored_at DATETIME,
	source_level VARCHAR(19),
	review_type VARCHAR(16),
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (revision_id),
	FOREIGN KEY(repository) REFERENCES "SlsaSourceRepository" (repository_uri),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaSourceRevision_revision_id" ON "SlsaSourceRevision" (revision_id);

CREATE TABLE "SlsaNamedReference" (
	id INTEGER NOT NULL,
	repository TEXT,
	revision TEXT,
	reference_type TEXT,
	reference_name TEXT NOT NULL,
	protected BOOLEAN,
	"SlsaDocument_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(repository) REFERENCES "SlsaSourceRepository" (repository_uri),
	FOREIGN KEY(revision) REFERENCES "SlsaSourceRevision" (revision_id),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id)
);
CREATE INDEX "ix_SlsaNamedReference_id" ON "SlsaNamedReference" (id);

CREATE TABLE "SlsaBranch" (
	id INTEGER NOT NULL,
	repository TEXT,
	revision TEXT,
	reference_type TEXT,
	reference_name TEXT NOT NULL,
	protected BOOLEAN,
	PRIMARY KEY (id),
	FOREIGN KEY(repository) REFERENCES "SlsaSourceRepository" (repository_uri),
	FOREIGN KEY(revision) REFERENCES "SlsaSourceRevision" (revision_id)
);
CREATE INDEX "ix_SlsaBranch_id" ON "SlsaBranch" (id);

CREATE TABLE "SlsaTag" (
	id INTEGER NOT NULL,
	repository TEXT,
	revision TEXT,
	reference_type TEXT,
	reference_name TEXT NOT NULL,
	protected BOOLEAN,
	PRIMARY KEY (id),
	FOREIGN KEY(repository) REFERENCES "SlsaSourceRepository" (repository_uri),
	FOREIGN KEY(revision) REFERENCES "SlsaSourceRevision" (revision_id)
);
CREATE INDEX "ix_SlsaTag_id" ON "SlsaTag" (id);

CREATE TABLE "SlsaSourceProvenance" (
	id INTEGER NOT NULL,
	revision TEXT NOT NULL,
	predicate_kind TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(revision) REFERENCES "SlsaSourceRevision" (revision_id)
);
CREATE INDEX "ix_SlsaSourceProvenance_id" ON "SlsaSourceProvenance" (id);

CREATE TABLE "SlsaBuildImage" (
	build_env_level VARCHAR(22),
	image_uri TEXT NOT NULL,
	"SlsaDocument_id" INTEGER,
	provenance_id INTEGER,
	produced_by_id INTEGER,
	PRIMARY KEY (image_uri),
	FOREIGN KEY("SlsaDocument_id") REFERENCES "SlsaDocument" (id),
	FOREIGN KEY(provenance_id) REFERENCES "SlsaBuildProvenance" (id),
	FOREIGN KEY(produced_by_id) REFERENCES "SlsaBuildImageProducer" (id)
);
CREATE INDEX "ix_SlsaBuildImage_image_uri" ON "SlsaBuildImage" (image_uri);

CREATE TABLE "SlsaSourceRevision_parent_revisions" (
	"SlsaSourceRevision_revision_id" TEXT,
	parent_revisions_revision_id TEXT,
	PRIMARY KEY ("SlsaSourceRevision_revision_id", parent_revisions_revision_id),
	FOREIGN KEY("SlsaSourceRevision_revision_id") REFERENCES "SlsaSourceRevision" (revision_id),
	FOREIGN KEY(parent_revisions_revision_id) REFERENCES "SlsaSourceRevision" (revision_id)
);
CREATE INDEX "ix_SlsaSourceRevision_parent_revisions_parent_revisions_revision_id" ON "SlsaSourceRevision_parent_revisions" (parent_revisions_revision_id);
CREATE INDEX "ix_SlsaSourceRevision_parent_revisions_SlsaSourceRevision_revision_id" ON "SlsaSourceRevision_parent_revisions" ("SlsaSourceRevision_revision_id");

CREATE TABLE "SlsaBuildEnvironmentAttestation" (
	id INTEGER NOT NULL,
	build_env_level VARCHAR(22),
	build_id TEXT NOT NULL,
	build_image TEXT,
	predicate_kind TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(build_image) REFERENCES "SlsaBuildImage" (image_uri)
);
CREATE INDEX "ix_SlsaBuildEnvironmentAttestation_id" ON "SlsaBuildEnvironmentAttestation" (id);

CREATE TABLE "SlsaSourceProvenance_controls_enforced" (
	"SlsaSourceProvenance_id" INTEGER,
	controls_enforced TEXT,
	PRIMARY KEY ("SlsaSourceProvenance_id", controls_enforced),
	FOREIGN KEY("SlsaSourceProvenance_id") REFERENCES "SlsaSourceProvenance" (id)
);
CREATE INDEX "ix_SlsaSourceProvenance_controls_enforced_controls_enforced" ON "SlsaSourceProvenance_controls_enforced" (controls_enforced);
CREATE INDEX "ix_SlsaSourceProvenance_controls_enforced_SlsaSourceProvenance_id" ON "SlsaSourceProvenance_controls_enforced" ("SlsaSourceProvenance_id");

CREATE TABLE "SlsaMeasurement" (
	id INTEGER NOT NULL,
	measured_component TEXT NOT NULL,
	"SlsaBuildEnvironmentAttestation_id" INTEGER,
	digest_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SlsaBuildEnvironmentAttestation_id") REFERENCES "SlsaBuildEnvironmentAttestation" (id),
	FOREIGN KEY(digest_id) REFERENCES "InTotoDigestSet" (id)
);
CREATE INDEX "ix_SlsaMeasurement_id" ON "SlsaMeasurement" (id);
