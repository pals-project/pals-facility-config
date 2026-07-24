# Accelerator Core Ontology

A lightweight LinkML schema for facility-agnostic accelerator components, their beamline relationships, and associated control-system signals.

URI: https://w3id.org/accelerator-core

Name: accelerator_core



## Classes

| Class | Description |
| --- | --- |
| [AdditionalMetadata](AdditionalMetadata.md) | A single generic key/value metadata entry, used as a GraphQL-compatible repla... |
| [Affiliation](Affiliation.md) | Contains affiliation information for an author or component, such as a ROR |
| [Author](Author.md) | Contains authorship information for a representation of an accelerator facili... |
| [BendParamGroup](BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properti... |
| [BodyShiftParamGroup](BodyShiftParamGroup.md) | Mixin class for floor plan shift parameters that are aligned with PALS BodySh... |
| [Component](Component.md) | A general class for accelerator components, which can be specialized into mor... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalComponent](PhysicalComponent.md) | A physical item that participates in or supports accelerator operation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiagnosticDevice](DiagnosticDevice.md) | An accelerator device used to measure beam or machine state |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamPositionMonitor](BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamProfileMonitor](BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RadiationMonitor](RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Magnet](Magnet.md) | An accelerator device that produces a magnetic field for beam control |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kicker](Kicker.md) | A magnet primarily used to steer the beam |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bend](Bend.md) | Dipole magnet used to bend the beam |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SupportingFacilityComponent](SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VirtualComponent](VirtualComponent.md) | A virtual or logical component that represents a concept, function, or role i... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BookkeepingComponent](BookkeepingComponent.md) | A virtual component that represents a bookkeeping or organizational role in t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamLineSection](BeamLineSection.md) | A virtual component used to represent a section of the BeamLine for organizat... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Marker](Marker.md) | A virtual component used as a reference point or marker in the beamline struc... |
| [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md) | Mixin for electric multipole parameters,  |
| [Facility](Facility.md) | A facility that houses one or more accelerators |
| [FloorParamGroup](FloorParamGroup.md) | Mixin class for floor plan parameters that are aligned with PALS FloorP (Floo... |
| [HasBendP](HasBendP.md) |  |
| [HasBodyShiftP](HasBodyShiftP.md) |  |
| [HasElectricMultipoleP](HasElectricMultipoleP.md) |  |
| [HasFloorP](HasFloorP.md) |  |
| [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md) |  |
| [HasMagneticMultipoleP](HasMagneticMultipoleP.md) |  |
| [HasMetaP](HasMetaP.md) |  |
| [HasReferenceP](HasReferenceP.md) |  |
| [HasRFP](HasRFP.md) |  |
| [HasSolenoidP](HasSolenoidP.md) |  |
| [HasTwissP](HasTwissP.md) |  |
| [Identifier](Identifier.md) | A unique, and ideally persistent, identifier for a facility, such as a DOI or... |
| [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direc... |
| [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md) | Mixin for magnetic multipole parameters,  which can be used to describe the m... |
| [MetaParamGroup](MetaParamGroup.md) | Mixin class for metadata parameters that are aligned with PALS MetaP (Metadat... |
| [MultipoleParameterGroup](MultipoleParameterGroup.md) | A single order's electric (or magnetic) multipole component |
| [PALS](PALS.md) | Root container for accelerator core components, semantic signals, and local b... |
| [ReferenceParamGroup](ReferenceParamGroup.md) | Mixin for reference parameters that are aligned with PALS ReferenceP (Referen... |
| [Relationship](Relationship.md) | Abstract base for subject-predicate-object associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComponentRelation](ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting con... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SignalBinding](SignalBinding.md) | Association between a PhysicalComponent and one of its Signals, e |
| [RFParamGroup](RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of a... |
| [Signal](Signal.md) | Semantic meaning of a control-system signal associated with a component |
| [SolenoidParamGroup](SolenoidParamGroup.md) | Mixin for solenoid-specific parameters |
| [TwissParamGroup](TwissParamGroup.md) | Mixin for Twiss parameters, which can be used to describe the beam optics of ... |



## Slots

| Slot | Description |
| --- | --- |
| [access_protocol](access_protocol.md) | The protocol used to access the signal in the source system,  such as EPICS C... |
| [additional_metadata](additional_metadata.md) | Additional metadata or annotations for the instance |
| [affiliation](affiliation.md) | The affiliation of the author or component, as a ROR |
| [alias](alias.md) | An alternative name or identifier for the instance |
| [alpha_a](alpha_a.md) | Twiss alpha parameter in the horizontal plane |
| [alpha_b](alpha_b.md) | Twiss alpha parameter in the vertical plane |
| [angle_ref](angle_ref.md) | Reference bend angle |
| [archive_identifier](archive_identifier.md) | The identifier used to reference the signal in an archival system |
| [authors](authors.md) | Contains the authorship information for this representation of an accelerator... |
| [axis](axis.md) |  |
| [beamline_context](beamline_context.md) | The specific BeamLine this relationship is defined with respect to (relevant ... |
| [beamline_relation](beamline_relation.md) | The relationship of the physical component to the beamline,  which can be use... |
| [beamlines](beamlines.md) | A list of beamlines in the accelerator system |
| [bend_field_actual](bend_field_actual.md) | Actual bend field |
| [bend_field_ref](bend_field_ref.md) | Reference bend field |
| [BendP](BendP.md) | A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters... |
| [beta_a](beta_a.md) | Twiss beta parameter in the horizontal plane |
| [beta_b](beta_b.md) | Twiss beta parameter in the vertical plane |
| [Bn](Bn.md) | Normal component of the magnetic field |
| [BodyShiftP](BodyShiftP.md) | A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP... |
| [Bs](Bs.md) | Skew component of the magnetic field |
| [Bsol](Bsol.md) | Solenoid field |
| [canonical_signal_type](canonical_signal_type.md) | The canonical semantic meaning of the signal |
| [cavity_type](cavity_type.md) | Cavity type |
| [component_direction](component_direction.md) |  |
| [component_relations](component_relations.md) | A list of component relations in the accelerator system (Component <-> Compon... |
| [components](components.md) | A list of physical components in the accelerator system |
| [context](context.md) | The frame of reference / domain in which this relationship is asserted to hol... |
| [datatype](datatype.md) | Hint for the value's original type, so consumers can parse it back (e |
| [dE_ref](dE_ref.md) | Reference energy gain |
| [description](description.md) | A human-readable description of the instance |
| [direction](direction.md) | Beam direction along the BeamLine: +1 or -1 |
| [distance_unit](distance_unit.md) |  |
| [distance_value](distance_value.md) |  |
| [e1](e1.md) | Entrance end pole face rotation with respect to a sector geometry |
| [e1_rect](e1_rect.md) | Entrance end pole face rotation with respect to a rectangular geometry |
| [e2](e2.md) | Exit end pole face rotation with respect to a sector geometry |
| [e2_rect](e2_rect.md) | Exit end pole face rotation with respect to a rectangular geometry |
| [E_tot_ref](E_tot_ref.md) | [eV] Reference total energy |
| [edge1_int](edge1_int.md) | Entrance end fringe field integral |
| [edge2_int](edge2_int.md) | Exit end fringe field integral |
| [elec_components](elec_components.md) | Electric multipole components, one per order N |
| [ElectricMultipoleP](ElectricMultipoleP.md) | A mixin for electric multipole parameters that are aligned with PALS Electric... |
| [email](email.md) | The email address of the author |
| [En](En.md) | Normal component of the field |
| [EnL](EnL.md) | Length-integrated normal component |
| [Es](Es.md) | Skew component of the field |
| [EsL](EsL.md) | Length-integrated skew component |
| [eta_x](eta_x.md) | Twiss dispersion parameter in the horizontal plane |
| [eta_y](eta_y.md) | Twiss dispersion parameter in the vertical plane |
| [etap_x](etap_x.md) | Twiss dispersion slope parameter in the horizontal plane |
| [etap_y](etap_y.md) | Twiss dispersion slope parameter in the vertical plane |
| [facility](facility.md) | A facility that contains lattice elements (physical and virtual), beamlines, ... |
| [FloorP](FloorP.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Pl... |
| [frequency](frequency.md) | RF frequency |
| [functions](functions.md) | The function of the physical component,  which can be used to identify the co... |
| [g_actual](g_actual.md) | Actual bend strength = 1/radius_actual |
| [g_ref](g_ref.md) | Reference bend strength = 1/radius_ref |
| [h1](h1.md) | Entrance end pole face curvature |
| [h2](h2.md) | Exit end pole face curvature |
| [harmon](harmon.md) | RF harmonic number |
| [id](id.md) | A unique identifier for the instance |
| [identifier_type](identifier_type.md) | The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK |
| [identifier_value](identifier_value.md) | The value of the identifier |
| [identifiers](identifiers.md) | A unique and ideally persistent identifier for the facility, such as a DOI or... |
| [key](key.md) | The metadata field name |
| [kind](kind.md) | The LinkML class name of this instance |
| [Kn](Kn.md) | Normalized normal component |
| [Ks](Ks.md) | Normalized skew component |
| [Ksol](Ksol.md) | Normalized solenoid strength |
| [L_active](L_active.md) | Active acceleration length |
| [L_chord](L_chord.md) | Chord length of the bend |
| [L_rectangle](L_rectangle.md) | Rectangular length |
| [L_sagitta](L_sagitta.md) | Output parameter |
| [label](label.md) | A label string |
| [length](length.md) | Length of the element (arc length for bends) |
| [LongitudinalPlacementP](LongitudinalPlacementP.md) | A mixin for an element's extent and position along the longitudinal (beam-dir... |
| [mag_components](mag_components.md) | Magnetic multipole components, one per order N |
| [MagneticMultipoleP](MagneticMultipoleP.md) | A mixin for magnetic multipole parameters that are aligned with PALS Magnetic... |
| [MetaP](MetaP.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Pa... |
| [multipass](multipass.md) | Indicates whether the BeamLine is a multipass BeamLine, where the beam passes... |
| [multipass_phase](multipass_phase.md) | rad/2pi RF Phase added to multipass elements |
| [multipole_geometry](multipole_geometry.md) | Multipole geometry type |
| [name](name.md) | The name of the entity |
| [native_data_type](native_data_type.md) | The native data type of the signal in the source system,  such as String, Int... |
| [native_description](native_description.md) | A human-readable description of the signal in the source system |
| [native_types](native_types.md) | The native type of the component in the source system, which can be used to i... |
| [native_unit](native_unit.md) | The native unit of the signal in the source system |
| [notes](notes.md) | Additional notes or comments about the representation of a particle accelerat... |
| [num_cells](num_cells.md) | Number of cells in the cavity |
| [object](object.md) |  |
| [orcid](orcid.md) | The ORCID identifier of the author |
| [order](order.md) | Multipole order N (0 = dipole, 1 = quadrupole, etc |
| [pc_ref](pc_ref.md) | [momentum*c] Reference momentum times speed of light |
| [periodic](periodic.md) | Indicates whether orbit and Twiss parameters periodic |
| [phase](phase.md) | RF phase |
| [phi](phi.md) | Rotation around the X-axis in the facility floor plan |
| [phi_a](phi_a.md) | Twiss phase advance parameter in the horizontal plane |
| [phi_b](phi_b.md) | Twiss phase advance parameter in the vertical plane |
| [plane](plane.md) | The transverse plane in which the kicker operates, either horizontal or verti... |
| [predicate](predicate.md) |  |
| [psi](psi.md) | Rotation around the Z-axis in the facility floor plan |
| [quantity_kind](quantity_kind.md) | The physical quantity kind of the signal |
| [ref_geometry](ref_geometry.md) | Reference geometry type |
| [reference_frame](reference_frame.md) |  |
| [ReferenceP](ReferenceP.md) | A mixin for reference parameters that are aligned with PALS ReferenceP (Refer... |
| [repeat](repeat.md) | Repetition count |
| [RFP](RFP.md) | A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for ... |
| [rho_ref](rho_ref.md) | Reference bend radius |
| [s_position](s_position.md) | Longitudinal position of the element along the beamline |
| [signal_bindings](signal_bindings.md) | A list of signal bindings in the accelerator system (Component <-> Signal rel... |
| [signal_role](signal_role.md) | The role of the signal in the control system, such as setpoint, readback, sta... |
| [signals](signals.md) | A list of signals in the accelerator system |
| [SolenoidP](SolenoidP.md) | A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP... |
| [source_system](source_system.md) | The source system from which the signal originates, such as EPICS, PALS-Ext, ... |
| [species_ref](species_ref.md) | A reference to a species or particle type, such as an ion, electron, or proto... |
| [subject](subject.md) |  |
| [theta](theta.md) | Orientation angle around the Y-axis in the facility floor plan |
| [tilt](tilt.md) | Tilt of the Nth multipole |
| [tilt_ref](tilt_ref.md) | Reference tilt of the bend |
| [time_ref](time_ref.md) | [s] Reference time |
| [tolerance_unit](tolerance_unit.md) |  |
| [tolerance_value](tolerance_value.md) |  |
| [TwissP](TwissP.md) | A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Paramet... |
| [value](value.md) | The metadata value, serialized as a string |
| [version](version.md) | Version of the representation of a particle accelerator and its operations |
| [voltage](voltage.md) | RF voltage |
| [x](x.md) | Global X coordinate in the facility floor plan |
| [x_offset](x_offset.md) | Shift in the X direction in the facility floor plan |
| [x_rot](x_rot.md) | Rotation around the X-axis in the facility floor plan |
| [y](y.md) | Global Y coordinate in the facility floor plan |
| [y_offset](y_offset.md) | Shift in the Y direction in the facility floor plan |
| [y_rot](y_rot.md) | Rotation around the Y-axis in the facility floor plan |
| [z](z.md) | Global Z coordinate in the facility floor plan |
| [z_offset](z_offset.md) | Shift in the Z direction in the facility floor plan |
| [z_rot](z_rot.md) | Rotation around the Z-axis in the facility floor plan |
| [zero_phase](zero_phase.md) | Sets what phase = 0 means |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AxisEnum](AxisEnum.md) |  |
| [CanonicalSignalTypeEnum](CanonicalSignalTypeEnum.md) | Portable semantic meanings for important signals |
| [CavityTypeEnum](CavityTypeEnum.md) | The type of cavity, which determines the field configuration and mode structu... |
| [ComponentRelationPredicateEnum](ComponentRelationPredicateEnum.md) |  |
| [DataTypeEnum](DataTypeEnum.md) | Data types for parameter values |
| [DirectionEnum](DirectionEnum.md) |  |
| [FacilityFunctionEnum](FacilityFunctionEnum.md) | Broad structural or support functions |
| [IdentifierTypeEnum](IdentifierTypeEnum.md) | Controlled values for identifier types |
| [MultipoleGeometryEnum](MultipoleGeometryEnum.md) | The geometric configuration of the multipole field |
| [PhysicalFunctionEnum](PhysicalFunctionEnum.md) | Broad device-level functions |
| [PhysicalRelationEnum](PhysicalRelationEnum.md) | Controlled values for physical relation to the beamline |
| [PlaneEnum](PlaneEnum.md) | Controlled values for transverse plane |
| [QuantityKindEnum](QuantityKindEnum.md) | Physical quantity kinds for signals |
| [ReferenceFrameEnum](ReferenceFrameEnum.md) |  |
| [ReferenceGeometryEnum](ReferenceGeometryEnum.md) | The reference geometry used to calculate multipoles |
| [RelationContextEnum](RelationContextEnum.md) |  |
| [SignalBindingPredicateEnum](SignalBindingPredicateEnum.md) | Controlled predicates for Component-to-Signal bindings |
| [SignalRoleEnum](SignalRoleEnum.md) | Roles for control-system signals |
| [SourceSystemEnum](SourceSystemEnum.md) | Controlled values for facility-local source systems |
| [UnitEnum](UnitEnum.md) | Engineering units using ASCII-safe enum names |
| [VirtualFunctionEnum](VirtualFunctionEnum.md) | Broad virtual component functions or roles |
| [VirtualRelationEnum](VirtualRelationEnum.md) | Controlled values for virtual relation to the beamline |
| [ZeroPhaseEnum](ZeroPhaseEnum.md) | The zero phase reference for the cavity, which determines the phase of the RF... |


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
