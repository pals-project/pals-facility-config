export type NamedThingName = string;
export type CapabilityName = string;
export type FacilitySystemName = string;
export type SignalBindingName = string;
export type BeamlineName = string;
export type BeamlineElementName = string;
export type SystemName = string;
export type DeployedSystemName = string;
export type ControlSystemName = string;
export type DeviceName = string;
export type NamingConventionExampleExample = string;
export type InstrumentName = string;
export type SystemCapabilityName = string;
export type NamingConventionName = string;
export type TemplateComponentName = string;
export type TemplateExampleExample = string;
export type SignalName = string;
export type ObservableSignalName = string;
export type ActuatableSignalName = string;
export type InstanceSignalBindingName = string;
/**
* Controlled vocabulary for beamline element types, shared between the capability layer (CapabilityProfile.device_type) and the element layer (BeamlineElement.kind). Keeping the enum here keeps profile device_type values in sync with element kind values without circular imports. Values must stay aligned with CapabilityProfile.device_type. NOTE: The kind of a BeamlineElement must match the device_type of the Device referenced by is_instance_of.
*/
export enum ElementKindEnum {
    
    /** A field-free drift space between elements. */
    Drift = "Drift",
    /** A zero-length reference point or survey marker. */
    Marker = "Marker",
    /** Beam Position Monitor. */
    BPM = "BPM",
    /** Dipole corrector magnet for orbit correction. */
    Corrector = "Corrector",
    /** Dipole bending magnet. */
    Dipole = "Dipole",
    /** Quadrupole focusing/defocusing magnet. */
    Quadrupole = "Quadrupole",
    /** Solenoid magnet. */
    Solenoid = "Solenoid",
    /** Accelerating or bunching cavity. */
    CavityGradient = "CavityGradient",
    /** Radio-frequency accelerating or bunching cavity. */
    RFCavity = "RFCavity",
    /** Generic beam diagnostic instrument (halo monitor, viewer, etc.). */
    Instrument = "Instrument",
    /** Generic powered magnet device (supertype for all magnet kinds). */
    Magnet = "Magnet",
};
/**
* High-level system type for classification and querying. This is a broad categorization that can be used for filtering or grouping systems without needing to traverse the has_sub_system and has_system_capability edges.
*/
export enum SystemTypeEnum {
    
    /** A physical facility or installation (e.g. BTA, CEBAF, or UITF). */
    Facility = "Facility",
    /** A control system (e.g. epics) that manages device process variables. */
    ControlSystem = "ControlSystem",
    /** A powered magnet device/system (generic supertype for all magnet kinds). */
    Magnet = "Magnet",
};
/**
* Allowed data types for signal values.
*/
export enum DataTypeEnum {
    
    /** Integer. */
    int = "int",
    /** Single-precision floating-point. */
    float = "float",
    /** Double-precision floating-point. */
    double = "double",
    /** Text string. */
    string = "string",
    /** True/false value. */
    boolean = "boolean",
    /** A code referenced from an external coding system. */
    coded_value = "coded_value",
};
/**
* Controlled vocabulary for the semantic role of a signal within a capability.
*/
export enum SignalRoleEnum {
    
    /** A writable signal that commands a device setpoint. */
    control = "control",
    /** A readable signal that reports a measured or monitored quantity. Differs from status in that it typically indicates a continuous measurement (e.g. current readback, beam position) rather than discrete states. */
    readback = "readback",
    /** A signal that defines an operational limit or boundary on a control quantity. */
    constraint = "constraint",
    /** A signal reporting the device or system operational state. Differs from readback in that it typically indicates discrete states (e.g. fault, standby, ready) rather than a continuous measurement. */
    status = "status",
};
/**
* Allowed identifier types for facilities and other entities.
*/
export enum IdentifierTypeEnum {
    
    /** Digital Object Identifier (DOI). */
    doi = "doi",
    /** Archival Resource Key (ARK). */
    ark = "ark",
    /** Handle System identifier. */
    handle = "handle",
    /** Uniform Resource Locator (URL). */
    url = "url",
    /** Local identifier unique within a specific context or namespace. */
    local = "local",
    /** Any other type of identifier not covered by the above categories. */
    other = "other",
};


