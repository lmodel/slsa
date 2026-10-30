# Auto generated from slsa.yaml by pythongen.py version: 0.0.1
# Schema: slsa
#
# id: https://w3id.org/lmodel/slsa
# description: A LinkML model of the SLSA specification: its tracks and levels, the roles and systems in a software supply chain, and the in-toto attestations that carry build provenance and verification summaries.
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

from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDateTime

metamodel_version = "1.12.0"
version = "1.2.0"

# Namespaces
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
IN_TOTO_LINKML = CurieNamespace('in_toto_linkml', 'https://w3id.org/lmodel/in-toto/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SLSA = CurieNamespace('slsa', 'https://w3id.org/lmodel/slsa/')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SLSA


# Types
class SlsaResultValue(String):
    """ A result as a VSA writes it: one of the SLSA-defined results SlsaResult lists, or one of the issuer's own, which never starts with SLSA_. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "slsa_result_value"
    type_model_uri = SLSA.SlsaResultValue


class InTotoResourceUri(Uri):
    """ A URI that identifies or locates a resource, such as a package URL or a git repository address, with its scheme and authority in lowercase. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "in_toto_resource_uri"
    type_model_uri = SLSA.InTotoResourceUri


class InTotoTypeUri(Uri):
    """ A URI that names a type, such as a statement's or a predicate's, with its scheme and authority in lowercase. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "in_toto_type_uri"
    type_model_uri = SLSA.InTotoTypeUri


class InTotoTimestamp(String):
    """ A point in time in RFC 3339 format in the UTC time zone, written with a trailing Z, such as 1985-04-12T23:20:50.52Z. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "in_toto_timestamp"
    type_model_uri = SLSA.InTotoTimestamp


# Class references
class SlsaBuildPlatformBuilderId(URI):
    pass


class SlsaPackageRegistryRegistryUri(URI):
    pass


class SlsaSourceControlSystemScsUri(URI):
    pass


class SlsaSourceRepositoryRepositoryUri(URI):
    pass


class SlsaSourceRevisionRevisionId(extended_str):
    pass


class SlsaBuildImageImageUri(URI):
    pass


@dataclass(repr=False)
class SlsaDocument(YAMLRoot):
    """
    A document that holds SLSA attestations and the parties, platforms, packages, repositories and images they concern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaDocument"]
    class_class_curie: ClassVar[str] = "slsa:SlsaDocument"
    class_name: ClassVar[str] = "SlsaDocument"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaDocument

    attestations: Optional[Union[Union[dict, "SlsaStatement"], list[Union[dict, "SlsaStatement"]]]] = empty_list()
    parties: Optional[Union[Union[dict, "SlsaParty"], list[Union[dict, "SlsaParty"]]]] = empty_list()
    build_platforms: Optional[Union[dict[Union[str, SlsaBuildPlatformBuilderId], Union[dict, "SlsaBuildPlatform"]], list[Union[dict, "SlsaBuildPlatform"]]]] = empty_dict()
    control_planes: Optional[Union[Union[dict, "SlsaControlPlane"], list[Union[dict, "SlsaControlPlane"]]]] = empty_list()
    packages: Optional[Union[Union[dict, "SlsaPackage"], list[Union[dict, "SlsaPackage"]]]] = empty_list()
    package_registries: Optional[Union[dict[Union[str, SlsaPackageRegistryRegistryUri], Union[dict, "SlsaPackageRegistry"]], list[Union[dict, "SlsaPackageRegistry"]]]] = empty_dict()
    source_control_systems: Optional[Union[list[Union[str, SlsaSourceControlSystemScsUri]], dict[Union[str, SlsaSourceControlSystemScsUri], Union[dict, "SlsaSourceControlSystem"]]]] = empty_dict()
    source_repositories: Optional[Union[dict[Union[str, SlsaSourceRepositoryRepositoryUri], Union[dict, "SlsaSourceRepository"]], list[Union[dict, "SlsaSourceRepository"]]]] = empty_dict()
    source_revisions: Optional[Union[dict[Union[str, SlsaSourceRevisionRevisionId], Union[dict, "SlsaSourceRevision"]], list[Union[dict, "SlsaSourceRevision"]]]] = empty_dict()
    named_references: Optional[Union[Union[dict, "SlsaNamedReference"], list[Union[dict, "SlsaNamedReference"]]]] = empty_list()
    build_images: Optional[Union[dict[Union[str, SlsaBuildImageImageUri], Union[dict, "SlsaBuildImage"]], list[Union[dict, "SlsaBuildImage"]]]] = empty_dict()
    dependency_inventories: Optional[Union[Union[dict, "SlsaDependencyInventory"], list[Union[dict, "SlsaDependencyInventory"]]]] = empty_list()
    adoption_metadata: Optional[Union[dict, "SlsaAdoptionMetadata"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="attestations", slot_type=SlsaStatement, key_name="statement_type", keyed=False)

        if not isinstance(self.parties, list):
            self.parties = [self.parties] if self.parties is not None else []
        self.parties = [v if isinstance(v, SlsaParty) else SlsaParty(**as_dict(v)) for v in self.parties]

        self._normalize_inlined_as_list(slot_name="build_platforms", slot_type=SlsaBuildPlatform, key_name="builder_id", keyed=True)

        if not isinstance(self.control_planes, list):
            self.control_planes = [self.control_planes] if self.control_planes is not None else []
        self.control_planes = [v if isinstance(v, SlsaControlPlane) else SlsaControlPlane(**as_dict(v)) for v in self.control_planes]

        self._normalize_inlined_as_list(slot_name="packages", slot_type=SlsaPackage, key_name="package_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="package_registries", slot_type=SlsaPackageRegistry, key_name="registry_uri", keyed=True)

        self._normalize_inlined_as_list(slot_name="source_control_systems", slot_type=SlsaSourceControlSystem, key_name="scs_uri", keyed=True)

        self._normalize_inlined_as_list(slot_name="source_repositories", slot_type=SlsaSourceRepository, key_name="repository_uri", keyed=True)

        self._normalize_inlined_as_list(slot_name="source_revisions", slot_type=SlsaSourceRevision, key_name="revision_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="named_references", slot_type=SlsaNamedReference, key_name="reference_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="build_images", slot_type=SlsaBuildImage, key_name="image_uri", keyed=True)

        if not isinstance(self.dependency_inventories, list):
            self.dependency_inventories = [self.dependency_inventories] if self.dependency_inventories is not None else []
        self.dependency_inventories = [v if isinstance(v, SlsaDependencyInventory) else SlsaDependencyInventory(**as_dict(v)) for v in self.dependency_inventories]

        if self.adoption_metadata is not None and not isinstance(self.adoption_metadata, SlsaAdoptionMetadata):
            self.adoption_metadata = SlsaAdoptionMetadata(**as_dict(self.adoption_metadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaParty(YAMLRoot):
    """
    A person or organization that takes part in a software supply chain, in one of the roles SLSA names.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaParty"]
    class_class_curie: ClassVar[str] = "slsa:SlsaParty"
    class_name: ClassVar[str] = "SlsaParty"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaParty

    party_type: Optional[str] = None
    party_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.party_type = str(self.class_name)

        if self.party_name is not None and not isinstance(self.party_name, str):
            self.party_name = str(self.party_name)

        super().__post_init__(**kwargs)
        self.unknown_party_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "party_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class SlsaProducer(SlsaParty):
    """
    A party that creates software and provides it to others, choosing a build platform and distributing provenance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaProducer"]
    class_class_curie: ClassVar[str] = "slsa:SlsaProducer"
    class_name: ClassVar[str] = "SlsaProducer"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaProducer

    build_platform: Optional[Union[str, SlsaBuildPlatformBuilderId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.build_platform is not None and not isinstance(self.build_platform, SlsaBuildPlatformBuilderId):
            self.build_platform = SlsaBuildPlatformBuilderId(self.build_platform)

        super().__post_init__(**kwargs)
        self.unknown_party_type = str(self.class_name)


class SlsaConsumer(SlsaParty):
    """
    A party that uses software a producer provides, verifying its provenance itself or through a verifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaConsumer"]
    class_class_curie: ClassVar[str] = "slsa:SlsaConsumer"
    class_name: ClassVar[str] = "SlsaConsumer"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaConsumer


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.unknown_party_type = str(self.class_name)


@dataclass(repr=False)
class SlsaVerifier(SlsaParty):
    """
    A party that inspects provenance or other attestations and decides whether an artifact is authentic.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaVerifier"]
    class_class_curie: ClassVar[str] = "slsa:SlsaVerifier"
    class_name: ClassVar[str] = "SlsaVerifier"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaVerifier

    verifier_id: Union[str, URI] = None
    component_versions: Optional[Union[Union[dict, "SlsaComponentVersion"], list[Union[dict, "SlsaComponentVersion"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.verifier_id):
            self.MissingRequiredField("verifier_id")
        if not isinstance(self.verifier_id, URI):
            self.verifier_id = URI(self.verifier_id)

        self._normalize_inlined_as_list(slot_name="component_versions", slot_type=SlsaComponentVersion, key_name="component", keyed=False)

        super().__post_init__(**kwargs)
        self.unknown_party_type = str(self.class_name)


class SlsaInfrastructureProvider(SlsaParty):
    """
    A party that provides software or services to the other roles, such as a package registry's or a build platform's
    maintainers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaInfrastructureProvider"]
    class_class_curie: ClassVar[str] = "slsa:SlsaInfrastructureProvider"
    class_name: ClassVar[str] = "SlsaInfrastructureProvider"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaInfrastructureProvider


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.unknown_party_type = str(self.class_name)


@dataclass(repr=False)
class SlsaBuildPlatform(YAMLRoot):
    """
    The system that runs builds and records their provenance: the transitive closure of software, hardware, people and
    organizations trusted to do so. Provenance names it as the builder.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildPlatform"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildPlatform"
    class_name: ClassVar[str] = "SlsaBuildPlatform"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildPlatform

    builder_id: Union[str, SlsaBuildPlatformBuilderId] = None
    component_versions: Optional[Union[Union[dict, "SlsaComponentVersion"], list[Union[dict, "SlsaComponentVersion"]]]] = empty_list()
    build_level: Optional[Union[str, "SlsaBuildLevel"]] = None
    hosted: Optional[Union[bool, Bool]] = None
    builder_dependencies: Optional[Union[Union[dict, "InTotoResourceDescriptor"], list[Union[dict, "InTotoResourceDescriptor"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.builder_id):
            self.MissingRequiredField("builder_id")
        if not isinstance(self.builder_id, SlsaBuildPlatformBuilderId):
            self.builder_id = SlsaBuildPlatformBuilderId(self.builder_id)

        self._normalize_inlined_as_list(slot_name="component_versions", slot_type=SlsaComponentVersion, key_name="component", keyed=False)

        if self.build_level is not None and not isinstance(self.build_level, SlsaBuildLevel):
            self.build_level = SlsaBuildLevel(self.build_level)

        if self.hosted is not None and not isinstance(self.hosted, Bool):
            self.hosted = Bool(self.hosted)

        if not isinstance(self.builder_dependencies, list):
            self.builder_dependencies = [self.builder_dependencies] if self.builder_dependencies is not None else []
        self.builder_dependencies = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.builder_dependencies]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaControlPlane(YAMLRoot):
    """
    The component of a build platform that orchestrates each build and generates its provenance, outside the tenant's
    control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaControlPlane"]
    class_class_curie: ClassVar[str] = "slsa:SlsaControlPlane"
    class_name: ClassVar[str] = "SlsaControlPlane"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaControlPlane

    build_platform: Optional[Union[str, SlsaBuildPlatformBuilderId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.build_platform is not None and not isinstance(self.build_platform, SlsaBuildPlatformBuilderId):
            self.build_platform = SlsaBuildPlatformBuilderId(self.build_platform)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaComponentVersion(YAMLRoot):
    """
    The version of one named component of a platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaComponentVersion"]
    class_class_curie: ClassVar[str] = "slsa:SlsaComponentVersion"
    class_name: ClassVar[str] = "SlsaComponentVersion"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaComponentVersion

    component: str = None
    component_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component):
            self.MissingRequiredField("component")
        if not isinstance(self.component, str):
            self.component = str(self.component)

        if self.component_version is not None and not isinstance(self.component_version, str):
            self.component_version = str(self.component_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaPackageRegistry(YAMLRoot):
    """
    A distribution platform that resolves package names to immutable package artifacts within an ecosystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaPackageRegistry"]
    class_class_curie: ClassVar[str] = "slsa:SlsaPackageRegistry"
    class_name: ClassVar[str] = "SlsaPackageRegistry"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaPackageRegistry

    registry_uri: Union[str, SlsaPackageRegistryRegistryUri] = None
    ecosystem: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.registry_uri):
            self.MissingRequiredField("registry_uri")
        if not isinstance(self.registry_uri, SlsaPackageRegistryRegistryUri):
            self.registry_uri = SlsaPackageRegistryRegistryUri(self.registry_uri)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaPackage(YAMLRoot):
    """
    A unit of software distributed under a package name, which is the primary security boundary SLSA protects. Its
    artifacts are the outputs of builds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaPackage"]
    class_class_curie: ClassVar[str] = "slsa:SlsaPackage"
    class_name: ClassVar[str] = "SlsaPackage"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaPackage

    package_name: str = None
    ecosystem: Optional[str] = None
    registry: Optional[Union[str, SlsaPackageRegistryRegistryUri]] = None
    package_artifacts: Optional[Union[Union[dict, "InTotoResourceDescriptor"], list[Union[dict, "InTotoResourceDescriptor"]]]] = empty_list()
    guac_uri: Optional[Union[str, URI]] = None
    security_insights_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.package_name):
            self.MissingRequiredField("package_name")
        if not isinstance(self.package_name, str):
            self.package_name = str(self.package_name)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.registry is not None and not isinstance(self.registry, SlsaPackageRegistryRegistryUri):
            self.registry = SlsaPackageRegistryRegistryUri(self.registry)

        if not isinstance(self.package_artifacts, list):
            self.package_artifacts = [self.package_artifacts] if self.package_artifacts is not None else []
        self.package_artifacts = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.package_artifacts]

        if self.guac_uri is not None and not isinstance(self.guac_uri, URI):
            self.guac_uri = URI(self.guac_uri)

        if self.security_insights_uri is not None and not isinstance(self.security_insights_uri, URI):
            self.security_insights_uri = URI(self.security_insights_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaBuildDefinition(YAMLRoot):
    """
    The inputs to a build, in enough detail to initialize it and begin execution; the builder vouches for their
    accuracy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildDefinition"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildDefinition"
    class_name: ClassVar[str] = "SlsaBuildDefinition"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildDefinition

    build_type: Union[str, URI] = None
    external_parameters: Union[Union[dict, "SlsaBuildParameter"], list[Union[dict, "SlsaBuildParameter"]]] = None
    internal_parameters: Optional[Union[Union[dict, "SlsaBuildParameter"], list[Union[dict, "SlsaBuildParameter"]]]] = empty_list()
    resolved_dependencies: Optional[Union[Union[dict, "InTotoResourceDescriptor"], list[Union[dict, "InTotoResourceDescriptor"]]]] = empty_list()
    hermetic: Optional[Union[bool, Bool]] = None
    provenance_generation_tool: Optional[Union[str, URI]] = None
    pipeline_orchestrator: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.build_type):
            self.MissingRequiredField("build_type")
        if not isinstance(self.build_type, URI):
            self.build_type = URI(self.build_type)

        if self._is_empty(self.external_parameters):
            self.MissingRequiredField("external_parameters")
        self._normalize_inlined_as_list(slot_name="external_parameters", slot_type=SlsaBuildParameter, key_name="parameter_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="internal_parameters", slot_type=SlsaBuildParameter, key_name="parameter_name", keyed=False)

        if not isinstance(self.resolved_dependencies, list):
            self.resolved_dependencies = [self.resolved_dependencies] if self.resolved_dependencies is not None else []
        self.resolved_dependencies = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.resolved_dependencies]

        if self.hermetic is not None and not isinstance(self.hermetic, Bool):
            self.hermetic = Bool(self.hermetic)

        if self.provenance_generation_tool is not None and not isinstance(self.provenance_generation_tool, URI):
            self.provenance_generation_tool = URI(self.provenance_generation_tool)

        if self.pipeline_orchestrator is not None and not isinstance(self.pipeline_orchestrator, URI):
            self.pipeline_orchestrator = URI(self.pipeline_orchestrator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaBuildParameter(YAMLRoot):
    """
    One named input to a build, with a string value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildParameter"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildParameter"
    class_name: ClassVar[str] = "SlsaBuildParameter"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildParameter

    parameter_name: str = None
    parameter_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.parameter_name):
            self.MissingRequiredField("parameter_name")
        if not isinstance(self.parameter_name, str):
            self.parameter_name = str(self.parameter_name)

        if self.parameter_value is not None and not isinstance(self.parameter_value, str):
            self.parameter_value = str(self.parameter_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaRunDetails(YAMLRoot):
    """
    What is specific to one execution of a build: the platform that ran it, metadata about the run and its by-products.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaRunDetails"]
    class_class_curie: ClassVar[str] = "slsa:SlsaRunDetails"
    class_name: ClassVar[str] = "SlsaRunDetails"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaRunDetails

    builder: Union[dict, SlsaBuildPlatform] = None
    build_metadata: Optional[Union[dict, "SlsaBuildMetadata"]] = None
    byproducts: Optional[Union[Union[dict, "InTotoResourceDescriptor"], list[Union[dict, "InTotoResourceDescriptor"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.builder):
            self.MissingRequiredField("builder")
        if not isinstance(self.builder, SlsaBuildPlatform):
            self.builder = SlsaBuildPlatform(**as_dict(self.builder))

        if self.build_metadata is not None and not isinstance(self.build_metadata, SlsaBuildMetadata):
            self.build_metadata = SlsaBuildMetadata(**as_dict(self.build_metadata))

        if not isinstance(self.byproducts, list):
            self.byproducts = [self.byproducts] if self.byproducts is not None else []
        self.byproducts = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.byproducts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaBuildMetadata(YAMLRoot):
    """
    Metadata about one execution of a build: its identifier and when it started and finished.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildMetadata"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildMetadata"
    class_name: ClassVar[str] = "SlsaBuildMetadata"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildMetadata

    invocation_id: Optional[str] = None
    started_on: Optional[Union[str, XSDDateTime]] = None
    finished_on: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.invocation_id is not None and not isinstance(self.invocation_id, str):
            self.invocation_id = str(self.invocation_id)

        if self.started_on is not None and not isinstance(self.started_on, XSDDateTime):
            self.started_on = XSDDateTime(self.started_on)

        if self.finished_on is not None and not isinstance(self.finished_on, XSDDateTime):
            self.finished_on = XSDDateTime(self.finished_on)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaDependencyLevelCount(YAMLRoot):
    """
    The number of an artifact's transitive dependencies verified at one level, each counted once per track at its
    highest level.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaDependencyLevelCount"]
    class_class_curie: ClassVar[str] = "slsa:SlsaDependencyLevelCount"
    class_name: ClassVar[str] = "SlsaDependencyLevelCount"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaDependencyLevelCount

    verified_level: Union[str, SlsaResultValue] = None
    dependency_count: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.verified_level):
            self.MissingRequiredField("verified_level")
        if not isinstance(self.verified_level, SlsaResultValue):
            self.verified_level = SlsaResultValue(self.verified_level)

        if self._is_empty(self.dependency_count):
            self.MissingRequiredField("dependency_count")
        if not isinstance(self.dependency_count, int):
            self.dependency_count = int(self.dependency_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaSourceControlSystem(YAMLRoot):
    """
    The platform or services that host a source repository and enforce its organization's policies on authentication,
    authorization and change management.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaSourceControlSystem"]
    class_class_curie: ClassVar[str] = "slsa:SlsaSourceControlSystem"
    class_name: ClassVar[str] = "SlsaSourceControlSystem"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaSourceControlSystem

    scs_uri: Union[str, SlsaSourceControlSystemScsUri] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scs_uri):
            self.MissingRequiredField("scs_uri")
        if not isinstance(self.scs_uri, SlsaSourceControlSystemScsUri):
            self.scs_uri = SlsaSourceControlSystemScsUri(self.scs_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaSourceRepository(YAMLRoot):
    """
    A self-contained unit that holds a set of files, their revision history and metadata such as branches and tags.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaSourceRepository"]
    class_class_curie: ClassVar[str] = "slsa:SlsaSourceRepository"
    class_name: ClassVar[str] = "SlsaSourceRepository"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaSourceRepository

    repository_uri: Union[str, SlsaSourceRepositoryRepositoryUri] = None
    hosted_by: Optional[Union[str, SlsaSourceControlSystemScsUri]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.repository_uri):
            self.MissingRequiredField("repository_uri")
        if not isinstance(self.repository_uri, SlsaSourceRepositoryRepositoryUri):
            self.repository_uri = SlsaSourceRepositoryRepositoryUri(self.repository_uri)

        if self.hosted_by is not None and not isinstance(self.hosted_by, SlsaSourceControlSystemScsUri):
            self.hosted_by = SlsaSourceControlSystemScsUri(self.hosted_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaSourceRevision(YAMLRoot):
    """
    A logically immutable snapshot of a repository's tracked files, with its version-control metadata: author, time
    and parent revisions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaSourceRevision"]
    class_class_curie: ClassVar[str] = "slsa:SlsaSourceRevision"
    class_name: ClassVar[str] = "SlsaSourceRevision"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaSourceRevision

    revision_id: Union[str, SlsaSourceRevisionRevisionId] = None
    repository: Optional[Union[str, SlsaSourceRepositoryRepositoryUri]] = None
    authored_by: Optional[str] = None
    authored_at: Optional[Union[str, XSDDateTime]] = None
    parent_revisions: Optional[Union[Union[str, SlsaSourceRevisionRevisionId], list[Union[str, SlsaSourceRevisionRevisionId]]]] = empty_list()
    source_level: Optional[Union[str, "SlsaSourceLevel"]] = None
    review_type: Optional[Union[str, "SlsaReviewType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.revision_id):
            self.MissingRequiredField("revision_id")
        if not isinstance(self.revision_id, SlsaSourceRevisionRevisionId):
            self.revision_id = SlsaSourceRevisionRevisionId(self.revision_id)

        if self.repository is not None and not isinstance(self.repository, SlsaSourceRepositoryRepositoryUri):
            self.repository = SlsaSourceRepositoryRepositoryUri(self.repository)

        if self.authored_by is not None and not isinstance(self.authored_by, str):
            self.authored_by = str(self.authored_by)

        if self.authored_at is not None and not isinstance(self.authored_at, XSDDateTime):
            self.authored_at = XSDDateTime(self.authored_at)

        if not isinstance(self.parent_revisions, list):
            self.parent_revisions = [self.parent_revisions] if self.parent_revisions is not None else []
        self.parent_revisions = [v if isinstance(v, SlsaSourceRevisionRevisionId) else SlsaSourceRevisionRevisionId(v) for v in self.parent_revisions]

        if self.source_level is not None and not isinstance(self.source_level, SlsaSourceLevel):
            self.source_level = SlsaSourceLevel(self.source_level)

        if self.review_type is not None and not isinstance(self.review_type, SlsaReviewType):
            self.review_type = SlsaReviewType(self.review_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaNamedReference(YAMLRoot):
    """
    A user-friendly name for a revision in a repository, such as main or v1.2.3; reference_type says whether it is a
    branch or a tag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaNamedReference"]
    class_class_curie: ClassVar[str] = "slsa:SlsaNamedReference"
    class_name: ClassVar[str] = "SlsaNamedReference"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaNamedReference

    reference_name: str = None
    repository: Optional[Union[str, SlsaSourceRepositoryRepositoryUri]] = None
    revision: Optional[Union[str, SlsaSourceRevisionRevisionId]] = None
    reference_type: Optional[str] = None
    protected: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_name):
            self.MissingRequiredField("reference_name")
        if not isinstance(self.reference_name, str):
            self.reference_name = str(self.reference_name)

        if self.repository is not None and not isinstance(self.repository, SlsaSourceRepositoryRepositoryUri):
            self.repository = SlsaSourceRepositoryRepositoryUri(self.repository)

        if self.revision is not None and not isinstance(self.revision, SlsaSourceRevisionRevisionId):
            self.revision = SlsaSourceRevisionRevisionId(self.revision)

        self.reference_type = str(self.class_name)

        if self.protected is not None and not isinstance(self.protected, Bool):
            self.protected = Bool(self.protected)

        super().__post_init__(**kwargs)
        self.unknown_reference_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "reference_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class SlsaBranch(SlsaNamedReference):
    """
    A named reference that moves to track a line of development.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBranch"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBranch"
    class_name: ClassVar[str] = "SlsaBranch"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBranch

    reference_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.unknown_reference_type = str(self.class_name)


@dataclass(repr=False)
class SlsaTag(SlsaNamedReference):
    """
    A named reference meant never to move once created.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaTag"]
    class_class_curie: ClassVar[str] = "slsa:SlsaTag"
    class_name: ClassVar[str] = "SlsaTag"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaTag

    reference_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.unknown_reference_type = str(self.class_name)


@dataclass(repr=False)
class SlsaDependencyInventory(YAMLRoot):
    """
    The inventory of every third-party build dependency, direct and transitive, of one artifact version.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaDependencyInventory"]
    class_class_curie: ClassVar[str] = "slsa:SlsaDependencyInventory"
    class_name: ClassVar[str] = "SlsaDependencyInventory"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaDependencyInventory

    artifact: Union[dict, "InTotoResourceDescriptor"] = None
    dependencies: Optional[Union[Union[dict, "InTotoResourceDescriptor"], list[Union[dict, "InTotoResourceDescriptor"]]]] = empty_list()
    dependency_level: Optional[Union[str, "SlsaDependencyLevel"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.artifact):
            self.MissingRequiredField("artifact")
        if not isinstance(self.artifact, InTotoResourceDescriptor):
            self.artifact = InTotoResourceDescriptor(**as_dict(self.artifact))

        if not isinstance(self.dependencies, list):
            self.dependencies = [self.dependencies] if self.dependencies is not None else []
        self.dependencies = [v if isinstance(v, InTotoResourceDescriptor) else InTotoResourceDescriptor(**as_dict(v)) for v in self.dependencies]

        if self.dependency_level is not None and not isinstance(self.dependency_level, SlsaDependencyLevel):
            self.dependency_level = SlsaDependencyLevel(self.dependency_level)

        super().__post_init__(**kwargs)


class SlsaBuildImageProducer(SlsaParty):
    """
    The party that creates and distributes build images; the hosted build platform itself, or a third party in a
    bring-your-own-image setting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildImageProducer"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildImageProducer"
    class_name: ClassVar[str] = "SlsaBuildImageProducer"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildImageProducer


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.unknown_party_type = str(self.class_name)


@dataclass(repr=False)
class SlsaBuildImage(YAMLRoot):
    """
    The template a build environment is instantiated from, such as a VM or container image: root filesystem, guest OS
    and packages, build executor and build agent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildImage"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildImage"
    class_name: ClassVar[str] = "SlsaBuildImage"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildImage

    image_uri: Union[str, SlsaBuildImageImageUri] = None
    build_env_level: Optional[Union[str, "SlsaBuildEnvironmentLevel"]] = None
    provenance: Optional[Union[dict, "SlsaBuildProvenance"]] = None
    produced_by: Optional[Union[dict, SlsaBuildImageProducer]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.image_uri):
            self.MissingRequiredField("image_uri")
        if not isinstance(self.image_uri, SlsaBuildImageImageUri):
            self.image_uri = SlsaBuildImageImageUri(self.image_uri)

        if self.build_env_level is not None and not isinstance(self.build_env_level, SlsaBuildEnvironmentLevel):
            self.build_env_level = SlsaBuildEnvironmentLevel(self.build_env_level)

        if self.provenance is not None and not isinstance(self.provenance, SlsaBuildProvenance):
            self.provenance = SlsaBuildProvenance(**as_dict(self.provenance))

        if self.produced_by is not None and not isinstance(self.produced_by, SlsaBuildImageProducer):
            self.produced_by = SlsaBuildImageProducer(**as_dict(self.produced_by))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaMeasurement(YAMLRoot):
    """
    The digest of one component or state of a build environment, to compare with its reference value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaMeasurement"]
    class_class_curie: ClassVar[str] = "slsa:SlsaMeasurement"
    class_name: ClassVar[str] = "SlsaMeasurement"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaMeasurement

    measured_component: str = None
    digest: Optional[Union[dict, "InTotoDigestSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measured_component):
            self.MissingRequiredField("measured_component")
        if not isinstance(self.measured_component, str):
            self.measured_component = str(self.measured_component)

        if self.digest is not None and not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaAdoptionMetadata(YAMLRoot):
    """
    The adoption challenges a deployment meets and the strategies it applies, from the study's taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaAdoptionMetadata"]
    class_class_curie: ClassVar[str] = "slsa:SlsaAdoptionMetadata"
    class_name: ClassVar[str] = "SlsaAdoptionMetadata"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaAdoptionMetadata

    challenges: Optional[Union[Union[str, "SlsaAdoptionChallenge"], list[Union[str, "SlsaAdoptionChallenge"]]]] = empty_list()
    strategies: Optional[Union[Union[str, "SlsaAdoptionStrategy"], list[Union[str, "SlsaAdoptionStrategy"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.challenges, list):
            self.challenges = [self.challenges] if self.challenges is not None else []
        self.challenges = [v if isinstance(v, SlsaAdoptionChallenge) else SlsaAdoptionChallenge(v) for v in self.challenges]

        if not isinstance(self.strategies, list):
            self.strategies = [self.strategies] if self.strategies is not None else []
        self.strategies = [v if isinstance(v, SlsaAdoptionStrategy) else SlsaAdoptionStrategy(v) for v in self.strategies]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoDigestSet(YAMLRoot):
    """
    A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it
    trusts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoDigestSet"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoDigestSet"
    class_name: ClassVar[str] = "InTotoDigestSet"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoDigestSet

    sha256: Optional[str] = None
    sha224: Optional[str] = None
    sha384: Optional[str] = None
    sha512: Optional[str] = None
    sha512_224: Optional[str] = None
    sha512_256: Optional[str] = None
    sha3_224: Optional[str] = None
    sha3_256: Optional[str] = None
    sha3_384: Optional[str] = None
    sha3_512: Optional[str] = None
    shake128: Optional[str] = None
    shake256: Optional[str] = None
    blake2b: Optional[str] = None
    blake2s: Optional[str] = None
    ripemd160: Optional[str] = None
    sm3: Optional[str] = None
    gost: Optional[str] = None
    sha1: Optional[str] = None
    md5: Optional[str] = None
    dir_hash: Optional[str] = None
    git_commit: Optional[str] = None
    git_tree: Optional[str] = None
    git_blob: Optional[str] = None
    git_tag: Optional[str] = None
    additional_digests: Optional[Union[Union[dict, "InTotoAdditionalDigest"], list[Union[dict, "InTotoAdditionalDigest"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sha256 is not None and not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self.sha224 is not None and not isinstance(self.sha224, str):
            self.sha224 = str(self.sha224)

        if self.sha384 is not None and not isinstance(self.sha384, str):
            self.sha384 = str(self.sha384)

        if self.sha512 is not None and not isinstance(self.sha512, str):
            self.sha512 = str(self.sha512)

        if self.sha512_224 is not None and not isinstance(self.sha512_224, str):
            self.sha512_224 = str(self.sha512_224)

        if self.sha512_256 is not None and not isinstance(self.sha512_256, str):
            self.sha512_256 = str(self.sha512_256)

        if self.sha3_224 is not None and not isinstance(self.sha3_224, str):
            self.sha3_224 = str(self.sha3_224)

        if self.sha3_256 is not None and not isinstance(self.sha3_256, str):
            self.sha3_256 = str(self.sha3_256)

        if self.sha3_384 is not None and not isinstance(self.sha3_384, str):
            self.sha3_384 = str(self.sha3_384)

        if self.sha3_512 is not None and not isinstance(self.sha3_512, str):
            self.sha3_512 = str(self.sha3_512)

        if self.shake128 is not None and not isinstance(self.shake128, str):
            self.shake128 = str(self.shake128)

        if self.shake256 is not None and not isinstance(self.shake256, str):
            self.shake256 = str(self.shake256)

        if self.blake2b is not None and not isinstance(self.blake2b, str):
            self.blake2b = str(self.blake2b)

        if self.blake2s is not None and not isinstance(self.blake2s, str):
            self.blake2s = str(self.blake2s)

        if self.ripemd160 is not None and not isinstance(self.ripemd160, str):
            self.ripemd160 = str(self.ripemd160)

        if self.sm3 is not None and not isinstance(self.sm3, str):
            self.sm3 = str(self.sm3)

        if self.gost is not None and not isinstance(self.gost, str):
            self.gost = str(self.gost)

        if self.sha1 is not None and not isinstance(self.sha1, str):
            self.sha1 = str(self.sha1)

        if self.md5 is not None and not isinstance(self.md5, str):
            self.md5 = str(self.md5)

        if self.dir_hash is not None and not isinstance(self.dir_hash, str):
            self.dir_hash = str(self.dir_hash)

        if self.git_commit is not None and not isinstance(self.git_commit, str):
            self.git_commit = str(self.git_commit)

        if self.git_tree is not None and not isinstance(self.git_tree, str):
            self.git_tree = str(self.git_tree)

        if self.git_blob is not None and not isinstance(self.git_blob, str):
            self.git_blob = str(self.git_blob)

        if self.git_tag is not None and not isinstance(self.git_tag, str):
            self.git_tag = str(self.git_tag)

        self._normalize_inlined_as_list(slot_name="additional_digests", slot_type=InTotoAdditionalDigest, key_name="algorithm", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoAdditionalDigest(YAMLRoot):
    """
    One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoAdditionalDigest"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoAdditionalDigest"
    class_name: ClassVar[str] = "InTotoAdditionalDigest"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoAdditionalDigest

    algorithm: str = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoAnnotation(YAMLRoot):
    """
    One vendor-specific annotation on a resource descriptor: a key and its values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoAnnotation"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoAnnotation"
    class_name: ClassVar[str] = "InTotoAnnotation"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoAnnotation

    annotation_key: str = None
    annotation_values: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.annotation_key):
            self.MissingRequiredField("annotation_key")
        if not isinstance(self.annotation_key, str):
            self.annotation_key = str(self.annotation_key)

        if not isinstance(self.annotation_values, list):
            self.annotation_values = [self.annotation_values] if self.annotation_values is not None else []
        self.annotation_values = [v if isinstance(v, str) else str(v) for v in self.annotation_values]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoResourceDescriptor(YAMLRoot):
    """
    A reference to a software artifact or other resource by URI or digest, or the resource itself as content, with
    optional metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoResourceDescriptor"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoResourceDescriptor"
    class_name: ClassVar[str] = "InTotoResourceDescriptor"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoResourceDescriptor

    resource_uri: Optional[Union[str, InTotoResourceUri]] = None
    digest: Optional[Union[dict, InTotoDigestSet]] = None
    resource_name: Optional[str] = None
    download_location: Optional[Union[str, InTotoResourceUri]] = None
    media_type: Optional[str] = None
    content: Optional[str] = None
    annotations: Optional[Union[Union[dict, InTotoAnnotation], list[Union[dict, InTotoAnnotation]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.resource_uri is not None and not isinstance(self.resource_uri, InTotoResourceUri):
            self.resource_uri = InTotoResourceUri(self.resource_uri)

        if self.digest is not None and not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        if self.resource_name is not None and not isinstance(self.resource_name, str):
            self.resource_name = str(self.resource_name)

        if self.download_location is not None and not isinstance(self.download_location, InTotoResourceUri):
            self.download_location = InTotoResourceUri(self.download_location)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        self._normalize_inlined_as_list(slot_name="annotations", slot_type=InTotoAnnotation, key_name="annotation_key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaVerificationSummaryPolicy(InTotoResourceDescriptor):
    """
    The policy a verification summary applied: a resource descriptor that names the policy by URI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaVerificationSummaryPolicy"]
    class_class_curie: ClassVar[str] = "slsa:SlsaVerificationSummaryPolicy"
    class_name: ClassVar[str] = "SlsaVerificationSummaryPolicy"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaVerificationSummaryPolicy

    resource_uri: Union[str, InTotoResourceUri] = None
    digest: Optional[Union[dict, InTotoDigestSet]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resource_uri):
            self.MissingRequiredField("resource_uri")
        if not isinstance(self.resource_uri, InTotoResourceUri):
            self.resource_uri = InTotoResourceUri(self.resource_uri)

        if self.digest is not None and not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaVerificationSummaryInputAttestation(InTotoResourceDescriptor):
    """
    One attestation a verifier consulted: a resource descriptor that carries the attestation's digest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaVerificationSummaryInputAttestation"]
    class_class_curie: ClassVar[str] = "slsa:SlsaVerificationSummaryInputAttestation"
    class_name: ClassVar[str] = "SlsaVerificationSummaryInputAttestation"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaVerificationSummaryInputAttestation

    digest: Union[dict, InTotoDigestSet] = None
    resource_uri: Optional[Union[str, InTotoResourceUri]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.digest):
            self.MissingRequiredField("digest")
        if not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        if self.resource_uri is not None and not isinstance(self.resource_uri, InTotoResourceUri):
            self.resource_uri = InTotoResourceUri(self.resource_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoStatementSubject(InTotoResourceDescriptor):
    """
    One artifact an in-toto statement is about: a resource descriptor that carries a digest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoStatementSubject"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoStatementSubject"
    class_name: ClassVar[str] = "InTotoStatementSubject"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoStatementSubject

    digest: Union[dict, InTotoDigestSet] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.digest):
            self.MissingRequiredField("digest")
        if not isinstance(self.digest, InTotoDigestSet):
            self.digest = InTotoDigestSet(**as_dict(self.digest))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoStatement(YAMLRoot):
    """
    The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the
    predicate itself.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoStatement"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoStatement"
    class_name: ClassVar[str] = "InTotoStatement"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoStatement

    statement_type: Union[str, InTotoTypeUri] = None
    subject: Union[Union[dict, InTotoStatementSubject], list[Union[dict, InTotoStatementSubject]]] = None
    predicate_type: Union[str, InTotoTypeUri] = None
    predicate: Optional[Union[dict, "InTotoPredicate"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement_type):
            self.MissingRequiredField("statement_type")
        if not isinstance(self.statement_type, InTotoTypeUri):
            self.statement_type = InTotoTypeUri(self.statement_type)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, InTotoStatementSubject) else InTotoStatementSubject(**as_dict(v)) for v in self.subject]

        if self._is_empty(self.predicate_type):
            self.MissingRequiredField("predicate_type")
        if not isinstance(self.predicate_type, InTotoTypeUri):
            self.predicate_type = InTotoTypeUri(self.predicate_type)

        if self.predicate is not None and not isinstance(self.predicate, InTotoPredicate):
            self.predicate = InTotoPredicate(**as_dict(self.predicate))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SlsaStatement(InTotoStatement):
    """
    An in-toto statement with the fields this schema adds: where the signed attestation is stored, the tool that
    signed it and the transparency log entry that records the signature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaStatement"]
    class_class_curie: ClassVar[str] = "slsa:SlsaStatement"
    class_name: ClassVar[str] = "SlsaStatement"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaStatement

    statement_type: Union[str, InTotoTypeUri] = None
    subject: Union[Union[dict, InTotoStatementSubject], list[Union[dict, InTotoStatementSubject]]] = None
    predicate_type: Union[str, InTotoTypeUri] = None
    attestation_storage_uri: Optional[Union[str, URI]] = None
    signing_tool: Optional[Union[str, URI]] = None
    transparency_log_entry: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.attestation_storage_uri is not None and not isinstance(self.attestation_storage_uri, URI):
            self.attestation_storage_uri = URI(self.attestation_storage_uri)

        if self.signing_tool is not None and not isinstance(self.signing_tool, URI):
            self.signing_tool = URI(self.signing_tool)

        if self.transparency_log_entry is not None and not isinstance(self.transparency_log_entry, URI):
            self.transparency_log_entry = URI(self.transparency_log_entry)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InTotoPredicate(YAMLRoot):
    """
    The base of every predicate an in-toto statement can carry; predicate_kind names the concrete kind.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IN_TOTO_LINKML["InTotoPredicate"]
    class_class_curie: ClassVar[str] = "in_toto_linkml:InTotoPredicate"
    class_name: ClassVar[str] = "InTotoPredicate"
    class_model_uri: ClassVar[URIRef] = SLSA.InTotoPredicate

    predicate_kind: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.predicate_kind = str(self.class_name)

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "predicate_kind"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



class SlsaPredicate(InTotoPredicate):
    """
    The base of every predicate this schema models; the predicate_kind it takes from InTotoPredicate names the
    concrete kind.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaPredicate"]
    class_class_curie: ClassVar[str] = "slsa:SlsaPredicate"
    class_name: ClassVar[str] = "SlsaPredicate"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaPredicate


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class SlsaBuildProvenance(SlsaPredicate):
    """
    The predicate that says how a build platform produced a set of artifacts, so that consumers can verify the build
    met their expectations and others can rebuild it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildProvenance"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildProvenance"
    class_name: ClassVar[str] = "SlsaBuildProvenance"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildProvenance

    build_definition: Union[dict, SlsaBuildDefinition] = None
    run_details: Union[dict, SlsaRunDetails] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.build_definition):
            self.MissingRequiredField("build_definition")
        if not isinstance(self.build_definition, SlsaBuildDefinition):
            self.build_definition = SlsaBuildDefinition(**as_dict(self.build_definition))

        if self._is_empty(self.run_details):
            self.MissingRequiredField("run_details")
        if not isinstance(self.run_details, SlsaRunDetails):
            self.run_details = SlsaRunDetails(**as_dict(self.run_details))

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class SlsaVerificationSummary(SlsaPredicate):
    """
    The predicate in which a verifier records that it evaluated artifacts against a policy and the SLSA levels they
    met, so consumers can rely on the verifier instead of reading every underlying attestation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaVerificationSummary"]
    class_class_curie: ClassVar[str] = "slsa:SlsaVerificationSummary"
    class_name: ClassVar[str] = "SlsaVerificationSummary"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaVerificationSummary

    resource_uri: Union[str, InTotoResourceUri] = None
    verifier: Union[dict, SlsaVerifier] = None
    policy: Union[dict, SlsaVerificationSummaryPolicy] = None
    verification_result: Union[str, "SlsaVerificationResult"] = None
    verified_levels: Union[Union[str, SlsaResultValue], list[Union[str, SlsaResultValue]]] = None
    time_verified: Optional[Union[str, XSDDateTime]] = None
    input_attestations: Optional[Union[Union[dict, SlsaVerificationSummaryInputAttestation], list[Union[dict, SlsaVerificationSummaryInputAttestation]]]] = empty_list()
    organization_properties: Optional[Union[str, list[str]]] = empty_list()
    dependency_levels: Optional[Union[Union[dict, SlsaDependencyLevelCount], list[Union[dict, SlsaDependencyLevelCount]]]] = empty_list()
    slsa_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resource_uri):
            self.MissingRequiredField("resource_uri")
        if not isinstance(self.resource_uri, InTotoResourceUri):
            self.resource_uri = InTotoResourceUri(self.resource_uri)

        if self._is_empty(self.verifier):
            self.MissingRequiredField("verifier")
        if not isinstance(self.verifier, SlsaVerifier):
            self.verifier = SlsaVerifier(**as_dict(self.verifier))

        if self._is_empty(self.policy):
            self.MissingRequiredField("policy")
        if not isinstance(self.policy, SlsaVerificationSummaryPolicy):
            self.policy = SlsaVerificationSummaryPolicy(**as_dict(self.policy))

        if self._is_empty(self.verification_result):
            self.MissingRequiredField("verification_result")
        if not isinstance(self.verification_result, SlsaVerificationResult):
            self.verification_result = SlsaVerificationResult(self.verification_result)

        if self._is_empty(self.verified_levels):
            self.MissingRequiredField("verified_levels")
        if not isinstance(self.verified_levels, list):
            self.verified_levels = [self.verified_levels] if self.verified_levels is not None else []
        self.verified_levels = [v if isinstance(v, SlsaResultValue) else SlsaResultValue(v) for v in self.verified_levels]

        if self.time_verified is not None and not isinstance(self.time_verified, XSDDateTime):
            self.time_verified = XSDDateTime(self.time_verified)

        if not isinstance(self.input_attestations, list):
            self.input_attestations = [self.input_attestations] if self.input_attestations is not None else []
        self.input_attestations = [v if isinstance(v, SlsaVerificationSummaryInputAttestation) else SlsaVerificationSummaryInputAttestation(**as_dict(v)) for v in self.input_attestations]

        if not isinstance(self.organization_properties, list):
            self.organization_properties = [self.organization_properties] if self.organization_properties is not None else []
        self.organization_properties = [v if isinstance(v, str) else str(v) for v in self.organization_properties]

        self._normalize_inlined_as_list(slot_name="dependency_levels", slot_type=SlsaDependencyLevelCount, key_name="verified_level", keyed=False)

        if self.slsa_version is not None and not isinstance(self.slsa_version, str):
            self.slsa_version = str(self.slsa_version)

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class SlsaSourceProvenance(SlsaPredicate):
    """
    Evidence from an SCS of how a revision came to exist and which technical controls were enforced when it did.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaSourceProvenance"]
    class_class_curie: ClassVar[str] = "slsa:SlsaSourceProvenance"
    class_name: ClassVar[str] = "SlsaSourceProvenance"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaSourceProvenance

    revision: Union[str, SlsaSourceRevisionRevisionId] = None
    controls_enforced: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.revision):
            self.MissingRequiredField("revision")
        if not isinstance(self.revision, SlsaSourceRevisionRevisionId):
            self.revision = SlsaSourceRevisionRevisionId(self.revision)

        if not isinstance(self.controls_enforced, list):
            self.controls_enforced = [self.controls_enforced] if self.controls_enforced is not None else []
        self.controls_enforced = [v if isinstance(v, str) else str(v) for v in self.controls_enforced]

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


@dataclass(repr=False)
class SlsaBuildEnvironmentAttestation(SlsaPredicate):
    """
    Evidence of the state of a build environment when a build was dispatched to it: the image it came from and the
    measurements taken at boot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SLSA["SlsaBuildEnvironmentAttestation"]
    class_class_curie: ClassVar[str] = "slsa:SlsaBuildEnvironmentAttestation"
    class_name: ClassVar[str] = "SlsaBuildEnvironmentAttestation"
    class_model_uri: ClassVar[URIRef] = SLSA.SlsaBuildEnvironmentAttestation

    build_id: str = None
    build_env_level: Optional[Union[str, "SlsaBuildEnvironmentLevel"]] = None
    build_image: Optional[Union[str, SlsaBuildImageImageUri]] = None
    measurements: Optional[Union[Union[dict, SlsaMeasurement], list[Union[dict, SlsaMeasurement]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.build_id):
            self.MissingRequiredField("build_id")
        if not isinstance(self.build_id, str):
            self.build_id = str(self.build_id)

        if self.build_env_level is not None and not isinstance(self.build_env_level, SlsaBuildEnvironmentLevel):
            self.build_env_level = SlsaBuildEnvironmentLevel(self.build_env_level)

        if self.build_image is not None and not isinstance(self.build_image, SlsaBuildImageImageUri):
            self.build_image = SlsaBuildImageImageUri(self.build_image)

        self._normalize_inlined_as_list(slot_name="measurements", slot_type=SlsaMeasurement, key_name="measured_component", keyed=False)

        super().__post_init__(**kwargs)
        self.unknown_predicate_kind = str(self.class_name)


# Enumerations
class SlsaBuildLevel(EnumDefinitionImpl):
    """
    The levels of the SLSA Build track, each adding protection against tampering with the build or its provenance.
    """
    SLSA_BUILD_LEVEL_0 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_0",
        description="No requirements; the absence of SLSA, as for development or test builds.")
    SLSA_BUILD_LEVEL_1 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_1",
        description="""Provenance exists and shows how the package was built; it prevents mistakes but is easy to forge.""")
    SLSA_BUILD_LEVEL_2 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_2",
        description="""A hosted platform generates and signs the provenance, so tampering after the build needs an explicit attack.""")
    SLSA_BUILD_LEVEL_3 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_3",
        description="""A hardened platform prevents runs from influencing one another and keeps signing material away from build steps, so forging provenance needs an exploit.""")

    _defn = EnumDefinition(
        name="SlsaBuildLevel",
        description="""The levels of the SLSA Build track, each adding protection against tampering with the build or its provenance.""",
    )

class SlsaVerificationResult(EnumDefinitionImpl):
    """
    The outcome of verifying an artifact against a policy.
    """
    PASSED = PermissibleValue(
        text="PASSED",
        description="The artifact met the policy.")
    FAILED = PermissibleValue(
        text="FAILED",
        description="The artifact did not meet the policy.")

    _defn = EnumDefinition(
        name="SlsaVerificationResult",
        description="The outcome of verifying an artifact against a policy.",
    )

class SlsaResult(EnumDefinitionImpl):
    """
    A result of evaluating an artifact against SLSA: a track level, a verified property, or a failure. A level implies
    the levels below it in the same track.
    """
    SLSA_BUILD_LEVEL_UNEVALUATED = PermissibleValue(
        text="SLSA_BUILD_LEVEL_UNEVALUATED",
        description="The issuer makes no claim about the Build track level.")
    SLSA_BUILD_LEVEL_0 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_0",
        description="No Build track guarantees were verified.")
    SLSA_BUILD_LEVEL_1 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_1",
        description="Build level 1 was verified.")
    SLSA_BUILD_LEVEL_2 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_2",
        description="Build level 2 was verified.")
    SLSA_BUILD_LEVEL_3 = PermissibleValue(
        text="SLSA_BUILD_LEVEL_3",
        description="Build level 3 was verified.")
    SLSA_SOURCE_LEVEL_UNEVALUATED = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_UNEVALUATED",
        description="The issuer makes no claim about the Source track level.")
    SLSA_SOURCE_LEVEL_0 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_0",
        description="No Source track guarantees were verified.")
    SLSA_SOURCE_LEVEL_1 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_1",
        description="Source level 1 was verified.")
    SLSA_SOURCE_LEVEL_2 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_2",
        description="Source level 2 was verified.")
    SLSA_SOURCE_LEVEL_3 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_3",
        description="Source level 3 was verified.")
    SLSA_SOURCE_LEVEL_4 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_4",
        description="Source level 4 was verified.")
    SLSA_SOURCE_TWO_PARTY_REVIEWED = PermissibleValue(
        text="SLSA_SOURCE_TWO_PARTY_REVIEWED",
        description="The verified property that two trusted persons reviewed the source, at whatever source level.")
    SLSA_BUILD_REPRODUCED = PermissibleValue(
        text="SLSA_BUILD_REPRODUCED",
        description="The verified property that two or more independent build platforms reproduced the artifact.")
    FAILED = PermissibleValue(
        text="FAILED",
        description="Policy evaluation failed.")

    _defn = EnumDefinition(
        name="SlsaResult",
        description="""A result of evaluating an artifact against SLSA: a track level, a verified property, or a failure. A level implies the levels below it in the same track.""",
    )

