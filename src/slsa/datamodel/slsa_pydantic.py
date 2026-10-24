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


metamodel_version = "1.12.0"
version = "1.2.0"


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


linkml_meta = LinkMLMeta({'comments': ['The version is the SLSA specification version the model '
                  'renders. The Dependency and Build Environment tracks follow the '
                  'working draft at that version, which the release does not '
                  'include.',
                  'slsa_core imports only the LinkML types, each track module '
                  'imports the core, and this file adds only the document root, so '
                  'an importer can take one module.'],
     'default_prefix': 'slsa',
     'default_range': 'string',
     'description': 'A LinkML model of the SLSA specification: its tracks and '
                    'levels, the roles and systems in a software supply chain, and '
                    'the in-toto attestations that carry build provenance and '
                    'verification summaries.',
     'id': 'https://w3id.org/lmodel/slsa',
     'imports': ['linkml:types',
                 './slsa_core',
                 './slsa_build',
                 './slsa_verification',
                 './slsa_source',
                 './slsa_dependency',
                 './slsa_build_environment',
                 './slsa_adoption'],
     'license': 'Apache-2.0',
     'name': 'slsa',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'slsa': {'prefix_prefix': 'slsa',
                           'prefix_reference': 'https://w3id.org/lmodel/slsa/'}},
     'see_also': ['https://lmodel.github.io/slsa',
                  'https://slsa.dev/spec/v1.2/',
                  'https://github.com/slsa-framework/slsa'],
     'source': 'https://slsa.dev/spec/v1.2',
     'source_file': 'src/slsa/schema/slsa.yaml',
     'title': 'Supply-chain Levels for Software Artifacts (SLSA)'} )

class SlsaBuildLevel(str, Enum):
    """
    The levels of the SLSA Build track, each adding protection against tampering with the build or its provenance.
    """
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0"
    """
    No requirements; the absence of SLSA, as for development or test builds.
    """
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1"
    """
    Provenance exists and shows how the package was built; it prevents mistakes but is easy to forge.
    """
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2"
    """
    A hosted platform generates and signs the provenance, so tampering after the build needs an explicit attack.
    """
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3"
    """
    A hardened platform prevents runs from influencing one another and keeps signing material away from build steps, so forging provenance needs an exploit.
    """


class SlsaVerificationResult(str, Enum):
    """
    The outcome of verifying an artifact against a policy.
    """
    PASSED = "PASSED"
    """
    The artifact met the policy.
    """
    FAILED = "FAILED"
    """
    The artifact did not meet the policy.
    """


class SlsaResult(str, Enum):
    """
    A result of evaluating an artifact against SLSA: a track level, a verified property, or a failure. A level implies the levels below it in the same track.
    """
    SLSA_BUILD_LEVEL_UNEVALUATED = "SLSA_BUILD_LEVEL_UNEVALUATED"
    """
    The issuer makes no claim about the Build track level.
    """
    SLSA_BUILD_LEVEL_0 = "SLSA_BUILD_LEVEL_0"
    """
    No Build track guarantees were verified.
    """
    SLSA_BUILD_LEVEL_1 = "SLSA_BUILD_LEVEL_1"
    """
    Build level 1 was verified.
    """
    SLSA_BUILD_LEVEL_2 = "SLSA_BUILD_LEVEL_2"
    """
    Build level 2 was verified.
    """
    SLSA_BUILD_LEVEL_3 = "SLSA_BUILD_LEVEL_3"
    """
    Build level 3 was verified.
    """
    SLSA_SOURCE_LEVEL_UNEVALUATED = "SLSA_SOURCE_LEVEL_UNEVALUATED"
    """
    The issuer makes no claim about the Source track level.
    """
    SLSA_SOURCE_LEVEL_0 = "SLSA_SOURCE_LEVEL_0"
    """
    No Source track guarantees were verified.
    """
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1"
    """
    Source level 1 was verified.
    """
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2"
    """
    Source level 2 was verified.
    """
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3"
    """
    Source level 3 was verified.
    """
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4"
    """
    Source level 4 was verified.
    """
    SLSA_SOURCE_TWO_PARTY_REVIEWED = "SLSA_SOURCE_TWO_PARTY_REVIEWED"
    """
    The verified property that two trusted persons reviewed the source, at whatever source level.
    """
    SLSA_BUILD_REPRODUCED = "SLSA_BUILD_REPRODUCED"
    """
    The verified property that two or more independent build platforms reproduced the artifact.
    """
    FAILED = "FAILED"
    """
    Policy evaluation failed.
    """


class SlsaSourceLevel(str, Enum):
    """
    The levels of the SLSA Source track, each adding trust in how a revision was created.
    """
    SLSA_SOURCE_LEVEL_0 = "SLSA_SOURCE_LEVEL_0"
    """
    No Source track claims; the SCS issued no VSA for the revision.
    """
    SLSA_SOURCE_LEVEL_1 = "SLSA_SOURCE_LEVEL_1"
    """
    The source is managed in a version control system, so it has discrete, immutable revisions.
    """
    SLSA_SOURCE_LEVEL_2 = "SLSA_SOURCE_LEVEL_2"
    """
    Branch history is continuous and retained, and the SCS issues source provenance for each new revision.
    """
    SLSA_SOURCE_LEVEL_3 = "SLSA_SOURCE_LEVEL_3"
    """
    The SCS enforces the organization's technical controls on protected named references and provides evidence of them.
    """
    SLSA_SOURCE_LEVEL_4 = "SLSA_SOURCE_LEVEL_4"
    """
    Two trusted persons agree to every change on protected branches.
    """


