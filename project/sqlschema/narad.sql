-- # Class: PALS Description: Root container for accelerator core components, semantic signals, and local bindings.
--     * Slot: id
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: description Description: A human-readable description of the instance.
--     * Slot: version Description: Version of the representation of a particle accelerator and its operations.
--     * Slot: affiliation_id Description: The affiliation of the author or component, as a ROR.
--     * Slot: facility_id Description: A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc.
-- # Class: Author Description: Contains authorship information for a representation of an accelerator facility and its operations.
--     * Slot: id
--     * Slot: name Description: The name of the entity. For example, the name of the person or organization.
--     * Slot: email Description: The email address of the author.
--     * Slot: orcid Description: The ORCID identifier of the author.
--     * Slot: PALS_id Description: Autocreated FK slot
--     * Slot: affiliation_id Description: The affiliation of the author or component, as a ROR.
-- # Class: Facility Description: A facility that houses one or more accelerators.
--     * Slot: id
-- # Class: Affiliation Description: Contains affiliation information for an author or component, such as a ROR.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: name Description: The name of the entity. For example, the name of the person or organization.
-- # Class: Identifier Description: A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.
--     * Slot: id
--     * Slot: identifier_type Description: The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK.
--     * Slot: identifier_value Description: The value of the identifier.
-- # Class: HasMetaP
--     * Slot: id
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: MetaParamGroup Description: Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: id
--     * Slot: description Description: A human-readable description of the instance.
--     * Slot: alias Description: An alternative name or identifier for the instance.
--     * Slot: label Description: A label string.
-- # Class: HasFloorP
--     * Slot: id
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: FloorParamGroup Description: Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: id
--     * Slot: x Description: Global X coordinate in the facility floor plan.
--     * Slot: y Description: Global Y coordinate in the facility floor plan.
--     * Slot: z Description: Global Z coordinate in the facility floor plan.
--     * Slot: theta Description: Orientation angle around the Y-axis in the facility floor plan.
--     * Slot: phi Description: Rotation around the X-axis in the facility floor plan.
--     * Slot: psi Description: Rotation around the Z-axis in the facility floor plan.
-- # Class: HasBodyShiftP
--     * Slot: id
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BodyShiftParamGroup Description: Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: id
--     * Slot: x_offset Description: Shift in the X direction in the facility floor plan.
--     * Slot: y_offset Description: Shift in the Y direction in the facility floor plan.
--     * Slot: z_offset Description: Shift in the Z direction in the facility floor plan.
--     * Slot: x_rot Description: Rotation around the X-axis in the facility floor plan.
--     * Slot: y_rot Description: Rotation around the Y-axis in the facility floor plan.
--     * Slot: z_rot Description: Rotation around the Z-axis in the facility floor plan.
-- # Class: HasLongitudinalPlacementP
--     * Slot: id
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: LongitudinalPlacementParamGroup Description: Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. Corresponds to PALS's ungrouped element parameters `length` and `s_position`.One (or both) `length` or `s_position` must be present.
--     * Slot: id
--     * Slot: length Description: Length of the element (arc length for bends).
--     * Slot: s_position Description: Longitudinal position of the element along the beamline.
-- # Class: HasReferenceP
--     * Slot: id
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: ReferenceParamGroup Description: Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: id
--     * Slot: species_ref Description: A reference to a species or particle type, such as an ion, electron, or proton.
--     * Slot: pc_ref Description: [momentum*c] Reference momentum times speed of light.
--     * Slot: E_tot_ref Description: [eV] Reference total energy
--     * Slot: time_ref Description: [s] Reference time
-- # Class: HasSolenoidP
--     * Slot: id
--     * Slot: SolenoidP_id Description: A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: SolenoidParamGroup Description: Mixin for solenoid-specific parameters.
--     * Slot: id
--     * Slot: Ksol Description: Normalized solenoid strength.
--     * Slot: Bsol Description: Solenoid field.
-- # Class: HasTwissP
--     * Slot: id
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: TwissParamGroup Description: Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
--     * Slot: id
--     * Slot: alpha_a Description: Twiss alpha parameter in the horizontal plane.
--     * Slot: alpha_b Description: Twiss alpha parameter in the vertical plane.
--     * Slot: beta_a Description: Twiss beta parameter in the horizontal plane.
--     * Slot: beta_b Description: Twiss beta parameter in the vertical plane.
--     * Slot: eta_x Description: Twiss dispersion parameter in the horizontal plane.
--     * Slot: eta_y Description: Twiss dispersion parameter in the vertical plane.
--     * Slot: etap_x Description: Twiss dispersion slope parameter in the horizontal plane.
--     * Slot: etap_y Description: Twiss dispersion slope parameter in the vertical plane.
--     * Slot: phi_a Description: Twiss phase advance parameter in the horizontal plane.
--     * Slot: phi_b Description: Twiss phase advance parameter in the vertical plane.
-- # Class: HasRFP
--     * Slot: id
--     * Slot: RFP_id Description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: RFParamGroup Description: Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: id
--     * Slot: frequency Description: RF frequency.
--     * Slot: harmon Description: RF harmonic number.
--     * Slot: voltage Description: RF voltage.
--     * Slot: phase Description: RF phase. rad/2pi RF phase in 0 to 2*pi
--     * Slot: multipass_phase Description: rad/2pi RF Phase added to multipass elements
--     * Slot: cavity_type Description: Cavity type
--     * Slot: num_cells Description: Number of cells in the cavity
--     * Slot: zero_phase Description: Sets what phase = 0 means.
--     * Slot: L_active Description: Active acceleration length.
--     * Slot: dE_ref Description: Reference energy gain.
-- # Class: HasElectricMultipoleP
--     * Slot: id
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: ElectricMultipoleParamGroup Description: Mixin for electric multipole parameters, which can be used to describe the electric field components of an accelerator element.This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7  tilt: 0.7- order: 3  En: 27.3- order: 2  EnL: 3.47e1```
--     * Slot: id
-- # Class: HasMagneticMultipoleP
--     * Slot: id
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: MagneticMultipoleParamGroup Description: Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7  tilt: 0.7- order: 3  Bn: 27.3- order: 2  BnL: 3.47e1- order: 1  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength```
--     * Slot: id
-- # Class: HasBendP
--     * Slot: id
--     * Slot: BendP_id Description: A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BendParamGroup Description: Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: id
--     * Slot: angle_ref Description: Reference bend angle.
--     * Slot: bend_field_ref Description: Reference bend field.
--     * Slot: bend_field_actual Description: Actual bend field.
--     * Slot: e1 Description: Entrance end pole face rotation with respect to a sector geometry.
--     * Slot: e2 Description: Exit end pole face rotation with respect to a sector geometry.
--     * Slot: e1_rect Description: Entrance end pole face rotation with respect to a rectangular geometry.
--     * Slot: e2_rect Description: Exit end pole face rotation with respect to a rectangular geometry.
--     * Slot: edge1_int Description: Entrance end fringe field integral.
--     * Slot: edge2_int Description: Exit end fringe field integral.
--     * Slot: g_ref Description: Reference bend strength = 1/radius_ref
--     * Slot: g_actual Description: Actual bend strength = 1/radius_actual
--     * Slot: h1 Description: Entrance end pole face curvature
--     * Slot: h2 Description: Exit end pole face curvature
--     * Slot: L_chord Description: Chord length of the bend.
--     * Slot: L_sagitta Description: Output parameter. Sagitta length.
--     * Slot: L_rectangle Description: Rectangular length.
--     * Slot: multipole_geometry Description: Multipole geometry type. Must be `follows_ref_geometry`.
--     * Slot: ref_geometry Description: Reference geometry type. Must be `arc`.
--     * Slot: rho_ref Description: Reference bend radius.
--     * Slot: tilt_ref Description: Reference tilt of the bend.
-- # Class: MultipoleParameterGroup Description: A single order's electric (or magnetic) multipole component.Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
--     * Slot: id
--     * Slot: order Description: Multipole order N (0 = dipole, 1 = quadrupole, etc.)
--     * Slot: tilt Description: Tilt of the Nth multipole.
--     * Slot: En Description: Normal component of the field.
--     * Slot: Es Description: Skew component of the field.
--     * Slot: EnL Description: Length-integrated normal component.
--     * Slot: EsL Description: Length-integrated skew component.
--     * Slot: Bn Description: Normal component of the magnetic field.
--     * Slot: Bs Description: Skew component of the magnetic field.
--     * Slot: Kn Description: Normalized normal component.
--     * Slot: Ks Description: Normalized skew component.
--     * Slot: ElectricMultipoleParamGroup_id Description: Autocreated FK slot
--     * Slot: MagneticMultipoleParamGroup_id Description: Autocreated FK slot
-- # Abstract Class: Component Description: A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: Facility_id Description: Autocreated FK slot
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: PhysicalComponent Description: A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: VirtualComponent Description: A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
--     * Slot: beamline_relation Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BeamLine Description: PALS element for an ordered sequence of beamline elements defining a beam path.
--     * Slot: length Description: The total length of the BeamLine. For pals interoperability, use m as the unit of length.
--     * Slot: description Description: A human-readable description of the instance.
--     * Slot: multipass Description: Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass.
--     * Slot: periodic Description: Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic.
--     * Slot: repeat Description: Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.If value is greater than 1, the beamline is repeated that many times.
--     * Slot: direction Description: Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1.
--     * Slot: beamline_relation Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: Facility_id Description: Autocreated FK slot
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Signal Description: Semantic meaning of a control-system signal associated with a component.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: alias Description: An alternative name or identifier for the instance.
--     * Slot: signal_role Description: The role of the signal in the control system, such as setpoint, readback, status, command, or limit.
--     * Slot: source_system Description: The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service.
--     * Slot: native_description Description: A human-readable description of the signal in the source system.
--     * Slot: canonical_signal_type Description: The canonical semantic meaning of the signal.
--     * Slot: quantity_kind Description: The physical quantity kind of the signal.
--     * Slot: native_data_type Description: The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean.
--     * Slot: native_unit Description: The native unit of the signal in the source system.
--     * Slot: access_protocol Description: The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
--     * Slot: archive_identifier Description: The identifier used to reference the signal in an archival system.
--     * Slot: Facility_id Description: Autocreated FK slot
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Abstract Class: Magnet Description: An accelerator device that produces a magnetic field for beam control.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Solenoid Description: A magnet with a primarily longitudinal magnetic field used for focusing.A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: SolenoidP_id Description: A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Multipole Description: A general magnet with a higher-order multipole field, such as a sextupole or octupole.Only one of the electric or magnetic multipole components should be present, not both.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Bend Description: Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: BendP_id Description: A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Quadrupole Description: A magnet primarily used to focus or defocus the beam. 4 poles.Only one of the electric or magnetic multipole components should be present, not both.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Octupole Description: A magnet primarily used to focus or defocus the beam. 8 poles.Only one of the electric or magnetic multipole components should be present, not both.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Sextupole Description: A magnet primarily used to focus or defocus the beam. 6 poles.Only one of the electric or magnetic multipole components should be present, not both.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Kicker Description: A magnet primarily used to steer the beam.Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. Only one of the electric or magnetic multipole components should be present, not both.
--     * Slot: plane Description: The transverse plane in which the kicker operates, either horizontal or vertical.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: ACKicker Description: An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.
--     * Slot: plane Description: The transverse plane in which the kicker operates, either horizontal or vertical.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: DiagnosticDevice Description: An accelerator device used to measure beam or machine state.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BeamProfileMonitor Description: A diagnostic device used to measure transverse beam profile.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BeamPositionMonitor Description: A diagnostic device used to measure transverse beam position.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: RadiationMonitor Description: A diagnostic device used to monitor radiation dose or dose rate.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Abstract Class: Cavity Description: A cavity used for beam acceleration or manipulation.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: CrabCavity Description: A cavity used for transverse beam manipulation, such as crabbing or deflecting.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Abstract Class: RFCavity Description: A cavity used for RF acceleration or longitudinal manipulation.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: RFP_id Description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: NormalConductingRFCavity Description: A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: RFP_id Description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: SuperConductingRFCavity Description: A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: RFP_id Description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ReferenceP_id Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: ElectricMultipoleP_id Description: A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MagneticMultipoleP_id Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: SupportingFacilityComponent Description: A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.
--     * Slot: beamline_relation Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: LongitudinalPlacementP_id Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BookkeepingComponent Description: A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.
--     * Slot: beamline_relation Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: Marker Description: A virtual component used as a reference point or marker in the beamline structure.
--     * Slot: beamline_relation Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: TwissP_id Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: BeamLineSection Description: A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components.
--     * Slot: beamline_relation Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: kind Description: The LinkML class name of this instance.
--     * Slot: FloorP_id Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: BodyShiftP_id Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
--     * Slot: MetaP_id Description: A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
-- # Class: AdditionalMetadata Description: A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
--     * Slot: key Description: The metadata field name.
--     * Slot: value Description: The metadata value, serialized as a string.
--     * Slot: datatype Description: Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string.
--     * Slot: MetaParamGroup_id Description: Autocreated FK slot
-- # Abstract Class: Relationship Description: Abstract base for subject-predicate-object associations.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: subject
--     * Slot: predicate
--     * Slot: object
-- # Class: SignalBinding Description: Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: subject
--     * Slot: predicate
--     * Slot: object
--     * Slot: Facility_id Description: Autocreated FK slot
-- # Class: ComponentRelation Description: Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
--     * Slot: context Description: The frame of reference / domain in which this relationship is asserted to hold.
--     * Slot: beamline_context Description: The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order).
--     * Slot: reference_frame
--     * Slot: distance_value
--     * Slot: distance_unit
--     * Slot: axis
--     * Slot: component_direction
--     * Slot: tolerance_value
--     * Slot: tolerance_unit
--     * Slot: id Description: A unique identifier for the instance.
--     * Slot: subject
--     * Slot: predicate
--     * Slot: object
--     * Slot: Facility_id Description: Autocreated FK slot
-- # Class: PALS_notes
--     * Slot: PALS_id Description: Autocreated FK slot
--     * Slot: notes Description: Additional notes or comments about the representation of a particle accelerator and its operations.
-- # Class: Facility_identifiers
--     * Slot: Facility_id Description: Autocreated FK slot
--     * Slot: identifiers_id Description: A unique and ideally persistent identifier for the facility, such as a DOI or ROR.
-- # Class: Affiliation_identifiers
--     * Slot: Affiliation_id Description: Autocreated FK slot
--     * Slot: identifiers_id Description: A unique and ideally persistent identifier for the facility, such as a DOI or ROR.
-- # Class: Component_native_types
--     * Slot: Component_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: PhysicalComponent_functions
--     * Slot: PhysicalComponent_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: PhysicalComponent_native_types
--     * Slot: PhysicalComponent_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: VirtualComponent_functions
--     * Slot: VirtualComponent_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the virtual component,  which can be used to identify the component across different source systems.
-- # Class: VirtualComponent_native_types
--     * Slot: VirtualComponent_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: BeamLine_functions
--     * Slot: BeamLine_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the virtual component,  which can be used to identify the component across different source systems.
-- # Class: BeamLine_native_types
--     * Slot: BeamLine_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Magnet_functions
--     * Slot: Magnet_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Magnet_native_types
--     * Slot: Magnet_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Solenoid_functions
--     * Slot: Solenoid_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Solenoid_native_types
--     * Slot: Solenoid_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Multipole_functions
--     * Slot: Multipole_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Multipole_native_types
--     * Slot: Multipole_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Bend_functions
--     * Slot: Bend_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Bend_native_types
--     * Slot: Bend_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Quadrupole_functions
--     * Slot: Quadrupole_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Quadrupole_native_types
--     * Slot: Quadrupole_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Octupole_functions
--     * Slot: Octupole_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Octupole_native_types
--     * Slot: Octupole_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Sextupole_functions
--     * Slot: Sextupole_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Sextupole_native_types
--     * Slot: Sextupole_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Kicker_functions
--     * Slot: Kicker_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Kicker_native_types
--     * Slot: Kicker_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: ACKicker_functions
--     * Slot: ACKicker_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: ACKicker_native_types
--     * Slot: ACKicker_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: DiagnosticDevice_functions
--     * Slot: DiagnosticDevice_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: DiagnosticDevice_native_types
--     * Slot: DiagnosticDevice_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: BeamProfileMonitor_functions
--     * Slot: BeamProfileMonitor_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: BeamProfileMonitor_native_types
--     * Slot: BeamProfileMonitor_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: BeamPositionMonitor_functions
--     * Slot: BeamPositionMonitor_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: BeamPositionMonitor_native_types
--     * Slot: BeamPositionMonitor_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: RadiationMonitor_functions
--     * Slot: RadiationMonitor_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: RadiationMonitor_native_types
--     * Slot: RadiationMonitor_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Cavity_functions
--     * Slot: Cavity_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: Cavity_native_types
--     * Slot: Cavity_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: CrabCavity_functions
--     * Slot: CrabCavity_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: CrabCavity_native_types
--     * Slot: CrabCavity_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: RFCavity_functions
--     * Slot: RFCavity_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: RFCavity_native_types
--     * Slot: RFCavity_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: NormalConductingRFCavity_functions
--     * Slot: NormalConductingRFCavity_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: NormalConductingRFCavity_native_types
--     * Slot: NormalConductingRFCavity_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: SuperConductingRFCavity_functions
--     * Slot: SuperConductingRFCavity_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the physical component,  which can be used to identify the component across different source systems.
-- # Class: SuperConductingRFCavity_native_types
--     * Slot: SuperConductingRFCavity_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: SupportingFacilityComponent_functions
--     * Slot: SupportingFacilityComponent_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the supporting facility component,  which can be used to identify the component across different source systems.
-- # Class: SupportingFacilityComponent_native_types
--     * Slot: SupportingFacilityComponent_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: BookkeepingComponent_functions
--     * Slot: BookkeepingComponent_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the virtual component,  which can be used to identify the component across different source systems.
-- # Class: BookkeepingComponent_native_types
--     * Slot: BookkeepingComponent_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: Marker_functions
--     * Slot: Marker_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the virtual component,  which can be used to identify the component across different source systems.
-- # Class: Marker_native_types
--     * Slot: Marker_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
-- # Class: BeamLineSection_functions
--     * Slot: BeamLineSection_id Description: Autocreated FK slot
--     * Slot: functions Description: The function of the virtual component,  which can be used to identify the component across different source systems.
-- # Class: BeamLineSection_native_types
--     * Slot: BeamLineSection_id Description: Autocreated FK slot
--     * Slot: native_types Description: The native type of the component in the source system, which can be used to identify the component across different source systems.

