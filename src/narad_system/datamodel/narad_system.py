# Auto generated from narad_system.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-14T12:12:17
# Schema: narad-system-schema
#
# id: https://w3id.org/narad_linkml/schema/narad/system
# description: LinkML schema for representing NARAD control-system semantics, facility-level signal templates, and facility-specific instance bindings aligned with SSN, SSN-System, and SOSA ontologies.
#   Main modeling layers:
#     - NaradModel — top-level document containing NaradConfig, beamlines, and elements
#       - NaradConfig — top-level NARAD-system container for the capability layer and signal layer
#         - ControlCapabilityLayer — reusable control-profile families, shared capabilities
#         - InstrumentLayer — facility-specific instrument definitions -> their  capabilities
#         - SignalLayer — facility-specific signal suffix templates for system/device types and instance bindings keyed by semantic signal name, linked to the
#           device type
#     - Beamline / BeamlineElement — ordered machine layout of the beamline/line
#     - Element instances — individual beamline elements with applied profiles and instance signal
#       bindings, parameters, and optional facility-specific parameters
#
#   System hierarchy:
#     - System
#       - ControlSystem
#       - Magnet
#         - Quadrupole, Corrector, Dipole, Solenoid
#       - Instrument
#         - BPM
#       - RFCavity
#       - Marker
#       - Drift
#
#   Control Capability hierarchy:
#     - SystemCapability
#       - MagnetControlCapability
#         - QuadrupoleStrengthControlCapability, CorrectorKickControlCapability, DipoleBendControlCapability
#       - InstrumentControlCapability
#       - BPMControlCapability
#       - CavityGradientControlCapability
#
#   Signal modeling:
#     - Signal — abstract control-system quantity
#       - ObservableSignal — readback, constraint, and status quantities
#       - ActuatableSignal — writable/control setpoints
#     - SignalBinding — signal template or suffix definition in the signal layer
#     - InstanceSignalBinding — facility-specific PV binding attached to a beamline element
#
#   Serialization conventions:
#     - beamlines are keyed by beamline name
#     - signals are keyed by semantic signal name
#     - instance_signal_bindings are keyed by semantic signal name
#
#   Alignments with PALS (Particle Accelerator Language Standard):
#     - Beamline aligns with pals:BeamLine
#     - BeamlineElement aligns with pals:Element
#     - Instrument aligns with pals:Instrument
#     - Dipole aligns with pals:Multipole
#     - Quadrupole aligns with pals:Quadrupole
#     - Solenoid aligns with pals:Solenoid
#     - RFCavity aligns with pals:RFCavity
#
#   Additional Notes on Usage: 1. On Signal, SignalBinding, and InstanceSignalBinding: These classes represent different levels of abstraction in the signal modeling.  Signal defines the abstract control-system quantity (e.g. current_readback), SignalBinding captures the control system suffix convention for that signal (e.g. .R for EPICS readback),  and InstanceSignalBinding represents the concrete binding of that signal to a specific beamline element instance, for example, MQWK202.S or RK11:GSET, depending on the facility naming convention.  The semantic signal name (e.g. current_readback) is the key that links these layers together, while the control-system suffix (e.g. .R)  is captured in the SignalBinding. 2. On the distinction between is_instance_of, facility_element_type, and device_type:
#     - BeamlineElement.is_instance_of identifies the element’s semantic class, device_type classifies capability or signal-definition scope, and facility_element_type records facility-local designation.
#     - facility_element_type (FacilityParamSet.facility_element_type) is an optional slot for recording the facility-specific type designation for this element, if it differs from the generic element_kind.
#     - device_type (ControlCapability.device_type) is the generic element type used for capability profile matching
#     and signal definition scoping, while facility_element_type captures the facility-specific type designation that may be used in the control system naming convention
#     or for other facility-specific purposes.
#     For example, a facility might have its own naming convention for magnet types that doesn't align one-to-one with the ElementKindEnum values.
#   3. Expected CURIE usage for is_instance_of, is_hosted_by, and is_property_of:
#     - is_instance_of typically points to the semantic class instantiated by the binding or element, using a CURIE such as narad:CavityGradientCapability if that is your intended convention.
#     - is_hosted_by typically points to the FacilitySystem this binding belongs to, e.g. narad:UITF.
#     - is_property_of typically points to the ControlSystem that implements this binding, e.g. narad:epics.
#   4. Open and constrained vocabularies:
#     - ElementKindEnum provides a controlled vocabulary for key classification slots, but the schema is designed to be extensible
#     with new enum values as needed.
#     - SystemTypeEnum is a high-level classification for systems that can be used for querying and filtering,
#     but it is not intended to capture all the nuance of device types or capabilities.
#     - DataTypeEnum and SignalRoleEnum provide a controlled vocabulary for signal data types and roles,
#     but the schema allows for additional values to be added as needed.
#     - IdentifierTypeEnum provides a controlled vocabulary for types of identifiers used in FacilityIdentifier,
#     but it can be extended to apply to other entities, and with additional identifier types as needed.
#     - The properties slot in FacilityParamSet allows for open-ended key-value pairs to capture any additional
#     facility-specific parameters that don't fit into the predefined schema structure.
#
#   Needed Custom Validations:
#     - Validation to ensure that the element_kind of a BeamlineElement matches the device_type of the DeviceSystem it is an instance of.
#     - Validation to ensure that the value of is_property_of in InstanceSignalBinding matches one of the control systems listed in narad_config.has_sub_system.
#     - Validation that each signal_layer -> facilities -> FacilitySystem -> control_system value has a corresponding entry in narad_config.has_sub_system to ensure that all control systems referenced in the signal layer are defined in the capability layer.
#     - Validation that the signal_bindings defined for a given device_type in the signal layer align with the signals defined in the capability profiles and instrument systems for that device type.
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
PALS = CurieNamespace('pals', 'https://pals-project.readthedocs.io/en/latest/overview.html')
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