class SlsaReviewType(str, Enum):
    """
    The forms of review that may approve a revision, including the contested forms the adoption study records.
    """
    TWO_PARTY = "TWO_PARTY"
    """
    A reviewer distinct from the author approved the change, both being trusted persons.
    """
    PAIR_PROGRAMMING = "PAIR_PROGRAMMING"
    """
    Two developers wrote the change together at one workstation or screen; whether this counts as two-party review is open.
    """
    MOB_PROGRAMMING = "MOB_PROGRAMMING"
    """
    A group wrote the change together; whether this counts as two-party review is open.
    """
    AUTOMATED = "AUTOMATED"
    """
    A tool or bot reviewed the change with no second person, which does not meet Source L4.
    """


class SlsaDependencyLevel(str, Enum):
    """
    The levels of the SLSA Dependency track, each reducing the risk third-party dependencies bring.
    """
    SLSA_DEPENDENCY_LEVEL_0 = "SLSA_DEPENDENCY_LEVEL_0"
    """
    No Dependency track claims.
    """
    SLSA_DEPENDENCY_LEVEL_1 = "SLSA_DEPENDENCY_LEVEL_1"
    """
    An inventory of all build dependencies, direct and transitive, exists.
    """
    SLSA_DEPENDENCY_LEVEL_2 = "SLSA_DEPENDENCY_LEVEL_2"
    """
    Every known vulnerability in the dependencies was triaged before release.
    """
    SLSA_DEPENDENCY_LEVEL_3 = "SLSA_DEPENDENCY_LEVEL_3"
    """
    Every third-party build dependency is consumed from a location the producer controls.
    """
    SLSA_DEPENDENCY_LEVEL_4 = "SLSA_DEPENDENCY_LEVEL_4"
    """
    An ingestion policy keeps compromised upstream dependencies out of the build.
    """


class SlsaBuildEnvironmentLevel(str, Enum):
    """
    The levels of the SLSA Build Environment track, each extending integrity further into the compute that runs builds.
    """
    SLSA_BUILD_ENV_LEVEL_0 = "SLSA_BUILD_ENV_LEVEL_0"
    """
    No Build Environment track claims.
    """
    SLSA_BUILD_ENV_LEVEL_1 = "SLSA_BUILD_ENV_LEVEL_1"
    """
    The build image has signed build provenance, protecting against tampering while the image is distributed.
    """
    SLSA_BUILD_ENV_LEVEL_2 = "SLSA_BUILD_ENV_LEVEL_2"
    """
    The compute platform attests to the environment's state at boot, protecting against tampering through the control plane.
    """
    SLSA_BUILD_ENV_LEVEL_3 = "SLSA_BUILD_ENV_LEVEL_3"
    """
    Trusted hardware attests to the host's state, protecting against tampering through the host interface.
    """


class SlsaAdoptionChallenge(str, Enum):
    """
    The four themes of difficulty practitioners met when adopting SLSA.
    """
    COMPLEX_IMPLEMENTATION = "COMPLEX_IMPLEMENTATION"
    """
    Generating provenance and maintaining the required tools is complicated.
    """
    UNCLEAR_COMMUNICATION = "UNCLEAR_COMMUNICATION"
    """
    SLSA's terms and its guidance for particular ecosystems are hard to understand.
    """
    LIMITED_FEASIBILITY = "LIMITED_FEASIBILITY"
    """
    Verification tooling, attestation storage and two-party review are hard to put into practice.
    """
    UNCLEAR_RELEVANCE = "UNCLEAR_RELEVANCE"
    """
    Which attacks SLSA mitigates, and how it differs from other practices, is unclear.
    """


class SlsaAdoptionStrategy(str, Enum):
    """
    The five themes of strategy practitioners proposed for the adoption challenges.
    """
    ENHANCE_ALIGNMENT_FLEXIBILITY = "ENHANCE_ALIGNMENT_FLEXIBILITY"
    """
    Make SLSA fit more contexts, with build-system tracks, flexibility for varied organizations and alignment with OpenSSF practices.
    """
    PROVIDE_DETAILED_DOCUMENTATION = "PROVIDE_DETAILED_DOCUMENTATION"
    """
    Give clearer definitions, standard terms, negative examples and better navigation.
    """
    STREAMLINE_PROVENANCE_GENERATION = "STREAMLINE_PROVENANCE_GENERATION"
    """
    Simplify and standardize provenance generation with tools and templates, and fix release-tool inconsistencies.
    """
    IMPROVE_VERIFICATION_PROCESS = "IMPROVE_VERIFICATION_PROCESS"
    """
    Strengthen verification and level determination, tag versions early, and give downstream users more signals.
    """
    COLLABORATE_WITH_COMMUNITY = "COLLABORATE_WITH_COMMUNITY"
    """
    Align with industry standards, guide newcomers, and share knowledge across projects.
    """