/**
 * Abstract base class providing identity and human-readable metadata.
 */
export interface NamedThing {
    /** Human-readable name or local string key for the entity. */
    name: string,
    /** Detailed description of the entity. */
    description?: string,
}


/**
 * Top-level NARAD document container.
 */
export interface NaradModel {
    /** Top-level NARAD configuration block (capability_layer + signal_layer). */
    narad_config?: NaradConfig,
    /** A top-level NARAD-system container for the ordered beamline definitions keyed by beamline name. Serializes as a keyed map by beamline name. */
    beamlines?: {[index: BeamlineName]: Beamline },
    /** Beamline element definitions referenced by name from beamline sequences. Serializes as a keyed map by element name. */
    elements?: BeamlineElement[],
}


/**
 * A top-level NARAD-system container for the: capability layer + signal layer.
 */
export interface NaradConfig {
    /** Version of the NARAD schema used in this document. */
    schema_version: string,
    /** A human-readable statement of the intended use or purpose of this NARAD configuration. */
    intent?: string,
    /** Identifier of the deployed system this configuration describes. */
    deployed_system: DeployedSystem,
    /** Identifier of the control system (e.g. epics) this configuration describes. */
    control_system: ControlSystem,
    /** Control Capability definitions for this facility. */
    capability_layer: {[index: CapabilityName]: Capability },
    /** Device Capability definitions keyed by capability name. */
    device_layer: {[index: DeviceName]: Device },
    /** Signal-layer container for facility-specific signal bindings. */
    signal_layer: SignalLayer,
}


/**
 * Capability-layer container for control profile families.
 */
export interface CapabilityLayer {
    capabilities?: {[index: CapabilityName]: Capability },
}


/**
 * A reusable device-type control profile that extends a generic shared capability with type-specific signals (e.g. QuadrupoleCurrentControlProfile).
 */
export interface Capability extends NamedThing {
    /** Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching. */
    device_type?: string,
    /** Links a type-specific capability to the generic capability it extends via rdfs:subClassOf. */
    subclass_of?: CapabilityName,
    /** Signals within a capability, keyed by a semantic signal name. */
    has_signal: {[index: SignalName]: Signal },
    /** Links the capability layer to the control systems it applies to via ssn:isPropertyOf. */
    is_property_of?: ControlSystemName,
}


/**
 * Signal-layer container for facility-specific signal bindings.
 */
export interface SignalLayer {
    /** Facility-specific signal binding configurations keyed by facility name. */
    facilities?: {[index: FacilitySystemName]: FacilitySystem },
}


/**
 * Facility-specific signal binding configuration.
 */
export interface FacilitySystem extends System {
    /** Relates a System to one of its control systems (SSN alignment to sub system). Use for facility → control-system, facility → device, and device → component decomposition.
 */
    has_control_system?: ControlSystemName,
    /** Structured container for facility-specific signal suffix templates. */
    hosts_device?: {[index: DeviceName]: Device },
}


/**
 * A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
 */
export interface FacilityIdentifier {
    /** The type of identifier used in the identifier slot (e.g. DOI, ARK, URL, local). */
    identifier_type?: string,
    /** The value of the identifier (e.g. the DOI string, ARK string, URL string, or local ID). */
    identifier_value?: string,
}


/**
 * A named control system suffix definition for one semantic signal. The suffix is used within in a template naming convention to construct the full control system PV name for a given device instance.
 */
export interface SignalBinding extends NamedThing {
    /** Facility-specific control-system (e.g. EPICS) naming suffix used to derive or interpret the signal binding, e.g. .S, M, :GSET.
 */
    signal_code_suffix?: string,
}


/**
 * A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
 */
