# Auto generated from slsa.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-22T23:42:41
# Schema: slsa
#
# id: https://w3id.org/lmodel/slsa
# description: Electronic (LinkML) Version of Supply-chain Levels for Software Artifacts (SLSA)
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "1.0.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SLSA = CurieNamespace('slsa', 'https://w3id.org/lmodel/slsa/')
DEFAULT_ = SLSA


# Types

# Class references



@dataclass(repr=False)
class SlsaDocument(YAMLRoot):
    """
    Root wrapper for any SLSA attestation payload. Acts as the entry point for schema validation and tools.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaDocument"]
    class_class_curie: ClassVar[str] = "slsa:SlsaDocument"
    class_name: ClassVar[str] = "SlsaDocument"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaDocument

    buildDefinition: Union[dict, "BuildDefinition"] = None
    runDetails: Union[dict, "RunDetails"] = None
    verifier: Union[dict, "Verifier"] = None
    verificationResult: Union[str, "VerificationResultEnum"] = None
    verifiedLevels: Union[Union[str, "SlsaResultEnum"], list[Union[str, "SlsaResultEnum"]]] = None
    adoptionMetadata: Optional[Union[dict, "AdoptionMetadata"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.buildDefinition):
            self.MissingRequiredField("buildDefinition")
        if not isinstance(self.buildDefinition, BuildDefinition):
            self.buildDefinition = BuildDefinition(**as_dict(self.buildDefinition))

        if self._is_empty(self.runDetails):
            self.MissingRequiredField("runDetails")
        if not isinstance(self.runDetails, RunDetails):
            self.runDetails = RunDetails(**as_dict(self.runDetails))

        if self._is_empty(self.verifier):
            self.MissingRequiredField("verifier")
        if not isinstance(self.verifier, Verifier):
            self.verifier = Verifier(**as_dict(self.verifier))

        if self._is_empty(self.verificationResult):
            self.MissingRequiredField("verificationResult")
        if not isinstance(self.verificationResult, VerificationResultEnum):
            self.verificationResult = VerificationResultEnum(self.verificationResult)

        if self._is_empty(self.verifiedLevels):
            self.MissingRequiredField("verifiedLevels")
        if not isinstance(self.verifiedLevels, list):
            self.verifiedLevels = [self.verifiedLevels] if self.verifiedLevels is not None else []
        self.verifiedLevels = [v if isinstance(v, SlsaResultEnum) else SlsaResultEnum(v) for v in self.verifiedLevels]

        if self.adoptionMetadata is not None and not isinstance(self.adoptionMetadata, AdoptionMetadata):
            self.adoptionMetadata = AdoptionMetadata(**as_dict(self.adoptionMetadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DigestSet(YAMLRoot):
    """
    A set of cryptographic digests for an artifact, keyed by algorithm name (e.g., "sha256", "gitCommit"). Provides
    enough information for consumers to verify artifact integrity using their preferred algorithm.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["DigestSet"]
    class_class_curie: ClassVar[str] = "slsa:DigestSet"
    class_name: ClassVar[str] = "DigestSet"
    class_model_uri: ClassVar[URIRef] = SLSA.DigestSet

    sha256: Optional[str] = None
    sha512: Optional[str] = None
    gitCommit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sha256 is not None and not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self.sha512 is not None and not isinstance(self.sha512, str):
            self.sha512 = str(self.sha512)

        if self.gitCommit is not None and not isinstance(self.gitCommit, str):
            self.gitCommit = str(self.gitCommit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceDescriptor(YAMLRoot):
    """
    A reference to a software artifact including its location, digest, and optional metadata. Used throughout SLSA to
    describe inputs, outputs, and dependencies in provenance attestations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["ResourceDescriptor"]
    class_class_curie: ClassVar[str] = "slsa:ResourceDescriptor"
    class_name: ClassVar[str] = "ResourceDescriptor"
    class_model_uri: ClassVar[URIRef] = SLSA.ResourceDescriptor

    uri: Optional[str] = None
    digest: Optional[Union[dict, DigestSet]] = None
    name: Optional[str] = None
    downloadLocation: Optional[str] = None
    mediaType: Optional[str] = None
    annotations: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.uri is not None and not isinstance(self.uri, str):
            self.uri = str(self.uri)

        if self.digest is not None and not isinstance(self.digest, DigestSet):
            self.digest = DigestSet(**as_dict(self.digest))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.downloadLocation is not None and not isinstance(self.downloadLocation, str):
            self.downloadLocation = str(self.downloadLocation)

        if self.mediaType is not None and not isinstance(self.mediaType, str):
            self.mediaType = str(self.mediaType)

        if not isinstance(self.annotations, list):
            self.annotations = [self.annotations] if self.annotations is not None else []
        self.annotations = [v if isinstance(v, str) else str(v) for v in self.annotations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Statement(YAMLRoot):
    """
    The middle layer of an in-toto software attestation (Statement v1). Binds an authenticated predicate to one or
    more subject artifacts, allowing predicate-agnostic processing and storage.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["Statement"]
    class_class_curie: ClassVar[str] = "slsa:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = SLSA.Statement

    _type: str = None
    subject: Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]] = None
    predicateType: str = None
    predicate: Optional[str] = None
    attestationStorageUri: Optional[str] = None
    signingTool: Optional[str] = None
    sigstoreLogEntry: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._type):
            self.MissingRequiredField("_type")
        if not isinstance(self._type, str):
            self._type = str(self._type)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, ResourceDescriptor) else ResourceDescriptor(**as_dict(v)) for v in self.subject]

        if self._is_empty(self.predicateType):
            self.MissingRequiredField("predicateType")
        if not isinstance(self.predicateType, str):
            self.predicateType = str(self.predicateType)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.attestationStorageUri is not None and not isinstance(self.attestationStorageUri, str):
            self.attestationStorageUri = str(self.attestationStorageUri)

        if self.signingTool is not None and not isinstance(self.signingTool, str):
            self.signingTool = str(self.signingTool)

        if self.sigstoreLogEntry is not None and not isinstance(self.sigstoreLogEntry, str):
            self.sigstoreLogEntry = str(self.sigstoreLogEntry)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuildProvenance(Statement):
    """
    An attestation predicate (predicateType "https://slsa.dev/provenance/v1") that describes how a set of output
    artifacts was produced by a build platform. Consumers use this to verify artifact authenticity and trace artifacts
    back through the supply chain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["BuildProvenance"]
    class_class_curie: ClassVar[str] = "slsa:BuildProvenance"
    class_name: ClassVar[str] = "BuildProvenance"
    class_model_uri: ClassVar[URIRef] = SLSA.BuildProvenance

    _type: str = None
    subject: Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]] = None
    predicateType: str = None
    buildDefinition: Union[dict, "BuildDefinition"] = None
    runDetails: Union[dict, "RunDetails"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.buildDefinition):
            self.MissingRequiredField("buildDefinition")
        if not isinstance(self.buildDefinition, BuildDefinition):
            self.buildDefinition = BuildDefinition(**as_dict(self.buildDefinition))

        if self._is_empty(self.runDetails):
            self.MissingRequiredField("runDetails")
        if not isinstance(self.runDetails, RunDetails):
            self.runDetails = RunDetails(**as_dict(self.runDetails))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuildDefinition(YAMLRoot):
    """
    Describes all inputs to the build in enough detail to initialise and reproduce the build. The accuracy and
    completeness are implied by the builder identified in runDetails.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["BuildDefinition"]
    class_class_curie: ClassVar[str] = "slsa:BuildDefinition"
    class_name: ClassVar[str] = "BuildDefinition"
    class_model_uri: ClassVar[URIRef] = SLSA.BuildDefinition

    buildType: str = None
    externalParameters: Optional[str] = None
    internalParameters: Optional[str] = None
    resolvedDependencies: Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]] = empty_list()
    hermeticBuild: Optional[Union[bool, Bool]] = None
    provenanceGenerationTool: Optional[str] = None
    pipelineOrchestrator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.buildType):
            self.MissingRequiredField("buildType")
        if not isinstance(self.buildType, str):
            self.buildType = str(self.buildType)

        if self.externalParameters is not None and not isinstance(self.externalParameters, str):
            self.externalParameters = str(self.externalParameters)

        if self.internalParameters is not None and not isinstance(self.internalParameters, str):
            self.internalParameters = str(self.internalParameters)

        if not isinstance(self.resolvedDependencies, list):
            self.resolvedDependencies = [self.resolvedDependencies] if self.resolvedDependencies is not None else []
        self.resolvedDependencies = [v if isinstance(v, ResourceDescriptor) else ResourceDescriptor(**as_dict(v)) for v in self.resolvedDependencies]

        if self.hermeticBuild is not None and not isinstance(self.hermeticBuild, Bool):
            self.hermeticBuild = Bool(self.hermeticBuild)

        if self.provenanceGenerationTool is not None and not isinstance(self.provenanceGenerationTool, str):
            self.provenanceGenerationTool = str(self.provenanceGenerationTool)

        if self.pipelineOrchestrator is not None and not isinstance(self.pipelineOrchestrator, str):
            self.pipelineOrchestrator = str(self.pipelineOrchestrator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RunDetails(YAMLRoot):
    """
    Details specific to this particular execution of the build, including the trusted builder and optional run-level
    metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["RunDetails"]
    class_class_curie: ClassVar[str] = "slsa:RunDetails"
    class_name: ClassVar[str] = "RunDetails"
    class_model_uri: ClassVar[URIRef] = SLSA.RunDetails

    builder: Union[dict, "Builder"] = None
    buildMetadata: Optional[Union[dict, "BuildMetadata"]] = None
    byproducts: Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.builder):
            self.MissingRequiredField("builder")
        if not isinstance(self.builder, Builder):
            self.builder = Builder(**as_dict(self.builder))

        if self.buildMetadata is not None and not isinstance(self.buildMetadata, BuildMetadata):
            self.buildMetadata = BuildMetadata(**as_dict(self.buildMetadata))

        if not isinstance(self.byproducts, list):
            self.byproducts = [self.byproducts] if self.byproducts is not None else []
        self.byproducts = [v if isinstance(v, ResourceDescriptor) else ResourceDescriptor(**as_dict(v)) for v in self.byproducts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Builder(YAMLRoot):
    """
    Represents the transitive closure of all software, hardware, and entities trusted to faithfully execute the build
    and record provenance. The builder.id is the primary basis for determining SLSA Build Level.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["Builder"]
    class_class_curie: ClassVar[str] = "slsa:Builder"
    class_name: ClassVar[str] = "Builder"
    class_model_uri: ClassVar[URIRef] = SLSA.Builder

    id: str = None
    builderDependencies: Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]] = empty_list()
    version: Optional[str] = None
    versionTag: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if not isinstance(self.builderDependencies, list):
            self.builderDependencies = [self.builderDependencies] if self.builderDependencies is not None else []
        self.builderDependencies = [v if isinstance(v, ResourceDescriptor) else ResourceDescriptor(**as_dict(v)) for v in self.builderDependencies]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.versionTag is not None and not isinstance(self.versionTag, str):
            self.versionTag = str(self.versionTag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuildMetadata(YAMLRoot):
    """
    Metadata about a specific invocation of the build, including timing information and a unique build identifier for
    log correlation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["BuildMetadata"]
    class_class_curie: ClassVar[str] = "slsa:BuildMetadata"
    class_name: ClassVar[str] = "BuildMetadata"
    class_model_uri: ClassVar[URIRef] = SLSA.BuildMetadata

    invocationId: Optional[str] = None
    startedOn: Optional[str] = None
    finishedOn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.invocationId is not None and not isinstance(self.invocationId, str):
            self.invocationId = str(self.invocationId)

        if self.startedOn is not None and not isinstance(self.startedOn, str):
            self.startedOn = str(self.startedOn)

        if self.finishedOn is not None and not isinstance(self.finishedOn, str):
            self.finishedOn = str(self.finishedOn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VerificationSummaryAttestation(Statement):
    """
    An attestation predicate (predicateType "https://slsa.dev/verification_summary/v1") issued by a trusted verifier
    stating that one or more artifacts were evaluated against a policy and the SLSA level at which they were verified.
    Allows consumers to trust the verifier's determination without needing access to all underlying provenance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["VerificationSummaryAttestation"]
    class_class_curie: ClassVar[str] = "slsa:VerificationSummaryAttestation"
    class_name: ClassVar[str] = "VerificationSummaryAttestation"
    class_model_uri: ClassVar[URIRef] = SLSA.VerificationSummaryAttestation

    _type: str = None
    subject: Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]] = None
    predicateType: str = None
    verifier: Union[dict, "Verifier"] = None
    resourceUri: str = None
    policy: Union[dict, ResourceDescriptor] = None
    verificationResult: Union[str, "VerificationResultEnum"] = None
    verifiedLevels: Union[Union[str, "SlsaResultEnum"], list[Union[str, "SlsaResultEnum"]]] = None
    timeVerified: Optional[str] = None
    inputAttestations: Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]] = empty_list()
    dependencyLevels: Optional[str] = None
    slsaVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.verifier):
            self.MissingRequiredField("verifier")
        if not isinstance(self.verifier, Verifier):
            self.verifier = Verifier(**as_dict(self.verifier))

        if self._is_empty(self.resourceUri):
            self.MissingRequiredField("resourceUri")
        if not isinstance(self.resourceUri, str):
            self.resourceUri = str(self.resourceUri)

        if self._is_empty(self.policy):
            self.MissingRequiredField("policy")
        if not isinstance(self.policy, ResourceDescriptor):
            self.policy = ResourceDescriptor(**as_dict(self.policy))

        if self._is_empty(self.verificationResult):
            self.MissingRequiredField("verificationResult")
        if not isinstance(self.verificationResult, VerificationResultEnum):
            self.verificationResult = VerificationResultEnum(self.verificationResult)

        if self._is_empty(self.verifiedLevels):
            self.MissingRequiredField("verifiedLevels")
        if not isinstance(self.verifiedLevels, list):
            self.verifiedLevels = [self.verifiedLevels] if self.verifiedLevels is not None else []
        self.verifiedLevels = [v if isinstance(v, SlsaResultEnum) else SlsaResultEnum(v) for v in self.verifiedLevels]

        if self.timeVerified is not None and not isinstance(self.timeVerified, str):
            self.timeVerified = str(self.timeVerified)

        if not isinstance(self.inputAttestations, list):
            self.inputAttestations = [self.inputAttestations] if self.inputAttestations is not None else []
        self.inputAttestations = [v if isinstance(v, ResourceDescriptor) else ResourceDescriptor(**as_dict(v)) for v in self.inputAttestations]

        if self.dependencyLevels is not None and not isinstance(self.dependencyLevels, str):
            self.dependencyLevels = str(self.dependencyLevels)

        if self.slsaVersion is not None and not isinstance(self.slsaVersion, str):
            self.slsaVersion = str(self.slsaVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Verifier(YAMLRoot):
    """
    The entity that performed verification of an artifact and issued a Verification Summary Attestation. Consumers
    MUST accept only specific (signer, verifier) pairs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["Verifier"]
    class_class_curie: ClassVar[str] = "slsa:Verifier"
    class_name: ClassVar[str] = "Verifier"
    class_model_uri: ClassVar[URIRef] = SLSA.Verifier

    id: str = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Producer(YAMLRoot):
    """
    A party who creates software and provides it to others. Responsible for choosing an appropriate build platform,
    following a consistent build process, and distributing provenance to consumers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["Producer"]
    class_class_curie: ClassVar[str] = "slsa:Producer"
    class_name: ClassVar[str] = "Producer"
    class_model_uri: ClassVar[URIRef] = SLSA.Producer

    name: Optional[str] = None
    buildPlatformId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.buildPlatformId is not None and not isinstance(self.buildPlatformId, str):
            self.buildPlatformId = str(self.buildPlatformId)

        super().__post_init__(**kwargs)


class Consumer(YAMLRoot):
    """
    A party who uses software provided by a producer. May verify provenance directly or delegate that responsibility
    to a separate verifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["Consumer"]
    class_class_curie: ClassVar[str] = "slsa:Consumer"
    class_name: ClassVar[str] = "Consumer"
    class_model_uri: ClassVar[URIRef] = SLSA.Consumer


class InfrastructureProvider(YAMLRoot):
    """
    A party who provides software or services to other roles in the supply chain, such as a package registry
    maintainer or build platform operator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["InfrastructureProvider"]
    class_class_curie: ClassVar[str] = "slsa:InfrastructureProvider"
    class_name: ClassVar[str] = "InfrastructureProvider"
    class_model_uri: ClassVar[URIRef] = SLSA.InfrastructureProvider


@dataclass(repr=False)
class BuildPlatform(YAMLRoot):
    """
    The infrastructure (software, hardware, people, and organizations) used to transform source code into package
    artifacts. Responsible for provenance generation and isolation between tenant builds. Often a hosted, multi-tenant
    build service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["BuildPlatform"]
    class_class_curie: ClassVar[str] = "slsa:BuildPlatform"
    class_name: ClassVar[str] = "BuildPlatform"
    class_model_uri: ClassVar[URIRef] = SLSA.BuildPlatform

    id: str = None
    buildLevel: Optional[Union[str, "BuildLevelEnum"]] = None
    isHosted: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.buildLevel is not None and not isinstance(self.buildLevel, BuildLevelEnum):
            self.buildLevel = BuildLevelEnum(self.buildLevel)

        if self.isHosted is not None and not isinstance(self.isHosted, Bool):
            self.isHosted = Bool(self.isHosted)

        super().__post_init__(**kwargs)


class ControlPlane(YAMLRoot):
    """
    The build platform component that orchestrates each independent build execution and generates provenance. Managed
    by an admin and trusted to be outside of tenant control. Responsible for generating and signing provenance at SLSA
    Build L2+.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["ControlPlane"]
    class_class_curie: ClassVar[str] = "slsa:ControlPlane"
    class_name: ClassVar[str] = "ControlPlane"
    class_model_uri: ClassVar[URIRef] = SLSA.ControlPlane


@dataclass(repr=False)
class Package(YAMLRoot):
    """
    An identifiable unit of software intended for distribution. In the SLSA model, a package is always the output of a
    build process (which may be a no-op). The package name is the primary security boundary within a package
    ecosystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["Package"]
    class_class_curie: ClassVar[str] = "slsa:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = SLSA.Package

    name: Optional[str] = None
    ecosystem: Optional[str] = None
    registry: Optional[str] = None
    artifact: Optional[Union[dict, ResourceDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.registry is not None and not isinstance(self.registry, str):
            self.registry = str(self.registry)

        if self.artifact is not None and not isinstance(self.artifact, ResourceDescriptor):
            self.artifact = ResourceDescriptor(**as_dict(self.artifact))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceRepository(YAMLRoot):
    """
    A self-contained unit that holds the content and complete revision history for a set of files, along with metadata
    such as branches and tags. Hosted and governed by a Source Control System.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SourceRepository"]
    class_class_curie: ClassVar[str] = "slsa:SourceRepository"
    class_name: ClassVar[str] = "SourceRepository"
    class_model_uri: ClassVar[URIRef] = SLSA.SourceRepository

    id: str = None
    description: Optional[str] = None
    sourceLevel: Optional[Union[str, "SourceLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.sourceLevel is not None and not isinstance(self.sourceLevel, SourceLevelEnum):
            self.sourceLevel = SourceLevelEnum(self.sourceLevel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceRevision(YAMLRoot):
    """
    A specific, logically immutable snapshot of a source repository's tracked files. Uniquely identified by a revision
    identifier such as a cryptographic hash (e.g., git commit SHA) or a path-qualified sequential number (e.g., SVN).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SourceRevision"]
    class_class_curie: ClassVar[str] = "slsa:SourceRevision"
    class_name: ClassVar[str] = "SourceRevision"
    class_model_uri: ClassVar[URIRef] = SLSA.SourceRevision

    revisionId: str = None
    repository: Optional[Union[dict, SourceRepository]] = None
    author: Optional[str] = None
    timestamp: Optional[str] = None
    parentRevisions: Optional[Union[str, list[str]]] = empty_list()
    reviewType: Optional[Union[str, "ReviewTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.revisionId):
            self.MissingRequiredField("revisionId")
        if not isinstance(self.revisionId, str):
            self.revisionId = str(self.revisionId)

        if self.repository is not None and not isinstance(self.repository, SourceRepository):
            self.repository = SourceRepository(**as_dict(self.repository))

        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.timestamp is not None and not isinstance(self.timestamp, str):
            self.timestamp = str(self.timestamp)

        if not isinstance(self.parentRevisions, list):
            self.parentRevisions = [self.parentRevisions] if self.parentRevisions is not None else []
        self.parentRevisions = [v if isinstance(v, str) else str(v) for v in self.parentRevisions]

        if self.reviewType is not None and not isinstance(self.reviewType, ReviewTypeEnum):
            self.reviewType = ReviewTypeEnum(self.reviewType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceProvenanceAttestation(Statement):
    """
    An attestation describing how a source revision came to exist: where it was hosted, when it was generated, what
    process was used, who the contributors were, and which technical controls were enforced by the Source Control
    System.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SourceProvenanceAttestation"]
    class_class_curie: ClassVar[str] = "slsa:SourceProvenanceAttestation"
    class_name: ClassVar[str] = "SourceProvenanceAttestation"
    class_model_uri: ClassVar[URIRef] = SLSA.SourceProvenanceAttestation

    _type: str = None
    subject: Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]] = None
    predicateType: str = None
    revision: Optional[Union[dict, SourceRevision]] = None
    sourceLevel: Optional[Union[str, "SourceLevelEnum"]] = None
    controlsEnforced: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.revision is not None and not isinstance(self.revision, SourceRevision):
            self.revision = SourceRevision(**as_dict(self.revision))

        if self.sourceLevel is not None and not isinstance(self.sourceLevel, SourceLevelEnum):
            self.sourceLevel = SourceLevelEnum(self.sourceLevel)

        if not isinstance(self.controlsEnforced, list):
            self.controlsEnforced = [self.controlsEnforced] if self.controlsEnforced is not None else []
        self.controlsEnforced = [v if isinstance(v, str) else str(v) for v in self.controlsEnforced]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DependencyInventory(YAMLRoot):
    """
    A comprehensive inventory of all third-party build dependencies for an artifact, capturing direct and transitive
    dependencies. Supports vulnerability management and incident response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["DependencyInventory"]
    class_class_curie: ClassVar[str] = "slsa:DependencyInventory"
    class_name: ClassVar[str] = "DependencyInventory"
    class_model_uri: ClassVar[URIRef] = SLSA.DependencyInventory

    artifact: Optional[Union[dict, ResourceDescriptor]] = None
    dependencies: Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]] = empty_list()
    dependencyLevel: Optional[Union[str, "DependencyLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.artifact is not None and not isinstance(self.artifact, ResourceDescriptor):
            self.artifact = ResourceDescriptor(**as_dict(self.artifact))

        if not isinstance(self.dependencies, list):
            self.dependencies = [self.dependencies] if self.dependencies is not None else []
        self.dependencies = [v if isinstance(v, ResourceDescriptor) else ResourceDescriptor(**as_dict(v)) for v in self.dependencies]

        if self.dependencyLevel is not None and not isinstance(self.dependencyLevel, DependencyLevelEnum):
            self.dependencyLevel = DependencyLevelEnum(self.dependencyLevel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuildImage(YAMLRoot):
    """
    The template for a build environment, such as a VM or container image. Comprises the root filesystem,
    pre-installed guest OS and packages, the build executor, and the build agent. Created by a build image producer
    and consumed by the hosted build platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["BuildImage"]
    class_class_curie: ClassVar[str] = "slsa:BuildImage"
    class_name: ClassVar[str] = "BuildImage"
    class_model_uri: ClassVar[URIRef] = SLSA.BuildImage

    id: str = None
    provenance: Optional[Union[dict, BuildProvenance]] = None
    buildEnvLevel: Optional[Union[str, "BuildEnvLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.provenance is not None and not isinstance(self.provenance, BuildProvenance):
            self.provenance = BuildProvenance(**as_dict(self.provenance))

        if self.buildEnvLevel is not None and not isinstance(self.buildEnvLevel, BuildEnvLevelEnum):
            self.buildEnvLevel = BuildEnvLevelEnum(self.buildEnvLevel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuildEnvironmentAttestation(Statement):
    """
    An attestation describing the integrity of a build environment at the time a specific build was dispatched and
    executed. Used to verify that a build ran in the expected, untampered environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["BuildEnvironmentAttestation"]
    class_class_curie: ClassVar[str] = "slsa:BuildEnvironmentAttestation"
    class_name: ClassVar[str] = "BuildEnvironmentAttestation"
    class_model_uri: ClassVar[URIRef] = SLSA.BuildEnvironmentAttestation

    _type: str = None
    subject: Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]] = None
    predicateType: str = None
    buildId: str = None
    buildImage: Optional[Union[dict, BuildImage]] = None
    measurements: Optional[Union[str, list[str]]] = empty_list()
    buildEnvLevel: Optional[Union[str, "BuildEnvLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.buildId):
            self.MissingRequiredField("buildId")
        if not isinstance(self.buildId, str):
            self.buildId = str(self.buildId)

        if self.buildImage is not None and not isinstance(self.buildImage, BuildImage):
            self.buildImage = BuildImage(**as_dict(self.buildImage))

        if not isinstance(self.measurements, list):
            self.measurements = [self.measurements] if self.measurements is not None else []
        self.measurements = [v if isinstance(v, str) else str(v) for v in self.measurements]

        if self.buildEnvLevel is not None and not isinstance(self.buildEnvLevel, BuildEnvLevelEnum):
            self.buildEnvLevel = BuildEnvLevelEnum(self.buildEnvLevel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdoptionMetadata(YAMLRoot):
    """
    Optional structured metadata capturing the SLSA adoption challenges and mitigation strategies relevant to a given
    attestation or deployment context. Derived from empirical analysis of 1,523 SLSA-related GitHub issues across 233
    repositories (Tamanna et al., 2024, arXiv:2409.05014). Use this class to document which challenge themes apply to
    the current deployment and which strategies are being employed or recommended. Attach via the adoptionMetadata
    slot on SlsaDocument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["AdoptionMetadata"]
    class_class_curie: ClassVar[str] = "slsa:AdoptionMetadata"
    class_name: ClassVar[str] = "AdoptionMetadata"
    class_model_uri: ClassVar[URIRef] = SLSA.AdoptionMetadata

    challenges: Optional[Union[Union[str, "AdoptionChallengeEnum"], list[Union[str, "AdoptionChallengeEnum"]]]] = empty_list()
    strategies: Optional[Union[Union[str, "AdoptionStrategyEnum"], list[Union[str, "AdoptionStrategyEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.challenges, list):
            self.challenges = [self.challenges] if self.challenges is not None else []
        self.challenges = [v if isinstance(v, AdoptionChallengeEnum) else AdoptionChallengeEnum(v) for v in self.challenges]

        if not isinstance(self.strategies, list):
            self.strategies = [self.strategies] if self.strategies is not None else []
        self.strategies = [v if isinstance(v, AdoptionStrategyEnum) else AdoptionStrategyEnum(v) for v in self.strategies]

        super().__post_init__(**kwargs)


# Enumerations
class BuildLevelEnum(EnumDefinitionImpl):
    """
    SLSA Build Track levels providing increasing supply chain security guarantees for the build process. Higher levels
    require stronger tamper-resistance and provenance integrity.
    """
    SLSA_BUILD_LEVEL_0 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_0",
        description="""No SLSA requirements. Represents the absence of SLSA guarantees; intended for development or test builds.""")
    SLSA_BUILD_LEVEL_1 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_1",
        description="""Provenance exists, showing how the package was built. Prevents mistakes and aids documentation, but is trivial to bypass.""")
    SLSA_BUILD_LEVEL_2 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_2",
        description="""Build runs on a hosted platform that generates and signs provenance, deterring tampering after the build.""")
    SLSA_BUILD_LEVEL_3 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_3",
        description="""Hardened build platform providing strong guarantees against tampering during the build; requires exploiting a vulnerability to forge provenance.""")

    _defn = EnumDefinition(
        name="BuildLevelEnum",
        description="""SLSA Build Track levels providing increasing supply chain security guarantees for the build process. Higher levels require stronger tamper-resistance and provenance integrity.""",
    )

class SourceLevelEnum(EnumDefinitionImpl):
    """
    SLSA Source Track levels providing increasing trust in source code provenance and the controls used to create
    source revisions.
    """
    SLSA_SOURCE_LEVEL_1 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_1",
        description="""Source is stored in a version control system, enabling discrete and immutable source revisions for precise consumption.""")
    SLSA_SOURCE_LEVEL_2 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_2",
        description="""Branch history is preserved and immutable; the SCS generates tamper- resistant source provenance attestations for each new revision.""")
    SLSA_SOURCE_LEVEL_3 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_3",
        description="""The SCS enforces the organization's technical controls on protected Named References, providing verifiable evidence of those controls.""")
    SLSA_SOURCE_LEVEL_4 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_4",
        description="""All changes to protected branches require two-party review by trusted persons, resisting insider threats and unilateral changes.""")

    _defn = EnumDefinition(
        name="SourceLevelEnum",
        description="""SLSA Source Track levels providing increasing trust in source code provenance and the controls used to create source revisions.""",
    )

class DependencyLevelEnum(EnumDefinitionImpl):
    """
    SLSA Dependency Track levels for measuring and controlling risk introduced from third-party dependencies.
    """
    SLSA_DEPENDENCY_LEVEL_0 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_0",
        description="No mitigations to dependency threats.")
    SLSA_DEPENDENCY_LEVEL_1 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_1",
        description="An inventory of all build dependencies (direct and transitive) exists.")
    SLSA_DEPENDENCY_LEVEL_2 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_2",
        description="""All known vulnerabilities in the artifact's dependencies have been triaged before each release.""")
    SLSA_DEPENDENCY_LEVEL_3 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_3",
        description="""All third-party build dependencies are consumed exclusively from locations under the producer's control.""")
    SLSA_DEPENDENCY_LEVEL_4 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_4",
        description="""Proactive defense against upstream attacks; an ingestion policy prevents consumption of compromised dependencies.""")

    _defn = EnumDefinition(
        name="DependencyLevelEnum",
        description="""SLSA Dependency Track levels for measuring and controlling risk introduced from third-party dependencies.""",
    )

