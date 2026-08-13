
# accelerator_core


**metamodel version:** 1.7.0

**version:** None


A lightweight LinkML schema for facility-agnostic accelerator components, their beamline relationships, and associated control-system signals.


### Classes

 * [AdditionalMetadata](AdditionalMetadata.md) - A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
 * [Affiliation](Affiliation.md) - Contains affiliation information for an author or component, such as a ROR.
 * [Author](Author.md) - Contains authorship information for a representation of an accelerator facility and its operations.
 * [CoordinateSet](CoordinateSet.md) - A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis.
 * [Edge](Edge.md) - Abstract base for subject-predicate-object associations.
     * [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
         * [AdjacentTo](AdjacentTo.md) - A relationship indicating that the subject component is adjacent to the object component and not overlapping
         * [Contains](Contains.md) - A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping.
         * [Controls](Controls.md) - A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet.
         * [HasConnectingBranch](HasConnectingBranch.md) - A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch.
         * [Intersects](Intersects.md) - A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device.
         * [IsPartOf](IsPartOf.md) - A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection.
         * [MountedOn](MountedOn.md) - A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet.
         * [NearestTo](NearestTo.md) - A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet.
         * [Overlaps](Overlaps.md) - A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device.
         * [Precedes](Precedes.md) - A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline.
     * [SignalBinding](SignalBinding.md) - Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.
         * [HasCommandSignal](HasCommandSignal.md)
         * [HasLimitSignal](HasLimitSignal.md)
         * [HasReadbackSignal](HasReadbackSignal.md)
         * [HasSetpointSignal](HasSetpointSignal.md)
         * [HasSignal](HasSignal.md)
 * [Facility](Facility.md) - A facility that houses one or more accelerators.
 * [Identifier](Identifier.md) - A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.
 * [MultipoleParameterGroup](MultipoleParameterGroup.md) - A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
 * [Node](Node.md) - Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology.
     * [Component](Component.md) - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
         * [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
             * [Cavity](Cavity.md) - A cavity used for beam acceleration or manipulation.
                 * [CrabCavity](CrabCavity.md) - A cavity used for transverse beam manipulation, such as crabbing or deflecting.
                 * [RFCavity](RFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation.
                     * [NormalConductingRFCavity](NormalConductingRFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.
                     * [SuperConductingRFCavity](SuperConductingRFCavity.md) - A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
             * [DiagnosticDevice](DiagnosticDevice.md) - An accelerator device used to measure beam or machine state.
                 * [Aperture](Aperture.md) - A diagnostic or limiting aperture element used to constrain or characterize beam passage.
                 * [BeamPositionMonitor](BeamPositionMonitor.md) - A diagnostic device used to measure transverse beam position.
                 * [BeamProfileMonitor](BeamProfileMonitor.md) - A diagnostic device used to measure transverse beam profile.
                 * [RadiationMonitor](RadiationMonitor.md) - A diagnostic device used to monitor radiation dose or dose rate.
             * [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.
                 * [Kicker](Kicker.md) - A magnet primarily used to steer the beam.
                     * [ACKicker](ACKicker.md) - An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.
                 * [Multipole](Multipole.md) - A general magnet with a higher-order multipole field, such as a sextupole or octupole.
                     * [Bend](Bend.md) - Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
                     * [Octupole](Octupole.md) - A magnet primarily used to focus or defocus the beam. 8 poles.
                     * [Quadrupole](Quadrupole.md) - A magnet primarily used to focus or defocus the beam. 4 poles.
                     * [Sextupole](Sextupole.md) - A magnet primarily used to focus or defocus the beam. 6 poles.
                 * [Solenoid](Solenoid.md) - A magnet with a primarily longitudinal magnetic field used for focusing.
             * [SupportingFacilityComponent](SupportingFacilityComponent.md) - A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.
         * [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
             * [BeamLine](BeamLine.md) - PALS element for an ordered sequence of beamline elements defining a beam path.
             * [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.
                 * [BeamLineSection](BeamLineSection.md) - A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components.
                 * [Marker](Marker.md) - A virtual component used as a reference point or marker in the beamline structure.
     * [Signal](Signal.md) - Semantic meaning of a control-system signal associated with a component.
 * [PALSAccelerator](PALSAccelerator.md) - Root container for accelerator core components, semantic signals, and local bindings.
 * [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.
     * [BendParamGroup](BendParamGroup.md) - Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
     * [BodyShiftParamGroup](BodyShiftParamGroup.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
     * [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md) - Mixin for electric multipole parameters,  which can be used to describe the electric field components of an accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7
     * [FloorParamGroup](FloorParamGroup.md) - Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
     * [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md) - Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present.
     * [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md) - Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7
     * [MetaParamGroup](MetaParamGroup.md) - Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * [RFParamGroup](RFParamGroup.md) - Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
     * [ReferenceParamGroup](ReferenceParamGroup.md) - Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
     * [SolenoidParamGroup](SolenoidParamGroup.md) - Mixin for solenoid-specific parameters.
     * [TwissParamGroup](TwissParamGroup.md) - Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.

### Mixins

 * [HasBendP](HasBendP.md)
 * [HasBodyShiftP](HasBodyShiftP.md)
 * [HasElectricMultipoleP](HasElectricMultipoleP.md)
 * [HasFloorP](HasFloorP.md)
 * [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md)
 * [HasMagneticMultipoleP](HasMagneticMultipoleP.md)
 * [HasMetaP](HasMetaP.md)
 * [HasRFP](HasRFP.md)
 * [HasReferenceP](HasReferenceP.md)
 * [HasSolenoidP](HasSolenoidP.md)
 * [HasTwissP](HasTwissP.md)

### Slots

 * [➞datatype](additionalMetadata__datatype.md) - Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string.
 * [➞key](additionalMetadata__key.md) - The metadata field name.
 * [➞value](additionalMetadata__value.md) - The metadata value, serialized as a string.
 * [affiliation](affiliation.md) - The affiliation of the author or component, as a ROR.
 * [alias](alias.md) - An alternative name or identifier for the instance.
 * [➞email](author__email.md) - The email address of the author.
 * [➞orcid](author__orcid.md) - The ORCID identifier of the author.
 * [➞direction](beamLine__direction.md) - Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1.
 * [➞multipass](beamLine__multipass.md) - Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass.
 * [➞periodic](beamLine__periodic.md) - Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic.
 * [➞repeat](beamLine__repeat.md) - Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
 * [beamline_context](beamline_context.md) - The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine.
 * [➞L_chord](bendParamGroup__L_chord.md) - Chord length of the bend.
 * [➞L_rectangle](bendParamGroup__L_rectangle.md) - Rectangular length.
 * [➞L_sagitta](bendParamGroup__L_sagitta.md) - Output parameter. Sagitta length.
 * [➞angle_ref](bendParamGroup__angle_ref.md) - Reference bend angle.
 * [➞bend_field_actual](bendParamGroup__bend_field_actual.md) - Actual bend field.
 * [➞bend_field_ref](bendParamGroup__bend_field_ref.md) - Reference bend field.
 * [➞e1](bendParamGroup__e1.md) - Entrance end pole face rotation with respect to a sector geometry.
 * [➞e1_rect](bendParamGroup__e1_rect.md) - Entrance end pole face rotation with respect to a rectangular geometry.
 * [➞e2](bendParamGroup__e2.md) - Exit end pole face rotation with respect to a sector geometry.
 * [➞e2_rect](bendParamGroup__e2_rect.md) - Exit end pole face rotation with respect to a rectangular geometry.
 * [➞edge1_int](bendParamGroup__edge1_int.md) - Entrance end fringe field integral.
 * [➞edge2_int](bendParamGroup__edge2_int.md) - Exit end fringe field integral.
 * [➞g_actual](bendParamGroup__g_actual.md) - Actual bend strength = 1/radius_actual
 * [➞g_ref](bendParamGroup__g_ref.md) - Reference bend strength = 1/radius_ref
 * [➞h1](bendParamGroup__h1.md) - Entrance end pole face curvature
 * [➞h2](bendParamGroup__h2.md) - Exit end pole face curvature
 * [➞multipole_geometry](bendParamGroup__multipole_geometry.md) - Multipole geometry type. Must be `follows_ref_geometry`.
 * [➞ref_geometry](bendParamGroup__ref_geometry.md) - Reference geometry type. Must be `arc`.
 * [➞rho_ref](bendParamGroup__rho_ref.md) - Reference bend radius.
 * [➞tilt_ref](bendParamGroup__tilt_ref.md) - Reference tilt of the bend.
 * [➞x_offset](bodyShiftParamGroup__x_offset.md) - Shift in the X direction in the facility floor plan.
 * [➞x_rot](bodyShiftParamGroup__x_rot.md) - Rotation around the X-axis in the facility floor plan.
 * [➞y_offset](bodyShiftParamGroup__y_offset.md) - Shift in the Y direction in the facility floor plan.
 * [➞y_rot](bodyShiftParamGroup__y_rot.md) - Rotation around the Y-axis in the facility floor plan.
 * [➞z_offset](bodyShiftParamGroup__z_offset.md) - Shift in the Z direction in the facility floor plan.
 * [➞z_rot](bodyShiftParamGroup__z_rot.md) - Rotation around the Z-axis in the facility floor plan.
 * [➞component_direction](componentRelation__component_direction.md)
 * [➞reference_frame](componentRelation__reference_frame.md)
 * [➞native_types](component__native_types.md) - The native type of the component in the source system, which can be used to identify the component across different source systems.
 * [context](context.md) - The frame of reference / domain in which this relationship is asserted to hold.
     * [HasConnectingBranch➞context](HasConnectingBranch_context.md) - The frame of reference / domain in which this relationship is asserted to hold. For pals:has_connecting_branch, this is the Beamline context = beamline_context.
     * [Precedes➞context](Precedes_context.md) - The frame of reference / domain in which this relationship is asserted to hold. For pals:precedes, this is the Beamline context = beamline_context.
 * [➞coordinate_system](coordinateSet__coordinate_system.md) - The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical).
 * [➞phi_coord](coordinateSet__phi_coord.md) - The azimuthal angle in spherical coordinates (in radians).
 * [➞r_coord](coordinateSet__r_coord.md) - The radial distance in cylindrical coordinates.
 * [➞theta_coord](coordinateSet__theta_coord.md) - The angular coordinate in cylindrical coordinates (in radians).
 * [➞x_coord](coordinateSet__x_coord.md) - The x-coordinate in the specified coordinate system.
 * [➞y_coord](coordinateSet__y_coord.md) - The y-coordinate in the specified coordinate system.
 * [➞z_coord](coordinateSet__z_coord.md) - The z-coordinate in the specified coordinate system.
 * [coordinates](coordinates.md) - A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.
 * [description](description.md) - A human-readable description of the instance.
 * [distance_unit](distance_unit.md) - Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.
 * [distance_value](distance_value.md) - Distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.
 * [➞elec_components](electricMultipoleParamGroup__elec_components.md) - Electric multipole components, one per order N.
 * [➞beamlines](facility__beamlines.md) - A list of beamlines in the accelerator system.
 * [➞component_relations](facility__component_relations.md) - A list of component relations in the accelerator system (Component <-> Component relationships).
 * [➞components](facility__components.md) - A list of physical components in the accelerator system.
 * [➞signal_bindings](facility__signal_bindings.md) - A list of signal bindings in the accelerator system (Component <-> Signal relationships).
 * [➞signals](facility__signals.md) - A list of signals in the accelerator system.
 * [➞phi](floorParamGroup__phi.md) - Rotation around the X-axis in the facility floor plan.
 * [➞psi](floorParamGroup__psi.md) - Rotation around the Z-axis in the facility floor plan.
 * [➞theta](floorParamGroup__theta.md) - Orientation angle around the Y-axis in the facility floor plan.
 * [➞x](floorParamGroup__x.md) - Global X coordinate in the facility floor plan.
 * [➞y](floorParamGroup__y.md) - Global Y coordinate in the facility floor plan.
 * [➞z](floorParamGroup__z.md) - Global Z coordinate in the facility floor plan.
 * [➞BendP](hasBendP__BendP.md) - A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞BodyShiftP](hasBodyShiftP__BodyShiftP.md) - A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞ElectricMultipoleP](hasElectricMultipoleP__ElectricMultipoleP.md) - A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞FloorP](hasFloorP__FloorP.md) - A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞LongitudinalPlacementP](hasLongitudinalPlacementP__LongitudinalPlacementP.md) - A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞MagneticMultipoleP](hasMagneticMultipoleP__MagneticMultipoleP.md) - A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞MetaP](hasMetaP__MetaP.md) - A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞RFP](hasRFP__RFP.md) - A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞ReferenceP](hasReferenceP__ReferenceP.md) - A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞SolenoidP](hasSolenoidP__SolenoidP.md) - A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [➞TwissP](hasTwissP__TwissP.md) - A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
 * [id](id.md) - A unique identifier for the instance.
 * [➞identifier_type](identifier__identifier_type.md) - The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK.
 * [➞identifier_value](identifier__identifier_value.md) - The value of the identifier.
 * [identifiers](identifiers.md) - A unique and ideally persistent identifier for the facility, such as a DOI or ROR.
 * [➞plane](kicker__plane.md) - The transverse plane in which the kicker operates, either horizontal or vertical.
 * [kind](kind.md) - The LinkML class name of this instance.
 * [length](length.md) - Length of the element (arc length for bends).
     * [BeamLine➞length](BeamLine_length.md) - The total length of the BeamLine. For pals interoperability, use m as the unit of length.
 * [➞s_position](longitudinalPlacementParamGroup__s_position.md) - Longitudinal position of the element along the beamline.
 * [➞mag_components](magneticMultipoleParamGroup__mag_components.md) - Magnetic multipole components, one per order N.
 * [➞additional_metadata](metaParamGroup__additional_metadata.md) - Additional metadata or annotations for the instance.
 * [➞label](metaParamGroup__label.md) - A label string.
 * [➞Bn](multipoleParameterGroup__Bn.md) - Normal component of the magnetic field.
 * [➞Bs](multipoleParameterGroup__Bs.md) - Skew component of the magnetic field.
 * [➞En](multipoleParameterGroup__En.md) - Normal component of the field.
 * [➞EnL](multipoleParameterGroup__EnL.md) - Length-integrated normal component.
 * [➞Es](multipoleParameterGroup__Es.md) - Skew component of the field.
 * [➞EsL](multipoleParameterGroup__EsL.md) - Length-integrated skew component.
 * [➞Kn](multipoleParameterGroup__Kn.md) - Normalized normal component.
 * [➞Ks](multipoleParameterGroup__Ks.md) - Normalized skew component.
 * [➞order](multipoleParameterGroup__order.md) - Multipole order N (0 = dipole, 1 = quadrupole, etc.)
 * [➞tilt](multipoleParameterGroup__tilt.md) - Tilt of the Nth multipole.
 * [name](name.md) - The name of the entity. For example, the name of the person or organization.
 * [object](object.md)
     * [ComponentRelation➞object](ComponentRelation_object.md)
     * [SignalBinding➞object](SignalBinding_object.md)
 * [➞authors](pALSAccelerator__authors.md) - Contains the authorship information for this representation of an accelerator facility and its operations.
 * [➞facility](pALSAccelerator__facility.md) - A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc.
 * [➞notes](pALSAccelerator__notes.md) - Additional notes or comments about the representation of a particle accelerator and its operations.
 * [➞version](pALSAccelerator__version.md) - Version of the representation of a particle accelerator and its operations.
 * [➞beamline_relation](physicalComponent__beamline_relation.md) - The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
 * [➞functions](physicalComponent__functions.md) - The function of the physical component,  which can be used to identify the component across different source systems.
 * [predicate](predicate.md)
     * [AdjacentTo➞predicate](AdjacentTo_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [Contains➞predicate](Contains_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [Controls➞predicate](Controls_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [HasCommandSignal➞predicate](HasCommandSignal_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [HasConnectingBranch➞predicate](HasConnectingBranch_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [HasLimitSignal➞predicate](HasLimitSignal_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [HasReadbackSignal➞predicate](HasReadbackSignal_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [HasSetpointSignal➞predicate](HasSetpointSignal_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [HasSignal➞predicate](HasSignal_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [Intersects➞predicate](Intersects_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [IsPartOf➞predicate](IsPartOf_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [MountedOn➞predicate](MountedOn_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [NearestTo➞predicate](NearestTo_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [Overlaps➞predicate](Overlaps_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * [Precedes➞predicate](Precedes_predicate.md) - The predicate of the relationship, which can be used to identify the relationship across different source systems.
 * [➞L_active](rFParamGroup__L_active.md) - Active acceleration length.
 * [➞cavity_type](rFParamGroup__cavity_type.md) - Cavity type
 * [➞dE_ref](rFParamGroup__dE_ref.md) - Reference energy gain.
 * [➞frequency](rFParamGroup__frequency.md) - RF frequency.
 * [➞harmon](rFParamGroup__harmon.md) - RF harmonic number.
 * [➞multipass_phase](rFParamGroup__multipass_phase.md) - rad/2pi RF Phase added to multipass elements
 * [➞num_cells](rFParamGroup__num_cells.md) - Number of cells in the cavity
 * [➞phase](rFParamGroup__phase.md) - RF phase. rad/2pi RF phase in 0 to 2*pi
 * [➞voltage](rFParamGroup__voltage.md) - RF voltage.
 * [➞zero_phase](rFParamGroup__zero_phase.md) - Sets what phase = 0 means.
 * [➞E_tot_ref](referenceParamGroup__E_tot_ref.md) - [eV] Reference total energy
 * [➞pc_ref](referenceParamGroup__pc_ref.md) - [momentum*c] Reference momentum times speed of light.
 * [➞species_ref](referenceParamGroup__species_ref.md) - A reference to a species or particle type, such as an ion, electron, or proton.
 * [➞time_ref](referenceParamGroup__time_ref.md) - [s] Reference time
 * [➞access_protocol](signal__access_protocol.md) - The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
 * [➞archive_identifier](signal__archive_identifier.md) - The identifier used to reference the signal in an archival system.
 * [➞canonical_signal_type](signal__canonical_signal_type.md) - The canonical semantic meaning of the signal.
 * [➞native_data_type](signal__native_data_type.md) - The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean.
 * [➞native_description](signal__native_description.md) - A human-readable description of the signal in the source system.
 * [➞native_unit](signal__native_unit.md) - The native unit of the signal in the source system.
 * [➞quantity_kind](signal__quantity_kind.md) - The physical quantity kind of the signal.
 * [➞signal_role](signal__signal_role.md) - The role of the signal in the control system, such as setpoint, readback, status, command, or limit.
 * [➞source_system](signal__source_system.md) - The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service.
 * [➞Bsol](solenoidParamGroup__Bsol.md) - Solenoid field.
 * [➞Ksol](solenoidParamGroup__Ksol.md) - Normalized solenoid strength.
 * [subject](subject.md)
     * [ComponentRelation➞subject](ComponentRelation_subject.md)
     * [SignalBinding➞subject](SignalBinding_subject.md)
 * [➞functions](supportingFacilityComponent__functions.md) - The function of the supporting facility component,  which can be used to identify the component across different source systems.
 * [tolerance_unit](tolerance_unit.md) - Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.
 * [tolerance_value](tolerance_value.md) - Tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.
 * [➞alpha_a](twissParamGroup__alpha_a.md) - Twiss alpha parameter in the horizontal plane.
 * [➞alpha_b](twissParamGroup__alpha_b.md) - Twiss alpha parameter in the vertical plane.
 * [➞beta_a](twissParamGroup__beta_a.md) - Twiss beta parameter in the horizontal plane.
 * [➞beta_b](twissParamGroup__beta_b.md) - Twiss beta parameter in the vertical plane.
 * [➞eta_x](twissParamGroup__eta_x.md) - Twiss dispersion parameter in the horizontal plane.
 * [➞eta_y](twissParamGroup__eta_y.md) - Twiss dispersion parameter in the vertical plane.
 * [➞etap_x](twissParamGroup__etap_x.md) - Twiss dispersion slope parameter in the horizontal plane.
 * [➞etap_y](twissParamGroup__etap_y.md) - Twiss dispersion slope parameter in the vertical plane.
 * [➞phi_a](twissParamGroup__phi_a.md) - Twiss phase advance parameter in the horizontal plane.
 * [➞phi_b](twissParamGroup__phi_b.md) - Twiss phase advance parameter in the vertical plane.
 * [➞beamline_relation](virtualComponent__beamline_relation.md) - The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
 * [➞functions](virtualComponent__functions.md) - The function of the virtual component,  which can be used to identify the component across different source systems.

### Enums

 * [CanonicalSignalTypeEnum](CanonicalSignalTypeEnum.md) - Portable semantic meanings for important signals.
 * [CavityTypeEnum](CavityTypeEnum.md) - The type of cavity, which determines the field configuration and mode structure.
 * [CoordinateSystemEnum](CoordinateSystemEnum.md) - Coordinate systems for spatial relationships.
 * [DataTypeEnum](DataTypeEnum.md) - Data types for parameter values.
 * [DirectionEnum](DirectionEnum.md)
 * [FacilityFunctionEnum](FacilityFunctionEnum.md) - Broad structural or support functions.
 * [IdentifierTypeEnum](IdentifierTypeEnum.md) - Controlled values for identifier types.
 * [MultipoleGeometryEnum](MultipoleGeometryEnum.md) - The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles.
 * [PhysicalFunctionEnum](PhysicalFunctionEnum.md) - Broad device-level functions.
 * [PhysicalRelationEnum](PhysicalRelationEnum.md) - Controlled values for physical relation to the beamline.
 * [PlaneEnum](PlaneEnum.md) - Controlled values for transverse plane.
 * [QuantityKindEnum](QuantityKindEnum.md) - Physical quantity kinds for signals.
 * [ReferenceFrameEnum](ReferenceFrameEnum.md)
 * [ReferenceGeometryEnum](ReferenceGeometryEnum.md) - The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles.
 * [RelationContextEnum](RelationContextEnum.md)
 * [SignalRoleEnum](SignalRoleEnum.md) - Roles for control-system signals.
 * [SourceSystemEnum](SourceSystemEnum.md) - Controlled values for facility-local source systems.
 * [UnitEnum](UnitEnum.md) - Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available.
 * [VirtualFunctionEnum](VirtualFunctionEnum.md) - Broad virtual component functions or roles.
 * [VirtualRelationEnum](VirtualRelationEnum.md) - Controlled values for virtual relation to the beamline.
 * [ZeroPhaseEnum](ZeroPhaseEnum.md) - The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity.

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
