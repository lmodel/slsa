/**
* SLSA Build Track levels providing increasing supply chain security guarantees for the build process. Higher levels require stronger tamper-resistance and provenance integrity.
*/
export enum BuildLevelEnum {
    
    /** No SLSA requirements. Represents the absence of SLSA guarantees; intended for development or test builds. */
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0",
    /** Provenance exists, showing how the package was built. Prevents mistakes and aids documentation, but is trivial to bypass. */
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1",
    /** Build runs on a hosted platform that generates and signs provenance, deterring tampering after the build. */
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2",
    /** Hardened build platform providing strong guarantees against tampering during the build; requires exploiting a vulnerability to forge provenance. */
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3",
};
/**
* SLSA Source Track levels providing increasing trust in source code provenance and the controls used to create source revisions.
*/
export enum SourceLevelEnum {
    
    /** Source is stored in a version control system, enabling discrete and immutable source revisions for precise consumption. */
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1",
    /** Branch history is preserved and immutable; the SCS generates tamper- resistant source provenance attestations for each new revision. */
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2",
    /** The SCS enforces the organization's technical controls on protected Named References, providing verifiable evidence of those controls. */
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3",
    /** All changes to protected branches require two-party review by trusted persons, resisting insider threats and unilateral changes. */
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4",
};
/**
* SLSA Dependency Track levels for measuring and controlling risk introduced from third-party dependencies.
*/
export enum DependencyLevelEnum {
    
    /** No mitigations to dependency threats. */
    SLSA_DEPENDENCY_LEVEL_0 = "SLSA_DEPENDENCY_LEVEL_0",
    /** An inventory of all build dependencies (direct and transitive) exists. */
    SLSA_DEPENDENCY_LEVEL_1 = "SLSA_DEPENDENCY_LEVEL_1",
    /** All known vulnerabilities in the artifact's dependencies have been triaged before each release. */
    SLSA_DEPENDENCY_LEVEL_2 = "SLSA_DEPENDENCY_LEVEL_2",
    /** All third-party build dependencies are consumed exclusively from locations under the producer's control. */
    SLSA_DEPENDENCY_LEVEL_3 = "SLSA_DEPENDENCY_LEVEL_3",
    /** Proactive defense against upstream attacks; an ingestion policy prevents consumption of compromised dependencies. */
    SLSA_DEPENDENCY_LEVEL_4 = "SLSA_DEPENDENCY_LEVEL_4",
};
/**
* SLSA Build Environment Track levels for validating the integrity of the compute environment executing builds.
*/
export enum BuildEnvLevelEnum {
    
    /** No build environment integrity requirements. */
    SLSA_BUILD_ENV_LEVEL_0 = "SLSA_BUILD_ENV_LEVEL_0",
    /** Signed build image provenance exists, protecting against tampering during build image distribution to the build platform. */
    SLSA_BUILD_ENV_LEVEL_1 = "SLSA_BUILD_ENV_LEVEL_1",
    /** The compute platform attests to the boot-time integrity of the build environment, providing evidence of correct instantiation. */
    SLSA_BUILD_ENV_LEVEL_2 = "SLSA_BUILD_ENV_LEVEL_2",
    /** The build environment runs in a hardware-attested trusted execution environment (TEE), providing runtime integrity guarantees. */
    SLSA_BUILD_ENV_LEVEL_3 = "SLSA_BUILD_ENV_LEVEL_3",
};
/**
* Outcome of a policy verification check on an artifact.
*/
export enum VerificationResultEnum {
    
    /** The artifact satisfied all policy requirements. */
    PASSED = "PASSED",
    /** The artifact did not satisfy one or more policy requirements. */
    FAILED = "FAILED",
};
/**
* A named SLSA result used in Verification Summary Attestations to indicate the verified level of an artifact or its dependencies.
*/
export enum SlsaResultEnum {
    
    /** No SLSA Build guarantees verified. */
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0",
    /** Build Level 1 verified for the artifact. */
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1",
    /** Build Level 2 verified for the artifact. */
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2",
    /** Build Level 3 verified for the artifact. */
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3",
    /** Source Level 1 verified for the artifact. */
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1",
    /** Source Level 2 verified for the artifact. */
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2",
    /** Source Level 3 verified for the artifact. */
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3",
    /** Source Level 4 verified for the artifact. */
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4",
};
/**
* Categories of code-review process applied to a source revision. Captures the forms of two-party review discussed by practitioners (Tamanna et al., 2024, LF.2), including contested alternatives whose security equivalence with standard asynchronous two-party review has not been formally established.
*/
export enum ReviewTypeEnum {
    
