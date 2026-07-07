
# accelerator_core


**metamodel version:** 1.7.0

**version:** None


A lightweight LinkML schema for facility-agnostic accelerator components, their beamline relationships, and associated control-system signals.


### Classes

 * [AnyValue](AnyValue.md) - A slot that can take any value, used for fields where a controlled vocabulary is not necessary or not yet established. Use when the field can contain a wide range of values that do not fit into a predefined set, or when flexibility is needed for future expansion.
 * [Component](Component.md) - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
     * [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
         * [Cavity](Cavity.md) - A cavity used for beam acceleration or manipulation.
             * [CrabCavity](CrabCavity.md) - A cavity used for transverse beam manipulation, such as crabbing or deflecting.
             * [RFCavity](RFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation.
         * [DiagnosticDevice](DiagnosticDevice.md) - An accelerator device used to measure beam or machine state.
             * [BeamPositionMonitor](BeamPositionMonitor.md) - A diagnostic device used to measure transverse beam position.
             * [RadiationMonitor](RadiationMonitor.md) - A diagnostic device used to monitor radiation dose or dose rate.
         * [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.
             * [Kicker](Kicker.md) - A magnet primarily used to steer the beam.
             * [Multipole](Multipole.md) - A general magnet with a higher-order multipole field, such as a sextupole or octupole.
                 * [Dipole](Dipole.md) - A magnet primarily used to bend the beam. 2 poles.
                 * [Octupole](Octupole.md) - A magnet primarily used to focus or defocus the beam. 8 poles.
                 * [Quadrupole](Quadrupole.md) - A magnet primarily used to focus or defocus the beam. 4 poles.
                 * [Sextupole](Sextupole.md) - A magnet primarily used to focus or defocus the beam. 6 poles.
             * [Solenoid](Solenoid.md) - A magnet with a primarily longitudinal magnetic field used for focusing.
         * [SupportingFacilityComponent](SupportingFacilityComponent.md) - A physical component that supports accelerator operation
     * [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
         * [Beamline](Beamline.md) - A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
         * [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,
             * [BeamlineSection](BeamlineSection.md) - A virtual component used to represent a section of the beamline for organizational
             * [Marker](Marker.md) - A virtual component used as a reference point or marker in the beamline structure.
 * [MultipoleComponent](MultipoleComponent.md) - A single order's electric (or magnetic) multipole component.
 * [NARAD](NARAD.md) - Root container for accelerator core components, semantic signals, and local bindings.
 * [Relationship](Relationship.md) - Abstract base for subject-predicate-object associations.
     * [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
     * [SignalBinding](SignalBinding.md) - Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.
 * [Signal](Signal.md) - Semantic meaning of a control-system signal associated with a component.

### Mixins

 * [BodyShiftP](BodyShiftP.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 * [ElectricMultipoleP](ElectricMultipoleP.md) - Mixin for electric multipole parameters,
 * [FloorP](FloorP.md) - Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 * [HasLongitudinalPlacement](HasLongitudinalPlacement.md) - Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.
 * [MagneticMultipoleP](MagneticMultipoleP.md) - Mixin for magnetic multipole parameters,
 * [MetaP](MetaP.md) - Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [ReferenceP](ReferenceP.md) - Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
 * [SolenoidP](SolenoidP.md) - Mixin for solenoid-specific parameters.
 * [TwissP](TwissP.md) - Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

### Slots

 * [➞value](anyValue__value.md)
 * [➞direction](beamline__direction.md) - Beam direction along the beamline: +1 or -1.
 * [➞length](beamline__length.md) - The total length of the beamline.
 * [➞multipass](beamline__multipass.md) - Indicates whether the beamline is a multipass beamline, where the beam passes through the same physical elements multiple times.
 * [➞periodic](beamline__periodic.md) - Indicates whether orbit and Twiss parameters periodic.
 * [➞repeat](beamline__repeat.md) - Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
 * [➞zero_point](beamline__zero_point.md) - Name of a line item used as a reference point when the BeamLine is used as a subline.
 * [➞x_offset](bodyShiftP__x_offset.md) - Shift in the X direction in the facility floor plan.
 * [➞x_rot](bodyShiftP__x_rot.md) - Rotation around the X-axis in the facility floor plan.
 * [➞y_offset](bodyShiftP__y_offset.md) - Shift in the Y direction in the facility floor plan.
 * [➞y_rot](bodyShiftP__y_rot.md) - Rotation around the Y-axis in the facility floor plan.
 * [➞z_offset](bodyShiftP__z_offset.md) - Shift in the Z direction in the facility floor plan.
 * [➞z_rot](bodyShiftP__z_rot.md) - Rotation around the Z-axis in the facility floor plan.
 * [➞axis](componentRelation__axis.md)
 * [➞beamline_context](componentRelation__beamline_context.md) - The specific Beamline this relationship is defined with respect to (relevant when context=beamline_order).
 * [➞context](componentRelation__context.md) - The frame of reference / domain in which this relationship is asserted to hold.
 * [➞direction](componentRelation__direction.md)
 * [➞distance_unit](componentRelation__distance_unit.md)
 * [➞distance_value](componentRelation__distance_value.md)
 * [➞reference_frame](componentRelation__reference_frame.md)
 * [➞tolerance_unit](componentRelation__tolerance_unit.md)
 * [➞tolerance_value](componentRelation__tolerance_value.md)
 * [➞id](component__id.md) - A unique identifier for the component.
 * [➞native_types](component__native_types.md) - The native type of the component in the source system, which can be used to identify the component across different source systems.
 * [➞type](component__type.md) - The LinkML class type of the component, which can be used to distinguish between different kinds of components.
 * [➞components](electricMultipoleP__components.md) - Electric multipole components, one per order N.
 * [➞phi](floorP__phi.md) - Rotation around the X-axis in the facility floor plan.
 * [➞psi](floorP__psi.md) - Rotation around the Z-axis in the facility floor plan.
 * [➞theta](floorP__theta.md) - Orientation angle around the Y-axis in the facility floor plan.
 * [➞x](floorP__x.md) - Global X coordinate in the facility floor plan.
 * [➞y](floorP__y.md) - Global Y coordinate in the facility floor plan.
 * [➞z](floorP__z.md) - Global Z coordinate in the facility floor plan.
 * [➞length](hasLongitudinalPlacement__length.md) - Length of the element (arc length for bends).
 * [➞s_position](hasLongitudinalPlacement__s_position.md) - Longitudinal position of the element along the beamline.
 * [id](id.md) - This is specific to the relationship class Unique identifier for this relationship instance.
 * [➞plane](kicker__plane.md) - The transverse plane in which the kicker operates, either horizontal or vertical.
 * [➞components](magneticMultipoleP__components.md) - Magnetic multipole components, one per order N.
 * [➞additional_metadata](metaP__additional_metadata.md) - Additional metadata or annotations for the instance.
 * [➞alias](metaP__alias.md) - An alternative name or identifier for the instance.
 * [➞description](metaP__description.md) - Human-readable description.
 * [➞label](metaP__label.md) - A label string.
 * [➞Bn](multipoleComponent__Bn.md) - Normal component of the magnetic field.
 * [➞Bs](multipoleComponent__Bs.md) - Skew component of the magnetic field.
 * [➞En](multipoleComponent__En.md) - Normal component of the field.
 * [➞EnL](multipoleComponent__EnL.md) - Length-integrated normal component.
 * [➞Es](multipoleComponent__Es.md) - Skew component of the field.
 * [➞EsL](multipoleComponent__EsL.md) - Length-integrated skew component.
 * [➞Kn](multipoleComponent__Kn.md) - Normalized normal component.
 * [➞Ks](multipoleComponent__Ks.md) - Normalized skew component.
 * [➞order](multipoleComponent__order.md) - Multipole order N (0 = dipole, 1 = quadrupole, etc.)
 * [➞tilt](multipoleComponent__tilt.md) - Tilt of the Nth multipole.
 * [➞beamlines](nARAD__beamlines.md) - A list of beamlines in the accelerator system.
 * [➞component_relations](nARAD__component_relations.md) - A list of component relations in the accelerator system (Component <-> Component relationships).
 * [➞description](nARAD__description.md) - Human-readable description for the representation of a particle accelerator and its operations.
 * [➞physical_components](nARAD__physical_components.md) - A list of physical components in the accelerator system.
 * [➞signal_bindings](nARAD__signal_bindings.md) - A list of signal bindings in the accelerator system (Component <-> Signal relationships).
 * [➞signals](nARAD__signals.md) - A list of signals in the accelerator system.
 * [➞supporting_facility_components](nARAD__supporting_facility_components.md) - A list of supporting facility components in the accelerator system.
 * [➞type](nARAD__type.md) - The LinkML class type of the NARAD root container, i.e., `NARAD`, which can be used to distinguish between different kinds of NARAD representations.
 * [➞virtual_components](nARAD__virtual_components.md) - A list of virtual components in the accelerator system.
 * [object](object.md)
     * [ComponentRelation➞object](ComponentRelation_object.md)
     * [SignalBinding➞object](SignalBinding_object.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md) - The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
 * [➞function](physicalComponent__function.md) - The function of the physical component,  which can be used to identify the component across different source systems.
 * [predicate](predicate.md)
     * [ComponentRelation➞predicate](ComponentRelation_predicate.md)
     * [SignalBinding➞predicate](SignalBinding_predicate.md)
 * [➞E_tot_ref](referenceP__E_tot_ref.md) - [eV] Reference total energy
 * [➞pc_ref](referenceP__pc_ref.md) - [momentum*c] Reference momentum times speed of light.
 * [➞species_ref](referenceP__species_ref.md) - A reference to a species or particle type, such as an ion, electron, or proton.
 * [➞time_ref](referenceP__time_ref.md) - [s] Reference time
 * [➞access_protocol](signal__access_protocol.md) - The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
 * [➞archive_identifier](signal__archive_identifier.md) - The identifier used to reference the signal in an archival system.
 * [➞canonical_signal_type](signal__canonical_signal_type.md) - The canonical semantic meaning of the signal.
 * [➞id](signal__id.md) - A unique identifier for the signal.
 * [➞native_data_type](signal__native_data_type.md) - The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean.
 * [➞native_description](signal__native_description.md) - A human-readable description of the signal in the source system.
 * [➞native_unit](signal__native_unit.md) - The native unit of the signal in the source system.
 * [➞quantity_kind](signal__quantity_kind.md) - The physical quantity kind of the signal.
 * [➞signal_role](signal__signal_role.md) - The role of the signal in the control system, such as setpoint, readback, status, command, or limit.
 * [➞source_system](signal__source_system.md) - The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service.
 * [➞type](signal__type.md) - The LinkML class type of the signal, i,e. Signal.
 * [➞Bsol](solenoidP__Bsol.md) - Solenoid field.
 * [➞Ksol](solenoidP__Ksol.md) - Normalized solenoid strength.
 * [subject](subject.md)
     * [ComponentRelation➞subject](ComponentRelation_subject.md)
     * [SignalBinding➞subject](SignalBinding_subject.md)
 * [➞function](supportingFacilityComponent__function.md) - The function of the supporting facility component,  which can be used to identify the component across different source systems.
 * [➞alpha_a](twissP__alpha_a.md) - Twiss alpha parameter in the horizontal plane.
 * [➞alpha_b](twissP__alpha_b.md) - Twiss alpha parameter in the vertical plane.
 * [➞beta_a](twissP__beta_a.md) - Twiss beta parameter in the horizontal plane.
 * [➞beta_b](twissP__beta_b.md) - Twiss beta parameter in the vertical plane.
 * [➞eta_x](twissP__eta_x.md) - Twiss dispersion parameter in the horizontal plane.
 * [➞eta_y](twissP__eta_y.md) - Twiss dispersion parameter in the vertical plane.
 * [➞etap_x](twissP__etap_x.md) - Twiss dispersion slope parameter in the horizontal plane.
 * [➞etap_y](twissP__etap_y.md) - Twiss dispersion slope parameter in the vertical plane.
 * [➞phi_a](twissP__phi_a.md) - Twiss phase advance parameter in the horizontal plane.
 * [➞phi_b](twissP__phi_b.md) - Twiss phase advance parameter in the vertical plane.
 * [➞beamline_relation](virtualComponent__beamline_relation.md) - The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
 * [➞function](virtualComponent__function.md) - The function of the virtual component,  which can be used to identify the component across different source systems.

### Enums

 * [AxisEnum](AxisEnum.md)
 * [CanonicalSignalTypeEnum](CanonicalSignalTypeEnum.md) - Portable semantic meanings for important signals.
 * [ComponentRelationPredicateEnum](ComponentRelationPredicateEnum.md)
 * [DataTypeEnum](DataTypeEnum.md) - Data types for parameter values.
 * [DirectionEnum](DirectionEnum.md)
 * [FacilityFunctionEnum](FacilityFunctionEnum.md) - Broad structural or support functions.
 * [PhysicalFunctionEnum](PhysicalFunctionEnum.md) - Broad device-level functions.
 * [PhysicalRelationEnum](PhysicalRelationEnum.md) - Controlled values for physical relation to the beamline.
 * [PlaneEnum](PlaneEnum.md) - Controlled values for transverse plane.
 * [QuantityKindEnum](QuantityKindEnum.md) - Physical quantity kinds for signals.
 * [ReferenceFrameEnum](ReferenceFrameEnum.md)
 * [RelationContextEnum](RelationContextEnum.md)
 * [SignalBindingPredicateEnum](SignalBindingPredicateEnum.md) - Controlled predicates for Component-to-Signal bindings.
 * [SignalRoleEnum](SignalRoleEnum.md) - Roles for control-system signals.
 * [SourceSystemEnum](SourceSystemEnum.md) - Controlled values for facility-local source systems.
 * [UnitEnum](UnitEnum.md) - Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available.
 * [VirtualFunctionEnum](VirtualFunctionEnum.md) - Broad virtual component functions or roles.
 * [VirtualRelationEnum](VirtualRelationEnum.md) - Controlled values for virtual relation to the beamline.

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
