export type SlsaBuildPlatformBuilderId = string;
export type SlsaPackageRegistryRegistryUri = string;
export type SlsaSourceControlSystemScsUri = string;
export type SlsaSourceRepositoryRepositoryUri = string;
export type SlsaSourceRevisionRevisionId = string;
export type SlsaBuildImageImageUri = string;
/**
* The levels of the SLSA Build track, each adding protection against tampering with the build or its provenance.
*/
export enum SlsaBuildLevel {
    
    /** No requirements; the absence of SLSA, as for development or test builds. */
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0",
    /** Provenance exists and shows how the package was built; it prevents mistakes but is easy to forge. */
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1",
    /** A hosted platform generates and signs the provenance, so tampering after the build needs an explicit attack. */
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2",
    /** A hardened platform prevents runs from influencing one another and keeps signing material away from build steps, so forging provenance needs an exploit. */
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3",
};
/**
* The outcome of verifying an artifact against a policy.
*/
export enum SlsaVerificationResult {
    
    /** The artifact met the policy. */
    PASSED = "PASSED",
    /** The artifact did not meet the policy. */
    FAILED = "FAILED",
};
/**
* A result of evaluating an artifact against SLSA: a track level, a verified property, or a failure. A level implies the levels below it in the same track.
*/
export enum SlsaResult {
    
    /** The issuer makes no claim about the Build track level. */
    SLSA_BUILD_LEVEL_UNEVALUATED = "SLSA_BUILD_LEVEL_UNEVALUATED",
    /** No Build track guarantees were verified. */
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0",
    /** Build level 1 was verified. */
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1",
    /** Build level 2 was verified. */
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2",
    /** Build level 3 was verified. */
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3",
    /** The issuer makes no claim about the Source track level. */
    SLSA_SOURCE_LEVEL_UNEVALUATED = "SLSA_SOURCE_LEVEL_UNEVALUATED",
    /** No Source track guarantees were verified. */
    SLSA_SOURCE_LEVEL_0 = "SLSA_SOURCE_LEVEL_0",
    /** Source level 1 was verified. */
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1",
    /** Source level 2 was verified. */
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2",
    /** Source level 3 was verified. */
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3",
    /** Source level 4 was verified. */
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4",
    /** The verified property that two trusted persons reviewed the source, at whatever source level. */
    SLSA_SOURCE_TWO_PARTY_REVIEWED = "SLSA_SOURCE_TWO_PARTY_REVIEWED",
    /** The verified property that two or more independent build platforms reproduced the artifact. */
    SLSA_BUILD_REPRODUCED = "SLSA_BUILD_REPRODUCED",
    /** Policy evaluation failed. */
    FAILED = "FAILED",
};
/**
* The levels of the SLSA Source track, each adding trust in how a revision was created.
*/
export enum SlsaSourceLevel {
    
    /** No Source track guarantees; a revision for which the SCS issues no Source VSA is at this level. */
    SLSA_SOURCE_LEVEL_0 = "SLSA_SOURCE_LEVEL_0",
    /** The source is managed in a version control system, so it has discrete, immutable revisions. */
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1",
    /** Branch history is continuous and retained, and the SCS issues source provenance for each new revision. */
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2",
    /** The SCS enforces the organization's technical controls on protected named references and provides evidence of them. */
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3",
    /** Two trusted persons agree to every change on protected branches. */
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4",
};
/**
* The forms of review that may approve a revision, including the contested forms the adoption study records.
*/
export enum SlsaReviewType {
    
    /** A reviewer distinct from the author approved the change, both being trusted persons. */
    TWO_PARTY = "TWO_PARTY",
    /** Two developers wrote the change together at one workstation or screen; whether this counts as two-party review is open. */
    PAIR_PROGRAMMING = "PAIR_PROGRAMMING",
    /** A group wrote the change together; whether this counts as two-party review is open. */
    MOB_PROGRAMMING = "MOB_PROGRAMMING",
    /** A tool or bot reviewed the change with no second person, which is not two-party review. */
    AUTOMATED = "AUTOMATED",
};
/**
* The levels of the SLSA Dependency track, each reducing the risk third-party dependencies bring.
*/
export enum SlsaDependencyLevel {
    
