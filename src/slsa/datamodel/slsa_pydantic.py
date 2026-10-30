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
    No Source track guarantees; a revision for which the SCS issues no Source VSA is at this level.
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
    A tool or bot reviewed the change with no second person, which is not two-party review.
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
    Make SLSA fit more contexts, with build-system tracks, gamified levels, flexibility for varied organizations and alignment with OpenSSF practices.
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

    build_platform: Optional[URI] = Field(default=None, description="""The build platform this party or component belongs to or uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaProducer', 'SlsaControlPlane'],
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
    verifier_id: URI = Field(default=..., description="""The URI that identifies the verifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerifier']} })
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
    builder_id: URI = Field(default=..., description="""The URI that identifies the platform and determines its SLSA Build level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildPlatform']} })
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

    build_platform: Optional[URI] = Field(default=None, description="""The build platform this party or component belongs to or uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaProducer', 'SlsaControlPlane'],
         'in_subset': ['slsa_build_track'],
         'slot_uri': 'slsa:build_platform'} })


class SlsaComponentVersion(ConfiguredBaseModel):
    """
    The version of one named component of a platform.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["Each component appears once in a list, since the attestation's "
                      'JSON uses its name as a key; the validator does not check '
                      'this.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
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

    ecosystem: Optional[str] = Field(default=None, description="""The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI.""", json_schema_extra = { "linkml_meta": {'comments': ["One ecosystem's tools can name the same package differently, "
                      'which the study found affects attestations and provenance, so '
                      'verifiers match provenance to package names with care (Tamanna '
                      'et al., 2024, UR.1).'],
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

    ecosystem: Optional[str] = Field(default=None, description="""The package ecosystem whose rules govern how a package is named and distributed, such as PyPA, npm or OCI.""", json_schema_extra = { "linkml_meta": {'comments': ["One ecosystem's tools can name the same package differently, "
                      'which the study found affects attestations and provenance, so '
                      'verifiers match provenance to package names with care (Tamanna '
                      'et al., 2024, UR.1).'],
         'domain_of': ['SlsaPackageRegistry', 'SlsaPackage'],
         'in_subset': ['slsa_build_track', 'slsa_dependency_track'],
         'slot_uri': 'slsa:ecosystem'} })
    package_name: str = Field(default=..., description="""The name consumers use to obtain the package within its ecosystem and registry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage']} })
    registry: Optional[str] = Field(default=None, description="""The registry the package is published to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage']} })
    package_artifacts: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The immutable artifacts the package name has resolved to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage']} })
    guac_uri: Optional[str] = Field(default=None, description="""Where a GUAC instance answers queries about the package's dependency and provenance graph.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage'], 'in_subset': ['slsa_ssf']} })
    security_insights_uri: Optional[str] = Field(default=None, description="""The SECURITY-INSIGHTS.yml file of the project that produces the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaPackage'], 'in_subset': ['slsa_ssf']} })


class SlsaBuildDefinition(ConfiguredBaseModel):
    """
    The inputs to a build, in enough detail to initialize it and begin execution; the builder vouches for their accuracy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/build-provenance#builddefinition']})

    build_type: URI = Field(default=..., description="""The URI of the template that says how to run the build and read its parameters and dependencies; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildDefinition']} })
    external_parameters: list[SlsaBuildParameter] = Field(default=..., description="""The inputs under the tenant's control; required at Build L1, complete at Build L3 and verified by consumers.""", min_length=1, json_schema_extra = { "linkml_meta": {'comments': ['Verifiers reject parameters they do not recognize here.'],
         'domain_of': ['SlsaBuildDefinition']} })
    internal_parameters: Optional[list[SlsaBuildParameter]] = Field(default=None, description="""The inputs the platform sets itself; kept for debugging, incident response and reproduction, and not verified by consumers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildDefinition']} })
    resolved_dependencies: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The artifacts fetched during the build, as far as the platform knows them; completeness is best effort through Build L3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildDefinition']} })
    hermetic: Optional[bool] = Field(default=None, description="""Whether the build could reach only the dependencies it declared, with no other network or filesystem access.""", json_schema_extra = { "linkml_meta": {'comments': ["SLSA v1.2 does not require hermetic builds; Build L3's "
                      'isolation is a different property, and hermeticity is a '
                      'candidate for a future Build L4.',
                      'The study cites a 2023 industry survey in which over half the '
                      'participants found hermetic builds hard to implement, and lists '
                      '"hermetic build" among SLSA\'s unclear terms (Tamanna et al., '
                      '2024, UC.1).'],
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
                      'is written as its JSON text.',
                      "Each name appears once in a list, since the attestation's JSON "
                      'uses it as a key; the validator does not check this.'],
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
    started_on: Optional[str] = Field(default=None, description="""When the build started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildMetadata']} })
    finished_on: Optional[str] = Field(default=None, description="""When the build finished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildMetadata']} })


class SlsaDependencyLevelCount(ConfiguredBaseModel):
    """
    The number of an artifact's transitive dependencies verified at one level, each counted once per track at its highest level.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["Each level appears once in a list, since the attestation's JSON "
                      'uses it as a key; the validator does not check this.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_verification',
         'in_subset': ['slsa_build_track']})

    verified_level: str = Field(default=..., description="""The level the dependencies were verified at, or a result of the issuer's own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyLevelCount']} })
    dependency_count: int = Field(default=..., description="""How many dependencies were verified at that level.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyLevelCount']} })

    @field_validator('verified_level')
    def pattern_verified_level(cls, v):
        pattern=re.compile(r"^(SLSA_BUILD_LEVEL_(UNEVALUATED|[0-3])|SLSA_SOURCE_LEVEL_(UNEVALUATED|[0-4])|SLSA_SOURCE_TWO_PARTY_REVIEWED|SLSA_BUILD_REPRODUCED|([!-RT-rt-~]|[Ss]$|[Ss][!-KM-km-~]|[Ss][Ll]$|[Ss][Ll][!-RT-rt-~]|[Ss][Ll][Ss]$|[Ss][Ll][Ss][!-@B-`b-~]|[Ss][Ll][Ss][Aa]$|[Ss][Ll][Ss][Aa][!-^`-~])[!-~]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid verified_level format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid verified_level format: {v}"
            raise ValueError(err_msg)
        return v


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
    dependencies: Optional[list[InTotoResourceDescriptor]] = Field(default=None, description="""The dependencies, each as a resource descriptor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyInventory']} })
    dependency_level: Optional[SlsaDependencyLevel] = Field(default=None, description="""The SLSA Dependency level the producer's process meets for this artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDependencyInventory']} })


