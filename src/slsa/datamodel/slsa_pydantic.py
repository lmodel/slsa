from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'slsa',
     'default_range': 'string',
     'description': 'Electronic (LinkML) Version of Supply-chain Levels for '
                    'Software Artifacts (SLSA)',
     'id': 'https://w3id.org/lmodel/slsa',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'slsa',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'slsa': {'prefix_prefix': 'slsa',
                           'prefix_reference': 'https://w3id.org/lmodel/slsa/'}},
     'see_also': ['https://lmodel.github.io/slsa',
                  'https://slsa.dev/spec/v1.2/',
                  'https://arxiv.org/abs/2409.05014',
                  'https://openssf.org/technical-initiatives/software-supply-chain/'],
     'source': 'https://slsa.dev/spec/v1.0',
     'source_file': 'src/slsa/schema/slsa.yaml',
     'subsets': {'slsa_adoption_study': {'description': 'Slots, classes, and enums '
                                                        'derived from empirical '
                                                        'analysis of SLSA adoption '
                                                        'challenges and '
                                                        'strategies. Based on '
                                                        'thematic analysis of '
                                                        '1,523 SLSA-related GitHub '
                                                        'issues from 233 '
                                                        'repositories (Tamanna et '
                                                        'al., 2024, '
                                                        'arXiv:2409.05014). These '
                                                        'elements model challenge '
                                                        'themes and mitigation '
                                                        'strategies to support '
                                                        'structured documentation '
                                                        'of adoption status '
                                                        'alongside attestation '
                                                        'payloads.',
                                         'from_schema': 'https://w3id.org/lmodel/slsa',
                                         'name': 'slsa_adoption_study'},
                 'slsa_build_env_track': {'description': 'Slots and classes '
                                                         'related to the SLSA '
                                                         'Build Environment Track, '
                                                         'which measures the '
                                                         'integrity of the compute '
                                                         'environment running '
                                                         'builds.',
                                          'from_schema': 'https://w3id.org/lmodel/slsa',
                                          'name': 'slsa_build_env_track'},
                 'slsa_build_track': {'description': 'Slots and classes related to '
                                                     'the SLSA Build Track, which '
                                                     'measures the trustworthiness '
                                                     'of the build process and '
                                                     'resulting provenance.',
                                      'from_schema': 'https://w3id.org/lmodel/slsa',
                                      'name': 'slsa_build_track'},
                 'slsa_dependency_track': {'description': 'Slots and classes '
                                                          'related to the SLSA '
                                                          'Dependency Track, which '
                                                          "measures a producer's "
                                                          'ability to manage risk '
                                                          'from third-party '
                                                          'dependencies.',
                                           'from_schema': 'https://w3id.org/lmodel/slsa',
                                           'name': 'slsa_dependency_track'},
                 'slsa_source_track': {'description': 'Slots and classes related '
                                                      'to the SLSA Source Track, '
                                                      'which measures the '
                                                      'trustworthiness of how '
                                                      'source revisions are '
                                                      'created and managed.',
                                       'from_schema': 'https://w3id.org/lmodel/slsa',
                                       'name': 'slsa_source_track'},
                 'slsa_ssf': {'description': 'Slots and classes related to the '
                                             'CNCF TAG-Security Secure Software '
                                             'Factory (SSF) reference architecture '
                                             'and the OpenSSF Supply Chain '
                                             'Integrity Working Group ecosystem. '
                                             'The SSF defines a standard pipeline '
                                             'pattern — Version Control, CI Build '
                                             'Service, Artifact Registry, Signing '
                                             'Service, and Policy Engine — that '
                                             'implements SLSA requirements '
                                             'end-to-end. See: '
                                             'https://github.com/cncf/tag-security/tree/main/supply-chain-security/secure-software-factory '
                                             'and '
                                             'https://openssf.org/technical-initiatives/software-supply-chain/',
                              'from_schema': 'https://w3id.org/lmodel/slsa',
                              'name': 'slsa_ssf'}},
     'title': 'slsa'} )

class BuildLevelEnum(str, Enum):
    """
    SLSA Build Track levels providing increasing supply chain security guarantees for the build process. Higher levels require stronger tamper-resistance and provenance integrity.
    """
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0"
    """
    No SLSA requirements. Represents the absence of SLSA guarantees; intended for development or test builds.
    """
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1"
    """
    Provenance exists, showing how the package was built. Prevents mistakes and aids documentation, but is trivial to bypass.
    """
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2"
    """
    Build runs on a hosted platform that generates and signs provenance, deterring tampering after the build.
    """
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3"
    """
    Hardened build platform providing strong guarantees against tampering during the build; requires exploiting a vulnerability to forge provenance.
    """


class SourceLevelEnum(str, Enum):
    """
    SLSA Source Track levels providing increasing trust in source code provenance and the controls used to create source revisions.
    """
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1"
    """
    Source is stored in a version control system, enabling discrete and immutable source revisions for precise consumption.
    """
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2"
    """
    Branch history is preserved and immutable; the SCS generates tamper- resistant source provenance attestations for each new revision.
    """
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3"
    """
    The SCS enforces the organization's technical controls on protected Named References, providing verifiable evidence of those controls.
    """
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4"
    """
    All changes to protected branches require two-party review by trusted persons, resisting insider threats and unilateral changes.
    """


class DependencyLevelEnum(str, Enum):
    """
    SLSA Dependency Track levels for measuring and controlling risk introduced from third-party dependencies.
    """
    SLSA_DEPENDENCY_LEVEL_0 = "SLSA_DEPENDENCY_LEVEL_0"
    """
    No mitigations to dependency threats.
    """
    SLSA_DEPENDENCY_LEVEL_1 = "SLSA_DEPENDENCY_LEVEL_1"
    """
    An inventory of all build dependencies (direct and transitive) exists.
    """
    SLSA_DEPENDENCY_LEVEL_2 = "SLSA_DEPENDENCY_LEVEL_2"
    """
    All known vulnerabilities in the artifact's dependencies have been triaged before each release.
    """
    SLSA_DEPENDENCY_LEVEL_3 = "SLSA_DEPENDENCY_LEVEL_3"
    """
    All third-party build dependencies are consumed exclusively from locations under the producer's control.
    """
    SLSA_DEPENDENCY_LEVEL_4 = "SLSA_DEPENDENCY_LEVEL_4"
    """
    Proactive defense against upstream attacks; an ingestion policy prevents consumption of compromised dependencies.
    """