    /** No Dependency track claims. */
    SLSA_DEPENDENCY_LEVEL_0 = "SLSA_DEPENDENCY_LEVEL_0",
    /** An inventory of all build dependencies, direct and transitive, exists. */
    SLSA_DEPENDENCY_LEVEL_1 = "SLSA_DEPENDENCY_LEVEL_1",
    /** Every known vulnerability in the dependencies was triaged before release. */
    SLSA_DEPENDENCY_LEVEL_2 = "SLSA_DEPENDENCY_LEVEL_2",
    /** Every third-party build dependency is consumed from a location the producer controls. */
    SLSA_DEPENDENCY_LEVEL_3 = "SLSA_DEPENDENCY_LEVEL_3",
    /** An ingestion policy keeps compromised upstream dependencies out of the build. */
    SLSA_DEPENDENCY_LEVEL_4 = "SLSA_DEPENDENCY_LEVEL_4",
};
/**
* The levels of the SLSA Build Environment track, each extending integrity further into the compute that runs builds.
*/
export enum SlsaBuildEnvironmentLevel {
    
    /** No Build Environment track claims. */
    SLSA_BUILD_ENV_LEVEL_0 = "SLSA_BUILD_ENV_LEVEL_0",
    /** The build image has signed build provenance, protecting against tampering while the image is distributed. */
    SLSA_BUILD_ENV_LEVEL_1 = "SLSA_BUILD_ENV_LEVEL_1",
    /** The compute platform attests to the environment's state at boot, protecting against tampering through the control plane. */
    SLSA_BUILD_ENV_LEVEL_2 = "SLSA_BUILD_ENV_LEVEL_2",
    /** Trusted hardware attests to the host's state, protecting against tampering through the host interface. */
    SLSA_BUILD_ENV_LEVEL_3 = "SLSA_BUILD_ENV_LEVEL_3",
};
/**
* The four themes of difficulty practitioners met when adopting SLSA.
*/
export enum SlsaAdoptionChallenge {
    
    /** Generating provenance and maintaining the required tools is complicated. */
    COMPLEX_IMPLEMENTATION = "COMPLEX_IMPLEMENTATION",
    /** SLSA's terms and its guidance for particular ecosystems are hard to understand. */
    UNCLEAR_COMMUNICATION = "UNCLEAR_COMMUNICATION",
    /** Verification tooling, attestation storage and two-party review are hard to put into practice. */
    LIMITED_FEASIBILITY = "LIMITED_FEASIBILITY",
    /** Which attacks SLSA mitigates, and how it differs from other practices, is unclear. */
    UNCLEAR_RELEVANCE = "UNCLEAR_RELEVANCE",
};
/**
* The five themes of strategy practitioners proposed for the adoption challenges.
*/
export enum SlsaAdoptionStrategy {
    
    /** Make SLSA fit more contexts, with build-system tracks, gamified levels, flexibility for varied organizations and alignment with OpenSSF practices. */
    ENHANCE_ALIGNMENT_FLEXIBILITY = "ENHANCE_ALIGNMENT_FLEXIBILITY",
    /** Give clearer definitions, standard terms, negative examples and better navigation. */
    PROVIDE_DETAILED_DOCUMENTATION = "PROVIDE_DETAILED_DOCUMENTATION",
    /** Simplify and standardize provenance generation with tools and templates, and fix release-tool inconsistencies. */
    STREAMLINE_PROVENANCE_GENERATION = "STREAMLINE_PROVENANCE_GENERATION",
    /** Strengthen verification and level determination, tag versions early, and give downstream users more signals. */
    IMPROVE_VERIFICATION_PROCESS = "IMPROVE_VERIFICATION_PROCESS",
    /** Align with industry standards, guide newcomers, and share knowledge across projects. */
    COLLABORATE_WITH_COMMUNITY = "COLLABORATE_WITH_COMMUNITY",
};


/**
 * A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
 */