class InTotoDigestSet(ConfiguredBaseModel):
    """
    A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'sha256': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha256',
                                                    'required': True}}},
                    {'slot_conditions': {'sha224': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha224',
                                                    'required': True}}},
                    {'slot_conditions': {'sha384': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha384',
                                                    'required': True}}},
                    {'slot_conditions': {'sha512': {'any_of': [{'range': 'string'}],
                                                    'name': 'sha512',
                                                    'required': True}}},
                    {'slot_conditions': {'sha512_224': {'any_of': [{'range': 'string'}],
                                                        'name': 'sha512_224',
                                                        'required': True}}},
                    {'slot_conditions': {'sha512_256': {'any_of': [{'range': 'string'}],
                                                        'name': 'sha512_256',
                                                        'required': True}}},
                    {'slot_conditions': {'sha3_224': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_224',
                                                      'required': True}}},
                    {'slot_conditions': {'sha3_256': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_256',
                                                      'required': True}}},
                    {'slot_conditions': {'sha3_384': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_384',
                                                      'required': True}}},
                    {'slot_conditions': {'sha3_512': {'any_of': [{'range': 'string'}],
                                                      'name': 'sha3_512',
                                                      'required': True}}},
                    {'slot_conditions': {'shake128': {'any_of': [{'range': 'string'}],
                                                      'name': 'shake128',
                                                      'required': True}}},
                    {'slot_conditions': {'shake256': {'any_of': [{'range': 'string'}],
                                                      'name': 'shake256',
                                                      'required': True}}},
                    {'slot_conditions': {'blake2b': {'any_of': [{'range': 'string'}],
                                                     'name': 'blake2b',
                                                     'required': True}}},
                    {'slot_conditions': {'blake2s': {'any_of': [{'range': 'string'}],
                                                     'name': 'blake2s',
                                                     'required': True}}},
                    {'slot_conditions': {'ripemd160': {'any_of': [{'range': 'string'}],
                                                       'name': 'ripemd160',
                                                       'required': True}}},
                    {'slot_conditions': {'sm3': {'any_of': [{'range': 'string'}],
                                                 'name': 'sm3',
                                                 'required': True}}},
                    {'slot_conditions': {'gost': {'any_of': [{'range': 'string'}],
                                                  'name': 'gost',
                                                  'required': True}}},
                    {'slot_conditions': {'sha1': {'any_of': [{'range': 'string'}],
                                                  'name': 'sha1',
                                                  'required': True}}},
                    {'slot_conditions': {'md5': {'any_of': [{'range': 'string'}],
                                                 'name': 'md5',
                                                 'required': True}}},
                    {'slot_conditions': {'dir_hash': {'any_of': [{'range': 'string'}],
                                                      'name': 'dir_hash',
                                                      'required': True}}},
                    {'slot_conditions': {'git_commit': {'any_of': [{'range': 'string'}],
                                                        'name': 'git_commit',
                                                        'required': True}}},
                    {'slot_conditions': {'git_tree': {'any_of': [{'range': 'string'}],
                                                      'name': 'git_tree',
                                                      'required': True}}},
                    {'slot_conditions': {'git_blob': {'any_of': [{'range': 'string'}],
                                                      'name': 'git_blob',
                                                      'required': True}}},
                    {'slot_conditions': {'git_tag': {'any_of': [{'range': 'string'}],
                                                     'name': 'git_tag',
                                                     'required': True}}},
                    {'slot_conditions': {'additional_digests': {'multivalued': True,
                                                                'name': 'additional_digests',
                                                                'required': True}}}],
         'comments': ['The named algorithms take lowercase hexadecimal, and '
                      "additional_digests holds any other algorithm, such as an SCS's "
                      'own revision type.',
                      'A consumer accepts only the algorithms it considers secure and '
                      'ignores the rest, and two sets match when any accepted '
                      'algorithm matches.',
                      'SHAKE and BLAKE2 digests can be of any length, and this schema '
                      'asks for at least 32 bytes, since a shorter digest resists '
                      'collisions too weakly to identify an artifact.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'notes': ['Each condition in any_of names its range through a nested any_of, '
                   "because the JSON Schema generator leaves a condition's own range "
                   'out, and a null value would then count as present.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md']})

    sha256: Optional[str] = Field(default=None, description="""The SHA-256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha256'} })
    sha224: Optional[str] = Field(default=None, description="""The SHA-224 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha224'} })
    sha384: Optional[str] = Field(default=None, description="""The SHA-384 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha384'} })
    sha512: Optional[str] = Field(default=None, description="""The SHA-512 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha512'} })
    sha512_224: Optional[str] = Field(default=None, description="""The SHA-512/224 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha512_224'} })
    sha512_256: Optional[str] = Field(default=None, description="""The SHA-512/256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha512_256'} })
    sha3_224: Optional[str] = Field(default=None, description="""The SHA3-224 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha3_224'} })
    sha3_256: Optional[str] = Field(default=None, description="""The SHA3-256 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha3_256'} })
    sha3_384: Optional[str] = Field(default=None, description="""The SHA3-384 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha3_384'} })
    sha3_512: Optional[str] = Field(default=None, description="""The SHA3-512 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sha3_512'} })
    shake128: Optional[str] = Field(default=None, description="""The SHAKE128 digest of the artifact, of at least 32 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:shake128'} })
    shake256: Optional[str] = Field(default=None, description="""The SHAKE256 digest of the artifact, of at least 32 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:shake256'} })
    blake2b: Optional[str] = Field(default=None, description="""The BLAKE2b digest of the artifact, of 32 to 64 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:blake2b'} })
    blake2s: Optional[str] = Field(default=None, description="""The BLAKE2s digest of the artifact, at its full 32 bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:blake2s'} })
    ripemd160: Optional[str] = Field(default=None, description="""The RIPEMD-160 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:ripemd160'} })
    sm3: Optional[str] = Field(default=None, description="""The SM3 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:sm3'} })
    gost: Optional[str] = Field(default=None, description="""The GOST R 34.11 digest of the artifact, of 256 or 512 bits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:gost'} })
    sha1: Optional[str] = Field(default=None, description="""The SHA-1 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'comments': ['SHA-1 lacks collision resistance, so most consumers should not '
                      'rely on it.'],
         'domain_of': ['InTotoDigestSet'],
         'slot_uri': 'in_toto_linkml:sha1'} })
    md5: Optional[str] = Field(default=None, description="""The MD5 digest of the artifact.""", json_schema_extra = { "linkml_meta": {'comments': ['MD5 lacks collision resistance, so most consumers should not '
                      'accept it.'],
         'domain_of': ['InTotoDigestSet'],
         'slot_uri': 'in_toto_linkml:md5'} })
    dir_hash: Optional[str] = Field(default=None, description="""A digest over a directory's content by the dirhash Hash1 function, in lowercase hexadecimal rather than base64.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:dir_hash'} })
    git_commit: Optional[str] = Field(default=None, description="""The git commit id of a source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:git_commit'} })
    git_tree: Optional[str] = Field(default=None, description="""The git tree id of a source revision's content, or of any file tree.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:git_tree'} })
    git_blob: Optional[str] = Field(default=None, description="""The git blob id of a file's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:git_blob'} })
    git_tag: Optional[str] = Field(default=None, description="""The git object id of an annotated tag.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'], 'slot_uri': 'in_toto_linkml:git_tag'} })
    additional_digests: Optional[list[InTotoAdditionalDigest]] = Field(default=None, description="""The digests under algorithms this class does not name.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoDigestSet'],
         'slot_uri': 'in_toto_linkml:additional_digests'} })

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

    @field_validator('sha224')
    def pattern_sha224(cls, v):
        pattern=re.compile(r"^[a-f0-9]{56}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha224 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha224 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha384')
    def pattern_sha384(cls, v):
        pattern=re.compile(r"^[a-f0-9]{96}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha384 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha384 format: {v}"
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

    @field_validator('sha512_224')
    def pattern_sha512_224(cls, v):
        pattern=re.compile(r"^[a-f0-9]{56}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha512_224 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha512_224 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha512_256')
    def pattern_sha512_256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha512_256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha512_256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_224')
    def pattern_sha3_224(cls, v):
        pattern=re.compile(r"^[a-f0-9]{56}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_224 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_224 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_256')
    def pattern_sha3_256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_384')
    def pattern_sha3_384(cls, v):
        pattern=re.compile(r"^[a-f0-9]{96}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_384 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_384 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha3_512')
    def pattern_sha3_512(cls, v):
        pattern=re.compile(r"^[a-f0-9]{128}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha3_512 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha3_512 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('shake128')
    def pattern_shake128(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{2})*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid shake128 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid shake128 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('shake256')
    def pattern_shake256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{2})*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid shake256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid shake256 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('blake2b')
    def pattern_blake2b(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{2}){0,32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid blake2b format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid blake2b format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('blake2s')
    def pattern_blake2s(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid blake2s format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid blake2s format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ripemd160')
    def pattern_ripemd160(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ripemd160 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ripemd160 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sm3')
    def pattern_sm3(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sm3 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sm3 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('gost')
    def pattern_gost(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}([a-f0-9]{64})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gost format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gost format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sha1')
    def pattern_sha1(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid sha1 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid sha1 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('md5')
    def pattern_md5(cls, v):
        pattern=re.compile(r"^[a-f0-9]{32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid md5 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid md5 format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('dir_hash')
    def pattern_dir_hash(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid dir_hash format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid dir_hash format: {v}"
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

    @field_validator('git_blob')
    def pattern_git_blob(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_blob format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_blob format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('git_tag')
    def pattern_git_tag(cls, v):
        pattern=re.compile(r"^[a-f0-9]{40}([a-f0-9]{24})?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid git_tag format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid git_tag format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoAdditionalDigest(ConfiguredBaseModel):
    """
    One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["In the attestation's JSON the algorithm is a key of the digest "
                      'set beside the named ones, and an algorithm the framework does '
                      'not define documents how its value is encoded.',
                      'An SCS that does not use cryptographic digests defines a '
                      'canonical revision type of its own that includes the '
                      'repository, such as svn_revision_id.',
                      "Each algorithm appears once in a list, since the attestation's "
                      'JSON uses it as a key; the validator does not check this.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md']})

    algorithm: str = Field(default=..., description="""The algorithm's name, as the key the attestation's JSON uses, such as svn_revision_id.""", json_schema_extra = { "linkml_meta": {'comments': ['An algorithm that InTotoDigestSet names, by its JSON key or by '
                      'its field name, goes in that field instead.',
                      "A name starts with a lowercase letter, as the framework's own "
                      'names do, so that SHA256 is not taken for sha256, and it may '
                      "hold a colon, as go-witness's gitoid:sha256 does. The framework "
                      'itself sets no rule for other names.'],
         'domain_of': ['InTotoAdditionalDigest'],
         'none_of': [{'equals_string_in': ['sha256',
                                           'sha224',
                                           'sha384',
                                           'sha512',
                                           'sha512_224',
                                           'sha512_256',
                                           'sha3_224',
                                           'sha3_256',
                                           'sha3_384',
                                           'sha3_512',
                                           'shake128',
                                           'shake256',
                                           'blake2b',
                                           'blake2s',
                                           'ripemd160',
                                           'sm3',
                                           'gost',
                                           'sha1',
                                           'md5',
                                           'dirHash',
                                           'gitCommit',
                                           'gitTree',
                                           'gitBlob',
                                           'gitTag',
                                           'dir_hash',
                                           'git_commit',
                                           'git_tree',
                                           'git_blob',
                                           'git_tag']}],
         'slot_uri': 'spdx:algorithm'} })
    value: str = Field(default=..., description="""The digest under that algorithm, in the encoding the algorithm documents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAdditionalDigest'], 'slot_uri': 'in_toto_linkml:value'} })

    @field_validator('algorithm')
    def pattern_algorithm(cls, v):
        pattern=re.compile(r"^[a-z][A-Za-z0-9_.:-]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid algorithm format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid algorithm format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid value format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid value format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoAnnotation(ConfiguredBaseModel):
    """
    One vendor-specific annotation on a resource descriptor: a key and its values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["The attestation's JSON allows any JSON value. A string becomes "
                      'one value and an array one value per item; any other value or '
                      'item is written as its JSON text, so one value cannot tell a '
                      'string from a one-item array.',
                      "Each key appears once in a list, since the attestation's JSON "
                      'uses it as a key; the validator does not check this.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core'})

    annotation_key: str = Field(default=..., description="""The annotation's key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAnnotation'], 'slot_uri': 'in_toto_linkml:annotation_key'} })
    annotation_values: Optional[list[str]] = Field(default=None, description="""The annotation's values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoAnnotation'],
         'slot_uri': 'in_toto_linkml:annotation_values'} })


class InTotoResourceDescriptor(ConfiguredBaseModel):
    """
    A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with optional metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'resource_uri': {'any_of': [{'range': 'uri'}],
                                                          'name': 'resource_uri',
                                                          'required': True}}},
                    {'slot_conditions': {'digest': {'any_of': [{'range': 'InTotoDigestSet'}],
                                                    'name': 'digest',
                                                    'required': True}}},
                    {'slot_conditions': {'content': {'any_of': [{'range': 'string'}],
                                                     'name': 'content',
                                                     'required': True}}}],
         'comments': ['A descriptor carries at least one of a URI, a digest or its '
                      'content; a field that needs a particular one says so.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'notes': ['Each condition in any_of names its range through a nested any_of, '
                   "because the JSON Schema generator leaves a condition's own range "
                   'out, and a null value would then count as present.'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/resource_descriptor.md']})

    resource_uri: Optional[URI] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary', 'InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: Optional[InTotoDigestSet] = Field(default=None, description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaMeasurement'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:resource_name'} })
    download_location: Optional[URI] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:download_location'} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:content'} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:annotations'} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class SlsaVerificationSummaryPolicy(InTotoResourceDescriptor):
    """
    The policy a verification summary applied: a resource descriptor that names the policy by URI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A digest is recommended as well, to pin the exact version of '
                      'the policy.'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_verification',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/verification_summary#policy'],
         'slot_usage': {'digest': {'name': 'digest', 'recommended': True},
                        'resource_uri': {'name': 'resource_uri', 'required': True}}})

    resource_uri: URI = Field(default=..., description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary', 'InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: Optional[InTotoDigestSet] = Field(default=None, description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaMeasurement'],
         'recommended': True,
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:resource_name'} })
    download_location: Optional[URI] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:download_location'} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:content'} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:annotations'} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class SlsaVerificationSummaryInputAttestation(InTotoResourceDescriptor):
    """
    One attestation a verifier consulted: a resource descriptor that carries the attestation's digest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/slsa/slsa_verification',
         'in_subset': ['slsa_build_track', 'slsa_source_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/verification_summary#inputAttestations'],
         'slot_usage': {'digest': {'name': 'digest', 'required': True},
                        'resource_uri': {'name': 'resource_uri', 'recommended': True}}})

    resource_uri: Optional[URI] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary', 'InTotoResourceDescriptor'],
         'recommended': True,
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: InTotoDigestSet = Field(default=..., description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaMeasurement'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:resource_name'} })
    download_location: Optional[URI] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:download_location'} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:content'} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:annotations'} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoStatementSubject(InTotoResourceDescriptor):
    """
    One artifact an in-toto statement is about: a resource descriptor that carries a digest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/statement.md'],
         'slot_usage': {'digest': {'name': 'digest', 'required': True}}})

    resource_uri: Optional[URI] = Field(default=None, description="""The URI that identifies a resource, such as a package URL, a git repository address or an OCI image reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary', 'InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    digest: InTotoDigestSet = Field(default=..., description="""The cryptographic digests of a resource's content, keyed by algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor', 'SlsaMeasurement'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
    resource_name: Optional[str] = Field(default=None, description="""A name for the resource within the attestation that carries it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:resource_name'} })
    download_location: Optional[URI] = Field(default=None, description="""Where the resource can be fetched, when that differs from its identifying URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:download_location'} })
    media_type: Optional[str] = Field(default=None, description="""The IANA media type of the resource's content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'], 'slot_uri': 'dcat:mediaType'} })
    content: Optional[str] = Field(default=None, description="""The resource's content itself, base64-encoded, for a resource small enough to carry inline.""", json_schema_extra = { "linkml_meta": {'comments': ['The in-toto framework asks for content under 1 KB, so that '
                      'attestations stay small.'],
         'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:content'} })
    annotations: Optional[list[InTotoAnnotation]] = Field(default=None, description="""Vendor-specific annotations on the resource, such as the source references a SLSA Source Verification Summary records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoResourceDescriptor'],
         'slot_uri': 'in_toto_linkml:annotations'} })

    @field_validator('content')
    def pattern_content(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9+/_-]+={0,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid content format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid content format: {v}"
            raise ValueError(err_msg)
        return v


class InTotoStatement(ConfiguredBaseModel):
    """
    The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The signature envelope around a statement, and the bundle that '
                      'collects signed statements, are outside this model.',
                      'A statement is the attestation, and its predicate is one kind '
                      'of claim about the subjects, such as a test result or build '
                      'provenance.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/statement.md']})

    predicate: Optional[Union[SlsaBuildProvenance,SlsaVerificationSummary,SlsaSourceProvenance,SlsaBuildEnvironmentAttestation]] = Field(default=None, description="""The predicate, one of the kinds this schema or an importing one models; predicate_kind names which. Unset means the same as empty.""", json_schema_extra = { "linkml_meta": {'comments': ['It is a slot of its own rather than an attribute of '
                      "InTotoStatement, because LOKF's predicate is a relation's type: "
                      '`lokf adapt` renames a slot whose name LOKF defines and keeps '
                      'its IRI, so a copy beside LOKF calls it '
                      'in_toto_linkml_predicate.'],
         'domain_of': ['InTotoStatement'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/statement.md'],
         'slot_uri': 'in_toto_linkml:predicate'} })
    statement_type: URI = Field(default=..., description="""The in-toto statement type, always https://in-toto.io/Statement/v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'slot_uri': 'in_toto_linkml:statement_type'} })
    subject: list[InTotoStatementSubject] = Field(default=..., description="""The artifacts the predicate is about, each with a digest.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'slot_uri': 'in_toto_linkml:subject'} })
    predicate_type: URI = Field(default=..., description="""The URI that names the predicate's type and so its schema, such as https://in-toto.io/attestation/test-result/v0.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'slot_uri': 'in_toto_linkml:predicate_type'} })

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


class SlsaStatement(InTotoStatement):
    """
    An in-toto statement with the fields this schema adds: where the signed attestation is stored, the tool that signed it and the transparency log entry that records the signature.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['InTotoStatement comes from lmodel/in-toto and holds only what '
                      "the in-toto specification defines, so the fields SLSA's "
                      'adoption study and the Secure Software Factory add live on this '
                      'subclass. A statement without them is a valid SlsaStatement '
                      'too.',
                      'Attestation and provenance are often confused; a statement is '
                      'the attestation, and build provenance is one kind of predicate '
                      'it may carry (Tamanna et al., 2024, UC.1).'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_environment_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/attestation-model',
                      'https://slsa.dev/spec/v1.2/distributing-provenance']})

    attestation_storage_uri: Optional[str] = Field(default=None, description="""Where the signed attestation is stored or can be fetched.""", json_schema_extra = { "linkml_meta": {'comments': ['SLSA asks producers to publish attestations in at least one '
                      "place and preferably more: beside the source repository's "
                      'releases, beside the artifact in its package registry, which it '
                      'prefers in the long term, or elsewhere with an entry in a '
                      'transparency log.',
                      'Where to store attestations was an open question for '
                      'practitioners (Tamanna et al., 2024, LF.1).'],
         'domain_of': ['SlsaStatement'],
         'in_subset': ['slsa_adoption_study']} })
    signing_tool: Optional[str] = Field(default=None, description="""The tool that signed the attestation, named by URI, such as Cosign or Notation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaStatement'], 'in_subset': ['slsa_ssf']} })
    transparency_log_entry: Optional[str] = Field(default=None, description="""The transparency log entry that records the signature, such as a Rekor entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaStatement'], 'in_subset': ['slsa_ssf']} })
    predicate: Optional[Union[SlsaBuildProvenance,SlsaVerificationSummary,SlsaSourceProvenance,SlsaBuildEnvironmentAttestation]] = Field(default=None, description="""The predicate, one of the kinds this schema or an importing one models; predicate_kind names which. Unset means the same as empty.""", json_schema_extra = { "linkml_meta": {'comments': ['It is a slot of its own rather than an attribute of '
                      "InTotoStatement, because LOKF's predicate is a relation's type: "
                      '`lokf adapt` renames a slot whose name LOKF defines and keeps '
                      'its IRI, so a copy beside LOKF calls it '
                      'in_toto_linkml_predicate.'],
         'domain_of': ['InTotoStatement'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/statement.md'],
         'slot_uri': 'in_toto_linkml:predicate'} })
    statement_type: URI = Field(default=..., description="""The in-toto statement type, always https://in-toto.io/Statement/v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'slot_uri': 'in_toto_linkml:statement_type'} })
    subject: list[InTotoStatementSubject] = Field(default=..., description="""The artifacts the predicate is about, each with a digest.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'slot_uri': 'in_toto_linkml:subject'} })
    predicate_type: URI = Field(default=..., description="""The URI that names the predicate's type and so its schema, such as https://in-toto.io/attestation/test-result/v0.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InTotoStatement'], 'slot_uri': 'in_toto_linkml:predicate_type'} })

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


class InTotoPredicate(ConfiguredBaseModel):
    """
    The base of every predicate an in-toto statement can carry; predicate_kind names the concrete kind.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'comments': ["The statement's predicate_type names the predicate's type by "
                      'URI, and each concrete class says which URI it renders. Nothing '
                      'ties the two, since a schema that imports this module may model '
                      'a predicate under its own URI.'],
         'from_schema': 'https://w3id.org/lmodel/in-toto/in_toto_core',
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/predicate.md']})

    predicate_kind: Literal["InTotoPredicate"] = Field(default="InTotoPredicate", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['InTotoPredicate'],
         'slot_uri': 'in_toto_linkml:predicate_kind'} })