export interface Beamline extends NamedThing {
    /** Indicates whether this beamline is a multipass recirculating line (true) or a single-pass line (false). */
    multipass?: boolean,
    /** Physical length of the element in meters. */
    length?: number,
    /** Name of a line item used as a reference point when  the beamline is used as a subline." */
    zero_point?: BeamlineElementName,
    /** For a beamline, indicates whether the orbit and Twiss parameters are periodic (true) or non-periodic (false). */
    periodic?: boolean,
    /** Ordered sequence of beamline elements in this beamline. Serializes as a list of element names (BeamlineElement names) referencing the keys in the elements map This is not a direct containment slot; the actual element definitions are in the top-level elements map. */
    line?: BeamlineElementName[],
}


/**
 * A single element in a beamline with its kind and optional NARAD capability annotations.
 */
export interface BeamlineElement extends NamedThing {
    /** NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Class that implements the signal binding.
 */
    is_instance_of?: string,
    /** Physical length of the element in meters. */
    length?: number,
    /** Control-system-specific, e.g. EPICS, suffix definitions keyed by signal name within a device/domain set. Can also be used to link a BeamlineElement instance to the signal bindings that observe or actuate it,  since the instance of the element is directly observed or controlled through a Device. Facility-specific bindings of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline element instance. These are the keyed by the semantic signal name (e.g. current_readback) rather than the control-system suffix, which is captured in the SignalBinding. The semantic signal name links the instance binding to the abstract Signal definition and its place in the capability profile, while the SignalBinding captures the concrete implementations of the abstract SignalBindings referenced by the element's capability profile. */
    is_observed_by?: {[index: InstanceSignalBindingName]: InstanceSignalBinding },
    /** Named physics-parameter blocks for this element (e.g. RFP, BendP, MagneticMultipoleP). */
    param_set?: ElementParamSet,
}


/**
 * A physical, logical, or cyber-physical system involved in sensing, monitoring, control, or actuation. Broadly aligned to ssn:System.

 */
export interface System extends NamedThing {
    /** High-level system type for classification and querying. */
    system_type?: string,
    /** Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
 */
    has_sub_system?: SystemName[],
    /** Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
 */
    has_system_capability?: {[index: SystemCapabilityName]: SystemCapability },
}


/**
 * A deployed system, with an identified facility, that is the subject of a NARAD configuration.  This is the child of the target of the narad_config.deployed_system slot. In the SSN graph a DeployedSystem is a broad mapping to the ssn:Deployment and also is equivalent to the signal_layers.facilities entries.

 */
export interface DeployedSystem extends System {
    /** Globally unique identifier for the facility, with specified type and value. */
    facility_identifier?: FacilityIdentifier[],
    /** Relates a System to one of its control systems (SSN alignment to sub system). Use for facility → control-system, facility → device, and device → component decomposition.
 */
    has_control_system?: ControlSystemName,
}


/**
 * A control system (e.g. EPICS) that manages device process variables. In the SSN graph a ControlSystem is a subsystem of the Facility.

 */
export interface ControlSystem extends System {
    /** Signal naming conventions used by this control system defined in a machine actionable manner.  This is where you would capture the patterns/templates for how control system PVs or signals are constructed for this control system,  for example, the EPICS convention of using suffixes like .R, .S, :GSET to indicate readback, status, and setpoint signals. Multiple naming conventions can be captured if a control system uses more than one convention for different device types or domains. */
    has_naming_convention?: NamingConvention[],
}


/**
 * A system representing a beam diagnostic instrument, magnet, or other non-magnet device. It represents the instrument as a whole rather than the control system for that instrument. In the SSN graph a Device is a subsystem of the Facility and a sibling to the ControlSystem. Also used in the SignalLayer to group signal bindings by device type. Aligned to ssn:System.

 */
