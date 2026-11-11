# PALS facility configuration

A lightweight LinkML schema for facility-agnostic accelerator facility configuration, their beamline relationships, and associated control-system signals.

URI: https://w3id.org/pals-config

Name: pals_config



## Classes

| Class | Description |
| --- | --- |
| [AdditionalMetadata](classes/AdditionalMetadata.md) | A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata. |
| [Affiliation](classes/Affiliation.md) | Contains affiliation information for an author or component, such as a ROR. |
| [Author](classes/Author.md) | Contains authorship information for a representation of an accelerator facility and its operations. |
| [ChangeLogEntryClass](classes/ChangeLogEntryClass.md) | An individual entry in the change log, documenting a specific change to the data instance. |
| [CoordinateSet](classes/CoordinateSet.md) | A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis. |
| [Edge](classes/Edge.md) | Abstract base for subject-predicate-object associations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComponentRelation](classes/ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AdjacentTo](classes/AdjacentTo.md) | A relationship indicating that the subject component is adjacent to the object component and not overlapping<br> in a specified context, such as radiation detector and a magnet. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Contains](classes/Contains.md) | A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Controls](classes/Controls.md) | A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HasConnectingBranch](classes/HasConnectingBranch.md) | A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Intersects](classes/Intersects.md) | A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IsPartOf](classes/IsPartOf.md) | A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MountedOn](classes/MountedOn.md) | A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NearestTo](classes/NearestTo.md) | A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Overlaps](classes/Overlaps.md) | A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Precedes](classes/Precedes.md) | A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SignalBinding](classes/SignalBinding.md) | Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HasCommandSignal](classes/HasCommandSignal.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HasLimitSignal](classes/HasLimitSignal.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HasReadbackSignal](classes/HasReadbackSignal.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HasSetpointSignal](classes/HasSetpointSignal.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HasSignal](classes/HasSignal.md) |  |
| [Facility](classes/Facility.md) | A facility that houses one or more accelerators. |
| [HasBendP](classes/HasBendP.md) |  |
| [HasBodyShiftP](classes/HasBodyShiftP.md) |  |
| [HasElectricMultipoleP](classes/HasElectricMultipoleP.md) |  |
| [HasFloorP](classes/HasFloorP.md) |  |
| [HasLongitudinalPlacementP](classes/HasLongitudinalPlacementP.md) |  |
| [HasMagneticMultipoleP](classes/HasMagneticMultipoleP.md) |  |
| [HasMetaP](classes/HasMetaP.md) |  |
| [HasReferenceP](classes/HasReferenceP.md) |  |
| [HasRFP](classes/HasRFP.md) |  |
| [HasSolenoidP](classes/HasSolenoidP.md) |  |
| [HasTwissP](classes/HasTwissP.md) |  |
| [Identifier](classes/Identifier.md) | A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR. |
| [MultipoleParameterGroup](classes/MultipoleParameterGroup.md) | A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components. |
| [Node](classes/Node.md) | Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Component](classes/Component.md) | A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalComponent](classes/PhysicalComponent.md) | A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Cavity](classes/Cavity.md) | A cavity used for beam acceleration or manipulation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrabCavity](classes/CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflecting. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RFCavity](classes/RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NormalConductingRFCavity](classes/NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SuperConductingRFCavity](classes/SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is superconducting. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiagnosticDevice](classes/DiagnosticDevice.md) | An accelerator device used to measure beam or machine state. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Aperture](classes/Aperture.md) | A diagnostic or limiting aperture element used to constrain or characterize beam passage. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamPositionMonitor](classes/BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamProfileMonitor](classes/BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RadiationMonitor](classes/RadiationMonitor.md) | A diagnostic device used to monitor radiation dose or dose rate. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Magnet](classes/Magnet.md) | An accelerator device that produces a magnetic field for beam control. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kicker](classes/Kicker.md) | A magnet primarily used to steer the beam.<br>Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. <br>Only one of the electric or magnetic multipole components should be present, not both. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ACKicker](classes/ACKicker.md) | An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Multipole](classes/Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or octupole.<br>Only one of the electric or magnetic multipole components should be present, not both. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bend](classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Octupole](classes/Octupole.md) | A magnet primarily used to focus or defocus the beam. 8 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Quadrupole](classes/Quadrupole.md) | A magnet primarily used to focus or defocus the beam. 4 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sextupole](classes/Sextupole.md) | A magnet primarily used to focus or defocus the beam. 6 poles.<br>Only one of the electric or magnetic multipole components should be present, not both. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Solenoid](classes/Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing.<br>A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SupportingFacilityComponent](classes/SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VirtualComponent](classes/VirtualComponent.md) | A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamLine](classes/BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam path. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BookkeepingComponent](classes/BookkeepingComponent.md) | A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeamLineSection](classes/BeamLineSection.md) | A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BeginningEle](classes/BeginningEle.md) | Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference parameters; otherwise it is expected to be the first element in the branch. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Marker](classes/Marker.md) | A virtual component used as a reference point or marker in the beamline structure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Drift](classes/Drift.md) | A field-free space between beamline components. A Drift is a virtual beamline component whose longitudinal extent preserves the separation between adjacent physical or virtual components. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Signal](classes/Signal.md) | Semantic meaning of a control-system signal associated with a component. |
| [PALSAccelerator](classes/PALSAccelerator.md) | Root container for accelerator core components, semantic signals, and local bindings. |
| [ParamGroup](classes/ParamGroup.md) | Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BendParamGroup](classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BodyShiftParamGroup](classes/BodyShiftParamGroup.md) | Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ElectricMultipoleParamGroup](classes/ElectricMultipoleParamGroup.md) | Mixin for electric multipole parameters,  which can be used to describe the electric field components of an accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7<br>  tilt: 0.7<br>- order: 3<br>  En: 27.3<br>- order: 2<br>  EnL: 3.47e1<br>``` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FloorParamGroup](classes/FloorParamGroup.md) | Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LongitudinalPlacementParamGroup](classes/LongitudinalPlacementParamGroup.md) | Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MagneticMultipoleParamGroup](classes/MagneticMultipoleParamGroup.md) | Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7<br>  tilt: 0.7<br>- order: 3<br>  Bn: 27.3<br>- order: 2<br>  BnL: 3.47e1<br>- order: 1<br>  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength<br>``` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetaParamGroup](classes/MetaParamGroup.md) | Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReferenceParamGroup](classes/ReferenceParamGroup.md) | Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RFParamGroup](classes/RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SolenoidParamGroup](classes/SolenoidParamGroup.md) | Mixin for solenoid-specific parameters. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TwissParamGroup](classes/TwissParamGroup.md) | Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element. |
| [TemporalCoverageClass](classes/TemporalCoverageClass.md) | Temporal coverage for time-based datasets, if applicable.<br>  Container for elements describing the start_date and end_date of the data instance's temporal coverage <br>  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SS±hh:mm for offset (e.g., 2024-06-05T14:30:00-04:00) or YYYY-MM-DDTHH:MM:SSZ for UTC (e.g., 2024-06-05T14:30:00Z).<br>  Use temporal_coverage when the dataset describes a specific historical or projected time period.<br>  This may not apply to simulations where temporal coverage of a specific facility during a specific time is not relevant. |