    /** Standard two-party review: a change is approved by at least one reviewer who is distinct from the author, where both the author and reviewer are trusted persons as defined by the organization. */
    TWO_PARTY = "TWO_PARTY",
    /** Two developers working simultaneously on the same code at the same workstation or via screen-sharing. Whether this satisfies the trusted-persons two-party review requirement is an open question raised in practitioner discussions (Tamanna et al., 2024, LF.2). */
    PAIR_PROGRAMMING = "PAIR_PROGRAMMING",
    /** Collaborative development with a whole group at once. As with pair programming, formal equivalence to asynchronous two-party review has not been established for SLSA purposes (Tamanna et al., 2024, LF.2). */
    MOB_PROGRAMMING = "MOB_PROGRAMMING",
    /** Review performed entirely by an automated tool or bot, without a second human reviewer. Does not satisfy the SLSA trusted-persons requirement for Source Level 4. */
    AUTOMATED = "AUTOMATED",
};
/**
* The four empirically identified themes of challenges practitioners encounter when deploying SLSA, derived from thematic analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Challenge counts in parentheses reflect total issues associated with each theme.
*/
export enum AdoptionChallengeEnum {
    
    /** (CI — 901 issues) Challenges integrating SLSA into projects: complicated provenance generation including blocking pre-submit jobs, lack of non-build configuration support, and sensitive-data handling risks (CI.1); and intricate ongoing maintenance of required tools including incompatibilities, silent failures, and documentation drift (CI.2). */
    COMPLEX_IMPLEMENTATION = "COMPLEX_IMPLEMENTATION",
    /** (UC — 357 issues) Challenges understanding SLSA documentation: unclear definitions of key terms such as "provenance", "attestation", "hermetic", "hosted", and "non-falsifiable" (UC.1); and lack of clear, ecosystem-specific guidance on how to apply SLSA requirements in practice (UC.2). */
    UNCLEAR_COMMUNICATION = "UNCLEAR_COMMUNICATION",
    /** (LF — 219 issues) Challenges with practical feasibility of SLSA requirements: complexity and lack of standardization in attestation verification tooling, no standardized storage model for attestations, and security concerns about verification accuracy (LF.1); and difficulty implementing two-party review for single-maintainer open-source projects (LF.2). */
    LIMITED_FEASIBILITY = "LIMITED_FEASIBILITY",
    /** (UR — 46 issues) Challenges understanding SLSA's relevance and distinct value: confusion about which attacks SLSA mitigates, how it differs from OpenSSF best practices, and ecosystem-level policy inconsistencies (e.g., npm package naming divergence) that undermine attestation accuracy (UR.1). */
    UNCLEAR_RELEVANCE = "UNCLEAR_RELEVANCE",
};
/**
* The five empirically identified themes of strategies practitioners suggested to overcome SLSA adoption challenges, derived from thematic analysis of 1,523 SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Each strategy theme contains 2–4 sub-strategies (13 total).
*/
export enum AdoptionStrategyEnum {
    
    /** (S1) Enhance SLSA alignment and flexibility: incorporate build-system tracks for more tailored approaches (S1.1); gamify adoption levels so producers aim for higher levels (S1.2); ensure flexibility for diverse organizational and ecosystem needs (S1.3); align SLSA with OpenSSF best practices including SECURITY.md and silver/gold criteria (S1.4). */
    ENHANCE_ALIGNMENT_FLEXIBILITY = "ENHANCE_ALIGNMENT_FLEXIBILITY",
    /** (S2) Provide specific and detailed documentation: enhance docs with clear definitions, standard terms, revised requirements, and patches (S2.1); use negative examples to explain complex concepts and improve website diagrams and navigation (S2.2). */
    PROVIDE_DETAILED_DOCUMENTATION = "PROVIDE_DETAILED_DOCUMENTATION",
    /** (S3) Streamline provenance generation processes: simplify and standardize the generation process via tools and templates to reduce confusion and improve consistency (S3.1); fix semantic-release tool inconsistencies with clear versioning rules and parallel pre-submit job execution (S3.2). */
    STREAMLINE_PROVENANCE_GENERATION = "STREAMLINE_PROVENANCE_GENERATION",
    /** (S4) Improve the SLSA verification process: strengthen verification with better security guarantees and level-determination algorithms (S4.1); implement versioning tagging early to facilitate progress tracking (S4.2); enhance framework tooling with more downstream signaling information (S4.3). */
    IMPROVE_VERIFICATION_PROCESS = "IMPROVE_VERIFICATION_PROCESS",
    /** (S5) Collaborate with the community: foster engagement by aligning SLSA verification with industry standards and providing guidance for novice users (S5.1); promote learning and knowledge-sharing, including cross-project collaboration for single-maintainer projects (S5.2). */
    COLLABORATE_WITH_COMMUNITY = "COLLABORATE_WITH_COMMUNITY",
};