class BuildEnvLevelEnum(EnumDefinitionImpl):
    """
    SLSA Build Environment Track levels for validating the integrity of the compute environment executing builds.
    """
    SLSA_BUILD_ENV_LEVEL_0 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_0",
        description="No build environment integrity requirements.")
    SLSA_BUILD_ENV_LEVEL_1 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_1",
        description="""Signed build image provenance exists, protecting against tampering during build image distribution to the build platform.""")
    SLSA_BUILD_ENV_LEVEL_2 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_2",
        description="""The compute platform attests to the boot-time integrity of the build environment, providing evidence of correct instantiation.""")
    SLSA_BUILD_ENV_LEVEL_3 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_3",
        description="""The build environment runs in a hardware-attested trusted execution environment (TEE), providing runtime integrity guarantees.""")

    _defn = EnumDefinition(
        name="BuildEnvLevelEnum",
        description="""SLSA Build Environment Track levels for validating the integrity of the compute environment executing builds.""",
    )

class VerificationResultEnum(EnumDefinitionImpl):
    """
    Outcome of a policy verification check on an artifact.
    """
    PASSED = PermissibleValue(
        text="PASSED",
        description="The artifact satisfied all policy requirements.")
    FAILED = PermissibleValue(
        text="FAILED",
        description="The artifact did not satisfy one or more policy requirements.")

    _defn = EnumDefinition(
        name="VerificationResultEnum",
        description="Outcome of a policy verification check on an artifact.",
    )

