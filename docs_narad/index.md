# narad-system-schema

LinkML schema for representing facility control-system structures using NARAD domain classes aligned with SSN, SSN-System, and SOSA.
Class hierarchy:
  - System (ssn:System) — base for all physical/logical entities
    - Facility — top-level facility (e.g. UITF); ssn-system:hasSubSystem → ControlSystem
    - ControlSystem — the EPICS or other control system
    - Magnet (ssn:System) — generic powered magnet
      - Quadrupole, Corrector, Dipole, Solenoid
    - Instrument (ssn:System) — generic beam diagnostic
      - BPM
    - RF_System (ssn:System)
      - RFCavity

Capability hierarchy (ssn-system:SystemCapability):
  - SystemCapability — base; linked from System via ssn-system:hasSystemCapability
    - MagnetCapability → QuadrupoleCapability, CorrectorCapability, DipoleCapability
    - InstrumentCapability → BPMCapability
    - CavityGradientCapability

Signal alignment:
  - Signal (broad: sosa:Property / ssn:Property) — abstract base
    - ObservableSignal (exact: sosa:ObservableProperty) — readback, status
    - ActuatableSignal (exact: sosa:ActuatableProperty) — setpoints, limits

SignalBinding alignment:
  - SignalBinding (exact sosa:Procedure) — facility-specific PV binding
    ssn:forProperty → Signal
    narad:isInstanceOf → rdf:type of the capability class


URI: https://w3id.org/narad_linkml/schema/narad/system

Name: narad-system-schema



## Classes

| Class | Description |
| --- | --- |
| [AnyValue](AnyValue.md) | Unconstrained type — accepts any YAML/JSON value (string, number, object, lis... |
| [BPMSignalSet](BPMSignalSet.md) | BPM-specific signal bindings |
| [CapabilityLayer](CapabilityLayer.md) | Capability-layer container for control profile families |
| [CorrectorSignalSet](CorrectorSignalSet.md) | Corrector-specific signal bindings |
| [DipoleSignalSet](DipoleSignalSet.md) | Dipole-specific signal bindings |
| [FacilityIdentifier](FacilityIdentifier.md) | A globally unique identifier for an entity (e |
| [FacilityParamSet](FacilityParamSet.md) | Facility-specific element parameters block for beamline elements |
| [MagnetSignalSet](MagnetSignalSet.md) | Shared magnet signal bindings |
| [NamedThing](NamedThing.md) | Abstract base class providing identity and human-readable metadata |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Beamline](Beamline.md) | An ordered sequence of beamline elements defining a beam path |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile that extends a gen... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds type-specific ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ElementParamSet](ElementParamSet.md) | Named physics-parameter block for a beamline element |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FacilityConfig](FacilityConfig.md) | Facility-specific signal binding configuration |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Signal](Signal.md) | Domain term for a control-system signal |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[System](System.md) | A physical, logical, or cyber-physical system involved in sensing, monitoring... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ControlSystem](ControlSystem.md) | A control system (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Instrument](Instrument.md) | A generic beam diagnostic instrument |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BPM](BPM.md) | A Beam Position Monitor |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Magnet](Magnet.md) | A powered magnet device (generic supertype for all magnet kinds) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Corrector](Corrector.md) | A dipole corrector magnet for orbit correction |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dipole](Dipole.md) | A dipole bending magnet |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Quadrupole](Quadrupole.md) | A quadrupole focusing/defocusing magnet |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Solenoid](Solenoid.md) | A solenoid magnet |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Marker](Marker.md) | A zero-length reference point, drift space, or survey marker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RFCavity](RFCavity.md) | A radio-frequency accelerating or bunching cavity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SystemCapability](SystemCapability.md) | A capability of a system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CavityGradientCapability](CavityGradientCapability.md) | RF cavity capability with gradient control, readback, and status signals |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InstrumentCapability](InstrumentCapability.md) | Generic instrument capability (position readback and status signals) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BPMCapability](BPMCapability.md) | BPM-specific capability with horizontal and vertical position readback signal... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MagnetCapability](MagnetCapability.md) | Generic magnet capability (current control and readback signals) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CorrectorCapability](CorrectorCapability.md) | Corrector-specific capability extending MagnetCapability with kick signals |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DipoleCapability](DipoleCapability.md) | Dipole-specific capability extending MagnetCapability with bend-field signals |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QuadrupoleCapability](QuadrupoleCapability.md) | Quadrupole-specific capability extending MagnetCapability with strength signa... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SolenoidCapability](SolenoidCapability.md) | Solenoid-specific capability extending MagnetCapability with focusing signals |
| [NaradConfig](NaradConfig.md) | NARAD configuration block: capability layer + signal layer |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |
| [QuadrupoleSignalSet](QuadrupoleSignalSet.md) | Quadrupole-specific signal bindings |
| [RFCavitySignalSet](RFCavitySignalSet.md) | RF cavity-specific signal bindings |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |
| [SignalDefinitions](SignalDefinitions.md) | EPICS signal suffix templates keyed by device type or device domain |
| [SignalLayer](SignalLayer.md) | Signal-layer container for facility-specific signal bindings |
| [TypeSignalSet](TypeSignalSet.md) | Explicit signal binding groups keyed by device domain or device type |



## Slots

