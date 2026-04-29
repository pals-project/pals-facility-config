# Auto generated from narad.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-29T16:33:39
# Schema: narad
#
# id: https://w3id.org/narad_linkml/schema/narad/
# description: NARAD extension for capability-layer semantics and facility-specific signal bindings
# license: CC-BY-4.0

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

from linkml_runtime.linkml_model.types import Boolean, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = "0.1.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NARAD = CurieNamespace('narad', 'https://w3id.org/narad_linkml/schema/narad/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SI_UNIT = CurieNamespace('si-unit', 'http://qudt.org/vocab/unit/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
DEFAULT_ = NARAD


# Types

# Class references
class FacilityName(extended_str):
    pass


class SignalBindingName(extended_str):
    pass


class DeviceTypeSignalSetName(extended_str):
    pass


class SignalName(extended_str):
    pass


class CapabilityName(extended_str):
    pass


class TypeSpecificCapabilityId(extended_str):
    pass


class CapabilityProfileName(extended_str):
    pass


class RelationshipId(extended_str):
    pass


class ControlProfileFamilyName(extended_str):
    pass


class BeamlineBeamlineName(extended_str):
    pass


class BeamlineElementName(extended_str):
    pass


class PVBindingName(extended_str):
    pass


@dataclass(repr=False)
class NaradModel(YAMLRoot):
    """
    Top-level NARAD document container.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["NaradModel"]
    class_class_curie: ClassVar[str] = "narad:NaradModel"
    class_name: ClassVar[str] = "NaradModel"
    class_model_uri: ClassVar[URIRef] = NARAD.NaradModel

    narad: Optional[Union[dict, "NaradConfig"]] = None
    beamlines: Optional[Union[dict[Union[str, BeamlineBeamlineName], Union[dict, "Beamline"]], list[Union[dict, "Beamline"]]]] = empty_dict()
    elements: Optional[Union[dict[Union[str, BeamlineElementName], Union[dict, "BeamlineElement"]], list[Union[dict, "BeamlineElement"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.narad is not None and not isinstance(self.narad, NaradConfig):
            self.narad = NaradConfig(**as_dict(self.narad))

        self._normalize_inlined_as_list(slot_name="beamlines", slot_type=Beamline, key_name="beamline_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="elements", slot_type=BeamlineElement, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NaradConfig(YAMLRoot):
    """
    NARAD configuration block containing the capability layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/NaradConfig"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/NaradConfig"
    class_name: ClassVar[str] = "NaradConfig"
    class_model_uri: ClassVar[URIRef] = NARAD.NaradConfig

    schema_version: Optional[str] = None
    intent: Optional[str] = None
    capability_layer: Optional[Union[dict, "CapabilityLayer"]] = None
    facility: Optional[str] = None
    control_system: Optional[str] = None
    signal_layer: Optional[Union[dict, "SignalLayer"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.intent is not None and not isinstance(self.intent, str):
            self.intent = str(self.intent)

        if self.capability_layer is not None and not isinstance(self.capability_layer, CapabilityLayer):
            self.capability_layer = CapabilityLayer(**as_dict(self.capability_layer))

        if self.facility is not None and not isinstance(self.facility, str):
            self.facility = str(self.facility)

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.signal_layer is not None and not isinstance(self.signal_layer, SignalLayer):
            self.signal_layer = SignalLayer(**as_dict(self.signal_layer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityLayer(YAMLRoot):
    """
    Capability-layer container for profile families and a shared default graph projection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/CapabilityLayer"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/CapabilityLayer"
    class_name: ClassVar[str] = "CapabilityLayer"
    class_model_uri: ClassVar[URIRef] = NARAD.CapabilityLayer

    default_graph_projection: Optional[Union[dict, "GraphProjection"]] = None
    profiles: Optional[Union[dict[Union[str, ControlProfileFamilyName], Union[dict, "ControlProfileFamily"]], list[Union[dict, "ControlProfileFamily"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.default_graph_projection is not None and not isinstance(self.default_graph_projection, GraphProjection):
            self.default_graph_projection = GraphProjection(**as_dict(self.default_graph_projection))

        self._normalize_inlined_as_dict(slot_name="profiles", slot_type=ControlProfileFamily, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalLayer(YAMLRoot):
    """
    Signal-layer container for facility-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/SignalLayer"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/SignalLayer"
    class_name: ClassVar[str] = "SignalLayer"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalLayer

    facilities: Optional[Union[dict[Union[str, FacilityName], Union[dict, "Facility"]], list[Union[dict, "Facility"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="facilities", slot_type=Facility, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Facility(YAMLRoot):
    """
    A facility with specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/Facility"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/Facility"
    class_name: ClassVar[str] = "Facility"
    class_model_uri: ClassVar[URIRef] = NARAD.Facility

    name: Union[str, FacilityName] = None
    identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    control_system: Optional[str] = None
    naming_convention: Optional[str] = None
    signal_definitions: Optional[Union[dict, "SignalDefinitions"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FacilityName):
            self.name = FacilityName(self.name)

        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier] if self.identifier is not None else []
        self.identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.identifier]

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.naming_convention is not None and not isinstance(self.naming_convention, str):
            self.naming_convention = str(self.naming_convention)

        if self.signal_definitions is not None and not isinstance(self.signal_definitions, SignalDefinitions):
            self.signal_definitions = SignalDefinitions(**as_dict(self.signal_definitions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalDefinitions(YAMLRoot):
    """
    EPICS signal suffix templates keyed by device type or device domain. Use a domain-level key (e.g. Magnet,
    RFCavity) for signals shared across all types in that domain; use a device-type key (e.g. Quadrupole, BPM) for
    type-specific signals. New device types require no schema changes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/SignalDefinitions"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/SignalDefinitions"
    class_name: ClassVar[str] = "SignalDefinitions"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalDefinitions

    type_signal_sets: Optional[Union[dict[Union[str, DeviceTypeSignalSetName], Union[dict, "DeviceTypeSignalSet"]], list[Union[dict, "DeviceTypeSignalSet"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="type_signal_sets", slot_type=DeviceTypeSignalSet, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalBinding(YAMLRoot):
    """
    A named EPICS suffix definition for one semantic signal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/SignalBinding"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/SignalBinding"
    class_name: ClassVar[str] = "SignalBinding"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalBinding

    name: Union[str, SignalBindingName] = None
    epics_suffix: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SignalBindingName):
            self.name = SignalBindingName(self.name)

        if self.epics_suffix is not None and not isinstance(self.epics_suffix, str):
            self.epics_suffix = str(self.epics_suffix)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeviceTypeSignalSet(YAMLRoot):
    """
    Signal binding set scoped to a device type (for example, Quadrupole or BPM).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/DeviceTypeSignalSet"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/DeviceTypeSignalSet"
    class_name: ClassVar[str] = "DeviceTypeSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.DeviceTypeSignalSet

    name: Union[str, DeviceTypeSignalSetName] = None
    signal_bindings: Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DeviceTypeSignalSetName):
            self.name = DeviceTypeSignalSetName(self.name)

        self._normalize_inlined_as_dict(slot_name="signal_bindings", slot_type=SignalBinding, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityMixin(YAMLRoot):
    """
    Shared structure common to all capability types: a description and an ordered list of signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/CapabilityMixin"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/CapabilityMixin"
    class_name: ClassVar[str] = "CapabilityMixin"
    class_model_uri: ClassVar[URIRef] = NARAD.CapabilityMixin

    description: Optional[str] = None
    signals: Optional[Union[dict[Union[str, SignalName], Union[dict, "Signal"]], list[Union[dict, "Signal"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signal(YAMLRoot):
    """
    A named semantic signal used by a capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["ObservableProperty"]
    class_class_curie: ClassVar[str] = "sosa:ObservableProperty"
    class_name: ClassVar[str] = "Signal"
    class_model_uri: ClassVar[URIRef] = NARAD.Signal

    name: Union[str, SignalName] = None
    role: Optional[Union[str, "SignalRoleEnum"]] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    units: Optional[str] = None
    units_uri: Optional[Union[str, URIorCURIE]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SignalName):
            self.name = SignalName(self.name)

        if self.role is not None and not isinstance(self.role, SignalRoleEnum):
            self.role = SignalRoleEnum(self.role)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        if self.units is not None and not isinstance(self.units, str):
            self.units = str(self.units)

        if self.units_uri is not None and not isinstance(self.units_uri, URIorCURIE):
            self.units_uri = URIorCURIE(self.units_uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Capability(YAMLRoot):
    """
    A named, shared grouping of semantically related signals for a control aspect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/Capability"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/Capability"
    class_name: ClassVar[str] = "Capability"
    class_model_uri: ClassVar[URIRef] = NARAD.Capability

    name: Union[str, CapabilityName] = None
    description: Optional[str] = None
    signals: Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CapabilityName):
            self.name = CapabilityName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypeSpecificCapability(YAMLRoot):
    """
    An inline capability declared within a device-type profile, with its own identifier, a semantic class label, a
    description, and a list of signals. Distinct from the shared capabilities referenced by name; these are
    profile-local definitions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/TypeSpecificCapability"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/TypeSpecificCapability"
    class_name: ClassVar[str] = "TypeSpecificCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.TypeSpecificCapability

    id: Union[str, TypeSpecificCapabilityId] = None
    capability_class: Optional[str] = None
    class_curie: Optional[Union[str, URIorCURIE]] = None
    description: Optional[str] = None
    signals: Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TypeSpecificCapabilityId):
            self.id = TypeSpecificCapabilityId(self.id)

        if self.capability_class is not None and not isinstance(self.capability_class, str):
            self.capability_class = str(self.capability_class)

        if self.class_curie is not None and not isinstance(self.class_curie, URIorCURIE):
            self.class_curie = URIorCURIE(self.class_curie)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityProfile(YAMLRoot):
    """
    A device-type profile that reuses shared capabilities and adds specific capabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/CapabilityProfile"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/CapabilityProfile"
    class_name: ClassVar[str] = "CapabilityProfile"
    class_model_uri: ClassVar[URIRef] = NARAD.CapabilityProfile

    name: Union[str, CapabilityProfileName] = None
    device_type: Optional[Union[str, "ElementKindEnum"]] = None
    description: Optional[str] = None
    is_abstract: Optional[Union[bool, Bool]] = False
    inherits_shared_capabilities: Optional[Union[Union[str, CapabilityName], list[Union[str, CapabilityName]]]] = empty_list()
    type_specific_capabilities: Optional[Union[dict[Union[str, TypeSpecificCapabilityId], Union[dict, TypeSpecificCapability]], list[Union[dict, TypeSpecificCapability]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CapabilityProfileName):
            self.name = CapabilityProfileName(self.name)

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.is_abstract is not None and not isinstance(self.is_abstract, Bool):
            self.is_abstract = Bool(self.is_abstract)

        if not isinstance(self.inherits_shared_capabilities, list):
            self.inherits_shared_capabilities = [self.inherits_shared_capabilities] if self.inherits_shared_capabilities is not None else []
        self.inherits_shared_capabilities = [v if isinstance(v, CapabilityName) else CapabilityName(v) for v in self.inherits_shared_capabilities]

        self._normalize_inlined_as_list(slot_name="type_specific_capabilities", slot_type=TypeSpecificCapability, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NodeLabels(YAMLRoot):
    """
    Static node-type label strings for the graph projection, covering all node categories except Device. The device
    label is derived from ControlProfileFamily.device_domain and need not be repeated here.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/NodeLabels"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/NodeLabels"
    class_name: ClassVar[str] = "NodeLabels"
    class_model_uri: ClassVar[URIRef] = NARAD.NodeLabels

    capability_family: Optional[str] = None
    profile: Optional[str] = None
    capability: Optional[str] = None
    signal: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.capability_family is not None and not isinstance(self.capability_family, str):
            self.capability_family = str(self.capability_family)

        if self.profile is not None and not isinstance(self.profile, str):
            self.profile = str(self.profile)

        if self.capability is not None and not isinstance(self.capability, str):
            self.capability = str(self.capability)

        if self.signal is not None and not isinstance(self.signal, str):
            self.signal = str(self.signal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GraphProjection(YAMLRoot):
    """
    Graph projection metadata for node labels and edge categories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/GraphProjection"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/GraphProjection"
    class_name: ClassVar[str] = "GraphProjection"
    class_model_uri: ClassVar[URIRef] = NARAD.GraphProjection

    node_labels: Optional[Union[dict, NodeLabels]] = None
    relationships: Optional[Union[dict[Union[str, RelationshipId], Union[dict, "Relationship"]], list[Union[dict, "Relationship"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.node_labels is not None and not isinstance(self.node_labels, NodeLabels):
            self.node_labels = NodeLabels(**as_dict(self.node_labels))

        self._normalize_inlined_as_list(slot_name="relationships", slot_type=Relationship, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    A directed edge type in the NARAD graph projection, modelled after the OBO Relation Ontology (RO) ObjectProperty
    metamodel. Each relationship carries an identifier, human-readable label, natural-language description, and
    explicit domain/range node-type constraints.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["ObjectProperty"]
    class_class_curie: ClassVar[str] = "owl:ObjectProperty"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = NARAD.Relationship

    id: Union[str, RelationshipId] = None
    range: Union[str, "NodeTypeEnum"] = None
    range_target: str = None
    domain: Optional[Union[str, "NodeTypeEnum"]] = None
    subproperty_of: Optional[Union[Union[str, RelationshipId], list[Union[str, RelationshipId]]]] = empty_list()
    inverse_of: Optional[Union[str, RelationshipId]] = None
    symmetric: Optional[Union[bool, Bool]] = None
    transitive: Optional[Union[bool, Bool]] = None
    asymmetric: Optional[Union[bool, Bool]] = None
    irreflexive: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipId):
            self.id = RelationshipId(self.id)

        if self._is_empty(self.range):
            self.MissingRequiredField("range")
        if not isinstance(self.range, NodeTypeEnum):
            self.range = NodeTypeEnum(self.range)

        if self._is_empty(self.range_target):
            self.MissingRequiredField("range_target")
        if not isinstance(self.range_target, str):
            self.range_target = str(self.range_target)

        if self.domain is not None and not isinstance(self.domain, NodeTypeEnum):
            self.domain = NodeTypeEnum(self.domain)

        if not isinstance(self.subproperty_of, list):
            self.subproperty_of = [self.subproperty_of] if self.subproperty_of is not None else []
        self.subproperty_of = [v if isinstance(v, RelationshipId) else RelationshipId(v) for v in self.subproperty_of]

        if self.inverse_of is not None and not isinstance(self.inverse_of, RelationshipId):
            self.inverse_of = RelationshipId(self.inverse_of)

        if self.symmetric is not None and not isinstance(self.symmetric, Bool):
            self.symmetric = Bool(self.symmetric)

        if self.transitive is not None and not isinstance(self.transitive, Bool):
            self.transitive = Bool(self.transitive)

        if self.asymmetric is not None and not isinstance(self.asymmetric, Bool):
            self.asymmetric = Bool(self.asymmetric)

        if self.irreflexive is not None and not isinstance(self.irreflexive, Bool):
            self.irreflexive = Bool(self.irreflexive)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlProfileFamily(YAMLRoot):
    """
    A reusable family of control profiles sharing common semantics and structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/ControlProfileFamily"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/ControlProfileFamily"
    class_name: ClassVar[str] = "ControlProfileFamily"
    class_model_uri: ClassVar[URIRef] = NARAD.ControlProfileFamily

    name: Union[str, ControlProfileFamilyName] = None
    device_domain: Optional[Union[str, "DeviceDomainEnum"]] = None
    description: Optional[str] = None
    shared_capabilities: Optional[Union[dict[Union[str, CapabilityName], Union[dict, Capability]], list[Union[dict, Capability]]]] = empty_dict()
    type_profiles: Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]] = empty_dict()
    graph_projection: Optional[Union[dict, GraphProjection]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlProfileFamilyName):
            self.name = ControlProfileFamilyName(self.name)

        if self.device_domain is not None and not isinstance(self.device_domain, DeviceDomainEnum):
            self.device_domain = DeviceDomainEnum(self.device_domain)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="shared_capabilities", slot_type=Capability, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="type_profiles", slot_type=CapabilityProfile, key_name="name", keyed=True)

        if self.graph_projection is not None and not isinstance(self.graph_projection, GraphProjection):
            self.graph_projection = GraphProjection(**as_dict(self.graph_projection))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifier(YAMLRoot):
    """
    A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["narad_narad/Identifier"]
    class_class_curie: ClassVar[str] = "narad:narad_narad/Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = NARAD.Identifier

    identifier_type: Optional[Union[str, "IdentifierTypeEnum"]] = None
    identifier_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.identifier_type is not None and not isinstance(self.identifier_type, IdentifierTypeEnum):
            self.identifier_type = IdentifierTypeEnum(self.identifier_type)

        if self.identifier_value is not None and not isinstance(self.identifier_value, str):
            self.identifier_value = str(self.identifier_value)

        super().__post_init__(**kwargs)


AnyValue = Any

@dataclass(repr=False)
class Beamline(YAMLRoot):
    """
    An ordered sequence of beamline elements defining a beam path.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["beamline/Beamline"]
    class_class_curie: ClassVar[str] = "narad:beamline/Beamline"
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = NARAD.Beamline

    beamline_name: Union[str, BeamlineBeamlineName] = None
    kind: Optional[str] = None
    line: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.beamline_name):
            self.MissingRequiredField("beamline_name")
        if not isinstance(self.beamline_name, BeamlineBeamlineName):
            self.beamline_name = BeamlineBeamlineName(self.beamline_name)

        if self.kind is not None and not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if not isinstance(self.line, list):
            self.line = [self.line] if self.line is not None else []
        self.line = [v if isinstance(v, str) else str(v) for v in self.line]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamlineElement(YAMLRoot):
    """
    A single element in a beamline with optional physics parameter blocks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/BeamlineElement"]
    class_class_curie: ClassVar[str] = "narad:elements/BeamlineElement"
    class_name: ClassVar[str] = "BeamlineElement"
    class_model_uri: ClassVar[URIRef] = NARAD.BeamlineElement

    name: Union[str, BeamlineElementName] = None
    kind: Optional[Union[str, "ElementKindEnum"]] = None
    length: Optional[float] = None
    RFP: Optional[Union[dict, "RFParams"]] = None
    BendP: Optional[Union[dict, "BendParams"]] = None
    MagneticMultipoleP: Optional[Union[dict, "MagneticMultipoleParams"]] = None
    SolenoidP: Optional[Union[dict, "SolenoidParams"]] = None
    narad: Optional[Union[dict, "ElementNaradRef"]] = None
    facility_params: Optional[Union[dict, "FacilityParams"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineElementName):
            self.name = BeamlineElementName(self.name)

        if self.kind is not None and not isinstance(self.kind, ElementKindEnum):
            self.kind = ElementKindEnum(self.kind)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.RFP is not None and not isinstance(self.RFP, RFParams):
            self.RFP = RFParams(**as_dict(self.RFP))

        if self.BendP is not None and not isinstance(self.BendP, BendParams):
            self.BendP = BendParams(**as_dict(self.BendP))

        if self.MagneticMultipoleP is not None and not isinstance(self.MagneticMultipoleP, MagneticMultipoleParams):
            self.MagneticMultipoleP = MagneticMultipoleParams(**as_dict(self.MagneticMultipoleP))

        if self.SolenoidP is not None and not isinstance(self.SolenoidP, SolenoidParams):
            self.SolenoidP = SolenoidParams(**as_dict(self.SolenoidP))

        if self.narad is not None and not isinstance(self.narad, ElementNaradRef):
            self.narad = ElementNaradRef(**as_dict(self.narad))

        if self.facility_params is not None and not isinstance(self.facility_params, FacilityParams):
            self.facility_params = FacilityParams(**as_dict(self.facility_params))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementNaradRef(YAMLRoot):
    """
    NARAD semantic reference block attached to a beamline element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/ElementNaradRef"]
    class_class_curie: ClassVar[str] = "narad:elements/ElementNaradRef"
    class_name: ClassVar[str] = "ElementNaradRef"
    class_model_uri: ClassVar[URIRef] = NARAD.ElementNaradRef

    capability_profile_family: Optional[Union[str, ControlProfileFamilyName]] = None
    capability_profile: Optional[Union[str, CapabilityProfileName]] = None
    signal_bindings: Optional[Union[dict[Union[str, PVBindingName], Union[dict, "PVBinding"]], list[Union[dict, "PVBinding"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.capability_profile_family is not None and not isinstance(self.capability_profile_family, ControlProfileFamilyName):
            self.capability_profile_family = ControlProfileFamilyName(self.capability_profile_family)

        if self.capability_profile is not None and not isinstance(self.capability_profile, CapabilityProfileName):
            self.capability_profile = CapabilityProfileName(self.capability_profile)

        self._normalize_inlined_as_dict(slot_name="signal_bindings", slot_type=PVBinding, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PVBinding(YAMLRoot):
    """
    A concrete PV (Process Variable) binding for one semantic signal on a beamline element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/PVBinding"]
    class_class_curie: ClassVar[str] = "narad:elements/PVBinding"
    class_name: ClassVar[str] = "PVBinding"
    class_model_uri: ClassVar[URIRef] = NARAD.PVBinding

    name: Union[str, PVBindingName] = None
    facility: Optional[str] = None
    control_system: Optional[str] = None
    pv: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PVBindingName):
            self.name = PVBindingName(self.name)

        if self.facility is not None and not isinstance(self.facility, str):
            self.facility = str(self.facility)

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.pv is not None and not isinstance(self.pv, str):
            self.pv = str(self.pv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RFParams(YAMLRoot):
    """
    RF cavity physics parameters (frequency, voltage, phase).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/RFParams"]
    class_class_curie: ClassVar[str] = "narad:elements/RFParams"
    class_name: ClassVar[str] = "RFParams"
    class_model_uri: ClassVar[URIRef] = NARAD.RFParams

    frequency: Optional[float] = None
    voltage: Optional[float] = None
    phase: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.frequency is not None and not isinstance(self.frequency, float):
            self.frequency = float(self.frequency)

        if self.voltage is not None and not isinstance(self.voltage, float):
            self.voltage = float(self.voltage)

        if self.phase is not None and not isinstance(self.phase, float):
            self.phase = float(self.phase)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BendParams(YAMLRoot):
    """
    Dipole/bend physics parameters (entry angle, exit edge angles).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/BendParams"]
    class_class_curie: ClassVar[str] = "narad:elements/BendParams"
    class_name: ClassVar[str] = "BendParams"
    class_model_uri: ClassVar[URIRef] = NARAD.BendParams

    angle_ref: Optional[float] = None
    e1: Optional[float] = None
    e2: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.angle_ref is not None and not isinstance(self.angle_ref, float):
            self.angle_ref = float(self.angle_ref)

        if self.e1 is not None and not isinstance(self.e1, float):
            self.e1 = float(self.e1)

        if self.e2 is not None and not isinstance(self.e2, float):
            self.e2 = float(self.e2)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MagneticMultipoleParams(YAMLRoot):
    """
    Magnetic multipole physics parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/MagneticMultipoleParams"]
    class_class_curie: ClassVar[str] = "narad:elements/MagneticMultipoleParams"
    class_name: ClassVar[str] = "MagneticMultipoleParams"
    class_model_uri: ClassVar[URIRef] = NARAD.MagneticMultipoleParams

    Kn1: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Kn1 is not None and not isinstance(self.Kn1, float):
            self.Kn1 = float(self.Kn1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolenoidParams(YAMLRoot):
    """
    Solenoid physics parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["elements/SolenoidParams"]
    class_class_curie: ClassVar[str] = "narad:elements/SolenoidParams"
    class_name: ClassVar[str] = "SolenoidParams"
    class_model_uri: ClassVar[URIRef] = NARAD.SolenoidParams

    Ksol: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Ksol is not None and not isinstance(self.Ksol, float):
            self.Ksol = float(self.Ksol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FacilityParams(YAMLRoot):
    """
    Facility-specific element parameters: type designation, accelerator model name, and open property map.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["facility_params/FacilityParams"]
    class_class_curie: ClassVar[str] = "narad:facility_params/FacilityParams"
    class_name: ClassVar[str] = "FacilityParams"
    class_model_uri: ClassVar[URIRef] = NARAD.FacilityParams

    facility_element_type: Optional[str] = None
    modeled_as: Optional[str] = None
    properties: Optional[Union[dict, AnyValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.facility_element_type is not None and not isinstance(self.facility_element_type, str):
            self.facility_element_type = str(self.facility_element_type)

        if self.modeled_as is not None and not isinstance(self.modeled_as, str):
            self.modeled_as = str(self.modeled_as)

        super().__post_init__(**kwargs)


# Enumerations
class DataTypeEnum(EnumDefinitionImpl):
    """
    Allowed data types for signal values.
    """
    int = PermissibleValue(
        text="int",
        description="""A data type comprised of numbers with no fractional part, including negative and positive values.""",
        meaning=NCIT["C47840"])
    float = PermissibleValue(
        text="float",
        description="A number that can have its decimal point in any position.",
        meaning=NCIT["C48150"])
    double = PermissibleValue(
        text="double",
        description="A 64-bit floating-point value.",
        meaning=NCIT["C48870"])
    string = PermissibleValue(
        text="string",
        description="A sequence of characters used to represent text.",
        meaning=NCIT["C45253"])
    boolean = PermissibleValue(
        text="boolean",
        description="A data type with two possible values: true and false.",
        meaning=NCIT["C45254"])
    boolean_non_null = PermissibleValue(
        text="boolean_non_null",
        description="A two-value boolean data type that does not include null flavor.",
        meaning=NCIT["C95630"])
    date = PermissibleValue(
        text="date",
        description="A calendar date (year, month, day).",
        meaning=NCIT["C48871"])
    coded_value = PermissibleValue(
        text="coded_value",
        description="A code value referenced from an external coding system or ontology.",
        meaning=NCIT["C95637"])

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Allowed data types for signal values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="""A special value that may represent an unknown, missing, not applicable, or undefined value.""",
                meaning=NCIT["C45255"]))

class ElementKindEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for beamline element types, shared between the capability layer
    (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here ensures that
    profile device_type values stay in sync with element kind values without circular imports. Kept intentionally
    small; ADD new values here as the NARAD schema evolves.
    """
    Drift = PermissibleValue(
        text="Drift",
        description="A field-free drift space between elements.")
    Marker = PermissibleValue(
        text="Marker",
        description="A zero-length reference point or survey marker.")
    BPM = PermissibleValue(
        text="BPM",
        description="Beam Position Monitor.")
    Corrector = PermissibleValue(
        text="Corrector",
        description="Dipole corrector magnet for orbit correction.")
    Dipole = PermissibleValue(
        text="Dipole",
        description="Dipole bending magnet.")
    Quadrupole = PermissibleValue(
        text="Quadrupole",
        description="Quadrupole focusing/defocusing magnet.")
    Solenoid = PermissibleValue(
        text="Solenoid",
        description="Solenoid magnet.")
    RFCavity = PermissibleValue(
        text="RFCavity",
        description="Radio-frequency accelerating or bunching cavity.")
    Instrument = PermissibleValue(
        text="Instrument",
        description="Generic beam diagnostic instrument (halo monitor, viewer, etc.).")

    _defn = EnumDefinition(
        name="ElementKindEnum",
        description="""Controlled vocabulary for beamline element types, shared between the capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here ensures that profile device_type values stay in sync with element kind values without circular imports. Kept intentionally small; ADD new values here as the NARAD schema evolves.""",
    )

class SignalRoleEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for the semantic role of a signal within a capability.
    """
    control = PermissibleValue(
        text="control",
        description="A writable signal that commands a device setpoint.")
    readback = PermissibleValue(
        text="readback",
        description="A readable signal that reports a measured or monitored quantity.")
    constraint = PermissibleValue(
        text="constraint",
        description="A signal that defines an operational limit or boundary on a control quantity.")
    status = PermissibleValue(
        text="status",
        description="A signal reporting the device or system operational state.")
    interlock = PermissibleValue(
        text="interlock",
        description="A signal associated with a machine protection or safety interlock condition.")
    diagnostic = PermissibleValue(
        text="diagnostic",
        description="A signal providing diagnostic or debugging information about a device.")

    _defn = EnumDefinition(
        name="SignalRoleEnum",
        description="Controlled vocabulary for the semantic role of a signal within a capability.",
    )

class DeviceDomainEnum(EnumDefinitionImpl):
    """
    High-level device domain for a control profile family. Intentionally kept small; ADD new values here as the NARAD
    schema evolves.
    """
    Magnet = PermissibleValue(
        text="Magnet",
        description="Magnet devices: dipoles, quadrupoles, correctors, solenoids.")
    Instrument = PermissibleValue(
        text="Instrument",
        description="Beam diagnostic instruments: BPMs, screens, halos, viewers, etc.")
    RFCavity = PermissibleValue(
        text="RFCavity",
        description="RF cavity and RF-related devices.")

    _defn = EnumDefinition(
        name="DeviceDomainEnum",
        description="""High-level device domain for a control profile family. Intentionally kept small;  ADD new values here as the NARAD schema evolves.""",
    )

class RelationshipTypeEnum(EnumDefinitionImpl):
    """
    Allowed relationship types in the NARAD graph projection; each corresponds to an RO (Relation Ontology)-inspired
    directed edge.
    """
    has_shared_capability = PermissibleValue(
        text="has_shared_capability",
        description="""A profile family has a shared capability available to all its member profiles. Analogous to ro:has_part for capability composition.""")
    has_type_profile = PermissibleValue(
        text="has_type_profile",
        description="A profile family has a device-type profile (e.g. Quadrupole, BPM).")
    inherits_capability = PermissibleValue(
        text="inherits_capability",
        description="""A type-specific profile inherits a named shared capability from its family. Sub-relation of has_shared_capability.""")
    has_type_specific_capability = PermissibleValue(
        text="has_type_specific_capability",
        description="A type profile has a locally-declared type-specific capability.")
    has_signal = PermissibleValue(
        text="has_signal",
        description="A capability has a semantic signal (EPICS PV or equivalent). Broad mapping to sosa:hasResult.")
    implemented_by = PermissibleValue(
        text="implemented_by",
        description="A semantic signal or capability is implemented by a concrete facility binding.")
    binds_to = PermissibleValue(
        text="binds_to",
        description="A PV signal binding is bound to a physical beamline element.")
    located_in = PermissibleValue(
        text="located_in",
        description="A element is contained in an element.")
    controlled_by = PermissibleValue(
        text="controlled_by",
        description="An entity is controlled by a control system element.")
    before = PermissibleValue(
        text="before",
        description="A beamline element is upstream of another in the beam path.")
    after = PermissibleValue(
        text="after",
        description="A beamline element is downstream of another in the beam path.")

    _defn = EnumDefinition(
        name="RelationshipTypeEnum",
        description="""Allowed relationship types in the NARAD graph projection; each corresponds to an RO (Relation Ontology)-inspired directed edge.""",
    )

class NodeTypeEnum(EnumDefinitionImpl):
    """
    Node types in the NARAD graph projection; used as domain/range values for Relationship.
    """
    Device = PermissibleValue(
        text="Device",
        description="A physical beamline element (BeamlineElement).")
    CapabilityFamily = PermissibleValue(
        text="CapabilityFamily",
        description="A control profile family (ControlProfileFamily).")
    Profile = PermissibleValue(
        text="Profile",
        description="A device-type capability profile (CapabilityProfile).")
    Capability = PermissibleValue(
        text="Capability",
        description="A shared capability grouping signals.")
    TypeSpecificCapability = PermissibleValue(
        text="TypeSpecificCapability",
        description="A profile-local type-specific capability.")
    Signal = PermissibleValue(
        text="Signal",
        description="An individual semantic signal (EPICS PV or equivalent).")
    Facility = PermissibleValue(
        text="Facility",
        description="A physical accelerator facility.")
    ControlSystem = PermissibleValue(
        text="ControlSystem",
        description="The control system (e.g. EPICS) managing device PVs.")
    SignalBinding = PermissibleValue(
        text="SignalBinding",
        description="A concrete facility-specific PV binding for a semantic signal.")

    _defn = EnumDefinition(
        name="NodeTypeEnum",
        description="Node types in the NARAD graph projection; used as domain/range values for Relationship.",
    )

class IdentifierTypeEnum(EnumDefinitionImpl):
    """
    Allowed identifier types for facilities and other entities.
    """
    doi = PermissibleValue(
        text="doi",
        description="Digital Object Identifier (DOI).")
    ark = PermissibleValue(
        text="ark",
        description="Archival Resource Key (ARK).")
    handle = PermissibleValue(
        text="handle",
        description="Handle System identifier.")
    url = PermissibleValue(
        text="url",
        description="Uniform Resource Locator (URL).")
    local = PermissibleValue(
        text="local",
        description="Local identifier unique within a specific context or namespace.")
    other = PermissibleValue(
        text="other",
        description="Any other type of identifier not covered by the above categories.")

    _defn = EnumDefinition(
        name="IdentifierTypeEnum",
        description="Allowed identifier types for facilities and other entities.",
    )

# Slots
class slots:
    pass

slots.beamlines = Slot(uri=NARAD.beamlines, name="beamlines", curie=NARAD.curie('beamlines'),
                   model_uri=NARAD.beamlines, domain=None, range=Optional[Union[dict[Union[str, BeamlineBeamlineName], Union[dict, Beamline]], list[Union[dict, Beamline]]]])

slots.elements = Slot(uri=NARAD.elements, name="elements", curie=NARAD.curie('elements'),
                   model_uri=NARAD.elements, domain=None, range=Optional[Union[dict[Union[str, BeamlineElementName], Union[dict, BeamlineElement]], list[Union[dict, BeamlineElement]]]])

slots.narad = Slot(uri=NARAD['narad_narad/narad'], name="narad", curie=NARAD.curie('narad_narad/narad'),
                   model_uri=NARAD.narad, domain=None, range=Optional[Union[dict, NaradConfig]])

slots.schema_version = Slot(uri=NARAD['narad_narad/schema_version'], name="schema_version", curie=NARAD.curie('narad_narad/schema_version'),
                   model_uri=NARAD.schema_version, domain=None, range=Optional[str])

slots.intent = Slot(uri=NARAD['narad_narad/intent'], name="intent", curie=NARAD.curie('narad_narad/intent'),
                   model_uri=NARAD.intent, domain=None, range=Optional[str])

slots.facility = Slot(uri=NARAD['narad_narad/facility'], name="facility", curie=NARAD.curie('narad_narad/facility'),
                   model_uri=NARAD.facility, domain=None, range=Optional[str])

slots.control_system = Slot(uri=NARAD['narad_narad/control_system'], name="control_system", curie=NARAD.curie('narad_narad/control_system'),
                   model_uri=NARAD.control_system, domain=None, range=Optional[str])

slots.naming_convention = Slot(uri=NARAD['narad_narad/naming_convention'], name="naming_convention", curie=NARAD.curie('narad_narad/naming_convention'),
                   model_uri=NARAD.naming_convention, domain=None, range=Optional[str])

slots.capability_layer = Slot(uri=NARAD['narad_narad/capability_layer'], name="capability_layer", curie=NARAD.curie('narad_narad/capability_layer'),
                   model_uri=NARAD.capability_layer, domain=None, range=Optional[Union[dict, CapabilityLayer]])

slots.profiles = Slot(uri=NARAD['narad_narad/profiles'], name="profiles", curie=NARAD.curie('narad_narad/profiles'),
                   model_uri=NARAD.profiles, domain=None, range=Optional[Union[dict[Union[str, ControlProfileFamilyName], Union[dict, ControlProfileFamily]], list[Union[dict, ControlProfileFamily]]]])

slots.id = Slot(uri=NARAD['narad_narad/id'], name="id", curie=NARAD.curie('narad_narad/id'),
                   model_uri=NARAD.id, domain=None, range=URIRef)

slots.name = Slot(uri=NARAD['narad_narad/name'], name="name", curie=NARAD.curie('narad_narad/name'),
                   model_uri=NARAD.name, domain=None, range=URIRef)

slots.description = Slot(uri=NARAD['narad_narad/description'], name="description", curie=NARAD.curie('narad_narad/description'),
                   model_uri=NARAD.description, domain=None, range=Optional[str])

slots.capability_class = Slot(uri=NARAD['narad_narad/capability_class'], name="capability_class", curie=NARAD.curie('narad_narad/capability_class'),
                   model_uri=NARAD.capability_class, domain=None, range=Optional[str])

slots.kind = Slot(uri=NARAD['narad_narad/kind'], name="kind", curie=NARAD.curie('narad_narad/kind'),
                   model_uri=NARAD.kind, domain=None, range=Optional[str])

slots.device_type = Slot(uri=NARAD['narad_narad/device_type'], name="device_type", curie=NARAD.curie('narad_narad/device_type'),
                   model_uri=NARAD.device_type, domain=None, range=Optional[Union[str, "ElementKindEnum"]])

slots.class_curie = Slot(uri=NARAD['narad_narad/class_curie'], name="class_curie", curie=NARAD.curie('narad_narad/class_curie'),
                   model_uri=NARAD.class_curie, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.role = Slot(uri=NARAD['narad_narad/role'], name="role", curie=NARAD.curie('narad_narad/role'),
                   model_uri=NARAD.role, domain=None, range=Optional[Union[str, "SignalRoleEnum"]])

slots.data_type = Slot(uri=NARAD['narad_narad/data_type'], name="data_type", curie=NARAD.curie('narad_narad/data_type'),
                   model_uri=NARAD.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.units = Slot(uri=NARAD['narad_narad/units'], name="units", curie=NARAD.curie('narad_narad/units'),
                   model_uri=NARAD.units, domain=None, range=Optional[str])

slots.units_uri = Slot(uri=NARAD['narad_narad/units_uri'], name="units_uri", curie=NARAD.curie('narad_narad/units_uri'),
                   model_uri=NARAD.units_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.signals = Slot(uri=NARAD['narad_narad/signals'], name="signals", curie=NARAD.curie('narad_narad/signals'),
                   model_uri=NARAD.signals, domain=None, range=Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]])

slots.shared_capabilities = Slot(uri=NARAD['narad_narad/shared_capabilities'], name="shared_capabilities", curie=NARAD.curie('narad_narad/shared_capabilities'),
                   model_uri=NARAD.shared_capabilities, domain=None, range=Optional[Union[dict[Union[str, CapabilityName], Union[dict, Capability]], list[Union[dict, Capability]]]])

slots.inherits_shared_capabilities = Slot(uri=NARAD['narad_narad/inherits_shared_capabilities'], name="inherits_shared_capabilities", curie=NARAD.curie('narad_narad/inherits_shared_capabilities'),
                   model_uri=NARAD.inherits_shared_capabilities, domain=None, range=Optional[Union[Union[str, CapabilityName], list[Union[str, CapabilityName]]]])

slots.type_specific_capabilities = Slot(uri=NARAD['narad_narad/type_specific_capabilities'], name="type_specific_capabilities", curie=NARAD.curie('narad_narad/type_specific_capabilities'),
                   model_uri=NARAD.type_specific_capabilities, domain=None, range=Optional[Union[dict[Union[str, TypeSpecificCapabilityId], Union[dict, TypeSpecificCapability]], list[Union[dict, TypeSpecificCapability]]]])

slots.type_profiles = Slot(uri=NARAD['narad_narad/type_profiles'], name="type_profiles", curie=NARAD.curie('narad_narad/type_profiles'),
                   model_uri=NARAD.type_profiles, domain=None, range=Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]])

slots.device_domain = Slot(uri=NARAD['narad_narad/device_domain'], name="device_domain", curie=NARAD.curie('narad_narad/device_domain'),
                   model_uri=NARAD.device_domain, domain=None, range=Optional[Union[str, "DeviceDomainEnum"]])

slots.is_abstract = Slot(uri=NARAD['narad_narad/is_abstract'], name="is_abstract", curie=NARAD.curie('narad_narad/is_abstract'),
                   model_uri=NARAD.is_abstract, domain=None, range=Optional[Union[bool, Bool]])

slots.default_graph_projection = Slot(uri=NARAD['narad_narad/default_graph_projection'], name="default_graph_projection", curie=NARAD.curie('narad_narad/default_graph_projection'),
                   model_uri=NARAD.default_graph_projection, domain=None, range=Optional[Union[dict, GraphProjection]])

slots.graph_projection = Slot(uri=NARAD['narad_narad/graph_projection'], name="graph_projection", curie=NARAD.curie('narad_narad/graph_projection'),
                   model_uri=NARAD.graph_projection, domain=None, range=Optional[Union[dict, GraphProjection]])

slots.node_labels = Slot(uri=NARAD['narad_narad/node_labels'], name="node_labels", curie=NARAD.curie('narad_narad/node_labels'),
                   model_uri=NARAD.node_labels, domain=None, range=Optional[Union[dict, NodeLabels]])

slots.capability_family = Slot(uri=NARAD['narad_narad/capability_family'], name="capability_family", curie=NARAD.curie('narad_narad/capability_family'),
                   model_uri=NARAD.capability_family, domain=None, range=Optional[str])

slots.profile = Slot(uri=NARAD['narad_narad/profile'], name="profile", curie=NARAD.curie('narad_narad/profile'),
                   model_uri=NARAD.profile, domain=None, range=Optional[str])

slots.capability = Slot(uri=NARAD['narad_narad/capability'], name="capability", curie=NARAD.curie('narad_narad/capability'),
                   model_uri=NARAD.capability, domain=None, range=Optional[str])

slots.signal = Slot(uri=NARAD['narad_narad/signal'], name="signal", curie=NARAD.curie('narad_narad/signal'),
                   model_uri=NARAD.signal, domain=None, range=Optional[str])

slots.relationships = Slot(uri=NARAD['narad_narad/relationships'], name="relationships", curie=NARAD.curie('narad_narad/relationships'),
                   model_uri=NARAD.relationships, domain=None, range=Optional[Union[dict[Union[str, RelationshipId], Union[dict, Relationship]], list[Union[dict, Relationship]]]])

slots.label = Slot(uri=NARAD['narad_narad/label'], name="label", curie=NARAD.curie('narad_narad/label'),
                   model_uri=NARAD.label, domain=None, range=Optional[str])

slots.domain = Slot(uri=NARAD['narad_narad/domain'], name="domain", curie=NARAD.curie('narad_narad/domain'),
                   model_uri=NARAD.domain, domain=None, range=Optional[Union[str, "NodeTypeEnum"]])

slots.range = Slot(uri=NARAD['narad_narad/range'], name="range", curie=NARAD.curie('narad_narad/range'),
                   model_uri=NARAD.range, domain=None, range=Optional[Union[str, "NodeTypeEnum"]])

slots.subproperty_of = Slot(uri=NARAD['narad_narad/subproperty_of'], name="subproperty_of", curie=NARAD.curie('narad_narad/subproperty_of'),
                   model_uri=NARAD.subproperty_of, domain=None, range=Optional[Union[Union[str, RelationshipId], list[Union[str, RelationshipId]]]])

slots.inverse_of = Slot(uri=NARAD['narad_narad/inverse_of'], name="inverse_of", curie=NARAD.curie('narad_narad/inverse_of'),
                   model_uri=NARAD.inverse_of, domain=None, range=Optional[Union[str, RelationshipId]])

slots.symmetric = Slot(uri=NARAD['narad_narad/symmetric'], name="symmetric", curie=NARAD.curie('narad_narad/symmetric'),
                   model_uri=NARAD.symmetric, domain=None, range=Optional[Union[bool, Bool]])

slots.transitive = Slot(uri=NARAD['narad_narad/transitive'], name="transitive", curie=NARAD.curie('narad_narad/transitive'),
                   model_uri=NARAD.transitive, domain=None, range=Optional[Union[bool, Bool]])

slots.asymmetric = Slot(uri=NARAD['narad_narad/asymmetric'], name="asymmetric", curie=NARAD.curie('narad_narad/asymmetric'),
                   model_uri=NARAD.asymmetric, domain=None, range=Optional[Union[bool, Bool]])

slots.irreflexive = Slot(uri=NARAD['narad_narad/irreflexive'], name="irreflexive", curie=NARAD.curie('narad_narad/irreflexive'),
                   model_uri=NARAD.irreflexive, domain=None, range=Optional[Union[bool, Bool]])

slots.signal_layer = Slot(uri=NARAD['narad_narad/signal_layer'], name="signal_layer", curie=NARAD.curie('narad_narad/signal_layer'),
                   model_uri=NARAD.signal_layer, domain=None, range=Optional[Union[dict, SignalLayer]])

slots.facilities = Slot(uri=NARAD['narad_narad/facilities'], name="facilities", curie=NARAD.curie('narad_narad/facilities'),
                   model_uri=NARAD.facilities, domain=None, range=Optional[Union[dict[Union[str, FacilityName], Union[dict, Facility]], list[Union[dict, Facility]]]])

slots.signal_definitions = Slot(uri=NARAD['narad_narad/signal_definitions'], name="signal_definitions", curie=NARAD.curie('narad_narad/signal_definitions'),
                   model_uri=NARAD.signal_definitions, domain=None, range=Optional[Union[dict, SignalDefinitions]])

slots.epics_suffix = Slot(uri=NARAD['narad_narad/epics_suffix'], name="epics_suffix", curie=NARAD.curie('narad_narad/epics_suffix'),
                   model_uri=NARAD.epics_suffix, domain=None, range=Optional[str])

slots.type_signal_sets = Slot(uri=NARAD['narad_narad/type_signal_sets'], name="type_signal_sets", curie=NARAD.curie('narad_narad/type_signal_sets'),
                   model_uri=NARAD.type_signal_sets, domain=None, range=Optional[Union[dict[Union[str, DeviceTypeSignalSetName], Union[dict, DeviceTypeSignalSet]], list[Union[dict, DeviceTypeSignalSet]]]])

slots.signal_bindings = Slot(uri=NARAD['narad_narad/signal_bindings'], name="signal_bindings", curie=NARAD.curie('narad_narad/signal_bindings'),
                   model_uri=NARAD.signal_bindings, domain=None, range=Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.capability_profile_family = Slot(uri=NARAD['narad_narad/capability_profile_family'], name="capability_profile_family", curie=NARAD.curie('narad_narad/capability_profile_family'),
                   model_uri=NARAD.capability_profile_family, domain=None, range=Optional[Union[str, ControlProfileFamilyName]])

slots.capability_profile = Slot(uri=NARAD['narad_narad/capability_profile'], name="capability_profile", curie=NARAD.curie('narad_narad/capability_profile'),
                   model_uri=NARAD.capability_profile, domain=None, range=Optional[Union[str, CapabilityProfileName]])

slots.identifier = Slot(uri=NARAD['narad_narad/identifier'], name="identifier", curie=NARAD.curie('narad_narad/identifier'),
                   model_uri=NARAD.identifier, domain=None, range=Optional[Union[Union[dict, Identifier], list[Union[dict, Identifier]]]])

slots.identifier_type = Slot(uri=NARAD['narad_narad/identifier_type'], name="identifier_type", curie=NARAD.curie('narad_narad/identifier_type'),
                   model_uri=NARAD.identifier_type, domain=None, range=Optional[Union[str, "IdentifierTypeEnum"]])

slots.identifier_value = Slot(uri=NARAD['narad_narad/identifier_value'], name="identifier_value", curie=NARAD.curie('narad_narad/identifier_value'),
                   model_uri=NARAD.identifier_value, domain=None, range=Optional[str])

slots.beamline_name = Slot(uri=NARAD['beamline/beamline_name'], name="beamline_name", curie=NARAD.curie('beamline/beamline_name'),
                   model_uri=NARAD.beamline_name, domain=None, range=URIRef)

slots.line = Slot(uri=NARAD['beamline/line'], name="line", curie=NARAD.curie('beamline/line'),
                   model_uri=NARAD.line, domain=None, range=Optional[Union[str, list[str]]])

slots.length = Slot(uri=NARAD['elements/length'], name="length", curie=NARAD.curie('elements/length'),
                   model_uri=NARAD.length, domain=None, range=Optional[float])

slots.RFP = Slot(uri=NARAD['elements/RFP'], name="RFP", curie=NARAD.curie('elements/RFP'),
                   model_uri=NARAD.RFP, domain=None, range=Optional[Union[dict, RFParams]])

slots.BendP = Slot(uri=NARAD['elements/BendP'], name="BendP", curie=NARAD.curie('elements/BendP'),
                   model_uri=NARAD.BendP, domain=None, range=Optional[Union[dict, BendParams]])

slots.MagneticMultipoleP = Slot(uri=NARAD['elements/MagneticMultipoleP'], name="MagneticMultipoleP", curie=NARAD.curie('elements/MagneticMultipoleP'),
                   model_uri=NARAD.MagneticMultipoleP, domain=None, range=Optional[Union[dict, MagneticMultipoleParams]])

slots.SolenoidP = Slot(uri=NARAD['elements/SolenoidP'], name="SolenoidP", curie=NARAD.curie('elements/SolenoidP'),
                   model_uri=NARAD.SolenoidP, domain=None, range=Optional[Union[dict, SolenoidParams]])

slots.magnet_semantics = Slot(uri=NARAD['elements/magnet_semantics'], name="magnet_semantics", curie=NARAD.curie('elements/magnet_semantics'),
                   model_uri=NARAD.magnet_semantics, domain=None, range=Optional[str])

slots.instrument_semantics = Slot(uri=NARAD['elements/instrument_semantics'], name="instrument_semantics", curie=NARAD.curie('elements/instrument_semantics'),
                   model_uri=NARAD.instrument_semantics, domain=None, range=Optional[str])

slots.cavity_semantics = Slot(uri=NARAD['elements/cavity_semantics'], name="cavity_semantics", curie=NARAD.curie('elements/cavity_semantics'),
                   model_uri=NARAD.cavity_semantics, domain=None, range=Optional[str])

slots.pv = Slot(uri=NARAD['elements/pv'], name="pv", curie=NARAD.curie('elements/pv'),
                   model_uri=NARAD.pv, domain=None, range=Optional[str])

slots.frequency = Slot(uri=NARAD['elements/frequency'], name="frequency", curie=NARAD.curie('elements/frequency'),
                   model_uri=NARAD.frequency, domain=None, range=Optional[float])

slots.voltage = Slot(uri=NARAD['elements/voltage'], name="voltage", curie=NARAD.curie('elements/voltage'),
                   model_uri=NARAD.voltage, domain=None, range=Optional[float])

slots.phase = Slot(uri=NARAD['elements/phase'], name="phase", curie=NARAD.curie('elements/phase'),
                   model_uri=NARAD.phase, domain=None, range=Optional[float])

slots.angle_ref = Slot(uri=NARAD['elements/angle_ref'], name="angle_ref", curie=NARAD.curie('elements/angle_ref'),
                   model_uri=NARAD.angle_ref, domain=None, range=Optional[float])

slots.e1 = Slot(uri=NARAD['elements/e1'], name="e1", curie=NARAD.curie('elements/e1'),
                   model_uri=NARAD.e1, domain=None, range=Optional[float])

slots.e2 = Slot(uri=NARAD['elements/e2'], name="e2", curie=NARAD.curie('elements/e2'),
                   model_uri=NARAD.e2, domain=None, range=Optional[float])

slots.Kn1 = Slot(uri=NARAD['elements/Kn1'], name="Kn1", curie=NARAD.curie('elements/Kn1'),
                   model_uri=NARAD.Kn1, domain=None, range=Optional[float])

slots.Ksol = Slot(uri=NARAD['elements/Ksol'], name="Ksol", curie=NARAD.curie('elements/Ksol'),
                   model_uri=NARAD.Ksol, domain=None, range=Optional[float])

slots.facility_params = Slot(uri=NARAD['facility_params/facility_params'], name="facility_params", curie=NARAD.curie('facility_params/facility_params'),
                   model_uri=NARAD.facility_params, domain=None, range=Optional[Union[dict, FacilityParams]])

slots.facility_element_type = Slot(uri=NARAD['facility_params/facility_element_type'], name="facility_element_type", curie=NARAD.curie('facility_params/facility_element_type'),
                   model_uri=NARAD.facility_element_type, domain=None, range=Optional[str])

slots.modeled_as = Slot(uri=NARAD['facility_params/modeled_as'], name="modeled_as", curie=NARAD.curie('facility_params/modeled_as'),
                   model_uri=NARAD.modeled_as, domain=None, range=Optional[str])

slots.properties = Slot(uri=NARAD['facility_params/properties'], name="properties", curie=NARAD.curie('facility_params/properties'),
                   model_uri=NARAD.properties, domain=None, range=Optional[Union[dict, AnyValue]])

slots.range_target = Slot(uri=NARAD.range_target, name="range_target", curie=NARAD.curie('range_target'),
                   model_uri=NARAD.range_target, domain=None, range=str)

slots.Relationship_id = Slot(uri=NARAD['narad_narad/id'], name="Relationship_id", curie=NARAD.curie('narad_narad/id'),
                   model_uri=NARAD.Relationship_id, domain=Relationship, range=Union[str, RelationshipId])

slots.Relationship_range = Slot(uri=NARAD['narad_narad/range'], name="Relationship_range", curie=NARAD.curie('narad_narad/range'),
                   model_uri=NARAD.Relationship_range, domain=Relationship, range=Union[str, "NodeTypeEnum"])

slots.Relationship_range_target = Slot(uri=NARAD.range_target, name="Relationship_range_target", curie=NARAD.curie('range_target'),
                   model_uri=NARAD.Relationship_range_target, domain=Relationship, range=str)

slots.ControlProfileFamily_graph_projection = Slot(uri=NARAD['narad_narad/graph_projection'], name="ControlProfileFamily_graph_projection", curie=NARAD.curie('narad_narad/graph_projection'),
                   model_uri=NARAD.ControlProfileFamily_graph_projection, domain=ControlProfileFamily, range=Optional[Union[dict, GraphProjection]])

slots.Beamline_beamline_name = Slot(uri=NARAD['beamline/beamline_name'], name="Beamline_beamline_name", curie=NARAD.curie('beamline/beamline_name'),
                   model_uri=NARAD.Beamline_beamline_name, domain=Beamline, range=Union[str, BeamlineBeamlineName])

slots.BeamlineElement_name = Slot(uri=NARAD['narad_narad/name'], name="BeamlineElement_name", curie=NARAD.curie('narad_narad/name'),
                   model_uri=NARAD.BeamlineElement_name, domain=BeamlineElement, range=Union[str, BeamlineElementName])

slots.BeamlineElement_kind = Slot(uri=NARAD['narad_narad/kind'], name="BeamlineElement_kind", curie=NARAD.curie('narad_narad/kind'),
                   model_uri=NARAD.BeamlineElement_kind, domain=BeamlineElement, range=Optional[Union[str, "ElementKindEnum"]])

slots.BeamlineElement_narad = Slot(uri=NARAD['narad_narad/narad'], name="BeamlineElement_narad", curie=NARAD.curie('narad_narad/narad'),
                   model_uri=NARAD.BeamlineElement_narad, domain=BeamlineElement, range=Optional[Union[dict, "ElementNaradRef"]])

slots.ElementNaradRef_signal_bindings = Slot(uri=NARAD['narad_narad/signal_bindings'], name="ElementNaradRef_signal_bindings", curie=NARAD.curie('narad_narad/signal_bindings'),
                   model_uri=NARAD.ElementNaradRef_signal_bindings, domain=ElementNaradRef, range=Optional[Union[dict[Union[str, PVBindingName], Union[dict, "PVBinding"]], list[Union[dict, "PVBinding"]]]])
