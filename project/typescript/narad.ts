export type AffiliationId = string;
export type ComponentId = string;
export type PhysicalComponentId = string;
export type VirtualComponentId = string;
export type BeamLineId = string;
export type SignalId = string;
export type MagnetId = string;
export type SolenoidId = string;
export type MultipoleId = string;
export type BendId = string;
export type QuadrupoleId = string;
export type OctupoleId = string;
export type SextupoleId = string;
export type KickerId = string;
export type ACKickerId = string;
export type DiagnosticDeviceId = string;
export type BeamProfileMonitorId = string;
export type BeamPositionMonitorId = string;
export type ApertureId = string;
export type RadiationMonitorId = string;
export type CavityId = string;
export type CrabCavityId = string;
export type RFCavityId = string;
export type NormalConductingRFCavityId = string;
export type SuperConductingRFCavityId = string;
export type SupportingFacilityComponentId = string;
export type BookkeepingComponentId = string;
export type MarkerId = string;
export type BeamLineSectionId = string;
export type RelationshipId = string;
export type SignalBindingId = string;
export type ComponentRelationId = string;
/**
* Controlled values for identifier types.
*/
export enum IdentifierTypeEnum {
    
    /** Digital Object Identifier. */
    DOI = "DOI",
    /** Persistent Uniform Resource Locator. */
    PURL = "PURL",
    /** Research Organization Registry identifier. */
    ROR = "ROR",
    /** Local identifier, specific to the facility or source system. */
    LOCAL = "LOCAL",
    /** Uniform Resource Locator. */
    URL = "URL",
    /** Archival Resource Key. */
    ARK = "ARK",
};
/**
* Controlled values for facility-local source systems.
*/
export enum SourceSystemEnum {
    
    /** EPICS control system. */
    EPICS = "EPICS",
    /** EPICS Channel Access source. */
    EPICS_ChannelAccess = "EPICS_ChannelAccess",
    /** PALS-Ext or middle-layer channel/export system. */
    PALS_Ext = "PALS_Ext",
    /** MYA archive or historical channel service. */
    MYA = "MYA",
    /** Facility element database. */
    ElementDatabase = "ElementDatabase",
    /** Facility channel database. */
    ChannelDatabase = "ChannelDatabase",
    /** Simulation or model-derived signal source. */
    Simulation = "Simulation",
    /** Other source system. */
    Other = "Other",
};
/**
* Controlled values for physical relation to the beamline.
*/
export enum PhysicalRelationEnum {
    
    /** Beam passes through the physical component or beamline aperture. The physical component is physically on the beamline. */
    Inline = "Inline",
    /** Mechanically attached to the beam pipe or vacuum envelope. */
    AttachedToPipe = "AttachedToPipe",
    /** Near and operationally associated with the beamline. */
    NearBeamLine = "NearBeamLine",
    /** Supports accelerator operation without a specific beam-pipe placement. */
    SupportingFacility = "SupportingFacility",
};
/**
* Controlled values for virtual relation to the beamline.
*/
export enum VirtualRelationEnum {
    
    /** Beam passes through the virtual component. Used for virtual components like Markers that represent important locations on the beamline but don't have a physical instantiation. */
    Inline = "Inline",
    /** Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the BeamLine structure and function but don't have a direct physical relationship to the beam path,  such as BeamLineSections or Markers that are not inline with the beam. */
    AssociatedWithBeamLine = "AssociatedWithBeamLine",
    /** Not inline with the BeamLine and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the BeamLine, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the BeamLine structure. */
    NotAssociatedWithBeamLine = "NotAssociatedWithBeamLine",
};
/**
* Broad device-level functions.
*/
export enum PhysicalFunctionEnum {
    