class SlsaSourceLevel(EnumDefinitionImpl):
    """
    The levels of the SLSA Source track, each adding trust in how a revision was created.
    """
    SLSA_SOURCE_LEVEL_0 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_0",
        description="""No Source track guarantees; a revision for which the SCS issues no Source VSA is at this level.""")
    SLSA_SOURCE_LEVEL_1 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_1",
        description="The source is managed in a version control system, so it has discrete, immutable revisions.")
    SLSA_SOURCE_LEVEL_2 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_2",
        description="""Branch history is continuous and retained, and the SCS issues source provenance for each new revision.""")
    SLSA_SOURCE_LEVEL_3 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_3",
        description="""The SCS enforces the organization's technical controls on protected named references and provides evidence of them.""")
    SLSA_SOURCE_LEVEL_4 = PermissibleValue(
        text="SLSA_SOURCE_LEVEL_4",
        description="Two trusted persons agree to every change on protected branches.")

    _defn = EnumDefinition(
        name="SlsaSourceLevel",
        description="The levels of the SLSA Source track, each adding trust in how a revision was created.",
    )

class SlsaReviewType(EnumDefinitionImpl):
    """
    The forms of review that may approve a revision, including the contested forms the adoption study records.
    """
    TWO_PARTY = PermissibleValue(
        text="TWO_PARTY",
        description="A reviewer distinct from the author approved the change, both being trusted persons.")
    PAIR_PROGRAMMING = PermissibleValue(
        text="PAIR_PROGRAMMING",
        description="""Two developers wrote the change together at one workstation or screen; whether this counts as two-party review is open.""")
    MOB_PROGRAMMING = PermissibleValue(
        text="MOB_PROGRAMMING",
        description="A group wrote the change together; whether this counts as two-party review is open.")
    AUTOMATED = PermissibleValue(
        text="AUTOMATED",
        description="A tool or bot reviewed the change with no second person, which is not two-party review.")

    _defn = EnumDefinition(
        name="SlsaReviewType",
        description="""The forms of review that may approve a revision, including the contested forms the adoption study records.""",
    )