class SlsaResultEnum(EnumDefinitionImpl):
    """
    A named SLSA result used in Verification Summary Attestations to indicate the verified level of an artifact or its
    dependencies.
    """
    SLSA_BUILD_LEVEL_0 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_0",
        description="No SLSA Build guarantees verified.")
    SLSA_BUILD_LEVEL_1 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_1",
        description="Build Level 1 verified for the artifact.")
    SLSA_BUILD_LEVEL_2 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_2",
        description="Build Level 2 verified for the artifact.")
    SLSA_BUILD_LEVEL_3 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_3",
        description="Build Level 3 verified for the artifact.")
    SLSA_SOURCE_LEVEL_1 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_1",
        description="Source Level 1 verified for the artifact.")
    SLSA_SOURCE_LEVEL_2 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_2",
        description="Source Level 2 verified for the artifact.")
    SLSA_SOURCE_LEVEL_3 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_3",
        description="Source Level 3 verified for the artifact.")
    SLSA_SOURCE_LEVEL_4 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_4",
        description="Source Level 4 verified for the artifact.")

    _defn = EnumDefinition(
        name="SlsaResultEnum",
        description="""A named SLSA result used in Verification Summary Attestations to indicate the verified level of an artifact or its dependencies.""",
    )

class ReviewTypeEnum(EnumDefinitionImpl):
    """
    Categories of code-review process applied to a source revision. Captures the forms of two-party review discussed
    by practitioners (Tamanna et al., 2024, LF.2), including contested alternatives whose security equivalence with
    standard asynchronous two-party review has not been formally established.
    """
    TWO_PARTY = PermissibleValue(
        text="TWO_PARTY",
        description="""Standard two-party review: a change is approved by at least one reviewer who is distinct from the author, where both the author and reviewer are trusted persons as defined by the organization.""")
    PAIR_PROGRAMMING = PermissibleValue(
        text="PAIR_PROGRAMMING",
        description="""Two developers working simultaneously on the same code at the same workstation or via screen-sharing. Whether this satisfies the trusted-persons two-party review requirement is an open question raised in practitioner discussions (Tamanna et al., 2024, LF.2).""")
    MOB_PROGRAMMING = PermissibleValue(
        text="MOB_PROGRAMMING",
        description="""Collaborative development with a whole group at once. As with pair programming, formal equivalence to asynchronous two-party review has not been established for SLSA purposes (Tamanna et al., 2024, LF.2).""")
    AUTOMATED = PermissibleValue(
        text="AUTOMATED",
        description="""Review performed entirely by an automated tool or bot, without a second human reviewer. Does not satisfy the SLSA trusted-persons requirement for Source Level 4.""")

    _defn = EnumDefinition(
        name="ReviewTypeEnum",
        description="""Categories of code-review process applied to a source revision. Captures the forms of two-party review discussed by practitioners (Tamanna et al., 2024, LF.2), including contested alternatives whose security equivalence with standard asynchronous two-party review has not been formally established.""",
    )