export interface Device extends System {
    /** Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching. */
    device_type: string,
    /** Relates a System to one of its subsystems (SSN alignment). Use for facility → control-system, facility → device, and device → component decomposition.
 */
    has_sub_system?: SystemName[],
    /** -> NARAD alias for rdfs:subClassOf. Links a type-specific capability to the generic capability it extends. In the graph this edge is labelled narad:subclassOf. */
    subclass_of?: SystemName,
    /** Relates a System to a SystemCapability it supports (SSN-System alignment). Prefer this over directly attaching signals to systems when capability context matters.
 */
    has_system_capability?: SystemCapabilityName,
    /** Control-system-specific, e.g. EPICS, suffix definitions keyed by signal name within a device/domain set. Can also be used to link a BeamlineElement instance to the signal bindings that observe or actuate it,  since the instance of the element is directly observed or controlled through a Device. Facility-specific bindings of signals to control-system interfaces (e.g. EPICS PVs) for a specific beamline element instance. These are the keyed by the semantic signal name (e.g. current_readback) rather than the control-system suffix, which is captured in the SignalBinding. The semantic signal name links the instance binding to the abstract Signal definition and its place in the capability profile, while the SignalBinding captures the concrete implementations of the abstract SignalBindings referenced by the element's capability profile. */
    is_observed_by?: {[index: SignalBindingName]: SignalBinding },
}


/**
 * An example of a control system naming convention, illustrating how the template is used to generate full control system PV names from semantic signal names and device instance information.  This can be used to provide concrete examples of the expected PV naming convention for different device types and signals based on the defined NamingConvention template.

 */
export interface NamingConventionExample {
    /** A single example of how this naming convention is applied to a specific device instance and signal. */
    example?: string,
    /** Detailed description of the entity. */
    description?: string,
}


/**
 * A generic beam diagnostic instrument.
 */
export interface Instrument extends System {
}


/**
 * A capability of a system. SystemCapability describes what a system can expose, monitor, control, or actuate with respect to one or more signals. Aligned to ssn-system:SystemCapability; linked from System instances via ssn-system:hasSystemCapability, and from Signals via ssn:forProperty. Profile-level inheritance (shared vs. type-specific signals) is expressed in CapabilityProfile, not here.

 */
export interface SystemCapability extends NamedThing {
    /** SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
 */
    for_property?: string[],
    /** Represents the generic, semantic class of the device (e.g., "Quadrupole", "BPM") and is used for capability, instrument, and signal profile matching. */
    device_type?: string,
}


/**
 * A template for constructing facility-specific signal names from a semantic signal name and a control-system-specific suffix.  The template is used to generate the full control system PV name for a given device instance and semantic signal by substituting the device name and signal code suffix into the template.

 */
export interface NamingConvention extends NamedThing {
    /** A template string for constructing control system PV names based on the semantic signal name and device instance. This can include placeholders for the device name and signal suffix, e.g. {device_name}{signal_suffix}. */
    template?: string,
    /** Structured components of the naming convention template, for capturing the template in a more machine-actionable way than a raw string.  For example, you could have components for the device name, signal suffix, and any fixed parts of the naming convention. */
    template_components?: TemplateComponent[],
    /** A regex pattern that the full resolved value (e.g. after template substitution) must match for validation. */
    full_pattern?: string,
    /** Examples of how this naming convention is applied to specific device instances and signals. */
    examples?: NamingConventionExample[],
}


/**
 * A component of a naming convention template, representing a variable part of the control system PV name that is substituted based on the device instance and signal definition.  For example, in the template "{device_name}{signal_code_suffix}", "device_name" and "signal_code_suffix" would be TemplateComponents that are replaced with the actual device name and signal code suffix for each specific binding.

 */
export interface TemplateComponent extends NamedThing {
    /** Indicates whether this configuration element is required for a valid configuration. */
    required?: boolean,
    /** A regex pattern that the value of this slot must match for validation. */
    pattern?: string,
}


/**
 * An example of a control system PV name generated from a naming convention template, along with a description of what it represents.  This can be used to illustrate how the template works in practice and to provide concrete examples of the expected PV naming convention for different device types and signals.

 */
export interface TemplateExample {
    /** A single example of how this naming convention is applied to a specific device instance and signal. */
    example?: string,
    /** Detailed description of the entity. */
    description?: string,
}


/**
 * Domain term for a control-system signal. A Signal represents an identifiable quantity, state, setpoint, readback, limit, or status. In SSN/SOSA alignment, NARAD Signals are treated as properties of systems (ssn:forProperty). The concrete facility binding is captured in SignalBinding.

 */
