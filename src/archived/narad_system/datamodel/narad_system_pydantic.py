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


metamodel_version = "None"
version = "None"


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

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



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


linkml_meta = LinkMLMeta({'default_prefix': 'narad',
     'default_range': 'string',
     'description': 'LinkML schema for representing NARAD control-system '
                    'semantics, facility-level signal templates, and '
                    'facility-specific instance bindings aligned with SSN, '
                    'SSN-System, and SOSA ontologies. \n'
                    'Main modeling layers:\n'
                    '  - NaradModel — top-level document containing NaradConfig, '
                    'beamlines, and elements\n'
                    '    - NaradConfig — top-level NARAD-system container for the '
                    'capability layer and signal layer\n'
                    '      - ControlCapabilityLayer — reusable control-profile '
                    'families, shared capabilities\n'
                    '      - InstrumentLayer — facility-specific instrument '
                    'definitions -> their  capabilities\n'
                    '      - SignalLayer — facility-specific signal suffix '
                    'templates for system/device types and instance bindings keyed '
                    'by semantic signal name, linked to the\n'
                    '        device type\n'
                    '  - Beamline / BeamlineElement — ordered machine layout of '
                    'the beamline/line\n'
                    '  - Element instances — individual beamline elements with '
                    'applied profiles and instance signal\n'
                    '    bindings, parameters, and optional facility-specific '
                    'parameters\n'
                    '\n'
                    'System hierarchy:\n'
                    '  - System\n'
                    '    - ControlSystem\n'
                    '    - Magnet\n'
                    '      - Quadrupole, Corrector, Dipole, Solenoid\n'
                    '    - Instrument\n'
                    '      - BPM\n'
                    '    - RFCavity\n'
                    '    - Marker\n'
                    '    - Drift\n'
                    '\n'
                    'Control Capability hierarchy:\n'
                    '  - SystemCapability\n'
                    '    - MagnetCapability\n'
                    '      - QuadrupoleCapability, CorrectorKickCapability, '
                    'DipoleCapability\n'
                    '    - InstrumentCapability\n'
                    '    - BPMCapability\n'
                    '    - CavityGradientCapability\n'
                    '\n'
                    'Signal modeling:\n'
                    '  - Signal — abstract control-system quantity\n'
                    '    - ObservableSignal — readback, constraint, and status '
                    'quantities\n'
                    '    - ActuatableSignal — writable/control setpoints\n'
                    '  - SignalBinding — signal template or suffix definition in '
                    'the signal layer\n'
                    '  - InstanceSignalBinding — facility-specific PV binding '
                    'attached to a beamline element\n'
                    '\n'
                    'Serialization conventions:\n'
                    '  - beamlines are keyed by beamline name\n'
                    '  - signals are keyed by semantic signal name\n'
                    '  - signal bindings are created through the is_observed_by '
                    'relationship to  and are keyed by semantic signal name\n'
                    '\n'
                    'Alignments with PALS (Particle Accelerator Language '
                    'Standard):\n'
                    '  - Beamline aligns with pals:BeamLine\n'
                    '  - BeamlineElement aligns with pals:Element\n'
                    '  - Instrument aligns with pals:Instrument\n'
                    '  - Dipole aligns with pals:Multipole\n'
                    '  - Quadrupole aligns with pals:Quadrupole\n'
                    '  - Solenoid aligns with pals:Solenoid\n'
                    '  - RFCavity aligns with pals:RFCavity\n'
                    '\n'
                    'Additional Notes on Usage: 1. On Signal, and '
                    'InstanceSignalBinding: These classes represent different '
                    'levels of abstraction in the signal modeling.  Signal defines '
                    'the abstract control-system quantity (e.g. current_readback), '
                    'SignalBinding captures the control system suffix convention '
                    'for that signal (e.g. .R for EPICS readback),  and '
                    'InstanceSignalBinding represents the concrete binding of that '
                    'signal to a specific beamline element instance, for example, '
                    'MQWK202.S or RK11:GSET, depending on the facility naming '
                    'convention.  The semantic signal name (e.g. current_readback) '
                    'is the key that links these layers together, while the '
                    'control-system suffix (e.g. .R)  is captured in the '
                    'InstanceSignalBinding. 2. On the distinction between '
                    'is_instance_of, facility_element_type, and device_type:\n'
                    '  - BeamlineElement.is_instance_of identifies the element’s '
                    'semantic class, device_type classifies capability or '
                    'signal-definition scope, and facility_element_type records '
                    'facility-local designation.\n'
                    '  - facility_element_type '
                    '(FacilityParamSet.facility_element_type) is an optional slot '
                    'for recording the facility-specific type designation for this '
                    'element, if it differs from the generic element_kind. \n'
                    '  - device_type (Capability.device_type) is the generic '
                    'element type used for capability profile matching \n'
                    '  and signal definition scoping, while facility_element_type '
                    'captures the facility-specific type designation that may be '
                    'used in the control system naming convention \n'
                    '  or for other facility-specific purposes.\n'
                    '  For example, a facility might have its own naming '
                    "convention for magnet types that doesn't align one-to-one "
                    'with the ElementKindEnum values.\n'
                    '3. Expected CURIE usage for is_instance_of, is_hosted_by, and '
                    'is_property_of: \n'
                    '  - is_instance_of typically points to the semantic class '
                    'instantiated by the binding or element, using a CURIE such as '
                    'narad:CavityGradientCapability if that is your intended '
                    'convention.\n'
                    '  - is_hosted_by typically points to the FacilitySystem this '
                    'binding belongs to, e.g. narad:UITF.\n'
                    '  - is_property_of typically points to the ControlSystem that '
                    'implements this binding, e.g. narad:epics.\n'
                    '4. Open and constrained vocabularies:\n'
                    '  - ElementKindEnum provides a controlled vocabulary for key '
                    'classification slots, but the schema is designed to be '
                    'extensible \n'
                    '  with new enum values as needed.\n'
                    '  - SystemTypeEnum is a high-level classification for systems '
                    'that can be used for querying and filtering, \n'
                    '  but it is not intended to capture all the nuance of device '
                    'types or capabilities.\n'
                    '  - DataTypeEnum and SignalRoleEnum provide a controlled '
                    'vocabulary for signal data types and roles, \n'
                    '  but the schema allows for additional values to be added as '
                    'needed.\n'
                    '  - IdentifierTypeEnum provides a controlled vocabulary for '
                    'types of identifiers used in FacilityIdentifier, \n'
                    '  but it can be extended to apply to other entities, and with '
                    'additional identifier types as needed.\n'
                    '  - The properties slot in FacilityParamSet allows for '
                    'open-ended key-value pairs to capture any additional \n'
                    "  facility-specific parameters that don't fit into the "
                    'predefined schema structure.\n'
                    '\n'
                    'Needed Custom Validations:\n'
                    '  - Validation to ensure that the element_kind of a '
                    'BeamlineElement matches the device_type of the Device it is '
                    'an instance of.\n'
                    '  - Validation to ensure that the value of is_property_of in '
                    'InstanceSignalBinding matches one of the control systems '
                    'listed in narad_config.has_sub_system.\n'
                    '  - Validation that each signal_layer -> facilities -> '
                    'FacilitySystem -> control_system value has a corresponding '
                    'entry in narad_config.has_sub_system to ensure that all '
                    'control systems referenced in the signal layer are defined in '
                    'the capability layer.\n'
                    '  - Validation that the signal_bindings defined for a given '
                    'device_type in the signal layer align with the signals '
                    'defined in the capability profiles and instrument systems for '
                    'that device type.\n',
     'id': 'https://w3id.org/narad_linkml/schema/narad/system',
     'imports': ['linkml:types'],
     'name': 'narad-system-schema',
     'prefixes': {'acc-core': {'prefix_prefix': 'acc-core',
                               'prefix_reference': 'https://example.org/acc-core/schema/acc-core/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'narad': {'prefix_prefix': 'narad',
                            'prefix_reference': 'https://example.org/narad_linkml/schema/narad/'},
                  'ncit': {'prefix_prefix': 'ncit',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ncit.owl'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'pals': {'prefix_prefix': 'pals',
                           'prefix_reference': 'https://pals-project.readthedocs.io/en/latest/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'si-unit': {'prefix_prefix': 'si-unit',
                              'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'sosa': {'prefix_prefix': 'sosa',
                           'prefix_reference': 'http://www.w3.org/ns/sosa/'},
                  'ssn': {'prefix_prefix': 'ssn',
                          'prefix_reference': 'http://www.w3.org/ns/ssn/'},
                  'ssn-system': {'prefix_prefix': 'ssn-system',
                                 'prefix_reference': 'http://www.w3.org/ns/ssn/systems/'}},
     'source_file': 'src/narad_system/schema/narad_system.yaml',
     'subsets': {'base_class': {'description': 'Base classes that are not intended '
                                               'to be instantiated directly but '
                                               'provide shared properties for '
                                               'subclasses.',
                                'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
                                'name': 'base_class'},
                 'instance': {'description': 'Instances of systems, capabilities, '
                                             'and signals that represent concrete '
                                             'entities in the graph.',
                              'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
                              'name': 'instance'},
                 'label': {'description': 'Slots that serve as labels or '
                                          'properties of base classes or instances '
                                          'rather than relationships between '
                                          'entities.',
                           'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
                           'name': 'label'},
                 'physical_device': {'description': 'Physical beamline devices '
                                                    'that interact with the beam, '
                                                    'including magnets and '
                                                    'instruments.',
                                     'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
                                     'name': 'physical_device'},
                 'relationship': {'description': 'Relationships between systems, '
                                                 'capabilities, and signals, '
                                                 'including system decomposition '
                                                 'and capability assignment.',
                                  'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
                                  'name': 'relationship'}}} )