class AdoptionChallengeEnum(EnumDefinitionImpl):
    """
    The four empirically identified themes of challenges practitioners encounter when deploying SLSA, derived from
    thematic analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024,
    arXiv:2409.05014). Challenge counts in parentheses reflect total issues associated with each theme.
    """
    COMPLEX_IMPLEMENTATION = PermissibleValue(
        text="COMPLEX_IMPLEMENTATION",
        description="""(CI — 901 issues) Challenges integrating SLSA into projects: complicated provenance generation including blocking pre-submit jobs, lack of non-build configuration support, and sensitive-data handling risks (CI.1); and intricate ongoing maintenance of required tools including incompatibilities, silent failures, and documentation drift (CI.2).""")
    UNCLEAR_COMMUNICATION = PermissibleValue(
        text="UNCLEAR_COMMUNICATION",
        description="""(UC — 357 issues) Challenges understanding SLSA documentation: unclear definitions of key terms such as \"provenance\", \"attestation\", \"hermetic\", \"hosted\", and \"non-falsifiable\" (UC.1); and lack of clear, ecosystem-specific guidance on how to apply SLSA requirements in practice (UC.2).""")
    LIMITED_FEASIBILITY = PermissibleValue(
        text="LIMITED_FEASIBILITY",
        description="""(LF — 219 issues) Challenges with practical feasibility of SLSA requirements: complexity and lack of standardization in attestation verification tooling, no standardized storage model for attestations, and security concerns about verification accuracy (LF.1); and difficulty implementing two-party review for single-maintainer open-source projects (LF.2).""")
    UNCLEAR_RELEVANCE = PermissibleValue(
        text="UNCLEAR_RELEVANCE",
        description="""(UR — 46 issues) Challenges understanding SLSA's relevance and distinct value: confusion about which attacks SLSA mitigates, how it differs from OpenSSF best practices, and ecosystem-level policy inconsistencies (e.g., npm package naming divergence) that undermine attestation accuracy (UR.1).""")

    _defn = EnumDefinition(
        name="AdoptionChallengeEnum",
        description="""The four empirically identified themes of challenges practitioners encounter when deploying SLSA, derived from thematic analysis of 1,523 SLSA-related GitHub issues across 233 repositories (Tamanna et al., 2024, arXiv:2409.05014). Challenge counts in parentheses reflect total issues associated with each theme.""",
    )