class SlsaDependencyLevel(EnumDefinitionImpl):
    """
    The levels of the SLSA Dependency track, each reducing the risk third-party dependencies bring.
    """
    SLSA_DEPENDENCY_LEVEL_0 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_0",
        description="No Dependency track claims.")
    SLSA_DEPENDENCY_LEVEL_1 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_1",
        description="An inventory of all build dependencies, direct and transitive, exists.")
    SLSA_DEPENDENCY_LEVEL_2 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_2",
        description="Every known vulnerability in the dependencies was triaged before release.")
    SLSA_DEPENDENCY_LEVEL_3 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_3",
        description="Every third-party build dependency is consumed from a location the producer controls.")
    SLSA_DEPENDENCY_LEVEL_4 = PermissibleValue(
        text="SLSA_DEPENDENCY_LEVEL_4",
        description="An ingestion policy keeps compromised upstream dependencies out of the build.")

    _defn = EnumDefinition(
        name="SlsaDependencyLevel",
        description="The levels of the SLSA Dependency track, each reducing the risk third-party dependencies bring.",
    )

class SlsaBuildEnvironmentLevel(EnumDefinitionImpl):
    """
    The levels of the SLSA Build Environment track, each extending integrity further into the compute that runs builds.
    """
    SLSA_BUILD_ENV_LEVEL_0 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_0",
        description="No Build Environment track claims.")
    SLSA_BUILD_ENV_LEVEL_1 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_1",
        description="""The build image has signed build provenance, protecting against tampering while the image is distributed.""")
    SLSA_BUILD_ENV_LEVEL_2 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_2",
        description="""The compute platform attests to the environment's state at boot, protecting against tampering through the control plane.""")
    SLSA_BUILD_ENV_LEVEL_3 = PermissibleValue(
        text="SLSA_BUILD_ENV_LEVEL_3",
        description="""Trusted hardware attests to the host's state, protecting against tampering through the host interface.""")

    _defn = EnumDefinition(
        name="SlsaBuildEnvironmentLevel",
        description="""The levels of the SLSA Build Environment track, each extending integrity further into the compute that runs builds.""",
    )