export interface InTotoDigestSet {
    /** The SHA-256 digest of the artifact. */
    sha256?: string,
    /** The SHA-224 digest of the artifact. */
    sha224?: string,
    /** The SHA-384 digest of the artifact. */
    sha384?: string,
    /** The SHA-512 digest of the artifact. */
    sha512?: string,
    /** The SHA-512/224 digest of the artifact. */
    sha512_224?: string,
    /** The SHA-512/256 digest of the artifact. */
    sha512_256?: string,
    /** The SHA3-224 digest of the artifact. */
    sha3_224?: string,
    /** The SHA3-256 digest of the artifact. */
    sha3_256?: string,
    /** The SHA3-384 digest of the artifact. */
    sha3_384?: string,
    /** The SHA3-512 digest of the artifact. */
    sha3_512?: string,
    /** The SHAKE128 digest of the artifact, of at least 32 bytes. */
    shake128?: string,
    /** The SHAKE256 digest of the artifact, of at least 32 bytes. */
    shake256?: string,
    /** The BLAKE2b digest of the artifact, of 32 to 64 bytes. */
    blake2b?: string,
    /** The BLAKE2s digest of the artifact, at its full 32 bytes. */
    blake2s?: string,
    /** The RIPEMD-160 digest of the artifact. */
    ripemd160?: string,
    /** The SM3 digest of the artifact. */
    sm3?: string,
    /** The GOST R 34.11 digest of the artifact, of 256 or 512 bits. */
    gost?: string,
    /** The SHA-1 digest of the artifact. */
    sha1?: string,
    /** The MD5 digest of the artifact. */
    md5?: string,
    /** A digest over a directory's content by the dirhash Hash1 function, in lowercase hexadecimal rather than base64. */
    dir_hash?: string,
    /** The git commit id of a source revision. */
    git_commit?: string,
    /** The git tree id of a source revision's content, or of any file tree. */
    git_tree?: string,
    /** The git blob id of a file's content. */
    git_blob?: string,
    /** The git object id of an annotated tag. */
    git_tag?: string,
    /** The digests under algorithms this class does not name. */
    additional_digests?: InTotoAdditionalDigest[],
}


/**
 * One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
 */
export interface InTotoAdditionalDigest {
    /** The algorithm's name, as the key the attestation's JSON uses, such as svn_revision_id. */
    algorithm: string,
    /** The digest under that algorithm, in the encoding the algorithm documents. */
    value: string,
}


/**
 * One vendor-specific annotation on a resource descriptor: a key and its values.
 */
export interface InTotoAnnotation {
    /** The annotation's key. */
    annotation_key: string,
    /** The annotation's values. */
    annotation_values?: string[],
}


/**
 * A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with optional metadata.
 */
export interface InTotoResourceDescriptor {
    /** The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference. */
    resource_uri?: string,
    /** The cryptographic digests of a resource's content, keyed by algorithm. */
    digest?: InTotoDigestSet,
    /** A name for the resource within the attestation that carries it. */
    resource_name?: string,
    /** Where the resource can be fetched, when that differs from its identifying URI. */
    download_location?: string,
    /** The IANA media type of the resource's content. */
    media_type?: string,
    /** The resource's content itself, base64-encoded, for a resource small enough to carry inline. */
    content?: string,
    /** Vendor-specific annotations on the resource, such as the source references a Source VSA records. */
    annotations?: InTotoAnnotation[],
}


/**
 * One artifact an in-toto statement is about: a resource descriptor that carries a digest.
 */
export interface InTotoStatementSubject extends InTotoResourceDescriptor {
}


/**
 * The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
 */
export interface InTotoStatement {
    /** The in-toto statement type, always https://in-toto.io/Statement/v1. */
    statement_type: string,
    /** The artifacts the predicate is about, each with a digest. */
    subject: InTotoStatementSubject[],
    /** The URI that names the predicate's type and so its schema, such as https://slsa.dev/provenance/v1. */
    predicate_type: string,
    /** The predicate, one of the kinds this schema models; predicate_kind names which. */
    predicate?: SlsaPredicate,
    /** Where the signed attestation is stored or can be fetched. */
    attestation_storage_uri?: string,
    /** The tool that signed the attestation, named by URI, such as Cosign or Notation. */
    signing_tool?: string,
    /** The transparency log entry that records the signature, such as a Rekor entry. */
    transparency_log_entry?: string,
}


/**
 * The base of every predicate this schema models; predicate_kind names the concrete kind.
 */
export interface SlsaPredicate {
    /** The kind of predicate, one of this class's descendants. */
    predicate_kind?: string,
}


/**
 * A person or organization that takes part in a software supply chain, in one of the roles SLSA names.
 */
export interface SlsaParty {
    /** The role the party acts in, one of this class's descendants. */
    party_type?: string,
    /** The party's name. */
    party_name?: string,
}


/**
 * A party that creates software and provides it to others, choosing a build platform and distributing provenance.
 */
export interface SlsaProducer extends SlsaParty {
    /** The build platform this party or component belongs to or uses. */
    build_platform?: SlsaBuildPlatformBuilderId,
}


/**
 * A party that uses software a producer provides, verifying its provenance itself or through a verifier.
 */
export interface SlsaConsumer extends SlsaParty {
}


/**
 * A party that inspects provenance or other attestations and decides whether an artifact is authentic.
 */