class AdoptionStrategyEnum(EnumDefinitionImpl):
    """
    The five empirically identified themes of strategies practitioners suggested to overcome SLSA adoption challenges,
    derived from thematic analysis of 1,523 SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Each
    strategy theme contains 2–4 sub-strategies (13 total).
    """
    ENHANCE_ALIGNMENT_FLEXIBILITY = PermissibleValue(
        text="ENHANCE_ALIGNMENT_FLEXIBILITY",
        description="""(S1) Enhance SLSA alignment and flexibility: incorporate build-system tracks for more tailored approaches (S1.1); gamify adoption levels so producers aim for higher levels (S1.2); ensure flexibility for diverse organizational and ecosystem needs (S1.3); align SLSA with OpenSSF best practices including SECURITY.md and silver/gold criteria (S1.4).""")
    PROVIDE_DETAILED_DOCUMENTATION = PermissibleValue(
        text="PROVIDE_DETAILED_DOCUMENTATION",
        description="""(S2) Provide specific and detailed documentation: enhance docs with clear definitions, standard terms, revised requirements, and patches (S2.1); use negative examples to explain complex concepts and improve website diagrams and navigation (S2.2).""")
    STREAMLINE_PROVENANCE_GENERATION = PermissibleValue(
        text="STREAMLINE_PROVENANCE_GENERATION",
        description="""(S3) Streamline provenance generation processes: simplify and standardize the generation process via tools and templates to reduce confusion and improve consistency (S3.1); fix semantic-release tool inconsistencies with clear versioning rules and parallel pre-submit job execution (S3.2).""")
    IMPROVE_VERIFICATION_PROCESS = PermissibleValue(
        text="IMPROVE_VERIFICATION_PROCESS",
        description="""(S4) Improve the SLSA verification process: strengthen verification with better security guarantees and level-determination algorithms (S4.1); implement versioning tagging early to facilitate progress tracking (S4.2); enhance framework tooling with more downstream signaling information (S4.3).""")
    COLLABORATE_WITH_COMMUNITY = PermissibleValue(
        text="COLLABORATE_WITH_COMMUNITY",
        description="""(S5) Collaborate with the community: foster engagement by aligning SLSA verification with industry standards and providing guidance for novice users (S5.1); promote learning and knowledge-sharing, including cross-project collaboration for single-maintainer projects (S5.2).""")

    _defn = EnumDefinition(
        name="AdoptionStrategyEnum",
        description="""The five empirically identified themes of strategies practitioners suggested to overcome SLSA adoption challenges, derived from thematic analysis of 1,523 SLSA-related GitHub issues (Tamanna et al., 2024, arXiv:2409.05014). Each strategy theme contains 2–4 sub-strategies (13 total).""",
    )