/**
 * Root wrapper for any SLSA attestation payload. Acts as the entry point for schema validation and tools.
 */
export interface SlsaDocument {
    /** All inputs to the build, sufficient to initialise and reproduce it. REQUIRED at SLSA Build L1. */
    buildDefinition: BuildDefinition,
    /** Details specific to this particular execution of the build, including builder identity and metadata. REQUIRED at SLSA Build L1. */
    runDetails: RunDetails,
    /** Identifies the entity that performed the verification. */
    verifier: Verifier,
    /** Whether the artifact passed or failed policy verification. */
    verificationResult: string,
    /** The highest verified SLSA level for each applicable track (not including transitive dependencies). At most one level per track. Implies all levels below it within the same track. */
    verifiedLevels: string,
    /** Optional structured metadata recording the SLSA adoption challenges and mitigation strategies relevant to this attestation context. Derived from empirical analysis of SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Intended for use by framework authors, practitioners, and tooling that tracks adoption progress alongside attestation payloads. */
    adoptionMetadata?: AdoptionMetadata,
}


/**
 * A set of cryptographic digests for an artifact, keyed by algorithm name (e.g., "sha256", "gitCommit"). Provides enough information for consumers to verify artifact integrity using their preferred algorithm.
 */
export interface DigestSet {
    /** Lowercase hex-encoded SHA-256 digest of the artifact. */
    sha256?: string,
    /** Lowercase hex-encoded SHA-512 digest of the artifact. */
    sha512?: string,
    /** Git commit SHA identifying a source-backed artifact. */
    gitCommit?: string,
}


/**
 * A reference to a software artifact including its location, digest, and optional metadata. Used throughout SLSA to describe inputs, outputs, and dependencies in provenance attestations.
 */
export interface ResourceDescriptor {
    /** A URI uniquely identifying a resource, such as a package URL (purl), git repository URL, or OCI image reference. */
    uri?: string,
    /** Set of cryptographic digests of a resource's content used for integrity verification. */
    digest?: DigestSet,
    /** A local name for a resource within the context of an attestation, or the name of a package, producer, or party. */
    name?: string,
    /** URI from which a resource can be downloaded, if different from its identifying URI. */
    downloadLocation?: string,
    /** IANA media type of a resource's content (e.g., "application/octet-stream", "application/vnd.oci.image.manifest.v1+json"). */
    mediaType?: string,
    /** Arbitrary vendor-specific key-value annotations. */
    annotations?: string[],
}


/**
 * The middle layer of an in-toto software attestation (Statement v1). Binds an authenticated predicate to one or more subject artifacts, allowing predicate-agnostic processing and storage.
 */
export interface Statement {
    /** Always "https://in-toto.io/Statement/v1". Identifies the in-toto statement schema version and namespace. */
    _type: string,
    /** The set of software artifacts to which a predicate applies. Each entry MUST contain a digest. */
    subject: ResourceDescriptor[],
    /** URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation). */
    predicateType: string,
    /** The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType. */
    predicate?: string,
    /** URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1). */
    attestationStorageUri?: string,
    /** URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., "https://github.com/sigstore/cosign", "https://github.com/notaryproject/notation"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI. */
    signingTool?: string,
    /** URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., "https://rekor.sigstore.dev/api/v1/log/entries/24296fb..."). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key. */
    sigstoreLogEntry?: string,
}


/**
 * An attestation predicate (predicateType "https://slsa.dev/provenance/v1") that describes how a set of output artifacts was produced by a build platform. Consumers use this to verify artifact authenticity and trace artifacts back through the supply chain.
 */
