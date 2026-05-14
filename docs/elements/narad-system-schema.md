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

Alignments with PALS (Particle Accelerator Language Standard):
  - Beamline aligns with pals:BeamLine
  - BeamlineElement aligns with pals:Element
  - Instrument aligns with pals:Instrument
  - Dipole aligns with pals:Multipole
  - Quadrupole aligns with pals:Quadrupole
  - Solenoid aligns with pals:Solenoid
  - RFCavity aligns with pals:RFCavity

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

Needed Custom Validations:
  - Validation to ensure that the element_kind of a BeamlineElement matches the device_type of the InstrumentSystem it is an instance of.
  - Validation to ensure that the value of is_property_of in InstanceSignalBinding matches one of the control systems listed in narad_config.has_sub_system.
  - Validation that each signal_layer -> facilities -> FacilitySystem -> control_system value has a corresponding entry in narad_config.has_sub_system to ensure that all control systems referenced in the signal layer are defined in the capability layer.
  - Validation that the signal_bindings defined for a given device_type in the signal layer align with the signals defined in the capability profiles and instrument systems for that device type.


URI: https://w3id.org/narad_linkml/schema/narad/system