class BuildEnvLevelEnum(str, Enum):
    """
    SLSA Build Environment Track levels for validating the integrity of the compute environment executing builds.
    """
    SLSA_BUILD_ENV_LEVEL_0 = "SLSA_BUILD_ENV_LEVEL_0"
    """
    No build environment integrity requirements.
    """
    SLSA_BUILD_ENV_LEVEL_1 = "SLSA_BUILD_ENV_LEVEL_1"
    """
    Signed build image provenance exists, protecting against tampering during build image distribution to the build platform.
    """
    SLSA_BUILD_ENV_LEVEL_2 = "SLSA_BUILD_ENV_LEVEL_2"
    """
    The compute platform attests to the boot-time integrity of the build environment, providing evidence of correct instantiation.
    """
    SLSA_BUILD_ENV_LEVEL_3 = "SLSA_BUILD_ENV_LEVEL_3"
    """
    The build environment runs in a hardware-attested trusted execution environment (TEE), providing runtime integrity guarantees.
    """


class VerificationResultEnum(str, Enum):
    """
    Outcome of a policy verification check on an artifact.
    """
    PASSED = "PASSED"
    """
    The artifact satisfied all policy requirements.
    """
    FAILED = "FAILED"
    """
    The artifact did not satisfy one or more policy requirements.
    """


class SlsaResultEnum(str, Enum):
    """
    A named SLSA result used in Verification Summary Attestations to indicate the verified level of an artifact or its dependencies.
    """
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0"
    """
    No SLSA Build guarantees verified.
    """
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1"
    """
    Build Level 1 verified for the artifact.
    """
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2"
    """
    Build Level 2 verified for the artifact.
    """
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3"
    """
    Build Level 3 verified for the artifact.
    """
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1"
    """
    Source Level 1 verified for the artifact.
    """
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2"
    """
    Source Level 2 verified for the artifact.
    """
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3"
    """
    Source Level 3 verified for the artifact.
    """
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4"
    """
    Source Level 4 verified for the artifact.
    """


class ReviewTypeEnum(str, Enum):
    """
    Categories of code-review process applied to a source revision. Captures the forms of two-party review discussed by practitioners (Tamanna et al., 2024, LF.2), including contested alternatives whose security equivalence with standard asynchronous two-party review has not been formally established.
    """
    TWO_PARTY = "TWO_PARTY"
    """
    Standard two-party review: a change is approved by at least one reviewer who is distinct from the author, where both the author and reviewer are trusted persons as defined by the organization.
    """
    PAIR_PROGRAMMING = "PAIR_PROGRAMMING"
    """
    Two developers working simultaneously on the same code at the same workstation or via screen-sharing. Whether this satisfies the trusted-persons two-party review requirement is an open question raised in practitioner discussions (Tamanna et al., 2024, LF.2).
    """
    MOB_PROGRAMMING = "MOB_PROGRAMMING"
    """
    Collaborative development with a whole group at once. As with pair programming, formal equivalence to asynchronous two-party review has not been established for SLSA purposes (Tamanna et al., 2024, LF.2).
    """
    AUTOMATED = "AUTOMATED"
    """
    Review performed entirely by an automated tool or bot, without a second human reviewer. Does not satisfy the SLSA trusted-persons requirement for Source Level 4.
    """


class AdoptionChallengeEnum(str, Enum):
    """
    The four empirically identified themes of challenges practitioners encounter when deploying SLSA, derived from thematic analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Challenge counts in parentheses reflect total issues associated with each theme.
    """
    COMPLEX_IMPLEMENTATION = "COMPLEX_IMPLEMENTATION"
    """
    (CI — 901 issues) Challenges integrating SLSA into projects: complicated provenance generation including blocking pre-submit jobs, lack of non-build configuration support, and sensitive-data handling risks (CI.1); and intricate ongoing maintenance of required tools including incompatibilities, silent failures, and documentation drift (CI.2).
    """
    UNCLEAR_COMMUNICATION = "UNCLEAR_COMMUNICATION"
    """
    (UC — 357 issues) Challenges understanding SLSA documentation: unclear definitions of key terms such as "provenance", "attestation", "hermetic", "hosted", and "non-falsifiable" (UC.1); and lack of clear, ecosystem-specific guidance on how to apply SLSA requirements in practice (UC.2).
    """
    LIMITED_FEASIBILITY = "LIMITED_FEASIBILITY"
    """
    (LF — 219 issues) Challenges with practical feasibility of SLSA requirements: complexity and lack of standardization in attestation verification tooling, no standardized storage model for attestations, and security concerns about verification accuracy (LF.1); and difficulty implementing two-party review for single-maintainer open-source projects (LF.2).
    """
    UNCLEAR_RELEVANCE = "UNCLEAR_RELEVANCE"
    """
    (UR — 46 issues) Challenges understanding SLSA's relevance and distinct value: confusion about which attacks SLSA mitigates, how it differs from OpenSSF best practices, and ecosystem-level policy inconsistencies (e.g., npm package naming divergence) that undermine attestation accuracy (UR.1).
    """