export interface BuildProvenance extends Statement {
    /** All inputs to the build, sufficient to initialise and reproduce it. REQUIRED at SLSA Build L1. */
    buildDefinition: BuildDefinition,
    /** Details specific to this particular execution of the build, including builder identity and metadata. REQUIRED at SLSA Build L1. */
    runDetails: RunDetails,
}


/**
 * Describes all inputs to the build in enough detail to initialise and reproduce the build. The accuracy and completeness are implied by the builder identified in runDetails.
 */
export interface BuildDefinition {
    /** URI identifying the template for how to perform the build and how to interpret the parameters and dependencies. SHOULD resolve to a human-readable specification. REQUIRED at SLSA Build L1. */
    buildType: string,
    /** Top-level, independent inputs under external (tenant or user) control. MUST be complete at SLSA Build L3. Stored as a JSON object. Verifiers SHOULD reject unrecognized fields. */
    externalParameters?: string,
    /** Parameters set internally by the build platform. Intended for debugging, incident response, and enabling reproducible builds. Stored as a JSON object; need not be verified by consumers. */
    internalParameters?: string,
    /** Unordered collection of artifacts needed at build time (config files, source, build tools). Completeness is best effort through SLSA Build L3. */
    resolvedDependencies?: ResourceDescriptor[],
    /** Whether all build inputs are fully isolated to the dependencies declared in resolvedDependencies, with no network access or filesystem references outside the explicit build graph. Hermetic builds are a stated requirement for SLSA Build L3; practitioners identified this as one of the most commonly cited implementation barriers, with over 50% of surveyed practitioners finding hermetic build requirements difficult to implement (Tamanna et al., 2024, CI.1). */
    hermeticBuild?: boolean,
    /** URI or name of the tool used to generate provenance for this build (e.g., "https://github.com/slsa-framework/slsa-github-generator"). Standardizing this field across builds reduces confusion, supports reproducibility verification, and aligns with the recommended strategy of simplifying and standardizing provenance generation processes (Tamanna et al., 2024, S3.1). */
    provenanceGenerationTool?: string,
    /** URI or name of the CI/CD pipeline orchestration system that coordinated this build (e.g., "https://tekton.dev", "https://github.com/features/actions", "https://jenkins.io"). In the SSF reference architecture this is the Build Service layer that feeds the Artifact Registry. Providing this field helps distinguish the orchestrator from the provenance-generating builder identity (builder.id) in complex deployments where they differ (e.g., a Tekton Pipeline running on Google Cloud Pipelines). */
    pipelineOrchestrator?: string,
}


/**
 * Details specific to this particular execution of the build, including the trusted builder and optional run-level metadata.
 */
export interface RunDetails {
    /** Identifies the build platform that executed the build and is trusted to have correctly generated this provenance. REQUIRED at SLSA Build L1. */
    builder: Builder,
    /** Metadata about this particular build execution. */
    buildMetadata?: BuildMetadata,
    /** Additional artifacts produced during the build that are NOT the primary output but may be useful for debugging or incident response (e.g., build logs, intermediate artifacts). */
    byproducts?: ResourceDescriptor[],
}


/**
 * Represents the transitive closure of all software, hardware, and entities trusted to faithfully execute the build and record provenance. The builder.id is the primary basis for determining SLSA Build Level.
 */
export interface Builder {
    /** A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers. */
    id: string,
    /** Dependencies used by the control plane orchestrator that are not run within the build workload but may affect provenance generation or security guarantees. */
    builderDependencies?: ResourceDescriptor[],
    /** Map of component names to their version strings, represented as a JSON object (string → string). */
    version?: string,
    /** A semantic version tag (e.g., "v1.2.3") assigned to the builder or the produced artifact at the time of the build. Practitioners recommended implementing versioning tagging early in SLSA framework deployment to facilitate progress tracking, reduce maintenance confusion from breaking changes, and enable more straightforward verification (Tamanna et al., 2024, S4.2). */
    versionTag?: string,
}


/**
 * Metadata about a specific invocation of the build, including timing information and a unique build identifier for log correlation.
 */
export interface BuildMetadata {
    /** A globally unique identifier for a build invocation, useful for finding associated logs. Format defined by builder.id; treated as opaque and case-sensitive. The value SHOULD be globally unique. */
    invocationId?: string,
    /** Timestamp (RFC 3339) of when the build started. */
    startedOn?: string,
    /** Timestamp (RFC 3339) of when the build completed. */
    finishedOn?: string,
}