    /** Focuses or defocuses the beam. */
    Focusing = "Focusing",
    /** Steers the beam in a transverse plane. */
    Steering = "Steering",
    /** Measures transverse beam position. */
    BeamPositionMeasurement = "BeamPositionMeasurement",
    /** Generates or maintains vacuum. */
    VacuumGeneration = "VacuumGeneration",
    /** Monitors radiation dose or dose rate. */
    RadiationMonitoring = "RadiationMonitoring",
    /** Measures beam or machine state. */
    Measurement = "Measurement",
    /** Accelerates the beam. */
    BeamAcceleration = "BeamAcceleration",
    /** Detects beam loss. */
    BeamLossDetection = "BeamLossDetection",
    /** Measures beam current or intensity. */
    BeamCurrentMeasurement = "BeamCurrentMeasurement",
    /** Measures beam profile. */
    BeamProfileMeasurement = "BeamProfileMeasurement",
    /** Supports machine protection. */
    MachineProtection = "MachineProtection",
    /** Supports timing or synchronization. */
    TimingSynchronization = "TimingSynchronization",
};
/**
* Broad structural or support functions.
*/
export enum FacilityFunctionEnum {
    
    /** Provides mechanical support for accelerator operations. */
    Support = "Support",
    /** Supports alignment of accelerator components. */
    Alignment = "Alignment",
    /** Provides electrical power to accelerator components. */
    PowerSupply = "PowerSupply",
    /** Houses control electronics for accelerator components. */
    ControlRack = "ControlRack",
    /** Provides cooling for accelerator components. */
    Cooling = "Cooling",
    /** Provides diagnostic capabilities for accelerator components, such as monitoring or measurement. */
    Diagnostics = "Diagnostics",
    /** Provides detection capabilities for accelerator components, such as radiation or particle detection. */
    Detection = "Detection",
};
/**
* Broad virtual component functions or roles.
*/
export enum VirtualFunctionEnum {
    
    /** A section of the BeamLine used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector. */
    BeamLineSection = "BeamLineSection",
    /** A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device. */
    Mark = "Mark",
    /** A virtual component representing a branching point in the beamline,  such as a beamline fork or switchyard. */
    Fork = "Fork",
    /** A virtual component representing a control system function or role that is important for understanding the overall accelerator system  but doesn't have a direct relationship to the beamline structure,  such as the EPICS control system that manages device process variables across the accelerator. */
    Control = "Control",
};
/**
* Controlled values for transverse plane.
*/
export enum PlaneEnum {
    
    /** Horizontal transverse plane. */
    Horizontal = "Horizontal",
    /** Vertical transverse plane. */
    Vertical = "Vertical",
};
/**
* Roles for control-system signals.
*/
export enum SignalRoleEnum {
    
    /** Requested or configured value. */
    Setpoint = "Setpoint",
    /** Measured or reported value. */
    Readback = "Readback",
    /** State or condition indicator. */
    Status = "Status",
    /** Command or action trigger. */
    Command = "Command",
    /** Minimum allowed signal value. */
    MinimumLimit = "MinimumLimit",
    /** Maximum allowed signal value. */
    MaximumLimit = "MaximumLimit",
};
/**
* Portable semantic meanings for important signals.
*/
export enum CanonicalSignalTypeEnum {
    
    /** Horizontal beam position signal. */
    HorizontalBeamPosition = "HorizontalBeamPosition",
    /** Vertical beam position signal. */
    VerticalBeamPosition = "VerticalBeamPosition",
    /** Horizontal beam position offset signal. */
    HorizontalBeamPositionOffset = "HorizontalBeamPositionOffset",
    /** Vertical beam position offset signal. */
    VerticalBeamPositionOffset = "VerticalBeamPositionOffset",
    /** Beam intensity or current signal. */
    BeamIntensity = "BeamIntensity",
    /** Device status signal. */
    DeviceStatus = "DeviceStatus",
    /** Cavity accelerating gradient setpoint signal. */
    GradientSetpoint = "GradientSetpoint",
    /** Cavity accelerating gradient readback signal. */
    GradientReadback = "GradientReadback",
    /** Magnet current setpoint signal. */
    MagnetCurrentSetpoint = "MagnetCurrentSetpoint",
    /** Magnet current readback signal. */
    MagnetCurrentReadback = "MagnetCurrentReadback",
    /** Magnet field setpoint signal. */
    MagnetFieldSetpoint = "MagnetFieldSetpoint",
    /** Integrated magnetic field setpoint signal. */
    IntegratedFieldSetpoint = "IntegratedFieldSetpoint",
    /** Integrated magnetic field readback signal. */
    IntegratedFieldReadback = "IntegratedFieldReadback",
    /** Vacuum pressure signal. */
    VacuumPressure = "VacuumPressure",
    /** Ion pump current signal. */
    IonPumpCurrent = "IonPumpCurrent",
    /** Ion pump voltage signal. */
    IonPumpVoltage = "IonPumpVoltage",
    /** Gamma radiation dose-rate signal. */
    GammaDoseRate = "GammaDoseRate",
    /** Neutron radiation dose-rate signal. */
    NeutronDoseRate = "NeutronDoseRate",
    /** Generic status signal for a device. */
    Status = "Status",
};
/**
* Physical quantity kinds for signals.
*/
export enum QuantityKindEnum {
    