class InTotoDigestSet(ConfiguredBaseModel):
    """
    A set of digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Digests are lowercase hexadecimal. The in-toto framework '
                      'defines more algorithms than the five modelled here.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'see_also': ['https://github.com/in-toto/attestation/blob/main/spec/v1/digest_set.md']})

    sha256: Optional[str] = Field(default=None, description="""The SHA-256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    sha512: Optional[str] = Field(default=None, description="""The SHA-512 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    git_commit: Optional[str] = Field(default=None, description="""The git commit id of a source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    git_tree: Optional[str] = Field(default=None, description="""The git tree id of a source revision's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })
    dir_hash: Optional[str] = Field(default=None, description="""A digest over a directory's content, as the in-toto framework defines it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet']} })

    @field_validator('sha256')
    def pattern_sha256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha512')
    def pattern_sha512(cls, v):
        pattern=re.compile(r"^[a-f0-9]{128}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha512 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha512 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_commit')
    def pattern_git_commit(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_commit format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_commit format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_tree')
    def pattern_git_tree(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_tree format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_tree format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoAnnotation(ConfiguredBaseModel):
    """
    One vendor-specific annotation on a resource descriptor, with a key and one or more values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    annotation_key: str = Field(default=..., description="""The annotation's key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAnnotation']} })
    annotation_values: Optional[list[str]] = Field(default=None, description="""The annotation's values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAnnotation']} })


class InTotoResourceDescriptor(ConfiguredBaseModel):
    """
    A reference to a software artifact or other resource, by URI, by digest, or both, with optional metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A descriptor needs a URI, a digest or both; which one a field '
                      'requires is said on that field.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_dependency_track',
                       'slsa_build_environment_track'],
         'see_also': ['https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md']})

    resource_uri: Optional[str] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaVerificationSummary'],
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'slot_uri': 'slsa:resource_uri'} })
    digest: Optional[InTotoDigestSet] = Field(default=None, description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaMeasurement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'slot_uri': 'slsa:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    download_location: Optional[str] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a Source VSA records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor']} })


class InTotoStatement(ConfiguredBaseModel):
    """
    The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The signature envelope around a statement is outside this '
                      'model.',
                      'Attestation and provenance are often confused; a statement is '
                      'the attestation, and build provenance is one kind of predicate '
                      'it may carry (Tamanna et al., 2024, UC.1).'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_environment_track'],
         'see_also': ['https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md',
                      'https://slsa.dev/spec/v1.2/attestation-model']})

    statement_type: str = Field(default=..., description="""The in-toto statement type, always https://in-toto.io/Statement/v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    subject: list[InTotoResourceDescriptor] = Field(default=..., description="""The artifacts the predicate is about; each carries a digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    predicate_type: str = Field(default=..., description="""The URI that names the predicate's type and so its schema, such as https://slsa.dev/provenance/v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    predicate: Optional[Union[SlsaBuildProvenance,SlsaVerificationSummary,SlsaSourceProvenance,SlsaBuildEnvironmentAttestation]] = Field(default=None, description="""The predicate, one of the kinds this schema models; predicate_kind names which.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement']} })
    attestation_storage_uri: Optional[str] = Field(default=None, description="""Where the signed attestation is stored or can be fetched.""", json_schema_extra = { "linkml_meta": {'comments': ['SLSA names no standard place to store attestations; recording '
                      'the place used helps consumers find them (Tamanna et al., 2024, '
                      'LF.1).'],
         'domain_of': ['InTotoStatement'],
         'in_subset': ['slsa_adoption_study']} })
    signing_tool: Optional[str] = Field(default=None, description="""The tool that signed the attestation, named by URI, such as Cosign or Notation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'in_subset': ['slsa_ssf']} })
    transparency_log_entry: Optional[str] = Field(default=None, description="""The transparency log entry that records the signature, such as a Rekor entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'in_subset': ['slsa_ssf']} })

    @field_validator('statement_type')
    def pattern_statement_type(cls, v):
        pattern=re.compile(r"^https://in-toto\.io/Statement/v1$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid statement_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid statement_type format: {v}"
            raise ValueError(err_msg)
        return v


class SlsaPredicate(ConfiguredBaseModel):
    """
    The base of every predicate this schema models; predicate_kind names the concrete kind.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_environment_track']})

    predicate_kind: Literal["SlsaPredicate"] = Field(default="SlsaPredicate", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaPredicate']} })


class SlsaParty(ConfiguredBaseModel):
    """
    A person or organization that takes part in a software supply chain, in one of the roles SLSA names.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'comments': ['One party may act in several roles, and several parties may '
                      'share one role.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/terminology#roles']})

    party_type: Literal["SlsaParty"] = Field(default="SlsaParty", description="""The role the party acts in, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaParty']} })
    party_name: Optional[str] = Field(default=None, description="""The party's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaParty']} })


class SlsaProducer(SlsaParty):
    """
    A party that creates software and provides it to others, choosing a build platform and distributing provenance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track']})

    build_platform: Optional[str] = Field(default=None, description="""The build platform this party or component belongs to or uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaProducer', 'SlsaControlPlane'],
         'in_subset': ['slsa_build_track'],
         'slot_uri': 'slsa:build_platform'} })
    party_type: Literal["SlsaProducer"] = Field(default="SlsaProducer", description="""The role the party acts in, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaParty']} })
    party_name: Optional[str] = Field(default=None, description="""The party's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaParty']} })