| Slot | Description |
| --- | --- |
| [angle_ref](angle_ref.md) | Reference bend angle in radians |
| [beamline_kind](beamline_kind.md) | Kind/type label for the beamline entry (e |
| [beamlines](beamlines.md) | Ordered beamline definitions keyed by beamline name |
| [bpm_signals](bpm_signals.md) | BPM-specific signal bindings |
| [capability_class](capability_class.md) | Semantic class label for a type-specific capability (e |
| [capability_layer](capability_layer.md) | Capability-layer container for profile families |
| [capability_profile](capability_profile.md) | Cross-reference to the specific capability profile applied to this element |
| [capability_profile_family](capability_profile_family.md) | Cross-reference to the control profile family for this element |
| [class_curie](class_curie.md) | Optional URI or CURIE for a TypeSpecificCapability class |
| [control_system](control_system.md) | Identifier of the control system (e |
| [control_system_suffix](control_system_suffix.md) | Facility-specific control-system (e |
| [corrector_signals](corrector_signals.md) | Corrector-specific signal bindings |
| [current_max](current_max.md) |  |
| [current_min](current_min.md) |  |
| [current_readback](current_readback.md) |  |
| [current_setpoint](current_setpoint.md) |  |
| [data_type](data_type.md) | The data type of the signal's value |
| [description](description.md) | Detailed description of the entity |
| [device_domain](device_domain.md) | High-level device domain that this profile family governs |
| [device_type](device_type.md) | The specific device type this capability profile or system capability targets... |
| [dipole_signals](dipole_signals.md) | Dipole-specific signal bindings |
| [e1](e1.md) | Entry edge angle in radians |
| [e2](e2.md) | Exit edge angle in radians |
| [element_kind](element_kind.md) | The type of this beamline element (e |
| [elements](elements.md) | Beamline element definitions referenced by name from beamline sequences |
| [facilities](facilities.md) | Facility-specific signal binding configurations keyed by facility name |
| [facility](facility.md) | Identifier of the facility this configuration describes |
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
| [inherits_from](inherits_from.md) | Explicit cross-reference from a TypeSpecificCapability to the generic shared ... |
| [inherits_shared_capabilities](inherits_shared_capabilities.md) | Shared capabilities inherited by this profile, cross-referenced by name |
| [instance_signal_bindings](instance_signal_bindings.md) | Facility-specific bindings of signals to control-system interfaces (e |
| [intent](intent.md) | A human-readable statement of the intended use or purpose of this NARAD confi... |
| [is_abstract](is_abstract.md) | If true, this profile is a template not intended to be directly assigned to a... |
| [is_hosted_by](is_hosted_by.md) | Links an InstanceSignalBinding to the FacilitySystem it belongs to |
| [is_instance_of](is_instance_of.md) | NARAD alias for rdf:type |
| [is_property_of](is_property_of.md) | Inverse of for_property: links the Class Signal to the Class of SignalBinding... |
| [kick_setpoint](kick_setpoint.md) |  |
| [Kn1](Kn1.md) | First-order magnetic multipole coefficient (quadrupole strength) |
| [Ksol](Ksol.md) | Solenoid integrated field strength |
| [length](length.md) | Physical length of the element in metres |
| [line](line.md) | Ordered sequence of cross-referenced element names forming a beamline |
| [magnet_signals](magnet_signals.md) | Shared magnet signal bindings |
| [modeled_as](modeled_as.md) | Accelerator physics code model element type (e |
| [name](name.md) | Human-readable name or local string key for the entity |
| [naming_convention](naming_convention.md) | Signal naming convention template (e |
| [narad_config](narad_config.md) | Top-level NARAD configuration block (capability_layer + signal_layer) |
| [param_set](param_set.md) | Named physics-parameter blocks for this element (e |
| [phase](phase.md) | RF phase in degrees |
| [profiles](profiles.md) | Control profile families keyed by family name |
| [properties](properties.md) | Open-ended key-value property map for element-specific or facility-specific p... |
| [pv_name](pv_name.md) | Fully-resolved facility-specific process variable name, e |
| [quadrupole_signals](quadrupole_signals.md) | Quadrupole-specific signal bindings |
| [rfcavity_signals](rfcavity_signals.md) | RF cavity-specific signal bindings |
| [role](role.md) | The semantic role of the signal within its capability |
| [schema_version](schema_version.md) | Version of the NARAD schema used in this document |
| [shared_capabilities](shared_capabilities.md) | Named shared capabilities reused by profile types in a family |
| [signal_bindings](signal_bindings.md) | Control-system-specific, e |
| [signal_definitions](signal_definitions.md) | Signal suffix templates for this facility |
| [signal_layer](signal_layer.md) | Signal-layer container for facility-specific signal bindings |
| [signals](signals.md) | Signals within a capability, keyed by signal name |
| [status](status.md) |  |
| [strength_setpoint](strength_setpoint.md) |  |
| [type_profiles](type_profiles.md) | Device-type profile definitions for this family, keyed by profile name |
| [type_signal_sets](type_signal_sets.md) | Signal suffix groups keyed by device type or device domain name |
| [type_specific_capabilities](type_specific_capabilities.md) | Type-specific capabilities declared directly in a profile |
| [units](units.md) | Conventional unit symbol (e |
| [units_uri](units_uri.md) | Machine-resolvable QUDT unit reference (e |
| [vertical_beam_position](vertical_beam_position.md) |  |
| [voltage](voltage.md) | RF voltage in volts |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DataTypeEnum](DataTypeEnum.md) | Allowed data types for signal values |
| [DeviceDomainEnum](DeviceDomainEnum.md) | High-level device domain for a control profile family |
| [ElementKindEnum](ElementKindEnum.md) | Controlled vocabulary for beamline element types, shared between the capabili... |
| [IdentifierTypeEnum](IdentifierTypeEnum.md) | Allowed identifier types for facilities and other entities |
| [SignalRoleEnum](SignalRoleEnum.md) | Controlled vocabulary for the semantic role of a signal within a capability |


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