export interface SlsaVerifier extends SlsaParty {
    /** The version of each named component of a platform. */
    component_versions?: SlsaComponentVersion[],
    /** The URI that identifies the verifier. */
    verifier_id: string,
}


/**
 * A party that provides software or services to the other roles, such as a package registry's or a build platform's maintainers.
 */
export interface SlsaInfrastructureProvider extends SlsaParty {
}


/**
 * The system that runs builds and records their provenance: the transitive closure of software, hardware, people and organizations trusted to do so. Provenance names it as the builder.
 */
export interface SlsaBuildPlatform {
    /** The version of each named component of a platform. */
    component_versions?: SlsaComponentVersion[],
    /** The URI that identifies the platform and determines its SLSA Build level. */
    builder_id: string,
    /** The highest SLSA Build level the platform's provenance can meet. */
    build_level?: string,
    /** Whether the platform is a hosted service on shared or dedicated infrastructure rather than an individual's workstation. */
    hosted?: boolean,
    /** Dependencies of the platform's orchestrator that do not run inside the build but may affect provenance generation or its guarantees. */
    builder_dependencies?: InTotoResourceDescriptor[],
}


/**
 * The component of a build platform that orchestrates each build and generates its provenance, outside the tenant's control.
 */
export interface SlsaControlPlane {
    /** The build platform this party or component belongs to or uses. */
    build_platform?: SlsaBuildPlatformBuilderId,
}


/**
 * The version of one named component of a platform.
 */
export interface SlsaComponentVersion {
    /** The component's name. */
    component: string,
    /** The component's version string. */
    component_version?: string,
}


/**
 * A distribution platform that resolves package names to immutable package artifacts within an ecosystem.
 */
export interface SlsaPackageRegistry {
    /** The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI. */
    ecosystem?: string,
    /** The URI that identifies the registry. */
    registry_uri: string,
}


/**
 * A unit of software distributed under a package name, which is the primary security boundary SLSA protects. Its artifacts are the outputs of builds.
 */
export interface SlsaPackage {
    /** The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI. */
    ecosystem?: string,
    /** The name consumers use to obtain the package within its ecosystem and registry. */
    package_name: string,
    /** The registry the package is published to. */
    registry?: SlsaPackageRegistryRegistryUri,
    /** The immutable artifacts the package name has resolved to. */
    package_artifacts?: InTotoResourceDescriptor[],
    /** Where a GUAC instance answers queries about the package's dependency and provenance graph. */
    guac_uri?: string,
    /** The SECURITY-INSIGHTS.yml file of the project that produces the package. */
    security_insights_uri?: string,
}


/**
 * The predicate that says how a build platform produced a set of artifacts, so that consumers can verify the build met their expectations and others can rebuild it.
 */
export interface SlsaBuildProvenance extends SlsaPredicate {
    /** The inputs to the build; required at Build L1. */
    build_definition: SlsaBuildDefinition,
    /** What is specific to this execution of the build; required at Build L1. */
    run_details: SlsaRunDetails,
}


/**
 * The inputs to a build, in enough detail to initialize it and begin execution; the builder vouches for their accuracy.
 */
export interface SlsaBuildDefinition {
    /** The URI of the template that says how to run the build and read its parameters and dependencies; required at Build L1. */
    build_type: string,
    /** The inputs under the tenant's control; required at Build L1, complete at Build L3 and verified by consumers. */
    external_parameters: SlsaBuildParameter[],
    /** The inputs the platform sets itself; kept for debugging, incident response and reproduction, and not verified by consumers. */
    internal_parameters?: SlsaBuildParameter[],
    /** The artifacts fetched during the build, as far as the platform knows them; completeness is best effort through Build L3. */
    resolved_dependencies?: InTotoResourceDescriptor[],
    /** Whether the build could reach only the dependencies it declared, with no other network or filesystem access. */
    hermetic?: boolean,
    /** The tool that generated this provenance, named by URI. */
    provenance_generation_tool?: string,
    /** The CI/CD system that coordinated the build, named by URI, where it differs from the builder. */
    pipeline_orchestrator?: string,
}


/**
 * One named input to a build, with a string value.
 */
export interface SlsaBuildParameter {
    /** The parameter's name. */
    parameter_name: string,
    /** The parameter's value. */
    parameter_value?: string,
}


/**
 * What is specific to one execution of a build: the platform that ran it, metadata about the run and its by-products.
 */