class SlsaConsumer(SlsaParty):
    """
    A party that uses software a producer provides, verifying its provenance itself or through a verifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    party_type: Literal["SlsaConsumer"] = Field(default="SlsaConsumer", description="""The role the party acts in, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaParty']} })
    party_name: Optional[str] = Field(default=None, description="""The party's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaParty']} })


class SlsaVerifier(SlsaParty):
    """
    A party that inspects provenance or other attestations and decides whether an artifact is authentic.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Consumers accept only specific signer and verifier pairs.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/verification_summary#verifier']})

    component_versions: Optional[list[SlsaComponentVersion]] = Field(default=None, description="""The version of each named component of a platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerifier', 'SlsaBuildPlatform'],
         'in_subset': ['slsa_build_track'],
         'slot_uri': 'slsa:component_versions'} })
    verifier_id: str = Field(default=..., description="""The URI that identifies the verifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerifier']} })
    party_type: Literal["SlsaVerifier"] = Field(default="SlsaVerifier", description="""The role the party acts in, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaParty']} })
    party_name: Optional[str] = Field(default=None, description="""The party's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaParty']} })


class SlsaInfrastructureProvider(SlsaParty):
    """
    A party that provides software or services to the other roles, such as a package registry's or a build platform's maintainers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_source_track']})

    party_type: Literal["SlsaInfrastructureProvider"] = Field(default="SlsaInfrastructureProvider", description="""The role the party acts in, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaParty']} })
    party_name: Optional[str] = Field(default=None, description="""The party's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaParty']} })


class SlsaBuildPlatform(ConfiguredBaseModel):
    """
    The system that runs builds and records their provenance: the transitive closure of software, hardware, people and organizations trusted to do so. Provenance names it as the builder.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A platform with several modes of operation at different levels '
                      'has a different builder_id for each.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/terminology#build-model',
                      'https://slsa.dev/spec/v1.2/build-provenance#builder']})

    component_versions: Optional[list[SlsaComponentVersion]] = Field(default=None, description="""The version of each named component of a platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerifier', 'SlsaBuildPlatform'],
         'in_subset': ['slsa_build_track'],
         'slot_uri': 'slsa:component_versions'} })
    builder_id: str = Field(default=..., description="""The URI that identifies the platform and determines its SLSA Build level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildPlatform']} })
    build_level: Optional[SlsaBuildLevel] = Field(default=None, description="""The highest SLSA Build level the platform's provenance can meet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildPlatform']} })
    hosted: Optional[bool] = Field(default=None, description="""Whether the platform is a hosted service on shared or dedicated infrastructure rather than an individual's workstation.""", json_schema_extra = { "linkml_meta": {'comments': ['Build L2 and above require a hosted platform.'],
         'domain_of': ['SlsaBuildPlatform']} })
    builder_dependencies: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""Dependencies of the platform's orchestrator that do not run inside the build but may affect provenance generation or its guarantees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildPlatform']} })


class SlsaControlPlane(ConfiguredBaseModel):
    """
    The component of a build platform that orchestrates each build and generates its provenance, outside the tenant's control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/terminology#build-model']})

    build_platform: Optional[str] = Field(default=None, description="""The build platform this party or component belongs to or uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaProducer', 'SlsaControlPlane'],
         'in_subset': ['slsa_build_track'],
         'slot_uri': 'slsa:build_platform'} })