class ElementKindEnum(str, Enum):
    """
    Controlled vocabulary for beamline element types, shared between the capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here keeps profile device_type values in sync with element kind values without circular imports. Values must stay aligned with CapabilityProfile.device_type. NOTE: The kind of a BeamlineElement must match the device_type of the Device referenced by is_instance_of.
    """
    Drift = "Drift"
    """
    A field-free drift space between elements.
    """
    Marker = "Marker"
    """
    A zero-length reference point or survey marker.
    """
    BPM = "BPM"
    """
    Beam Position Monitor.
    """
    Corrector = "Corrector"
    """
    Dipole corrector magnet for orbit correction.
    """
    Dipole = "Dipole"
    """
    Dipole bending magnet.
    """
    Quadrupole = "Quadrupole"
    """
    Quadrupole focusing/defocusing magnet.
    """
    Solenoid = "Solenoid"
    """
    Solenoid magnet.
    """
    CavityGradient = "CavityGradient"
    """
    Accelerating or bunching cavity.
    """
    RFCavity = "RFCavity"
    """
    Radio-frequency accelerating or bunching cavity.
    """
    Instrument = "Instrument"
    """
    Generic beam diagnostic instrument (halo monitor, viewer, etc.).
    """
    Magnet = "Magnet"
    """
    Generic powered magnet device (supertype for all magnet kinds).
    """