class AdoptionStrategyEnum(str, Enum):
    """
    The five empirically identified themes of strategies practitioners suggested to overcome SLSA adoption challenges, derived from thematic analysis of 1,523 SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Each strategy theme contains 2–4 sub-strategies (13 total).
    """
    ENHANCE_ALIGNMENT_FLEXIBILITY = "ENHANCE_ALIGNMENT_FLEXIBILITY"
    """
    (S1) Enhance SLSA alignment and flexibility: incorporate build-system tracks for more tailored approaches (S1.1); gamify adoption levels so producers aim for higher levels (S1.2); ensure flexibility for diverse organizational and ecosystem needs (S1.3); align SLSA with OpenSSF best practices including SECURITY.md and silver/gold criteria (S1.4).
    """
    PROVIDE_DETAILED_DOCUMENTATION = "PROVIDE_DETAILED_DOCUMENTATION"
    """
    (S2) Provide specific and detailed documentation: enhance docs with clear definitions, standard terms, revised requirements, and patches (S2.1); use negative examples to explain complex concepts and improve website diagrams and navigation (S2.2).
    """
    STREAMLINE_PROVENANCE_GENERATION = "STREAMLINE_PROVENANCE_GENERATION"
    """
    (S3) Streamline provenance generation processes: simplify and standardize the generation process via tools and templates to reduce confusion and improve consistency (S3.1); fix semantic-release tool inconsistencies with clear versioning rules and parallel pre-submit job execution (S3.2).
    """
    IMPROVE_VERIFICATION_PROCESS = "IMPROVE_VERIFICATION_PROCESS"
    """
    (S4) Improve the SLSA verification process: strengthen verification with better security guarantees and level-determination algorithms (S4.1); implement versioning tagging early to facilitate progress tracking (S4.2); enhance framework tooling with more downstream signaling information (S4.3).
    """
    COLLABORATE_WITH_COMMUNITY = "COLLABORATE_WITH_COMMUNITY"
    """
    (S5) Collaborate with the community: foster engagement by aligning SLSA verification with industry standards and providing guidance for novice users (S5.1); promote learning and knowledge-sharing, including cross-project collaboration for single-maintainer projects (S5.2).
    """