class SlsaPredicate(InTotoPredicate):
    """
    The base of every predicate this schema models; the predicate_kind it takes from InTotoPredicate names the concrete kind.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_core',
         'in_subset': ['slsa_build_track',
                       'slsa_source_track',
                       'slsa_build_environment_track']})

    predicate_kind: Literal["SlsaPredicate"] = Field(default="SlsaPredicate", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['InTotoPredicate'],
         'slot_uri': 'in_toto_linkml:predicate_kind'} })


class SlsaBuildProvenance(SlsaPredicate):
    """
    The predicate that says how a build platform produced a set of artifacts, so that consumers can verify the build met their expectations and others can rebuild it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The statement that carries it has predicate_type '
                      'https://slsa.dev/provenance/v1.',
                      'Complicated provenance generation was the challenge with the '
                      'most issues in the study (Tamanna et al., 2024, CI.1).'],
         'from_schema': 'https://w3id.org/lmodel/slsa/slsa_build',
         'in_subset': ['slsa_build_track'],
         'see_also': ['https://slsa.dev/spec/v1.2/build-provenance#provenance']})

    build_definition: SlsaBuildDefinition = Field(default=..., description="""The inputs to the build; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildProvenance']} })
    run_details: SlsaRunDetails = Field(default=..., description="""What is specific to this execution of the build; required at Build L1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaBuildProvenance']} })
    predicate_kind: Literal["SlsaBuildProvenance"] = Field(default="SlsaBuildProvenance", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['InTotoPredicate'],
         'slot_uri': 'in_toto_linkml:predicate_kind'} })


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

    resource_uri: URI = Field(default=..., description="""The URI consumers fetch the artifact from, which the verifier verified it as.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary', 'InTotoResourceDescriptor'],
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/field_types.md#resourceuri'],
         'slot_uri': 'in_toto_linkml:resource_uri'} })
    verifier: SlsaVerifier = Field(default=..., description="""The verifier that made this determination.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    time_verified: Optional[str] = Field(default=None, description="""When the verification happened.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    policy: SlsaVerificationSummaryPolicy = Field(default=..., description="""The policy the subject was verified against, by URI and preferably by digest too.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    input_attestations: Optional[list[SlsaVerificationSummaryInputAttestation]] = Field(default=None, description="""Every attestation the verifier consulted, each with a digest; complete when present.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    verification_result: SlsaVerificationResult = Field(default=..., description="""Whether the subject passed the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    verified_levels: list[str] = Field(default=..., description="""The highest level verified in each track, any verified property, and any result of the issuer's own; a level implies the levels below it.""", min_length=1, json_schema_extra = { "linkml_meta": {'comments': ['A VSA lists at most one level per track, and only FAILED when '
                      'verification failed; the validator checks neither.'],
         'domain_of': ['SlsaVerificationSummary']} })
    organization_properties: Optional[list[str]] = Field(default=None, description="""Properties the organization defines for the revision, each prefixed ORG_SOURCE_; ORG_SOURCE_INTERNAL_ marks one not meant for external consumers.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Write these properties in verified_levels, where the '
                       "attestation's JSON puts them; this field goes in a later "
                       'release.',
         'deprecated_element_has_possible_replacement': 'slsa:verified_levels',
         'domain_of': ['SlsaVerificationSummary'],
         'in_subset': ['slsa_source_track']} })
    dependency_levels: Optional[list[SlsaDependencyLevelCount]] = Field(default=None, description="""How many transitive dependencies were verified at each level; absent when the verifier makes no claim about dependencies.""", json_schema_extra = { "linkml_meta": {'comments': ["The attestation's JSON tells an empty map (no dependencies) "
                      'from an absent one (no claim); this list cannot, so an empty '
                      'list reads as no claim.'],
         'domain_of': ['SlsaVerificationSummary']} })
    slsa_version: Optional[str] = Field(default=None, description="""The SLSA specification version the verifier applied, as MAJOR.MINOR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaVerificationSummary']} })
    predicate_kind: Literal["SlsaVerificationSummary"] = Field(default="SlsaVerificationSummary", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['InTotoPredicate'],
         'slot_uri': 'in_toto_linkml:predicate_kind'} })

    @field_validator('verified_levels')
    def pattern_verified_levels(cls, v):
        pattern=re.compile(r"^(SLSA_BUILD_LEVEL_(UNEVALUATED|[0-3])|SLSA_SOURCE_LEVEL_(UNEVALUATED|[0-4])|SLSA_SOURCE_TWO_PARTY_REVIEWED|SLSA_BUILD_REPRODUCED|([!-RT-rt-~]|[Ss]$|[Ss][!-KM-km-~]|[Ss][Ll]$|[Ss][Ll][!-RT-rt-~]|[Ss][Ll][Ss]$|[Ss][Ll][Ss][!-@B-`b-~]|[Ss][Ll][Ss][Aa]$|[Ss][Ll][Ss][Aa][!-^`-~])[!-~]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid verified_levels format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid verified_levels format: {v}"
            raise ValueError(err_msg)
        return v

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
    predicate_kind: Literal["SlsaSourceProvenance"] = Field(default="SlsaSourceProvenance", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['InTotoPredicate'],
         'slot_uri': 'in_toto_linkml:predicate_kind'} })


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
         'see_also': ['https://github.com/in-toto/attestation/blob/v1.2.0/spec/v1/digest_set.md'],
         'slot_uri': 'in_toto_linkml:digest'} })
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
    predicate_kind: Literal["SlsaBuildEnvironmentAttestation"] = Field(default="SlsaBuildEnvironmentAttestation", description="""The kind of predicate, one of this class's descendants.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['InTotoPredicate'],
         'slot_uri': 'in_toto_linkml:predicate_kind'} })


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

    attestations: Optional[list[SlsaStatement]] = Field(default=None, description="""The attestations, as in-toto statements with SLSA's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    parties: Optional[list[Union[SlsaProducer,SlsaConsumer,SlsaVerifier,SlsaInfrastructureProvider,SlsaBuildImageProducer]]] = Field(default=None, description="""The parties, each in its role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    build_platforms: Optional[list[SlsaBuildPlatform]] = Field(default=None, description="""The build platforms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
    control_planes: Optional[list[SlsaControlPlane]] = Field(default=None, description="""The control planes of the build platforms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SlsaDocument']} })
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
SlsaBuildDefinition.model_rebuild()
SlsaBuildParameter.model_rebuild()
SlsaRunDetails.model_rebuild()
SlsaBuildMetadata.model_rebuild()
SlsaDependencyLevelCount.model_rebuild()
SlsaSourceControlSystem.model_rebuild()
SlsaSourceRepository.model_rebuild()
SlsaSourceRevision.model_rebuild()
SlsaNamedReference.model_rebuild()
SlsaBranch.model_rebuild()
SlsaTag.model_rebuild()
SlsaDependencyInventory.model_rebuild()
InTotoDigestSet.model_rebuild()
InTotoAdditionalDigest.model_rebuild()
InTotoAnnotation.model_rebuild()
InTotoResourceDescriptor.model_rebuild()
SlsaVerificationSummaryPolicy.model_rebuild()
SlsaVerificationSummaryInputAttestation.model_rebuild()
InTotoStatementSubject.model_rebuild()
InTotoStatement.model_rebuild()
SlsaStatement.model_rebuild()
InTotoPredicate.model_rebuild()
SlsaPredicate.model_rebuild()
SlsaBuildProvenance.model_rebuild()
SlsaVerificationSummary.model_rebuild()
SlsaSourceProvenance.model_rebuild()
SlsaBuildImageProducer.model_rebuild()
SlsaBuildImage.model_rebuild()
SlsaMeasurement.model_rebuild()
SlsaBuildEnvironmentAttestation.model_rebuild()
SlsaAdoptionMetadata.model_rebuild()
SlsaDocument.model_rebuild()
