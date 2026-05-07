-- # Abstract Class: NamedThing Description: Abstract base class providing identity and human-readable metadata.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: NaradModel Description: Top-level NARAD document container.
--     * Slot: id
--     * Slot: narad_config_id Description: Top-level NARAD configuration block (capability_layer + signal_layer).
-- # Class: NaradConfig Description: NARAD configuration block: capability layer + signal layer.
--     * Slot: id
--     * Slot: schema_version Description: Version of the NARAD schema used in this document.
--     * Slot: intent Description: A human-readable statement of the intended use or purpose of this NARAD configuration.
--     * Slot: facility Description: Identifier of the facility this configuration describes.
--     * Slot: control_system Description: Identifier of the control system (e.g. epics) this configuration describes.
--     * Slot: capability_layer_id Description: Capability-layer container for control profile families.
--     * Slot: signal_layer_id Description: Signal-layer container for facility-specific signal bindings.
-- # Class: CapabilityLayer Description: Capability-layer container for control profile families.
--     * Slot: id
-- # Class: ControlProfileFamily Description: A reusable family of control profiles sharing common semantics and structure (e.g. MagnetCurrentControlProfileFamily).
--     * Slot: device_domain Description: High-level device domain that this profile family governs.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: CapabilityLayer_id Description: Autocreated FK slot
-- # Class: Capability Description: A named, shared grouping of semantically related signals for a control aspect (e.g. MagnetCurrentControlCapability).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: ControlProfileFamily_name Description: Autocreated FK slot
-- # Class: TypeSpecificCapability Description: An inline capability declared within a device-type profile that extends a generic shared Capability. The explicit link to the shared Capability being extended is given by inherits_from. Adds type-specific signals on top of those already defined in the referenced shared Capability.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: CapabilityProfile_name Description: Autocreated FK slot
-- # Class: CapabilityProfile Description: A device-type profile that reuses shared capabilities and adds type-specific ones (e.g. QuadrupoleProfile).
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: ControlProfileFamily_name Description: Autocreated FK slot
-- # Class: SignalLayer Description: Signal-layer container for facility-specific signal bindings.
--     * Slot: id
-- # Class: FacilityConfig Description: Facility-specific signal binding configuration.
--     * Slot: control_system Description: Identifier of the control system (e.g. epics).
--     * Slot: naming_convention Description: Signal naming convention template (e.g. <device><signal_code>).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: SignalLayer_id Description: Autocreated FK slot
--     * Slot: signal_definitions_id Description: Signal suffix templates for this facility.
-- # Class: FacilityIdentifier Description: A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
--     * Slot: id
--     * Slot: identifier_type Description: The type of identifier used in the identifier slot (e.g. DOI, ARK, URL, local).
--     * Slot: identifier_value Description: The value of the identifier (e.g. the DOI string, ARK string, URL string, or local ID).
-- # Class: SignalDefinitions Description: EPICS signal suffix templates keyed by device type or device domain. Domain-level keys (e.g. Magnet, RFCavity) cover signals shared across all types in that domain; device-type keys are type-specific.
--     * Slot: id
--     * Slot: type_signal_sets_id Description: Signal suffix groups keyed by device type or device domain name. Domain-level keys cover signals shared across all types in that domain; device-type keys are type-specific.
-- # Class: SignalBinding Description: A named EPICS suffix definition for one semantic signal.
--     * Slot: id
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: control_system_suffix Description: Facility-specific control-system (e.g. EPICS) naming suffix used to derive or interpret the signal binding, e.g. .S, M, :GSET.
-- # Class: TypeSignalSet Description: Explicit signal binding groups keyed by device domain or device type.
--     * Slot: id
--     * Slot: magnet_signals_id Description: Shared magnet signal bindings.
--     * Slot: quadrupole_signals_id Description: Quadrupole-specific signal bindings.
--     * Slot: corrector_signals_id Description: Corrector-specific signal bindings.
--     * Slot: dipole_signals_id Description: Dipole-specific signal bindings.
--     * Slot: bpm_signals_id Description: BPM-specific signal bindings.
--     * Slot: rfcavity_signals_id Description: RF cavity-specific signal bindings.
-- # Class: MagnetSignalSet Description: Shared magnet signal bindings.
--     * Slot: id
--     * Slot: current_setpoint_id
--     * Slot: current_readback_id
--     * Slot: current_min_id
--     * Slot: current_max_id
--     * Slot: status_id
-- # Class: QuadrupoleSignalSet Description: Quadrupole-specific signal bindings.
--     * Slot: id
--     * Slot: strength_setpoint_id
-- # Class: CorrectorSignalSet Description: Corrector-specific signal bindings.
--     * Slot: id
--     * Slot: kick_setpoint_id
-- # Class: DipoleSignalSet Description: Dipole-specific signal bindings.
--     * Slot: id
--     * Slot: field_setpoint_id
-- # Class: BPMSignalSet Description: BPM-specific signal bindings.
--     * Slot: id
--     * Slot: horizontal_beam_position_id
--     * Slot: vertical_beam_position_id
--     * Slot: status_id
-- # Class: RFCavitySignalSet Description: RF cavity-specific signal bindings.
--     * Slot: id
--     * Slot: gradient_setpoint_id
--     * Slot: gradient_readback_id
--     * Slot: status_id
-- # Class: Beamline Description: An ordered sequence of beamline elements defining a beam path.
--     * Slot: beamline_kind Description: Kind/type label for the beamline entry (e.g. BeamLine).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: NaradModel_id Description: Autocreated FK slot
-- # Class: BeamlineElement Description: A single element in a beamline with its kind and optional NARAD capability annotations.
--     * Slot: element_kind Description: The type of this beamline element (e.g. Quadrupole, BPM, RFCavity).
--     * Slot: length Description: Physical length of the element in metres.
--     * Slot: capability_profile_family Description: Cross-reference to the control profile family for this element.
--     * Slot: capability_profile Description: Cross-reference to the specific capability profile applied to this element.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: NaradModel_id Description: Autocreated FK slot
--     * Slot: facility_param_set_id Description: Facility-specific element parameters (type designation, model name, open property map).
-- # Class: System Description: A physical, logical, or cyber-physical system involved in sensing, monitoring, control, or actuation. Broadly aligned to ssn:System.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: ControlSystem Description: A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a subsystem of the Facility.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Magnet Description: A powered magnet device (generic supertype for all magnet kinds).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Quadrupole Description: A quadrupole focusing/defocusing magnet.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Corrector Description: A dipole corrector magnet for orbit correction.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Dipole Description: A dipole bending magnet.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Solenoid Description: A solenoid magnet.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Instrument Description: A generic beam diagnostic instrument.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: BPM Description: A Beam Position Monitor.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: RFCavity Description: A radio-frequency accelerating or bunching cavity.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Marker Description: A zero-length reference point, drift space, or survey marker.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: SystemCapability Description: A capability of a system. SystemCapability describes what a system can expose, monitor, control, or actuate with respect to one or more signals. Aligned to ssn-system:SystemCapability; linked from System instances via ssn-system:hasSystemCapability, and from Signals via ssn:forProperty. Profile-level inheritance (shared vs. type-specific signals) is expressed in CapabilityProfile, not here.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: MagnetCapability Description: Generic magnet capability (current control and readback signals).
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: QuadrupoleCapability Description: Quadrupole-specific capability extending MagnetCapability with strength signals.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: CorrectorCapability Description: Corrector-specific capability extending MagnetCapability with kick signals.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: DipoleCapability Description: Dipole-specific capability extending MagnetCapability with bend-field signals.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: SolenoidCapability Description: Solenoid-specific capability extending MagnetCapability with focusing signals.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: InstrumentCapability Description: Generic instrument capability (position readback and status signals).
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: BPMCapability Description: BPM-specific capability with horizontal and vertical position readback signals.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: CavityGradientCapability Description: RF cavity capability with gradient control, readback, and status signals.
--     * Slot: device_type Description: The specific device type this capability profile or system capability targets (e.g. Quadrupole, Corrector, BPM).
--     * Slot: is_abstract Description: If true, this profile is a template not intended to be directly assigned to a beamline element. Concrete profiles set this to false (default).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: Signal Description: Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The concrete facility binding is captured in SignalBinding.
--     * Slot: role Description: The semantic role of the signal within its capability.
--     * Slot: data_type Description: The data type of the signal's value.
--     * Slot: units Description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
--     * Slot: units_uri Description: Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: Capability_name Description: Autocreated FK slot
--     * Slot: TypeSpecificCapability_name Description: Autocreated FK slot
-- # Class: ObservableSignal Description: A NARAD signal that is read, monitored, observed, or exposed by a system. Examples: current_readback, status, horizontal_beam_position, gradient_readback. Aligned to sosa:ObservableProperty.
--     * Slot: role Description: The semantic role of the signal within its capability.
--     * Slot: data_type Description: The data type of the signal's value.
--     * Slot: units Description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
--     * Slot: units_uri Description: Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: ActuatableSignal Description: A NARAD signal that can be commanded, set, or acted upon. Examples: current_setpoint, strength_setpoint, kick_setpoint, field_setpoint, current_min, current_max, gradient_setpoint. Aligned to sosa:ActuatableProperty.
--     * Slot: role Description: The semantic role of the signal within its capability.
--     * Slot: data_type Description: The data type of the signal's value.
--     * Slot: units Description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
--     * Slot: units_uri Description: Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: InstanceSignalBinding Description: A facility-specific binding between a NARAD Signal and an implementation interface (e.g. an EPICS process variable). Modeled as sosa:Sensor because it describes how a signal is observed, monitored, or actuated. ssn:forProperty → Signal; narad:isInstanceOf → the capability class.
--     * Slot: is_property_of Description: Inverse of for_property: links the Class Signal to the Class of SignalBinding Procedure that implements it. This can also link the Instance of a SignalBinding to the ControlSystem that implements it. This is the edge that connects the signal definitions to the facility-specific bindings in the graph.
--     * Slot: pv_name Description: Fully-resolved facility-specific process variable name, e.g. MQWK202:STAT or MQWK202:BDL.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: BeamlineElement_name Description: Autocreated FK slot
-- # Class: ElementParamSet Description: Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP, MagneticMultipoleP, SolenoidP).
--     * Slot: frequency Description: RF frequency in Hz.
--     * Slot: voltage Description: RF voltage in volts.
--     * Slot: phase Description: RF phase in degrees.
--     * Slot: angle_ref Description: Reference bend angle in radians.
--     * Slot: e1 Description: Entry edge angle in radians.
--     * Slot: e2 Description: Exit edge angle in radians.
--     * Slot: Kn1 Description: First-order magnetic multipole coefficient (quadrupole strength).
--     * Slot: Ksol Description: Solenoid integrated field strength.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: BeamlineElement_name Description: Autocreated FK slot
-- # Class: FacilityParamSet Description: Facility-specific element parameters block for beamline elements.
--     * Slot: id
--     * Slot: facility_element_type Description: Facility-specific element type designation (e.g. WarmCavity, QW, HCorrector). named facility_element_type here to avoid conflict with the LinkML metamodel 'type'  designator used for polymorphic class selection.
--     * Slot: modeled_as Description: Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).
--     * Slot: properties_id Description: Open-ended key-value property map for element-specific or facility-specific parameters.
-- # Class: AnyValue Description: Unconstrained type — accepts any YAML/JSON value (string, number, object, list, etc.).
--     * Slot: id
-- # Class: CapabilityProfile_inherits_shared_capabilities
--     * Slot: CapabilityProfile_name Description: Autocreated FK slot
--     * Slot: inherits_shared_capabilities_name Description: Shared capabilities inherited by this profile, cross-referenced by name.
-- # Class: FacilityConfig_facility_identifier
--     * Slot: FacilityConfig_name Description: Autocreated FK slot
--     * Slot: facility_identifier_id Description: Globally unique identifier for the facility, with specified type and value.
-- # Class: Beamline_line
--     * Slot: Beamline_name Description: Autocreated FK slot
--     * Slot: line_name Description: Ordered sequence of cross-referenced element names forming a beamline.
-- # Class: System_has_sub_system
--     * Slot: System_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: System_has_system_capability
--     * Slot: System_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: ControlSystem_has_sub_system
--     * Slot: ControlSystem_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: ControlSystem_has_system_capability
--     * Slot: ControlSystem_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Magnet_has_sub_system
--     * Slot: Magnet_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Magnet_has_system_capability
--     * Slot: Magnet_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Quadrupole_has_sub_system
--     * Slot: Quadrupole_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Quadrupole_has_system_capability
--     * Slot: Quadrupole_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Corrector_has_sub_system
--     * Slot: Corrector_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Corrector_has_system_capability
--     * Slot: Corrector_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Dipole_has_sub_system
--     * Slot: Dipole_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Dipole_has_system_capability
--     * Slot: Dipole_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Solenoid_has_sub_system
--     * Slot: Solenoid_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Solenoid_has_system_capability
--     * Slot: Solenoid_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Instrument_has_sub_system
--     * Slot: Instrument_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Instrument_has_system_capability
--     * Slot: Instrument_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: BPM_has_sub_system
--     * Slot: BPM_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: BPM_has_system_capability
--     * Slot: BPM_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: RFCavity_has_sub_system
--     * Slot: RFCavity_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: RFCavity_has_system_capability
--     * Slot: RFCavity_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: Marker_has_sub_system
--     * Slot: Marker_name Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
-- # Class: Marker_has_system_capability
--     * Slot: Marker_name Description: Autocreated FK slot
--     * Slot: has_system_capability_name Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
-- # Class: SystemCapability_for_property
--     * Slot: SystemCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: MagnetCapability_for_property
--     * Slot: MagnetCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: QuadrupoleCapability_for_property
--     * Slot: QuadrupoleCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: CorrectorCapability_for_property
--     * Slot: CorrectorCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: DipoleCapability_for_property
--     * Slot: DipoleCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: SolenoidCapability_for_property
--     * Slot: SolenoidCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: InstrumentCapability_for_property
--     * Slot: InstrumentCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: BPMCapability_for_property
--     * Slot: BPMCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: CavityGradientCapability_for_property
--     * Slot: CavityGradientCapability_name Description: Autocreated FK slot
--     * Slot: for_property_name Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
-- # Class: InstanceSignalBinding_is_instance_of
--     * Slot: InstanceSignalBinding_name Description: Autocreated FK slot
--     * Slot: is_instance_of Description: NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf.
-- # Class: InstanceSignalBinding_is_hosted_by
--     * Slot: InstanceSignalBinding_name Description: Autocreated FK slot
--     * Slot: is_hosted_by Description: Links an InstanceSignalBinding to the FacilitySystem it belongs to. This is the edge that connects the facility-specific bindings to the Facility node in the graph.