class SlsaComponentVersion(ConfiguredBaseModel):
    """
    The version of one named component of a platform.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track']})

    component: str = Field(default=..., description="""The component's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaComponentVersion']} })
    component_version: Optional[str] = Field(default=None, description="""The component's version string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaComponentVersion']} })


class SlsaPackageRegistry(ConfiguredBaseModel):
    """
    A distribution platform that resolves package names to immutable package artifacts within an ecosystem.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_dependency_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/terminology#distribution-model']})

    ecosystem: Optional[str] = Field(default=None, description="""The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI.""", json_schema_extra = { "linkml_meta": {'comments': ['The same source can yield differently named packages in one '
                      'ecosystem, so verifiers match provenance to package names with '
                      'care (Tamanna et al., 2024, UR.1).'],
         'domain_of': ['SlsaPackageRegistry', 'SlsaPackage'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track'],
         'slot_uri': 'slsa:ecosystem'} })
    registry_uri: str = Field(default=..., description="""The URI that identifies the registry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackageRegistry']} })


class SlsaPackage(ConfiguredBaseModel):
    """
    A unit of software distributed under a package name, which is the primary security boundary SLSA protects. Its artifacts are the outputs of builds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track', 'slsa_dependency_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/terminology#distribution-model']})

    ecosystem: Optional[str] = Field(default=None, description="""The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI.""", json_schema_extra = { "linkml_meta": {'comments': ['The same source can yield differently named packages in one '
                      'ecosystem, so verifiers match provenance to package names with '
                      'care (Tamanna et al., 2024, UR.1).'],
         'domain_of': ['SlsaPackageRegistry', 'SlsaPackage'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track'],
         'slot_uri': 'slsa:ecosystem'} })
    package_name: str = Field(default=..., description="""The name consumers use to obtain the package within its ecosystem and registry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage']} })
    registry: Optional[str] = Field(default=None, description="""The registry the package is published to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage']} })
    package_artifacts: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The immutable artifacts the package name has resolved to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage']} })
    guac_uri: Optional[str] = Field(default=None, description="""Where a GUAC instance answers queries about the package's dependency and provenance graph.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage'], 'in_subset': ['slsa_ssf']} })
    security_insights_uri: Optional[str] = Field(default=None, description="""The SECURITY-INSIGHTS.yml file of the project that produces the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage'], 'in_subset': ['slsa_ssf']} })


class SlsaBuildProvenance(SlsaPredicate):
    """
    The predicate that says how a build platform produced a set of artifacts, so that consumers can verify the build met their expectations and others can rebuild it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://slsa.dev/provenance/v1.',
                      'Generating valid provenance was the most frequent adoption '
                      'difficulty practitioners reported (Tamanna et al., 2024, '
                      'CI.1).'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/build-provenance#provenance']})

    build_definition: SlsaBuildDefinition = Field(default=..., description="""The inputs to the build; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildProvenance']} })
    run_details: SlsaRunDetails = Field(default=..., description="""What is specific to this execution of the build; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildProvenance']} })
    predicate_kind: Literal["SlsaBuildProvenance"] = Field(default="SlsaBuildProvenance", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaPredicate']} })


class SlsaBuildDefinition(ConfiguredBaseModel):
    """
    The inputs to a build, in enough detail to initialize it and begin execution; the builder vouches for their accuracy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/build-provenance#builddefinition']})

    build_type: str = Field(default=..., description="""The URI of the template that says how to run the build and read its parameters and dependencies; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildDefinition']} })
    external_parameters: Optional[list[SlsaBuildParameter]] = Field(default=None, description="""The inputs under the tenant's control; complete at Build L3 and verified by consumers.""", json_schema_extra = { "linkml_meta": {'comments': ['Verifiers reject parameters they do not recognize here.'],
         'domain_of': ['SlsaBuildDefinition']} })
    internal_parameters: Optional[list[SlsaBuildParameter]] = Field(default=None, description="""The inputs the platform sets itself; kept for debugging, incident response and reproduction, and not verified by consumers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildDefinition']} })
    resolved_dependencies: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The artifacts fetched during the build, as far as the platform knows them; completeness is best effort through Build L3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildDefinition']} })
    hermetic: Optional[bool] = Field(default=None, description="""Whether the build could reach only the dependencies it declared, with no other network or filesystem access.""", json_schema_extra = { "linkml_meta": {'comments': ['Hermetic builds are an isolation property Build L3 platforms '
                      'aim for, and the one practitioners found hardest (Tamanna et '
                      'al., 2024, CI.1).'],
         'domain_of': ['SlsaBuildDefinition'],
         'in_subset': ['slsa_adoption_study']} })
    provenance_generation_tool: Optional[str] = Field(default=None, description="""The tool that generated this provenance, named by URI.""", json_schema_extra = { "linkml_meta": {'comments': ['Naming the generator supports the strategy of standardizing '
                      'provenance generation (Tamanna et al., 2024, S3.1).'],
         'domain_of': ['SlsaBuildDefinition'],
         'in_subset': ['slsa_adoption_study']} })
    pipeline_orchestrator: Optional[str] = Field(default=None, description="""The CI/CD system that coordinated the build, named by URI, where it differs from the builder.""", json_schema_extra = { "linkml_meta": {'comments': ['In the Secure Software Factory architecture this is the Build '
                      'Service layer, distinct from the provenance-generating '
                      'builder.'],
         'domain_of': ['SlsaBuildDefinition'],
         'in_subset': ['slsa_ssf']} })


class SlsaBuildParameter(ConfiguredBaseModel):
    """
    One named input to a build, with a string value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The specification recommends string values; a structured value '
                      'is written as its JSON text.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track']})

    parameter_name: str = Field(default=..., description="""The parameter's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildParameter']} })
    parameter_value: Optional[str] = Field(default=None, description="""The parameter's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildParameter']} })