# Slots
class slots:
    pass

slots.sha256 = Slot(uri=SLSA.sha256, name="sha256", curie=SLSA.curie('sha256'),
                   model_uri=SLSA.sha256, domain=None, range=Optional[str])

slots.sha512 = Slot(uri=SLSA.sha512, name="sha512", curie=SLSA.curie('sha512'),
                   model_uri=SLSA.sha512, domain=None, range=Optional[str])

slots.gitCommit = Slot(uri=SLSA.gitCommit, name="gitCommit", curie=SLSA.curie('gitCommit'),
                   model_uri=SLSA.gitCommit, domain=None, range=Optional[str])

slots.uri = Slot(uri=SLSA.uri, name="uri", curie=SLSA.curie('uri'),
                   model_uri=SLSA.uri, domain=None, range=Optional[str])

slots.digest = Slot(uri=SLSA.digest, name="digest", curie=SLSA.curie('digest'),
                   model_uri=SLSA.digest, domain=None, range=Optional[Union[dict, DigestSet]])

slots.name = Slot(uri=SLSA.name, name="name", curie=SLSA.curie('name'),
                   model_uri=SLSA.name, domain=None, range=Optional[str])

slots.downloadLocation = Slot(uri=SLSA.downloadLocation, name="downloadLocation", curie=SLSA.curie('downloadLocation'),
                   model_uri=SLSA.downloadLocation, domain=None, range=Optional[str])

slots.mediaType = Slot(uri=SLSA.mediaType, name="mediaType", curie=SLSA.curie('mediaType'),
                   model_uri=SLSA.mediaType, domain=None, range=Optional[str])

slots.annotations = Slot(uri=SLSA.annotations, name="annotations", curie=SLSA.curie('annotations'),
                   model_uri=SLSA.annotations, domain=None, range=Optional[Union[str, list[str]]])

slots._type = Slot(uri=SLSA._type, name="_type", curie=SLSA.curie('_type'),
                   model_uri=SLSA._type, domain=None, range=str)

slots.subject = Slot(uri=SLSA.subject, name="subject", curie=SLSA.curie('subject'),
                   model_uri=SLSA.subject, domain=None, range=Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]])