export interface SlsaRunDetails {
    /** The build platform that ran the build and is trusted to have written this provenance; required at Build L1. */
    builder: SlsaBuildPlatform,
    /** Metadata about this execution of the build. */
    build_metadata?: SlsaBuildMetadata,
    /** Artifacts the build produced beside its outputs that may help debugging or incident response, such as logs. */
    byproducts?: InTotoResourceDescriptor[],
}


/**
 * Metadata about one execution of a build: its identifier and when it started and finished.
 */
export interface SlsaBuildMetadata {
    /** An identifier for this build invocation, in a format the builder defines; useful for finding its logs. */
    invocation_id?: string,
    /** When the build started. */
    started_on?: string,
    /** When the build finished. */
    finished_on?: string,
}


/**
 * The predicate in which a verifier records that it evaluated artifacts against a policy and the SLSA levels they met, so consumers can rely on the verifier instead of reading every underlying attestation.
 */
export interface SlsaVerificationSummary extends SlsaPredicate {
    /** The URI consumers fetch the artifact from, which the verifier verified it as. */
    resource_uri: string,
    /** The verifier that made this determination. */
    verifier: SlsaVerifier,
    /** When the verification happened. */
    time_verified?: string,
    /** The policy the subject was verified against, by URI and preferably by digest too. */
    policy: SlsaVerificationSummaryPolicy,
    /** Every attestation the verifier consulted, each with a digest; complete when present. */
    input_attestations?: SlsaVerificationSummaryInputAttestation[],
    /** Whether the subject passed the policy. */
    verification_result: string,
    /** The highest level verified in each track, any verified property, and any result of the issuer's own; a level implies the levels below it. */
    verified_levels: string[],
    /** Properties the organization defines for the revision, each prefixed ORG_SOURCE_; ORG_SOURCE_INTERNAL_ marks one not meant for external consumers. */
    organization_properties?: string[],
    /** How many transitive dependencies were verified at each level; absent when the verifier makes no claim about dependencies. */
    dependency_levels?: SlsaDependencyLevelCount[],
    /** The SLSA specification version the verifier applied, as MAJOR.MINOR. */
    slsa_version?: string,
}


/**
 * The number of an artifact's transitive dependencies verified at one level, each counted once per track at its highest level.
 */
export interface SlsaDependencyLevelCount {
    /** The level the dependencies were verified at, or a result of the issuer's own. */
    verified_level: string,
    /** How many dependencies were verified at that level. */
    dependency_count: number,
}


/**
 * The policy a verification summary applied: a resource descriptor that names the policy by URI.
 */
export interface SlsaVerificationSummaryPolicy extends InTotoResourceDescriptor {
}


/**
 * One attestation a verifier consulted: a resource descriptor that carries the attestation's digest.
 */
export interface SlsaVerificationSummaryInputAttestation extends InTotoResourceDescriptor {
}


/**
 * The platform or services that host a source repository and enforce its organization's policies on authentication, authorization and change management.
 */
export interface SlsaSourceControlSystem {
    /** The URI that identifies the source control system. */
    scs_uri: string,
}


/**
 * A self-contained unit that holds a set of files, their revision history and metadata such as branches and tags.
 */
export interface SlsaSourceRepository {
    /** The stable locator the SCS gives the repository. */
    repository_uri: string,
    /** The source control system that hosts the repository. */
    hosted_by?: SlsaSourceControlSystemScsUri,
}


/**
 * A logically immutable snapshot of a repository's tracked files, with its version-control metadata: author, time and parent revisions.
 */
export interface SlsaSourceRevision {
    /** The source repository this belongs to. */
    repository?: SlsaSourceRepositoryRepositoryUri,
    /** The revision identifier the SCS assigns, such as a git commit id or a path- qualified sequence number. */
    revision_id: string,
    /** The identity of the person or automation that authored the revision. */
    authored_by?: string,
    /** When the revision was created. */
    authored_at?: string,
    /** The revisions this one descends from, which together form the change history. */
    parent_revisions?: SlsaSourceRevisionRevisionId[],
    /** The SLSA Source level the SCS asserts for the revision. */
    source_level?: string,
    /** The form of review that approved the revision. */
    review_type?: string,
}


/**
 * A user-friendly name for a revision in a repository, such as main or v1.2.3; reference_type says whether it is a branch or a tag.
 */