class SlsaDocument(ConfiguredBaseModel):
    """
    Root wrapper for any SLSA attestation payload. Acts as the entry point for schema validation and tools.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track'],
         'tree_root': True})

    buildDefinition: BuildDefinition = Field(default=..., description="""All inputs to the build, sufficient to initialise and reproduce it. REQUIRED at SLSA Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'BuildProvenance'],
         'in_subset': ['slsa_build_track']} })
    runDetails: RunDetails = Field(default=..., description="""Details specific to this particular execution of the build, including builder identity and metadata. REQUIRED at SLSA Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'BuildProvenance'],
         'in_subset': ['slsa_build_track']} })
    verifier: Verifier = Field(default=..., description="""Identifies the entity that performed the verification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    verificationResult: VerificationResultEnum = Field(default=..., description="""Whether the artifact passed or failed policy verification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    verifiedLevels: list[SlsaResultEnum] = Field(default=..., description="""The highest verified SLSA level for each applicable track (not including transitive dependencies). At most one level per track. Implies all levels below it within the same track.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    adoptionMetadata: Optional[AdoptionMetadata] = Field(default=None, description="""Optional structured metadata recording the SLSA adoption challenges and mitigation strategies relevant to this attestation context. Derived from empirical analysis of SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Intended for use by framework authors, practitioners, and tooling that tracks adoption progress alongside attestation payloads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument'], 'in_subset': ['slsa_adoption_study']} })


class DigestSet(ConfiguredBaseModel):
    """
    A set of cryptographic digests for an artifact, keyed by algorithm name (e.g., \"sha256\", \"gitCommit\"). Provides enough information for consumers to verify artifact integrity using their preferred algorithm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    sha256: Optional[str] = Field(default=None, description="""Lowercase hex-encoded SHA-256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DigestSet'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    sha512: Optional[str] = Field(default=None, description="""Lowercase hex-encoded SHA-512 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DigestSet'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    gitCommit: Optional[str] = Field(default=None, description="""Git commit SHA identifying a source-backed artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DigestSet'],
         'in_subset': ['slsa_source_track', 'slsa_build_track']} })


class ResourceDescriptor(ConfiguredBaseModel):
    """
    A reference to a software artifact including its location, digest, and optional metadata. Used throughout SLSA to describe inputs, outputs, and dependencies in provenance attestations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']})

    uri: Optional[str] = Field(default=None, description="""A URI uniquely identifying a resource, such as a package URL (purl), git repository URL, or OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    digest: Optional[DigestSet] = Field(default=None, description="""Set of cryptographic digests of a resource's content used for integrity verification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    name: Optional[str] = Field(default=None, description="""A local name for a resource within the context of an attestation, or the name of a package, producer, or party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor', 'Producer', 'Package'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track']} })
    downloadLocation: Optional[str] = Field(default=None, description="""URI from which a resource can be downloaded, if different from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track']} })
    mediaType: Optional[str] = Field(default=None, description="""IANA media type of a resource's content (e.g., \"application/octet-stream\", \"application/vnd.oci.image.manifest.v1+json\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor'],
         'in_subset': ['slsa_build_track', 'slsa_build_env_track']} })
    annotations: Optional[list[str]] = Field(default=None, description="""Arbitrary vendor-specific key-value annotations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track']} })


class Statement(ConfiguredBaseModel):
    """
    The middle layer of an in-toto software attestation (Statement v1). Binds an authenticated predicate to one or more subject artifacts, allowing predicate-agnostic processing and storage.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track'],
         'notes': ['Terminology clarity (Tamanna et al., 2024, UC.1): Practitioners '
                   'report widespread confusion between "attestation" and '
                   '"provenance". An attestation is this signed Statement wrapper; '
                   'provenance is the specific BuildProvenance predicate payload. '
                   'Documenting this distinction addresses the most frequently cited '
                   'terminology barrier.',
                   'Attestation storage gap (Tamanna et al., 2024, LF.1): No '
                   'standardized location for publishing signed attestations was '
                   'defined in SLSA v1.0. Sigstore and VCS-embedded storage are two '
                   'common approaches. Use the attestationStorageUri slot to record '
                   'where this statement is stored.']})

    type: str = Field(default=..., alias="_type", description="""Always \"https://in-toto.io/Statement/v1\". Identifies the in-toto statement schema version and namespace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    subject: list[ResourceDescriptor] = Field(default=..., description="""The set of software artifacts to which a predicate applies. Each entry MUST contain a digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicateType: str = Field(default=..., description="""URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicate: Optional[str] = Field(default=None, description="""The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    attestationStorageUri: Optional[str] = Field(default=None, description="""URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_env_track',
                       'slsa_adoption_study']} })
    signingTool: Optional[str] = Field(default=None, description="""URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., \"https://github.com/sigstore/cosign\", \"https://github.com/notaryproject/notation\"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })
    sigstoreLogEntry: Optional[str] = Field(default=None, description="""URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., \"https://rekor.sigstore.dev/api/v1/log/entries/24296fb...\"). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })


class BuildProvenance(Statement):
    """
    An attestation predicate (predicateType \"https://slsa.dev/provenance/v1\") that describes how a set of output artifacts was produced by a build platform. Consumers use this to verify artifact authenticity and trace artifacts back through the supply chain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track'],
         'notes': ['Top adoption challenge (Tamanna et al., 2024, CI.1 — 901 issues): '
                   'Generating valid provenance is the highest-volume challenge theme '
                   'in practitioner GitHub issues. Key sub-challenges include the '
                   'blocking nature of check-verifier pre-submit jobs, lack of support '
                   'for non-build configurations (e.g., GoReleaser publish-only '
                   'steps), laborious multi-build script setup, and risk of leaking '
                   'credentials or other sensitive data in externalParameters.']})

    buildDefinition: BuildDefinition = Field(default=..., description="""All inputs to the build, sufficient to initialise and reproduce it. REQUIRED at SLSA Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'BuildProvenance'],
         'in_subset': ['slsa_build_track']} })
    runDetails: RunDetails = Field(default=..., description="""Details specific to this particular execution of the build, including builder identity and metadata. REQUIRED at SLSA Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'BuildProvenance'],
         'in_subset': ['slsa_build_track']} })
    type: str = Field(default=..., alias="_type", description="""Always \"https://in-toto.io/Statement/v1\". Identifies the in-toto statement schema version and namespace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    subject: list[ResourceDescriptor] = Field(default=..., description="""The set of software artifacts to which a predicate applies. Each entry MUST contain a digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicateType: str = Field(default=..., description="""URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicate: Optional[str] = Field(default=None, description="""The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    attestationStorageUri: Optional[str] = Field(default=None, description="""URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_env_track',
                       'slsa_adoption_study']} })
    signingTool: Optional[str] = Field(default=None, description="""URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., \"https://github.com/sigstore/cosign\", \"https://github.com/notaryproject/notation\"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })
    sigstoreLogEntry: Optional[str] = Field(default=None, description="""URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., \"https://rekor.sigstore.dev/api/v1/log/entries/24296fb...\"). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })


class BuildDefinition(ConfiguredBaseModel):
    """
    Describes all inputs to the build in enough detail to initialise and reproduce the build. The accuracy and completeness are implied by the builder identified in runDetails.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track'],
         'notes': ['Hermetic build challenge (Tamanna et al., 2024, CI.1): Over 50% of '
                   'practitioners surveyed by OpenSSF found hermetic builds difficult '
                   'to implement. Non-build configurations (e.g., GoReleaser '
                   'publish-only steps) lack explicit hermetic-build tool support. Use '
                   'hermeticBuild to record whether L3 isolation is satisfied.',
                   'Provenance generation standardization (Tamanna et al., 2024, '
                   'S3.1): Recording which tool generated this provenance via '
                   'provenanceGenerationTool supports standardization, reproducibility '
                   'verification, and incident response.']})

    buildType: str = Field(default=..., description="""URI identifying the template for how to perform the build and how to interpret the parameters and dependencies. SHOULD resolve to a human-readable specification. REQUIRED at SLSA Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'], 'in_subset': ['slsa_build_track']} })
    externalParameters: Optional[str] = Field(default=None, description="""Top-level, independent inputs under external (tenant or user) control. MUST be complete at SLSA Build L3. Stored as a JSON object. Verifiers SHOULD reject unrecognized fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'],
         'in_subset': ['slsa_build_track'],
         'notes': ['SSF pipeline definition files (CNCF TAG-Security Secure Software '
                   'Factory): In Tekton-based SSF pipelines, externalParameters '
                   'typically contains the PipelineRun YAML reference or TaskRun '
                   'definition URI. For GitHub Actions, it would contain the workflow '
                   'file path and ref. These values MUST be complete and verifiable at '
                   'SLSA Build L3 so that consumers can confirm the exact build '
                   'recipe. Use pipelineOrchestrator to record the CI system and '
                   'provenanceGenerationTool (in BuildDefinition) to record the '
                   'attestation generator (e.g., Tekton Chains).']} })
    internalParameters: Optional[str] = Field(default=None, description="""Parameters set internally by the build platform. Intended for debugging, incident response, and enabling reproducible builds. Stored as a JSON object; need not be verified by consumers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'], 'in_subset': ['slsa_build_track']} })
    resolvedDependencies: Optional[list[ResourceDescriptor]] = Field(default=None, description="""Unordered collection of artifacts needed at build time (config files, source, build tools). Completeness is best effort through SLSA Build L3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'], 'in_subset': ['slsa_build_track']} })
    hermeticBuild: Optional[bool] = Field(default=None, description="""Whether all build inputs are fully isolated to the dependencies declared in resolvedDependencies, with no network access or filesystem references outside the explicit build graph. Hermetic builds are a stated requirement for SLSA Build L3; practitioners identified this as one of the most commonly cited implementation barriers, with over 50% of surveyed practitioners finding hermetic build requirements difficult to implement (Tamanna et al., 2024, CI.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'],
         'in_subset': ['slsa_build_track', 'slsa_adoption_study']} })
    provenanceGenerationTool: Optional[str] = Field(default=None, description="""URI or name of the tool used to generate provenance for this build (e.g., \"https://github.com/slsa-framework/slsa-github-generator\"). Standardizing this field across builds reduces confusion, supports reproducibility verification, and aligns with the recommended strategy of simplifying and standardizing provenance generation processes (Tamanna et al., 2024, S3.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'],
         'in_subset': ['slsa_build_track', 'slsa_adoption_study']} })
    pipelineOrchestrator: Optional[str] = Field(default=None, description="""URI or name of the CI/CD pipeline orchestration system that coordinated this build (e.g., \"https://tekton.dev\", \"https://github.com/features/actions\", \"https://jenkins.io\"). In the SSF reference architecture this is the Build Service layer that feeds the Artifact Registry. Providing this field helps distinguish the orchestrator from the provenance-generating builder identity (builder.id) in complex deployments where they differ (e.g., a Tekton Pipeline running on Google Cloud Pipelines).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildDefinition'],
         'in_subset': ['slsa_build_track', 'slsa_ssf']} })


class RunDetails(ConfiguredBaseModel):
    """
    Details specific to this particular execution of the build, including the trusted builder and optional run-level metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track']})

    builder: Builder = Field(default=..., description="""Identifies the build platform that executed the build and is trusted to have correctly generated this provenance. REQUIRED at SLSA Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RunDetails'], 'in_subset': ['slsa_build_track']} })
    buildMetadata: Optional[BuildMetadata] = Field(default=None, description="""Metadata about this particular build execution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RunDetails'], 'in_subset': ['slsa_build_track']} })
    byproducts: Optional[list[ResourceDescriptor]] = Field(default=None, description="""Additional artifacts produced during the build that are NOT the primary output but may be useful for debugging or incident response (e.g., build logs, intermediate artifacts).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RunDetails'], 'in_subset': ['slsa_build_track']} })


class Builder(ConfiguredBaseModel):
    """
    Represents the transitive closure of all software, hardware, and entities trusted to faithfully execute the build and record provenance. The builder.id is the primary basis for determining SLSA Build Level.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track']})

    id: str = Field(default=..., description="""A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder',
                       'Verifier',
                       'BuildPlatform',
                       'SourceRepository',
                       'BuildImage'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    builderDependencies: Optional[list[ResourceDescriptor]] = Field(default=None, description="""Dependencies used by the control plane orchestrator that are not run within the build workload but may affect provenance generation or security guarantees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder'], 'in_subset': ['slsa_build_track']} })
    version: Optional[str] = Field(default=None, description="""Map of component names to their version strings, represented as a JSON object (string → string).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder', 'Verifier'], 'in_subset': ['slsa_build_track']} })
    versionTag: Optional[str] = Field(default=None, description="""A semantic version tag (e.g., \"v1.2.3\") assigned to the builder or the produced artifact at the time of the build. Practitioners recommended implementing versioning tagging early in SLSA framework deployment to facilitate progress tracking, reduce maintenance confusion from breaking changes, and enable more straightforward verification (Tamanna et al., 2024, S4.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder'],
         'in_subset': ['slsa_build_track', 'slsa_adoption_study']} })


class BuildMetadata(ConfiguredBaseModel):
    """
    Metadata about a specific invocation of the build, including timing information and a unique build identifier for log correlation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track']})

    invocationId: Optional[str] = Field(default=None, description="""A globally unique identifier for a build invocation, useful for finding associated logs. Format defined by builder.id; treated as opaque and case-sensitive. The value SHOULD be globally unique.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildMetadata'], 'in_subset': ['slsa_build_track']} })
    startedOn: Optional[str] = Field(default=None, description="""Timestamp (RFC 3339) of when the build started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildMetadata'], 'in_subset': ['slsa_build_track']} })
    finishedOn: Optional[str] = Field(default=None, description="""Timestamp (RFC 3339) of when the build completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildMetadata'], 'in_subset': ['slsa_build_track']} })


class VerificationSummaryAttestation(Statement):
    """
    An attestation predicate (predicateType \"https://slsa.dev/verification_summary/v1\") issued by a trusted verifier stating that one or more artifacts were evaluated against a policy and the SLSA level at which they were verified. Allows consumers to trust the verifier's determination without needing access to all underlying provenance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'notes': ['Verification complexity (Tamanna et al., 2024, LF.1): The '
                   'slsa-verifier tool was highlighted by practitioners for complexity '
                   'and redundancy. No standardized attestation storage model existed '
                   'as of SLSA v1.0; inconsistencies between package manager '
                   'registries and stored files can undermine verification accuracy. '
                   'Downstream systems also lack clear guidance on how to consume and '
                   'communicate attestation data to other stakeholders.'],
         'see_also': ['https://openssf.org/projects/guac/']})

    verifier: Verifier = Field(default=..., description="""Identifies the entity that performed the verification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    timeVerified: Optional[str] = Field(default=None, description="""Timestamp (RFC 3339) indicating when the verification occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    resourceUri: str = Field(default=..., description="""URI identifying the resource associated with the artifact being verified. SHOULD be the URI from which the consumer fetches the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    policy: ResourceDescriptor = Field(default=..., description="""The policy the subject was verified against. MUST contain a URI; SHOULD contain a digest identifying the exact policy version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'notes': ['SSF Policy Engine layer (CNCF TAG-Security): In the SSF reference '
                   'architecture, the policy consumed here is enforced at admission '
                   'time by a Policy Engine such as OPA/Gatekeeper or Kyverno. These '
                   'engines consume Verification Summary Attestations (VSAs) to verify '
                   'that an artifact meets the required SLSA level before allowing '
                   'deployment. Best practice is to reference a versioned, '
                   'content-addressed policy document so verifiers can reconstruct the '
                   'exact policy evaluated.']} })
    inputAttestations: Optional[list[ResourceDescriptor]] = Field(default=None, description="""All attestations consulted during verification. If non-empty, MUST be complete — it MUST list every attestation used. Each entry MUST contain a digest; SHOULD contain a URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    verificationResult: VerificationResultEnum = Field(default=..., description="""Whether the artifact passed or failed policy verification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    verifiedLevels: list[SlsaResultEnum] = Field(default=..., description="""The highest verified SLSA level for each applicable track (not including transitive dependencies). At most one level per track. Implies all levels below it within the same track.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument', 'VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    dependencyLevels: Optional[str] = Field(default=None, description="""Map from SlsaResult to count of transitive dependencies verified at that level (JSON object string). Allows policy engines to enforce minimum levels on the full dependency graph.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    slsaVersion: Optional[str] = Field(default=None, description="""Version of the SLSA specification used during verification, in MAJOR.MINOR format (e.g., \"1.0\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationSummaryAttestation'],
         'in_subset': ['slsa_build_track', 'slsa_source_track']} })
    type: str = Field(default=..., alias="_type", description="""Always \"https://in-toto.io/Statement/v1\". Identifies the in-toto statement schema version and namespace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    subject: list[ResourceDescriptor] = Field(default=..., description="""The set of software artifacts to which a predicate applies. Each entry MUST contain a digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicateType: str = Field(default=..., description="""URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicate: Optional[str] = Field(default=None, description="""The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    attestationStorageUri: Optional[str] = Field(default=None, description="""URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_env_track',
                       'slsa_adoption_study']} })
    signingTool: Optional[str] = Field(default=None, description="""URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., \"https://github.com/sigstore/cosign\", \"https://github.com/notaryproject/notation\"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })
    sigstoreLogEntry: Optional[str] = Field(default=None, description="""URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., \"https://rekor.sigstore.dev/api/v1/log/entries/24296fb...\"). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })


class Verifier(ConfiguredBaseModel):
    """
    The entity that performed verification of an artifact and issued a Verification Summary Attestation. Consumers MUST accept only specific (signer, verifier) pairs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    id: str = Field(default=..., description="""A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder',
                       'Verifier',
                       'BuildPlatform',
                       'SourceRepository',
                       'BuildImage'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    version: Optional[str] = Field(default=None, description="""Map of component names to their version strings, represented as a JSON object (string → string).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder', 'Verifier'], 'in_subset': ['slsa_build_track']} })


class Producer(ConfiguredBaseModel):
    """
    A party who creates software and provides it to others. Responsible for choosing an appropriate build platform, following a consistent build process, and distributing provenance to consumers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track']})

    name: Optional[str] = Field(default=None, description="""A local name for a resource within the context of an attestation, or the name of a package, producer, or party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor', 'Producer', 'Package'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track']} })
    buildPlatformId: Optional[str] = Field(default=None, description="""URI of the build platform chosen to produce artifacts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Producer'], 'in_subset': ['slsa_build_track']} })


class Consumer(ConfiguredBaseModel):
    """
    A party who uses software provided by a producer. May verify provenance directly or delegate that responsibility to a separate verifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    pass


class InfrastructureProvider(ConfiguredBaseModel):
    """
    A party who provides software or services to other roles in the supply chain, such as a package registry maintainer or build platform operator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    pass


class BuildPlatform(ConfiguredBaseModel):
    """
    The infrastructure (software, hardware, people, and organizations) used to transform source code into package artifacts. Responsible for provenance generation and isolation between tenant builds. Often a hosted, multi-tenant build service.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track']})

    id: str = Field(default=..., description="""A URI uniquely identifying an entity (build platform, verifier, build image, or source repository). The primary trust anchor for consumers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder',
                       'Verifier',
                       'BuildPlatform',
                       'SourceRepository',
                       'BuildImage'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    buildLevel: Optional[BuildLevelEnum] = Field(default=None, description="""The SLSA Build Level this platform is capable of producing, as determined by its provenance generation and isolation guarantees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildPlatform'], 'in_subset': ['slsa_build_track']} })
    isHosted: Optional[bool] = Field(default=None, description="""True if this is a hosted (multi-tenant) platform running on shared or dedicated infrastructure, rather than an individual's workstation. Required for SLSA Build L2+.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildPlatform'],
         'in_subset': ['slsa_build_track'],
         'notes': ['SSF reference architecture (CNCF TAG-Security): Hosted, '
                   'multi-tenant build services (GitHub Actions, Google Cloud Build, '
                   'GitLab CI/CD, CircleCI) are the recommended Build Service layer in '
                   'the SSF pattern. Using a hosted service is a prerequisite for SLSA '
                   'Build L2 because it provides the separation of concerns that '
                   'prevents tenants from tampering with provenance generated by the '
                   'control plane. Self-hosted runners can be used at SLSA Build L2+ '
                   'only if they replicate the isolation guarantees of hosted '
                   'services.']} })


class ControlPlane(ConfiguredBaseModel):
    """
    The build platform component that orchestrates each independent build execution and generates provenance. Managed by an admin and trusted to be outside of tenant control. Responsible for generating and signing provenance at SLSA Build L2+.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track']})

    pass


class Package(ConfiguredBaseModel):
    """
    An identifiable unit of software intended for distribution. In the SLSA model, a package is always the output of a build process (which may be a no-op). The package name is the primary security boundary within a package ecosystem.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_track', 'slsa_dependency_track']})

    name: Optional[str] = Field(default=None, description="""A local name for a resource within the context of an attestation, or the name of a package, producer, or party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceDescriptor', 'Producer', 'Package'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track']} })
    ecosystem: Optional[str] = Field(default=None, description="""The package ecosystem (e.g., \"PyPA\", \"npm\", \"OCI\", \"cargo\") governing distribution conventions for this package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track'],
         'notes': ['Ecosystem naming inconsistency can undermine attestation accuracy '
                   '(Tamanna et al., 2024, UR.1): For example, "npm install P" '
                   'produces package name A while "npm download P && npm install '
                   'P.tar.gz" produces name B from the same source, causing metadata '
                   'and provenance mismatches that persist even with lock files. '
                   'Policy engines must account for these cross-registry naming '
                   'discrepancies when verifying provenance.']} })
    registry: Optional[str] = Field(default=None, description="""URI of the package registry where a package is published and from which consumers resolve the package name to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track']} })
    artifact: Optional[ResourceDescriptor] = Field(default=None, description="""A specific immutable package artifact or the artifact whose dependency inventory is recorded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package', 'DependencyInventory'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track']} })


class SourceRepository(ConfiguredBaseModel):
    """
    A self-contained unit that holds the content and complete revision history for a set of files, along with metadata such as branches and tags. Hosted and governed by a Source Control System.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_source_track'],
         'slot_usage': {'id': {'description': 'Canonical URI that uniquely identifies '
                                              'this source repository.',
                               'name': 'id'}}})

    id: str = Field(default=..., description="""Canonical URI that uniquely identifies this source repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder',
                       'Verifier',
                       'BuildPlatform',
                       'SourceRepository',
                       'BuildImage'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description of a repository's purpose or a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRepository'], 'in_subset': ['slsa_source_track']} })
    sourceLevel: Optional[SourceLevelEnum] = Field(default=None, description="""The SLSA Source Level achieved or verified for a source repository or revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRepository', 'SourceProvenanceAttestation'],
         'in_subset': ['slsa_source_track']} })


class SourceRevision(ConfiguredBaseModel):
    """
    A specific, logically immutable snapshot of a source repository's tracked files. Uniquely identified by a revision identifier such as a cryptographic hash (e.g., git commit SHA) or a path-qualified sequential number (e.g., SVN).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_source_track'],
         'notes': ['if SourceRevision ever needs signingTool/sigstoreLogEntry (for  '
                   'Sigstore-signed git tags via Cosign, gittuf), then consider '
                   'adding  a SigstoreSignable mixin on both Statement and '
                   'SourceRevision']})

    revisionId: str = Field(default=..., description="""Immutable identifier for a source revision (e.g., git commit SHA, path-qualified sequential number).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRevision'], 'in_subset': ['slsa_source_track']} })
    repository: Optional[SourceRepository] = Field(default=None, description="""The source repository that contains this revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRevision'], 'in_subset': ['slsa_source_track']} })
    author: Optional[str] = Field(default=None, description="""Identity of the person or automation that authored this revision (e.g., an email address or platform username).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRevision'], 'in_subset': ['slsa_source_track']} })
    timestamp: Optional[str] = Field(default=None, description="""Timestamp (RFC 3339) of when this source revision was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRevision'], 'in_subset': ['slsa_source_track']} })
    parentRevisions: Optional[list[str]] = Field(default=None, description="""Revision IDs of the parent revision(s), forming the directed acyclic graph of change history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRevision'], 'in_subset': ['slsa_source_track']} })
    reviewType: Optional[ReviewTypeEnum] = Field(default=None, description="""The type of human or automated review process used to approve this source revision. Captures the contested forms of two-party review — including pair programming and mob programming — whose security equivalence to standard asynchronous two-party review is an open question identified in practitioner community discussions (Tamanna et al., 2024, LF.2). See ReviewTypeEnum for defined values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRevision'],
         'in_subset': ['slsa_source_track', 'slsa_adoption_study']} })


class SourceProvenanceAttestation(Statement):
    """
    An attestation describing how a source revision came to exist: where it was hosted, when it was generated, what process was used, who the contributors were, and which technical controls were enforced by the Source Control System.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_source_track']})

    revision: Optional[SourceRevision] = Field(default=None, description="""The source revision that this attestation describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceProvenanceAttestation'],
         'in_subset': ['slsa_source_track']} })
    sourceLevel: Optional[SourceLevelEnum] = Field(default=None, description="""The SLSA Source Level achieved or verified for a source repository or revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceRepository', 'SourceProvenanceAttestation'],
         'in_subset': ['slsa_source_track']} })
    controlsEnforced: Optional[list[str]] = Field(default=None, description="""Technical controls actively enforced by the Source Control System when this revision was created (e.g., \"two-party review\", \"branch protection\", \"status checks\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceProvenanceAttestation'],
         'in_subset': ['slsa_source_track'],
         'notes': ['Two-party review feasibility (Tamanna et al., 2024, LF.2): Many '
                   'open-source projects have a single maintainer, making the '
                   'two-party review requirement impractical. Pair programming and mob '
                   'programming were raised as contested alternatives whose security '
                   'equivalence has not been formally established. Use the reviewType '
                   'slot on SourceRevision to record the specific form of review '
                   'applied.']} })
    type: str = Field(default=..., alias="_type", description="""Always \"https://in-toto.io/Statement/v1\". Identifies the in-toto statement schema version and namespace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    subject: list[ResourceDescriptor] = Field(default=..., description="""The set of software artifacts to which a predicate applies. Each entry MUST contain a digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicateType: str = Field(default=..., description="""URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicate: Optional[str] = Field(default=None, description="""The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    attestationStorageUri: Optional[str] = Field(default=None, description="""URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_env_track',
                       'slsa_adoption_study']} })
    signingTool: Optional[str] = Field(default=None, description="""URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., \"https://github.com/sigstore/cosign\", \"https://github.com/notaryproject/notation\"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })
    sigstoreLogEntry: Optional[str] = Field(default=None, description="""URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., \"https://rekor.sigstore.dev/api/v1/log/entries/24296fb...\"). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })


class DependencyInventory(ConfiguredBaseModel):
    """
    A comprehensive inventory of all third-party build dependencies for an artifact, capturing direct and transitive dependencies. Supports vulnerability management and incident response.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_dependency_track']})

    artifact: Optional[ResourceDescriptor] = Field(default=None, description="""A specific immutable package artifact or the artifact whose dependency inventory is recorded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package', 'DependencyInventory'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track']} })
    dependencies: Optional[list[ResourceDescriptor]] = Field(default=None, description="""All third-party build dependencies (direct and transitive) for an artifact version, identified by URI and digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DependencyInventory'], 'in_subset': ['slsa_dependency_track']} })
    dependencyLevel: Optional[DependencyLevelEnum] = Field(default=None, description="""The SLSA Dependency Level that this inventory and associated triage process supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DependencyInventory'], 'in_subset': ['slsa_dependency_track']} })


class BuildImage(ConfiguredBaseModel):
    """
    The template for a build environment, such as a VM or container image. Comprises the root filesystem, pre-installed guest OS and packages, the build executor, and the build agent. Created by a build image producer and consumed by the hosted build platform.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_env_track'],
         'slot_usage': {'id': {'description': 'URI uniquely identifying this build '
                                              'image version (e.g., an OCI image '
                                              'reference with digest).',
                               'name': 'id'}}})

    id: str = Field(default=..., description="""URI uniquely identifying this build image version (e.g., an OCI image reference with digest).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Builder',
                       'Verifier',
                       'BuildPlatform',
                       'SourceRepository',
                       'BuildImage'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_env_track']} })
    provenance: Optional[BuildProvenance] = Field(default=None, description="""SLSA Build Provenance for a build image, describing how the image itself was produced. Required for SLSA Build Environment L1+.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildImage'], 'in_subset': ['slsa_build_env_track']} })
    buildEnvLevel: Optional[BuildEnvLevelEnum] = Field(default=None, description="""The SLSA Build Environment Level supported or represented, reflecting the strength of the integrity guarantees provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildImage', 'BuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_env_track']} })


class BuildEnvironmentAttestation(Statement):
    """
    An attestation describing the integrity of a build environment at the time a specific build was dispatched and executed. Used to verify that a build ran in the expected, untampered environment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_build_env_track']})

    buildId: str = Field(default=..., description="""An immutable identifier uniquely assigned to a build execution (e.g., a UUID). Links a BuildEnvironmentAttestation to the corresponding build provenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_env_track']} })
    buildImage: Optional[BuildImage] = Field(default=None, description="""The build image from which the build environment was instantiated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_env_track']} })
    measurements: Optional[list[str]] = Field(default=None, description="""Cryptographic measurements (hashes) of build environment components captured during boot and initialization, used to verify integrity against known-good reference values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_env_track']} })
    buildEnvLevel: Optional[BuildEnvLevelEnum] = Field(default=None, description="""The SLSA Build Environment Level supported or represented, reflecting the strength of the integrity guarantees provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BuildImage', 'BuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_env_track']} })
    type: str = Field(default=..., alias="_type", description="""Always \"https://in-toto.io/Statement/v1\". Identifies the in-toto statement schema version and namespace.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    subject: list[ResourceDescriptor] = Field(default=..., description="""The set of software artifacts to which a predicate applies. Each entry MUST contain a digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicateType: str = Field(default=..., description="""URI identifying the schema and semantics of the predicate field. Used to distinguish different attestation types (e.g., SLSA Provenance vs. Verification Summary Attestation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    predicate: Optional[str] = Field(default=None, description="""The attestation payload — an arbitrary JSON object whose schema is fully determined by predicateType.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_build_env_track']} })
    attestationStorageUri: Optional[str] = Field(default=None, description="""URI indicating where this signed attestation is publicly stored or retrievable. No universal standard for attestation storage location was established in SLSA v1.0; Sigstore and VCS-embedded storage are two common approaches. Explicitly recording this URI addresses the storage ambiguity identified as a significant adoption barrier: practitioners reported uncertainty about where generated attestations should be stored (Tamanna et al., 2024, LF.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_env_track',
                       'slsa_adoption_study']} })
    signingTool: Optional[str] = Field(default=None, description="""URI or name of the tool used to cryptographically sign the artifact or attestation (e.g., \"https://github.com/sigstore/cosign\", \"https://github.com/notaryproject/notation\"). In the SSF reference architecture the Signing Service layer is distinct from the Build Service; recording the signing tool enables verifiers to select the matching verification workflow. For Sigstore keyless signing the value should be the Cosign release URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })
    sigstoreLogEntry: Optional[str] = Field(default=None, description="""URI of the Rekor transparency log entry recording this attestation or artifact signature (e.g., \"https://rekor.sigstore.dev/api/v1/log/entries/24296fb...\"). The Rekor log provides an immutable, auditable record of signing events that underpins Sigstore keyless signing. Verifiers can fetch this entry to confirm the cryptographic signature was recorded in the public-good log and obtain the signing certificate chain issued by Fulcio. Recording this URI enables offline and third-party verification without requiring direct access to the original signing key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track', 'slsa_ssf']} })


class AdoptionMetadata(ConfiguredBaseModel):
    """
    Optional structured metadata capturing the SLSA adoption challenges and mitigation strategies relevant to a given attestation or deployment context. Derived from empirical analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Use this class to document which challenge themes apply to the current deployment and which strategies are being employed or recommended. Attach via the adoptionMetadata slot on SlsaDocument.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa',
         'in_subset': ['slsa_adoption_study']})

    challenges: Optional[list[AdoptionChallengeEnum]] = Field(default=None, description="""The adoption challenge themes that apply to this attestation or deployment context, drawn from the empirically identified challenge taxonomy (Tamanna et al., 2024, arXiv:2409.05014).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdoptionMetadata'], 'in_subset': ['slsa_adoption_study']} })
    strategies: Optional[list[AdoptionStrategyEnum]] = Field(default=None, description="""The mitigation strategies being employed or recommended in this attestation or deployment context, drawn from the empirically identified strategy taxonomy (Tamanna et al., 2024, arXiv:2409.05014).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdoptionMetadata'], 'in_subset': ['slsa_adoption_study']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SlsaDocument.model_rebuild()
DigestSet.model_rebuild()
ResourceDescriptor.model_rebuild()
Statement.model_rebuild()
BuildProvenance.model_rebuild()
BuildDefinition.model_rebuild()
RunDetails.model_rebuild()
Builder.model_rebuild()
BuildMetadata.model_rebuild()
VerificationSummaryAttestation.model_rebuild()
Verifier.model_rebuild()
Producer.model_rebuild()
Consumer.model_rebuild()
InfrastructureProvider.model_rebuild()
BuildPlatform.model_rebuild()
ControlPlane.model_rebuild()
Package.model_rebuild()
SourceRepository.model_rebuild()
SourceRevision.model_rebuild()
SourceProvenanceAttestation.model_rebuild()
DependencyInventory.model_rebuild()
BuildImage.model_rebuild()
BuildEnvironmentAttestation.model_rebuild()
AdoptionMetadata.model_rebuild()
