# narad-system-schema

LinkML schema for representing NARAD control-system semantics, facility-level signal templates, and facility-specific instance bindings aligned with SSN, SSN-System, and SOSA ontologies.
Main modeling layers:
  - NaradModel — top-level document containing NaradConfig, beamlines, and elements
    - NaradConfig — top-level NARAD-system container for the capability layer and signal layer
      - ControlCapabilityLayer — reusable control-profile families, shared capabilities
      - InstrumentLayer — facility-specific instrument definitions -> their  capabilities
      - SignalLayer — facility-specific signal suffix templates for system/device types and instance bindings keyed by semantic signal name, linked to the
        device type
  - Beamline / BeamlineElement — ordered machine layout of the beamline/line
  - Element instances — individual beamline elements with applied profiles and instance signal
    bindings, parameters, and optional facility-specific parameters

System hierarchy:
  - System
    - ControlSystem
    - Magnet
      - Quadrupole, Corrector, Dipole, Solenoid
    - Instrument
      - BPM
    - RFCavity
    - Marker
    - Drift

Control Capability hierarchy:
  - SystemCapability
    - MagnetControlCapability
      - QuadrupoleStrengthControlCapability, CorrectorKickControlCapability, DipoleBendControlCapability
    - InstrumentControlCapability
    - BPMControlCapability
    - CavityGradientControlCapability

Signal modeling:
  - Signal — abstract control-system quantity
    - ObservableSignal — readback, constraint, and status quantities
    - ActuatableSignal — writable/control setpoints
  - SignalBinding — signal template or suffix definition in the signal layer
  - InstanceSignalBinding — facility-specific PV binding attached to a beamline element

Serialization conventions:
  - beamlines are keyed by beamline name
  - signals are keyed by semantic signal name
  - instance_signal_bindings are keyed by semantic signal name

Additional Notes on Usage: 1. On Signal, SignalBinding, and InstanceSignalBinding: These classes represent different levels of abstraction in the signal modeling.  Signal defines the abstract control-system quantity (e.g. current_readback), SignalBinding captures the control system suffix convention for that signal (e.g. .R for EPICS readback),  and InstanceSignalBinding represents the concrete binding of that signal to a specific beamline element instance, for example, MQWK202.S or RK11:GSET, depending on the facility naming convention.  The semantic signal name (e.g. current_readback) is the key that links these layers together, while the control-system suffix (e.g. .R)  is captured in the SignalBinding. 2. On the distinction between is_instance_of, facility_element_type, and device_type:
  - BeamlineElement.is_instance_of identifies the element’s semantic class, device_type classifies capability or signal-definition scope, and facility_element_type records facility-local designation.
  - facility_element_type (FacilityParamSet.facility_element_type) is an optional slot for recording the facility-specific type designation for this element, if it differs from the generic element_kind. 
  - device_type (ControlCapability.device_type) is the generic element type used for capability profile matching 
  and signal definition scoping, while facility_element_type captures the facility-specific type designation that may be used in the control system naming convention 
  or for other facility-specific purposes.
  For example, a facility might have its own naming convention for magnet types that doesn't align one-to-one with the ElementKindEnum values.
3. Expected CURIE usage for is_instance_of, is_hosted_by, and is_property_of: 
  - is_instance_of typically points to the semantic class instantiated by the binding or element, using a CURIE such as narad:CavityGradientCapability if that is your intended convention.
  - is_hosted_by typically points to the FacilitySystem this binding belongs to, e.g. narad:UITF.
  - is_property_of typically points to the ControlSystem that implements this binding, e.g. narad:epics.