    /** Beam transverse position. */
    BeamPosition = "BeamPosition",
    /** Device state or condition. */
    State = "State",
    /** Electric current. */
    ElectricCurrent = "ElectricCurrent",
    /** Integrated magnetic field. */
    IntegratedMagneticField = "IntegratedMagneticField",
    /** Magnetic field. */
    MagneticField = "MagneticField",
    /** Gas or vacuum pressure. */
    Pressure = "Pressure",
    /** Radiation dose rate. */
    DoseRate = "DoseRate",
    /** Electric potential difference. */
    Voltage = "Voltage",
    /** Power. */
    Power = "Power",
    /** Cavity phase. */
    CavityPhase = "CavityPhase",
    /** Cavity accelerating gradient. */
    CavityGradient = "CavityGradient",
};
/**
* Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available.
*/
export enum UnitEnum {
    
    /** ampere */
    A = "A",
    /** degree */
    degree = "degree",
    /** electron volt */
    eV = "eV",
    /** momentum in electron volts per speed of light */
    eV_per_c = "eV_per_c",
    /** mass in electron volts per speed of light squared */
    eV_per_c2 = "eV_per_c2",
    /** fundamental charge */
    fundamental_charge = "fundamental_charge",
    /** gauss per centimeter */
    G_per_cm = "G_per_cm",
    /** hertz */
    Hz = "Hz",
    /** kilowatt */
    kW = "kW",
    /** meter */
    m = "m",
    /** millimeter */
    mm = "mm",
    /** millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary. */
    mrem_per_h = "mrem_per_h",
    /** megavolt per meter */
    MV_per_m = "MV_per_m",
    /** pascal */
    PA = "PA",
    /** radians divided by 2 pi - angles and phases */
    randians_pi2 = "randians_pi2",
    /** rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary. */
    rem_per_h = "rem_per_h",
    /** second */
    seconds = "seconds",
    /** tesla */
    T = "T",
    /** tesla meter */
    T_M = "T_M",
    /** torr */
    Torr = "Torr",
    /** volt */
    V = "V",
    /** volt per meter */
    V_per_m = "V_per_m",
    /** dimensionless numeric value */
    unitless = "unitless",
    /** no unit or not applicable */
    none = "none",
};
/**
* Data types for parameter values.
*/
export enum DataTypeEnum {
    
    /** string data type */
    String = "String",
    /** integer data type */
    Integer = "Integer",
    /** floating-point data type */
    Float = "Float",
    /** boolean data type */
    Boolean = "Boolean",
};

export enum ComponentRelationPredicateEnum {
    
    /** Subject occurs immediately before object in the sequence/beamline order. */
    precedes = "precedes",
    /** Subject occurs after object in the sequence/beamline order. */
    follows = "follows",
    /** Subject spatially or mereologically contains object. */
    contains = "contains",
    /** Subject is spatially or mereologically contained in object. */
    contained_in = "contained_in",
    /** Subject and object are physically connected. a is connected to b if and only if a and b are discrete structure,  and there exists some connecting structure c, such that c connects a and b */
    connected_to = "connected_to",
    /** Subject controls the state or behavior of object. */
    controls = "controls",
    /** Subject is controlled by object. */
    is_controlled_by = "is_controlled_by",
    /** Subject is a part of object. */
    is_part_of = "is_part_of",
    /** Subject has part object. */
    has_part = "has_part",
    /** Subject and object are spatially adjacent, without overlapping. */
    adjacent_to = "adjacent_to",
    /** Subject and object share at least one part in common. */
    overlaps = "overlaps",
    /** Subject is mounted on object. */
    mounted_on = "mounted_on",
    /** Subject intersects with object. */
    intersects = "intersects",
    /** Subject is nearest to object. */
    nearest_to = "nearest_to",
};
/**
* Controlled predicates for Component-to-Signal bindings.
*/
export enum SignalBindingPredicateEnum {
    