class SlsaAdoptionChallenge(EnumDefinitionImpl):
    """
    The four themes of difficulty practitioners met when adopting SLSA.
    """
    COMPLEX_IMPLEMENTATION = PermissibleValue(
        text="COMPLEX_IMPLEMENTATION",
        description="Generating provenance and maintaining the required tools is complicated.")
    UNCLEAR_COMMUNICATION = PermissibleValue(
        text="UNCLEAR_COMMUNICATION",
        description="SLSA's terms and its guidance for particular ecosystems are hard to understand.")
    LIMITED_FEASIBILITY = PermissibleValue(
        text="LIMITED_FEASIBILITY",
        description="Verification tooling, attestation storage and two-party review are hard to put into practice.")
    UNCLEAR_RELEVANCE = PermissibleValue(
        text="UNCLEAR_RELEVANCE",
        description="Which attacks SLSA mitigates, and how it differs from other practices, is unclear.")

    _defn = EnumDefinition(
        name="SlsaAdoptionChallenge",
        description="The four themes of difficulty practitioners met when adopting SLSA.",
    )

class SlsaAdoptionStrategy(EnumDefinitionImpl):
    """
    The five themes of strategy practitioners proposed for the adoption challenges.
    """
    ENHANCE_ALIGNMENT_FLEXIBILITY = PermissibleValue(
        text="ENHANCE_ALIGNMENT_FLEXIBILITY",
        description="""Make SLSA fit more contexts, with build-system tracks, gamified levels, flexibility for varied organizations and alignment with OpenSSF practices.""")
    PROVIDE_DETAILED_DOCUMENTATION = PermissibleValue(
        text="PROVIDE_DETAILED_DOCUMENTATION",
        description="Give clearer definitions, standard terms, negative examples and better navigation.")
    STREAMLINE_PROVENANCE_GENERATION = PermissibleValue(
        text="STREAMLINE_PROVENANCE_GENERATION",
        description="""Simplify and standardize provenance generation with tools and templates, and fix release-tool inconsistencies.""")
    IMPROVE_VERIFICATION_PROCESS = PermissibleValue(
        text="IMPROVE_VERIFICATION_PROCESS",
        description="""Strengthen verification and level determination, tag versions early, and give downstream users more signals.""")
    COLLABORATE_WITH_COMMUNITY = PermissibleValue(
        text="COLLABORATE_WITH_COMMUNITY",
        description="Align with industry standards, guide newcomers, and share knowledge across projects.")

    _defn = EnumDefinition(
        name="SlsaAdoptionStrategy",
        description="The five themes of strategy practitioners proposed for the adoption challenges.",
    )