4. Open and constrained vocabularies:
  - ElementKindEnum provides a controlled vocabulary for key classification slots, but the schema is designed to be extensible 
  with new enum values as needed.
  - SystemTypeEnum is a high-level classification for systems that can be used for querying and filtering, 
  but it is not intended to capture all the nuance of device types or capabilities.
  - DataTypeEnum and SignalRoleEnum provide a controlled vocabulary for signal data types and roles, 
  but the schema allows for additional values to be added as needed.
  - IdentifierTypeEnum provides a controlled vocabulary for types of identifiers used in FacilityIdentifier, 
  but it can be extended to apply to other entities, and with additional identifier types as needed.
  - The properties slot in FacilityParamSet allows for open-ended key-value pairs to capture any additional 
  facility-specific parameters that don't fit into the predefined schema structure.


URI: https://w3id.org/narad_linkml/schema/narad/system

Name: narad-system-schema



## Classes

| Class | Description |
| --- | --- |
| [AnyValue](AnyValue.md) | Unconstrained type — accepts any YAML/JSON value (string, number, object, lis... |
| [CapabilityLayer](CapabilityLayer.md) | Capability-layer container for control profile families |
| [ElementParamSet](ElementParamSet.md) | Named physics-parameter block for a beamline element |
| [FacilityIdentifier](FacilityIdentifier.md) | A globally unique identifier for an entity (e |
| [FacilityParamSet](FacilityParamSet.md) | Facility-specific element parameters block for beamline elements |
| [NamedThing](NamedThing.md) | Abstract base class providing identity and human-readable metadata |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ControlCapability](ControlCapability.md) | A reusable device-type control profile that extends a generic shared capabili... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Signal](Signal.md) | Domain term for a control-system signal |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SignalBinding](SignalBinding.md) | A named control system suffix definition for one semantic signal |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SignalDefinitions](SignalDefinitions.md) | Signal binding set scoped to a device type or device domain |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ControlSystem](ControlSystem.md) | A control system (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FacilitySystem](FacilitySystem.md) | Facility-specific signal binding configuration |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Instrument](Instrument.md) | A generic beam diagnostic instrument |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InstrumentSystem](InstrumentSystem.md) | A system representing a beam diagnostic instrument, magnet, or other non-magn... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SystemCapability](SystemCapability.md) | A capability of a system |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |
| [SignalLayer](SignalLayer.md) | Signal-layer container for facility-specific signal bindings |



## Slots