    /** Generic association between a component and one of its signals. The specific role (setpoint, readback, status, etc.) is carried by the Signal's own signal_role field, not the predicate. */
    has_signal = "has_signal",
    /** Subject has the given signal as its status indicator. */
    has_status_signal = "has_status_signal",
    /** Subject has the given signal as its setpoint. */
    has_setpoint_signal = "has_setpoint_signal",
    /** Subject has the given signal as its readback. */
    has_readback_signal = "has_readback_signal",
    /** Subject has the given signal as a command trigger. */
    has_command_signal = "has_command_signal",
    /** Subject has the given signal as a limit/constraint value. */
    has_limit_signal = "has_limit_signal",
};

export enum RelationContextEnum {
    
    beamline_order = "beamline_order",
    Euclidean_3D = "Euclidean_3D",
    Euclidean_2D = "Euclidean_2D",
    floorplan = "floorplan",
    containment = "containment",
    installation_mounting = "installation_mounting",
};

export enum ReferenceFrameEnum {
    
    beam_direction = "beam_direction",
    facility_coordinates = "facility_coordinates",
    local_component_frame = "local_component_frame",
    tunnel_stationing = "tunnel_stationing",
};

export enum AxisEnum {
    
    x = "x",
    y = "y",
    z = "z",
    s = "s",
};

export enum DirectionEnum {
    
    upstream = "upstream",
    downstream = "downstream",
    positive = "positive",
    negative = "negative",
};
/**
* The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles.
*/
export enum MultipoleGeometryEnum {
    
    /** Use geometry equivalent to the setting of `ref_geometry`. */
    follows_ref_geometry = "follows_ref_geometry",
    /** Vertically pure multipoles with arc geometry. */
    vertically_pure = "vertically_pure",
    /** Horizontally pure multipoles with arc geometry. */
    horizontally_pure = "horizontally_pure",
    /** Z-axis is the chord connecting the entrance origin point to the exit origin point. */
    chord = "chord",
    /** Rectangular coordinates commensurate with the entrance coordinates. */
    entrance_coords = "entrance_coords",
    /** Rectangular coordinates commensurate with the exit coordinates. */
    exit_coords = "exit_coords",
};
/**
* The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles.
*/
export enum ReferenceGeometryEnum {
    
    /** Default. Reference are the curvelinear arc coordinates. */
    arc = "arc",
    /** Z-axis is the chord connecting the entrance origin point to the exit origin point. */
    chord = "chord",
    /** Rectangular coordinates commensurate with the entrance coordinates. */
    entrance_coords = "entrance_coords",
    /** Rectangular coordinates commensurate with the exit coordinates. */
    exit_coords = "exit_coords",
};
/**
* The type of cavity, which determines the field configuration and mode structure.
*/
export enum CavityTypeEnum {
    
    /** Default. A cavity that supports standing wave modes, typically with fixed geometry and resonant frequencies. */
    STANDING_WAVE = "STANDING_WAVE",
    /** A cavity that supports traveling wave modes, typically with a waveguide structure and phase velocity matching the beam. */
    TRAVELING_WAVE = "TRAVELING_WAVE",
};
/**
* The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity.
*/
export enum ZeroPhaseEnum {
    
    /** Default. The zero phase is the maximum accelerating phase, where the beam gains energy. */
    ACCELERATING = "ACCELERATING",
    /** Zero phase is at the stable zero crossing for particles below transition. */
    BELOW_TRANSITION = "BELOW_TRANSITION",
    /** Zero phase is at the stable zero crossing for particles above transition.. */
    ABOVE_TRANSITION = "ABOVE_TRANSITION",
};


/**
 * Root container for accelerator core components, semantic signals, and local bindings.
 */
export interface PALSAccelerator {
    /** The LinkML class name of this instance. */
    kind: string,
    /** A human-readable description of the instance. */
    description?: string,
    /** The affiliation of the author or component, as a ROR. */
    affiliation?: Affiliation,
    /** Version of the representation of a particle accelerator and its operations. */
    version?: string,
    /** Contains the authorship information for this representation of an accelerator facility and its operations. */
    authors?: Author[],
    /** Additional notes or comments about the representation of a particle accelerator and its operations. */
    notes?: string[],
    /** A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc. */
    facility?: Facility,
}