/**
 * An attestation predicate (predicateType "https://slsa.dev/verification_summary/v1") issued by a trusted verifier stating that one or more artifacts were evaluated against a policy and the SLSA level at which they were verified. Allows consumers to trust the verifier's determination without needing access to all underlying provenance.
 */
export interface VerificationSummaryAttestation extends Statement {
    /** Identifies the entity that performed the verification. */
    verifier: Verifier,
    /** Timestamp (RFC 3339) indicating when the verification occurred. */
    timeVerified?: string,
    /** URI identifying the resource associated with the artifact being verified. SHOULD be the URI from which the consumer fetches the artifact. */
    resourceUri: string,
    /** The policy the subject was verified against. MUST contain a URI; SHOULD contain a digest identifying the exact policy version. */
    policy: ResourceDescriptor,
    /** All attestations consulted during verification. If non-empty, MUST be complete — it MUST list every attestation used. Each entry MUST contain a digest; SHOULD contain a URI. */
    inputAttestations?: ResourceDescriptor[],
    /** Whether the artifact passed or failed policy verification. */
    verificationResult: string,
    /** The highest verified SLSA level for each applicable track (not including transitive dependencies). At most one level per track. Implies all levels below it within the same track. */
    verifiedLevels: string,
    /** Map from SlsaResult to count of transitive dependencies verified at that level (JSON object string). Allows policy engines to enforce minimum levels on the full dependency graph. */
    dependencyLevels?: string,
    /** Version of the SLSA specification used during verification, in MAJOR.MINOR format (e.g., "1.0"). */
    slsaVersion?: string,
}


/**
 * The entity that performed verification of an artifact and issued a Verification Summary Attestation. Consumers MUST accept only specific (signer, verifier) pairs.
 */
export interface Verifier {
    /** A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers. */
    id: string,
    /** Map of component names to their version strings, represented as a JSON object (string → string). */
    version?: string,
}


/**
 * A party who creates software and provides it to others. Responsible for choosing an appropriate build platform, following a consistent build process, and distributing provenance to consumers.
 */
export interface Producer {
    /** A local name for a resource within the context of an attestation, or the name of a package, producer, or party. */
    name?: string,
    /** URI of the build platform chosen to produce artifacts. */
    buildPlatformId?: string,
}


/**
 * A party who uses software provided by a producer. May verify provenance directly or delegate that responsibility to a separate verifier.
 */
export interface Consumer {
}


/**
 * A party who provides software or services to other roles in the supply chain, such as a package registry maintainer or build platform operator.
 */
export interface InfrastructureProvider {
}


/**
 * The infrastructure (software, hardware, people, and organizations) used to transform source code into package artifacts. Responsible for provenance generation and isolation between tenant builds. Often a hosted, multi-tenant build service.
 */
export interface BuildPlatform {
    /** A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers. */
    id: string,
    /** The SLSA Build Level this platform is capable of producing, as determined by its provenance generation and isolation guarantees. */
    buildLevel?: string,
    /** True if this is a hosted (multi-tenant) platform running on shared or dedicated infrastructure, rather than an individual's workstation. Required for SLSA Build L2+. */
    isHosted?: boolean,
}


/**
 * The build platform component that orchestrates each independent build execution and generates provenance. Managed by an admin and trusted to be outside of tenant control. Responsible for generating and signing provenance at SLSA Build L2+.
 */
export interface ControlPlane {
}


/**
 * An identifiable unit of software intended for distribution. In the SLSA model, a package is always the output of a build process (which may be a no-op). The package name is the primary security boundary within a package ecosystem.
 */
export interface Package {
    /** A local name for a resource within the context of an attestation, or the name of a package, producer, or party. */
    name?: string,
    /** The package ecosystem (e.g., "PyPA", "npm", "OCI", "cargo") governing distribution conventions for this package. */
    ecosystem?: string,
    /** URI of the package registry where a package is published and from which consumers resolve the package name to an artifact. */
    registry?: string,
    /** A specific immutable package artifact or the artifact whose dependency inventory is recorded. */
    artifact?: ResourceDescriptor,
}


/**
 * A self-contained unit that holds the content and complete revision history for a set of files, along with metadata such as branches and tags. Hosted and governed by a Source Control System.
 */
export interface SourceRepository {
    /** Canonical URI that uniquely identifies this source repository. */
    id: string,
    /** Human-readable description of a repository's purpose or a resource. */
    description?: string,
    /** The SLSA Source Level achieved or verified for a source repository or revision. */
    sourceLevel?: string,
}