# Slots
class slots:
    pass

slots.component_versions = Slot(uri=SLSA.component_versions, name="component_versions", curie=SLSA.curie('component_versions'),
                   model_uri=SLSA.component_versions, domain=None, range=Optional[Union[Union[dict, SlsaComponentVersion], list[Union[dict, SlsaComponentVersion]]]])

slots.ecosystem = Slot(uri=SLSA.ecosystem, name="ecosystem", curie=SLSA.curie('ecosystem'),
                   model_uri=SLSA.ecosystem, domain=None, range=Optional[str])

slots.build_platform = Slot(uri=SLSA.build_platform, name="build_platform", curie=SLSA.curie('build_platform'),
                   model_uri=SLSA.build_platform, domain=None, range=Optional[Union[str, SlsaBuildPlatformBuilderId]])

slots.repository = Slot(uri=SLSA.repository, name="repository", curie=SLSA.curie('repository'),
                   model_uri=SLSA.repository, domain=None, range=Optional[Union[str, SlsaSourceRepositoryRepositoryUri]])

slots.revision = Slot(uri=SLSA.revision, name="revision", curie=SLSA.curie('revision'),
                   model_uri=SLSA.revision, domain=None, range=Optional[Union[str, SlsaSourceRevisionRevisionId]])

slots.build_env_level = Slot(uri=SLSA.build_env_level, name="build_env_level", curie=SLSA.curie('build_env_level'),
                   model_uri=SLSA.build_env_level, domain=None, range=Optional[Union[str, "SlsaBuildEnvironmentLevel"]])

slots.resource_uri = Slot(uri=IN_TOTO_LINKML.resource_uri, name="resource_uri", curie=IN_TOTO_LINKML.curie('resource_uri'),
                   model_uri=SLSA.resource_uri, domain=None, range=Optional[Union[str, InTotoResourceUri]])