/**
 * Contains authorship information for a representation of an accelerator facility and its operations.
 */
export interface Author {
    /** The name of the entity. For example, the name of the person or organization. */
    name?: string,
    /** The affiliation of the author or component, as a ROR. */
    affiliation?: Affiliation,
    /** The email address of the author. */
    email?: string,
    /** The ORCID identifier of the author. */
    orcid?: string,
}


/**
 * A facility that houses one or more accelerators.
 */
export interface Facility {
    /** A unique and ideally persistent identifier for the facility, such as a DOI or ROR. */
    identifiers?: Identifier[],
    /** A list of physical components in the accelerator system. */
    components?: Component[],
    /** A list of beamlines in the accelerator system. */
    beamlines?: BeamLine[],
    /** A list of signals in the accelerator system. */
    signals?: Signal[],
    /** A list of signal bindings in the accelerator system (Component <-> Signal relationships). */
    signal_bindings?: SignalBinding[],
    /** A list of component relations in the accelerator system (Component <-> Component relationships). */
    component_relations?: ComponentRelation[],
}


/**
 * Contains affiliation information for an author or component, such as a ROR.
 */
export interface Affiliation {
    /** A unique identifier for the instance. */
    id: string,
    /** The name of the entity. For example, the name of the person or organization. */
    name?: string,
    /** A unique and ideally persistent identifier for the facility, such as a DOI or ROR. */
    identifiers?: Identifier[],
}


/**
 * A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.
 */
export interface Identifier {
    /** The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK. */
    identifier_type?: string,
    /** The value of the identifier. */
    identifier_value?: string,
}