/**
 * A specific, logically immutable snapshot of a source repository's tracked files. Uniquely identified by a revision identifier such as a cryptographic hash (e.g., git commit SHA) or a path-qualified sequential number (e.g., SVN).
 */
export interface SourceRevision {
    /** Immutable identifier for a source revision (e.g., git commit SHA, path-qualified sequential number). */
    revisionId: string,
    /** The source repository that contains this revision. */
    repository?: SourceRepository,
    /** Identity of the person or automation that authored this revision (e.g., an email address or platform username). */
    author?: string,
    /** Timestamp (RFC 3339) of when this source revision was created. */
    timestamp?: string,
    /** Revision IDs of the parent revision(s), forming the directed acyclic graph of change history. */
    parentRevisions?: string[],
    /** The type of human or automated review process used to approve this source revision. Captures the contested forms of two-party review — including pair programming and mob programming — whose security equivalence to standard asynchronous two-party review is an open question identified in practitioner community discussions (Tamanna et al., 2024, LF.2). See ReviewTypeEnum for defined values. */
    reviewType?: string,
}


/**
 * An attestation describing how a source revision came to exist: where it was hosted, when it was generated, what process was used, who the contributors were, and which technical controls were enforced by the Source Control System.
 */
export interface SourceProvenanceAttestation extends Statement {
    /** The source revision that this attestation describes. */
    revision?: SourceRevision,
    /** The SLSA Source Level achieved or verified for a source repository or revision. */
    sourceLevel?: string,
    /** Technical controls actively enforced by the Source Control System when this revision was created (e.g., "two-party review", "branch protection", "status checks"). */
    controlsEnforced?: string[],
}


/**
 * A comprehensive inventory of all third-party build dependencies for an artifact, capturing direct and transitive dependencies. Supports vulnerability management and incident response.
 */
export interface DependencyInventory {
    /** A specific immutable package artifact or the artifact whose dependency inventory is recorded. */
    artifact?: ResourceDescriptor,
    /** All third-party build dependencies (direct and transitive) for an artifact version, identified by URI and digest. */
    dependencies?: ResourceDescriptor[],
    /** The SLSA Dependency Level that this inventory and associated triage process supports. */
    dependencyLevel?: string,
}


/**
 * The template for a build environment, such as a VM or container image. Comprises the root filesystem, pre-installed guest OS and packages, the build executor, and the build agent. Created by a build image producer and consumed by the hosted build platform.
 */
export interface BuildImage {
    /** URI uniquely identifying this build image version (e.g., an OCI image reference with digest). */
    id: string,
    /** SLSA Build Provenance for a build image, describing how the image itself was produced. Required for SLSA Build Environment L1+. */
    provenance?: BuildProvenance,
    /** The SLSA Build Environment Level supported or represented, reflecting the strength of the integrity guarantees provided. */
    buildEnvLevel?: string,
}


/**
 * An attestation describing the integrity of a build environment at the time a specific build was dispatched and executed. Used to verify that a build ran in the expected, untampered environment.
 */
export interface BuildEnvironmentAttestation extends Statement {
    /** An immutable identifier uniquely assigned to a build execution (e.g., a UUID). Links a BuildEnvironmentAttestation to the corresponding build provenance. */
    buildId: string,
    /** The build image from which the build environment was instantiated. */
    buildImage?: BuildImage,
    /** Cryptographic measurements (hashes) of build environment components captured during boot and initialization, used to verify integrity against known-good reference values. */
    measurements?: string[],
    /** The SLSA Build Environment Level supported or represented, reflecting the strength of the integrity guarantees provided. */
    buildEnvLevel?: string,
}


/**
 * Optional structured metadata capturing the SLSA adoption challenges and mitigation strategies relevant to a given attestation or deployment context. Derived from empirical analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Use this class to document which challenge themes apply to the current deployment and which strategies are being employed or recommended. Attach via the adoptionMetadata slot on SlsaDocument.
 */
export interface AdoptionMetadata {
    /** The adoption challenge themes that apply to this attestation or deployment context, drawn from the empirically identified challenge taxonomy (Tamanna et al., 2024, arXiv:2409.05014). */
    challenges?: string,
    /** The mitigation strategies being employed or recommended in this attestation or deployment context, drawn from the empirically identified strategy taxonomy (Tamanna et al., 2024, arXiv:2409.05014). */
    strategies?: string,
}