export interface Signal extends NamedThing {
    /** The semantic role of the signal within its capability. */
    role?: string,
    /** The data type of the signal's value. */
    data_type?: string,
    /** Conventional unit symbol (e.g. A, MV/m, T*m, G/cm). */
    units?: string,
    /** Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/. */
    units_uri?: string,
}


/**
 * A NARAD signal that is read, monitored, observed, or exposed by a system. Examples: current_readback, status, horizontal_beam_position, gradient_readback. Aligned to sosa:ObservableProperty.

 */
export interface ObservableSignal extends Signal {
}


/**
 * A NARAD signal that can be commanded, set, or acted upon. Examples: current_setpoint, strength_setpoint, kick_setpoint, field_setpoint, current_min, current_max, gradient_setpoint. Aligned to sosa:ActuatableProperty.

 */
export interface ActuatableSignal extends Signal {
}


/**
 * A facility-specific binding between a NARAD Signal and an implementation interface (e.g. an EPICS process variable). Modeled as sosa:Sensor because it describes how a signal is observed, monitored, or actuated. ssn:forProperty → Signal; narad:isInstanceOf → the capability class.

 */
export interface InstanceSignalBinding extends NamedThing {
    /** Fully-resolved facility-specific process variable name, e.g. MQWK202:STAT or MQWK202:BDL.
 */
    pv_name?: string,
    /** NARAD alias for rdf:type. Links a facility-specific instance node to the LinkML class or semantic class it instantiates. In the graph this edge is labelled narad:isInstanceOf. Values are typically the rdf:type of the Class that implements the signal binding.
 */
    is_instance_of?: SignalName,
    /** SystemCapability → Signal: the capability can expose, monitor, control, or actuate that signal.
 */
    for_property?: SignalBindingName,
    /** Links an InstanceSignalBinding to the FacilitySystem it belongs to. This is the edge that connects the facility-specific bindings to the Facility node in the graph.
 */
    is_hosted_by?: string,
    /** Inverse of for_property: links the Class Signal to the Class of SignalBinding Procedure that implements it. This can also link the Instance of a SignalBinding to the ControlSystem that implements it. This is the edge that connects the signal definitions to the facility-specific bindings in the graph. Values are typically the ControlSystem that implements this binding, e.g. narad:epics (for EPICS control system). NOTE: The value of this slot must match one of the values in narad_config.has_sub_system.
 */
    is_property_of?: ControlSystemName,
}


/**
 * Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP, MagneticMultipoleP, SolenoidP).
 */
export interface ElementParamSet {
    /** RF frequency in Hz. */
    frequency?: number,
    /** RF voltage in volts. */
    voltage?: number,
    /** RF phase in degrees. */
    phase?: number,
    /** Reference bend angle in radians. */
    angle_ref?: number,
    /** Entry edge angle in radians. */
    e1?: number,
    /** Exit edge angle in radians. */
    e2?: number,
    /** First-order magnetic multipole coefficient (quadrupole strength). */
    Kn1?: number,
    /** Solenoid integrated field strength. */
    Ksol?: number,
    /** Facility-specific element parameters (type designation, model name, open property map). */
    facility_param_set?: FacilityParamSet,
}


/**
 * Facility-specific element parameters block for beamline elements. Differs from an ElementParamSet in that it captures facility-specific metadata about the element (e.g. type designation, model name) rather than physics parameters.
 */
export interface FacilityParamSet {
    /** capture the facility-specific or local designation (e.g., "QW", "WarmCavity", "HCorrector").  Isused for local naming, inventory, or legacy mapping of instances of facility elements (within elements:)  to the facility-specific type designations used in the control system or elsewhere at the facility. */
    facility_element_type?: string,
    /** Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK). */
    modeled_as?: string,
    /** Intentionally open-ended key-value property map for element-specific or facility-specific parameters. */
    properties?: AnyValue,
}


/**
 * Unconstrained type — accepts any YAML/JSON value (string, number, object, list, etc.).
 */
export interface AnyValue {
}



