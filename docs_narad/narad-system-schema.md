# narad-system-schema 

LinkML schema for representing NARAD control-system semantics, facility-level signal templates, and facility-specific instance bindings aligned with SSN, SSN-System, and SOSA ontologies.
Main modeling layers:
  - NaradModel — top-level document containing narad_config, beamlines, and elements
  - CapabilityLayer — reusable control-profile families, shared capabilities,
    and device-type profiles
  - SignalLayer — facility-specific signal suffix templates organized by
    device domain and device type
  - Beamline / BeamlineElement — ordered machine layout plus applied profiles
    and facility-specific instance bindings
  - Element instances — individual beamline elements with applied profiles and instance signal
    bindings

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

Capability hierarchy:
  - SystemCapability
    - MagnetCapability
      - QuadrupoleCapability, CorrectorCapability, DipoleCapability, SolenoidCapability
    - InstrumentCapability
      - BPMCapability
    - CavityGradientCapability

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
  - type_signal_sets is a single structured container with explicit
    per-domain and per-device signal-set slots

Additional Notes on Usage: 1. On Signal, SignalBinding, and InstanceSignalBinding: These classes represent different levels of abstraction in the signal modeling.  Signal defines the abstract control-system quantity (e.g. current_readback), SignalBinding captures the facility-specific naming convention for that signal (e.g. .R for EPICS readback),  and InstanceSignalBinding represents the concrete binding of that signal to a specific beamline element instance (e.g. MQWK202.R). The semantic signal name (e.g. current_readback) is the key that links these layers together, while the control-system suffix (e.g. .R) is captured in the SignalBinding. 2. On the distinction between element_kind, capability_profile, and facility_element_type.
  - element_kind (BeamlineElement.element_kind) is the high-level type of the beamline element, drawn from ElementKindEnum. This is used for sequencing and general classification of elements in the beamline.
  - capability_profile (BeamlineElement.capability_profile) is the specific control profile assigned to that element, which determines what capabilities and signals are relevant for it. This is a cross-reference to a CapabilityProfile defined in the capability layer.
  - facility_element_type (FacilityParamSet.facility_element_type) is an optional slot for recording the facility-specific type designation for this element, if it differs from the generic element_kind. For example, a facility might have its own naming convention for magnet types that doesn't align one-to-one with the ElementKindEnum values.
3. Expected CURIE usage for is_instance_of, is_hosted_by, and is_property_of: 
  - is_instance_of typically points to the rdf:type of the Procedure class that implements the signal binding, e.g. narad:narad:CavityGradientControlCapability.
  - is_hosted_by typically points to the FacilitySystem this binding belongs to, e.g. narad:[ExampleFacilitySystem] (such as UITF).
  - is_property_of typically points to the ControlSystem that implements this binding, e.g. narad:[ExampleControlSystem] (such as epics).
4. Open and constrained vocabularies:
  - ElementKindEnum and DeviceDomainEnum provide controlled vocabularies for key classification slots, but the schema is designed to be extensible with new enum values as needed.
  - The properties slot in FacilityParamSet allows for open-ended key-value pairs to capture any additional facility-specific parameters that don't fit into the predefined schema structure.


URI: https://w3id.org/narad_linkml/schema/narad/system