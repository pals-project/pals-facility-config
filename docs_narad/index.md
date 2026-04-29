# narad

NARAD extension for capability-layer semantics and facility-specific signal bindings

URI: https://w3id.org/narad_linkml/schema/narad/

Name: narad



## Classes

| Class | Description |
| --- | --- |
| [AnyValue](AnyValue.md) | Unconstrained type — accepts any YAML/JSON value (string, number, object, lis... |
| [Beamline](Beamline.md) | An ordered sequence of beamline elements defining a beam path |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |
| [BendParams](BendParams.md) | Dipole/bend physics parameters (entry angle, exit edge angles) |
| [Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect |
| [CapabilityLayer](CapabilityLayer.md) | Capability-layer container for profile families and a shared default graph pr... |
| [CapabilityMixin](CapabilityMixin.md) | Shared structure common to all capability types: a description and an ordered... |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |
| [DeviceTypeSignalSet](DeviceTypeSignalSet.md) | Signal binding set scoped to a device type (for example, Quadrupole or BPM) |
| [ElementNaradRef](ElementNaradRef.md) | NARAD semantic reference block attached to a beamline element |
| [Facility](Facility.md) | A facility with specific signal bindings |
| [FacilityParams](FacilityParams.md) | Facility-specific element parameters: type designation, accelerator model nam... |
| [GraphProjection](GraphProjection.md) | Graph projection metadata for node labels and edge categories |
| [Identifier](Identifier.md) | A globally unique identifier for an entity (e |
| [MagneticMultipoleParams](MagneticMultipoleParams.md) | Magnetic multipole physics parameters |
| [NaradConfig](NaradConfig.md) | NARAD configuration block containing the capability layer |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |
| [NodeLabels](NodeLabels.md) | Static node-type label strings for the graph projection, covering all node ca... |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |
| [Relationship](Relationship.md) | A directed edge type in the NARAD graph projection, modelled after the OBO Re... |
| [RFParams](RFParams.md) | RF cavity physics parameters (frequency, voltage, phase) |
| [Signal](Signal.md) | A named semantic signal used by a capability |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |
| [SignalDefinitions](SignalDefinitions.md) | EPICS signal suffix templates keyed by device type or device domain |
| [SignalLayer](SignalLayer.md) | Signal-layer container for facility-specific signal bindings |
| [SolenoidParams](SolenoidParams.md) | Solenoid physics parameters |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |



## Slots

| Slot | Description |
| --- | --- |
| [angle_ref](angle_ref.md) | Reference bend angle in radians |
| [asymmetric](asymmetric.md) | True if the relation is asymmetric: if A rel B then NOT B rel A |
| [beamline_name](beamline_name.md) | Name of the beamline |
| [beamlines](beamlines.md) | Beamlines — open structure to accommodate the list-of-named-dict serializatio... |
| [BendP](BendP.md) | Dipole/bend physics parameters block |
| [capability](capability.md) |  |
| [capability_class](capability_class.md) | Semantic class label for a type-specific capability (e |
| [capability_family](capability_family.md) |  |
| [capability_layer](capability_layer.md) |  |
| [capability_profile](capability_profile.md) | Cross-reference to the specific capability profile applied to this element |
| [capability_profile_family](capability_profile_family.md) | Cross-reference to the control profile family for this element |
| [cavity_semantics](cavity_semantics.md) | Deprecated — capabilities are now derived from capability_profile |
| [class_curie](class_curie.md) | Optional machine-resolvable URI or CURIE for a TypeSpecificCapability class |
| [control_system](control_system.md) |  |
| [data_type](data_type.md) | The data type of the signal's value |
| [default_graph_projection](default_graph_projection.md) | The canonical graph projection for all profile families in this capability la... |
| [description](description.md) |  |
| [device_domain](device_domain.md) | High-level device domain that this profile family governs |
| [device_type](device_type.md) | The specific device type this capability profile targets (e |
| [domain](domain.md) | The node type that can appear as the subject (source) of this relationship |
| [e1](e1.md) | Entry edge angle in radians |
| [e2](e2.md) | Exit edge angle in radians |
| [elements](elements.md) | Beamline element definitions (referenced by name from beamline line sequences... |
| [epics_suffix](epics_suffix.md) | Facility-specific EPICS suffix for a semantic signal |
| [facilities](facilities.md) | Facility identifiers for facility-specific signal bindings |
| [facility](facility.md) |  |
| [facility_element_type](facility_element_type.md) | Facility-specific element type designation (e |
| [facility_params](facility_params.md) | Facility-specific element parameters block |
| [frequency](frequency.md) | RF frequency in Hz |
| [graph_projection](graph_projection.md) | Optional graph projection metadata attached to a profile family |
| [id](id.md) | Unique identifier for the entity |
| [identifier](identifier.md) | Globally unique identifier for the facility, with specified type and value |
| [identifier_type](identifier_type.md) | The type of identifier used in the identifier slot (e |
| [identifier_value](identifier_value.md) | The value of the identifier (e |
| [inherits_shared_capabilities](inherits_shared_capabilities.md) | Shared capabilities inherited by this profile, cross-referenced by name |
| [instrument_semantics](instrument_semantics.md) | Deprecated — capabilities are now derived from capability_profile |
| [intent](intent.md) |  |
| [inverse_of](inverse_of.md) | The inverse relationship, if any |
| [irreflexive](irreflexive.md) | True if no entity can stand in this relation to itself |
| [is_abstract](is_abstract.md) | If true, this profile is a template or abstract definition not intended to be... |
| [kind](kind.md) | Generic kind/type label |
| [Kn1](Kn1.md) | First-order magnetic multipole coefficient (quadrupole strength) |
| [Ksol](Ksol.md) | Solenoid integrated field strength |
| [label](label.md) | Human-readable label for the relationship (e |
| [length](length.md) | Physical length of the element in meters |
| [line](line.md) | Ordered sequence of cross-referenced element names forming a beamline |
| [magnet_semantics](magnet_semantics.md) | Deprecated — capabilities are now derived from capability_profile |
| [MagneticMultipoleP](MagneticMultipoleP.md) | Magnetic multipole physics parameters block |
| [modeled_as](modeled_as.md) | Accelerator physics code model element type (e |
| [name](name.md) | Name/identifier of the entity |
| [naming_convention](naming_convention.md) |  |
| [narad](narad.md) |  |
| [node_labels](node_labels.md) | Node label mapping for the graph projection |
| [phase](phase.md) | RF phase in degrees |
| [profile](profile.md) |  |
| [profiles](profiles.md) | Control profile families keyed by family name |
| [properties](properties.md) | Open-ended key-value property map for element-specific parameters |
| [pv](pv.md) | The EPICS Process Variable name (e |
| [range](range.md) | The node type that can appear as the object (target) of this relationship |
| [relationships](relationships.md) | Relationship definitions used in the graph projection |
| [RFP](RFP.md) | RF cavity physics parameters block |
| [role](role.md) | The semantic role of the signal within its capability |
| [schema_version](schema_version.md) |  |
| [shared_capabilities](shared_capabilities.md) | Named shared capabilities reused by profile types in a family |
| [signal](signal.md) |  |
| [signal_bindings](signal_bindings.md) | Signal definitions keyed by signal name within a device type |
| [signal_definitions](signal_definitions.md) |  |
| [signal_layer](signal_layer.md) | Signal-layer container for facility-specific signal bindings |
| [signals](signals.md) | Signals within a capability |
| [SolenoidP](SolenoidP.md) | Solenoid physics parameters block |
| [subproperty_of](subproperty_of.md) | Parent relationships of which this is a more specific sub-relation |
| [symmetric](symmetric.md) | True if the relation is symmetric: if A rel B then B rel A |
| [transitive](transitive.md) | True if the relation is transitive: if A rel B and B rel C then A rel C |
| [type_profiles](type_profiles.md) | Device-type profile definitions for this family, keyed by profile name |
| [type_signal_sets](type_signal_sets.md) | Signal suffix groups keyed by device type or device domain name |
| [type_specific_capabilities](type_specific_capabilities.md) | Type-specific capabilities declared directly in a profile, each with an id, c... |
| [units](units.md) | Conventional unit symbol (e |
| [units_uri](units_uri.md) | Machine-resolvable QUDT unit reference (e |
| [voltage](voltage.md) | RF voltage in volts |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DataTypeEnum](DataTypeEnum.md) | Allowed data types for signal values |
| [DeviceDomainEnum](DeviceDomainEnum.md) | High-level device domain for a control profile family |
| [ElementKindEnum](ElementKindEnum.md) | Controlled vocabulary for beamline element types, shared between the capabili... |
| [IdentifierTypeEnum](IdentifierTypeEnum.md) | Allowed identifier types for facilities and other entities |
| [NodeTypeEnum](NodeTypeEnum.md) | Node types in the NARAD graph projection; used as domain/range values for Rel... |
| [RelationshipTypeEnum](RelationshipTypeEnum.md) | Allowed relationship types in the NARAD graph projection; each corresponds to... |
| [SignalRoleEnum](SignalRoleEnum.md) | Controlled vocabulary for the semantic role of a signal within a capability |


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
