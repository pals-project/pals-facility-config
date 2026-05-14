-- # Abstract Class: NamedThing Description: Abstract base class providing identity and human-readable metadata.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: NaradModel Description: Top-level NARAD document container.
--     * Slot: id
--     * Slot: narad_config_id Description: Top-level NARAD configuration block (capability_layer + signal_layer).
-- # Class: NaradConfig Description: A top-level NARAD-system container for the: capability layer + signal layer.
--     * Slot: id
--     * Slot: schema_version Description: Version of the NARAD schema used in this document.
--     * Slot: intent Description: A human-readable statement of the intended use or purpose of this NARAD configuration.
--     * Slot: deployed_system Description: Identifier of the deployed system this configuration describes.
--     * Slot: signal_layer_id Description: Signal-layer container for facility-specific signal bindings.
-- # Class: CapabilityLayer Description: Capability-layer container for control profile families.
--     * Slot: id
-- # Class: ControlCapability Description: A reusable device-type control profile that extends a generic shared capability with type-specific signals (e.g. QuadrupoleCurrentControlProfile).
--     * Slot: device_type Description: Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching.
--     * Slot: subclass_of Description: -> NARAD alias for rdfs:subClassOf. Links a type-specific capability to the generic capability it extends. In the graph this edge is labelled narad:subclassOf.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: NaradConfig_id Description: Autocreated FK slot
--     * Slot: CapabilityLayer_id Description: Autocreated FK slot
-- # Class: SignalLayer Description: Signal-layer container for facility-specific signal bindings.
--     * Slot: id
-- # Class: FacilitySystem Description: Facility-specific signal binding configuration.
--     * Slot: naming_convention Description: Signal naming convention template (e.g. <device><signal_code>).
--     * Slot: system_type Description: High-level system type for classification and querying.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: SignalLayer_id Description: Autocreated FK slot
--     * Slot: control_system_name Description: Identifier of the control system (e.g. epics).
-- # Class: FacilityIdentifier Description: A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
--     * Slot: id
--     * Slot: identifier_type Description: The type of identifier used in the identifier slot (e.g. DOI, ARK, URL, local).
--     * Slot: identifier_value Description: The value of the identifier (e.g. the DOI string, ARK string, URL string, or local ID).
-- # Class: SignalDefinitions Description: Signal binding set scoped to a device type or device domain.
--     * Slot: device_type Description: Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: FacilitySystem_name Description: Autocreated FK slot
-- # Class: SignalBinding Description: A named control system suffix definition for one semantic signal. The suffix is used within in a template naming convention to construct the full control system PV name for a given device instance.
--     * Slot: control_system_suffix Description: Facility-specific control-system (e.g. EPICS) naming suffix used to derive or interpret the signal binding, e.g. .S, M, :GSET.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: SignalDefinitions_name Description: Autocreated FK slot
-- # Class: Beamline Description: A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
--     * Slot: multipass Description: Indicates whether this beamline is a multipass recirculating line (true) or a single-pass line (false).
--     * Slot: length Description: Physical length of the element in meters.
--     * Slot: zero_point Description: Name of a line item used as a reference point when  the beamline is used as a subline."
--     * Slot: periodic Description: For a beamline, indicates whether the orbit and Twiss parameters are periodic (true) or non-periodic (false).
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: NaradModel_id Description: Autocreated FK slot
-- # Class: BeamlineElement Description: A single element in a beamline with its kind and optional NARAD capability annotations.
--     * Slot: is_instance_of Description: NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Class that implements the signal binding.
--     * Slot: length Description: Physical length of the element in meters.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: NaradModel_id Description: Autocreated FK slot
--     * Slot: param_set_id Description: Named physics-parameter blocks for this element (e.g. RFP, BendP, MagneticMultipoleP).
-- # Class: System Description: A physical, logical, or cyber-physical system involved in sensing, monitoring, control, or actuation. Broadly aligned to ssn:System.
--     * Slot: system_type Description: High-level system type for classification and querying.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: FacilitySystem_name Description: Autocreated FK slot
--     * Slot: System_name Description: Autocreated FK slot
--     * Slot: ControlSystem_name Description: Autocreated FK slot
--     * Slot: InstrumentSystem_name Description: Autocreated FK slot
--     * Slot: Instrument_name Description: Autocreated FK slot
-- # Class: ControlSystem Description: A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a subsystem of the Facility.
--     * Slot: naming_convention Description: Signal naming convention template (e.g. <device><signal_code>).
--     * Slot: system_type Description: High-level system type for classification and querying.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: InstrumentSystem Description: A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the instrument as a whole rather than the control system for that instrument. In the SSN graph an InstrumentSystem is a subsystem of the Facility and a sibling to the ControlSystem.
--     * Slot: device_type Description: Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching.
--     * Slot: has_system_capability Description: Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
--     * Slot: system_type Description: High-level system type for classification and querying.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: NaradConfig_id Description: Autocreated FK slot
-- # Class: Instrument Description: A generic beam diagnostic instrument.
--     * Slot: system_type Description: High-level system type for classification and querying.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
-- # Class: SystemCapability Description: A capability of a system. SystemCapability describes what a system can expose, monitor, control, or actuate with respect to one or more signals. Aligned to ssn-system:SystemCapability; linked from System instances via ssn-system:hasSystemCapability, and from Signals via ssn:forProperty. Profile-level inheritance (shared vs. type-specific signals) is expressed in CapabilityProfile, not here.
--     * Slot: device_type Description: Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: FacilitySystem_name Description: Autocreated FK slot
--     * Slot: System_name Description: Autocreated FK slot
--     * Slot: ControlSystem_name Description: Autocreated FK slot
--     * Slot: Instrument_name Description: Autocreated FK slot
-- # Class: Signal Description: Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The concrete facility binding is captured in SignalBinding.
--     * Slot: role Description: The semantic role of the signal within its capability.
--     * Slot: data_type Description: The data type of the signal's value.
--     * Slot: units Description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
--     * Slot: units_uri Description: Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: ControlCapability_name Description: Autocreated FK slot
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
--     * Slot: pv_name Description: Fully-resolved facility-specific process variable name, e.g. MQWK202:STAT or MQWK202:BDL.
--     * Slot: is_instance_of Description: NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Class that implements the signal binding.
--     * Slot: for_property Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
--     * Slot: is_hosted_by Description: Links an InstanceSignalBinding to the FacilitySystem it belongs to. This is the edge that connects the facility-specific bindings to the Facility node in the graph.
--     * Slot: is_property_of Description: Inverse of for_property: links the Class Signal to the Class of SignalBinding Procedure that implements it. This can also link the Instance of a SignalBinding to the ControlSystem that implements it. This is the edge that connects the signal definitions to the facility-specific bindings in the graph. Values are typically the ControlSystem that implements this binding, e.g. narad:epics (for EPICS control system). NOTE: The value of this slot must match one of the values in narad_config.has_sub_system.
--     * Slot: name Description: Human-readable name or local string key for the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: BeamlineElement_name Description: Autocreated FK slot
-- # Class: ElementParamSet Description: Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP, MagneticMultipoleP, SolenoidP).
--     * Slot: id
--     * Slot: frequency Description: RF frequency in Hz.
--     * Slot: voltage Description: RF voltage in volts.
--     * Slot: phase Description: RF phase in degrees.
--     * Slot: angle_ref Description: Reference bend angle in radians.
--     * Slot: e1 Description: Entry edge angle in radians.
--     * Slot: e2 Description: Exit edge angle in radians.
--     * Slot: Kn1 Description: First-order magnetic multipole coefficient (quadrupole strength).
--     * Slot: Ksol Description: Solenoid integrated field strength.
--     * Slot: facility_param_set_id Description: Facility-specific element parameters (type designation, model name, open property map).
-- # Class: FacilityParamSet Description: Facility-specific element parameters block for beamline elements. Differs from an ElementParamSet in that it captures facility-specific metadata about the element (e.g. type designation, model name) rather than physics parameters.
--     * Slot: id
--     * Slot: facility_element_type Description: capture the facility-specific or local designation (e.g., "QW", "WarmCavity", "HCorrector").  Isused for local naming, inventory, or legacy mapping of instances of facility elements (within elements:)  to the facility-specific type designations used in the control system or elsewhere at the facility.
--     * Slot: modeled_as Description: Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).
--     * Slot: properties_id Description: Intentionally open-ended key-value property map for element-specific or facility-specific parameters.
-- # Class: AnyValue Description: Unconstrained type — accepts any YAML/JSON value (string, number, object, list, etc.).
--     * Slot: id
-- # Class: NaradConfig_has_sub_system
--     * Slot: NaradConfig_id Description: Autocreated FK slot
--     * Slot: has_sub_system_name Description: Identifier of the control system (e.g. epics) this configuration describes.
-- # Class: FacilitySystem_facility_identifier
--     * Slot: FacilitySystem_name Description: Autocreated FK slot
--     * Slot: facility_identifier_id Description: Globally unique identifier for the facility, with specified type and value.
-- # Class: Beamline_line
--     * Slot: Beamline_name Description: Autocreated FK slot
--     * Slot: line_name Description: Ordered sequence of beamline elements in this beamline. Serializes as a list of element names (BeamlineElement names) referencing the keys in the elements map This is not a direct containment slot; the actual element definitions are in the top-level elements map.
-- # Class: SystemCapability_for_property
--     * Slot: SystemCapability_name Description: Autocreated FK slot
--     * Slot: for_property Description: SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.

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
CREATE TABLE "System" (
	system_type VARCHAR(13),
	name TEXT NOT NULL,
	description TEXT,
	"FacilitySystem_name" TEXT,
	"System_name" TEXT,
	"ControlSystem_name" TEXT,
	"InstrumentSystem_name" TEXT,
	"Instrument_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("FacilitySystem_name") REFERENCES "FacilitySystem" (name),
	FOREIGN KEY("System_name") REFERENCES "System" (name),
	FOREIGN KEY("ControlSystem_name") REFERENCES "ControlSystem" (name),
	FOREIGN KEY("InstrumentSystem_name") REFERENCES "InstrumentSystem" (name),
	FOREIGN KEY("Instrument_name") REFERENCES "Instrument" (name)
);CREATE INDEX "ix_System_name" ON "System" (name);
CREATE TABLE "ControlSystem" (
	naming_convention TEXT,
	system_type VARCHAR(13),
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_ControlSystem_name" ON "ControlSystem" (name);
CREATE TABLE "InstrumentSystem" (
	device_type VARCHAR(14),
	has_system_capability TEXT,
	system_type VARCHAR(13),
	name TEXT NOT NULL,
	description TEXT,
	"NaradConfig_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY(has_system_capability) REFERENCES "SystemCapability" (name),
	FOREIGN KEY("NaradConfig_id") REFERENCES "NaradConfig" (id)
);CREATE INDEX "ix_InstrumentSystem_name" ON "InstrumentSystem" (name);
CREATE TABLE "Instrument" (
	system_type VARCHAR(13),
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Instrument_name" ON "Instrument" (name);
CREATE TABLE "SystemCapability" (
	device_type VARCHAR(14),
	name TEXT NOT NULL,
	description TEXT,
	"FacilitySystem_name" TEXT,
	"System_name" TEXT,
	"ControlSystem_name" TEXT,
	"Instrument_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("FacilitySystem_name") REFERENCES "FacilitySystem" (name),
	FOREIGN KEY("System_name") REFERENCES "System" (name),
	FOREIGN KEY("ControlSystem_name") REFERENCES "ControlSystem" (name),
	FOREIGN KEY("Instrument_name") REFERENCES "Instrument" (name)
);CREATE INDEX "ix_SystemCapability_name" ON "SystemCapability" (name);
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
CREATE TABLE "FacilitySystem" (
	naming_convention TEXT,
	system_type VARCHAR(13),
	name TEXT NOT NULL,
	description TEXT,
	"SignalLayer_id" INTEGER,
	control_system_name TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalLayer_id") REFERENCES "SignalLayer" (id),
	FOREIGN KEY(control_system_name) REFERENCES "ControlSystem" (name)
);CREATE INDEX "ix_FacilitySystem_name" ON "FacilitySystem" (name);
CREATE TABLE "FacilityParamSet" (
	id INTEGER NOT NULL,
	facility_element_type TEXT,
	modeled_as TEXT,
	properties_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(properties_id) REFERENCES "AnyValue" (id)
);CREATE INDEX "ix_FacilityParamSet_id" ON "FacilityParamSet" (id);
CREATE TABLE "SystemCapability_for_property" (
	"SystemCapability_name" TEXT,
	for_property TEXT,
	PRIMARY KEY ("SystemCapability_name", for_property),
	FOREIGN KEY("SystemCapability_name") REFERENCES "SystemCapability" (name)
);CREATE INDEX "ix_SystemCapability_for_property_SystemCapability_name" ON "SystemCapability_for_property" ("SystemCapability_name");CREATE INDEX "ix_SystemCapability_for_property_for_property" ON "SystemCapability_for_property" (for_property);
CREATE TABLE "NaradConfig" (
	id INTEGER NOT NULL,
	schema_version TEXT NOT NULL,
	intent TEXT,
	deployed_system TEXT NOT NULL,
	signal_layer_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(deployed_system) REFERENCES "FacilitySystem" (name),
	FOREIGN KEY(signal_layer_id) REFERENCES "SignalLayer" (id)
);CREATE INDEX "ix_NaradConfig_id" ON "NaradConfig" (id);
CREATE TABLE "SignalDefinitions" (
	device_type VARCHAR(14),
	name TEXT NOT NULL,
	description TEXT,
	"FacilitySystem_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("FacilitySystem_name") REFERENCES "FacilitySystem" (name)
);CREATE INDEX "ix_SignalDefinitions_name" ON "SignalDefinitions" (name);
CREATE TABLE "ElementParamSet" (
	id INTEGER NOT NULL,
	frequency FLOAT,
	voltage FLOAT,
	phase FLOAT,
	angle_ref FLOAT,
	e1 FLOAT,
	e2 FLOAT,
	"Kn1" FLOAT,
	"Ksol" FLOAT,
	facility_param_set_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(facility_param_set_id) REFERENCES "FacilityParamSet" (id)
);CREATE INDEX "ix_ElementParamSet_id" ON "ElementParamSet" (id);
CREATE TABLE "FacilitySystem_facility_identifier" (
	"FacilitySystem_name" TEXT,
	facility_identifier_id INTEGER,
	PRIMARY KEY ("FacilitySystem_name", facility_identifier_id),
	FOREIGN KEY("FacilitySystem_name") REFERENCES "FacilitySystem" (name),
	FOREIGN KEY(facility_identifier_id) REFERENCES "FacilityIdentifier" (id)
);CREATE INDEX "ix_FacilitySystem_facility_identifier_FacilitySystem_name" ON "FacilitySystem_facility_identifier" ("FacilitySystem_name");CREATE INDEX "ix_FacilitySystem_facility_identifier_facility_identifier_id" ON "FacilitySystem_facility_identifier" (facility_identifier_id);
CREATE TABLE "NaradModel" (
	id INTEGER NOT NULL,
	narad_config_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(narad_config_id) REFERENCES "NaradConfig" (id)
);CREATE INDEX "ix_NaradModel_id" ON "NaradModel" (id);
CREATE TABLE "ControlCapability" (
	device_type VARCHAR(14),
	subclass_of TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"NaradConfig_id" INTEGER,
	"CapabilityLayer_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY(subclass_of) REFERENCES "ControlCapability" (name),
	FOREIGN KEY("NaradConfig_id") REFERENCES "NaradConfig" (id),
	FOREIGN KEY("CapabilityLayer_id") REFERENCES "CapabilityLayer" (id)
);CREATE INDEX "ix_ControlCapability_name" ON "ControlCapability" (name);
CREATE TABLE "SignalBinding" (
	control_system_suffix TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"SignalDefinitions_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalDefinitions_name") REFERENCES "SignalDefinitions" (name)
);CREATE INDEX "ix_SignalBinding_name" ON "SignalBinding" (name);
CREATE TABLE "NaradConfig_has_sub_system" (
	"NaradConfig_id" INTEGER,
	has_sub_system_name TEXT NOT NULL,
	PRIMARY KEY ("NaradConfig_id", has_sub_system_name),
	FOREIGN KEY("NaradConfig_id") REFERENCES "NaradConfig" (id),
	FOREIGN KEY(has_sub_system_name) REFERENCES "ControlSystem" (name)
);CREATE INDEX "ix_NaradConfig_has_sub_system_NaradConfig_id" ON "NaradConfig_has_sub_system" ("NaradConfig_id");CREATE INDEX "ix_NaradConfig_has_sub_system_has_sub_system_name" ON "NaradConfig_has_sub_system" (has_sub_system_name);
CREATE TABLE "BeamlineElement" (
	is_instance_of TEXT,
	length FLOAT,
	name TEXT NOT NULL,
	description TEXT,
	"NaradModel_id" INTEGER,
	param_set_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id),
	FOREIGN KEY(param_set_id) REFERENCES "ElementParamSet" (id)
);CREATE INDEX "ix_BeamlineElement_name" ON "BeamlineElement" (name);
CREATE TABLE "Signal" (
	role VARCHAR(10),
	data_type VARCHAR(11),
	units TEXT,
	units_uri TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"ControlCapability_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlCapability_name") REFERENCES "ControlCapability" (name)
);CREATE INDEX "ix_Signal_name" ON "Signal" (name);
CREATE TABLE "Beamline" (
	multipass BOOLEAN,
	length FLOAT,
	zero_point TEXT,
	periodic BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	"NaradModel_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY(zero_point) REFERENCES "BeamlineElement" (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id)
);CREATE INDEX "ix_Beamline_name" ON "Beamline" (name);
CREATE TABLE "InstanceSignalBinding" (
	pv_name TEXT,
	is_instance_of TEXT,
	for_property TEXT,
	is_hosted_by TEXT,
	is_property_of TEXT,
	name TEXT NOT NULL,
	description TEXT,
	"BeamlineElement_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("BeamlineElement_name") REFERENCES "BeamlineElement" (name)
);CREATE INDEX "ix_InstanceSignalBinding_name" ON "InstanceSignalBinding" (name);
CREATE TABLE "Beamline_line" (
	"Beamline_name" TEXT,
	line_name TEXT,
	PRIMARY KEY ("Beamline_name", line_name),
	FOREIGN KEY("Beamline_name") REFERENCES "Beamline" (name),
	FOREIGN KEY(line_name) REFERENCES "BeamlineElement" (name)
);CREATE INDEX "ix_Beamline_line_line_name" ON "Beamline_line" (line_name);CREATE INDEX "ix_Beamline_line_Beamline_name" ON "Beamline_line" ("Beamline_name");