export interface HasMetaP {
    /** A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    MetaP?: MetaParamGroup,
}


/**
 * Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 */
export interface MetaParamGroup {
    /** A human-readable description of the instance. */
    description?: string,
    /** An alternative name or identifier for the instance. */
    alias?: string,
    /** A label string. */
    label?: string,
    /** Additional metadata or annotations for the instance. */
    additional_metadata?: AdditionalMetadata[],
}



export interface HasFloorP {
    /** A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    FloorP?: FloorParamGroup,
}


/**
 * Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 */
export interface FloorParamGroup {
    /** Global X coordinate in the facility floor plan. */
    x?: number,
    /** Global Y coordinate in the facility floor plan. */
    y?: number,
    /** Global Z coordinate in the facility floor plan. */
    z?: number,
    /** Orientation angle around the Y-axis in the facility floor plan. */
    theta?: number,
    /** Rotation around the X-axis in the facility floor plan. */
    phi?: number,
    /** Rotation around the Z-axis in the facility floor plan. */
    psi?: number,
}



export interface HasBodyShiftP {
    /** A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    BodyShiftP?: BodyShiftParamGroup,
}


/**
 * Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 */
export interface BodyShiftParamGroup {
    /** Shift in the X direction in the facility floor plan. */
    x_offset?: number,
    /** Shift in the Y direction in the facility floor plan. */
    y_offset?: number,
    /** Shift in the Z direction in the facility floor plan. */
    z_offset?: number,
    /** Rotation around the X-axis in the facility floor plan. */
    x_rot?: number,
    /** Rotation around the Y-axis in the facility floor plan. */
    y_rot?: number,
    /** Rotation around the Z-axis in the facility floor plan. */
    z_rot?: number,
}



export interface HasLongitudinalPlacementP {
    /** A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    LongitudinalPlacementP?: LongitudinalPlacementParamGroup,
}


/**
 * Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. 
Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
One (or both) `length` or `s_position` must be present.
 */
export interface LongitudinalPlacementParamGroup {
    /** Length of the element (arc length for bends). */
    length?: number,
    /** Longitudinal position of the element along the beamline. */
    s_position?: number,
}



export interface HasReferenceP {
    /** A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    ReferenceP?: ReferenceParamGroup,
}


/**
 * Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 */
export interface ReferenceParamGroup {
    /** A reference to a species or particle type, such as an ion, electron, or proton. */
    species_ref?: string,
    /** [momentum*c] Reference momentum times speed of light. */
    pc_ref?: number,
    /** [eV] Reference total energy */
    E_tot_ref?: number,
    /** [s] Reference time */
    time_ref?: number,
}



export interface HasSolenoidP {
    /** A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    SolenoidP?: SolenoidParamGroup,
}


/**
 * Mixin for solenoid-specific parameters.
 */
export interface SolenoidParamGroup {
    /** Normalized solenoid strength. */
    Ksol?: number,
    /** Solenoid field. */
    Bsol?: number,
}



export interface HasTwissP {
    /** A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    TwissP?: TwissParamGroup,
}


/**
 * Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
 */
export interface TwissParamGroup {
    /** Twiss alpha parameter in the horizontal plane. */
    alpha_a?: number,
    /** Twiss alpha parameter in the vertical plane. */
    alpha_b?: number,
    /** Twiss beta parameter in the horizontal plane. */
    beta_a?: number,
    /** Twiss beta parameter in the vertical plane. */
    beta_b?: number,
    /** Twiss dispersion parameter in the horizontal plane. */
    eta_x?: number,
    /** Twiss dispersion parameter in the vertical plane. */
    eta_y?: number,
    /** Twiss dispersion slope parameter in the horizontal plane. */
    etap_x?: number,
    /** Twiss dispersion slope parameter in the vertical plane. */
    etap_y?: number,
    /** Twiss phase advance parameter in the horizontal plane. */
    phi_a?: number,
    /** Twiss phase advance parameter in the vertical plane. */
    phi_b?: number,
}



export interface HasRFP {
    /** A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    RFP?: RFParamGroup,
}


/**
 * Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
 */
export interface RFParamGroup {
    /** RF frequency. */
    frequency?: number,
    /** RF harmonic number. */
    harmon?: number,
    /** RF voltage. */
    voltage?: number,
    /** RF phase. rad/2pi RF phase in 0 to 2*pi */
    phase?: number,
    /** rad/2pi RF Phase added to multipass elements */
    multipass_phase?: number,
    /** Cavity type */
    cavity_type?: string,
    /** Number of cells in the cavity */
    num_cells?: number,
    /** Sets what phase = 0 means. */
    zero_phase?: string,
    /** Active acceleration length. */
    L_active?: number,
    /** Reference energy gain. */
    dE_ref?: number,
}



export interface HasElectricMultipoleP {
    /** A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    ElectricMultipoleP?: ElectricMultipoleParamGroup,
}


/**
 * Mixin for electric multipole parameters, 
which can be used to describe the electric field components of an accelerator element.
This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).
Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7
  tilt: 0.7
- order: 3
  En: 27.3
- order: 2
  EnL: 3.47e1
```
 */
export interface ElectricMultipoleParamGroup {
    /** Electric multipole components, one per order N. */
    elec_components?: MultipoleParameterGroup[],
}



export interface HasMagneticMultipoleP {
    /** A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    MagneticMultipoleP?: MagneticMultipoleParamGroup,
}


/**
 * Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7
  tilt: 0.7
- order: 3
  Bn: 27.3
- order: 2
  BnL: 3.47e1
- order: 1
  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength
```
 */
export interface MagneticMultipoleParamGroup {
    /** Magnetic multipole components, one per order N. */
    mag_components?: MultipoleParameterGroup[],
}



export interface HasBendP {
    /** A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). */
    BendP?: BendParamGroup,
}


/**
 * Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.
This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
 */
export interface BendParamGroup {
    /** Reference bend angle. */
    angle_ref?: number,
    /** Reference bend field. */
    bend_field_ref?: number,
    /** Actual bend field. */
    bend_field_actual?: number,
    /** Entrance end pole face rotation with respect to a sector geometry. */
    e1?: number,
    /** Exit end pole face rotation with respect to a sector geometry. */
    e2?: number,
    /** Entrance end pole face rotation with respect to a rectangular geometry. */
    e1_rect?: number,
    /** Exit end pole face rotation with respect to a rectangular geometry. */
    e2_rect?: number,
    /** Entrance end fringe field integral. */
    edge1_int?: number,
    /** Exit end fringe field integral. */
    edge2_int?: number,
    /** Reference bend strength = 1/radius_ref */
    g_ref?: number,
    /** Actual bend strength = 1/radius_actual */
    g_actual?: number,
    /** Entrance end pole face curvature */
    h1?: number,
    /** Exit end pole face curvature */
    h2?: number,
    /** Chord length of the bend. */
    L_chord?: number,
    /** Output parameter. Sagitta length. */
    L_sagitta?: number,
    /** Rectangular length. */
    L_rectangle?: number,
    /** Multipole geometry type. Must be `follows_ref_geometry`. */
    multipole_geometry?: string,
    /** Reference geometry type. Must be `arc`. */
    ref_geometry?: string,
    /** Reference bend radius. */
    rho_ref?: number,
    /** Reference tilt of the bend. */
    tilt_ref?: number,
}


/**
 * A single order's electric (or magnetic) multipole component.
Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.
Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
 */
export interface MultipoleParameterGroup {
    /** Multipole order N (0 = dipole, 1 = quadrupole, etc.) */
    order: number,
    /** Tilt of the Nth multipole. */
    tilt?: number,
    /** Normal component of the field. */
    En?: number,
    /** Skew component of the field. */
    Es?: number,
    /** Length-integrated normal component. */
    EnL?: number,
    /** Length-integrated skew component. */
    EsL?: number,
    /** Normal component of the magnetic field. */
    Bn?: number,
    /** Skew component of the magnetic field. */
    Bs?: number,
    /** Normalized normal component. */
    Kn?: number,
    /** Normalized skew component. */
    Ks?: number,
}


/**
 * A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
 */
export interface Component extends HasMetaP {
    /** A unique identifier for the instance. */
    id: string,
    /** The LinkML class name of this instance. */
    kind: string,
    /** The native type of the component in the source system, which can be used to identify the component across different source systems. */
    native_types?: string[],
}


/**
 * A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 */
export interface PhysicalComponent extends Component, HasFloorP, HasLongitudinalPlacementP {
    /** The function of the physical component,  which can be used to identify the component across different source systems. */
    functions: string,
    /** The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems. */
    beamline_relation: string,
}


/**
 * A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
 */
export interface VirtualComponent extends Component, HasFloorP {
    /** The function of the virtual component,  which can be used to identify the component across different source systems. */
    functions: string,
    /** The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems. */
    beamline_relation: string,
}


/**
 * PALS element for an ordered sequence of beamline elements defining a beam path.
 */
export interface BeamLine extends VirtualComponent {
    /** The total length of the BeamLine. For pals interoperability, use m as the unit of length. */
    length?: number,
    /** A human-readable description of the instance. */
    description?: string,
    /** Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass. */
    multipass?: boolean,
    /** Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic. */
    periodic?: boolean,
    /** Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
If value is greater than 1, the beamline is repeated that many times. */
    repeat?: number,
    /** Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1. */
    direction?: number,
}


/**
 * Semantic meaning of a control-system signal associated with a component.
 */
export interface Signal extends HasMetaP {
    /** A unique identifier for the instance. */
    id: string,
    /** The LinkML class name of this instance. */
    kind: string,
    /** An alternative name or identifier for the instance. */
    alias?: string,
    /** The role of the signal in the control system, such as setpoint, readback, status, command, or limit. */
    signal_role: string,
    /** The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service. */
    source_system: string,
    /** A human-readable description of the signal in the source system. */
    native_description?: string,
    /** The canonical semantic meaning of the signal. */
    canonical_signal_type: string,
    /** The physical quantity kind of the signal. */
    quantity_kind: string,
    /** The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean. */
    native_data_type: string,
    /** The native unit of the signal in the source system. */
    native_unit: string,
    /** The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service. */
    access_protocol?: string,
    /** The identifier used to reference the signal in an archival system. */
    archive_identifier?: string,
}


/**
 * An accelerator device that produces a magnetic field for beam control.
 */
export interface Magnet extends PhysicalComponent, HasReferenceP, HasBodyShiftP, HasTwissP {
}


/**
 * A magnet with a primarily longitudinal magnetic field used for focusing.
A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. 
 */
export interface Solenoid extends Magnet, HasSolenoidP {
}


/**
 * A general magnet with a higher-order multipole field, such as a sextupole or octupole.
Only one of the electric or magnetic multipole components should be present, not both.
 */
export interface Multipole extends Magnet, HasElectricMultipoleP, HasMagneticMultipoleP {
}


/**
 * Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
 */
export interface Bend extends Multipole, HasBendP {
}


/**
 * A magnet primarily used to focus or defocus the beam. 4 poles.
Only one of the electric or magnetic multipole components should be present, not both.
 */
export interface Quadrupole extends Multipole {
}


/**
 * A magnet primarily used to focus or defocus the beam. 8 poles.
Only one of the electric or magnetic multipole components should be present, not both.
 */
export interface Octupole extends Multipole {
}


/**
 * A magnet primarily used to focus or defocus the beam. 6 poles.
Only one of the electric or magnetic multipole components should be present, not both.
 */
export interface Sextupole extends Multipole {
}


/**
 * A magnet primarily used to steer the beam.
Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. 
Only one of the electric or magnetic multipole components should be present, not both.
 */
export interface Kicker extends Magnet, HasElectricMultipoleP, HasMagneticMultipoleP {
    /** The transverse plane in which the kicker operates, either horizontal or vertical. */
    plane?: string,
}


/**
 * An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.
 */
export interface ACKicker extends Kicker {
}


/**
 * An accelerator device used to measure beam or machine state.
 */
export interface DiagnosticDevice extends PhysicalComponent {
}


/**
 * A diagnostic device used to measure transverse beam profile.
 */
export interface BeamProfileMonitor extends DiagnosticDevice, HasReferenceP, HasBodyShiftP, HasTwissP {
}


/**
 * A diagnostic device used to measure transverse beam position.
 */
export interface BeamPositionMonitor extends DiagnosticDevice, HasReferenceP, HasBodyShiftP, HasTwissP {
}


/**
 * A diagnostic or limiting aperture element used to constrain or characterize beam passage.
 */
export interface Aperture extends DiagnosticDevice, HasReferenceP, HasTwissP {
}


/**
 * A diagnostic device used to monitor radiation dose or dose rate.
 */
export interface RadiationMonitor extends DiagnosticDevice, HasBodyShiftP {
}


/**
 * A cavity used for beam acceleration or manipulation.
 */
export interface Cavity extends PhysicalComponent, HasReferenceP, HasElectricMultipoleP, HasMagneticMultipoleP, HasBodyShiftP, HasTwissP {
}


/**
 * A cavity used for transverse beam manipulation, such as crabbing or deflecting.
 */
export interface CrabCavity extends Cavity {
}


/**
 * A cavity used for RF acceleration or longitudinal manipulation.
 */
export interface RFCavity extends Cavity, HasRFP {
}


/**
 * A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.
 */
export interface NormalConductingRFCavity extends RFCavity {
}


/**
 * A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
 */
export interface SuperConductingRFCavity extends RFCavity {
}


/**
 * A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.
 */
export interface SupportingFacilityComponent extends PhysicalComponent, HasFloorP, HasLongitudinalPlacementP, HasBodyShiftP {
    /** The function of the supporting facility component,  which can be used to identify the component across different source systems. */
    functions: string,
}


/**
 * A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.
 */
export interface BookkeepingComponent extends VirtualComponent, HasBodyShiftP {
}


/**
 * A virtual component used as a reference point or marker in the beamline structure.
 */
export interface Marker extends BookkeepingComponent, HasTwissP {
}


/**
 * A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components.
 */
export interface BeamLineSection extends BookkeepingComponent, HasFloorP {
}


/**
 * A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
 */
export interface AdditionalMetadata {
    /** The metadata field name. */
    key: string,
    /** The metadata value, serialized as a string. */
    value: string,
    /** Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string. */
    datatype?: string,
}


/**
 * Abstract base for subject-predicate-object associations.
 */
export interface Relationship {
    /** A unique identifier for the instance. */
    id: string,
    subject: string,
    predicate: string,
    object: string,
}


/**
 * Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.
 */
export interface SignalBinding extends Relationship {
}


/**
 * Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
 */
export interface ComponentRelation extends Relationship {
    /** The frame of reference / domain in which this relationship is asserted to hold. */
    context?: string,
    /** The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). */
    beamline_context?: BeamLineId,
    reference_frame?: string,
    distance_value?: number,
    distance_unit?: string,
    axis?: string,
    component_direction?: string,
    tolerance_value?: number,
    tolerance_unit?: string,
}



