# Auto generated from narad_system.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-07T13:24:23
# Schema: narad-system-schema
#
# id: https://w3id.org/narad_linkml/schema/narad/system
# description: LinkML schema for representing facility control-system structures using NARAD domain classes aligned with SSN, SSN-System, and SOSA.
#   Class hierarchy:
#     - System (ssn:System) — base for all physical/logical entities
#       - Facility — top-level facility (e.g. UITF); ssn-system:hasSubSystem → ControlSystem
#       - ControlSystem — the EPICS or other control system
#       - Magnet (ssn:System) — generic powered magnet
#         - Quadrupole, Corrector, Dipole, Solenoid
#       - Instrument (ssn:System) — generic beam diagnostic
#         - BPM
#       - RF_System (ssn:System)
#         - RFCavity
#
#   Capability hierarchy (ssn-system:SystemCapability):
#     - SystemCapability — base; linked from System via ssn-system:hasSystemCapability
#       - MagnetCapability → QuadrupoleCapability, CorrectorCapability, DipoleCapability
#       - InstrumentCapability → BPMCapability
#       - CavityGradientCapability
#
#   Signal alignment:
#     - Signal (broad: sosa:Property / ssn:Property) — abstract base
#       - ObservableSignal (exact: sosa:ObservableProperty) — readback, status
#       - ActuatableSignal (exact: sosa:ActuatableProperty) — setpoints, limits
#
#   SignalBinding alignment:
#     - SignalBinding (exact sosa:Procedure) — facility-specific PV binding
#       ssn:forProperty → Signal
#       narad:isInstanceOf → rdf:type of the capability class
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NARAD = CurieNamespace('narad', 'https://w3id.org/narad_linkml/schema/narad/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/ncit.owl')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SI_UNIT = CurieNamespace('si-unit', 'http://qudt.org/vocab/unit/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
DEFAULT_ = NARAD


# Types

# Class references
class NamedThingName(extended_str):
    pass


class ControlProfileFamilyName(NamedThingName):
    pass


class CapabilityName(NamedThingName):
    pass


class TypeSpecificCapabilityName(CapabilityName):
    pass


class CapabilityProfileName(NamedThingName):
    pass


class FacilityConfigName(NamedThingName):
    pass


class BeamlineName(NamedThingName):
    pass


class BeamlineElementName(NamedThingName):
    pass


class SystemName(NamedThingName):
    pass


class ControlSystemName(SystemName):
    pass


class MagnetName(SystemName):
    pass


class QuadrupoleName(MagnetName):
    pass


class CorrectorName(MagnetName):
    pass


class DipoleName(MagnetName):
    pass


class SolenoidName(MagnetName):
    pass


class InstrumentName(SystemName):
    pass


class BPMName(InstrumentName):
    pass


class RFCavityName(SystemName):
    pass


class MarkerName(SystemName):
    pass


class SystemCapabilityName(NamedThingName):
    pass


class MagnetCapabilityName(SystemCapabilityName):
    pass


class QuadrupoleCapabilityName(MagnetCapabilityName):
    pass


class CorrectorCapabilityName(MagnetCapabilityName):
    pass


class DipoleCapabilityName(MagnetCapabilityName):
    pass


class SolenoidCapabilityName(MagnetCapabilityName):
    pass


class InstrumentCapabilityName(SystemCapabilityName):
    pass


class BPMCapabilityName(InstrumentCapabilityName):
    pass


class CavityGradientCapabilityName(SystemCapabilityName):
    pass


class SignalName(NamedThingName):
    pass


class ObservableSignalName(SignalName):
    pass


class ActuatableSignalName(SignalName):
    pass


class InstanceSignalBindingName(NamedThingName):
    pass


class ElementParamSetName(NamedThingName):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    Abstract base class providing identity and human-readable metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["NamedThing"]
    class_class_curie: ClassVar[str] = "narad:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NARAD.NamedThing

    name: Union[str, NamedThingName] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, NamedThingName):
            self.name = NamedThingName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


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

    narad_config: Optional[Union[dict, "NaradConfig"]] = None
    beamlines: Optional[Union[dict[Union[str, BeamlineName], Union[dict, "Beamline"]], list[Union[dict, "Beamline"]]]] = empty_dict()
    elements: Optional[Union[dict[Union[str, BeamlineElementName], Union[dict, "BeamlineElement"]], list[Union[dict, "BeamlineElement"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.narad_config is not None and not isinstance(self.narad_config, NaradConfig):
            self.narad_config = NaradConfig(**as_dict(self.narad_config))

        self._normalize_inlined_as_dict(slot_name="beamlines", slot_type=Beamline, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="elements", slot_type=BeamlineElement, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NaradConfig(YAMLRoot):
    """
    NARAD configuration block: capability layer + signal layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["NaradConfig"]
    class_class_curie: ClassVar[str] = "narad:NaradConfig"
    class_name: ClassVar[str] = "NaradConfig"
    class_model_uri: ClassVar[URIRef] = NARAD.NaradConfig

    schema_version: str = None
    capability_layer: Union[dict, "CapabilityLayer"] = None
    facility: str = None
    control_system: str = None
    signal_layer: Union[dict, "SignalLayer"] = None
    intent: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.schema_version):
            self.MissingRequiredField("schema_version")
        if not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self._is_empty(self.capability_layer):
            self.MissingRequiredField("capability_layer")
        if not isinstance(self.capability_layer, CapabilityLayer):
            self.capability_layer = CapabilityLayer(**as_dict(self.capability_layer))

        if self._is_empty(self.facility):
            self.MissingRequiredField("facility")
        if not isinstance(self.facility, str):
            self.facility = str(self.facility)

        if self._is_empty(self.control_system):
            self.MissingRequiredField("control_system")
        if not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self._is_empty(self.signal_layer):
            self.MissingRequiredField("signal_layer")
        if not isinstance(self.signal_layer, SignalLayer):
            self.signal_layer = SignalLayer(**as_dict(self.signal_layer))

        if self.intent is not None and not isinstance(self.intent, str):
            self.intent = str(self.intent)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityLayer(YAMLRoot):
    """
    Capability-layer container for control profile families.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["CapabilityLayer"]
    class_class_curie: ClassVar[str] = "narad:CapabilityLayer"
    class_name: ClassVar[str] = "CapabilityLayer"
    class_model_uri: ClassVar[URIRef] = NARAD.CapabilityLayer

    profiles: Optional[Union[dict[Union[str, ControlProfileFamilyName], Union[dict, "ControlProfileFamily"]], list[Union[dict, "ControlProfileFamily"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="profiles", slot_type=ControlProfileFamily, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlProfileFamily(NamedThing):
    """
    A reusable family of control profiles sharing common semantics and structure (e.g.
    MagnetCurrentControlProfileFamily).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ControlProfileFamily"]
    class_class_curie: ClassVar[str] = "narad:ControlProfileFamily"
    class_name: ClassVar[str] = "ControlProfileFamily"
    class_model_uri: ClassVar[URIRef] = NARAD.ControlProfileFamily

    name: Union[str, ControlProfileFamilyName] = None
    device_domain: Optional[Union[str, "DeviceDomainEnum"]] = None
    shared_capabilities: Optional[Union[dict[Union[str, CapabilityName], Union[dict, "Capability"]], list[Union[dict, "Capability"]]]] = empty_dict()
    type_profiles: Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, "CapabilityProfile"]], list[Union[dict, "CapabilityProfile"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlProfileFamilyName):
            self.name = ControlProfileFamilyName(self.name)

        if self.device_domain is not None and not isinstance(self.device_domain, DeviceDomainEnum):
            self.device_domain = DeviceDomainEnum(self.device_domain)

        self._normalize_inlined_as_dict(slot_name="shared_capabilities", slot_type=Capability, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="type_profiles", slot_type=CapabilityProfile, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Capability(NamedThing):
    """
    A named, shared grouping of semantically related signals for a control aspect (e.g.
    MagnetCurrentControlCapability).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Capability"]
    class_class_curie: ClassVar[str] = "narad:Capability"
    class_name: ClassVar[str] = "Capability"
    class_model_uri: ClassVar[URIRef] = NARAD.Capability

    name: Union[str, CapabilityName] = None
    signals: Optional[Union[dict[Union[str, SignalName], Union[dict, "Signal"]], list[Union[dict, "Signal"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CapabilityName):
            self.name = CapabilityName(self.name)

        self._normalize_inlined_as_dict(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypeSpecificCapability(Capability):
    """
    An inline capability declared within a device-type profile that extends a generic shared Capability. The explicit
    link to the shared Capability being extended is given by inherits_from. Adds type-specific signals on top of those
    already defined in the referenced shared Capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["TypeSpecificCapability"]
    class_class_curie: ClassVar[str] = "narad:TypeSpecificCapability"
    class_name: ClassVar[str] = "TypeSpecificCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.TypeSpecificCapability

    name: Union[str, TypeSpecificCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TypeSpecificCapabilityName):
            self.name = TypeSpecificCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityProfile(NamedThing):
    """
    A device-type profile that reuses shared capabilities and adds type-specific ones (e.g. QuadrupoleProfile).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["CapabilityProfile"]
    class_class_curie: ClassVar[str] = "narad:CapabilityProfile"
    class_name: ClassVar[str] = "CapabilityProfile"
    class_model_uri: ClassVar[URIRef] = NARAD.CapabilityProfile

    name: Union[str, CapabilityProfileName] = None
    device_type: Optional[Union[str, "ElementKindEnum"]] = None
    is_abstract: Optional[Union[bool, Bool]] = False
    inherits_shared_capabilities: Optional[Union[Union[str, CapabilityName], list[Union[str, CapabilityName]]]] = empty_list()
    type_specific_capabilities: Optional[Union[dict[Union[str, TypeSpecificCapabilityName], Union[dict, TypeSpecificCapability]], list[Union[dict, TypeSpecificCapability]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CapabilityProfileName):
            self.name = CapabilityProfileName(self.name)

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

        if self.is_abstract is not None and not isinstance(self.is_abstract, Bool):
            self.is_abstract = Bool(self.is_abstract)

        if not isinstance(self.inherits_shared_capabilities, list):
            self.inherits_shared_capabilities = [self.inherits_shared_capabilities] if self.inherits_shared_capabilities is not None else []
        self.inherits_shared_capabilities = [v if isinstance(v, CapabilityName) else CapabilityName(v) for v in self.inherits_shared_capabilities]

        self._normalize_inlined_as_dict(slot_name="type_specific_capabilities", slot_type=TypeSpecificCapability, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalLayer(YAMLRoot):
    """
    Signal-layer container for facility-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SignalLayer"]
    class_class_curie: ClassVar[str] = "narad:SignalLayer"
    class_name: ClassVar[str] = "SignalLayer"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalLayer

    facilities: Optional[Union[dict[Union[str, FacilityConfigName], Union[dict, "FacilityConfig"]], list[Union[dict, "FacilityConfig"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="facilities", slot_type=FacilityConfig, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FacilityConfig(NamedThing):
    """
    Facility-specific signal binding configuration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["FacilityConfig"]
    class_class_curie: ClassVar[str] = "narad:FacilityConfig"
    class_name: ClassVar[str] = "FacilityConfig"
    class_model_uri: ClassVar[URIRef] = NARAD.FacilityConfig

    name: Union[str, FacilityConfigName] = None
    facility_identifier: Optional[Union[Union[dict, "FacilityIdentifier"], list[Union[dict, "FacilityIdentifier"]]]] = empty_list()
    control_system: Optional[str] = None
    naming_convention: Optional[str] = None
    signal_definitions: Optional[Union[dict, "SignalDefinitions"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FacilityConfigName):
            self.name = FacilityConfigName(self.name)

        if not isinstance(self.facility_identifier, list):
            self.facility_identifier = [self.facility_identifier] if self.facility_identifier is not None else []
        self.facility_identifier = [v if isinstance(v, FacilityIdentifier) else FacilityIdentifier(**as_dict(v)) for v in self.facility_identifier]

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.naming_convention is not None and not isinstance(self.naming_convention, str):
            self.naming_convention = str(self.naming_convention)

        if self.signal_definitions is not None and not isinstance(self.signal_definitions, SignalDefinitions):
            self.signal_definitions = SignalDefinitions(**as_dict(self.signal_definitions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FacilityIdentifier(YAMLRoot):
    """
    A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["FacilityIdentifier"]
    class_class_curie: ClassVar[str] = "narad:FacilityIdentifier"
    class_name: ClassVar[str] = "FacilityIdentifier"
    class_model_uri: ClassVar[URIRef] = NARAD.FacilityIdentifier

    identifier_type: Optional[Union[str, "IdentifierTypeEnum"]] = None
    identifier_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.identifier_type is not None and not isinstance(self.identifier_type, IdentifierTypeEnum):
            self.identifier_type = IdentifierTypeEnum(self.identifier_type)

        if self.identifier_value is not None and not isinstance(self.identifier_value, str):
            self.identifier_value = str(self.identifier_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalDefinitions(YAMLRoot):
    """
    EPICS signal suffix templates keyed by device type or device domain. Domain-level keys (e.g. Magnet, RFCavity)
    cover signals shared across all types in that domain; device-type keys are type-specific.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SignalDefinitions"]
    class_class_curie: ClassVar[str] = "narad:SignalDefinitions"
    class_name: ClassVar[str] = "SignalDefinitions"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalDefinitions

    type_signal_sets: Optional[Union[dict, "TypeSignalSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type_signal_sets is not None and not isinstance(self.type_signal_sets, TypeSignalSet):
            self.type_signal_sets = TypeSignalSet(**as_dict(self.type_signal_sets))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalBinding(YAMLRoot):
    """
    A named EPICS suffix definition for one semantic signal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SignalBinding"]
    class_class_curie: ClassVar[str] = "narad:SignalBinding"
    class_name: ClassVar[str] = "SignalBinding"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalBinding

    description: Optional[str] = None
    control_system_suffix: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.control_system_suffix is not None and not isinstance(self.control_system_suffix, str):
            self.control_system_suffix = str(self.control_system_suffix)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypeSignalSet(YAMLRoot):
    """
    Explicit signal binding groups keyed by device domain or device type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["TypeSignalSet"]
    class_class_curie: ClassVar[str] = "narad:TypeSignalSet"
    class_name: ClassVar[str] = "TypeSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.TypeSignalSet

    magnet_signals: Optional[Union[dict, "MagnetSignalSet"]] = None
    quadrupole_signals: Optional[Union[dict, "QuadrupoleSignalSet"]] = None
    corrector_signals: Optional[Union[dict, "CorrectorSignalSet"]] = None
    dipole_signals: Optional[Union[dict, "DipoleSignalSet"]] = None
    bpm_signals: Optional[Union[dict, "BPMSignalSet"]] = None
    rfcavity_signals: Optional[Union[dict, "RFCavitySignalSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.magnet_signals is not None and not isinstance(self.magnet_signals, MagnetSignalSet):
            self.magnet_signals = MagnetSignalSet(**as_dict(self.magnet_signals))

        if self.quadrupole_signals is not None and not isinstance(self.quadrupole_signals, QuadrupoleSignalSet):
            self.quadrupole_signals = QuadrupoleSignalSet(**as_dict(self.quadrupole_signals))

        if self.corrector_signals is not None and not isinstance(self.corrector_signals, CorrectorSignalSet):
            self.corrector_signals = CorrectorSignalSet(**as_dict(self.corrector_signals))

        if self.dipole_signals is not None and not isinstance(self.dipole_signals, DipoleSignalSet):
            self.dipole_signals = DipoleSignalSet(**as_dict(self.dipole_signals))

        if self.bpm_signals is not None and not isinstance(self.bpm_signals, BPMSignalSet):
            self.bpm_signals = BPMSignalSet(**as_dict(self.bpm_signals))

        if self.rfcavity_signals is not None and not isinstance(self.rfcavity_signals, RFCavitySignalSet):
            self.rfcavity_signals = RFCavitySignalSet(**as_dict(self.rfcavity_signals))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MagnetSignalSet(YAMLRoot):
    """
    Shared magnet signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["MagnetSignalSet"]
    class_class_curie: ClassVar[str] = "narad:MagnetSignalSet"
    class_name: ClassVar[str] = "MagnetSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.MagnetSignalSet

    current_setpoint: Optional[Union[dict, SignalBinding]] = None
    current_readback: Optional[Union[dict, SignalBinding]] = None
    current_min: Optional[Union[dict, SignalBinding]] = None
    current_max: Optional[Union[dict, SignalBinding]] = None
    status: Optional[Union[dict, SignalBinding]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.current_setpoint is not None and not isinstance(self.current_setpoint, SignalBinding):
            self.current_setpoint = SignalBinding(**as_dict(self.current_setpoint))

        if self.current_readback is not None and not isinstance(self.current_readback, SignalBinding):
            self.current_readback = SignalBinding(**as_dict(self.current_readback))

        if self.current_min is not None and not isinstance(self.current_min, SignalBinding):
            self.current_min = SignalBinding(**as_dict(self.current_min))

        if self.current_max is not None and not isinstance(self.current_max, SignalBinding):
            self.current_max = SignalBinding(**as_dict(self.current_max))

        if self.status is not None and not isinstance(self.status, SignalBinding):
            self.status = SignalBinding(**as_dict(self.status))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuadrupoleSignalSet(YAMLRoot):
    """
    Quadrupole-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["QuadrupoleSignalSet"]
    class_class_curie: ClassVar[str] = "narad:QuadrupoleSignalSet"
    class_name: ClassVar[str] = "QuadrupoleSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.QuadrupoleSignalSet

    strength_setpoint: Optional[Union[dict, SignalBinding]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.strength_setpoint is not None and not isinstance(self.strength_setpoint, SignalBinding):
            self.strength_setpoint = SignalBinding(**as_dict(self.strength_setpoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectorSignalSet(YAMLRoot):
    """
    Corrector-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["CorrectorSignalSet"]
    class_class_curie: ClassVar[str] = "narad:CorrectorSignalSet"
    class_name: ClassVar[str] = "CorrectorSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.CorrectorSignalSet

    kick_setpoint: Optional[Union[dict, SignalBinding]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.kick_setpoint is not None and not isinstance(self.kick_setpoint, SignalBinding):
            self.kick_setpoint = SignalBinding(**as_dict(self.kick_setpoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DipoleSignalSet(YAMLRoot):
    """
    Dipole-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["DipoleSignalSet"]
    class_class_curie: ClassVar[str] = "narad:DipoleSignalSet"
    class_name: ClassVar[str] = "DipoleSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.DipoleSignalSet

    field_setpoint: Optional[Union[dict, SignalBinding]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.field_setpoint is not None and not isinstance(self.field_setpoint, SignalBinding):
            self.field_setpoint = SignalBinding(**as_dict(self.field_setpoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BPMSignalSet(YAMLRoot):
    """
    BPM-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BPMSignalSet"]
    class_class_curie: ClassVar[str] = "narad:BPMSignalSet"
    class_name: ClassVar[str] = "BPMSignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.BPMSignalSet

    horizontal_beam_position: Optional[Union[dict, SignalBinding]] = None
    vertical_beam_position: Optional[Union[dict, SignalBinding]] = None
    status: Optional[Union[dict, SignalBinding]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.horizontal_beam_position is not None and not isinstance(self.horizontal_beam_position, SignalBinding):
            self.horizontal_beam_position = SignalBinding(**as_dict(self.horizontal_beam_position))

        if self.vertical_beam_position is not None and not isinstance(self.vertical_beam_position, SignalBinding):
            self.vertical_beam_position = SignalBinding(**as_dict(self.vertical_beam_position))

        if self.status is not None and not isinstance(self.status, SignalBinding):
            self.status = SignalBinding(**as_dict(self.status))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RFCavitySignalSet(YAMLRoot):
    """
    RF cavity-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["RFCavitySignalSet"]
    class_class_curie: ClassVar[str] = "narad:RFCavitySignalSet"
    class_name: ClassVar[str] = "RFCavitySignalSet"
    class_model_uri: ClassVar[URIRef] = NARAD.RFCavitySignalSet

    gradient_setpoint: Optional[Union[dict, SignalBinding]] = None
    gradient_readback: Optional[Union[dict, SignalBinding]] = None
    status: Optional[Union[dict, SignalBinding]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.gradient_setpoint is not None and not isinstance(self.gradient_setpoint, SignalBinding):
            self.gradient_setpoint = SignalBinding(**as_dict(self.gradient_setpoint))

        if self.gradient_readback is not None and not isinstance(self.gradient_readback, SignalBinding):
            self.gradient_readback = SignalBinding(**as_dict(self.gradient_readback))

        if self.status is not None and not isinstance(self.status, SignalBinding):
            self.status = SignalBinding(**as_dict(self.status))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Beamline(NamedThing):
    """
    An ordered sequence of beamline elements defining a beam path.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Beamline"]
    class_class_curie: ClassVar[str] = "narad:Beamline"
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = NARAD.Beamline

    name: Union[str, BeamlineName] = None
    beamline_kind: Optional[str] = None
    line: Optional[Union[Union[str, BeamlineElementName], list[Union[str, BeamlineElementName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineName):
            self.name = BeamlineName(self.name)

        if self.beamline_kind is not None and not isinstance(self.beamline_kind, str):
            self.beamline_kind = str(self.beamline_kind)

        if not isinstance(self.line, list):
            self.line = [self.line] if self.line is not None else []
        self.line = [v if isinstance(v, BeamlineElementName) else BeamlineElementName(v) for v in self.line]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamlineElement(NamedThing):
    """
    A single element in a beamline with its kind and optional NARAD capability annotations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BeamlineElement"]
    class_class_curie: ClassVar[str] = "narad:BeamlineElement"
    class_name: ClassVar[str] = "BeamlineElement"
    class_model_uri: ClassVar[URIRef] = NARAD.BeamlineElement

    name: Union[str, BeamlineElementName] = None
    element_kind: Optional[Union[str, "ElementKindEnum"]] = None
    length: Optional[float] = None
    capability_profile_family: Optional[Union[str, ControlProfileFamilyName]] = None
    capability_profile: Optional[Union[str, CapabilityProfileName]] = None
    instance_signal_bindings: Optional[Union[dict[Union[str, InstanceSignalBindingName], Union[dict, "InstanceSignalBinding"]], list[Union[dict, "InstanceSignalBinding"]]]] = empty_dict()
    param_set: Optional[Union[dict[Union[str, ElementParamSetName], Union[dict, "ElementParamSet"]], list[Union[dict, "ElementParamSet"]]]] = empty_dict()
    facility_param_set: Optional[Union[dict, "FacilityParamSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineElementName):
            self.name = BeamlineElementName(self.name)

        if self.element_kind is not None and not isinstance(self.element_kind, ElementKindEnum):
            self.element_kind = ElementKindEnum(self.element_kind)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.capability_profile_family is not None and not isinstance(self.capability_profile_family, ControlProfileFamilyName):
            self.capability_profile_family = ControlProfileFamilyName(self.capability_profile_family)

        if self.capability_profile is not None and not isinstance(self.capability_profile, CapabilityProfileName):
            self.capability_profile = CapabilityProfileName(self.capability_profile)

        self._normalize_inlined_as_dict(slot_name="instance_signal_bindings", slot_type=InstanceSignalBinding, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="param_set", slot_type=ElementParamSet, key_name="name", keyed=True)

        if self.facility_param_set is not None and not isinstance(self.facility_param_set, FacilityParamSet):
            self.facility_param_set = FacilityParamSet(**as_dict(self.facility_param_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class System(NamedThing):
    """
    A physical, logical, or cyber-physical system involved in sensing, monitoring, control, or actuation. Broadly
    aligned to ssn:System.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["System"]
    class_class_curie: ClassVar[str] = "narad:System"
    class_name: ClassVar[str] = "System"
    class_model_uri: ClassVar[URIRef] = NARAD.System

    name: Union[str, SystemName] = None
    has_sub_system: Optional[Union[Union[str, SystemName], list[Union[str, SystemName]]]] = empty_list()
    has_system_capability: Optional[Union[Union[str, SystemCapabilityName], list[Union[str, SystemCapabilityName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SystemName):
            self.name = SystemName(self.name)

        if not isinstance(self.has_sub_system, list):
            self.has_sub_system = [self.has_sub_system] if self.has_sub_system is not None else []
        self.has_sub_system = [v if isinstance(v, SystemName) else SystemName(v) for v in self.has_sub_system]

        if not isinstance(self.has_system_capability, list):
            self.has_system_capability = [self.has_system_capability] if self.has_system_capability is not None else []
        self.has_system_capability = [v if isinstance(v, SystemCapabilityName) else SystemCapabilityName(v) for v in self.has_system_capability]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlSystem(System):
    """
    A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a
    subsystem of the Facility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ControlSystem"]
    class_class_curie: ClassVar[str] = "narad:ControlSystem"
    class_name: ClassVar[str] = "ControlSystem"
    class_model_uri: ClassVar[URIRef] = NARAD.ControlSystem

    name: Union[str, ControlSystemName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlSystemName):
            self.name = ControlSystemName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Magnet(System):
    """
    A powered magnet device (generic supertype for all magnet kinds).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Magnet"]
    class_class_curie: ClassVar[str] = "narad:Magnet"
    class_name: ClassVar[str] = "Magnet"
    class_model_uri: ClassVar[URIRef] = NARAD.Magnet

    name: Union[str, MagnetName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MagnetName):
            self.name = MagnetName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quadrupole(Magnet):
    """
    A quadrupole focusing/defocusing magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Quadrupole"]
    class_class_curie: ClassVar[str] = "narad:Quadrupole"
    class_name: ClassVar[str] = "Quadrupole"
    class_model_uri: ClassVar[URIRef] = NARAD.Quadrupole

    name: Union[str, QuadrupoleName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, QuadrupoleName):
            self.name = QuadrupoleName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Corrector(Magnet):
    """
    A dipole corrector magnet for orbit correction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Corrector"]
    class_class_curie: ClassVar[str] = "narad:Corrector"
    class_name: ClassVar[str] = "Corrector"
    class_model_uri: ClassVar[URIRef] = NARAD.Corrector

    name: Union[str, CorrectorName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CorrectorName):
            self.name = CorrectorName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dipole(Magnet):
    """
    A dipole bending magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Dipole"]
    class_class_curie: ClassVar[str] = "narad:Dipole"
    class_name: ClassVar[str] = "Dipole"
    class_model_uri: ClassVar[URIRef] = NARAD.Dipole

    name: Union[str, DipoleName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DipoleName):
            self.name = DipoleName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Solenoid(Magnet):
    """
    A solenoid magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Solenoid"]
    class_class_curie: ClassVar[str] = "narad:Solenoid"
    class_name: ClassVar[str] = "Solenoid"
    class_model_uri: ClassVar[URIRef] = NARAD.Solenoid

    name: Union[str, SolenoidName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SolenoidName):
            self.name = SolenoidName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Instrument(System):
    """
    A generic beam diagnostic instrument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Instrument"]
    class_class_curie: ClassVar[str] = "narad:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = NARAD.Instrument

    name: Union[str, InstrumentName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InstrumentName):
            self.name = InstrumentName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BPM(Instrument):
    """
    A Beam Position Monitor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BPM"]
    class_class_curie: ClassVar[str] = "narad:BPM"
    class_name: ClassVar[str] = "BPM"
    class_model_uri: ClassVar[URIRef] = NARAD.BPM

    name: Union[str, BPMName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BPMName):
            self.name = BPMName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RFCavity(System):
    """
    A radio-frequency accelerating or bunching cavity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["RFCavity"]
    class_class_curie: ClassVar[str] = "narad:RFCavity"
    class_name: ClassVar[str] = "RFCavity"
    class_model_uri: ClassVar[URIRef] = NARAD.RFCavity

    name: Union[str, RFCavityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, RFCavityName):
            self.name = RFCavityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Marker(System):
    """
    A zero-length reference point, drift space, or survey marker.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Marker"]
    class_class_curie: ClassVar[str] = "narad:Marker"
    class_name: ClassVar[str] = "Marker"
    class_model_uri: ClassVar[URIRef] = NARAD.Marker

    name: Union[str, MarkerName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MarkerName):
            self.name = MarkerName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemCapability(NamedThing):
    """
    A capability of a system. SystemCapability describes what a system can expose, monitor, control, or actuate with
    respect to one or more signals. Aligned to ssn-system:SystemCapability; linked from System instances via
    ssn-system:hasSystemCapability, and from Signals via ssn:forProperty. Profile-level inheritance (shared vs.
    type-specific signals) is expressed in CapabilityProfile, not here.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SystemCapability"]
    class_class_curie: ClassVar[str] = "narad:SystemCapability"
    class_name: ClassVar[str] = "SystemCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.SystemCapability

    name: Union[str, SystemCapabilityName] = None
    for_property: Optional[Union[Union[str, SignalName], list[Union[str, SignalName]]]] = empty_list()
    device_type: Optional[Union[str, "ElementKindEnum"]] = None
    is_abstract: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SystemCapabilityName):
            self.name = SystemCapabilityName(self.name)

        if not isinstance(self.for_property, list):
            self.for_property = [self.for_property] if self.for_property is not None else []
        self.for_property = [v if isinstance(v, SignalName) else SignalName(v) for v in self.for_property]

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

        if self.is_abstract is not None and not isinstance(self.is_abstract, Bool):
            self.is_abstract = Bool(self.is_abstract)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MagnetCapability(SystemCapability):
    """
    Generic magnet capability (current control and readback signals).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["MagnetCapability"]
    class_class_curie: ClassVar[str] = "narad:MagnetCapability"
    class_name: ClassVar[str] = "MagnetCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.MagnetCapability

    name: Union[str, MagnetCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MagnetCapabilityName):
            self.name = MagnetCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuadrupoleCapability(MagnetCapability):
    """
    Quadrupole-specific capability extending MagnetCapability with strength signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["QuadrupoleCapability"]
    class_class_curie: ClassVar[str] = "narad:QuadrupoleCapability"
    class_name: ClassVar[str] = "QuadrupoleCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.QuadrupoleCapability

    name: Union[str, QuadrupoleCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, QuadrupoleCapabilityName):
            self.name = QuadrupoleCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectorCapability(MagnetCapability):
    """
    Corrector-specific capability extending MagnetCapability with kick signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["CorrectorCapability"]
    class_class_curie: ClassVar[str] = "narad:CorrectorCapability"
    class_name: ClassVar[str] = "CorrectorCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.CorrectorCapability

    name: Union[str, CorrectorCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CorrectorCapabilityName):
            self.name = CorrectorCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DipoleCapability(MagnetCapability):
    """
    Dipole-specific capability extending MagnetCapability with bend-field signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["DipoleCapability"]
    class_class_curie: ClassVar[str] = "narad:DipoleCapability"
    class_name: ClassVar[str] = "DipoleCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.DipoleCapability

    name: Union[str, DipoleCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DipoleCapabilityName):
            self.name = DipoleCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolenoidCapability(MagnetCapability):
    """
    Solenoid-specific capability extending MagnetCapability with focusing signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SolenoidCapability"]
    class_class_curie: ClassVar[str] = "narad:SolenoidCapability"
    class_name: ClassVar[str] = "SolenoidCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.SolenoidCapability

    name: Union[str, SolenoidCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SolenoidCapabilityName):
            self.name = SolenoidCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InstrumentCapability(SystemCapability):
    """
    Generic instrument capability (position readback and status signals).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["InstrumentCapability"]
    class_class_curie: ClassVar[str] = "narad:InstrumentCapability"
    class_name: ClassVar[str] = "InstrumentCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.InstrumentCapability

    name: Union[str, InstrumentCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InstrumentCapabilityName):
            self.name = InstrumentCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BPMCapability(InstrumentCapability):
    """
    BPM-specific capability with horizontal and vertical position readback signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BPMCapability"]
    class_class_curie: ClassVar[str] = "narad:BPMCapability"
    class_name: ClassVar[str] = "BPMCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.BPMCapability

    name: Union[str, BPMCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BPMCapabilityName):
            self.name = BPMCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CavityGradientCapability(SystemCapability):
    """
    RF cavity capability with gradient control, readback, and status signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["CavityGradientCapability"]
    class_class_curie: ClassVar[str] = "narad:CavityGradientCapability"
    class_name: ClassVar[str] = "CavityGradientCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.CavityGradientCapability

    name: Union[str, CavityGradientCapabilityName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CavityGradientCapabilityName):
            self.name = CavityGradientCapabilityName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signal(NamedThing):
    """
    Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback,
    limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The
    concrete facility binding is captured in SignalBinding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Signal"]
    class_class_curie: ClassVar[str] = "narad:Signal"
    class_name: ClassVar[str] = "Signal"
    class_model_uri: ClassVar[URIRef] = NARAD.Signal

    name: Union[str, SignalName] = None
    role: Optional[Union[str, "SignalRoleEnum"]] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    units: Optional[str] = None
    units_uri: Optional[Union[str, URIorCURIE]] = None

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservableSignal(Signal):
    """
    A NARAD signal that is read, monitored, observed, or exposed by a system. Examples: current_readback, status,
    horizontal_beam_position, gradient_readback. Aligned to sosa:ObservableProperty.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ObservableSignal"]
    class_class_curie: ClassVar[str] = "narad:ObservableSignal"
    class_name: ClassVar[str] = "ObservableSignal"
    class_model_uri: ClassVar[URIRef] = NARAD.ObservableSignal

    name: Union[str, ObservableSignalName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ObservableSignalName):
            self.name = ObservableSignalName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActuatableSignal(Signal):
    """
    A NARAD signal that can be commanded, set, or acted upon. Examples: current_setpoint, strength_setpoint,
    kick_setpoint, field_setpoint, current_min, current_max, gradient_setpoint. Aligned to sosa:ActuatableProperty.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ActuatableSignal"]
    class_class_curie: ClassVar[str] = "narad:ActuatableSignal"
    class_name: ClassVar[str] = "ActuatableSignal"
    class_model_uri: ClassVar[URIRef] = NARAD.ActuatableSignal

    name: Union[str, ActuatableSignalName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ActuatableSignalName):
            self.name = ActuatableSignalName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InstanceSignalBinding(NamedThing):
    """
    A facility-specific binding between a NARAD Signal and an implementation interface (e.g. an EPICS process
    variable). Modeled as sosa:Sensor because it describes how a signal is observed, monitored, or actuated.
    ssn:forProperty → Signal; narad:isInstanceOf → the capability class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["InstanceSignalBinding"]
    class_class_curie: ClassVar[str] = "narad:InstanceSignalBinding"
    class_name: ClassVar[str] = "InstanceSignalBinding"
    class_model_uri: ClassVar[URIRef] = NARAD.InstanceSignalBinding

    name: Union[str, InstanceSignalBindingName] = None
    is_instance_of: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    is_hosted_by: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    is_property_of: Optional[Union[str, URIorCURIE]] = None
    pv_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InstanceSignalBindingName):
            self.name = InstanceSignalBindingName(self.name)

        if not isinstance(self.is_instance_of, list):
            self.is_instance_of = [self.is_instance_of] if self.is_instance_of is not None else []
        self.is_instance_of = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.is_instance_of]

        if not isinstance(self.is_hosted_by, list):
            self.is_hosted_by = [self.is_hosted_by] if self.is_hosted_by is not None else []
        self.is_hosted_by = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.is_hosted_by]

        if self.is_property_of is not None and not isinstance(self.is_property_of, URIorCURIE):
            self.is_property_of = URIorCURIE(self.is_property_of)

        if self.pv_name is not None and not isinstance(self.pv_name, str):
            self.pv_name = str(self.pv_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementParamSet(NamedThing):
    """
    Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP,
    MagneticMultipoleP, SolenoidP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ElementParamSet"]
    class_class_curie: ClassVar[str] = "narad:ElementParamSet"
    class_name: ClassVar[str] = "ElementParamSet"
    class_model_uri: ClassVar[URIRef] = NARAD.ElementParamSet

    name: Union[str, ElementParamSetName] = None
    frequency: Optional[float] = None
    voltage: Optional[float] = None
    phase: Optional[float] = None
    angle_ref: Optional[float] = None
    e1: Optional[float] = None
    e2: Optional[float] = None
    Kn1: Optional[float] = None
    Ksol: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ElementParamSetName):
            self.name = ElementParamSetName(self.name)

        if self.frequency is not None and not isinstance(self.frequency, float):
            self.frequency = float(self.frequency)

        if self.voltage is not None and not isinstance(self.voltage, float):
            self.voltage = float(self.voltage)

        if self.phase is not None and not isinstance(self.phase, float):
            self.phase = float(self.phase)

        if self.angle_ref is not None and not isinstance(self.angle_ref, float):
            self.angle_ref = float(self.angle_ref)

        if self.e1 is not None and not isinstance(self.e1, float):
            self.e1 = float(self.e1)

        if self.e2 is not None and not isinstance(self.e2, float):
            self.e2 = float(self.e2)

        if self.Kn1 is not None and not isinstance(self.Kn1, float):
            self.Kn1 = float(self.Kn1)

        if self.Ksol is not None and not isinstance(self.Ksol, float):
            self.Ksol = float(self.Ksol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FacilityParamSet(YAMLRoot):
    """
    Facility-specific element parameters block for beamline elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["FacilityParamSet"]
    class_class_curie: ClassVar[str] = "narad:FacilityParamSet"
    class_name: ClassVar[str] = "FacilityParamSet"
    class_model_uri: ClassVar[URIRef] = NARAD.FacilityParamSet

    facility_element_type: Optional[str] = None
    modeled_as: Optional[str] = None
    properties: Optional[Union[dict, "AnyValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.facility_element_type is not None and not isinstance(self.facility_element_type, str):
            self.facility_element_type = str(self.facility_element_type)

        if self.modeled_as is not None and not isinstance(self.modeled_as, str):
            self.modeled_as = str(self.modeled_as)

        super().__post_init__(**kwargs)


AnyValue = Any

# Enumerations
class ElementKindEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for beamline element types, shared between the capability layer
    (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here keeps profile
    device_type values in sync with element kind values without circular imports.
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
        description="""Controlled vocabulary for beamline element types, shared between the capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here keeps profile device_type values in sync with element kind values without circular imports.""",
    )

class DeviceDomainEnum(EnumDefinitionImpl):
    """
    High-level device domain for a control profile family.
    """
    Magnet = PermissibleValue(
        text="Magnet",
        description="Magnet devices: dipoles, quadrupoles, correctors, solenoids.")
    Instrument = PermissibleValue(
        text="Instrument",
        description="Beam diagnostic instruments: BPMs, screens, viewers, etc.")
    RFCavity = PermissibleValue(
        text="RFCavity",
        description="RF cavity and RF-related devices.")

    _defn = EnumDefinition(
        name="DeviceDomainEnum",
        description="High-level device domain for a control profile family.",
    )

class DataTypeEnum(EnumDefinitionImpl):
    """
    Allowed data types for signal values.
    """
    int = PermissibleValue(
        text="int",
        description="Integer.",
        meaning=NCIT["C47840"])
    float = PermissibleValue(
        text="float",
        description="Single-precision floating-point.",
        meaning=NCIT["C48150"])
    double = PermissibleValue(
        text="double",
        description="Double-precision floating-point.",
        meaning=NCIT["C48870"])
    string = PermissibleValue(
        text="string",
        description="Text string.",
        meaning=NCIT["C45253"])
    boolean = PermissibleValue(
        text="boolean",
        description="True/false value.",
        meaning=NCIT["C45254"])
    coded_value = PermissibleValue(
        text="coded_value",
        description="A code referenced from an external coding system.",
        meaning=NCIT["C95637"])

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Allowed data types for signal values.",
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

    _defn = EnumDefinition(
        name="SignalRoleEnum",
        description="Controlled vocabulary for the semantic role of a signal within a capability.",
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

slots.name = Slot(uri=NARAD.name, name="name", curie=NARAD.curie('name'),
                   model_uri=NARAD.name, domain=None, range=URIRef)

slots.description = Slot(uri=NARAD.description, name="description", curie=NARAD.curie('description'),
                   model_uri=NARAD.description, domain=None, range=Optional[str])

slots.has_sub_system = Slot(uri=NARAD.has_sub_system, name="has_sub_system", curie=NARAD.curie('has_sub_system'),
                   model_uri=NARAD.has_sub_system, domain=System, range=Optional[Union[Union[str, SystemName], list[Union[str, SystemName]]]])

slots.has_system_capability = Slot(uri=NARAD.has_system_capability, name="has_system_capability", curie=NARAD.curie('has_system_capability'),
                   model_uri=NARAD.has_system_capability, domain=System, range=Optional[Union[Union[str, SystemCapabilityName], list[Union[str, SystemCapabilityName]]]])

slots.for_property = Slot(uri=NARAD.for_property, name="for_property", curie=NARAD.curie('for_property'),
                   model_uri=NARAD.for_property, domain=None, range=Optional[Union[Union[str, SignalName], list[Union[str, SignalName]]]])

slots.is_property_of = Slot(uri=NARAD.is_property_of, name="is_property_of", curie=NARAD.curie('is_property_of'),
                   model_uri=NARAD.is_property_of, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.is_hosted_by = Slot(uri=NARAD.is_hosted_by, name="is_hosted_by", curie=NARAD.curie('is_hosted_by'),
                   model_uri=NARAD.is_hosted_by, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.is_instance_of = Slot(uri=NARAD.is_instance_of, name="is_instance_of", curie=NARAD.curie('is_instance_of'),
                   model_uri=NARAD.is_instance_of, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.pv_name = Slot(uri=NARAD.pv_name, name="pv_name", curie=NARAD.curie('pv_name'),
                   model_uri=NARAD.pv_name, domain=None, range=Optional[str])

slots.control_system_suffix = Slot(uri=NARAD.control_system_suffix, name="control_system_suffix", curie=NARAD.curie('control_system_suffix'),
                   model_uri=NARAD.control_system_suffix, domain=None, range=Optional[str])

slots.beamlines = Slot(uri=NARAD.beamlines, name="beamlines", curie=NARAD.curie('beamlines'),
                   model_uri=NARAD.beamlines, domain=None, range=Optional[Union[dict[Union[str, BeamlineName], Union[dict, Beamline]], list[Union[dict, Beamline]]]])

slots.elements = Slot(uri=NARAD.elements, name="elements", curie=NARAD.curie('elements'),
                   model_uri=NARAD.elements, domain=None, range=Optional[Union[dict[Union[str, BeamlineElementName], Union[dict, BeamlineElement]], list[Union[dict, BeamlineElement]]]])

slots.narad_config = Slot(uri=NARAD.narad_config, name="narad_config", curie=NARAD.curie('narad_config'),
                   model_uri=NARAD.narad_config, domain=None, range=Optional[Union[dict, NaradConfig]])

slots.schema_version = Slot(uri=NARAD.schema_version, name="schema_version", curie=NARAD.curie('schema_version'),
                   model_uri=NARAD.schema_version, domain=None, range=Optional[str])

slots.facility = Slot(uri=NARAD.facility, name="facility", curie=NARAD.curie('facility'),
                   model_uri=NARAD.facility, domain=None, range=Optional[str])

slots.control_system = Slot(uri=NARAD.control_system, name="control_system", curie=NARAD.curie('control_system'),
                   model_uri=NARAD.control_system, domain=None, range=Optional[str])

slots.naming_convention = Slot(uri=NARAD.naming_convention, name="naming_convention", curie=NARAD.curie('naming_convention'),
                   model_uri=NARAD.naming_convention, domain=None, range=Optional[str])

slots.capability_layer = Slot(uri=NARAD.capability_layer, name="capability_layer", curie=NARAD.curie('capability_layer'),
                   model_uri=NARAD.capability_layer, domain=None, range=Optional[Union[dict, CapabilityLayer]])

slots.signal_layer = Slot(uri=NARAD.signal_layer, name="signal_layer", curie=NARAD.curie('signal_layer'),
                   model_uri=NARAD.signal_layer, domain=None, range=Optional[Union[dict, SignalLayer]])

slots.facilities = Slot(uri=NARAD.facilities, name="facilities", curie=NARAD.curie('facilities'),
                   model_uri=NARAD.facilities, domain=None, range=Optional[Union[dict[Union[str, FacilityConfigName], Union[dict, FacilityConfig]], list[Union[dict, FacilityConfig]]]])

slots.signal_definitions = Slot(uri=NARAD.signal_definitions, name="signal_definitions", curie=NARAD.curie('signal_definitions'),
                   model_uri=NARAD.signal_definitions, domain=None, range=Optional[Union[dict, SignalDefinitions]])

slots.type_signal_sets = Slot(uri=NARAD.type_signal_sets, name="type_signal_sets", curie=NARAD.curie('type_signal_sets'),
                   model_uri=NARAD.type_signal_sets, domain=None, range=Optional[Union[dict, TypeSignalSet]])

slots.signal_bindings = Slot(uri=NARAD.signal_bindings, name="signal_bindings", curie=NARAD.curie('signal_bindings'),
                   model_uri=NARAD.signal_bindings, domain=None, range=Optional[Union[Union[dict, SignalBinding], list[Union[dict, SignalBinding]]]])

slots.instance_signal_bindings = Slot(uri=NARAD.instance_signal_bindings, name="instance_signal_bindings", curie=NARAD.curie('instance_signal_bindings'),
                   model_uri=NARAD.instance_signal_bindings, domain=None, range=Optional[Union[dict[Union[str, InstanceSignalBindingName], Union[dict, InstanceSignalBinding]], list[Union[dict, InstanceSignalBinding]]]])

slots.capability_profile_family = Slot(uri=NARAD.capability_profile_family, name="capability_profile_family", curie=NARAD.curie('capability_profile_family'),
                   model_uri=NARAD.capability_profile_family, domain=None, range=Optional[Union[str, ControlProfileFamilyName]])

slots.capability_profile = Slot(uri=NARAD.capability_profile, name="capability_profile", curie=NARAD.curie('capability_profile'),
                   model_uri=NARAD.capability_profile, domain=None, range=Optional[Union[str, CapabilityProfileName]])

slots.profiles = Slot(uri=NARAD.profiles, name="profiles", curie=NARAD.curie('profiles'),
                   model_uri=NARAD.profiles, domain=None, range=Optional[Union[dict[Union[str, ControlProfileFamilyName], Union[dict, ControlProfileFamily]], list[Union[dict, ControlProfileFamily]]]])

slots.shared_capabilities = Slot(uri=NARAD.shared_capabilities, name="shared_capabilities", curie=NARAD.curie('shared_capabilities'),
                   model_uri=NARAD.shared_capabilities, domain=None, range=Optional[Union[dict[Union[str, CapabilityName], Union[dict, Capability]], list[Union[dict, Capability]]]])

slots.type_profiles = Slot(uri=NARAD.type_profiles, name="type_profiles", curie=NARAD.curie('type_profiles'),
                   model_uri=NARAD.type_profiles, domain=None, range=Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]])

slots.inherits_shared_capabilities = Slot(uri=NARAD.inherits_shared_capabilities, name="inherits_shared_capabilities", curie=NARAD.curie('inherits_shared_capabilities'),
                   model_uri=NARAD.inherits_shared_capabilities, domain=None, range=Optional[Union[Union[str, CapabilityName], list[Union[str, CapabilityName]]]])

slots.type_specific_capabilities = Slot(uri=NARAD.type_specific_capabilities, name="type_specific_capabilities", curie=NARAD.curie('type_specific_capabilities'),
                   model_uri=NARAD.type_specific_capabilities, domain=None, range=Optional[Union[dict[Union[str, TypeSpecificCapabilityName], Union[dict, TypeSpecificCapability]], list[Union[dict, TypeSpecificCapability]]]])

slots.inherits_from = Slot(uri=NARAD.inherits_from, name="inherits_from", curie=NARAD.curie('inherits_from'),
                   model_uri=NARAD.inherits_from, domain=None, range=Optional[Union[str, CapabilityName]])

slots.capability_class = Slot(uri=NARAD.capability_class, name="capability_class", curie=NARAD.curie('capability_class'),
                   model_uri=NARAD.capability_class, domain=None, range=Optional[str])

slots.class_curie = Slot(uri=NARAD.class_curie, name="class_curie", curie=NARAD.curie('class_curie'),
                   model_uri=NARAD.class_curie, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.signals = Slot(uri=NARAD.signals, name="signals", curie=NARAD.curie('signals'),
                   model_uri=NARAD.signals, domain=None, range=Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]])

slots.device_type = Slot(uri=NARAD.device_type, name="device_type", curie=NARAD.curie('device_type'),
                   model_uri=NARAD.device_type, domain=None, range=Optional[Union[str, "ElementKindEnum"]])

slots.device_domain = Slot(uri=NARAD.device_domain, name="device_domain", curie=NARAD.curie('device_domain'),
                   model_uri=NARAD.device_domain, domain=None, range=Optional[Union[str, "DeviceDomainEnum"]])

slots.is_abstract = Slot(uri=NARAD.is_abstract, name="is_abstract", curie=NARAD.curie('is_abstract'),
                   model_uri=NARAD.is_abstract, domain=None, range=Optional[Union[bool, Bool]])

slots.role = Slot(uri=NARAD.role, name="role", curie=NARAD.curie('role'),
                   model_uri=NARAD.role, domain=None, range=Optional[Union[str, "SignalRoleEnum"]])

slots.data_type = Slot(uri=NARAD.data_type, name="data_type", curie=NARAD.curie('data_type'),
                   model_uri=NARAD.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.units = Slot(uri=NARAD.units, name="units", curie=NARAD.curie('units'),
                   model_uri=NARAD.units, domain=None, range=Optional[str])

slots.units_uri = Slot(uri=NARAD.units_uri, name="units_uri", curie=NARAD.curie('units_uri'),
                   model_uri=NARAD.units_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.beamline_kind = Slot(uri=NARAD.beamline_kind, name="beamline_kind", curie=NARAD.curie('beamline_kind'),
                   model_uri=NARAD.beamline_kind, domain=None, range=Optional[str])

slots.magnet_signals = Slot(uri=NARAD.magnet_signals, name="magnet_signals", curie=NARAD.curie('magnet_signals'),
                   model_uri=NARAD.magnet_signals, domain=None, range=Optional[Union[dict, MagnetSignalSet]])

slots.quadrupole_signals = Slot(uri=NARAD.quadrupole_signals, name="quadrupole_signals", curie=NARAD.curie('quadrupole_signals'),
                   model_uri=NARAD.quadrupole_signals, domain=None, range=Optional[Union[dict, QuadrupoleSignalSet]])

slots.corrector_signals = Slot(uri=NARAD.corrector_signals, name="corrector_signals", curie=NARAD.curie('corrector_signals'),
                   model_uri=NARAD.corrector_signals, domain=None, range=Optional[Union[dict, CorrectorSignalSet]])

slots.dipole_signals = Slot(uri=NARAD.dipole_signals, name="dipole_signals", curie=NARAD.curie('dipole_signals'),
                   model_uri=NARAD.dipole_signals, domain=None, range=Optional[Union[dict, DipoleSignalSet]])

slots.bpm_signals = Slot(uri=NARAD.bpm_signals, name="bpm_signals", curie=NARAD.curie('bpm_signals'),
                   model_uri=NARAD.bpm_signals, domain=None, range=Optional[Union[dict, BPMSignalSet]])

slots.rfcavity_signals = Slot(uri=NARAD.rfcavity_signals, name="rfcavity_signals", curie=NARAD.curie('rfcavity_signals'),
                   model_uri=NARAD.rfcavity_signals, domain=None, range=Optional[Union[dict, RFCavitySignalSet]])

slots.current_setpoint = Slot(uri=NARAD.current_setpoint, name="current_setpoint", curie=NARAD.curie('current_setpoint'),
                   model_uri=NARAD.current_setpoint, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.current_readback = Slot(uri=NARAD.current_readback, name="current_readback", curie=NARAD.curie('current_readback'),
                   model_uri=NARAD.current_readback, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.current_min = Slot(uri=NARAD.current_min, name="current_min", curie=NARAD.curie('current_min'),
                   model_uri=NARAD.current_min, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.current_max = Slot(uri=NARAD.current_max, name="current_max", curie=NARAD.curie('current_max'),
                   model_uri=NARAD.current_max, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.strength_setpoint = Slot(uri=NARAD.strength_setpoint, name="strength_setpoint", curie=NARAD.curie('strength_setpoint'),
                   model_uri=NARAD.strength_setpoint, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.kick_setpoint = Slot(uri=NARAD.kick_setpoint, name="kick_setpoint", curie=NARAD.curie('kick_setpoint'),
                   model_uri=NARAD.kick_setpoint, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.field_setpoint = Slot(uri=NARAD.field_setpoint, name="field_setpoint", curie=NARAD.curie('field_setpoint'),
                   model_uri=NARAD.field_setpoint, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.horizontal_beam_position = Slot(uri=NARAD.horizontal_beam_position, name="horizontal_beam_position", curie=NARAD.curie('horizontal_beam_position'),
                   model_uri=NARAD.horizontal_beam_position, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.vertical_beam_position = Slot(uri=NARAD.vertical_beam_position, name="vertical_beam_position", curie=NARAD.curie('vertical_beam_position'),
                   model_uri=NARAD.vertical_beam_position, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.gradient_setpoint = Slot(uri=NARAD.gradient_setpoint, name="gradient_setpoint", curie=NARAD.curie('gradient_setpoint'),
                   model_uri=NARAD.gradient_setpoint, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.gradient_readback = Slot(uri=NARAD.gradient_readback, name="gradient_readback", curie=NARAD.curie('gradient_readback'),
                   model_uri=NARAD.gradient_readback, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.status = Slot(uri=NARAD.status, name="status", curie=NARAD.curie('status'),
                   model_uri=NARAD.status, domain=None, range=Optional[Union[dict, SignalBinding]])

slots.line = Slot(uri=NARAD.line, name="line", curie=NARAD.curie('line'),
                   model_uri=NARAD.line, domain=None, range=Optional[Union[Union[str, BeamlineElementName], list[Union[str, BeamlineElementName]]]])

slots.element_kind = Slot(uri=NARAD.element_kind, name="element_kind", curie=NARAD.curie('element_kind'),
                   model_uri=NARAD.element_kind, domain=None, range=Optional[Union[str, "ElementKindEnum"]])

slots.length = Slot(uri=NARAD.length, name="length", curie=NARAD.curie('length'),
                   model_uri=NARAD.length, domain=None, range=Optional[float])

slots.param_set = Slot(uri=NARAD.param_set, name="param_set", curie=NARAD.curie('param_set'),
                   model_uri=NARAD.param_set, domain=None, range=Optional[Union[dict[Union[str, ElementParamSetName], Union[dict, ElementParamSet]], list[Union[dict, ElementParamSet]]]])

slots.facility_param_set = Slot(uri=NARAD.facility_param_set, name="facility_param_set", curie=NARAD.curie('facility_param_set'),
                   model_uri=NARAD.facility_param_set, domain=None, range=Optional[Union[dict, FacilityParamSet]])

slots.properties = Slot(uri=NARAD.properties, name="properties", curie=NARAD.curie('properties'),
                   model_uri=NARAD.properties, domain=None, range=Optional[Union[dict, AnyValue]])

slots.modeled_as = Slot(uri=NARAD.modeled_as, name="modeled_as", curie=NARAD.curie('modeled_as'),
                   model_uri=NARAD.modeled_as, domain=None, range=Optional[str])

slots.facility_element_type = Slot(uri=NARAD.facility_element_type, name="facility_element_type", curie=NARAD.curie('facility_element_type'),
                   model_uri=NARAD.facility_element_type, domain=None, range=Optional[str])

slots.frequency = Slot(uri=NARAD.frequency, name="frequency", curie=NARAD.curie('frequency'),
                   model_uri=NARAD.frequency, domain=None, range=Optional[float])

slots.voltage = Slot(uri=NARAD.voltage, name="voltage", curie=NARAD.curie('voltage'),
                   model_uri=NARAD.voltage, domain=None, range=Optional[float])

slots.phase = Slot(uri=NARAD.phase, name="phase", curie=NARAD.curie('phase'),
                   model_uri=NARAD.phase, domain=None, range=Optional[float])

slots.angle_ref = Slot(uri=NARAD.angle_ref, name="angle_ref", curie=NARAD.curie('angle_ref'),
                   model_uri=NARAD.angle_ref, domain=None, range=Optional[float])

slots.e1 = Slot(uri=NARAD.e1, name="e1", curie=NARAD.curie('e1'),
                   model_uri=NARAD.e1, domain=None, range=Optional[float])

slots.e2 = Slot(uri=NARAD.e2, name="e2", curie=NARAD.curie('e2'),
                   model_uri=NARAD.e2, domain=None, range=Optional[float])

slots.Kn1 = Slot(uri=NARAD.Kn1, name="Kn1", curie=NARAD.curie('Kn1'),
                   model_uri=NARAD.Kn1, domain=None, range=Optional[float])

slots.Ksol = Slot(uri=NARAD.Ksol, name="Ksol", curie=NARAD.curie('Ksol'),
                   model_uri=NARAD.Ksol, domain=None, range=Optional[float])

slots.facility_identifier = Slot(uri=NARAD.facility_identifier, name="facility_identifier", curie=NARAD.curie('facility_identifier'),
                   model_uri=NARAD.facility_identifier, domain=None, range=Optional[Union[Union[dict, FacilityIdentifier], list[Union[dict, FacilityIdentifier]]]])

slots.identifier_type = Slot(uri=NARAD.identifier_type, name="identifier_type", curie=NARAD.curie('identifier_type'),
                   model_uri=NARAD.identifier_type, domain=None, range=Optional[Union[str, "IdentifierTypeEnum"]])

slots.identifier_value = Slot(uri=NARAD.identifier_value, name="identifier_value", curie=NARAD.curie('identifier_value'),
                   model_uri=NARAD.identifier_value, domain=None, range=Optional[str])

slots.intent = Slot(uri=NARAD.intent, name="intent", curie=NARAD.curie('intent'),
                   model_uri=NARAD.intent, domain=None, range=Optional[str])

slots.NaradConfig_schema_version = Slot(uri=NARAD.schema_version, name="NaradConfig_schema_version", curie=NARAD.curie('schema_version'),
                   model_uri=NARAD.NaradConfig_schema_version, domain=NaradConfig, range=str)

slots.NaradConfig_facility = Slot(uri=NARAD.facility, name="NaradConfig_facility", curie=NARAD.curie('facility'),
                   model_uri=NARAD.NaradConfig_facility, domain=NaradConfig, range=str)

slots.NaradConfig_control_system = Slot(uri=NARAD.control_system, name="NaradConfig_control_system", curie=NARAD.curie('control_system'),
                   model_uri=NARAD.NaradConfig_control_system, domain=NaradConfig, range=str)

slots.NaradConfig_capability_layer = Slot(uri=NARAD.capability_layer, name="NaradConfig_capability_layer", curie=NARAD.curie('capability_layer'),
                   model_uri=NARAD.NaradConfig_capability_layer, domain=NaradConfig, range=Union[dict, "CapabilityLayer"])

slots.NaradConfig_signal_layer = Slot(uri=NARAD.signal_layer, name="NaradConfig_signal_layer", curie=NARAD.curie('signal_layer'),
                   model_uri=NARAD.NaradConfig_signal_layer, domain=NaradConfig, range=Union[dict, "SignalLayer"])

slots.System_has_sub_system = Slot(uri=NARAD.has_sub_system, name="System_has_sub_system", curie=NARAD.curie('has_sub_system'),
                   model_uri=NARAD.System_has_sub_system, domain=System, range=Optional[Union[Union[str, SystemName], list[Union[str, SystemName]]]])

slots.System_has_system_capability = Slot(uri=NARAD.has_system_capability, name="System_has_system_capability", curie=NARAD.curie('has_system_capability'),
                   model_uri=NARAD.System_has_system_capability, domain=System, range=Optional[Union[Union[str, SystemCapabilityName], list[Union[str, SystemCapabilityName]]]])

slots.SystemCapability_for_property = Slot(uri=NARAD.for_property, name="SystemCapability_for_property", curie=NARAD.curie('for_property'),
                   model_uri=NARAD.SystemCapability_for_property, domain=SystemCapability, range=Optional[Union[Union[str, SignalName], list[Union[str, SignalName]]]])

slots.InstanceSignalBinding_is_instance_of = Slot(uri=NARAD.is_instance_of, name="InstanceSignalBinding_is_instance_of", curie=NARAD.curie('is_instance_of'),
                   model_uri=NARAD.InstanceSignalBinding_is_instance_of, domain=InstanceSignalBinding, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.InstanceSignalBinding_is_hosted_by = Slot(uri=NARAD.is_hosted_by, name="InstanceSignalBinding_is_hosted_by", curie=NARAD.curie('is_hosted_by'),
                   model_uri=NARAD.InstanceSignalBinding_is_hosted_by, domain=InstanceSignalBinding, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.InstanceSignalBinding_is_property_of = Slot(uri=NARAD.is_property_of, name="InstanceSignalBinding_is_property_of", curie=NARAD.curie('is_property_of'),
                   model_uri=NARAD.InstanceSignalBinding_is_property_of, domain=InstanceSignalBinding, range=Optional[Union[str, URIorCURIE]])