## Slots

| Slot | Description |
| --- | --- |
| [access_protocol](slots/access_protocol.md) | The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service. |
| [additional_metadata](slots/additional_metadata.md) | Additional metadata or annotations for the instance. |
| [affiliation](slots/affiliation.md) | The affiliation of the author or component, as a ROR. |
| [alias](slots/alias.md) | An alternative name or identifier for the instance. |
| [alpha_a](slots/alpha_a.md) | Twiss alpha parameter in the horizontal plane. |
| [alpha_b](slots/alpha_b.md) | Twiss alpha parameter in the vertical plane. |
| [angle_ref](slots/angle_ref.md) | Reference bend angle. |
| [archive_identifier](slots/archive_identifier.md) | The identifier used to reference the signal in an archival system. |
| [authors](slots/authors.md) | Contains the authorship information for this representation of an accelerator facility and its operations. |
| [beamline_context](slots/beamline_context.md) | The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine. |
| [beamline_relation](slots/beamline_relation.md) | The relationship of the component to the beamline,  which can be used to identify the component across different source systems. |
| [beamlines](slots/beamlines.md) | A list of beamlines in the accelerator system. |
| [bend_field_actual](slots/bend_field_actual.md) | Actual bend field. |
| [bend_field_ref](slots/bend_field_ref.md) | Reference bend field. |
| [BendP](slots/BendP.md) | A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [beta_a](slots/beta_a.md) | Twiss beta parameter in the horizontal plane. Must be strictly positive (> 0). |
| [beta_b](slots/beta_b.md) | Twiss beta parameter in the vertical plane. Must be strictly positive (> 0). |
| [Bn](slots/Bn.md) | Normal component of the magnetic field. |
| [BodyShiftP](slots/BodyShiftP.md) | A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [Bs](slots/Bs.md) | Skew component of the magnetic field. |
| [Bsol](slots/Bsol.md) | Solenoid field. |
| [canonical_signal_type](slots/canonical_signal_type.md) | The canonical semantic meaning of the signal. |
| [cavity_type](slots/cavity_type.md) | Cavity type |
| [change_date](slots/change_date.md) | The date the change was made, in ISO 8601 format (YYYY-MM-DD). |
| [change_log](slots/change_log.md) | Running history of meaningful changes to a data instance of a facility's configuration. Add a new entry every time the instance is updated. Do not overwrite or delete prior entries. If there have been no changes since creation, include a single entry with the creation date and the summary 'Initial creation'. |
| [component_direction](slots/component_direction.md) |  |
| [component_relations](slots/component_relations.md) | A list of component relations in the accelerator system (Component <-> Component relationships). |
| [components](slots/components.md) | A list of physical components in the accelerator system. |
| [context](slots/context.md) | The frame of reference / domain in which this relationship is asserted to hold. |
| [coordinate_system](slots/coordinate_system.md) | The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical). |
| [coordinates](slots/coordinates.md) | A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship. |
| [created_date](slots/created_date.md) | The date the PALS/NARAD data instance of the facility configuration was first created, in ISO 8601 format (YYYY-MM-DD).  Provides temporal context for the data instance and can be used for tracking its age and relevance. |
| [datatype](slots/datatype.md) | Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string. |
| [dE_ref](slots/dE_ref.md) | Reference energy gain. |
| [description](slots/description.md) | A human-readable description of the instance. |
| [direction](slots/direction.md) | Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1. |
| [distance_unit](slots/distance_unit.md) | Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship. |
| [distance_value](slots/distance_value.md) | Distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship. |
| [e1](slots/e1.md) | Entrance end pole face rotation with respect to a sector geometry. |
| [e1_rect](slots/e1_rect.md) | Entrance end pole face rotation with respect to a rectangular geometry. |
| [e2](slots/e2.md) | Exit end pole face rotation with respect to a sector geometry. |
| [e2_rect](slots/e2_rect.md) | Exit end pole face rotation with respect to a rectangular geometry. |
| [E_tot_ref](slots/E_tot_ref.md) | [eV] Reference total energy |
| [edge1_int](slots/edge1_int.md) | Entrance end fringe field integral. |
| [edge2_int](slots/edge2_int.md) | Exit end fringe field integral. |
| [elec_components](slots/elec_components.md) | Electric multipole components, one per order N. |
| [ElectricMultipoleP](slots/ElectricMultipoleP.md) | A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [email](slots/email.md) | The email address of the author. |
| [En](slots/En.md) | Normal component of the field. |
| [end_date](slots/end_date.md) | End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SS±hh:mm for offset or YYYY-MM-DDTHH:MM:SSZ for UTC). |
| [EnL](slots/EnL.md) | Length-integrated normal component. |
| [Es](slots/Es.md) | Skew component of the field. |
| [EsL](slots/EsL.md) | Length-integrated skew component. |
| [eta_x](slots/eta_x.md) | Twiss dispersion parameter in the horizontal plane. May be any real value. |
| [eta_y](slots/eta_y.md) | Twiss dispersion parameter in the vertical plane. May be any real value. |
| [etap_x](slots/etap_x.md) | Twiss dispersion slope parameter in the horizontal plane. |
| [etap_y](slots/etap_y.md) | Twiss dispersion slope parameter in the vertical plane. |
| [facility](slots/facility.md) | A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc. |
| [facility_functions](slots/facility_functions.md) | The function of the supporting facility component,  which can be used to identify the component across different source systems. |
| [FloorP](slots/FloorP.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [frequency](slots/frequency.md) | RF frequency. |
| [functions](slots/functions.md) | The function of the component,  which can be used to identify the component across different source systems. |
| [g_actual](slots/g_actual.md) | Actual bend strength = 1/radius_actual |
| [g_ref](slots/g_ref.md) | Reference bend strength = 1/radius_ref |
| [h1](slots/h1.md) | Entrance end pole face curvature |
| [h2](slots/h2.md) | Exit end pole face curvature |
| [harmon](slots/harmon.md) | RF harmonic number. |
| [id](slots/id.md) | A unique identifier for the instance. |
| [identifier_type](slots/identifier_type.md) | The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK. |
| [identifier_value](slots/identifier_value.md) | The value of the identifier. |
| [identifiers](slots/identifiers.md) | A unique and ideally persistent identifier for the facility, such as a DOI or ROR. |
| [instance_version](slots/instance_version.md) | The version of the data instance that was changed. |
| [key](slots/key.md) | The metadata field name. |
| [kind](slots/kind.md) | The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor` (no prefix). |
| [Kn](slots/Kn.md) | Normalized normal component. |
| [Ks](slots/Ks.md) | Normalized skew component. |
| [Ksol](slots/Ksol.md) | Normalized solenoid strength. |
| [L_active](slots/L_active.md) | Active acceleration length. |
| [L_chord](slots/L_chord.md) | Chord length of the bend. |
| [L_rectangle](slots/L_rectangle.md) | Rectangular length. |
| [L_sagitta](slots/L_sagitta.md) | Output parameter. Sagitta length. |
| [label](slots/label.md) | A label string. |
| [length](slots/length.md) | Length of the element (arc length for bends). |
| [LongitudinalPlacementP](slots/LongitudinalPlacementP.md) | A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [mag_components](slots/mag_components.md) | Magnetic multipole components, one per order N. |
| [MagneticMultipoleP](slots/MagneticMultipoleP.md) | A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [MetaP](slots/MetaP.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [multipass](slots/multipass.md) | Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass. |
| [multipass_phase](slots/multipass_phase.md) | rad/2pi RF Phase added to multipass elements |
| [multipole_geometry](slots/multipole_geometry.md) | Multipole geometry type. Must be `follows_ref_geometry`. |
| [name](slots/name.md) | The name of the entity. For example, the name of the person or organization. |
| [native_data_type](slots/native_data_type.md) | The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean. |
| [native_description](slots/native_description.md) | A human-readable description of the signal in the source system. |
| [native_types](slots/native_types.md) | The native type of the component in the source system, which can be used to identify the component across different source systems. |
| [native_unit](slots/native_unit.md) | The native unit of the signal in the source system. |
| [notes](slots/notes.md) | Additional notes or comments about the representation of a particle accelerator and its operations. |
| [num_cells](slots/num_cells.md) | Number of cells in the cavity |
| [object](slots/object.md) |  |
| [orcid](slots/orcid.md) | The ORCID identifier of the author. |
| [order](slots/order.md) | Multipole order N (0 = dipole, 1 = quadrupole, etc.) |
| [pc_ref](slots/pc_ref.md) | [momentum*c] Reference momentum times speed of light. |
| [periodic](slots/periodic.md) | Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic. |
| [phase](slots/phase.md) | RF phase. rad/2pi RF phase in 0 to 2*pi |
| [phi](slots/phi.md) | Rotation around the X-axis in the facility floor plan. |
| [phi_a](slots/phi_a.md) | Twiss phase advance parameter in the horizontal plane. |
| [phi_b](slots/phi_b.md) | Twiss phase advance parameter in the vertical plane. |
| [phi_coord](slots/phi_coord.md) | The azimuthal angle in spherical coordinates (in radians). |
| [plane](slots/plane.md) | The transverse plane in which the kicker operates, either horizontal or vertical. |
| [predicate](slots/predicate.md) |  |
| [psi](slots/psi.md) | Rotation around the Z-axis in the facility floor plan. |
| [quantity_kind](slots/quantity_kind.md) | The physical quantity kind of the signal. |
| [r_coord](slots/r_coord.md) | The radial distance in cylindrical coordinates. |
| [ref_geometry](slots/ref_geometry.md) | Reference geometry type. Must be `arc`. |
| [reference_frame](slots/reference_frame.md) |  |
| [ReferenceP](slots/ReferenceP.md) | A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [repeat](slots/repeat.md) | Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.<br>If value is greater than 1, the beamline is repeated that many times. |
| [RFP](slots/RFP.md) | A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [rho_ref](slots/rho_ref.md) | Reference bend radius. |
| [s_position](slots/s_position.md) | Longitudinal position of the element along the beamline. |
| [schema_version](slots/schema_version.md) | Version of the schema used for this representation of a particle accelerator and its operations. Should follow the semantic versioning convention (MAJOR.MINOR.PATCH). Should match the schema version of the NARAD/PALS instance configuration schema being used. |
| [signal_bindings](slots/signal_bindings.md) | A list of signal bindings in the accelerator system (Component <-> Signal relationships). |
| [signal_role](slots/signal_role.md) | The role of the signal in the control system, such as setpoint, readback, status, command, or limit. |
| [signals](slots/signals.md) | A list of signals in the accelerator system. |
| [SolenoidP](slots/SolenoidP.md) | A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [source_system](slots/source_system.md) | The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service. |
| [species_ref](slots/species_ref.md) | A reference to a species or particle type, such as an ion, electron, or proton. |
| [start_date](slots/start_date.md) | Start date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DDTHH:MM:SS±hh:mm for offset or YYYY-MM-DDTHH:MM:SSZ for UTC). |
| [subject](slots/subject.md) |  |
| [summary](slots/summary.md) | A brief summary of the change. |
| [temporal_coverage](slots/temporal_coverage.md) | Temporal coverage for time-based datasets, if applicable. Container for elements describing the start_date and end_date of the data instance's temporal coverage  in ISO 8601 datetime format YYYY-MM-DDTHH:MM:SSZ±hh:mm (e.g., 2024-06-05T14:30:00-05:00). Use temporal_coverage when the dataset describes a specific historical or projected time period. This may not apply to simulations where temporal coverage of a specific facility during a specific time is not relevant. |
| [theta](slots/theta.md) | Orientation angle around the Y-axis in the facility floor plan. |
| [theta_coord](slots/theta_coord.md) | The angular coordinate in cylindrical coordinates (in radians). |
| [tilt](slots/tilt.md) | Tilt of the Nth multipole. |
| [tilt_ref](slots/tilt_ref.md) | Reference tilt of the bend. |
| [time_ref](slots/time_ref.md) | [s] Reference time |
| [tolerance_unit](slots/tolerance_unit.md) | Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship. |
| [tolerance_value](slots/tolerance_value.md) | Tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship. |
| [TwissP](slots/TwissP.md) | A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |
| [updated_date](slots/updated_date.md) | The date the data instance for the facility configuration was last updated, in ISO 8601 format (YYYY-MM-DD). Date of most recent update; revise on every change/version to the data instance, including minor edits and version updates.  This provides temporal context for the data instance and can be used for tracking its currency and maintenance. |
| [value](slots/value.md) | The metadata value, serialized as a string. |
| [version](slots/version.md) | Version of the representation of a particle accelerator and its operations. |
| [voltage](slots/voltage.md) | RF voltage. |
| [x](slots/x.md) | Global X coordinate in the facility floor plan. |
| [x_coord](slots/x_coord.md) | The x-coordinate in the specified coordinate system. |
| [x_offset](slots/x_offset.md) | Shift in the X direction in the facility floor plan. |
| [x_rot](slots/x_rot.md) | Rotation around the X-axis in the facility floor plan. |
| [y](slots/y.md) | Global Y coordinate in the facility floor plan. |
| [y_coord](slots/y_coord.md) | The y-coordinate in the specified coordinate system. |
| [y_offset](slots/y_offset.md) | Shift in the Y direction in the facility floor plan. |
| [y_rot](slots/y_rot.md) | Rotation around the Y-axis in the facility floor plan. |
| [z](slots/z.md) | Global Z coordinate in the facility floor plan. |
| [z_coord](slots/z_coord.md) | The z-coordinate in the specified coordinate system. |
| [z_offset](slots/z_offset.md) | Shift in the Z direction in the facility floor plan. |
| [z_rot](slots/z_rot.md) | Rotation around the Z-axis in the facility floor plan. |
| [zero_phase](slots/zero_phase.md) | Sets what phase = 0 means. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CanonicalSignalTypeEnum](enums/CanonicalSignalTypeEnum.md) | Portable semantic meanings for important signals. |
| [CavityTypeEnum](enums/CavityTypeEnum.md) | The type of cavity, which determines the field configuration and mode structure. |
| [CoordinateSystemEnum](enums/CoordinateSystemEnum.md) | Coordinate systems for spatial relationships. |
| [DataTypeEnum](enums/DataTypeEnum.md) | Data types for parameter values. |
| [DirectionEnum](enums/DirectionEnum.md) |  |
| [FacilityFunctionEnum](enums/FacilityFunctionEnum.md) | Broad structural or support functions. |
| [IdentifierTypeEnum](enums/IdentifierTypeEnum.md) | Controlled values for identifier types. |
| [MultipoleGeometryEnum](enums/MultipoleGeometryEnum.md) | The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles. |
| [PhysicalFunctionEnum](enums/PhysicalFunctionEnum.md) | Broad device-level functions. |
| [PhysicalRelationEnum](enums/PhysicalRelationEnum.md) | Controlled values for physical relation to the beamline. |
| [PlaneEnum](enums/PlaneEnum.md) | Controlled values for transverse plane. |
| [QuantityKindEnum](enums/QuantityKindEnum.md) | Physical quantity kinds for signals. |
| [ReferenceFrameEnum](enums/ReferenceFrameEnum.md) |  |
| [ReferenceGeometryEnum](enums/ReferenceGeometryEnum.md) | The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles. |
| [RelationContextEnum](enums/RelationContextEnum.md) |  |
| [SignalRoleEnum](enums/SignalRoleEnum.md) | Roles for control-system signals. |
| [SourceSystemEnum](enums/SourceSystemEnum.md) | Controlled values for facility-local source systems. |
| [UnitEnum](enums/UnitEnum.md) | Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available. |
| [VirtualFunctionEnum](enums/VirtualFunctionEnum.md) | Broad virtual component functions or roles. |
| [VirtualRelationEnum](enums/VirtualRelationEnum.md) | Controlled values for virtual relation to the beamline. |
| [ZeroPhaseEnum](enums/ZeroPhaseEnum.md) | The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity. |


## Types

| Type | Description |
| --- | --- |
| [Boolean](types/Boolean.md) | A binary (true or false) value |
| [Curie](types/Curie.md) | a compact URI |
| [Date](types/Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](types/DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](types/Datetime.md) | The combination of a date and time |
| [Decimal](types/Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](types/Double.md) | A real number that conforms to the xsd:double specification |
| [Float](types/Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](types/Integer.md) | An integer |
| [Iso8601Datetime](types/Iso8601Datetime.md) | Strict ISO 8601 date-time string allowing optional fractional seconds and timezones,  e.g., 2024-06-05T14:30:00-05:00 for June 5th, 2024 at 14:30:00 (2:30 PM) with UTC timezone offset -05:00 (America/New_York). |
| [Isodate](types/Isodate.md) | Strict ISO 8601 date string (YYYY-MM-DD). e.g., 2024-06-05 for June 5th, 2024. |
| [Jsonpath](types/Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](types/Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [Ncname](types/Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](types/Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [Objectidentifier](types/Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [Sparqlpath](types/Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](types/String.md) | A character string |
| [Time](types/Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](types/Uri.md) | a complete URI |
| [Uriorcurie](types/Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