slots.predicateType = Slot(uri=SLSA.predicateType, name="predicateType", curie=SLSA.curie('predicateType'),
                   model_uri=SLSA.predicateType, domain=None, range=str)

slots.predicate = Slot(uri=SLSA.predicate, name="predicate", curie=SLSA.curie('predicate'),
                   model_uri=SLSA.predicate, domain=None, range=Optional[str])

slots.buildDefinition = Slot(uri=SLSA.buildDefinition, name="buildDefinition", curie=SLSA.curie('buildDefinition'),
                   model_uri=SLSA.buildDefinition, domain=None, range=Union[dict, BuildDefinition])

slots.runDetails = Slot(uri=SLSA.runDetails, name="runDetails", curie=SLSA.curie('runDetails'),
                   model_uri=SLSA.runDetails, domain=None, range=Union[dict, RunDetails])

slots.buildType = Slot(uri=SLSA.buildType, name="buildType", curie=SLSA.curie('buildType'),
                   model_uri=SLSA.buildType, domain=None, range=str)

slots.externalParameters = Slot(uri=SLSA.externalParameters, name="externalParameters", curie=SLSA.curie('externalParameters'),
                   model_uri=SLSA.externalParameters, domain=None, range=Optional[str])

slots.internalParameters = Slot(uri=SLSA.internalParameters, name="internalParameters", curie=SLSA.curie('internalParameters'),
                   model_uri=SLSA.internalParameters, domain=None, range=Optional[str])

slots.resolvedDependencies = Slot(uri=SLSA.resolvedDependencies, name="resolvedDependencies", curie=SLSA.curie('resolvedDependencies'),
                   model_uri=SLSA.resolvedDependencies, domain=None, range=Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]])

slots.builder = Slot(uri=SLSA.builder, name="builder", curie=SLSA.curie('builder'),
                   model_uri=SLSA.builder, domain=None, range=Union[dict, Builder])

slots.buildMetadata = Slot(uri=SLSA.buildMetadata, name="buildMetadata", curie=SLSA.curie('buildMetadata'),
                   model_uri=SLSA.buildMetadata, domain=None, range=Optional[Union[dict, BuildMetadata]])

slots.byproducts = Slot(uri=SLSA.byproducts, name="byproducts", curie=SLSA.curie('byproducts'),
                   model_uri=SLSA.byproducts, domain=None, range=Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]])

slots.id = Slot(uri=SLSA.id, name="id", curie=SLSA.curie('id'),
                   model_uri=SLSA.id, domain=None, range=str)

slots.version = Slot(uri=SLSA.version, name="version", curie=SLSA.curie('version'),
                   model_uri=SLSA.version, domain=None, range=Optional[str])

slots.builderDependencies = Slot(uri=SLSA.builderDependencies, name="builderDependencies", curie=SLSA.curie('builderDependencies'),
                   model_uri=SLSA.builderDependencies, domain=None, range=Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]])

slots.invocationId = Slot(uri=SLSA.invocationId, name="invocationId", curie=SLSA.curie('invocationId'),
                   model_uri=SLSA.invocationId, domain=None, range=Optional[str])

slots.startedOn = Slot(uri=SLSA.startedOn, name="startedOn", curie=SLSA.curie('startedOn'),
                   model_uri=SLSA.startedOn, domain=None, range=Optional[str])

slots.finishedOn = Slot(uri=SLSA.finishedOn, name="finishedOn", curie=SLSA.curie('finishedOn'),
                   model_uri=SLSA.finishedOn, domain=None, range=Optional[str])

slots.verifier = Slot(uri=SLSA.verifier, name="verifier", curie=SLSA.curie('verifier'),
                   model_uri=SLSA.verifier, domain=None, range=Union[dict, Verifier])

slots.timeVerified = Slot(uri=SLSA.timeVerified, name="timeVerified", curie=SLSA.curie('timeVerified'),
                   model_uri=SLSA.timeVerified, domain=None, range=Optional[str])

slots.resourceUri = Slot(uri=SLSA.resourceUri, name="resourceUri", curie=SLSA.curie('resourceUri'),
                   model_uri=SLSA.resourceUri, domain=None, range=str)

slots.policy = Slot(uri=SLSA.policy, name="policy", curie=SLSA.curie('policy'),
                   model_uri=SLSA.policy, domain=None, range=Union[dict, ResourceDescriptor])

slots.inputAttestations = Slot(uri=SLSA.inputAttestations, name="inputAttestations", curie=SLSA.curie('inputAttestations'),
                   model_uri=SLSA.inputAttestations, domain=None, range=Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]])

slots.verificationResult = Slot(uri=SLSA.verificationResult, name="verificationResult", curie=SLSA.curie('verificationResult'),
                   model_uri=SLSA.verificationResult, domain=None, range=Union[str, "VerificationResultEnum"])

slots.verifiedLevels = Slot(uri=SLSA.verifiedLevels, name="verifiedLevels", curie=SLSA.curie('verifiedLevels'),
                   model_uri=SLSA.verifiedLevels, domain=None, range=Union[Union[str, "SlsaResultEnum"], list[Union[str, "SlsaResultEnum"]]])

slots.dependencyLevels = Slot(uri=SLSA.dependencyLevels, name="dependencyLevels", curie=SLSA.curie('dependencyLevels'),
                   model_uri=SLSA.dependencyLevels, domain=None, range=Optional[str])

slots.slsaVersion = Slot(uri=SLSA.slsaVersion, name="slsaVersion", curie=SLSA.curie('slsaVersion'),
                   model_uri=SLSA.slsaVersion, domain=None, range=Optional[str])

slots.buildPlatformId = Slot(uri=SLSA.buildPlatformId, name="buildPlatformId", curie=SLSA.curie('buildPlatformId'),
                   model_uri=SLSA.buildPlatformId, domain=None, range=Optional[str])

slots.buildLevel = Slot(uri=SLSA.buildLevel, name="buildLevel", curie=SLSA.curie('buildLevel'),
                   model_uri=SLSA.buildLevel, domain=None, range=Optional[Union[str, "BuildLevelEnum"]])

slots.isHosted = Slot(uri=SLSA.isHosted, name="isHosted", curie=SLSA.curie('isHosted'),
                   model_uri=SLSA.isHosted, domain=None, range=Optional[Union[bool, Bool]])

slots.ecosystem = Slot(uri=SLSA.ecosystem, name="ecosystem", curie=SLSA.curie('ecosystem'),
                   model_uri=SLSA.ecosystem, domain=None, range=Optional[str])

slots.registry = Slot(uri=SLSA.registry, name="registry", curie=SLSA.curie('registry'),
                   model_uri=SLSA.registry, domain=None, range=Optional[str])

slots.artifact = Slot(uri=SLSA.artifact, name="artifact", curie=SLSA.curie('artifact'),
                   model_uri=SLSA.artifact, domain=None, range=Optional[Union[dict, ResourceDescriptor]])

slots.description = Slot(uri=SLSA.description, name="description", curie=SLSA.curie('description'),
                   model_uri=SLSA.description, domain=None, range=Optional[str])