CREATE TABLE "NamedThing" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_NamedThing_name" ON "NamedThing" (name);
CREATE TABLE "CapabilityLayer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CapabilityLayer_id" ON "CapabilityLayer" (id);
CREATE TABLE "SignalLayer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SignalLayer_id" ON "SignalLayer" (id);
CREATE TABLE "FacilityIdentifier" (
	id INTEGER NOT NULL,
	identifier_type VARCHAR(6),
	identifier_value TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FacilityIdentifier_id" ON "FacilityIdentifier" (id);
CREATE TABLE "SignalBinding" (
	id INTEGER NOT NULL,
	description TEXT,
	control_system_suffix TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SignalBinding_id" ON "SignalBinding" (id);
CREATE TABLE "System" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_System_name" ON "System" (name);
CREATE TABLE "ControlSystem" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_ControlSystem_name" ON "ControlSystem" (name);
CREATE TABLE "Magnet" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Magnet_name" ON "Magnet" (name);
CREATE TABLE "Quadrupole" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Quadrupole_name" ON "Quadrupole" (name);
CREATE TABLE "Corrector" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Corrector_name" ON "Corrector" (name);
CREATE TABLE "Dipole" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Dipole_name" ON "Dipole" (name);
CREATE TABLE "Solenoid" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Solenoid_name" ON "Solenoid" (name);
CREATE TABLE "Instrument" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Instrument_name" ON "Instrument" (name);
CREATE TABLE "BPM" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_BPM_name" ON "BPM" (name);
CREATE TABLE "RFCavity" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_RFCavity_name" ON "RFCavity" (name);
CREATE TABLE "Marker" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Marker_name" ON "Marker" (name);
CREATE TABLE "SystemCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_SystemCapability_name" ON "SystemCapability" (name);
CREATE TABLE "MagnetCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_MagnetCapability_name" ON "MagnetCapability" (name);
CREATE TABLE "QuadrupoleCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_QuadrupoleCapability_name" ON "QuadrupoleCapability" (name);
CREATE TABLE "CorrectorCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_CorrectorCapability_name" ON "CorrectorCapability" (name);
CREATE TABLE "DipoleCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_DipoleCapability_name" ON "DipoleCapability" (name);
CREATE TABLE "SolenoidCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_SolenoidCapability_name" ON "SolenoidCapability" (name);
CREATE TABLE "InstrumentCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_InstrumentCapability_name" ON "InstrumentCapability" (name);
CREATE TABLE "BPMCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_BPMCapability_name" ON "BPMCapability" (name);
CREATE TABLE "CavityGradientCapability" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_CavityGradientCapability_name" ON "CavityGradientCapability" (name);
CREATE TABLE "ObservableSignal" (
	role VARCHAR(10),
	data_type VARCHAR(11),
	units TEXT,
	units_uri TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_ObservableSignal_name" ON "ObservableSignal" (name);
CREATE TABLE "ActuatableSignal" (
	role VARCHAR(10),
	data_type VARCHAR(11),
	units TEXT,
	units_uri TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_ActuatableSignal_name" ON "ActuatableSignal" (name);
CREATE TABLE "AnyValue" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_AnyValue_id" ON "AnyValue" (id);
CREATE TABLE "NaradConfig" (
	id INTEGER NOT NULL,
	schema_version TEXT NOT NULL,
	intent TEXT,
	facility TEXT NOT NULL,
	control_system TEXT NOT NULL,
	capability_layer_id INTEGER NOT NULL,
	signal_layer_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(capability_layer_id) REFERENCES "CapabilityLayer" (id),
	FOREIGN KEY(signal_layer_id) REFERENCES "SignalLayer" (id)
);CREATE INDEX "ix_NaradConfig_id" ON "NaradConfig" (id);
CREATE TABLE "ControlProfileFamily" (
	device_domain VARCHAR(10),
	name TEXT NOT NULL,
	description TEXT,
	"CapabilityLayer_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("CapabilityLayer_id") REFERENCES "CapabilityLayer" (id)
);CREATE INDEX "ix_ControlProfileFamily_name" ON "ControlProfileFamily" (name);
CREATE TABLE "MagnetSignalSet" (
	id INTEGER NOT NULL,
	current_setpoint_id INTEGER,
	current_readback_id INTEGER,
	current_min_id INTEGER,
	current_max_id INTEGER,
	status_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(current_setpoint_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(current_readback_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(current_min_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(current_max_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(status_id) REFERENCES "SignalBinding" (id)
);CREATE INDEX "ix_MagnetSignalSet_id" ON "MagnetSignalSet" (id);
CREATE TABLE "QuadrupoleSignalSet" (
	id INTEGER NOT NULL,
	strength_setpoint_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(strength_setpoint_id) REFERENCES "SignalBinding" (id)
);CREATE INDEX "ix_QuadrupoleSignalSet_id" ON "QuadrupoleSignalSet" (id);
CREATE TABLE "CorrectorSignalSet" (
	id INTEGER NOT NULL,
	kick_setpoint_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(kick_setpoint_id) REFERENCES "SignalBinding" (id)
);CREATE INDEX "ix_CorrectorSignalSet_id" ON "CorrectorSignalSet" (id);
CREATE TABLE "DipoleSignalSet" (
	id INTEGER NOT NULL,
	field_setpoint_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(field_setpoint_id) REFERENCES "SignalBinding" (id)
);CREATE INDEX "ix_DipoleSignalSet_id" ON "DipoleSignalSet" (id);
CREATE TABLE "BPMSignalSet" (
	id INTEGER NOT NULL,
	horizontal_beam_position_id INTEGER,
	vertical_beam_position_id INTEGER,
	status_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(horizontal_beam_position_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(vertical_beam_position_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(status_id) REFERENCES "SignalBinding" (id)
);CREATE INDEX "ix_BPMSignalSet_id" ON "BPMSignalSet" (id);
CREATE TABLE "RFCavitySignalSet" (
	id INTEGER NOT NULL,
	gradient_setpoint_id INTEGER,
	gradient_readback_id INTEGER,
	status_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(gradient_setpoint_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(gradient_readback_id) REFERENCES "SignalBinding" (id),
	FOREIGN KEY(status_id) REFERENCES "SignalBinding" (id)
);CREATE INDEX "ix_RFCavitySignalSet_id" ON "RFCavitySignalSet" (id);
CREATE TABLE "FacilityParamSet" (
	id INTEGER NOT NULL,
	facility_element_type TEXT,
	modeled_as TEXT,
	properties_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(properties_id) REFERENCES "AnyValue" (id)
);CREATE INDEX "ix_FacilityParamSet_id" ON "FacilityParamSet" (id);
CREATE TABLE "System_has_sub_system" (
	"System_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("System_name", has_sub_system_name),
	FOREIGN KEY("System_name") REFERENCES "System" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_System_has_sub_system_has_sub_system_name" ON "System_has_sub_system" (has_sub_system_name);CREATE INDEX "ix_System_has_sub_system_System_name" ON "System_has_sub_system" ("System_name");
CREATE TABLE "System_has_system_capability" (
	"System_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("System_name", has_system_capability_name),
	FOREIGN KEY("System_name") REFERENCES "System" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_System_has_system_capability_System_name" ON "System_has_system_capability" ("System_name");CREATE INDEX "ix_System_has_system_capability_has_system_capability_name" ON "System_has_system_capability" (has_system_capability_name);
CREATE TABLE "ControlSystem_has_sub_system" (
	"ControlSystem_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("ControlSystem_name", has_sub_system_name),
	FOREIGN KEY("ControlSystem_name") REFERENCES "ControlSystem" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_ControlSystem_has_sub_system_ControlSystem_name" ON "ControlSystem_has_sub_system" ("ControlSystem_name");CREATE INDEX "ix_ControlSystem_has_sub_system_has_sub_system_name" ON "ControlSystem_has_sub_system" (has_sub_system_name);
CREATE TABLE "ControlSystem_has_system_capability" (
	"ControlSystem_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("ControlSystem_name", has_system_capability_name),
	FOREIGN KEY("ControlSystem_name") REFERENCES "ControlSystem" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_ControlSystem_has_system_capability_has_system_capability_name" ON "ControlSystem_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_ControlSystem_has_system_capability_ControlSystem_name" ON "ControlSystem_has_system_capability" ("ControlSystem_name");
CREATE TABLE "Magnet_has_sub_system" (
	"Magnet_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Magnet_name", has_sub_system_name),
	FOREIGN KEY("Magnet_name") REFERENCES "Magnet" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Magnet_has_sub_system_Magnet_name" ON "Magnet_has_sub_system" ("Magnet_name");CREATE INDEX "ix_Magnet_has_sub_system_has_sub_system_name" ON "Magnet_has_sub_system" (has_sub_system_name);
CREATE TABLE "Magnet_has_system_capability" (
	"Magnet_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Magnet_name", has_system_capability_name),
	FOREIGN KEY("Magnet_name") REFERENCES "Magnet" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Magnet_has_system_capability_Magnet_name" ON "Magnet_has_system_capability" ("Magnet_name");CREATE INDEX "ix_Magnet_has_system_capability_has_system_capability_name" ON "Magnet_has_system_capability" (has_system_capability_name);
CREATE TABLE "Quadrupole_has_sub_system" (
	"Quadrupole_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Quadrupole_name", has_sub_system_name),
	FOREIGN KEY("Quadrupole_name") REFERENCES "Quadrupole" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Quadrupole_has_sub_system_Quadrupole_name" ON "Quadrupole_has_sub_system" ("Quadrupole_name");CREATE INDEX "ix_Quadrupole_has_sub_system_has_sub_system_name" ON "Quadrupole_has_sub_system" (has_sub_system_name);
CREATE TABLE "Quadrupole_has_system_capability" (
	"Quadrupole_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Quadrupole_name", has_system_capability_name),
	FOREIGN KEY("Quadrupole_name") REFERENCES "Quadrupole" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Quadrupole_has_system_capability_has_system_capability_name" ON "Quadrupole_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_Quadrupole_has_system_capability_Quadrupole_name" ON "Quadrupole_has_system_capability" ("Quadrupole_name");
CREATE TABLE "Corrector_has_sub_system" (
	"Corrector_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Corrector_name", has_sub_system_name),
	FOREIGN KEY("Corrector_name") REFERENCES "Corrector" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Corrector_has_sub_system_has_sub_system_name" ON "Corrector_has_sub_system" (has_sub_system_name);CREATE INDEX "ix_Corrector_has_sub_system_Corrector_name" ON "Corrector_has_sub_system" ("Corrector_name");
CREATE TABLE "Corrector_has_system_capability" (
	"Corrector_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Corrector_name", has_system_capability_name),
	FOREIGN KEY("Corrector_name") REFERENCES "Corrector" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Corrector_has_system_capability_has_system_capability_name" ON "Corrector_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_Corrector_has_system_capability_Corrector_name" ON "Corrector_has_system_capability" ("Corrector_name");
CREATE TABLE "Dipole_has_sub_system" (
	"Dipole_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Dipole_name", has_sub_system_name),
	FOREIGN KEY("Dipole_name") REFERENCES "Dipole" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Dipole_has_sub_system_Dipole_name" ON "Dipole_has_sub_system" ("Dipole_name");CREATE INDEX "ix_Dipole_has_sub_system_has_sub_system_name" ON "Dipole_has_sub_system" (has_sub_system_name);
CREATE TABLE "Dipole_has_system_capability" (
	"Dipole_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Dipole_name", has_system_capability_name),
	FOREIGN KEY("Dipole_name") REFERENCES "Dipole" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Dipole_has_system_capability_has_system_capability_name" ON "Dipole_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_Dipole_has_system_capability_Dipole_name" ON "Dipole_has_system_capability" ("Dipole_name");
CREATE TABLE "Solenoid_has_sub_system" (
	"Solenoid_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Solenoid_name", has_sub_system_name),
	FOREIGN KEY("Solenoid_name") REFERENCES "Solenoid" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Solenoid_has_sub_system_Solenoid_name" ON "Solenoid_has_sub_system" ("Solenoid_name");CREATE INDEX "ix_Solenoid_has_sub_system_has_sub_system_name" ON "Solenoid_has_sub_system" (has_sub_system_name);
CREATE TABLE "Solenoid_has_system_capability" (
	"Solenoid_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Solenoid_name", has_system_capability_name),
	FOREIGN KEY("Solenoid_name") REFERENCES "Solenoid" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Solenoid_has_system_capability_has_system_capability_name" ON "Solenoid_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_Solenoid_has_system_capability_Solenoid_name" ON "Solenoid_has_system_capability" ("Solenoid_name");
CREATE TABLE "Instrument_has_sub_system" (
	"Instrument_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Instrument_name", has_sub_system_name),
	FOREIGN KEY("Instrument_name") REFERENCES "Instrument" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Instrument_has_sub_system_Instrument_name" ON "Instrument_has_sub_system" ("Instrument_name");CREATE INDEX "ix_Instrument_has_sub_system_has_sub_system_name" ON "Instrument_has_sub_system" (has_sub_system_name);
CREATE TABLE "Instrument_has_system_capability" (
	"Instrument_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Instrument_name", has_system_capability_name),
	FOREIGN KEY("Instrument_name") REFERENCES "Instrument" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Instrument_has_system_capability_has_system_capability_name" ON "Instrument_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_Instrument_has_system_capability_Instrument_name" ON "Instrument_has_system_capability" ("Instrument_name");
CREATE TABLE "BPM_has_sub_system" (
	"BPM_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("BPM_name", has_sub_system_name),
	FOREIGN KEY("BPM_name") REFERENCES "BPM" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_BPM_has_sub_system_has_sub_system_name" ON "BPM_has_sub_system" (has_sub_system_name);CREATE INDEX "ix_BPM_has_sub_system_BPM_name" ON "BPM_has_sub_system" ("BPM_name");
CREATE TABLE "BPM_has_system_capability" (
	"BPM_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("BPM_name", has_system_capability_name),
	FOREIGN KEY("BPM_name") REFERENCES "BPM" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_BPM_has_system_capability_BPM_name" ON "BPM_has_system_capability" ("BPM_name");CREATE INDEX "ix_BPM_has_system_capability_has_system_capability_name" ON "BPM_has_system_capability" (has_system_capability_name);
CREATE TABLE "RFCavity_has_sub_system" (
	"RFCavity_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("RFCavity_name", has_sub_system_name),
	FOREIGN KEY("RFCavity_name") REFERENCES "RFCavity" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_RFCavity_has_sub_system_has_sub_system_name" ON "RFCavity_has_sub_system" (has_sub_system_name);CREATE INDEX "ix_RFCavity_has_sub_system_RFCavity_name" ON "RFCavity_has_sub_system" ("RFCavity_name");
CREATE TABLE "RFCavity_has_system_capability" (
	"RFCavity_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("RFCavity_name", has_system_capability_name),
	FOREIGN KEY("RFCavity_name") REFERENCES "RFCavity" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_RFCavity_has_system_capability_has_system_capability_name" ON "RFCavity_has_system_capability" (has_system_capability_name);CREATE INDEX "ix_RFCavity_has_system_capability_RFCavity_name" ON "RFCavity_has_system_capability" ("RFCavity_name");
CREATE TABLE "Marker_has_sub_system" (
	"Marker_name" TEXT,
	has_sub_system_name TEXT,
	PRIMARY KEY ("Marker_name", has_sub_system_name),
	FOREIGN KEY("Marker_name") REFERENCES "Marker" (name),
	FOREIGN KEY(has_sub_system_name) REFERENCES "System" (name)
);CREATE INDEX "ix_Marker_has_sub_system_has_sub_system_name" ON "Marker_has_sub_system" (has_sub_system_name);CREATE INDEX "ix_Marker_has_sub_system_Marker_name" ON "Marker_has_sub_system" ("Marker_name");
CREATE TABLE "Marker_has_system_capability" (
	"Marker_name" TEXT,
	has_system_capability_name TEXT,
	PRIMARY KEY ("Marker_name", has_system_capability_name),
	FOREIGN KEY("Marker_name") REFERENCES "Marker" (name),
	FOREIGN KEY(has_system_capability_name) REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_Marker_has_system_capability_Marker_name" ON "Marker_has_system_capability" ("Marker_name");CREATE INDEX "ix_Marker_has_system_capability_has_system_capability_name" ON "Marker_has_system_capability" (has_system_capability_name);
CREATE TABLE "NaradModel" (
	id INTEGER NOT NULL,
	narad_config_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(narad_config_id) REFERENCES "NaradConfig" (id)
);CREATE INDEX "ix_NaradModel_id" ON "NaradModel" (id);
CREATE TABLE "Capability" (
	name TEXT NOT NULL,
	description TEXT,
	"ControlProfileFamily_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlProfileFamily_name") REFERENCES "ControlProfileFamily" (name)
);CREATE INDEX "ix_Capability_name" ON "Capability" (name);
CREATE TABLE "CapabilityProfile" (
	device_type VARCHAR(10),
	is_abstract BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	"ControlProfileFamily_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlProfileFamily_name") REFERENCES "ControlProfileFamily" (name)
);CREATE INDEX "ix_CapabilityProfile_name" ON "CapabilityProfile" (name);
CREATE TABLE "TypeSignalSet" (
	id INTEGER NOT NULL,
	magnet_signals_id INTEGER,
	quadrupole_signals_id INTEGER,
	corrector_signals_id INTEGER,
	dipole_signals_id INTEGER,
	bpm_signals_id INTEGER,
	rfcavity_signals_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(magnet_signals_id) REFERENCES "MagnetSignalSet" (id),
	FOREIGN KEY(quadrupole_signals_id) REFERENCES "QuadrupoleSignalSet" (id),
	FOREIGN KEY(corrector_signals_id) REFERENCES "CorrectorSignalSet" (id),
	FOREIGN KEY(dipole_signals_id) REFERENCES "DipoleSignalSet" (id),
	FOREIGN KEY(bpm_signals_id) REFERENCES "BPMSignalSet" (id),
	FOREIGN KEY(rfcavity_signals_id) REFERENCES "RFCavitySignalSet" (id)
);CREATE INDEX "ix_TypeSignalSet_id" ON "TypeSignalSet" (id);
CREATE TABLE "TypeSpecificCapability" (
	name TEXT NOT NULL,
	description TEXT,
	"CapabilityProfile_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("CapabilityProfile_name") REFERENCES "CapabilityProfile" (name)
);CREATE INDEX "ix_TypeSpecificCapability_name" ON "TypeSpecificCapability" (name);
CREATE TABLE "SignalDefinitions" (
	id INTEGER NOT NULL,
	type_signal_sets_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(type_signal_sets_id) REFERENCES "TypeSignalSet" (id)
);CREATE INDEX "ix_SignalDefinitions_id" ON "SignalDefinitions" (id);
CREATE TABLE "Beamline" (
	beamline_kind TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"NaradModel_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id)
);CREATE INDEX "ix_Beamline_name" ON "Beamline" (name);
CREATE TABLE "BeamlineElement" (
	element_kind VARCHAR(10),
	length FLOAT,
	capability_profile_family TEXT,
	capability_profile TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"NaradModel_id" INTEGER,
	facility_param_set_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY(capability_profile_family) REFERENCES "ControlProfileFamily" (name),
	FOREIGN KEY(capability_profile) REFERENCES "CapabilityProfile" (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id),
	FOREIGN KEY(facility_param_set_id) REFERENCES "FacilityParamSet" (id)
);CREATE INDEX "ix_BeamlineElement_name" ON "BeamlineElement" (name);
CREATE TABLE "CapabilityProfile_inherits_shared_capabilities" (
	"CapabilityProfile_name" TEXT,
	inherits_shared_capabilities_name TEXT,
	PRIMARY KEY ("CapabilityProfile_name", inherits_shared_capabilities_name),
	FOREIGN KEY("CapabilityProfile_name") REFERENCES "CapabilityProfile" (name),
	FOREIGN KEY(inherits_shared_capabilities_name) REFERENCES "Capability" (name)
);CREATE INDEX "ix_CapabilityProfile_inherits_shared_capabilities_inherits_shared_capabilities_name" ON "CapabilityProfile_inherits_shared_capabilities" (inherits_shared_capabilities_name);CREATE INDEX "ix_CapabilityProfile_inherits_shared_capabilities_CapabilityProfile_name" ON "CapabilityProfile_inherits_shared_capabilities" ("CapabilityProfile_name");
CREATE TABLE "FacilityConfig" (
	control_system TEXT,
	naming_convention TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"SignalLayer_id" INTEGER,
	signal_definitions_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalLayer_id") REFERENCES "SignalLayer" (id),
	FOREIGN KEY(signal_definitions_id) REFERENCES "SignalDefinitions" (id)
);CREATE INDEX "ix_FacilityConfig_name" ON "FacilityConfig" (name);
CREATE TABLE "Signal" (
	role VARCHAR(10),
	data_type VARCHAR(11),
	units TEXT,
	units_uri TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"Capability_name" TEXT,
	"TypeSpecificCapability_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Capability_name") REFERENCES "Capability" (name),
	FOREIGN KEY("TypeSpecificCapability_name") REFERENCES "TypeSpecificCapability" (name)
);CREATE INDEX "ix_Signal_name" ON "Signal" (name);
CREATE TABLE "InstanceSignalBinding" (
	is_property_of TEXT,
	pv_name TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"BeamlineElement_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("BeamlineElement_name") REFERENCES "BeamlineElement" (name)
);CREATE INDEX "ix_InstanceSignalBinding_name" ON "InstanceSignalBinding" (name);
CREATE TABLE "ElementParamSet" (
	frequency FLOAT,
	voltage FLOAT,
	phase FLOAT,
	angle_ref FLOAT,
	e1 FLOAT,
	e2 FLOAT,
	"Kn1" FLOAT,
	"Ksol" FLOAT,
	name TEXT NOT NULL,
	description TEXT,
	"BeamlineElement_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("BeamlineElement_name") REFERENCES "BeamlineElement" (name)
);CREATE INDEX "ix_ElementParamSet_name" ON "ElementParamSet" (name);
CREATE TABLE "Beamline_line" (
	"Beamline_name" TEXT,
	line_name TEXT,
	PRIMARY KEY ("Beamline_name", line_name),
	FOREIGN KEY("Beamline_name") REFERENCES "Beamline" (name),
	FOREIGN KEY(line_name) REFERENCES "BeamlineElement" (name)
);CREATE INDEX "ix_Beamline_line_line_name" ON "Beamline_line" (line_name);CREATE INDEX "ix_Beamline_line_Beamline_name" ON "Beamline_line" ("Beamline_name");
CREATE TABLE "FacilityConfig_facility_identifier" (
	"FacilityConfig_name" TEXT,
	facility_identifier_id INTEGER,
	PRIMARY KEY ("FacilityConfig_name", facility_identifier_id),
	FOREIGN KEY("FacilityConfig_name") REFERENCES "FacilityConfig" (name),
	FOREIGN KEY(facility_identifier_id) REFERENCES "FacilityIdentifier" (id)
);CREATE INDEX "ix_FacilityConfig_facility_identifier_FacilityConfig_name" ON "FacilityConfig_facility_identifier" ("FacilityConfig_name");CREATE INDEX "ix_FacilityConfig_facility_identifier_facility_identifier_id" ON "FacilityConfig_facility_identifier" (facility_identifier_id);
CREATE TABLE "SystemCapability_for_property" (
	"SystemCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("SystemCapability_name", for_property_name),
	FOREIGN KEY("SystemCapability_name") REFERENCES "SystemCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_SystemCapability_for_property_for_property_name" ON "SystemCapability_for_property" (for_property_name);CREATE INDEX "ix_SystemCapability_for_property_SystemCapability_name" ON "SystemCapability_for_property" ("SystemCapability_name");
CREATE TABLE "MagnetCapability_for_property" (
	"MagnetCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("MagnetCapability_name", for_property_name),
	FOREIGN KEY("MagnetCapability_name") REFERENCES "MagnetCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_MagnetCapability_for_property_for_property_name" ON "MagnetCapability_for_property" (for_property_name);CREATE INDEX "ix_MagnetCapability_for_property_MagnetCapability_name" ON "MagnetCapability_for_property" ("MagnetCapability_name");
CREATE TABLE "QuadrupoleCapability_for_property" (
	"QuadrupoleCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("QuadrupoleCapability_name", for_property_name),
	FOREIGN KEY("QuadrupoleCapability_name") REFERENCES "QuadrupoleCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_QuadrupoleCapability_for_property_for_property_name" ON "QuadrupoleCapability_for_property" (for_property_name);CREATE INDEX "ix_QuadrupoleCapability_for_property_QuadrupoleCapability_name" ON "QuadrupoleCapability_for_property" ("QuadrupoleCapability_name");
CREATE TABLE "CorrectorCapability_for_property" (
	"CorrectorCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("CorrectorCapability_name", for_property_name),
	FOREIGN KEY("CorrectorCapability_name") REFERENCES "CorrectorCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_CorrectorCapability_for_property_CorrectorCapability_name" ON "CorrectorCapability_for_property" ("CorrectorCapability_name");CREATE INDEX "ix_CorrectorCapability_for_property_for_property_name" ON "CorrectorCapability_for_property" (for_property_name);
CREATE TABLE "DipoleCapability_for_property" (
	"DipoleCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("DipoleCapability_name", for_property_name),
	FOREIGN KEY("DipoleCapability_name") REFERENCES "DipoleCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_DipoleCapability_for_property_DipoleCapability_name" ON "DipoleCapability_for_property" ("DipoleCapability_name");CREATE INDEX "ix_DipoleCapability_for_property_for_property_name" ON "DipoleCapability_for_property" (for_property_name);
CREATE TABLE "SolenoidCapability_for_property" (
	"SolenoidCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("SolenoidCapability_name", for_property_name),
	FOREIGN KEY("SolenoidCapability_name") REFERENCES "SolenoidCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_SolenoidCapability_for_property_for_property_name" ON "SolenoidCapability_for_property" (for_property_name);CREATE INDEX "ix_SolenoidCapability_for_property_SolenoidCapability_name" ON "SolenoidCapability_for_property" ("SolenoidCapability_name");
CREATE TABLE "InstrumentCapability_for_property" (
	"InstrumentCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("InstrumentCapability_name", for_property_name),
	FOREIGN KEY("InstrumentCapability_name") REFERENCES "InstrumentCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_InstrumentCapability_for_property_InstrumentCapability_name" ON "InstrumentCapability_for_property" ("InstrumentCapability_name");CREATE INDEX "ix_InstrumentCapability_for_property_for_property_name" ON "InstrumentCapability_for_property" (for_property_name);
CREATE TABLE "BPMCapability_for_property" (
	"BPMCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("BPMCapability_name", for_property_name),
	FOREIGN KEY("BPMCapability_name") REFERENCES "BPMCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_BPMCapability_for_property_BPMCapability_name" ON "BPMCapability_for_property" ("BPMCapability_name");CREATE INDEX "ix_BPMCapability_for_property_for_property_name" ON "BPMCapability_for_property" (for_property_name);
CREATE TABLE "CavityGradientCapability_for_property" (
	"CavityGradientCapability_name" TEXT,
	for_property_name TEXT,
	PRIMARY KEY ("CavityGradientCapability_name", for_property_name),
	FOREIGN KEY("CavityGradientCapability_name") REFERENCES "CavityGradientCapability" (name),
	FOREIGN KEY(for_property_name) REFERENCES "Signal" (name)
);CREATE INDEX "ix_CavityGradientCapability_for_property_CavityGradientCapability_name" ON "CavityGradientCapability_for_property" ("CavityGradientCapability_name");CREATE INDEX "ix_CavityGradientCapability_for_property_for_property_name" ON "CavityGradientCapability_for_property" (for_property_name);
CREATE TABLE "InstanceSignalBinding_is_instance_of" (
	"InstanceSignalBinding_name" TEXT,
	is_instance_of TEXT,
	PRIMARY KEY ("InstanceSignalBinding_name", is_instance_of),
	FOREIGN KEY("InstanceSignalBinding_name") REFERENCES "InstanceSignalBinding" (name)
);CREATE INDEX "ix_InstanceSignalBinding_is_instance_of_InstanceSignalBinding_name" ON "InstanceSignalBinding_is_instance_of" ("InstanceSignalBinding_name");CREATE INDEX "ix_InstanceSignalBinding_is_instance_of_is_instance_of" ON "InstanceSignalBinding_is_instance_of" (is_instance_of);
CREATE TABLE "InstanceSignalBinding_is_hosted_by" (
	"InstanceSignalBinding_name" TEXT,
	is_hosted_by TEXT,
	PRIMARY KEY ("InstanceSignalBinding_name", is_hosted_by),
	FOREIGN KEY("InstanceSignalBinding_name") REFERENCES "InstanceSignalBinding" (name)
);CREATE INDEX "ix_InstanceSignalBinding_is_hosted_by_is_hosted_by" ON "InstanceSignalBinding_is_hosted_by" (is_hosted_by);CREATE INDEX "ix_InstanceSignalBinding_is_hosted_by_InstanceSignalBinding_name" ON "InstanceSignalBinding_is_hosted_by" ("InstanceSignalBinding_name");