slots.digest = Slot(uri=IN_TOTO_LINKML.digest, name="digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=SLSA.digest, domain=None, range=Optional[Union[dict, InTotoDigestSet]])

slots.predicate = Slot(uri=IN_TOTO_LINKML.predicate, name="predicate", curie=IN_TOTO_LINKML.curie('predicate'),
                   model_uri=SLSA.predicate, domain=None, range=Optional[Union[dict, InTotoPredicate]])

slots.slsaDocument__attestations = Slot(uri=SLSA.attestations, name="slsaDocument__attestations", curie=SLSA.curie('attestations'),
                   model_uri=SLSA.slsaDocument__attestations, domain=None, range=Optional[Union[Union[dict, SlsaStatement], list[Union[dict, SlsaStatement]]]])

slots.slsaDocument__parties = Slot(uri=SLSA.parties, name="slsaDocument__parties", curie=SLSA.curie('parties'),
                   model_uri=SLSA.slsaDocument__parties, domain=None, range=Optional[Union[Union[dict, SlsaParty], list[Union[dict, SlsaParty]]]])

slots.slsaDocument__build_platforms = Slot(uri=SLSA.build_platforms, name="slsaDocument__build_platforms", curie=SLSA.curie('build_platforms'),
                   model_uri=SLSA.slsaDocument__build_platforms, domain=None, range=Optional[Union[dict[Union[str, SlsaBuildPlatformBuilderId], Union[dict, SlsaBuildPlatform]], list[Union[dict, SlsaBuildPlatform]]]])

slots.slsaDocument__control_planes = Slot(uri=SLSA.control_planes, name="slsaDocument__control_planes", curie=SLSA.curie('control_planes'),
                   model_uri=SLSA.slsaDocument__control_planes, domain=None, range=Optional[Union[Union[dict, SlsaControlPlane], list[Union[dict, SlsaControlPlane]]]])

slots.slsaDocument__packages = Slot(uri=SLSA.packages, name="slsaDocument__packages", curie=SLSA.curie('packages'),
                   model_uri=SLSA.slsaDocument__packages, domain=None, range=Optional[Union[Union[dict, SlsaPackage], list[Union[dict, SlsaPackage]]]])

slots.slsaDocument__package_registries = Slot(uri=SLSA.package_registries, name="slsaDocument__package_registries", curie=SLSA.curie('package_registries'),
                   model_uri=SLSA.slsaDocument__package_registries, domain=None, range=Optional[Union[dict[Union[str, SlsaPackageRegistryRegistryUri], Union[dict, SlsaPackageRegistry]], list[Union[dict, SlsaPackageRegistry]]]])

slots.slsaDocument__source_control_systems = Slot(uri=SLSA.source_control_systems, name="slsaDocument__source_control_systems", curie=SLSA.curie('source_control_systems'),
                   model_uri=SLSA.slsaDocument__source_control_systems, domain=None, range=Optional[Union[list[Union[str, SlsaSourceControlSystemScsUri]], dict[Union[str, SlsaSourceControlSystemScsUri], Union[dict, SlsaSourceControlSystem]]]])

slots.slsaDocument__source_repositories = Slot(uri=SLSA.source_repositories, name="slsaDocument__source_repositories", curie=SLSA.curie('source_repositories'),
                   model_uri=SLSA.slsaDocument__source_repositories, domain=None, range=Optional[Union[dict[Union[str, SlsaSourceRepositoryRepositoryUri], Union[dict, SlsaSourceRepository]], list[Union[dict, SlsaSourceRepository]]]])

slots.slsaDocument__source_revisions = Slot(uri=SLSA.source_revisions, name="slsaDocument__source_revisions", curie=SLSA.curie('source_revisions'),
                   model_uri=SLSA.slsaDocument__source_revisions, domain=None, range=Optional[Union[dict[Union[str, SlsaSourceRevisionRevisionId], Union[dict, SlsaSourceRevision]], list[Union[dict, SlsaSourceRevision]]]])

slots.slsaDocument__named_references = Slot(uri=SLSA.named_references, name="slsaDocument__named_references", curie=SLSA.curie('named_references'),
                   model_uri=SLSA.slsaDocument__named_references, domain=None, range=Optional[Union[Union[dict, SlsaNamedReference], list[Union[dict, SlsaNamedReference]]]])

slots.slsaDocument__build_images = Slot(uri=SLSA.build_images, name="slsaDocument__build_images", curie=SLSA.curie('build_images'),
                   model_uri=SLSA.slsaDocument__build_images, domain=None, range=Optional[Union[dict[Union[str, SlsaBuildImageImageUri], Union[dict, SlsaBuildImage]], list[Union[dict, SlsaBuildImage]]]])

slots.slsaDocument__dependency_inventories = Slot(uri=SLSA.dependency_inventories, name="slsaDocument__dependency_inventories", curie=SLSA.curie('dependency_inventories'),
                   model_uri=SLSA.slsaDocument__dependency_inventories, domain=None, range=Optional[Union[Union[dict, SlsaDependencyInventory], list[Union[dict, SlsaDependencyInventory]]]])

slots.slsaDocument__adoption_metadata = Slot(uri=SLSA.adoption_metadata, name="slsaDocument__adoption_metadata", curie=SLSA.curie('adoption_metadata'),
                   model_uri=SLSA.slsaDocument__adoption_metadata, domain=None, range=Optional[Union[dict, SlsaAdoptionMetadata]])

slots.slsaStatement__attestation_storage_uri = Slot(uri=SLSA.attestation_storage_uri, name="slsaStatement__attestation_storage_uri", curie=SLSA.curie('attestation_storage_uri'),
                   model_uri=SLSA.slsaStatement__attestation_storage_uri, domain=None, range=Optional[Union[str, URI]])

slots.slsaStatement__signing_tool = Slot(uri=SLSA.signing_tool, name="slsaStatement__signing_tool", curie=SLSA.curie('signing_tool'),
                   model_uri=SLSA.slsaStatement__signing_tool, domain=None, range=Optional[Union[str, URI]])

slots.slsaStatement__transparency_log_entry = Slot(uri=SLSA.transparency_log_entry, name="slsaStatement__transparency_log_entry", curie=SLSA.curie('transparency_log_entry'),
                   model_uri=SLSA.slsaStatement__transparency_log_entry, domain=None, range=Optional[Union[str, URI]])

slots.slsaParty__party_type = Slot(uri=SLSA.party_type, name="slsaParty__party_type", curie=SLSA.curie('party_type'),
                   model_uri=SLSA.slsaParty__party_type, domain=None, range=Optional[str])

slots.slsaParty__party_name = Slot(uri=SLSA.party_name, name="slsaParty__party_name", curie=SLSA.curie('party_name'),
                   model_uri=SLSA.slsaParty__party_name, domain=None, range=Optional[str])

slots.slsaVerifier__verifier_id = Slot(uri=SLSA.verifier_id, name="slsaVerifier__verifier_id", curie=SLSA.curie('verifier_id'),
                   model_uri=SLSA.slsaVerifier__verifier_id, domain=None, range=Union[str, URI])

slots.slsaBuildPlatform__builder_id = Slot(uri=SLSA.builder_id, name="slsaBuildPlatform__builder_id", curie=SLSA.curie('builder_id'),
                   model_uri=SLSA.slsaBuildPlatform__builder_id, domain=None, range=URIRef)

slots.slsaBuildPlatform__build_level = Slot(uri=SLSA.build_level, name="slsaBuildPlatform__build_level", curie=SLSA.curie('build_level'),
                   model_uri=SLSA.slsaBuildPlatform__build_level, domain=None, range=Optional[Union[str, "SlsaBuildLevel"]])

slots.slsaBuildPlatform__hosted = Slot(uri=SLSA.hosted, name="slsaBuildPlatform__hosted", curie=SLSA.curie('hosted'),
                   model_uri=SLSA.slsaBuildPlatform__hosted, domain=None, range=Optional[Union[bool, Bool]])

slots.slsaBuildPlatform__builder_dependencies = Slot(uri=SLSA.builder_dependencies, name="slsaBuildPlatform__builder_dependencies", curie=SLSA.curie('builder_dependencies'),
                   model_uri=SLSA.slsaBuildPlatform__builder_dependencies, domain=None, range=Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]])

slots.slsaComponentVersion__component = Slot(uri=SLSA.component, name="slsaComponentVersion__component", curie=SLSA.curie('component'),
                   model_uri=SLSA.slsaComponentVersion__component, domain=None, range=str)

slots.slsaComponentVersion__component_version = Slot(uri=SLSA.component_version, name="slsaComponentVersion__component_version", curie=SLSA.curie('component_version'),
                   model_uri=SLSA.slsaComponentVersion__component_version, domain=None, range=Optional[str])

slots.slsaPackageRegistry__registry_uri = Slot(uri=SLSA.registry_uri, name="slsaPackageRegistry__registry_uri", curie=SLSA.curie('registry_uri'),
                   model_uri=SLSA.slsaPackageRegistry__registry_uri, domain=None, range=URIRef)

slots.slsaPackage__package_name = Slot(uri=SLSA.package_name, name="slsaPackage__package_name", curie=SLSA.curie('package_name'),
                   model_uri=SLSA.slsaPackage__package_name, domain=None, range=str)

slots.slsaPackage__registry = Slot(uri=SLSA.registry, name="slsaPackage__registry", curie=SLSA.curie('registry'),
                   model_uri=SLSA.slsaPackage__registry, domain=None, range=Optional[Union[str, SlsaPackageRegistryRegistryUri]])

slots.slsaPackage__package_artifacts = Slot(uri=SLSA.package_artifacts, name="slsaPackage__package_artifacts", curie=SLSA.curie('package_artifacts'),
                   model_uri=SLSA.slsaPackage__package_artifacts, domain=None, range=Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]])

slots.slsaPackage__guac_uri = Slot(uri=SLSA.guac_uri, name="slsaPackage__guac_uri", curie=SLSA.curie('guac_uri'),
                   model_uri=SLSA.slsaPackage__guac_uri, domain=None, range=Optional[Union[str, URI]])

slots.slsaPackage__security_insights_uri = Slot(uri=SLSA.security_insights_uri, name="slsaPackage__security_insights_uri", curie=SLSA.curie('security_insights_uri'),
                   model_uri=SLSA.slsaPackage__security_insights_uri, domain=None, range=Optional[Union[str, URI]])

slots.slsaBuildProvenance__build_definition = Slot(uri=SLSA.build_definition, name="slsaBuildProvenance__build_definition", curie=SLSA.curie('build_definition'),
                   model_uri=SLSA.slsaBuildProvenance__build_definition, domain=None, range=Union[dict, SlsaBuildDefinition])

slots.slsaBuildProvenance__run_details = Slot(uri=SLSA.run_details, name="slsaBuildProvenance__run_details", curie=SLSA.curie('run_details'),
                   model_uri=SLSA.slsaBuildProvenance__run_details, domain=None, range=Union[dict, SlsaRunDetails])

slots.slsaBuildDefinition__build_type = Slot(uri=SLSA.build_type, name="slsaBuildDefinition__build_type", curie=SLSA.curie('build_type'),
                   model_uri=SLSA.slsaBuildDefinition__build_type, domain=None, range=Union[str, URI])

slots.slsaBuildDefinition__external_parameters = Slot(uri=SLSA.external_parameters, name="slsaBuildDefinition__external_parameters", curie=SLSA.curie('external_parameters'),
                   model_uri=SLSA.slsaBuildDefinition__external_parameters, domain=None, range=Union[Union[dict, SlsaBuildParameter], list[Union[dict, SlsaBuildParameter]]])

slots.slsaBuildDefinition__internal_parameters = Slot(uri=SLSA.internal_parameters, name="slsaBuildDefinition__internal_parameters", curie=SLSA.curie('internal_parameters'),
                   model_uri=SLSA.slsaBuildDefinition__internal_parameters, domain=None, range=Optional[Union[Union[dict, SlsaBuildParameter], list[Union[dict, SlsaBuildParameter]]]])

slots.slsaBuildDefinition__resolved_dependencies = Slot(uri=SLSA.resolved_dependencies, name="slsaBuildDefinition__resolved_dependencies", curie=SLSA.curie('resolved_dependencies'),
                   model_uri=SLSA.slsaBuildDefinition__resolved_dependencies, domain=None, range=Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]])

slots.slsaBuildDefinition__hermetic = Slot(uri=SLSA.hermetic, name="slsaBuildDefinition__hermetic", curie=SLSA.curie('hermetic'),
                   model_uri=SLSA.slsaBuildDefinition__hermetic, domain=None, range=Optional[Union[bool, Bool]])

slots.slsaBuildDefinition__provenance_generation_tool = Slot(uri=SLSA.provenance_generation_tool, name="slsaBuildDefinition__provenance_generation_tool", curie=SLSA.curie('provenance_generation_tool'),
                   model_uri=SLSA.slsaBuildDefinition__provenance_generation_tool, domain=None, range=Optional[Union[str, URI]])

slots.slsaBuildDefinition__pipeline_orchestrator = Slot(uri=SLSA.pipeline_orchestrator, name="slsaBuildDefinition__pipeline_orchestrator", curie=SLSA.curie('pipeline_orchestrator'),
                   model_uri=SLSA.slsaBuildDefinition__pipeline_orchestrator, domain=None, range=Optional[Union[str, URI]])

slots.slsaBuildParameter__parameter_name = Slot(uri=SLSA.parameter_name, name="slsaBuildParameter__parameter_name", curie=SLSA.curie('parameter_name'),
                   model_uri=SLSA.slsaBuildParameter__parameter_name, domain=None, range=str)

slots.slsaBuildParameter__parameter_value = Slot(uri=SLSA.parameter_value, name="slsaBuildParameter__parameter_value", curie=SLSA.curie('parameter_value'),
                   model_uri=SLSA.slsaBuildParameter__parameter_value, domain=None, range=Optional[str])

slots.slsaRunDetails__builder = Slot(uri=SLSA.builder, name="slsaRunDetails__builder", curie=SLSA.curie('builder'),
                   model_uri=SLSA.slsaRunDetails__builder, domain=None, range=Union[dict, SlsaBuildPlatform])

slots.slsaRunDetails__build_metadata = Slot(uri=SLSA.build_metadata, name="slsaRunDetails__build_metadata", curie=SLSA.curie('build_metadata'),
                   model_uri=SLSA.slsaRunDetails__build_metadata, domain=None, range=Optional[Union[dict, SlsaBuildMetadata]])

slots.slsaRunDetails__byproducts = Slot(uri=SLSA.byproducts, name="slsaRunDetails__byproducts", curie=SLSA.curie('byproducts'),
                   model_uri=SLSA.slsaRunDetails__byproducts, domain=None, range=Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]])

slots.slsaBuildMetadata__invocation_id = Slot(uri=SLSA.invocation_id, name="slsaBuildMetadata__invocation_id", curie=SLSA.curie('invocation_id'),
                   model_uri=SLSA.slsaBuildMetadata__invocation_id, domain=None, range=Optional[str])