class ControlCapabilityName(NamedThingName):
    pass


class SignalDefinitionsName(NamedThingName):
    pass


class SignalBindingName(NamedThingName):
    pass


class BeamlineName(NamedThingName):
    pass


class BeamlineElementName(NamedThingName):
    pass


class SystemName(NamedThingName):
    pass


class FacilitySystemName(SystemName):
    pass


class ControlSystemName(SystemName):
    pass


class DeviceSystemName(SystemName):
    pass


class InstrumentName(SystemName):
    pass


class SystemCapabilityName(NamedThingName):
    pass


class SignalName(NamedThingName):
    pass


class ObservableSignalName(SignalName):
    pass


class ActuatableSignalName(SignalName):
    pass


class InstanceSignalBindingName(NamedThingName):
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
    A top-level NARAD-system container for the: capability layer + signal layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["NaradConfig"]
    class_class_curie: ClassVar[str] = "narad:NaradConfig"
    class_name: ClassVar[str] = "NaradConfig"
    class_model_uri: ClassVar[URIRef] = NARAD.NaradConfig

    schema_version: str = None
    deployed_system: Union[str, FacilitySystemName] = None
    has_sub_system: Union[Union[str, ControlSystemName], list[Union[str, ControlSystemName]]] = None
    control_capability_layer: Union[dict[Union[str, ControlCapabilityName], Union[dict, "ControlCapability"]], list[Union[dict, "ControlCapability"]]] = empty_dict()
    device_layer: Union[dict[Union[str, DeviceSystemName], Union[dict, "DeviceSystem"]], list[Union[dict, "DeviceSystem"]]] = empty_dict()
    signal_layer: Union[dict, "SignalLayer"] = None
    intent: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.schema_version):
            self.MissingRequiredField("schema_version")
        if not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self._is_empty(self.deployed_system):
            self.MissingRequiredField("deployed_system")
        if not isinstance(self.deployed_system, FacilitySystemName):
            self.deployed_system = FacilitySystemName(self.deployed_system)

        if self._is_empty(self.has_sub_system):
            self.MissingRequiredField("has_sub_system")
        if not isinstance(self.has_sub_system, list):
            self.has_sub_system = [self.has_sub_system] if self.has_sub_system is not None else []
        self.has_sub_system = [v if isinstance(v, ControlSystemName) else ControlSystemName(v) for v in self.has_sub_system]

        if self._is_empty(self.control_capability_layer):
            self.MissingRequiredField("control_capability_layer")
        self._normalize_inlined_as_dict(slot_name="control_capability_layer", slot_type=ControlCapability, key_name="name", keyed=True)

        if self._is_empty(self.device_layer):
            self.MissingRequiredField("device_layer")
        self._normalize_inlined_as_dict(slot_name="device_layer", slot_type=DeviceSystem, key_name="name", keyed=True)

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

    control_capabilities: Optional[Union[dict[Union[str, ControlCapabilityName], Union[dict, "ControlCapability"]], list[Union[dict, "ControlCapability"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="control_capabilities", slot_type=ControlCapability, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlCapability(NamedThing):
    """
    A reusable device-type control profile that extends a generic shared capability with type-specific signals (e.g.
    QuadrupoleCurrentControlProfile).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ControlCapability"]
    class_class_curie: ClassVar[str] = "narad:ControlCapability"
    class_name: ClassVar[str] = "ControlCapability"
    class_model_uri: ClassVar[URIRef] = NARAD.ControlCapability

    name: Union[str, ControlCapabilityName] = None
    signals: Union[dict[Union[str, SignalName], Union[dict, "Signal"]], list[Union[dict, "Signal"]]] = empty_dict()
    device_type: Optional[Union[str, "ElementKindEnum"]] = None
    subclass_of: Optional[Union[str, SystemName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlCapabilityName):
            self.name = ControlCapabilityName(self.name)

        if self._is_empty(self.signals):
            self.MissingRequiredField("signals")
        self._normalize_inlined_as_dict(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

        if self.subclass_of is not None and not isinstance(self.subclass_of, SystemName):
            self.subclass_of = SystemName(self.subclass_of)

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

    facilities: Optional[Union[dict[Union[str, FacilitySystemName], Union[dict, "FacilitySystem"]], list[Union[dict, "FacilitySystem"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="facilities", slot_type=FacilitySystem, key_name="name", keyed=True)

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
class SignalDefinitions(NamedThing):
    """
    Signal binding set scoped to a device type or device domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SignalDefinitions"]
    class_class_curie: ClassVar[str] = "narad:SignalDefinitions"
    class_name: ClassVar[str] = "SignalDefinitions"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalDefinitions

    name: Union[str, SignalDefinitionsName] = None
    device_type: Optional[Union[str, "ElementKindEnum"]] = None
    signal_bindings: Optional[Union[dict[Union[str, SignalBindingName], Union[dict, "SignalBinding"]], list[Union[dict, "SignalBinding"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SignalDefinitionsName):
            self.name = SignalDefinitionsName(self.name)

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

        self._normalize_inlined_as_dict(slot_name="signal_bindings", slot_type=SignalBinding, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalBinding(NamedThing):
    """
    A named control system suffix definition for one semantic signal. The suffix is used within in a template naming
    convention to construct the full control system PV name for a given device instance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SignalBinding"]
    class_class_curie: ClassVar[str] = "narad:SignalBinding"
    class_name: ClassVar[str] = "SignalBinding"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalBinding

    name: Union[str, SignalBindingName] = None
    control_system_suffix: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SignalBindingName):
            self.name = SignalBindingName(self.name)

        if self.control_system_suffix is not None and not isinstance(self.control_system_suffix, str):
            self.control_system_suffix = str(self.control_system_suffix)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Beamline(NamedThing):
    """
    A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Beamline"]
    class_class_curie: ClassVar[str] = "narad:Beamline"
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = NARAD.Beamline

    name: Union[str, BeamlineName] = None
    multipass: Optional[Union[bool, Bool]] = None
    length: Optional[float] = None
    zero_point: Optional[Union[str, BeamlineElementName]] = None
    periodic: Optional[Union[bool, Bool]] = None
    line: Optional[Union[Union[str, BeamlineElementName], list[Union[str, BeamlineElementName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineName):
            self.name = BeamlineName(self.name)

        if self.multipass is not None and not isinstance(self.multipass, Bool):
            self.multipass = Bool(self.multipass)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.zero_point is not None and not isinstance(self.zero_point, BeamlineElementName):
            self.zero_point = BeamlineElementName(self.zero_point)

        if self.periodic is not None and not isinstance(self.periodic, Bool):
            self.periodic = Bool(self.periodic)

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
    is_instance_of: Optional[Union[str, list[str]]] = empty_list()
    length: Optional[float] = None
    instance_signal_bindings: Optional[Union[dict[Union[str, InstanceSignalBindingName], Union[dict, "InstanceSignalBinding"]], list[Union[dict, "InstanceSignalBinding"]]]] = empty_dict()
    param_set: Optional[Union[dict, "ElementParamSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineElementName):
            self.name = BeamlineElementName(self.name)

        if not isinstance(self.is_instance_of, list):
            self.is_instance_of = [self.is_instance_of] if self.is_instance_of is not None else []
        self.is_instance_of = [v if isinstance(v, str) else str(v) for v in self.is_instance_of]

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        self._normalize_inlined_as_dict(slot_name="instance_signal_bindings", slot_type=InstanceSignalBinding, key_name="name", keyed=True)

        if self.param_set is not None and not isinstance(self.param_set, ElementParamSet):
            self.param_set = ElementParamSet(**as_dict(self.param_set))

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
    system_type: Optional[Union[str, "SystemTypeEnum"]] = None
    has_sub_system: Optional[Union[dict[Union[str, SystemName], Union[dict, "System"]], list[Union[dict, "System"]]]] = empty_dict()
    has_system_capability: Optional[Union[dict[Union[str, SystemCapabilityName], Union[dict, "SystemCapability"]], list[Union[dict, "SystemCapability"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SystemName):
            self.name = SystemName(self.name)

        if self.system_type is not None and not isinstance(self.system_type, SystemTypeEnum):
            self.system_type = SystemTypeEnum(self.system_type)

        self._normalize_inlined_as_list(slot_name="has_sub_system", slot_type=System, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="has_system_capability", slot_type=SystemCapability, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FacilitySystem(System):
    """
    Facility-specific signal binding configuration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["FacilitySystem"]
    class_class_curie: ClassVar[str] = "narad:FacilitySystem"
    class_name: ClassVar[str] = "FacilitySystem"
    class_model_uri: ClassVar[URIRef] = NARAD.FacilitySystem

    name: Union[str, FacilitySystemName] = None
    facility_identifier: Optional[Union[Union[dict, FacilityIdentifier], list[Union[dict, FacilityIdentifier]]]] = empty_list()
    control_system: Optional[Union[dict, "ControlSystem"]] = None
    naming_convention: Optional[str] = None
    signal_definitions: Optional[Union[dict[Union[str, SignalDefinitionsName], Union[dict, SignalDefinitions]], list[Union[dict, SignalDefinitions]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FacilitySystemName):
            self.name = FacilitySystemName(self.name)

        if not isinstance(self.facility_identifier, list):
            self.facility_identifier = [self.facility_identifier] if self.facility_identifier is not None else []
        self.facility_identifier = [v if isinstance(v, FacilityIdentifier) else FacilityIdentifier(**as_dict(v)) for v in self.facility_identifier]

        if self.control_system is not None and not isinstance(self.control_system, ControlSystem):
            self.control_system = ControlSystem(**as_dict(self.control_system))

        if self.naming_convention is not None and not isinstance(self.naming_convention, str):
            self.naming_convention = str(self.naming_convention)

        self._normalize_inlined_as_dict(slot_name="signal_definitions", slot_type=SignalDefinitions, key_name="name", keyed=True)

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
    naming_convention: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlSystemName):
            self.name = ControlSystemName(self.name)

        if self.naming_convention is not None and not isinstance(self.naming_convention, str):
            self.naming_convention = str(self.naming_convention)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeviceSystem(System):
    """
    A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the
    instrument as a whole rather than the control system for that instrument. In the SSN graph a DeviceSystem is a
    subsystem of the Facility and a sibling to the ControlSystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["DeviceSystem"]
    class_class_curie: ClassVar[str] = "narad:DeviceSystem"
    class_name: ClassVar[str] = "DeviceSystem"
    class_model_uri: ClassVar[URIRef] = NARAD.DeviceSystem

    name: Union[str, DeviceSystemName] = None
    device_type: Optional[Union[str, "ElementKindEnum"]] = None
    has_sub_system: Optional[Union[Union[str, SystemName], list[Union[str, SystemName]]]] = empty_list()
    subclass_of: Optional[Union[str, SystemName]] = None
    has_system_capability: Optional[Union[Union[str, SystemCapabilityName], list[Union[str, SystemCapabilityName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DeviceSystemName):
            self.name = DeviceSystemName(self.name)

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

        if not isinstance(self.has_sub_system, list):
            self.has_sub_system = [self.has_sub_system] if self.has_sub_system is not None else []
        self.has_sub_system = [v if isinstance(v, SystemName) else SystemName(v) for v in self.has_sub_system]

        if self.subclass_of is not None and not isinstance(self.subclass_of, SystemName):
            self.subclass_of = SystemName(self.subclass_of)

        if not isinstance(self.has_system_capability, list):
            self.has_system_capability = [self.has_system_capability] if self.has_system_capability is not None else []
        self.has_system_capability = [v if isinstance(v, SystemCapabilityName) else SystemCapabilityName(v) for v in self.has_system_capability]

        self._normalize_inlined_as_list(slot_name="has_sub_system", slot_type=System, key_name="name", keyed=True)

        if not isinstance(self.has_system_capability, list):
            self.has_system_capability = [self.has_system_capability] if self.has_system_capability is not None else []
        self.has_system_capability = [v if isinstance(v, SystemCapabilityName) else SystemCapabilityName(v) for v in self.has_system_capability]

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
    for_property: Optional[Union[str, list[str]]] = empty_list()
    device_type: Optional[Union[str, "ElementKindEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SystemCapabilityName):
            self.name = SystemCapabilityName(self.name)

        if not isinstance(self.for_property, list):
            self.for_property = [self.for_property] if self.for_property is not None else []
        self.for_property = [v if isinstance(v, str) else str(v) for v in self.for_property]

        if self.device_type is not None and not isinstance(self.device_type, ElementKindEnum):
            self.device_type = ElementKindEnum(self.device_type)

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
    pv_name: Optional[str] = None
    is_instance_of: Optional[Union[str, list[str]]] = empty_list()
    for_property: Optional[Union[str, list[str]]] = empty_list()
    is_hosted_by: Optional[str] = None
    is_property_of: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InstanceSignalBindingName):
            self.name = InstanceSignalBindingName(self.name)

        if self.pv_name is not None and not isinstance(self.pv_name, str):
            self.pv_name = str(self.pv_name)

        if not isinstance(self.is_instance_of, list):
            self.is_instance_of = [self.is_instance_of] if self.is_instance_of is not None else []
        self.is_instance_of = [v if isinstance(v, str) else str(v) for v in self.is_instance_of]

        if not isinstance(self.for_property, list):
            self.for_property = [self.for_property] if self.for_property is not None else []
        self.for_property = [v if isinstance(v, str) else str(v) for v in self.for_property]

        if self.is_hosted_by is not None and not isinstance(self.is_hosted_by, str):
            self.is_hosted_by = str(self.is_hosted_by)

        if self.is_property_of is not None and not isinstance(self.is_property_of, str):
            self.is_property_of = str(self.is_property_of)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementParamSet(YAMLRoot):
    """
    Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP,
    MagneticMultipoleP, SolenoidP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ElementParamSet"]
    class_class_curie: ClassVar[str] = "narad:ElementParamSet"
    class_name: ClassVar[str] = "ElementParamSet"
    class_model_uri: ClassVar[URIRef] = NARAD.ElementParamSet

    frequency: Optional[float] = None
    voltage: Optional[float] = None
    phase: Optional[float] = None
    angle_ref: Optional[float] = None
    e1: Optional[float] = None
    e2: Optional[float] = None
    Kn1: Optional[float] = None
    Ksol: Optional[float] = None
    facility_param_set: Optional[Union[dict, "FacilityParamSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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

        if self.facility_param_set is not None and not isinstance(self.facility_param_set, FacilityParamSet):
            self.facility_param_set = FacilityParamSet(**as_dict(self.facility_param_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FacilityParamSet(YAMLRoot):
    """
    Facility-specific element parameters block for beamline elements. Differs from an ElementParamSet in that it
    captures facility-specific metadata about the element (e.g. type designation, model name) rather than physics
    parameters.
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
    device_type values in sync with element kind values without circular imports. Values must stay aligned with
    CapabilityProfile.device_type. NOTE: The element_kind of this BeamlineElement must match the device_type of the
    DeviceSystem referenced by is_instance_of.
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
    CavityGradient = PermissibleValue(
        text="CavityGradient",
        description="Accelerating or bunching cavity.")
    RFCavity = PermissibleValue(
        text="RFCavity",
        description="Radio-frequency accelerating or bunching cavity.")
    Instrument = PermissibleValue(
        text="Instrument",
        description="Generic beam diagnostic instrument (halo monitor, viewer, etc.).")
    Magnet = PermissibleValue(
        text="Magnet",
        description="Generic powered magnet device (supertype for all magnet kinds).")

    _defn = EnumDefinition(
        name="ElementKindEnum",
        description="""Controlled vocabulary for beamline element types, shared between the capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here keeps profile device_type values in sync with element kind values without circular imports. Values must stay aligned with CapabilityProfile.device_type. NOTE: The element_kind of this BeamlineElement must match the device_type of the DeviceSystem referenced by is_instance_of.""",
    )

class SystemTypeEnum(EnumDefinitionImpl):
    """
    High-level system type for classification and querying. This is a broad categorization that can be used for
    filtering or grouping systems without needing to traverse the has_sub_system and has_system_capability edges.
    """
    Facility = PermissibleValue(
        text="Facility",
        description="A physical facility or installation (e.g. BTA, CEBAF, or UITF).")
    ControlSystem = PermissibleValue(
        text="ControlSystem",
        description="A control system (e.g. epics) that manages device process variables.")
    Magnet = PermissibleValue(
        text="Magnet",
        description="A powered magnet device/system (generic supertype for all magnet kinds).")

    _defn = EnumDefinition(
        name="SystemTypeEnum",
        description="""High-level system type for classification and querying. This is a broad categorization that can be used for filtering or grouping systems without needing to traverse the has_sub_system and has_system_capability edges.""",
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
        description="""A readable signal that reports a measured or monitored quantity. Differs from status in that it typically indicates a continuous measurement (e.g. current readback, beam position) rather than discrete states.""")
    constraint = PermissibleValue(
        text="constraint",
        description="A signal that defines an operational limit or boundary on a control quantity.")
    status = PermissibleValue(
        text="status",
        description="""A signal reporting the device or system operational state. Differs from readback in that it typically indicates discrete states (e.g. fault, standby, ready) rather than a continuous measurement.""")

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

slots.control_capability = Slot(uri=NARAD.control_capability, name="control_capability", curie=NARAD.curie('control_capability'),
                   model_uri=NARAD.control_capability, domain=None, range=Optional[Union[str, ControlCapabilityName]])

slots.has_system_capability = Slot(uri=NARAD.has_system_capability, name="has_system_capability", curie=NARAD.curie('has_system_capability'),
                   model_uri=NARAD.has_system_capability, domain=System, range=Optional[Union[Union[str, SystemCapabilityName], list[Union[str, SystemCapabilityName]]]])

slots.for_property = Slot(uri=NARAD.for_property, name="for_property", curie=NARAD.curie('for_property'),
                   model_uri=NARAD.for_property, domain=None, range=Optional[Union[str, list[str]]])

slots.is_property_of = Slot(uri=NARAD.is_property_of, name="is_property_of", curie=NARAD.curie('is_property_of'),
                   model_uri=NARAD.is_property_of, domain=None, range=Optional[str])

slots.is_hosted_by = Slot(uri=NARAD.is_hosted_by, name="is_hosted_by", curie=NARAD.curie('is_hosted_by'),
                   model_uri=NARAD.is_hosted_by, domain=None, range=Optional[str])

slots.is_instance_of = Slot(uri=NARAD.is_instance_of, name="is_instance_of", curie=NARAD.curie('is_instance_of'),
                   model_uri=NARAD.is_instance_of, domain=None, range=Optional[Union[str, list[str]]])

slots.subclass_of = Slot(uri=NARAD.subclass_of, name="subclass_of", curie=NARAD.curie('subclass_of'),
                   model_uri=NARAD.subclass_of, domain=None, range=Optional[Union[str, SystemName]])

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

slots.deployed_system = Slot(uri=NARAD.deployed_system, name="deployed_system", curie=NARAD.curie('deployed_system'),
                   model_uri=NARAD.deployed_system, domain=None, range=Optional[Union[str, FacilitySystemName]])

slots.system_type = Slot(uri=NARAD.system_type, name="system_type", curie=NARAD.curie('system_type'),
                   model_uri=NARAD.system_type, domain=None, range=Optional[Union[str, "SystemTypeEnum"]])

slots.control_system = Slot(uri=NARAD.control_system, name="control_system", curie=NARAD.curie('control_system'),
                   model_uri=NARAD.control_system, domain=None, range=Optional[Union[dict, ControlSystem]])

slots.naming_convention = Slot(uri=NARAD.naming_convention, name="naming_convention", curie=NARAD.curie('naming_convention'),
                   model_uri=NARAD.naming_convention, domain=None, range=Optional[str])

slots.control_capability_layer = Slot(uri=NARAD.control_capability_layer, name="control_capability_layer", curie=NARAD.curie('control_capability_layer'),
                   model_uri=NARAD.control_capability_layer, domain=None, range=Union[dict[Union[str, ControlCapabilityName], Union[dict, ControlCapability]], list[Union[dict, ControlCapability]]])

slots.control_capabilities = Slot(uri=NARAD.control_capabilities, name="control_capabilities", curie=NARAD.curie('control_capabilities'),
                   model_uri=NARAD.control_capabilities, domain=None, range=Optional[Union[dict[Union[str, ControlCapabilityName], Union[dict, ControlCapability]], list[Union[dict, ControlCapability]]]])

slots.device_layer = Slot(uri=NARAD.device_layer, name="device_layer", curie=NARAD.curie('device_layer'),
                   model_uri=NARAD.device_layer, domain=None, range=Optional[Union[dict[Union[str, DeviceSystemName], Union[dict, DeviceSystem]], list[Union[dict, DeviceSystem]]]])

slots.facilities = Slot(uri=NARAD.facilities, name="facilities", curie=NARAD.curie('facilities'),
                   model_uri=NARAD.facilities, domain=None, range=Optional[Union[dict[Union[str, FacilitySystemName], Union[dict, FacilitySystem]], list[Union[dict, FacilitySystem]]]])

slots.signal_layer = Slot(uri=NARAD.signal_layer, name="signal_layer", curie=NARAD.curie('signal_layer'),
                   model_uri=NARAD.signal_layer, domain=None, range=Optional[Union[dict, SignalLayer]])

slots.signal_definitions = Slot(uri=NARAD.signal_definitions, name="signal_definitions", curie=NARAD.curie('signal_definitions'),
                   model_uri=NARAD.signal_definitions, domain=None, range=Optional[Union[dict[Union[str, SignalDefinitionsName], Union[dict, SignalDefinitions]], list[Union[dict, SignalDefinitions]]]])

slots.signal_bindings = Slot(uri=NARAD.signal_bindings, name="signal_bindings", curie=NARAD.curie('signal_bindings'),
                   model_uri=NARAD.signal_bindings, domain=None, range=Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.instance_signal_bindings = Slot(uri=NARAD.instance_signal_bindings, name="instance_signal_bindings", curie=NARAD.curie('instance_signal_bindings'),
                   model_uri=NARAD.instance_signal_bindings, domain=None, range=Optional[Union[dict[Union[str, InstanceSignalBindingName], Union[dict, InstanceSignalBinding]], list[Union[dict, InstanceSignalBinding]]]])

slots.capability_class = Slot(uri=NARAD.capability_class, name="capability_class", curie=NARAD.curie('capability_class'),
                   model_uri=NARAD.capability_class, domain=None, range=Optional[str])

slots.class_curie = Slot(uri=NARAD.class_curie, name="class_curie", curie=NARAD.curie('class_curie'),
                   model_uri=NARAD.class_curie, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.signals = Slot(uri=NARAD.signals, name="signals", curie=NARAD.curie('signals'),
                   model_uri=NARAD.signals, domain=None, range=Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]])

slots.device_type = Slot(uri=NARAD.device_type, name="device_type", curie=NARAD.curie('device_type'),
                   model_uri=NARAD.device_type, domain=None, range=Optional[Union[str, "ElementKindEnum"]])

slots.role = Slot(uri=NARAD.role, name="role", curie=NARAD.curie('role'),
                   model_uri=NARAD.role, domain=None, range=Optional[Union[str, "SignalRoleEnum"]])

slots.data_type = Slot(uri=NARAD.data_type, name="data_type", curie=NARAD.curie('data_type'),
                   model_uri=NARAD.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.units = Slot(uri=NARAD.units, name="units", curie=NARAD.curie('units'),
                   model_uri=NARAD.units, domain=None, range=Optional[str])

slots.units_uri = Slot(uri=NARAD.units_uri, name="units_uri", curie=NARAD.curie('units_uri'),
                   model_uri=NARAD.units_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

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

slots.multipass = Slot(uri=NARAD.multipass, name="multipass", curie=NARAD.curie('multipass'),
                   model_uri=NARAD.multipass, domain=None, range=Optional[Union[bool, Bool]])

slots.zero_point = Slot(uri=NARAD.zero_point, name="zero_point", curie=NARAD.curie('zero_point'),
                   model_uri=NARAD.zero_point, domain=None, range=Optional[Union[str, BeamlineElementName]])

slots.periodic = Slot(uri=NARAD.periodic, name="periodic", curie=NARAD.curie('periodic'),
                   model_uri=NARAD.periodic, domain=None, range=Optional[Union[bool, Bool]])

slots.element_kind = Slot(uri=NARAD.element_kind, name="element_kind", curie=NARAD.curie('element_kind'),
                   model_uri=NARAD.element_kind, domain=None, range=Optional[Union[str, "ElementKindEnum"]])

slots.length = Slot(uri=NARAD.length, name="length", curie=NARAD.curie('length'),
                   model_uri=NARAD.length, domain=None, range=Optional[float])

slots.param_set = Slot(uri=NARAD.param_set, name="param_set", curie=NARAD.curie('param_set'),
                   model_uri=NARAD.param_set, domain=None, range=Optional[Union[dict, ElementParamSet]])

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

slots.NaradConfig_deployed_system = Slot(uri=NARAD.deployed_system, name="NaradConfig_deployed_system", curie=NARAD.curie('deployed_system'),
                   model_uri=NARAD.NaradConfig_deployed_system, domain=NaradConfig, range=Union[str, FacilitySystemName])

slots.NaradConfig_has_sub_system = Slot(uri=NARAD.has_sub_system, name="NaradConfig_has_sub_system", curie=NARAD.curie('has_sub_system'),
                   model_uri=NARAD.NaradConfig_has_sub_system, domain=NaradConfig, range=Union[Union[str, ControlSystemName], list[Union[str, ControlSystemName]]])

slots.NaradConfig_device_layer = Slot(uri=NARAD.device_layer, name="NaradConfig_device_layer", curie=NARAD.curie('device_layer'),
                   model_uri=NARAD.NaradConfig_device_layer, domain=NaradConfig, range=Union[dict[Union[str, DeviceSystemName], Union[dict, "DeviceSystem"]], list[Union[dict, "DeviceSystem"]]])

slots.NaradConfig_signal_layer = Slot(uri=NARAD.signal_layer, name="NaradConfig_signal_layer", curie=NARAD.curie('signal_layer'),
                   model_uri=NARAD.NaradConfig_signal_layer, domain=NaradConfig, range=Union[dict, "SignalLayer"])

slots.ControlCapability_signals = Slot(uri=NARAD.signals, name="ControlCapability_signals", curie=NARAD.curie('signals'),
                   model_uri=NARAD.ControlCapability_signals, domain=ControlCapability, range=Union[dict[Union[str, SignalName], Union[dict, "Signal"]], list[Union[dict, "Signal"]]])

slots.SignalDefinitions_signal_bindings = Slot(uri=NARAD.signal_bindings, name="SignalDefinitions_signal_bindings", curie=NARAD.curie('signal_bindings'),
                   model_uri=NARAD.SignalDefinitions_signal_bindings, domain=SignalDefinitions, range=Optional[Union[dict[Union[str, SignalBindingName], Union[dict, "SignalBinding"]], list[Union[dict, "SignalBinding"]]]])

slots.BeamlineElement_is_instance_of = Slot(uri=NARAD.is_instance_of, name="BeamlineElement_is_instance_of", curie=NARAD.curie('is_instance_of'),
                   model_uri=NARAD.BeamlineElement_is_instance_of, domain=BeamlineElement, range=Optional[Union[str, list[str]]])

slots.System_has_sub_system = Slot(uri=NARAD.has_sub_system, name="System_has_sub_system", curie=NARAD.curie('has_sub_system'),
                   model_uri=NARAD.System_has_sub_system, domain=System, range=Optional[Union[dict[Union[str, SystemName], Union[dict, "System"]], list[Union[dict, "System"]]]])

slots.System_has_system_capability = Slot(uri=NARAD.has_system_capability, name="System_has_system_capability", curie=NARAD.curie('has_system_capability'),
                   model_uri=NARAD.System_has_system_capability, domain=System, range=Optional[Union[dict[Union[str, SystemCapabilityName], Union[dict, "SystemCapability"]], list[Union[dict, "SystemCapability"]]]])

slots.DeviceSystem_has_sub_system = Slot(uri=NARAD.has_sub_system, name="DeviceSystem_has_sub_system", curie=NARAD.curie('has_sub_system'),
                   model_uri=NARAD.DeviceSystem_has_sub_system, domain=DeviceSystem, range=Optional[Union[dict[Union[str, SystemName], Union[dict, System]], list[Union[dict, System]]]])

slots.DeviceSystem_has_system_capability = Slot(uri=NARAD.has_system_capability, name="DeviceSystem_has_system_capability", curie=NARAD.curie('has_system_capability'),
                   model_uri=NARAD.DeviceSystem_has_system_capability, domain=DeviceSystem, range=Optional[Union[Union[str, SystemCapabilityName], list[Union[str, SystemCapabilityName]]]])

slots.SystemCapability_for_property = Slot(uri=NARAD.for_property, name="SystemCapability_for_property", curie=NARAD.curie('for_property'),
                   model_uri=NARAD.SystemCapability_for_property, domain=SystemCapability, range=Optional[Union[str, list[str]]])

slots.InstanceSignalBinding_is_instance_of = Slot(uri=NARAD.is_instance_of, name="InstanceSignalBinding_is_instance_of", curie=NARAD.curie('is_instance_of'),
                   model_uri=NARAD.InstanceSignalBinding_is_instance_of, domain=InstanceSignalBinding, range=Optional[Union[str, list[str]]])

slots.InstanceSignalBinding_is_hosted_by = Slot(uri=NARAD.is_hosted_by, name="InstanceSignalBinding_is_hosted_by", curie=NARAD.curie('is_hosted_by'),
                   model_uri=NARAD.InstanceSignalBinding_is_hosted_by, domain=InstanceSignalBinding, range=Optional[str])

slots.InstanceSignalBinding_is_property_of = Slot(uri=NARAD.is_property_of, name="InstanceSignalBinding_is_property_of", curie=NARAD.curie('is_property_of'),
                   model_uri=NARAD.InstanceSignalBinding_is_property_of, domain=InstanceSignalBinding, range=Optional[str])

slots.InstanceSignalBinding_for_property = Slot(uri=NARAD.for_property, name="InstanceSignalBinding_for_property", curie=NARAD.curie('for_property'),
                   model_uri=NARAD.InstanceSignalBinding_for_property, domain=InstanceSignalBinding, range=Optional[Union[str, list[str]]])
