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