class SystemTypeEnum(str, Enum):
    """
    High-level system type for classification and querying. This is a broad categorization that can be used for filtering or grouping systems without needing to traverse the has_sub_system and has_system_capability edges.
    """
    Facility = "Facility"
    """
    A physical facility or installation (e.g. BTA, CEBAF, or UITF).
    """
    ControlSystem = "ControlSystem"
    """
    A control system (e.g. epics) that manages device process variables.
    """
    Magnet = "Magnet"
    """
    A powered magnet device/system (generic supertype for all magnet kinds).
    """


class DataTypeEnum(str, Enum):
    """
    Allowed data types for signal values.
    """
    int = "int"
    """
    Integer.
    """
    float = "float"
    """
    Single-precision floating-point.
    """
    double = "double"
    """
    Double-precision floating-point.
    """
    string = "string"
    """
    Text string.
    """
    boolean = "boolean"
    """
    True/false value.
    """
    coded_value = "coded_value"
    """
    A code referenced from an external coding system.
    """


class SignalRoleEnum(str, Enum):
    """
    Controlled vocabulary for the semantic role of a signal within a capability.
    """
    control = "control"
    """
    A writable signal that commands a device setpoint.
    """
    readback = "readback"
    """
    A readable signal that reports a measured or monitored quantity. Differs from status in that it typically indicates a continuous measurement (e.g. current readback, beam position) rather than discrete states.
    """
    constraint = "constraint"
    """
    A signal that defines an operational limit or boundary on a control quantity.
    """
    status = "status"
    """
    A signal reporting the device or system operational state. Differs from readback in that it typically indicates discrete states (e.g. fault, standby, ready) rather than a continuous measurement.
    """


class IdentifierTypeEnum(str, Enum):
    """
    Allowed identifier types for facilities and other entities.
    """
    doi = "doi"
    """
    Digital Object Identifier (DOI).
    """
    ark = "ark"
    """
    Archival Resource Key (ARK).
    """
    handle = "handle"
    """
    Handle System identifier.
    """
    url = "url"
    """
    Uniform Resource Locator (URL).
    """
    local = "local"
    """
    Local identifier unique within a specific context or namespace.
    """
    other = "other"
    """
    Any other type of identifier not covered by the above categories.
    """



class NamedThing(ConfiguredBaseModel):
    """
    Abstract base class providing identity and human-readable metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class NaradModel(ConfiguredBaseModel):
    """
    Top-level NARAD document container.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'tree_root': True})

    narad_config: Optional[NaradConfig] = Field(default=None, description="""Top-level NARAD configuration block (capability_layer + signal_layer).""", json_schema_extra = { "linkml_meta": {'aliases': ['narad'], 'domain_of': ['NaradModel']} })
    beamlines: Optional[dict[str, Beamline]] = Field(default=None, description="""A top-level NARAD-system container for the ordered beamline definitions keyed by beamline name. Serializes as a keyed map by beamline name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradModel']} })
    elements: Optional[list[BeamlineElement]] = Field(default=[], description="""Beamline element definitions referenced by name from beamline sequences. Serializes as a keyed map by element name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradModel']} })


class NaradConfig(ConfiguredBaseModel):
    """
    A top-level NARAD-system container for the: capability layer + signal layer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['ssn:Deployment'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'control_system': {'description': 'Identifier of the control '
                                                          'system (e.g. epics) this '
                                                          'configuration describes.',
                                           'multivalued': False,
                                           'name': 'control_system',
                                           'range': 'ControlSystem',
                                           'required': True},
                        'deployed_system': {'description': 'Identifier of the deployed '
                                                           'system this configuration '
                                                           'describes.',
                                            'inlined': True,
                                            'multivalued': False,
                                            'name': 'deployed_system',
                                            'range': 'DeployedSystem',
                                            'required': True},
                        'device_layer': {'description': 'Device Capability definitions '
                                                        'keyed by capability name.',
                                         'inlined': True,
                                         'multivalued': True,
                                         'name': 'device_layer',
                                         'range': 'Device',
                                         'required': True},
                        'schema_version': {'description': 'Version of the NARAD schema '
                                                          'used in this document.',
                                           'name': 'schema_version',
                                           'range': 'string',
                                           'required': True},
                        'signal_layer': {'description': 'Signal-layer container for '
                                                        'facility-specific signal '
                                                        'bindings.',
                                         'inlined': False,
                                         'name': 'signal_layer',
                                         'range': 'SignalLayer',
                                         'required': True}}})

    schema_version: str = Field(default=..., description="""Version of the NARAD schema used in this document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig'], 'in_subset': ['label']} })
    intent: Optional[str] = Field(default=None, description="""A human-readable statement of the intended use or purpose of this NARAD configuration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig'], 'in_subset': ['label']} })
    deployed_system: DeployedSystem = Field(default=..., description="""Identifier of the deployed system this configuration describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig'], 'in_subset': ['instance']} })
    control_system: ControlSystem = Field(default=..., description="""Identifier of the control system (e.g. epics) this configuration describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig'], 'in_subset': ['instance']} })
    capability_layer: dict[str, Capability] = Field(default=..., description="""Control Capability definitions for this facility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })
    device_layer: dict[str, Device] = Field(default=..., description="""Device Capability definitions keyed by capability name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })
    signal_layer: SignalLayer = Field(default=..., description="""Signal-layer container for facility-specific signal bindings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })


class CapabilityLayer(ConfiguredBaseModel):
    """
    Capability-layer container for control profile families.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    capabilities: Optional[dict[str, Capability]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CapabilityLayer']} })


class Capability(NamedThing):
    """
    A reusable device-type control profile that extends a generic shared capability with type-specific signals (e.g. QuadrupoleCurrentControlProfile).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'has_signal': {'name': 'has_signal', 'required': True},
                        'is_property_of': {'description': 'Links the capability layer '
                                                          'to the control systems it '
                                                          'applies to via '
                                                          'ssn:isPropertyOf.',
                                           'inlined': False,
                                           'multivalued': False,
                                           'name': 'is_property_of',
                                           'range': 'ControlSystem'},
                        'subclass_of': {'description': 'Links a type-specific '
                                                       'capability to the generic '
                                                       'capability it extends via '
                                                       'rdfs:subClassOf.',
                                        'inlined': False,
                                        'multivalued': False,
                                        'name': 'subclass_of',
                                        'range': 'Capability'}}})

    device_type: Optional[ElementKindEnum] = Field(default=None, description="""Represents the generic, semantic class of the device (e.g., \"Quadrupole\", \"BPM\") and is used for capability, instrument, and signal profile matching.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability', 'Device', 'SystemCapability'],
         'in_subset': ['label']} })
    subclass_of: Optional[str] = Field(default=None, description="""Links a type-specific capability to the generic capability it extends via rdfs:subClassOf.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability', 'Device'],
         'exact_mappings': ['rdfs:subClassOf'],
         'in_subset': ['relationship']} })
    has_signal: dict[str, Signal] = Field(default=..., description="""Signals within a capability, keyed by a semantic signal name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability'], 'in_subset': ['relationship']} })
    is_property_of: Optional[str] = Field(default=None, description="""Links the capability layer to the control systems it applies to via ssn:isPropertyOf.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['ssn:isPropertyOf'],
         'domain_of': ['Capability', 'InstanceSignalBinding'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class SignalLayer(ConfiguredBaseModel):
    """
    Signal-layer container for facility-specific signal bindings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    facilities: Optional[dict[str, FacilitySystem]] = Field(default=None, description="""Facility-specific signal binding configurations keyed by facility name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalLayer']} })


class FacilityIdentifier(ConfiguredBaseModel):
    """
    A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    identifier_type: Optional[IdentifierTypeEnum] = Field(default=None, description="""The type of identifier used in the identifier slot (e.g. DOI, ARK, URL, local).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FacilityIdentifier'], 'in_subset': ['label']} })
    identifier_value: Optional[str] = Field(default=None, description="""The value of the identifier (e.g. the DOI string, ARK string, URL string, or local ID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FacilityIdentifier'], 'in_subset': ['label']} })


class SignalBinding(NamedThing):
    """
    A named control system suffix definition for one semantic signal. The suffix is used within in a template naming convention to construct the full control system PV name for a given device instance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    signal_code_suffix: Optional[str] = Field(default=None, description="""Facility-specific control-system (e.g. EPICS) naming suffix used to derive or interpret the signal binding, e.g. .S, M, :GSET.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding'], 'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class Beamline(NamedThing):
    """
    A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BeamLine'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    multipass: Optional[bool] = Field(default=None, description="""Indicates whether this beamline is a multipass recirculating line (true) or a single-pass line (false).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline'], 'in_subset': ['label']} })
    length: Optional[float] = Field(default=None, description="""Physical length of the element in meters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline', 'BeamlineElement'], 'in_subset': ['label']} })
    zero_point: Optional[str] = Field(default=None, description="""Name of a line item used as a reference point when  the beamline is used as a subline.\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline'], 'in_subset': ['label']} })
    periodic: Optional[bool] = Field(default=None, description="""For a beamline, indicates whether the orbit and Twiss parameters are periodic (true) or non-periodic (false).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline'], 'in_subset': ['label']} })
    line: Optional[list[str]] = Field(default=[], description="""Ordered sequence of beamline elements in this beamline. Serializes as a list of element names (BeamlineElement names) referencing the keys in the elements map This is not a direct containment slot; the actual element definitions are in the top-level elements map.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class BeamlineElement(NamedThing):
    """
    A single element in a beamline with its kind and optional NARAD capability annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'is_instance_of': {'multivalued': False,
                                           'name': 'is_instance_of',
                                           'range': 'ElementKindEnum'},
                        'is_observed_by': {'name': 'is_observed_by',
                                           'range': 'InstanceSignalBinding'}}})

    is_instance_of: Optional[ElementKindEnum] = Field(default=None, description="""NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Class that implements the signal binding.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement', 'InstanceSignalBinding'],
         'exact_mappings': ['rdf:type'],
         'in_subset': ['relationship']} })
    length: Optional[float] = Field(default=None, description="""Physical length of the element in meters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline', 'BeamlineElement'], 'in_subset': ['label']} })
    is_observed_by: Optional[dict[str, InstanceSignalBinding]] = Field(default=None, description="""Control-system-specific, e.g. EPICS, suffix definitions keyed by signal name within a device/domain set. Can also be used to link a BeamlineElement instance to the signal bindings that observe or actuate it,  since the instance of the element is directly observed or controlled through a Device. Facility-specific bindings of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline element instance. These are the keyed by the semantic signal name (e.g. current_readback) rather than the control-system suffix, which is captured in the SignalBinding. The semantic signal name links the instance binding to the abstract Signal definition and its place in the capability profile, while the SignalBinding captures the concrete implementations of the abstract SignalBindings referenced by the element's capability profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement', 'Device'], 'in_subset': ['relationship']} })
    param_set: Optional[ElementParamSet] = Field(default=None, description="""Named physics-parameter blocks for this element (e.g. RFP, BendP, MagneticMultipoleP).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class System(NamedThing):
    """
    A physical, logical, or cyber-physical system involved in sensing, monitoring, control, or actuation. Broadly aligned to ssn:System.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['ssn:System'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'has_sub_system': {'inlined_as_list': True,
                                           'name': 'has_sub_system',
                                           'range': 'System'},
                        'has_system_capability': {'inlined': True,
                                                  'multivalued': True,
                                                  'name': 'has_system_capability',
                                                  'range': 'SystemCapability'}}})

    system_type: Optional[SystemTypeEnum] = Field(default=None, description="""High-level system type for classification and querying.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System'], 'in_subset': ['label']} })
    has_sub_system: Optional[list[System]] = Field(default=[], description="""Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSubSystem'],
         'in_subset': ['relationship']} })
    has_system_capability: Optional[dict[str, SystemCapability]] = Field(default=None, description="""Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSystemCapability'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class FacilitySystem(System):
    """
    Facility-specific signal binding configuration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    has_control_system: Optional[str] = Field(default=None, description="""Relates a System to one of its control systems (SSN alignment to sub system). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['ssn-system:hasSubSystem'],
         'domain': 'System',
         'domain_of': ['FacilitySystem', 'DeployedSystem'],
         'in_subset': ['relationship']} })
    hosts_device: Optional[dict[str, Device]] = Field(default=None, description="""Structured container for facility-specific signal suffix templates.""", json_schema_extra = { "linkml_meta": {'domain': 'FacilitySystem',
         'domain_of': ['FacilitySystem'],
         'in_subset': ['relationship']} })
    system_type: Optional[SystemTypeEnum] = Field(default=None, description="""High-level system type for classification and querying.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System'], 'in_subset': ['label']} })
    has_sub_system: Optional[list[System]] = Field(default=[], description="""Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSubSystem'],
         'in_subset': ['relationship']} })
    has_system_capability: Optional[dict[str, SystemCapability]] = Field(default=None, description="""Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSystemCapability'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class DeployedSystem(System):
    """
    A deployed system, with an identified facility, that is the subject of a NARAD configuration.  This is the child of the target of the narad_config.deployed_system slot. In the SSN graph a DeployedSystem is a broad mapping to the ssn:Deployment and also is equivalent to the signal_layers.facilities entries.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['ssn:Deployment', 'ssn-system:System'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'has_control_system': {'name': 'has_control_system',
                                               'required': False},
                        'has_system_capability': {'multivalued': True,
                                                  'name': 'has_system_capability',
                                                  'required': True},
                        'system_type': {'description': 'High-level system type for '
                                                       'classification and querying - '
                                                       'set to Facility for all '
                                                       'DeployedSystem instances.',
                                        'name': 'system_type',
                                        'range': 'SystemTypeEnum'}}})

    facility_identifier: Optional[list[FacilityIdentifier]] = Field(default=[], description="""Globally unique identifier for the facility, with specified type and value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DeployedSystem']} })
    has_control_system: Optional[str] = Field(default=None, description="""Relates a System to one of its control systems (SSN alignment to sub system). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['ssn-system:hasSubSystem'],
         'domain': 'System',
         'domain_of': ['FacilitySystem', 'DeployedSystem'],
         'in_subset': ['relationship']} })
    system_type: Optional[SystemTypeEnum] = Field(default=None, description="""High-level system type for classification and querying - set to Facility for all DeployedSystem instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System'], 'in_subset': ['label']} })
    has_sub_system: Optional[list[System]] = Field(default=[], description="""Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSubSystem'],
         'in_subset': ['relationship']} })
    has_system_capability: dict[str, SystemCapability] = Field(default=..., description="""Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSystemCapability'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class ControlSystem(System):
    """
    A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a subsystem of the Facility.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['ssn:System'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'has_naming_convention': {'inlined': True,
                                                  'multivalued': True,
                                                  'name': 'has_naming_convention',
                                                  'range': 'NamingConvention'},
                        'has_sub_system': {'name': 'has_sub_system', 'required': False},
                        'has_system_capability': {'name': 'has_system_capability',
                                                  'required': False},
                        'system_type': {'description': 'High-level system type for '
                                                       'classification and querying - '
                                                       'set to ControlSystem for all '
                                                       'ControlSystem instances.',
                                        'name': 'system_type',
                                        'range': 'SystemTypeEnum'}}})

    has_naming_convention: Optional[list[NamingConvention]] = Field(default=[], description="""Signal naming conventions used by this control system defined in a machine actionable manner.  This is where you would capture the patterns/templates for how control system PVs or signals are constructed for this control system,  for example, the EPICS convention of using suffixes like .R, .S, :GSET to indicate readback, status, and setpoint signals. Multiple naming conventions can be captured if a control system uses more than one convention for different device types or domains.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlSystem']} })
    system_type: Optional[SystemTypeEnum] = Field(default=None, description="""High-level system type for classification and querying - set to ControlSystem for all ControlSystem instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System'], 'in_subset': ['label']} })
    has_sub_system: Optional[list[System]] = Field(default=[], description="""Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSubSystem'],
         'in_subset': ['relationship']} })
    has_system_capability: Optional[dict[str, SystemCapability]] = Field(default=None, description="""Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSystemCapability'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class Device(System):
    """
    A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the instrument as a whole rather than the control system for that instrument. In the SSN graph a Device is a subsystem of the Facility and a sibling to the ControlSystem. Also used in the SignalLayer to group signal bindings by device type. Aligned to ssn:System.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Element'],
         'exact_mappings': ['ssn:System'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'device_type': {'name': 'device_type', 'required': True},
                        'has_sub_system': {'inlined_as_list': True,
                                           'multivalued': True,
                                           'name': 'has_sub_system',
                                           'range': 'System'},
                        'has_system_capability': {'inlined': False,
                                                  'multivalued': False,
                                                  'name': 'has_system_capability',
                                                  'range': 'SystemCapability'},
                        'is_observed_by': {'inlined': True,
                                           'multivalued': True,
                                           'name': 'is_observed_by'}}})

    device_type: ElementKindEnum = Field(default=..., description="""Represents the generic, semantic class of the device (e.g., \"Quadrupole\", \"BPM\") and is used for capability, instrument, and signal profile matching.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability', 'Device', 'SystemCapability'],
         'in_subset': ['label']} })
    has_sub_system: Optional[list[System]] = Field(default=[], description="""Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSubSystem'],
         'in_subset': ['relationship']} })
    subclass_of: Optional[str] = Field(default=None, description="""-> NARAD alias for rdfs:subClassOf. Links a type-specific capability to the generic capability it extends. In the graph this edge is labelled narad:subclassOf.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability', 'Device'],
         'exact_mappings': ['rdfs:subClassOf'],
         'in_subset': ['relationship']} })
    has_system_capability: Optional[str] = Field(default=None, description="""Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSystemCapability'],
         'in_subset': ['relationship']} })
    is_observed_by: Optional[dict[str, SignalBinding]] = Field(default=None, description="""Control-system-specific, e.g. EPICS, suffix definitions keyed by signal name within a device/domain set. Can also be used to link a BeamlineElement instance to the signal bindings that observe or actuate it,  since the instance of the element is directly observed or controlled through a Device. Facility-specific bindings of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline element instance. These are the keyed by the semantic signal name (e.g. current_readback) rather than the control-system suffix, which is captured in the SignalBinding. The semantic signal name links the instance binding to the abstract Signal definition and its place in the capability profile, while the SignalBinding captures the concrete implementations of the abstract SignalBindings referenced by the element's capability profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement', 'Device'], 'in_subset': ['relationship']} })
    system_type: Optional[SystemTypeEnum] = Field(default=None, description="""High-level system type for classification and querying.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System'], 'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class NamingConventionExample(ConfiguredBaseModel):
    """
    An example of a control system naming convention, illustrating how the template is used to generate full control system PV names from semantic signal names and device instance information.  This can be used to provide concrete examples of the expected PV naming convention for different device types and signals based on the defined NamingConvention template.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'example': {'identifier': True, 'name': 'example'}}})

    example: str = Field(default=..., description="""A single example of how this naming convention is applied to a specific device instance and signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class Instrument(System):
    """
    A generic beam diagnostic instrument.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['ssn:System'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    system_type: Optional[SystemTypeEnum] = Field(default=None, description="""High-level system type for classification and querying.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System'], 'in_subset': ['label']} })
    has_sub_system: Optional[list[System]] = Field(default=[], description="""Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSubSystem'],
         'in_subset': ['relationship']} })
    has_system_capability: Optional[dict[str, SystemCapability]] = Field(default=None, description="""Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
""", json_schema_extra = { "linkml_meta": {'domain': 'System',
         'domain_of': ['System', 'Device'],
         'exact_mappings': ['ssn-system:hasSystemCapability'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class SystemCapability(NamedThing):
    """
    A capability of a system. SystemCapability describes what a system can expose, monitor, control, or actuate with respect to one or more signals. Aligned to ssn-system:SystemCapability; linked from System instances via ssn-system:hasSystemCapability, and from Signals via ssn:forProperty. Profile-level inheritance (shared vs. type-specific signals) is expressed in CapabilityProfile, not here.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['ssn-system:SystemCapability'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'for_property': {'multivalued': True, 'name': 'for_property'}}})

    for_property: Optional[list[str]] = Field(default=[], description="""SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemCapability', 'InstanceSignalBinding'],
         'exact_mappings': ['ssn:forProperty'],
         'in_subset': ['relationship']} })
    device_type: Optional[ElementKindEnum] = Field(default=None, description="""Represents the generic, semantic class of the device (e.g., \"Quadrupole\", \"BPM\") and is used for capability, instrument, and signal profile matching.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability', 'Device', 'SystemCapability'],
         'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class NamingConvention(NamedThing):
    """
    A template for constructing facility-specific signal names from a semantic signal name and a control-system-specific suffix.  The template is used to generate the full control system PV name for a given device instance and semantic signal by substituting the device name and signal code suffix into the template.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    template: Optional[str] = Field(default=None, description="""A template string for constructing control system PV names based on the semantic signal name and device instance. This can include placeholders for the device name and signal suffix, e.g. {device_name}{signal_suffix}.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamingConvention'], 'in_subset': ['label']} })
    template_components: Optional[list[TemplateComponent]] = Field(default=[], description="""Structured components of the naming convention template, for capturing the template in a more machine-actionable way than a raw string.  For example, you could have components for the device name, signal suffix, and any fixed parts of the naming convention.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamingConvention']} })
    full_pattern: Optional[str] = Field(default=None, description="""A regex pattern that the full resolved value (e.g. after template substitution) must match for validation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamingConvention'], 'in_subset': ['label']} })
    examples: Optional[list[NamingConventionExample]] = Field(default=[], description="""Examples of how this naming convention is applied to specific device instances and signals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamingConvention']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class TemplateComponent(NamedThing):
    """
    A component of a naming convention template, representing a variable part of the control system PV name that is substituted based on the device instance and signal definition.  For example, in the template \"{device_name}{signal_code_suffix}\", \"device_name\" and \"signal_code_suffix\" would be TemplateComponents that are replaced with the actual device name and signal code suffix for each specific binding.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    required: Optional[bool] = Field(default=None, description="""Indicates whether this configuration element is required for a valid configuration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemplateComponent'], 'in_subset': ['label']} })
    pattern: Optional[str] = Field(default=None, description="""A regex pattern that the value of this slot must match for validation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemplateComponent'], 'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class TemplateExample(ConfiguredBaseModel):
    """
    An example of a control system PV name generated from a naming convention template, along with a description of what it represents.  This can be used to illustrate how the template works in practice and to provide concrete examples of the expected PV naming convention for different device types and signals.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'example': {'identifier': True, 'name': 'example'}}})

    example: str = Field(default=..., description="""A single example of how this naming convention is applied to a specific device instance and signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class Signal(NamedThing):
    """
    Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The concrete facility binding is captured in SignalBinding.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['epics_pv',
                     'pv',
                     'process_variable',
                     'EPICS Process Variable',
                     'control signal',
                     'control-system signal'],
         'broad_mappings': ['sosa:Property', 'ssn:Property', 'qudt:QuantityKind'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    role: Optional[SignalRoleEnum] = Field(default=None, description="""The semantic role of the signal within its capability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""The data type of the signal's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    units: Optional[str] = Field(default=None, description="""Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    units_uri: Optional[str] = Field(default=None, description="""Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class ObservableSignal(Signal):
    """
    A NARAD signal that is read, monitored, observed, or exposed by a system. Examples: current_readback, status, horizontal_beam_position, gradient_readback. Aligned to sosa:ObservableProperty.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['sosa:ObservableProperty'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    role: Optional[SignalRoleEnum] = Field(default=None, description="""The semantic role of the signal within its capability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""The data type of the signal's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    units: Optional[str] = Field(default=None, description="""Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    units_uri: Optional[str] = Field(default=None, description="""Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class ActuatableSignal(Signal):
    """
    A NARAD signal that can be commanded, set, or acted upon. Examples: current_setpoint, strength_setpoint, kick_setpoint, field_setpoint, current_min, current_max, gradient_setpoint. Aligned to sosa:ActuatableProperty.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['sosa:ActuatableProperty'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    role: Optional[SignalRoleEnum] = Field(default=None, description="""The semantic role of the signal within its capability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""The data type of the signal's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    units: Optional[str] = Field(default=None, description="""Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    units_uri: Optional[str] = Field(default=None, description="""Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal'], 'in_subset': ['label']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class InstanceSignalBinding(NamedThing):
    """
    A facility-specific binding between a NARAD Signal and an implementation interface (e.g. an EPICS process variable). Modeled as sosa:Sensor because it describes how a signal is observed, monitored, or actuated. ssn:forProperty → Signal; narad:isInstanceOf → the capability class.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['rdf:type', 'sosa:Sensor'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system',
         'slot_usage': {'for_property': {'multivalued': False,
                                         'name': 'for_property',
                                         'range': 'SignalBinding'},
                        'is_hosted_by': {'multivalued': False,
                                         'name': 'is_hosted_by',
                                         'range': 'string'},
                        'is_instance_of': {'multivalued': False,
                                           'name': 'is_instance_of',
                                           'range': 'Signal'},
                        'is_property_of': {'multivalued': False,
                                           'name': 'is_property_of',
                                           'range': 'ControlSystem'}}})

    pv_name: Optional[str] = Field(default=None, description="""Fully-resolved facility-specific process variable name, e.g. MQWK202:STAT or MQWK202:BDL.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['InstanceSignalBinding'], 'in_subset': ['label']} })
    is_instance_of: Optional[str] = Field(default=None, description="""NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Class that implements the signal binding.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement', 'InstanceSignalBinding'],
         'exact_mappings': ['rdf:type'],
         'in_subset': ['relationship']} })
    for_property: Optional[str] = Field(default=None, description="""SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemCapability', 'InstanceSignalBinding'],
         'exact_mappings': ['ssn:forProperty'],
         'in_subset': ['relationship']} })
    is_hosted_by: Optional[str] = Field(default=None, description="""Links an InstanceSignalBinding to the FacilitySystem it belongs to. This is the edge that connects the facility-specific bindings to the Facility node in the graph.
""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['ssn-system:hasSubSystem', 'ssn:isHostedBy'],
         'domain_of': ['InstanceSignalBinding'],
         'in_subset': ['relationship']} })
    is_property_of: Optional[str] = Field(default=None, description="""Inverse of for_property: links the Class Signal to the Class of SignalBinding Procedure that implements it. This can also link the Instance of a SignalBinding to the ControlSystem that implements it. This is the edge that connects the signal definitions to the facility-specific bindings in the graph. Values are typically the ControlSystem that implements this binding, e.g. narad:epics (for EPICS control system). NOTE: The value of this slot must match one of the values in narad_config.has_sub_system.
""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['ssn:isPropertyOf'],
         'domain_of': ['Capability', 'InstanceSignalBinding'],
         'in_subset': ['relationship']} })
    name: str = Field(default=..., description="""Human-readable name or local string key for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'in_subset': ['label']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'NamingConventionExample', 'TemplateExample'],
         'in_subset': ['label']} })


class ElementParamSet(ConfiguredBaseModel):
    """
    Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP, MagneticMultipoleP, SolenoidP).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    frequency: Optional[float] = Field(default=None, description="""RF frequency in Hz.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    voltage: Optional[float] = Field(default=None, description="""RF voltage in volts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    phase: Optional[float] = Field(default=None, description="""RF phase in degrees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    angle_ref: Optional[float] = Field(default=None, description="""Reference bend angle in radians.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    e1: Optional[float] = Field(default=None, description="""Entry edge angle in radians.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    e2: Optional[float] = Field(default=None, description="""Exit edge angle in radians.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    Kn1: Optional[float] = Field(default=None, description="""First-order magnetic multipole coefficient (quadrupole strength).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    Ksol: Optional[float] = Field(default=None, description="""Solenoid integrated field strength.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet'], 'in_subset': ['label']} })
    facility_param_set: Optional[FacilityParamSet] = Field(default=None, description="""Facility-specific element parameters (type designation, model name, open property map).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementParamSet']} })


class FacilityParamSet(ConfiguredBaseModel):
    """
    Facility-specific element parameters block for beamline elements. Differs from an ElementParamSet in that it captures facility-specific metadata about the element (e.g. type designation, model name) rather than physics parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/system'})

    facility_element_type: Optional[str] = Field(default=None, description="""capture the facility-specific or local designation (e.g., \"QW\", \"WarmCavity\", \"HCorrector\").  Isused for local naming, inventory, or legacy mapping of instances of facility elements (within elements:)  to the facility-specific type designations used in the control system or elsewhere at the facility.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'], 'domain_of': ['FacilityParamSet'], 'in_subset': ['label']} })
    modeled_as: Optional[str] = Field(default=None, description="""Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FacilityParamSet'], 'in_subset': ['label']} })
    properties: Optional[Any] = Field(default=None, description="""Intentionally open-ended key-value property map for element-specific or facility-specific parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FacilityParamSet']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
NaradModel.model_rebuild()
NaradConfig.model_rebuild()
CapabilityLayer.model_rebuild()
Capability.model_rebuild()
SignalLayer.model_rebuild()
FacilityIdentifier.model_rebuild()
SignalBinding.model_rebuild()
Beamline.model_rebuild()
BeamlineElement.model_rebuild()
System.model_rebuild()
FacilitySystem.model_rebuild()
DeployedSystem.model_rebuild()
ControlSystem.model_rebuild()
Device.model_rebuild()
NamingConventionExample.model_rebuild()
Instrument.model_rebuild()
SystemCapability.model_rebuild()
NamingConvention.model_rebuild()
TemplateComponent.model_rebuild()
TemplateExample.model_rebuild()
Signal.model_rebuild()
ObservableSignal.model_rebuild()
ActuatableSignal.model_rebuild()
InstanceSignalBinding.model_rebuild()
ElementParamSet.model_rebuild()
FacilityParamSet.model_rebuild()