| Slot | Description |
| --- | --- |
| [angle_ref](angle_ref.md) | Reference bend angle in radians |
| [beamline_kind](beamline_kind.md) | Kind/type label for the beamline entry (e |
| [beamlines](beamlines.md) | A top-level NARAD-system container for the ordered beamline definitions keyed... |
| [capability_class](capability_class.md) | Semantic class label for a type-specific capability (e |
| [class_curie](class_curie.md) | Optional URI or CURIE |
| [control_capabilities](control_capabilities.md) |  |
| [control_capability](control_capability.md) | Cross-reference to the specific control capability applied to this element |
| [control_capability_layer](control_capability_layer.md) | Control Capability definitions for this facility |
| [control_system](control_system.md) | Identifier of the control system (e |
| [control_system_suffix](control_system_suffix.md) | Facility-specific control-system (e |
| [current_max](current_max.md) |  |
| [current_min](current_min.md) |  |
| [current_readback](current_readback.md) |  |
| [current_setpoint](current_setpoint.md) |  |
| [data_type](data_type.md) | The data type of the signal's value |
| [deployed_system](deployed_system.md) | Identifier of the deployed system this configuration describes |
| [description](description.md) | Detailed description of the entity |
| [device_type](device_type.md) | The specific device type this capability profile or system capability targets... |
| [e1](e1.md) | Entry edge angle in radians |
| [e2](e2.md) | Exit edge angle in radians |
| [element_kind](element_kind.md) | The type of this beamline element (e |
| [elements](elements.md) | Beamline element definitions referenced by name from beamline sequences |
| [facilities](facilities.md) | Facility-specific signal binding configurations keyed by facility name |
| [facility_element_type](facility_element_type.md) | Facility-specific element type designation (e |
| [facility_identifier](facility_identifier.md) | Globally unique identifier for the facility, with specified type and value |
| [facility_param_set](facility_param_set.md) | Facility-specific element parameters (type designation, model name, open prop... |
| [field_setpoint](field_setpoint.md) |  |
| [for_property](for_property.md) | SystemCapability → Signal: the capability can expose, monitor, control, or ac... |
| [frequency](frequency.md) | RF frequency in Hz |
| [gradient_readback](gradient_readback.md) |  |
| [gradient_setpoint](gradient_setpoint.md) |  |
| [has_sub_system](has_sub_system.md) | Relates a System to one of its subsystems (SSN alignment) |
| [has_system_capability](has_system_capability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) |
| [horizontal_beam_position](horizontal_beam_position.md) |  |
| [identifier_type](identifier_type.md) | The type of identifier used in the identifier slot (e |
| [identifier_value](identifier_value.md) | The value of the identifier (e |
| [instance_signal_bindings](instance_signal_bindings.md) | Facility-specific bindings of signals to control-system interfaces (e |
| [instrument_layer](instrument_layer.md) | Instrument definitions for this facility |
| [intent](intent.md) | A human-readable statement of the intended use or purpose of this NARAD confi... |
| [is_hosted_by](is_hosted_by.md) | Links an InstanceSignalBinding to the FacilitySystem it belongs to |
| [is_instance_of](is_instance_of.md) | NARAD alias for rdf:type |
| [is_property_of](is_property_of.md) | Inverse of for_property: links the Class Signal to the Class of SignalBinding... |
| [kick_setpoint](kick_setpoint.md) |  |
| [Kn1](Kn1.md) | First-order magnetic multipole coefficient (quadrupole strength) |
| [Ksol](Ksol.md) | Solenoid integrated field strength |
| [length](length.md) | Physical length of the element in metres |
| [line](line.md) | Ordered sequence of beamline elements in this beamline |
| [modeled_as](modeled_as.md) | Accelerator physics code model element type (e |
| [name](name.md) | Human-readable name or local string key for the entity |
| [naming_convention](naming_convention.md) | Signal naming convention template (e |
| [narad_config](narad_config.md) | Top-level NARAD configuration block (capability_layer + signal_layer) |
| [param_set](param_set.md) | Named physics-parameter blocks for this element (e |
| [phase](phase.md) | RF phase in degrees |
| [properties](properties.md) | Intentionally open-ended key-value property map for element-specific or facil... |
| [pv_name](pv_name.md) | Fully-resolved facility-specific process variable name, e |
| [role](role.md) | The semantic role of the signal within its capability |
| [schema_version](schema_version.md) | Version of the NARAD schema used in this document |
| [signal_bindings](signal_bindings.md) | Control-system-specific, e |
| [signal_definitions](signal_definitions.md) | Structured container for facility-specific signal suffix templates |
| [signal_layer](signal_layer.md) | Signal suffix templates for this facility |
| [signals](signals.md) | Signals within a capability, keyed by a semantic signal name |
| [status](status.md) |  |
| [strength_setpoint](strength_setpoint.md) |  |
| [subclass_of](subclass_of.md) | -> NARAD alias for rdfs:subClassOf |
| [system_type](system_type.md) | High-level system type for classification and querying |
| [units](units.md) | Conventional unit symbol (e |
| [units_uri](units_uri.md) | Machine-resolvable QUDT unit reference (e |
| [vertical_beam_position](vertical_beam_position.md) |  |
| [voltage](voltage.md) | RF voltage in volts |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DataTypeEnum](DataTypeEnum.md) | Allowed data types for signal values |
| [ElementKindEnum](ElementKindEnum.md) | Controlled vocabulary for beamline element types, shared between the capabili... |
| [IdentifierTypeEnum](IdentifierTypeEnum.md) | Allowed identifier types for facilities and other entities |
| [SignalRoleEnum](SignalRoleEnum.md) | Controlled vocabulary for the semantic role of a signal within a capability |
| [SystemTypeEnum](SystemTypeEnum.md) | High-level system type for classification and querying |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