slots.slsaBuildMetadata__started_on = Slot(uri=SLSA.started_on, name="slsaBuildMetadata__started_on", curie=SLSA.curie('started_on'),
                   model_uri=SLSA.slsaBuildMetadata__started_on, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slsaBuildMetadata__finished_on = Slot(uri=SLSA.finished_on, name="slsaBuildMetadata__finished_on", curie=SLSA.curie('finished_on'),
                   model_uri=SLSA.slsaBuildMetadata__finished_on, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slsaVerificationSummary__verifier = Slot(uri=SLSA.verifier, name="slsaVerificationSummary__verifier", curie=SLSA.curie('verifier'),
                   model_uri=SLSA.slsaVerificationSummary__verifier, domain=None, range=Union[dict, SlsaVerifier])

slots.slsaVerificationSummary__time_verified = Slot(uri=SLSA.time_verified, name="slsaVerificationSummary__time_verified", curie=SLSA.curie('time_verified'),
                   model_uri=SLSA.slsaVerificationSummary__time_verified, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slsaVerificationSummary__policy = Slot(uri=SLSA.policy, name="slsaVerificationSummary__policy", curie=SLSA.curie('policy'),
                   model_uri=SLSA.slsaVerificationSummary__policy, domain=None, range=Union[dict, SlsaVerificationSummaryPolicy])

slots.slsaVerificationSummary__input_attestations = Slot(uri=SLSA.input_attestations, name="slsaVerificationSummary__input_attestations", curie=SLSA.curie('input_attestations'),
                   model_uri=SLSA.slsaVerificationSummary__input_attestations, domain=None, range=Optional[Union[Union[dict, SlsaVerificationSummaryInputAttestation], list[Union[dict, SlsaVerificationSummaryInputAttestation]]]])

slots.slsaVerificationSummary__verification_result = Slot(uri=SLSA.verification_result, name="slsaVerificationSummary__verification_result", curie=SLSA.curie('verification_result'),
                   model_uri=SLSA.slsaVerificationSummary__verification_result, domain=None, range=Union[str, "SlsaVerificationResult"])

slots.slsaVerificationSummary__verified_levels = Slot(uri=SLSA.verified_levels, name="slsaVerificationSummary__verified_levels", curie=SLSA.curie('verified_levels'),
                   model_uri=SLSA.slsaVerificationSummary__verified_levels, domain=None, range=Union[Union[str, SlsaResultValue], list[Union[str, SlsaResultValue]]],
                   pattern=re.compile(r'^(SLSA_BUILD_LEVEL_(UNEVALUATED|[0-3])|SLSA_SOURCE_LEVEL_(UNEVALUATED|[0-4])|SLSA_SOURCE_TWO_PARTY_REVIEWED|SLSA_BUILD_REPRODUCED|([!-RT-rt-~]|[Ss]$|[Ss][!-KM-km-~]|[Ss][Ll]$|[Ss][Ll][!-RT-rt-~]|[Ss][Ll][Ss]$|[Ss][Ll][Ss][!-@B-`b-~]|[Ss][Ll][Ss][Aa]$|[Ss][Ll][Ss][Aa][!-^`-~])[!-~]*)$'))

slots.slsaVerificationSummary__organization_properties = Slot(uri=SLSA.organization_properties, name="slsaVerificationSummary__organization_properties", curie=SLSA.curie('organization_properties'),
                   model_uri=SLSA.slsaVerificationSummary__organization_properties, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^ORG_SOURCE_'))

slots.slsaVerificationSummary__dependency_levels = Slot(uri=SLSA.dependency_levels, name="slsaVerificationSummary__dependency_levels", curie=SLSA.curie('dependency_levels'),
                   model_uri=SLSA.slsaVerificationSummary__dependency_levels, domain=None, range=Optional[Union[Union[dict, SlsaDependencyLevelCount], list[Union[dict, SlsaDependencyLevelCount]]]])

slots.slsaVerificationSummary__slsa_version = Slot(uri=SLSA.slsa_version, name="slsaVerificationSummary__slsa_version", curie=SLSA.curie('slsa_version'),
                   model_uri=SLSA.slsaVerificationSummary__slsa_version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9]+\.[0-9]+$'))

slots.slsaDependencyLevelCount__verified_level = Slot(uri=SLSA.verified_level, name="slsaDependencyLevelCount__verified_level", curie=SLSA.curie('verified_level'),
                   model_uri=SLSA.slsaDependencyLevelCount__verified_level, domain=None, range=Union[str, SlsaResultValue],
                   pattern=re.compile(r'^(SLSA_BUILD_LEVEL_(UNEVALUATED|[0-3])|SLSA_SOURCE_LEVEL_(UNEVALUATED|[0-4])|SLSA_SOURCE_TWO_PARTY_REVIEWED|SLSA_BUILD_REPRODUCED|([!-RT-rt-~]|[Ss]$|[Ss][!-KM-km-~]|[Ss][Ll]$|[Ss][Ll][!-RT-rt-~]|[Ss][Ll][Ss]$|[Ss][Ll][Ss][!-@B-`b-~]|[Ss][Ll][Ss][Aa]$|[Ss][Ll][Ss][Aa][!-^`-~])[!-~]*)$'))

slots.slsaDependencyLevelCount__dependency_count = Slot(uri=SLSA.dependency_count, name="slsaDependencyLevelCount__dependency_count", curie=SLSA.curie('dependency_count'),
                   model_uri=SLSA.slsaDependencyLevelCount__dependency_count, domain=None, range=int)

slots.slsaSourceControlSystem__scs_uri = Slot(uri=SLSA.scs_uri, name="slsaSourceControlSystem__scs_uri", curie=SLSA.curie('scs_uri'),
                   model_uri=SLSA.slsaSourceControlSystem__scs_uri, domain=None, range=URIRef)

slots.slsaSourceRepository__repository_uri = Slot(uri=SLSA.repository_uri, name="slsaSourceRepository__repository_uri", curie=SLSA.curie('repository_uri'),
                   model_uri=SLSA.slsaSourceRepository__repository_uri, domain=None, range=URIRef)

slots.slsaSourceRepository__hosted_by = Slot(uri=SLSA.hosted_by, name="slsaSourceRepository__hosted_by", curie=SLSA.curie('hosted_by'),
                   model_uri=SLSA.slsaSourceRepository__hosted_by, domain=None, range=Optional[Union[str, SlsaSourceControlSystemScsUri]])

slots.slsaSourceRevision__revision_id = Slot(uri=SLSA.revision_id, name="slsaSourceRevision__revision_id", curie=SLSA.curie('revision_id'),
                   model_uri=SLSA.slsaSourceRevision__revision_id, domain=None, range=URIRef)

slots.slsaSourceRevision__authored_by = Slot(uri=SLSA.authored_by, name="slsaSourceRevision__authored_by", curie=SLSA.curie('authored_by'),
                   model_uri=SLSA.slsaSourceRevision__authored_by, domain=None, range=Optional[str])

slots.slsaSourceRevision__authored_at = Slot(uri=SLSA.authored_at, name="slsaSourceRevision__authored_at", curie=SLSA.curie('authored_at'),
                   model_uri=SLSA.slsaSourceRevision__authored_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slsaSourceRevision__parent_revisions = Slot(uri=SLSA.parent_revisions, name="slsaSourceRevision__parent_revisions", curie=SLSA.curie('parent_revisions'),
                   model_uri=SLSA.slsaSourceRevision__parent_revisions, domain=None, range=Optional[Union[Union[str, SlsaSourceRevisionRevisionId], list[Union[str, SlsaSourceRevisionRevisionId]]]])

slots.slsaSourceRevision__source_level = Slot(uri=SLSA.source_level, name="slsaSourceRevision__source_level", curie=SLSA.curie('source_level'),
                   model_uri=SLSA.slsaSourceRevision__source_level, domain=None, range=Optional[Union[str, "SlsaSourceLevel"]])

slots.slsaSourceRevision__review_type = Slot(uri=SLSA.review_type, name="slsaSourceRevision__review_type", curie=SLSA.curie('review_type'),
                   model_uri=SLSA.slsaSourceRevision__review_type, domain=None, range=Optional[Union[str, "SlsaReviewType"]])

slots.slsaNamedReference__reference_type = Slot(uri=SLSA.reference_type, name="slsaNamedReference__reference_type", curie=SLSA.curie('reference_type'),
                   model_uri=SLSA.slsaNamedReference__reference_type, domain=None, range=Optional[str])

slots.slsaNamedReference__reference_name = Slot(uri=SLSA.reference_name, name="slsaNamedReference__reference_name", curie=SLSA.curie('reference_name'),
                   model_uri=SLSA.slsaNamedReference__reference_name, domain=None, range=str)

slots.slsaNamedReference__protected = Slot(uri=SLSA.protected, name="slsaNamedReference__protected", curie=SLSA.curie('protected'),
                   model_uri=SLSA.slsaNamedReference__protected, domain=None, range=Optional[Union[bool, Bool]])

slots.slsaSourceProvenance__controls_enforced = Slot(uri=SLSA.controls_enforced, name="slsaSourceProvenance__controls_enforced", curie=SLSA.curie('controls_enforced'),
                   model_uri=SLSA.slsaSourceProvenance__controls_enforced, domain=None, range=Optional[Union[str, list[str]]])

slots.slsaDependencyInventory__artifact = Slot(uri=SLSA.artifact, name="slsaDependencyInventory__artifact", curie=SLSA.curie('artifact'),
                   model_uri=SLSA.slsaDependencyInventory__artifact, domain=None, range=Union[dict, InTotoResourceDescriptor])

slots.slsaDependencyInventory__dependencies = Slot(uri=SLSA.dependencies, name="slsaDependencyInventory__dependencies", curie=SLSA.curie('dependencies'),
                   model_uri=SLSA.slsaDependencyInventory__dependencies, domain=None, range=Optional[Union[Union[dict, InTotoResourceDescriptor], list[Union[dict, InTotoResourceDescriptor]]]])

slots.slsaDependencyInventory__dependency_level = Slot(uri=SLSA.dependency_level, name="slsaDependencyInventory__dependency_level", curie=SLSA.curie('dependency_level'),
                   model_uri=SLSA.slsaDependencyInventory__dependency_level, domain=None, range=Optional[Union[str, "SlsaDependencyLevel"]])

slots.slsaBuildImage__image_uri = Slot(uri=SLSA.image_uri, name="slsaBuildImage__image_uri", curie=SLSA.curie('image_uri'),
                   model_uri=SLSA.slsaBuildImage__image_uri, domain=None, range=URIRef)

slots.slsaBuildImage__provenance = Slot(uri=SLSA.provenance, name="slsaBuildImage__provenance", curie=SLSA.curie('provenance'),
                   model_uri=SLSA.slsaBuildImage__provenance, domain=None, range=Optional[Union[dict, SlsaBuildProvenance]])

slots.slsaBuildImage__produced_by = Slot(uri=SLSA.produced_by, name="slsaBuildImage__produced_by", curie=SLSA.curie('produced_by'),
                   model_uri=SLSA.slsaBuildImage__produced_by, domain=None, range=Optional[Union[dict, SlsaBuildImageProducer]])

slots.slsaMeasurement__measured_component = Slot(uri=SLSA.measured_component, name="slsaMeasurement__measured_component", curie=SLSA.curie('measured_component'),
                   model_uri=SLSA.slsaMeasurement__measured_component, domain=None, range=str)

slots.slsaBuildEnvironmentAttestation__build_id = Slot(uri=SLSA.build_id, name="slsaBuildEnvironmentAttestation__build_id", curie=SLSA.curie('build_id'),
                   model_uri=SLSA.slsaBuildEnvironmentAttestation__build_id, domain=None, range=str)

slots.slsaBuildEnvironmentAttestation__build_image = Slot(uri=SLSA.build_image, name="slsaBuildEnvironmentAttestation__build_image", curie=SLSA.curie('build_image'),
                   model_uri=SLSA.slsaBuildEnvironmentAttestation__build_image, domain=None, range=Optional[Union[str, SlsaBuildImageImageUri]])

slots.slsaBuildEnvironmentAttestation__measurements = Slot(uri=SLSA.measurements, name="slsaBuildEnvironmentAttestation__measurements", curie=SLSA.curie('measurements'),
                   model_uri=SLSA.slsaBuildEnvironmentAttestation__measurements, domain=None, range=Optional[Union[Union[dict, SlsaMeasurement], list[Union[dict, SlsaMeasurement]]]])

slots.slsaAdoptionMetadata__challenges = Slot(uri=SLSA.challenges, name="slsaAdoptionMetadata__challenges", curie=SLSA.curie('challenges'),
                   model_uri=SLSA.slsaAdoptionMetadata__challenges, domain=None, range=Optional[Union[Union[str, "SlsaAdoptionChallenge"], list[Union[str, "SlsaAdoptionChallenge"]]]])

slots.slsaAdoptionMetadata__strategies = Slot(uri=SLSA.strategies, name="slsaAdoptionMetadata__strategies", curie=SLSA.curie('strategies'),
                   model_uri=SLSA.slsaAdoptionMetadata__strategies, domain=None, range=Optional[Union[Union[str, "SlsaAdoptionStrategy"], list[Union[str, "SlsaAdoptionStrategy"]]]])

slots.inTotoDigestSet__sha256 = Slot(uri=IN_TOTO_LINKML.sha256, name="inTotoDigestSet__sha256", curie=IN_TOTO_LINKML.curie('sha256'),
                   model_uri=SLSA.inTotoDigestSet__sha256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__sha224 = Slot(uri=IN_TOTO_LINKML.sha224, name="inTotoDigestSet__sha224", curie=IN_TOTO_LINKML.curie('sha224'),
                   model_uri=SLSA.inTotoDigestSet__sha224, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{56}$'))

slots.inTotoDigestSet__sha384 = Slot(uri=IN_TOTO_LINKML.sha384, name="inTotoDigestSet__sha384", curie=IN_TOTO_LINKML.curie('sha384'),
                   model_uri=SLSA.inTotoDigestSet__sha384, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{96}$'))

slots.inTotoDigestSet__sha512 = Slot(uri=IN_TOTO_LINKML.sha512, name="inTotoDigestSet__sha512", curie=IN_TOTO_LINKML.curie('sha512'),
                   model_uri=SLSA.inTotoDigestSet__sha512, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{128}$'))

slots.inTotoDigestSet__sha512_224 = Slot(uri=IN_TOTO_LINKML.sha512_224, name="inTotoDigestSet__sha512_224", curie=IN_TOTO_LINKML.curie('sha512_224'),
                   model_uri=SLSA.inTotoDigestSet__sha512_224, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{56}$'))

slots.inTotoDigestSet__sha512_256 = Slot(uri=IN_TOTO_LINKML.sha512_256, name="inTotoDigestSet__sha512_256", curie=IN_TOTO_LINKML.curie('sha512_256'),
                   model_uri=SLSA.inTotoDigestSet__sha512_256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__sha3_224 = Slot(uri=IN_TOTO_LINKML.sha3_224, name="inTotoDigestSet__sha3_224", curie=IN_TOTO_LINKML.curie('sha3_224'),
                   model_uri=SLSA.inTotoDigestSet__sha3_224, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{56}$'))

slots.inTotoDigestSet__sha3_256 = Slot(uri=IN_TOTO_LINKML.sha3_256, name="inTotoDigestSet__sha3_256", curie=IN_TOTO_LINKML.curie('sha3_256'),
                   model_uri=SLSA.inTotoDigestSet__sha3_256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__sha3_384 = Slot(uri=IN_TOTO_LINKML.sha3_384, name="inTotoDigestSet__sha3_384", curie=IN_TOTO_LINKML.curie('sha3_384'),
                   model_uri=SLSA.inTotoDigestSet__sha3_384, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{96}$'))

slots.inTotoDigestSet__sha3_512 = Slot(uri=IN_TOTO_LINKML.sha3_512, name="inTotoDigestSet__sha3_512", curie=IN_TOTO_LINKML.curie('sha3_512'),
                   model_uri=SLSA.inTotoDigestSet__sha3_512, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{128}$'))

slots.inTotoDigestSet__shake128 = Slot(uri=IN_TOTO_LINKML.shake128, name="inTotoDigestSet__shake128", curie=IN_TOTO_LINKML.curie('shake128'),
                   model_uri=SLSA.inTotoDigestSet__shake128, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{2})*$'))

slots.inTotoDigestSet__shake256 = Slot(uri=IN_TOTO_LINKML.shake256, name="inTotoDigestSet__shake256", curie=IN_TOTO_LINKML.curie('shake256'),
                   model_uri=SLSA.inTotoDigestSet__shake256, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{2})*$'))

slots.inTotoDigestSet__blake2b = Slot(uri=IN_TOTO_LINKML.blake2b, name="inTotoDigestSet__blake2b", curie=IN_TOTO_LINKML.curie('blake2b'),
                   model_uri=SLSA.inTotoDigestSet__blake2b, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{2}){0,32}$'))

slots.inTotoDigestSet__blake2s = Slot(uri=IN_TOTO_LINKML.blake2s, name="inTotoDigestSet__blake2s", curie=IN_TOTO_LINKML.curie('blake2s'),
                   model_uri=SLSA.inTotoDigestSet__blake2s, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__ripemd160 = Slot(uri=IN_TOTO_LINKML.ripemd160, name="inTotoDigestSet__ripemd160", curie=IN_TOTO_LINKML.curie('ripemd160'),
                   model_uri=SLSA.inTotoDigestSet__ripemd160, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}$'))

slots.inTotoDigestSet__sm3 = Slot(uri=IN_TOTO_LINKML.sm3, name="inTotoDigestSet__sm3", curie=IN_TOTO_LINKML.curie('sm3'),
                   model_uri=SLSA.inTotoDigestSet__sm3, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__gost = Slot(uri=IN_TOTO_LINKML.gost, name="inTotoDigestSet__gost", curie=IN_TOTO_LINKML.curie('gost'),
                   model_uri=SLSA.inTotoDigestSet__gost, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}([a-f0-9]{64})?$'))

slots.inTotoDigestSet__sha1 = Slot(uri=IN_TOTO_LINKML.sha1, name="inTotoDigestSet__sha1", curie=IN_TOTO_LINKML.curie('sha1'),
                   model_uri=SLSA.inTotoDigestSet__sha1, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}$'))

slots.inTotoDigestSet__md5 = Slot(uri=IN_TOTO_LINKML.md5, name="inTotoDigestSet__md5", curie=IN_TOTO_LINKML.curie('md5'),
                   model_uri=SLSA.inTotoDigestSet__md5, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{32}$'))

slots.inTotoDigestSet__dir_hash = Slot(uri=IN_TOTO_LINKML.dir_hash, name="inTotoDigestSet__dir_hash", curie=IN_TOTO_LINKML.curie('dir_hash'),
                   model_uri=SLSA.inTotoDigestSet__dir_hash, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.inTotoDigestSet__git_commit = Slot(uri=IN_TOTO_LINKML.git_commit, name="inTotoDigestSet__git_commit", curie=IN_TOTO_LINKML.curie('git_commit'),
                   model_uri=SLSA.inTotoDigestSet__git_commit, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__git_tree = Slot(uri=IN_TOTO_LINKML.git_tree, name="inTotoDigestSet__git_tree", curie=IN_TOTO_LINKML.curie('git_tree'),
                   model_uri=SLSA.inTotoDigestSet__git_tree, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__git_blob = Slot(uri=IN_TOTO_LINKML.git_blob, name="inTotoDigestSet__git_blob", curie=IN_TOTO_LINKML.curie('git_blob'),
                   model_uri=SLSA.inTotoDigestSet__git_blob, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__git_tag = Slot(uri=IN_TOTO_LINKML.git_tag, name="inTotoDigestSet__git_tag", curie=IN_TOTO_LINKML.curie('git_tag'),
                   model_uri=SLSA.inTotoDigestSet__git_tag, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{40}([a-f0-9]{24})?$'))

slots.inTotoDigestSet__additional_digests = Slot(uri=IN_TOTO_LINKML.additional_digests, name="inTotoDigestSet__additional_digests", curie=IN_TOTO_LINKML.curie('additional_digests'),
                   model_uri=SLSA.inTotoDigestSet__additional_digests, domain=None, range=Optional[Union[Union[dict, InTotoAdditionalDigest], list[Union[dict, InTotoAdditionalDigest]]]])

slots.inTotoAdditionalDigest__algorithm = Slot(uri=SPDX.algorithm, name="inTotoAdditionalDigest__algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=SLSA.inTotoAdditionalDigest__algorithm, domain=None, range=str,
                   pattern=re.compile(r'^[a-z][A-Za-z0-9_.:-]*$'))

slots.inTotoAdditionalDigest__value = Slot(uri=IN_TOTO_LINKML.value, name="inTotoAdditionalDigest__value", curie=IN_TOTO_LINKML.curie('value'),
                   model_uri=SLSA.inTotoAdditionalDigest__value, domain=None, range=str,
                   pattern=re.compile(r'^\S+$'))

slots.inTotoAnnotation__annotation_key = Slot(uri=IN_TOTO_LINKML.annotation_key, name="inTotoAnnotation__annotation_key", curie=IN_TOTO_LINKML.curie('annotation_key'),
                   model_uri=SLSA.inTotoAnnotation__annotation_key, domain=None, range=str)

slots.inTotoAnnotation__annotation_values = Slot(uri=IN_TOTO_LINKML.annotation_values, name="inTotoAnnotation__annotation_values", curie=IN_TOTO_LINKML.curie('annotation_values'),
                   model_uri=SLSA.inTotoAnnotation__annotation_values, domain=None, range=Optional[Union[str, list[str]]])

slots.inTotoResourceDescriptor__resource_name = Slot(uri=IN_TOTO_LINKML.resource_name, name="inTotoResourceDescriptor__resource_name", curie=IN_TOTO_LINKML.curie('resource_name'),
                   model_uri=SLSA.inTotoResourceDescriptor__resource_name, domain=None, range=Optional[str])

slots.inTotoResourceDescriptor__download_location = Slot(uri=IN_TOTO_LINKML.download_location, name="inTotoResourceDescriptor__download_location", curie=IN_TOTO_LINKML.curie('download_location'),
                   model_uri=SLSA.inTotoResourceDescriptor__download_location, domain=None, range=Optional[Union[str, InTotoResourceUri]])

slots.inTotoResourceDescriptor__media_type = Slot(uri=DCAT.mediaType, name="inTotoResourceDescriptor__media_type", curie=DCAT.curie('mediaType'),
                   model_uri=SLSA.inTotoResourceDescriptor__media_type, domain=None, range=Optional[str])

slots.inTotoResourceDescriptor__content = Slot(uri=IN_TOTO_LINKML.content, name="inTotoResourceDescriptor__content", curie=IN_TOTO_LINKML.curie('content'),
                   model_uri=SLSA.inTotoResourceDescriptor__content, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9+/_-]+={0,2}$'))

slots.inTotoResourceDescriptor__annotations = Slot(uri=IN_TOTO_LINKML.annotations, name="inTotoResourceDescriptor__annotations", curie=IN_TOTO_LINKML.curie('annotations'),
                   model_uri=SLSA.inTotoResourceDescriptor__annotations, domain=None, range=Optional[Union[Union[dict, InTotoAnnotation], list[Union[dict, InTotoAnnotation]]]])

slots.inTotoStatement__statement_type = Slot(uri=IN_TOTO_LINKML.statement_type, name="inTotoStatement__statement_type", curie=IN_TOTO_LINKML.curie('statement_type'),
                   model_uri=SLSA.inTotoStatement__statement_type, domain=None, range=Union[str, InTotoTypeUri],
                   pattern=re.compile(r'^https://in-toto\.io/Statement/v1$'))

slots.inTotoStatement__subject = Slot(uri=IN_TOTO_LINKML.subject, name="inTotoStatement__subject", curie=IN_TOTO_LINKML.curie('subject'),
                   model_uri=SLSA.inTotoStatement__subject, domain=None, range=Union[Union[dict, InTotoStatementSubject], list[Union[dict, InTotoStatementSubject]]])

slots.inTotoStatement__predicate_type = Slot(uri=IN_TOTO_LINKML.predicate_type, name="inTotoStatement__predicate_type", curie=IN_TOTO_LINKML.curie('predicate_type'),
                   model_uri=SLSA.inTotoStatement__predicate_type, domain=None, range=Union[str, InTotoTypeUri])

slots.inTotoPredicate__predicate_kind = Slot(uri=IN_TOTO_LINKML.predicate_kind, name="inTotoPredicate__predicate_kind", curie=IN_TOTO_LINKML.curie('predicate_kind'),
                   model_uri=SLSA.inTotoPredicate__predicate_kind, domain=None, range=Optional[str])

slots.SlsaVerificationSummary_resource_uri = Slot(uri=IN_TOTO_LINKML.resource_uri, name="SlsaVerificationSummary_resource_uri", curie=IN_TOTO_LINKML.curie('resource_uri'),
                   model_uri=SLSA.SlsaVerificationSummary_resource_uri, domain=SlsaVerificationSummary, range=Union[str, InTotoResourceUri])

slots.SlsaVerificationSummaryPolicy_resource_uri = Slot(uri=IN_TOTO_LINKML.resource_uri, name="SlsaVerificationSummaryPolicy_resource_uri", curie=IN_TOTO_LINKML.curie('resource_uri'),
                   model_uri=SLSA.SlsaVerificationSummaryPolicy_resource_uri, domain=SlsaVerificationSummaryPolicy, range=Union[str, InTotoResourceUri])

slots.SlsaVerificationSummaryPolicy_digest = Slot(uri=IN_TOTO_LINKML.digest, name="SlsaVerificationSummaryPolicy_digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=SLSA.SlsaVerificationSummaryPolicy_digest, domain=SlsaVerificationSummaryPolicy, range=Optional[Union[dict, InTotoDigestSet]])

slots.SlsaVerificationSummaryInputAttestation_digest = Slot(uri=IN_TOTO_LINKML.digest, name="SlsaVerificationSummaryInputAttestation_digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=SLSA.SlsaVerificationSummaryInputAttestation_digest, domain=SlsaVerificationSummaryInputAttestation, range=Union[dict, InTotoDigestSet])

slots.SlsaVerificationSummaryInputAttestation_resource_uri = Slot(uri=IN_TOTO_LINKML.resource_uri, name="SlsaVerificationSummaryInputAttestation_resource_uri", curie=IN_TOTO_LINKML.curie('resource_uri'),
                   model_uri=SLSA.SlsaVerificationSummaryInputAttestation_resource_uri, domain=SlsaVerificationSummaryInputAttestation, range=Optional[Union[str, InTotoResourceUri]])

slots.SlsaSourceProvenance_revision = Slot(uri=SLSA.revision, name="SlsaSourceProvenance_revision", curie=SLSA.curie('revision'),
                   model_uri=SLSA.SlsaSourceProvenance_revision, domain=SlsaSourceProvenance, range=Union[str, SlsaSourceRevisionRevisionId])

slots.InTotoStatementSubject_digest = Slot(uri=IN_TOTO_LINKML.digest, name="InTotoStatementSubject_digest", curie=IN_TOTO_LINKML.curie('digest'),
                   model_uri=SLSA.InTotoStatementSubject_digest, domain=InTotoStatementSubject, range=Union[dict, InTotoDigestSet])