class SlsaRunDetails(ConfiguredBaseModel):
    """
    What is specific to one execution of a build: the platform that ran it, metadata about the run and its by-products.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/build-provenance#rundetails']})

    builder: SlsaBuildPlatform = Field(default=..., description="""The build platform that ran the build and is trusted to have written this provenance; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaRunDetails']} })
    build_metadata: Optional[SlsaBuildMetadata] = Field(default=None, description="""Metadata about this execution of the build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaRunDetails']} })
    byproducts: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""Artifacts the build produced beside its outputs that may help debugging or incident response, such as logs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaRunDetails']} })


class SlsaBuildMetadata(ConfiguredBaseModel):
    """
    Metadata about one execution of a build: its identifier and when it started and finished.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/build-provenance#buildmetadata']})

    invocation_id: Optional[str] = Field(default=None, description="""An identifier for this build invocation, in a format the builder defines; useful for finding its logs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildMetadata']} })
    started_on: Optional[datetime ] = Field(default=None, description="""When the build started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildMetadata']} })
    finished_on: Optional[datetime ] = Field(default=None, description="""When the build finished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildMetadata']} })


class SlsaVerificationSummary(SlsaPredicate):
    """
    The predicate in which a verifier records that it evaluated artifacts against a policy and the SLSA levels they met, so consumers can rely on the verifier instead of reading every underlying attestation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://slsa.dev/verification_summary/v1.',
                      'A Source VSA is this predicate with the repository as '
                      "resource_uri and the revision id in the subject's digest.",
                      'Verification tooling and the places attestations are stored '
                      'were an adoption difficulty practitioners reported (Tamanna et '
                      'al., 2024, LF.1).'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_verification',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/verification_summary',
                      'https://slsa.dev/spec/v1.2/source-requirements#source-verification-summary-attestation'],
         'slot_usage': {'resource_uri': {'description': 'The URI consumers fetch the '
                                                        'artifact from, which the '
                                                        'verifier verified it as.',
                                         'name': 'resource_uri',
                                         'required': True}}})

    resource_uri: str = Field(default=..., description="""The URI consumers fetch the artifact from, which the verifier verified it as.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaVerificationSummary'],
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'slot_uri': 'slsa:resource_uri'} })
    verifier: SlsaVerifier = Field(default=..., description="""The verifier that made this determination.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    time_verified: Optional[datetime ] = Field(default=None, description="""When the verification happened.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    policy: InTotoResourceDescriptor = Field(default=..., description="""The policy the subject was verified against, by URI and preferably by digest too.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    input_attestations: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""Every attestation the verifier consulted, each with a digest; complete when present.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    verification_result: SlsaVerificationResult = Field(default=..., description="""Whether the subject passed the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    verified_levels: list[SlsaResult] = Field(default=..., description="""The highest level verified in each track, and any verified property; a level implies the levels below it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    organization_properties: Optional[list[str]] = Field(default=None, description="""Properties an organization defines for its own consumers, each prefixed ORG_SOURCE_.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary'], 'in_subset': ['slsa_source_track']} })
    dependency_levels: Optional[list[SlsaDependencyLevelCount]] = Field(default=None, description="""How many transitive dependencies were verified at each level; absent when the verifier makes no claim about dependencies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    slsa_version: Optional[str] = Field(default=None, description="""The SLSA specification version the verifier applied, as MAJOR.MINOR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    predicate_kind: Literal["SlsaVerificationSummary"] = Field(default="SlsaVerificationSummary", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaPredicate']} })

    @field_validator('organization_properties')
    def pattern_organization_properties(cls, v):
        pattern=re.compile(r"^ORG_SOURCE_")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid organization_properties format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid organization_properties format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('slsa_version')
    def pattern_slsa_version(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid slsa_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid slsa_version format: {v}"
            raise ValueError(err_msg)
        return v


class SlsaDependencyLevelCount(ConfiguredBaseModel):
    """
    The number of an artifact's transitive dependencies verified at one level, each counted once per track at its highest level.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_verification',
         'in_subset': ['slsa_build_track']})

    verified_level: SlsaResult = Field(default=..., description="""The level the dependencies were verified at.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyLevelCount']} })
    dependency_count: int = Field(default=..., description="""How many dependencies were verified at that level.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyLevelCount']} })


class SlsaSourceControlSystem(ConfiguredBaseModel):
    """
    The platform or services that host a source repository and enforce its organization's policies on authentication, authorization and change management.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The SCS issues the Source VSAs and source provenance for the '
                      'revisions it hosts.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/source-requirements#definitions']})

    scs_uri: str = Field(default=..., description="""The URI that identifies the source control system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceControlSystem']} })


class SlsaSourceRepository(ConfiguredBaseModel):
    """
    A self-contained unit that holds a set of files, their revision history and metadata such as branches and tags.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/source-requirements#definitions']})

    repository_uri: str = Field(default=..., description="""The stable locator the SCS gives the repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRepository']} })
    hosted_by: Optional[str] = Field(default=None, description="""The source control system that hosts the repository.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRepository']} })


class SlsaSourceRevision(ConfiguredBaseModel):
    """
    A logically immutable snapshot of a repository's tracked files, with its version-control metadata: author, time and parent revisions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A revision id is unique within its repository and may recur in '
                      'another; a document that holds revisions from several '
                      'repositories qualifies them.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/source-requirements#definitions']})

    repository: Optional[str] = Field(default=None, description="""The source repository this belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision', 'SlsaNamedReference'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:repository'} })
    revision_id: str = Field(default=..., description="""The revision identifier the SCS assigns, such as a git commit id or a path- qualified sequence number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision']} })
    authored_by: Optional[str] = Field(default=None, description="""The identity of the person or automation that authored the revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision']} })
    authored_at: Optional[datetime ] = Field(default=None, description="""When the revision was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision']} })
    parent_revisions: Optional[list[str]] = Field(default=None, description="""The revisions this one descends from, which together form the change history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision']} })
    source_level: Optional[SlsaSourceLevel] = Field(default=None, description="""The SLSA Source level the SCS asserts for the revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision']} })
    review_type: Optional[SlsaReviewType] = Field(default=None, description="""The form of review that approved the revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision'], 'in_subset': ['slsa_adoption_study']} })


class SlsaNamedReference(ConfiguredBaseModel):
    """
    A user-friendly name for a revision in a repository, such as main or v1.2.3; reference_type says whether it is a branch or a tag.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/source-requirements#definitions']})

    repository: Optional[str] = Field(default=None, description="""The source repository this belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision', 'SlsaNamedReference'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:repository'} })
    revision: Optional[str] = Field(default=None, description="""The source revision this refers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference', 'SlsaSourceProvenance'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:revision'} })
    reference_type: Literal["SlsaNamedReference"] = Field(default="SlsaNamedReference", description="""The kind of named reference, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaNamedReference']} })
    reference_name: str = Field(default=..., description="""The reference's name, fully qualified in git, such as refs/heads/main.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference']} })
    protected: Optional[bool] = Field(default=None, description="""Whether the organization has the SCS enforce its technical controls on this reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference']} })


class SlsaBranch(SlsaNamedReference):
    """
    A named reference that moves to track a line of development.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track']})

    repository: Optional[str] = Field(default=None, description="""The source repository this belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision', 'SlsaNamedReference'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:repository'} })
    revision: Optional[str] = Field(default=None, description="""The source revision this refers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference', 'SlsaSourceProvenance'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:revision'} })
    reference_type: Literal["SlsaBranch"] = Field(default="SlsaBranch", description="""The kind of named reference, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaNamedReference']} })
    reference_name: str = Field(default=..., description="""The reference's name, fully qualified in git, such as refs/heads/main.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference']} })
    protected: Optional[bool] = Field(default=None, description="""Whether the organization has the SCS enforce its technical controls on this reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference']} })


class SlsaTag(SlsaNamedReference):
    """
    A named reference meant never to move once created.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A version-control tag that is allowed to move, such as latest, '
                      'is a named reference and not a tag in this sense.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track']})

    repository: Optional[str] = Field(default=None, description="""The source repository this belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaSourceRevision', 'SlsaNamedReference'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:repository'} })
    revision: Optional[str] = Field(default=None, description="""The source revision this refers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference', 'SlsaSourceProvenance'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:revision'} })
    reference_type: Literal["SlsaTag"] = Field(default="SlsaTag", description="""The kind of named reference, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaNamedReference']} })
    reference_name: str = Field(default=..., description="""The reference's name, fully qualified in git, such as refs/heads/main.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference']} })
    protected: Optional[bool] = Field(default=None, description="""Whether the organization has the SCS enforce its technical controls on this reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference']} })


class SlsaSourceProvenance(SlsaPredicate):
    """
    Evidence from an SCS of how a revision came to exist and which technical controls were enforced when it did.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['SLSA leaves the format of source provenance to each SCS and '
                      'defines no predicate type for it; this class holds what the '
                      'specification says such provenance conveys.',
                      'Source L2 and above require the SCS to issue it with each new '
                      'revision.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_source',
         'in_subset': ['slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/source-requirements#source-provenance-attestations'],
         'slot_usage': {'revision': {'name': 'revision', 'required': True}}})

    revision: str = Field(default=..., description="""The source revision this refers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaNamedReference', 'SlsaSourceProvenance'],
         'in_subset': ['slsa_source_track'],
         'slot_uri': 'slsa:revision'} })
    controls_enforced: Optional[list[str]] = Field(default=None, description="""The technical controls the SCS enforced when the revision was created, as the organization documents them.""", json_schema_extra = { "linkml_meta": {'comments': ['Two-party review is a control many single-maintainer projects '
                      'cannot meet (Tamanna et al., 2024, LF.2).'],
         'domain_of': ['SlsaSourceProvenance']} })
    predicate_kind: Literal["SlsaSourceProvenance"] = Field(default="SlsaSourceProvenance", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaPredicate']} })


class SlsaDependencyInventory(ConfiguredBaseModel):
    """
    The inventory of every third-party build dependency, direct and transitive, of one artifact version.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The Dependency track is a working draft and not part of the '
                      'SLSA v1.2 release.',
                      'A build-time SBOM or a lock file with hashes is a common form '
                      'of the inventory.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_dependency',
         'in_subset': ['slsa_dependency_track'],
         'see_also': ['https://slsa.dev/spec/draft/dependency-track']})

    artifact: InTotoResourceDescriptor = Field(default=..., description="""The artifact whose dependencies are inventoried.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyInventory']} })
    dependencies: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The dependencies, each identified by URI and digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyInventory']} })
    dependency_level: Optional[SlsaDependencyLevel] = Field(default=None, description="""The SLSA Dependency level the producer's process meets for this artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyInventory']} })