slots.sourceLevel = Slot(uri=SLSA.sourceLevel, name="sourceLevel", curie=SLSA.curie('sourceLevel'),
                   model_uri=SLSA.sourceLevel, domain=None, range=Optional[Union[str, "SourceLevelEnum"]])

slots.revisionId = Slot(uri=SLSA.revisionId, name="revisionId", curie=SLSA.curie('revisionId'),
                   model_uri=SLSA.revisionId, domain=None, range=str)

slots.repository = Slot(uri=SLSA.repository, name="repository", curie=SLSA.curie('repository'),
                   model_uri=SLSA.repository, domain=None, range=Optional[Union[dict, SourceRepository]])

slots.author = Slot(uri=SLSA.author, name="author", curie=SLSA.curie('author'),
                   model_uri=SLSA.author, domain=None, range=Optional[str])

slots.timestamp = Slot(uri=SLSA.timestamp, name="timestamp", curie=SLSA.curie('timestamp'),
                   model_uri=SLSA.timestamp, domain=None, range=Optional[str])

slots.parentRevisions = Slot(uri=SLSA.parentRevisions, name="parentRevisions", curie=SLSA.curie('parentRevisions'),
                   model_uri=SLSA.parentRevisions, domain=None, range=Optional[Union[str, list[str]]])

slots.revision = Slot(uri=SLSA.revision, name="revision", curie=SLSA.curie('revision'),
                   model_uri=SLSA.revision, domain=None, range=Optional[Union[dict, SourceRevision]])

slots.controlsEnforced = Slot(uri=SLSA.controlsEnforced, name="controlsEnforced", curie=SLSA.curie('controlsEnforced'),
                   model_uri=SLSA.controlsEnforced, domain=None, range=Optional[Union[str, list[str]]])

slots.dependencies = Slot(uri=SLSA.dependencies, name="dependencies", curie=SLSA.curie('dependencies'),
                   model_uri=SLSA.dependencies, domain=None, range=Optional[Union[Union[dict, ResourceDescriptor], list[Union[dict, ResourceDescriptor]]]])

slots.dependencyLevel = Slot(uri=SLSA.dependencyLevel, name="dependencyLevel", curie=SLSA.curie('dependencyLevel'),
                   model_uri=SLSA.dependencyLevel, domain=None, range=Optional[Union[str, "DependencyLevelEnum"]])

slots.provenance = Slot(uri=SLSA.provenance, name="provenance", curie=SLSA.curie('provenance'),
                   model_uri=SLSA.provenance, domain=None, range=Optional[Union[dict, BuildProvenance]])

slots.buildEnvLevel = Slot(uri=SLSA.buildEnvLevel, name="buildEnvLevel", curie=SLSA.curie('buildEnvLevel'),
                   model_uri=SLSA.buildEnvLevel, domain=None, range=Optional[Union[str, "BuildEnvLevelEnum"]])

slots.buildId = Slot(uri=SLSA.buildId, name="buildId", curie=SLSA.curie('buildId'),
                   model_uri=SLSA.buildId, domain=None, range=str)

slots.buildImage = Slot(uri=SLSA.buildImage, name="buildImage", curie=SLSA.curie('buildImage'),
                   model_uri=SLSA.buildImage, domain=None, range=Optional[Union[dict, BuildImage]])

slots.measurements = Slot(uri=SLSA.measurements, name="measurements", curie=SLSA.curie('measurements'),
                   model_uri=SLSA.measurements, domain=None, range=Optional[Union[str, list[str]]])

slots.hermeticBuild = Slot(uri=SLSA.hermeticBuild, name="hermeticBuild", curie=SLSA.curie('hermeticBuild'),
                   model_uri=SLSA.hermeticBuild, domain=None, range=Optional[Union[bool, Bool]])

slots.provenanceGenerationTool = Slot(uri=SLSA.provenanceGenerationTool, name="provenanceGenerationTool", curie=SLSA.curie('provenanceGenerationTool'),
                   model_uri=SLSA.provenanceGenerationTool, domain=None, range=Optional[str])

slots.attestationStorageUri = Slot(uri=SLSA.attestationStorageUri, name="attestationStorageUri", curie=SLSA.curie('attestationStorageUri'),
                   model_uri=SLSA.attestationStorageUri, domain=None, range=Optional[str])

slots.reviewType = Slot(uri=SLSA.reviewType, name="reviewType", curie=SLSA.curie('reviewType'),
                   model_uri=SLSA.reviewType, domain=None, range=Optional[Union[str, "ReviewTypeEnum"]])

slots.versionTag = Slot(uri=SLSA.versionTag, name="versionTag", curie=SLSA.curie('versionTag'),
                   model_uri=SLSA.versionTag, domain=None, range=Optional[str])

slots.challenges = Slot(uri=SLSA.challenges, name="challenges", curie=SLSA.curie('challenges'),
                   model_uri=SLSA.challenges, domain=None, range=Optional[Union[Union[str, "AdoptionChallengeEnum"], list[Union[str, "AdoptionChallengeEnum"]]]])

slots.strategies = Slot(uri=SLSA.strategies, name="strategies", curie=SLSA.curie('strategies'),
                   model_uri=SLSA.strategies, domain=None, range=Optional[Union[Union[str, "AdoptionStrategyEnum"], list[Union[str, "AdoptionStrategyEnum"]]]])

slots.adoptionMetadata = Slot(uri=SLSA.adoptionMetadata, name="adoptionMetadata", curie=SLSA.curie('adoptionMetadata'),
                   model_uri=SLSA.adoptionMetadata, domain=None, range=Optional[Union[dict, AdoptionMetadata]])

slots.pipelineOrchestrator = Slot(uri=SLSA.pipelineOrchestrator, name="pipelineOrchestrator", curie=SLSA.curie('pipelineOrchestrator'),
                   model_uri=SLSA.pipelineOrchestrator, domain=None, range=Optional[str])

slots.signingTool = Slot(uri=SLSA.signingTool, name="signingTool", curie=SLSA.curie('signingTool'),
                   model_uri=SLSA.signingTool, domain=None, range=Optional[str])

slots.sigstoreLogEntry = Slot(uri=SLSA.sigstoreLogEntry, name="sigstoreLogEntry", curie=SLSA.curie('sigstoreLogEntry'),
                   model_uri=SLSA.sigstoreLogEntry, domain=None, range=Optional[str])

slots.guacUri = Slot(uri=SLSA.guacUri, name="guacUri", curie=SLSA.curie('guacUri'),
                   model_uri=SLSA.guacUri, domain=None, range=Optional[str])

slots.securityInsightsUri = Slot(uri=SLSA.securityInsightsUri, name="securityInsightsUri", curie=SLSA.curie('securityInsightsUri'),
                   model_uri=SLSA.securityInsightsUri, domain=None, range=Optional[str])

slots.SourceRepository_id = Slot(uri=SLSA.id, name="SourceRepository_id", curie=SLSA.curie('id'),
                   model_uri=SLSA.SourceRepository_id, domain=SourceRepository, range=str)

slots.BuildImage_id = Slot(uri=SLSA.id, name="BuildImage_id", curie=SLSA.curie('id'),
                   model_uri=SLSA.BuildImage_id, domain=BuildImage, range=str)