CREATE TABLE "Facility" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Facility_id" ON "Facility" (id);
CREATE TABLE "Affiliation" (
	id TEXT NOT NULL,
	name TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Affiliation_id" ON "Affiliation" (id);
CREATE TABLE "Identifier" (
	id INTEGER NOT NULL,
	identifier_type VARCHAR(5),
	identifier_value TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Identifier_id" ON "Identifier" (id);
CREATE TABLE "MetaParamGroup" (
	id INTEGER NOT NULL,
	description TEXT,
	alias TEXT,
	label TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MetaParamGroup_id" ON "MetaParamGroup" (id);
CREATE TABLE "FloorParamGroup" (
	id INTEGER NOT NULL,
	x FLOAT,
	y FLOAT,
	z FLOAT,
	theta FLOAT,
	phi FLOAT,
	psi FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FloorParamGroup_id" ON "FloorParamGroup" (id);
CREATE TABLE "BodyShiftParamGroup" (
	id INTEGER NOT NULL,
	x_offset FLOAT,
	y_offset FLOAT,
	z_offset FLOAT,
	x_rot FLOAT,
	y_rot FLOAT,
	z_rot FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_BodyShiftParamGroup_id" ON "BodyShiftParamGroup" (id);
CREATE TABLE "LongitudinalPlacementParamGroup" (
	id INTEGER NOT NULL,
	length FLOAT,
	s_position FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_LongitudinalPlacementParamGroup_id" ON "LongitudinalPlacementParamGroup" (id);
CREATE TABLE "ReferenceParamGroup" (
	id INTEGER NOT NULL,
	species_ref TEXT,
	pc_ref FLOAT,
	"E_tot_ref" FLOAT,
	time_ref FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ReferenceParamGroup_id" ON "ReferenceParamGroup" (id);
CREATE TABLE "SolenoidParamGroup" (
	id INTEGER NOT NULL,
	"Ksol" FLOAT,
	"Bsol" FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SolenoidParamGroup_id" ON "SolenoidParamGroup" (id);
CREATE TABLE "TwissParamGroup" (
	id INTEGER NOT NULL,
	alpha_a FLOAT,
	alpha_b FLOAT,
	beta_a FLOAT,
	beta_b FLOAT,
	eta_x FLOAT,
	eta_y FLOAT,
	etap_x FLOAT,
	etap_y FLOAT,
	phi_a FLOAT,
	phi_b FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TwissParamGroup_id" ON "TwissParamGroup" (id);
CREATE TABLE "RFParamGroup" (
	id INTEGER NOT NULL,
	frequency FLOAT,
	harmon INTEGER,
	voltage FLOAT,
	phase FLOAT,
	multipass_phase FLOAT,
	cavity_type VARCHAR(14),
	num_cells INTEGER,
	zero_phase VARCHAR(16),
	"L_active" FLOAT,
	"dE_ref" FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RFParamGroup_id" ON "RFParamGroup" (id);
CREATE TABLE "ElectricMultipoleParamGroup" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ElectricMultipoleParamGroup_id" ON "ElectricMultipoleParamGroup" (id);
CREATE TABLE "MagneticMultipoleParamGroup" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MagneticMultipoleParamGroup_id" ON "MagneticMultipoleParamGroup" (id);
CREATE TABLE "BendParamGroup" (
	id INTEGER NOT NULL,
	angle_ref FLOAT,
	bend_field_ref FLOAT,
	bend_field_actual FLOAT,
	e1 FLOAT,
	e2 FLOAT,
	e1_rect FLOAT,
	e2_rect FLOAT,
	edge1_int FLOAT,
	edge2_int FLOAT,
	g_ref FLOAT,
	g_actual FLOAT,
	h1 FLOAT,
	h2 FLOAT,
	"L_chord" FLOAT,
	"L_sagitta" FLOAT,
	"L_rectangle" FLOAT,
	multipole_geometry VARCHAR(20),
	ref_geometry VARCHAR(15),
	rho_ref FLOAT,
	tilt_ref FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_BendParamGroup_id" ON "BendParamGroup" (id);
CREATE TABLE "Relationship" (
	id TEXT NOT NULL,
	subject TEXT NOT NULL,
	predicate TEXT NOT NULL,
	object TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Relationship_id" ON "Relationship" (id);
CREATE TABLE "PALS" (
	id INTEGER NOT NULL,
	kind TEXT NOT NULL,
	description TEXT,
	version TEXT,
	affiliation_id TEXT,
	facility_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(affiliation_id) REFERENCES "Affiliation" (id),
	FOREIGN KEY(facility_id) REFERENCES "Facility" (id)
);CREATE INDEX "ix_PALS_id" ON "PALS" (id);
CREATE TABLE "HasMetaP" (
	id INTEGER NOT NULL,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_HasMetaP_id" ON "HasMetaP" (id);
CREATE TABLE "HasFloorP" (
	id INTEGER NOT NULL,
	"FloorP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id)
);CREATE INDEX "ix_HasFloorP_id" ON "HasFloorP" (id);
CREATE TABLE "HasBodyShiftP" (
	id INTEGER NOT NULL,
	"BodyShiftP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id)
);CREATE INDEX "ix_HasBodyShiftP_id" ON "HasBodyShiftP" (id);
CREATE TABLE "HasLongitudinalPlacementP" (
	id INTEGER NOT NULL,
	"LongitudinalPlacementP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id)
);CREATE INDEX "ix_HasLongitudinalPlacementP_id" ON "HasLongitudinalPlacementP" (id);
CREATE TABLE "HasReferenceP" (
	id INTEGER NOT NULL,
	"ReferenceP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id)
);CREATE INDEX "ix_HasReferenceP_id" ON "HasReferenceP" (id);
CREATE TABLE "HasSolenoidP" (
	id INTEGER NOT NULL,
	"SolenoidP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SolenoidP_id") REFERENCES "SolenoidParamGroup" (id)
);CREATE INDEX "ix_HasSolenoidP_id" ON "HasSolenoidP" (id);
CREATE TABLE "HasTwissP" (
	id INTEGER NOT NULL,
	"TwissP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id)
);CREATE INDEX "ix_HasTwissP_id" ON "HasTwissP" (id);
CREATE TABLE "HasRFP" (
	id INTEGER NOT NULL,
	"RFP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RFP_id") REFERENCES "RFParamGroup" (id)
);CREATE INDEX "ix_HasRFP_id" ON "HasRFP" (id);
CREATE TABLE "HasElectricMultipoleP" (
	id INTEGER NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id)
);CREATE INDEX "ix_HasElectricMultipoleP_id" ON "HasElectricMultipoleP" (id);
CREATE TABLE "HasMagneticMultipoleP" (
	id INTEGER NOT NULL,
	"MagneticMultipoleP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id)
);CREATE INDEX "ix_HasMagneticMultipoleP_id" ON "HasMagneticMultipoleP" (id);
CREATE TABLE "HasBendP" (
	id INTEGER NOT NULL,
	"BendP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BendP_id") REFERENCES "BendParamGroup" (id)
);CREATE INDEX "ix_HasBendP_id" ON "HasBendP" (id);
CREATE TABLE "MultipoleParameterGroup" (
	id INTEGER NOT NULL,
	"order" INTEGER NOT NULL,
	tilt FLOAT,
	"En" FLOAT,
	"Es" FLOAT,
	"EnL" FLOAT,
	"EsL" FLOAT,
	"Bn" FLOAT,
	"Bs" FLOAT,
	"Kn" FLOAT,
	"Ks" FLOAT,
	"ElectricMultipoleParamGroup_id" INTEGER,
	"MagneticMultipoleParamGroup_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleParamGroup_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleParamGroup_id") REFERENCES "MagneticMultipoleParamGroup" (id)
);CREATE INDEX "ix_MultipoleParameterGroup_id" ON "MultipoleParameterGroup" (id);
CREATE TABLE "Component" (
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"Facility_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Component_id" ON "Component" (id);
CREATE TABLE "PhysicalComponent" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_PhysicalComponent_id" ON "PhysicalComponent" (id);
CREATE TABLE "VirtualComponent" (
	beamline_relation VARCHAR(25) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"FloorP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_VirtualComponent_id" ON "VirtualComponent" (id);
CREATE TABLE "BeamLine" (
	length FLOAT,
	description TEXT,
	multipass BOOLEAN,
	periodic BOOLEAN,
	repeat INTEGER,
	direction INTEGER,
	beamline_relation VARCHAR(25) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"Facility_id" INTEGER,
	"FloorP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_BeamLine_id" ON "BeamLine" (id);
CREATE TABLE "Signal" (
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	alias TEXT,
	signal_role VARCHAR(12) NOT NULL,
	source_system VARCHAR(19) NOT NULL,
	native_description TEXT,
	canonical_signal_type VARCHAR(28) NOT NULL,
	quantity_kind VARCHAR(23) NOT NULL,
	native_data_type VARCHAR(7) NOT NULL,
	native_unit VARCHAR(18) NOT NULL,
	access_protocol TEXT,
	archive_identifier TEXT,
	"Facility_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Signal_id" ON "Signal" (id);
CREATE TABLE "Magnet" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Magnet_id" ON "Magnet" (id);
CREATE TABLE "Solenoid" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"SolenoidP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SolenoidP_id") REFERENCES "SolenoidParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Solenoid_id" ON "Solenoid" (id);
CREATE TABLE "Multipole" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Multipole_id" ON "Multipole" (id);
CREATE TABLE "Bend" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"BendP_id" INTEGER,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BendP_id") REFERENCES "BendParamGroup" (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Bend_id" ON "Bend" (id);
CREATE TABLE "Quadrupole" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Quadrupole_id" ON "Quadrupole" (id);
CREATE TABLE "Octupole" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Octupole_id" ON "Octupole" (id);
CREATE TABLE "Sextupole" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Sextupole_id" ON "Sextupole" (id);
CREATE TABLE "Kicker" (
	plane VARCHAR(10),
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Kicker_id" ON "Kicker" (id);
CREATE TABLE "ACKicker" (
	plane VARCHAR(10),
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_ACKicker_id" ON "ACKicker" (id);
CREATE TABLE "DiagnosticDevice" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_DiagnosticDevice_id" ON "DiagnosticDevice" (id);
CREATE TABLE "BeamProfileMonitor" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_BeamProfileMonitor_id" ON "BeamProfileMonitor" (id);
CREATE TABLE "BeamPositionMonitor" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ReferenceP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_BeamPositionMonitor_id" ON "BeamPositionMonitor" (id);
CREATE TABLE "RadiationMonitor" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"BodyShiftP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_RadiationMonitor_id" ON "RadiationMonitor" (id);
CREATE TABLE "Cavity" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ReferenceP_id" INTEGER,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Cavity_id" ON "Cavity" (id);
CREATE TABLE "CrabCavity" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"ReferenceP_id" INTEGER,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_CrabCavity_id" ON "CrabCavity" (id);
CREATE TABLE "RFCavity" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"RFP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RFP_id") REFERENCES "RFParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_RFCavity_id" ON "RFCavity" (id);
CREATE TABLE "NormalConductingRFCavity" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"RFP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RFP_id") REFERENCES "RFParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_NormalConductingRFCavity_id" ON "NormalConductingRFCavity" (id);
CREATE TABLE "SuperConductingRFCavity" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"RFP_id" INTEGER,
	"ReferenceP_id" INTEGER,
	"ElectricMultipoleP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"TwissP_id" INTEGER,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RFP_id") REFERENCES "RFParamGroup" (id),
	FOREIGN KEY("ReferenceP_id") REFERENCES "ReferenceParamGroup" (id),
	FOREIGN KEY("ElectricMultipoleP_id") REFERENCES "ElectricMultipoleParamGroup" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_SuperConductingRFCavity_id" ON "SuperConductingRFCavity" (id);
CREATE TABLE "SupportingFacilityComponent" (
	beamline_relation VARCHAR(18) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"FloorP_id" INTEGER,
	"LongitudinalPlacementP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("LongitudinalPlacementP_id") REFERENCES "LongitudinalPlacementParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_SupportingFacilityComponent_id" ON "SupportingFacilityComponent" (id);
CREATE TABLE "BookkeepingComponent" (
	beamline_relation VARCHAR(25) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"BodyShiftP_id" INTEGER,
	"FloorP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_BookkeepingComponent_id" ON "BookkeepingComponent" (id);
CREATE TABLE "Marker" (
	beamline_relation VARCHAR(25) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"TwissP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"FloorP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("TwissP_id") REFERENCES "TwissParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_Marker_id" ON "Marker" (id);
CREATE TABLE "BeamLineSection" (
	beamline_relation VARCHAR(25) NOT NULL,
	id TEXT NOT NULL,
	kind TEXT NOT NULL,
	"FloorP_id" INTEGER,
	"BodyShiftP_id" INTEGER,
	"MetaP_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FloorP_id") REFERENCES "FloorParamGroup" (id),
	FOREIGN KEY("BodyShiftP_id") REFERENCES "BodyShiftParamGroup" (id),
	FOREIGN KEY("MetaP_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_BeamLineSection_id" ON "BeamLineSection" (id);
CREATE TABLE "AdditionalMetadata" (
	"key" TEXT NOT NULL,
	value TEXT NOT NULL,
	datatype VARCHAR(7),
	"MetaParamGroup_id" INTEGER,
	PRIMARY KEY ("key"),
	FOREIGN KEY("MetaParamGroup_id") REFERENCES "MetaParamGroup" (id)
);CREATE INDEX "ix_AdditionalMetadata_key" ON "AdditionalMetadata" ("key");
CREATE TABLE "Facility_identifiers" (
	"Facility_id" INTEGER,
	identifiers_id INTEGER,
	PRIMARY KEY ("Facility_id", identifiers_id),
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id),
	FOREIGN KEY(identifiers_id) REFERENCES "Identifier" (id)
);CREATE INDEX "ix_Facility_identifiers_Facility_id" ON "Facility_identifiers" ("Facility_id");CREATE INDEX "ix_Facility_identifiers_identifiers_id" ON "Facility_identifiers" (identifiers_id);
CREATE TABLE "Affiliation_identifiers" (
	"Affiliation_id" TEXT,
	identifiers_id INTEGER,
	PRIMARY KEY ("Affiliation_id", identifiers_id),
	FOREIGN KEY("Affiliation_id") REFERENCES "Affiliation" (id),
	FOREIGN KEY(identifiers_id) REFERENCES "Identifier" (id)
);CREATE INDEX "ix_Affiliation_identifiers_Affiliation_id" ON "Affiliation_identifiers" ("Affiliation_id");CREATE INDEX "ix_Affiliation_identifiers_identifiers_id" ON "Affiliation_identifiers" (identifiers_id);
CREATE TABLE "Author" (
	id INTEGER NOT NULL,
	name TEXT,
	email TEXT,
	orcid TEXT,
	"PALS_id" INTEGER,
	affiliation_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PALS_id") REFERENCES "PALS" (id),
	FOREIGN KEY(affiliation_id) REFERENCES "Affiliation" (id)
);CREATE INDEX "ix_Author_id" ON "Author" (id);
CREATE TABLE "SignalBinding" (
	id TEXT NOT NULL,
	subject TEXT NOT NULL,
	predicate VARCHAR(19) NOT NULL,
	object TEXT NOT NULL,
	"Facility_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(subject) REFERENCES "PhysicalComponent" (id),
	FOREIGN KEY(object) REFERENCES "Signal" (id),
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id)
);CREATE INDEX "ix_SignalBinding_id" ON "SignalBinding" (id);
CREATE TABLE "ComponentRelation" (
	context VARCHAR(21),
	beamline_context TEXT,
	reference_frame VARCHAR(21),
	distance_value FLOAT,
	distance_unit VARCHAR(18),
	axis VARCHAR(1),
	component_direction VARCHAR(10),
	tolerance_value FLOAT,
	tolerance_unit VARCHAR(18),
	id TEXT NOT NULL,
	subject TEXT NOT NULL,
	predicate VARCHAR(16) NOT NULL,
	object TEXT NOT NULL,
	"Facility_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(beamline_context) REFERENCES "BeamLine" (id),
	FOREIGN KEY(subject) REFERENCES "Component" (id),
	FOREIGN KEY(object) REFERENCES "Component" (id),
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id)
);CREATE INDEX "ix_ComponentRelation_id" ON "ComponentRelation" (id);
CREATE TABLE "PALS_notes" (
	"PALS_id" INTEGER,
	notes TEXT,
	PRIMARY KEY ("PALS_id", notes),
	FOREIGN KEY("PALS_id") REFERENCES "PALS" (id)
);CREATE INDEX "ix_PALS_notes_PALS_id" ON "PALS_notes" ("PALS_id");CREATE INDEX "ix_PALS_notes_notes" ON "PALS_notes" (notes);
CREATE TABLE "Component_native_types" (
	"Component_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Component_id", native_types),
	FOREIGN KEY("Component_id") REFERENCES "Component" (id)
);CREATE INDEX "ix_Component_native_types_native_types" ON "Component_native_types" (native_types);CREATE INDEX "ix_Component_native_types_Component_id" ON "Component_native_types" ("Component_id");
CREATE TABLE "PhysicalComponent_functions" (
	"PhysicalComponent_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("PhysicalComponent_id", functions),
	FOREIGN KEY("PhysicalComponent_id") REFERENCES "PhysicalComponent" (id)
);CREATE INDEX "ix_PhysicalComponent_functions_functions" ON "PhysicalComponent_functions" (functions);CREATE INDEX "ix_PhysicalComponent_functions_PhysicalComponent_id" ON "PhysicalComponent_functions" ("PhysicalComponent_id");
CREATE TABLE "PhysicalComponent_native_types" (
	"PhysicalComponent_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("PhysicalComponent_id", native_types),
	FOREIGN KEY("PhysicalComponent_id") REFERENCES "PhysicalComponent" (id)
);CREATE INDEX "ix_PhysicalComponent_native_types_native_types" ON "PhysicalComponent_native_types" (native_types);CREATE INDEX "ix_PhysicalComponent_native_types_PhysicalComponent_id" ON "PhysicalComponent_native_types" ("PhysicalComponent_id");
CREATE TABLE "VirtualComponent_functions" (
	"VirtualComponent_id" TEXT,
	functions VARCHAR(15) NOT NULL,
	PRIMARY KEY ("VirtualComponent_id", functions),
	FOREIGN KEY("VirtualComponent_id") REFERENCES "VirtualComponent" (id)
);CREATE INDEX "ix_VirtualComponent_functions_VirtualComponent_id" ON "VirtualComponent_functions" ("VirtualComponent_id");CREATE INDEX "ix_VirtualComponent_functions_functions" ON "VirtualComponent_functions" (functions);
CREATE TABLE "VirtualComponent_native_types" (
	"VirtualComponent_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("VirtualComponent_id", native_types),
	FOREIGN KEY("VirtualComponent_id") REFERENCES "VirtualComponent" (id)
);CREATE INDEX "ix_VirtualComponent_native_types_VirtualComponent_id" ON "VirtualComponent_native_types" ("VirtualComponent_id");CREATE INDEX "ix_VirtualComponent_native_types_native_types" ON "VirtualComponent_native_types" (native_types);
CREATE TABLE "BeamLine_functions" (
	"BeamLine_id" TEXT,
	functions VARCHAR(15) NOT NULL,
	PRIMARY KEY ("BeamLine_id", functions),
	FOREIGN KEY("BeamLine_id") REFERENCES "BeamLine" (id)
);CREATE INDEX "ix_BeamLine_functions_BeamLine_id" ON "BeamLine_functions" ("BeamLine_id");CREATE INDEX "ix_BeamLine_functions_functions" ON "BeamLine_functions" (functions);
CREATE TABLE "BeamLine_native_types" (
	"BeamLine_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("BeamLine_id", native_types),
	FOREIGN KEY("BeamLine_id") REFERENCES "BeamLine" (id)
);CREATE INDEX "ix_BeamLine_native_types_native_types" ON "BeamLine_native_types" (native_types);CREATE INDEX "ix_BeamLine_native_types_BeamLine_id" ON "BeamLine_native_types" ("BeamLine_id");
CREATE TABLE "Magnet_functions" (
	"Magnet_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Magnet_id", functions),
	FOREIGN KEY("Magnet_id") REFERENCES "Magnet" (id)
);CREATE INDEX "ix_Magnet_functions_Magnet_id" ON "Magnet_functions" ("Magnet_id");CREATE INDEX "ix_Magnet_functions_functions" ON "Magnet_functions" (functions);
CREATE TABLE "Magnet_native_types" (
	"Magnet_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Magnet_id", native_types),
	FOREIGN KEY("Magnet_id") REFERENCES "Magnet" (id)
);CREATE INDEX "ix_Magnet_native_types_native_types" ON "Magnet_native_types" (native_types);CREATE INDEX "ix_Magnet_native_types_Magnet_id" ON "Magnet_native_types" ("Magnet_id");
CREATE TABLE "Solenoid_functions" (
	"Solenoid_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Solenoid_id", functions),
	FOREIGN KEY("Solenoid_id") REFERENCES "Solenoid" (id)
);CREATE INDEX "ix_Solenoid_functions_functions" ON "Solenoid_functions" (functions);CREATE INDEX "ix_Solenoid_functions_Solenoid_id" ON "Solenoid_functions" ("Solenoid_id");
CREATE TABLE "Solenoid_native_types" (
	"Solenoid_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Solenoid_id", native_types),
	FOREIGN KEY("Solenoid_id") REFERENCES "Solenoid" (id)
);CREATE INDEX "ix_Solenoid_native_types_native_types" ON "Solenoid_native_types" (native_types);CREATE INDEX "ix_Solenoid_native_types_Solenoid_id" ON "Solenoid_native_types" ("Solenoid_id");
CREATE TABLE "Multipole_functions" (
	"Multipole_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Multipole_id", functions),
	FOREIGN KEY("Multipole_id") REFERENCES "Multipole" (id)
);CREATE INDEX "ix_Multipole_functions_functions" ON "Multipole_functions" (functions);CREATE INDEX "ix_Multipole_functions_Multipole_id" ON "Multipole_functions" ("Multipole_id");
CREATE TABLE "Multipole_native_types" (
	"Multipole_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Multipole_id", native_types),
	FOREIGN KEY("Multipole_id") REFERENCES "Multipole" (id)
);CREATE INDEX "ix_Multipole_native_types_native_types" ON "Multipole_native_types" (native_types);CREATE INDEX "ix_Multipole_native_types_Multipole_id" ON "Multipole_native_types" ("Multipole_id");
CREATE TABLE "Bend_functions" (
	"Bend_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Bend_id", functions),
	FOREIGN KEY("Bend_id") REFERENCES "Bend" (id)
);CREATE INDEX "ix_Bend_functions_Bend_id" ON "Bend_functions" ("Bend_id");CREATE INDEX "ix_Bend_functions_functions" ON "Bend_functions" (functions);
CREATE TABLE "Bend_native_types" (
	"Bend_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Bend_id", native_types),
	FOREIGN KEY("Bend_id") REFERENCES "Bend" (id)
);CREATE INDEX "ix_Bend_native_types_native_types" ON "Bend_native_types" (native_types);CREATE INDEX "ix_Bend_native_types_Bend_id" ON "Bend_native_types" ("Bend_id");
CREATE TABLE "Quadrupole_functions" (
	"Quadrupole_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Quadrupole_id", functions),
	FOREIGN KEY("Quadrupole_id") REFERENCES "Quadrupole" (id)
);CREATE INDEX "ix_Quadrupole_functions_Quadrupole_id" ON "Quadrupole_functions" ("Quadrupole_id");CREATE INDEX "ix_Quadrupole_functions_functions" ON "Quadrupole_functions" (functions);
CREATE TABLE "Quadrupole_native_types" (
	"Quadrupole_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Quadrupole_id", native_types),
	FOREIGN KEY("Quadrupole_id") REFERENCES "Quadrupole" (id)
);CREATE INDEX "ix_Quadrupole_native_types_native_types" ON "Quadrupole_native_types" (native_types);CREATE INDEX "ix_Quadrupole_native_types_Quadrupole_id" ON "Quadrupole_native_types" ("Quadrupole_id");
CREATE TABLE "Octupole_functions" (
	"Octupole_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Octupole_id", functions),
	FOREIGN KEY("Octupole_id") REFERENCES "Octupole" (id)
);CREATE INDEX "ix_Octupole_functions_functions" ON "Octupole_functions" (functions);CREATE INDEX "ix_Octupole_functions_Octupole_id" ON "Octupole_functions" ("Octupole_id");
CREATE TABLE "Octupole_native_types" (
	"Octupole_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Octupole_id", native_types),
	FOREIGN KEY("Octupole_id") REFERENCES "Octupole" (id)
);CREATE INDEX "ix_Octupole_native_types_Octupole_id" ON "Octupole_native_types" ("Octupole_id");CREATE INDEX "ix_Octupole_native_types_native_types" ON "Octupole_native_types" (native_types);
CREATE TABLE "Sextupole_functions" (
	"Sextupole_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Sextupole_id", functions),
	FOREIGN KEY("Sextupole_id") REFERENCES "Sextupole" (id)
);CREATE INDEX "ix_Sextupole_functions_Sextupole_id" ON "Sextupole_functions" ("Sextupole_id");CREATE INDEX "ix_Sextupole_functions_functions" ON "Sextupole_functions" (functions);
CREATE TABLE "Sextupole_native_types" (
	"Sextupole_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Sextupole_id", native_types),
	FOREIGN KEY("Sextupole_id") REFERENCES "Sextupole" (id)
);CREATE INDEX "ix_Sextupole_native_types_native_types" ON "Sextupole_native_types" (native_types);CREATE INDEX "ix_Sextupole_native_types_Sextupole_id" ON "Sextupole_native_types" ("Sextupole_id");
CREATE TABLE "Kicker_functions" (
	"Kicker_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Kicker_id", functions),
	FOREIGN KEY("Kicker_id") REFERENCES "Kicker" (id)
);CREATE INDEX "ix_Kicker_functions_functions" ON "Kicker_functions" (functions);CREATE INDEX "ix_Kicker_functions_Kicker_id" ON "Kicker_functions" ("Kicker_id");
CREATE TABLE "Kicker_native_types" (
	"Kicker_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Kicker_id", native_types),
	FOREIGN KEY("Kicker_id") REFERENCES "Kicker" (id)
);CREATE INDEX "ix_Kicker_native_types_native_types" ON "Kicker_native_types" (native_types);CREATE INDEX "ix_Kicker_native_types_Kicker_id" ON "Kicker_native_types" ("Kicker_id");
CREATE TABLE "ACKicker_functions" (
	"ACKicker_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("ACKicker_id", functions),
	FOREIGN KEY("ACKicker_id") REFERENCES "ACKicker" (id)
);CREATE INDEX "ix_ACKicker_functions_functions" ON "ACKicker_functions" (functions);CREATE INDEX "ix_ACKicker_functions_ACKicker_id" ON "ACKicker_functions" ("ACKicker_id");
CREATE TABLE "ACKicker_native_types" (
	"ACKicker_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("ACKicker_id", native_types),
	FOREIGN KEY("ACKicker_id") REFERENCES "ACKicker" (id)
);CREATE INDEX "ix_ACKicker_native_types_native_types" ON "ACKicker_native_types" (native_types);CREATE INDEX "ix_ACKicker_native_types_ACKicker_id" ON "ACKicker_native_types" ("ACKicker_id");
CREATE TABLE "DiagnosticDevice_functions" (
	"DiagnosticDevice_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("DiagnosticDevice_id", functions),
	FOREIGN KEY("DiagnosticDevice_id") REFERENCES "DiagnosticDevice" (id)
);CREATE INDEX "ix_DiagnosticDevice_functions_DiagnosticDevice_id" ON "DiagnosticDevice_functions" ("DiagnosticDevice_id");CREATE INDEX "ix_DiagnosticDevice_functions_functions" ON "DiagnosticDevice_functions" (functions);
CREATE TABLE "DiagnosticDevice_native_types" (
	"DiagnosticDevice_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("DiagnosticDevice_id", native_types),
	FOREIGN KEY("DiagnosticDevice_id") REFERENCES "DiagnosticDevice" (id)
);CREATE INDEX "ix_DiagnosticDevice_native_types_DiagnosticDevice_id" ON "DiagnosticDevice_native_types" ("DiagnosticDevice_id");CREATE INDEX "ix_DiagnosticDevice_native_types_native_types" ON "DiagnosticDevice_native_types" (native_types);
CREATE TABLE "BeamProfileMonitor_functions" (
	"BeamProfileMonitor_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("BeamProfileMonitor_id", functions),
	FOREIGN KEY("BeamProfileMonitor_id") REFERENCES "BeamProfileMonitor" (id)
);CREATE INDEX "ix_BeamProfileMonitor_functions_BeamProfileMonitor_id" ON "BeamProfileMonitor_functions" ("BeamProfileMonitor_id");CREATE INDEX "ix_BeamProfileMonitor_functions_functions" ON "BeamProfileMonitor_functions" (functions);
CREATE TABLE "BeamProfileMonitor_native_types" (
	"BeamProfileMonitor_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("BeamProfileMonitor_id", native_types),
	FOREIGN KEY("BeamProfileMonitor_id") REFERENCES "BeamProfileMonitor" (id)
);CREATE INDEX "ix_BeamProfileMonitor_native_types_BeamProfileMonitor_id" ON "BeamProfileMonitor_native_types" ("BeamProfileMonitor_id");CREATE INDEX "ix_BeamProfileMonitor_native_types_native_types" ON "BeamProfileMonitor_native_types" (native_types);
CREATE TABLE "BeamPositionMonitor_functions" (
	"BeamPositionMonitor_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("BeamPositionMonitor_id", functions),
	FOREIGN KEY("BeamPositionMonitor_id") REFERENCES "BeamPositionMonitor" (id)
);CREATE INDEX "ix_BeamPositionMonitor_functions_functions" ON "BeamPositionMonitor_functions" (functions);CREATE INDEX "ix_BeamPositionMonitor_functions_BeamPositionMonitor_id" ON "BeamPositionMonitor_functions" ("BeamPositionMonitor_id");
CREATE TABLE "BeamPositionMonitor_native_types" (
	"BeamPositionMonitor_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("BeamPositionMonitor_id", native_types),
	FOREIGN KEY("BeamPositionMonitor_id") REFERENCES "BeamPositionMonitor" (id)
);CREATE INDEX "ix_BeamPositionMonitor_native_types_native_types" ON "BeamPositionMonitor_native_types" (native_types);CREATE INDEX "ix_BeamPositionMonitor_native_types_BeamPositionMonitor_id" ON "BeamPositionMonitor_native_types" ("BeamPositionMonitor_id");
CREATE TABLE "RadiationMonitor_functions" (
	"RadiationMonitor_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("RadiationMonitor_id", functions),
	FOREIGN KEY("RadiationMonitor_id") REFERENCES "RadiationMonitor" (id)
);CREATE INDEX "ix_RadiationMonitor_functions_RadiationMonitor_id" ON "RadiationMonitor_functions" ("RadiationMonitor_id");CREATE INDEX "ix_RadiationMonitor_functions_functions" ON "RadiationMonitor_functions" (functions);
CREATE TABLE "RadiationMonitor_native_types" (
	"RadiationMonitor_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("RadiationMonitor_id", native_types),
	FOREIGN KEY("RadiationMonitor_id") REFERENCES "RadiationMonitor" (id)
);CREATE INDEX "ix_RadiationMonitor_native_types_native_types" ON "RadiationMonitor_native_types" (native_types);CREATE INDEX "ix_RadiationMonitor_native_types_RadiationMonitor_id" ON "RadiationMonitor_native_types" ("RadiationMonitor_id");
CREATE TABLE "Cavity_functions" (
	"Cavity_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("Cavity_id", functions),
	FOREIGN KEY("Cavity_id") REFERENCES "Cavity" (id)
);CREATE INDEX "ix_Cavity_functions_Cavity_id" ON "Cavity_functions" ("Cavity_id");CREATE INDEX "ix_Cavity_functions_functions" ON "Cavity_functions" (functions);
CREATE TABLE "Cavity_native_types" (
	"Cavity_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Cavity_id", native_types),
	FOREIGN KEY("Cavity_id") REFERENCES "Cavity" (id)
);CREATE INDEX "ix_Cavity_native_types_Cavity_id" ON "Cavity_native_types" ("Cavity_id");CREATE INDEX "ix_Cavity_native_types_native_types" ON "Cavity_native_types" (native_types);
CREATE TABLE "CrabCavity_functions" (
	"CrabCavity_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("CrabCavity_id", functions),
	FOREIGN KEY("CrabCavity_id") REFERENCES "CrabCavity" (id)
);CREATE INDEX "ix_CrabCavity_functions_functions" ON "CrabCavity_functions" (functions);CREATE INDEX "ix_CrabCavity_functions_CrabCavity_id" ON "CrabCavity_functions" ("CrabCavity_id");
CREATE TABLE "CrabCavity_native_types" (
	"CrabCavity_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("CrabCavity_id", native_types),
	FOREIGN KEY("CrabCavity_id") REFERENCES "CrabCavity" (id)
);CREATE INDEX "ix_CrabCavity_native_types_native_types" ON "CrabCavity_native_types" (native_types);CREATE INDEX "ix_CrabCavity_native_types_CrabCavity_id" ON "CrabCavity_native_types" ("CrabCavity_id");
CREATE TABLE "RFCavity_functions" (
	"RFCavity_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("RFCavity_id", functions),
	FOREIGN KEY("RFCavity_id") REFERENCES "RFCavity" (id)
);CREATE INDEX "ix_RFCavity_functions_functions" ON "RFCavity_functions" (functions);CREATE INDEX "ix_RFCavity_functions_RFCavity_id" ON "RFCavity_functions" ("RFCavity_id");
CREATE TABLE "RFCavity_native_types" (
	"RFCavity_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("RFCavity_id", native_types),
	FOREIGN KEY("RFCavity_id") REFERENCES "RFCavity" (id)
);CREATE INDEX "ix_RFCavity_native_types_RFCavity_id" ON "RFCavity_native_types" ("RFCavity_id");CREATE INDEX "ix_RFCavity_native_types_native_types" ON "RFCavity_native_types" (native_types);
CREATE TABLE "NormalConductingRFCavity_functions" (
	"NormalConductingRFCavity_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("NormalConductingRFCavity_id", functions),
	FOREIGN KEY("NormalConductingRFCavity_id") REFERENCES "NormalConductingRFCavity" (id)
);CREATE INDEX "ix_NormalConductingRFCavity_functions_NormalConductingRFCavity_id" ON "NormalConductingRFCavity_functions" ("NormalConductingRFCavity_id");CREATE INDEX "ix_NormalConductingRFCavity_functions_functions" ON "NormalConductingRFCavity_functions" (functions);
CREATE TABLE "NormalConductingRFCavity_native_types" (
	"NormalConductingRFCavity_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("NormalConductingRFCavity_id", native_types),
	FOREIGN KEY("NormalConductingRFCavity_id") REFERENCES "NormalConductingRFCavity" (id)
);CREATE INDEX "ix_NormalConductingRFCavity_native_types_native_types" ON "NormalConductingRFCavity_native_types" (native_types);CREATE INDEX "ix_NormalConductingRFCavity_native_types_NormalConductingRFCavity_id" ON "NormalConductingRFCavity_native_types" ("NormalConductingRFCavity_id");
CREATE TABLE "SuperConductingRFCavity_functions" (
	"SuperConductingRFCavity_id" TEXT,
	functions VARCHAR(23) NOT NULL,
	PRIMARY KEY ("SuperConductingRFCavity_id", functions),
	FOREIGN KEY("SuperConductingRFCavity_id") REFERENCES "SuperConductingRFCavity" (id)
);CREATE INDEX "ix_SuperConductingRFCavity_functions_SuperConductingRFCavity_id" ON "SuperConductingRFCavity_functions" ("SuperConductingRFCavity_id");CREATE INDEX "ix_SuperConductingRFCavity_functions_functions" ON "SuperConductingRFCavity_functions" (functions);
CREATE TABLE "SuperConductingRFCavity_native_types" (
	"SuperConductingRFCavity_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("SuperConductingRFCavity_id", native_types),
	FOREIGN KEY("SuperConductingRFCavity_id") REFERENCES "SuperConductingRFCavity" (id)
);CREATE INDEX "ix_SuperConductingRFCavity_native_types_native_types" ON "SuperConductingRFCavity_native_types" (native_types);CREATE INDEX "ix_SuperConductingRFCavity_native_types_SuperConductingRFCavity_id" ON "SuperConductingRFCavity_native_types" ("SuperConductingRFCavity_id");
CREATE TABLE "SupportingFacilityComponent_functions" (
	"SupportingFacilityComponent_id" TEXT,
	functions VARCHAR(11) NOT NULL,
	PRIMARY KEY ("SupportingFacilityComponent_id", functions),
	FOREIGN KEY("SupportingFacilityComponent_id") REFERENCES "SupportingFacilityComponent" (id)
);CREATE INDEX "ix_SupportingFacilityComponent_functions_SupportingFacilityComponent_id" ON "SupportingFacilityComponent_functions" ("SupportingFacilityComponent_id");CREATE INDEX "ix_SupportingFacilityComponent_functions_functions" ON "SupportingFacilityComponent_functions" (functions);
CREATE TABLE "SupportingFacilityComponent_native_types" (
	"SupportingFacilityComponent_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("SupportingFacilityComponent_id", native_types),
	FOREIGN KEY("SupportingFacilityComponent_id") REFERENCES "SupportingFacilityComponent" (id)
);CREATE INDEX "ix_SupportingFacilityComponent_native_types_native_types" ON "SupportingFacilityComponent_native_types" (native_types);CREATE INDEX "ix_SupportingFacilityComponent_native_types_SupportingFacilityComponent_id" ON "SupportingFacilityComponent_native_types" ("SupportingFacilityComponent_id");
CREATE TABLE "BookkeepingComponent_functions" (
	"BookkeepingComponent_id" TEXT,
	functions VARCHAR(15) NOT NULL,
	PRIMARY KEY ("BookkeepingComponent_id", functions),
	FOREIGN KEY("BookkeepingComponent_id") REFERENCES "BookkeepingComponent" (id)
);CREATE INDEX "ix_BookkeepingComponent_functions_functions" ON "BookkeepingComponent_functions" (functions);CREATE INDEX "ix_BookkeepingComponent_functions_BookkeepingComponent_id" ON "BookkeepingComponent_functions" ("BookkeepingComponent_id");
CREATE TABLE "BookkeepingComponent_native_types" (
	"BookkeepingComponent_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("BookkeepingComponent_id", native_types),
	FOREIGN KEY("BookkeepingComponent_id") REFERENCES "BookkeepingComponent" (id)
);CREATE INDEX "ix_BookkeepingComponent_native_types_BookkeepingComponent_id" ON "BookkeepingComponent_native_types" ("BookkeepingComponent_id");CREATE INDEX "ix_BookkeepingComponent_native_types_native_types" ON "BookkeepingComponent_native_types" (native_types);
CREATE TABLE "Marker_functions" (
	"Marker_id" TEXT,
	functions VARCHAR(15) NOT NULL,
	PRIMARY KEY ("Marker_id", functions),
	FOREIGN KEY("Marker_id") REFERENCES "Marker" (id)
);CREATE INDEX "ix_Marker_functions_functions" ON "Marker_functions" (functions);CREATE INDEX "ix_Marker_functions_Marker_id" ON "Marker_functions" ("Marker_id");
CREATE TABLE "Marker_native_types" (
	"Marker_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("Marker_id", native_types),
	FOREIGN KEY("Marker_id") REFERENCES "Marker" (id)
);CREATE INDEX "ix_Marker_native_types_native_types" ON "Marker_native_types" (native_types);CREATE INDEX "ix_Marker_native_types_Marker_id" ON "Marker_native_types" ("Marker_id");
CREATE TABLE "BeamLineSection_functions" (
	"BeamLineSection_id" TEXT,
	functions VARCHAR(15) NOT NULL,
	PRIMARY KEY ("BeamLineSection_id", functions),
	FOREIGN KEY("BeamLineSection_id") REFERENCES "BeamLineSection" (id)
);CREATE INDEX "ix_BeamLineSection_functions_BeamLineSection_id" ON "BeamLineSection_functions" ("BeamLineSection_id");CREATE INDEX "ix_BeamLineSection_functions_functions" ON "BeamLineSection_functions" (functions);
CREATE TABLE "BeamLineSection_native_types" (
	"BeamLineSection_id" TEXT,
	native_types TEXT,
	PRIMARY KEY ("BeamLineSection_id", native_types),
	FOREIGN KEY("BeamLineSection_id") REFERENCES "BeamLineSection" (id)
);CREATE INDEX "ix_BeamLineSection_native_types_native_types" ON "BeamLineSection_native_types" (native_types);CREATE INDEX "ix_BeamLineSection_native_types_BeamLineSection_id" ON "BeamLineSection_native_types" ("BeamLineSection_id");