export interface SlsaNamedReference {
    /** The source repository this belongs to. */
    repository?: SlsaSourceRepositoryRepositoryUri,
    /** The source revision this refers to. */
    revision?: SlsaSourceRevisionRevisionId,
    /** The kind of named reference, one of this class's descendants. */
    reference_type?: string,
    /** The reference's name, fully qualified in git, such as refs/heads/main. */
    reference_name: string,
    /** Whether the organization has the SCS enforce its technical controls on this reference. */
    protected?: boolean,
}


/**
 * A named reference that moves to track a line of development.
 */
export interface SlsaBranch extends SlsaNamedReference {
}


/**
 * A named reference meant never to move once created.
 */
export interface SlsaTag extends SlsaNamedReference {
}


/**
 * Evidence from an SCS of how a revision came to exist and which technical controls were enforced when it did.
 */
export interface SlsaSourceProvenance extends SlsaPredicate {
    /** The source revision this refers to. */
    revision: SlsaSourceRevisionRevisionId,
    /** The technical controls the SCS enforced when the revision was created, as the organization documents them. */
    controls_enforced?: string[],
}


/**
 * The inventory of every third-party build dependency, direct and transitive, of one artifact version.
 */
export interface SlsaDependencyInventory {
    /** The artifact whose dependencies are inventoried. */
    artifact: InTotoResourceDescriptor,
    /** The dependencies, each as a resource descriptor. */
    dependencies?: InTotoResourceDescriptor[],
    /** The SLSA Dependency level the producer's process meets for this artifact. */
    dependency_level?: string,
}


/**
 * The party that creates and distributes build images; the hosted build platform itself, or a third party in a bring-your-own-image setting.
 */
export interface SlsaBuildImageProducer extends SlsaParty {
}


/**
 * The template a build environment is instantiated from, such as a VM or container image: root filesystem, guest OS and packages, build executor and build agent.
 */
export interface SlsaBuildImage {
    /** The SLSA Build Environment level this meets. */
    build_env_level?: string,
    /** The URI that identifies the image version, such as an OCI reference with its digest. */
    image_uri: string,
    /** The build provenance of the image itself, required at Build Environment L1. */
    provenance?: SlsaBuildProvenance,
    /** The party that created and distributes the image. */
    produced_by?: SlsaBuildImageProducer,
}


/**
 * The digest of one component or state of a build environment, to compare with its reference value.
 */
export interface SlsaMeasurement {
    /** The cryptographic digests of a resource's content, keyed by algorithm. */
    digest?: InTotoDigestSet,
    /** The component or state that was measured, such as the bootloader, guest kernel, build agent or root filesystem. */
    measured_component: string,
}


/**
 * Evidence of the state of a build environment when a build was dispatched to it: the image it came from and the measurements taken at boot.
 */
export interface SlsaBuildEnvironmentAttestation extends SlsaPredicate {
    /** The SLSA Build Environment level this meets. */
    build_env_level?: string,
    /** The immutable identifier of the build execution the environment was assigned to. */
    build_id: string,
    /** The image the environment was instantiated from. */
    build_image?: SlsaBuildImageImageUri,
    /** The measurements of the environment's components taken during boot. */
    measurements?: SlsaMeasurement[],
}


/**
 * The adoption challenges a deployment meets and the strategies it applies, from the study's taxonomy.
 */
export interface SlsaAdoptionMetadata {
    /** The challenge themes that apply. */
    challenges?: string,
    /** The strategy themes applied or recommended. */
    strategies?: string,
}


/**
 * A document that holds SLSA attestations and the parties, platforms, packages, repositories and images they concern.
 */
export interface SlsaDocument {
    /** The attestations, as in-toto statements. */
    attestations?: InTotoStatement[],
    /** The parties, each in its role. */
    parties?: SlsaParty[],
    /** The build platforms. */
    build_platforms?: SlsaBuildPlatform[],
    /** The control planes of the build platforms. */
    control_planes?: SlsaControlPlane[],
    /** The packages. */
    packages?: SlsaPackage[],
    /** The package registries. */
    package_registries?: SlsaPackageRegistry[],
    /** The source control systems. */
    source_control_systems?: SlsaSourceControlSystem[],
    /** The source repositories. */
    source_repositories?: SlsaSourceRepository[],
    /** The source revisions. */
    source_revisions?: SlsaSourceRevision[],
    /** The branches and tags. */
    named_references?: SlsaNamedReference[],
    /** The build images. */
    build_images?: SlsaBuildImage[],
    /** The dependency inventories. */
    dependency_inventories?: SlsaDependencyInventory[],
    /** How the deployment the document describes fares against the adoption study's themes. */
    adoption_metadata?: SlsaAdoptionMetadata,
}