class SlsaBuildImageProducer(SlsaParty):
    """
    The party that creates and distributes build images; the hosted build platform itself, or a third party in a bring-your-own-image setting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build_environment',
         'in_subset': ['slsa_build_environment_track'],
         'see_also': ['https://slsa.dev/spec/draft/build-env-track-basics#build-environment-model']})

    party_type: Literal["SlsaBuildImageProducer"] = Field(default="SlsaBuildImageProducer", description="""The role the party acts in, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaParty']} })
    party_name: Optional[str] = Field(default=None, description="""The party's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaParty']} })


class SlsaBuildImage(ConfiguredBaseModel):
    """
    The template a build environment is instantiated from, such as a VM or container image: root filesystem, guest OS and packages, build executor and build agent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The Build Environment track is a working draft and not part of '
                      'the SLSA v1.2 release.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build_environment',
         'in_subset': ['slsa_build_environment_track'],
         'see_also': ['https://slsa.dev/spec/draft/build-env-track-basics#build-environment-model']})

    build_env_level: Optional[SlsaBuildEnvironmentLevel] = Field(default=None, description="""The SLSA Build Environment level this meets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildImage', 'SlsaBuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_environment_track'],
         'slot_uri': 'slsa:build_env_level'} })
    image_uri: str = Field(default=..., description="""The URI that identifies the image version, such as an OCI reference with its digest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildImage']} })
    provenance: Optional[SlsaBuildProvenance] = Field(default=None, description="""The build provenance of the image itself, required at Build Environment L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildImage']} })
    produced_by: Optional[SlsaBuildImageProducer] = Field(default=None, description="""The party that created and distributes the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildImage']} })


class SlsaMeasurement(ConfiguredBaseModel):
    """
    The digest of one component or state of a build environment, to compare with its reference value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build_environment',
         'in_subset': ['slsa_build_environment_track'],
         'see_also': ['https://slsa.dev/spec/draft/build-env-track-basics#build-environment-model']})

    digest: Optional[InTotoDigestSet] = Field(default=None, description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaMeasurement'],
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'slot_uri': 'slsa:digest'} })
    measured_component: str = Field(default=..., description="""The component or state that was measured, such as the bootloader, guest kernel, build agent or root filesystem.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaMeasurement']} })


class SlsaBuildEnvironmentAttestation(SlsaPredicate):
    """
    Evidence of the state of a build environment when a build was dispatched to it: the image it came from and the measurements taken at boot.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The track names no single predicate type; platforms issue this '
                      'evidence in formats such as SCAI or a VSA.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build_environment',
         'in_subset': ['slsa_build_environment_track'],
         'see_also': ['https://slsa.dev/spec/draft/build-env-track-basics#buildenv-levels']})

    build_env_level: Optional[SlsaBuildEnvironmentLevel] = Field(default=None, description="""The SLSA Build Environment level this meets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildImage', 'SlsaBuildEnvironmentAttestation'],
         'in_subset': ['slsa_build_environment_track'],
         'slot_uri': 'slsa:build_env_level'} })
    build_id: str = Field(default=..., description="""The immutable identifier of the build execution the environment was assigned to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildEnvironmentAttestation']} })
    build_image: Optional[str] = Field(default=None, description="""The image the environment was instantiated from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildEnvironmentAttestation']} })
    measurements: Optional[list[SlsaMeasurement]] = Field(default=None, description="""The measurements of the environment's components taken during boot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildEnvironmentAttestation']} })
    predicate_kind: Literal["SlsaBuildEnvironmentAttestation"] = Field(default="SlsaBuildEnvironmentAttestation", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['SlsaPredicate']} })


class SlsaAdoptionMetadata(ConfiguredBaseModel):
    """
    The adoption challenges a deployment meets and the strategies it applies, from the study's taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_adoption',
         'in_subset': ['slsa_adoption_study'],
         'notes': ['The study analysed 1,523 SLSA-related GitHub issues from 233 '
                   'repositories and derived four challenge themes and five strategy '
                   'themes.'],
         'see_also': ['https://arxiv.org/abs/2409.05014']})

    challenges: Optional[list[SlsaAdoptionChallenge]] = Field(default=None, description="""The challenge themes that apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaAdoptionMetadata']} })
    strategies: Optional[list[SlsaAdoptionStrategy]] = Field(default=None, description="""The strategy themes applied or recommended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaAdoptionMetadata']} })


class SlsaDocument(ConfiguredBaseModel):
    """
    A document that holds SLSA attestations and the parties, platforms, packages, repositories and images they concern.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa', 'tree_root': True})

    attestations: Optional[list[InTotoStatement]] = Field(default=None, description="""The attestations, as in-toto statements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    parties: Optional[list[Union[SlsaProducer,SlsaConsumer,SlsaVerifier,SlsaInfrastructureProvider,SlsaBuildImageProducer]]] = Field(default=None, description="""The parties, each in its role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    build_platforms: Optional[list[SlsaBuildPlatform]] = Field(default=None, description="""The build platforms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    packages: Optional[list[SlsaPackage]] = Field(default=None, description="""The packages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    package_registries: Optional[list[SlsaPackageRegistry]] = Field(default=None, description="""The package registries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    source_control_systems: Optional[list[SlsaSourceControlSystem]] = Field(default=None, description="""The source control systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    source_repositories: Optional[list[SlsaSourceRepository]] = Field(default=None, description="""The source repositories.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    source_revisions: Optional[list[SlsaSourceRevision]] = Field(default=None, description="""The source revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    named_references: Optional[list[Union[SlsaNamedReference,SlsaBranch,SlsaTag]]] = Field(default=None, description="""The branches and tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    build_images: Optional[list[SlsaBuildImage]] = Field(default=None, description="""The build images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    dependency_inventories: Optional[list[SlsaDependencyInventory]] = Field(default=None, description="""The dependency inventories.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    adoption_metadata: Optional[SlsaAdoptionMetadata] = Field(default=None, description="""How the deployment the document describes fares against the adoption study's themes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
InTotoDigestSet.model_rebuild()
InTotoAnnotation.model_rebuild()
InTotoResourceDescriptor.model_rebuild()
InTotoStatement.model_rebuild()
SlsaPredicate.model_rebuild()
SlsaParty.model_rebuild()
SlsaProducer.model_rebuild()
SlsaConsumer.model_rebuild()
SlsaVerifier.model_rebuild()
SlsaInfrastructureProvider.model_rebuild()
SlsaBuildPlatform.model_rebuild()
SlsaControlPlane.model_rebuild()
SlsaComponentVersion.model_rebuild()
SlsaPackageRegistry.model_rebuild()
SlsaPackage.model_rebuild()
SlsaBuildProvenance.model_rebuild()
SlsaBuildDefinition.model_rebuild()
SlsaBuildParameter.model_rebuild()
SlsaRunDetails.model_rebuild()
SlsaBuildMetadata.model_rebuild()
SlsaVerificationSummary.model_rebuild()
SlsaDependencyLevelCount.model_rebuild()
SlsaSourceControlSystem.model_rebuild()
SlsaSourceRepository.model_rebuild()
SlsaSourceRevision.model_rebuild()
SlsaNamedReference.model_rebuild()
SlsaBranch.model_rebuild()
SlsaTag.model_rebuild()
SlsaSourceProvenance.model_rebuild()
SlsaDependencyInventory.model_rebuild()
SlsaBuildImageProducer.model_rebuild()
SlsaBuildImage.model_rebuild()
SlsaMeasurement.model_rebuild()
SlsaBuildEnvironmentAttestation.model_rebuild()
SlsaAdoptionMetadata.model_rebuild()
SlsaDocument.model_rebuild()
