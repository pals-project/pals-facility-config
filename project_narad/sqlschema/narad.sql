-- # Class: NaradModel Description: Top-level NARAD document container.
--     * Slot: id
--     * Slot: narad_id
-- # Class: NaradConfig Description: NARAD configuration block containing the capability layer.
--     * Slot: id
--     * Slot: schema_version
--     * Slot: intent
--     * Slot: facility
--     * Slot: control_system
--     * Slot: capability_layer_id
--     * Slot: signal_layer_id Description: Signal-layer container for facility-specific signal bindings.
-- # Class: CapabilityLayer Description: Capability-layer container for profile families and a shared default graph projection.
--     * Slot: id
--     * Slot: default_graph_projection_id Description: The canonical graph projection for all profile families in this capability layer. Defines the full set of possible node labels (except device, which is derived from each family's device_domain) and the complete relationship vocabulary. Individual families may provide a graph_projection override when needed.
-- # Class: SignalLayer Description: Signal-layer container for facility-specific signal bindings.
--     * Slot: id
-- # Class: Facility Description: A facility with specific signal bindings.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: control_system
--     * Slot: naming_convention
--     * Slot: SignalLayer_id Description: Autocreated FK slot
--     * Slot: signal_definitions_id
-- # Class: SignalDefinitions Description: EPICS signal suffix templates keyed by device type or device domain. Use a domain-level key (e.g. Magnet, RFCavity) for signals shared across all types in that domain; use a device-type key (e.g. Quadrupole, BPM) for type-specific signals. New device types require no schema changes.
--     * Slot: id
-- # Class: SignalBinding Description: A named EPICS suffix definition for one semantic signal.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: epics_suffix Description: Facility-specific EPICS suffix for a semantic signal.
--     * Slot: description
--     * Slot: DeviceTypeSignalSet_name Description: Autocreated FK slot
-- # Class: DeviceTypeSignalSet Description: Signal binding set scoped to a device type (for example, Quadrupole or BPM).
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: SignalDefinitions_id Description: Autocreated FK slot
-- # Class: CapabilityMixin Description: Shared structure common to all capability types: a description and an ordered list of signals.
--     * Slot: id
--     * Slot: description
-- # Class: Signal Description: A named semantic signal used by a capability.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: role Description: The semantic role of the signal within its capability.
--     * Slot: data_type Description: The data type of the signal's value.
--     * Slot: units Description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
--     * Slot: units_uri Description: Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere, si-unit:MegaV-PER-M for MV/m, si-unit:T-M for T*m). The si-unit: prefix maps to http://qudt.org/vocab/unit/. Companion to the human-readable symbol in the units slot. Use the narad:CustomUnit for user-defined units not in QUDT; these should be defined in the graph projection with a narad:CustomUnit class and linked to signals via the units_uri slot.
--     * Slot: description
--     * Slot: CapabilityMixin_id Description: Autocreated FK slot
--     * Slot: Capability_name Description: Autocreated FK slot
--     * Slot: TypeSpecificCapability_id Description: Autocreated FK slot
-- # Class: Capability Description: A named, shared grouping of semantically related signals for a control aspect.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: description
--     * Slot: ControlProfileFamily_name Description: Autocreated FK slot
-- # Class: TypeSpecificCapability Description: An inline capability declared within a device-type profile, with its own identifier, a semantic class label, a description, and a list of signals. Distinct from the shared capabilities referenced by name; these are profile-local definitions.
--     * Slot: id Description: Unique identifier for the entity.
--     * Slot: capability_class Description: Semantic class label for a type-specific capability (e.g. QuadrupoleStrengthCapability). Serialized as 'class' in source YAML; renamed here to avoid conflict with reserved keywords.
--     * Slot: class_curie Description: Optional machine-resolvable URI or CURIE for a TypeSpecificCapability class. Use the narad: prefix for NARAD-defined classes (e.g. narad:QuadrupoleStrengthCapability), or any registered prefix for externally defined capability types. New capability classes can be introduced freely by using a suitable namespace.
--     * Slot: description
--     * Slot: CapabilityProfile_name Description: Autocreated FK slot
-- # Class: CapabilityProfile Description: A device-type profile that reuses shared capabilities and adds specific capabilities.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: device_type Description: The specific device type this capability profile targets (e.g. Quadrupole, Corrector, BPM). Uses ElementKindEnum to stay in sync with BeamlineElement.kind.
--     * Slot: description
--     * Slot: is_abstract Description: If true, this profile is a template or abstract definition not intended to be directly assigned to a beamline element. Concrete profiles that refine a template should set this to false (the default).
--     * Slot: ControlProfileFamily_name Description: Autocreated FK slot
-- # Class: NodeLabels Description: Static node-type label strings for the graph projection, covering all node categories except Device. The device label is derived from ControlProfileFamily.device_domain and need not be repeated here.
--     * Slot: id
--     * Slot: capability_family
--     * Slot: profile
--     * Slot: capability
--     * Slot: signal
-- # Class: GraphProjection Description: Graph projection metadata for node labels and edge categories.
--     * Slot: id
--     * Slot: node_labels_id Description: Node label mapping for the graph projection.
-- # Class: Relationship Description: A directed edge type in the NARAD graph projection, modelled after the OBO Relation Ontology (RO) ObjectProperty metamodel. Each relationship carries an identifier, human-readable label, natural-language description, and explicit domain/range node-type constraints.
--     * Slot: id Description: Unique identifier for the entity.
--     * Slot: domain Description: The node type that can appear as the subject (source) of this relationship.
--     * Slot: range Description: The node type that can appear as the object (target) of this relationship.
--     * Slot: inverse_of Description: The inverse relationship, if any.
--     * Slot: symmetric Description: True if the relation is symmetric: if A rel B then B rel A.
--     * Slot: transitive Description: True if the relation is transitive: if A rel B and B rel C then A rel C.
--     * Slot: asymmetric Description: True if the relation is asymmetric: if A rel B then NOT B rel A.
--     * Slot: irreflexive Description: True if no entity can stand in this relation to itself.
--     * Slot: GraphProjection_id Description: Autocreated FK slot
-- # Class: ControlProfileFamily Description: A reusable family of control profiles sharing common semantics and structure.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: device_domain Description: High-level device domain that this profile family governs.
--     * Slot: description
--     * Slot: CapabilityLayer_id Description: Autocreated FK slot
--     * Slot: graph_projection_id Description: Optional per-family graph projection override. If absent, the CapabilityLayer.default_graph_projection applies. Provide only when this family genuinely requires a different projection.
-- # Class: Identifier Description: A globally unique identifier for an entity (e.g., facility), with a specified type (e.g. DOI, ROR, ARK, local).
--     * Slot: id
--     * Slot: identifier_type Description: The type of identifier used in the identifier slot (e.g. DOI, ARK, URL, local).
--     * Slot: identifier_value Description: The value of the identifier (e.g. the DOI string, ARK string, URL string, or local ID).
-- # Class: AnyValue Description: Unconstrained type — accepts any YAML/JSON value (string, number, object, list, etc.).
--     * Slot: id
-- # Class: BeamlineElement Description: A single element in a beamline with optional physics parameter blocks.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: kind Description: Generic kind/type label. Used for Beamline entries (e.g. BeamLine). For ControlProfileFamily device domain use device_domain: DeviceDomainEnum. For CapabilityProfile device type use device_type: ElementKindEnum.
--     * Slot: length Description: Physical length of the element in meters.
--     * Slot: NaradModel_id Description: Autocreated FK slot
--     * Slot: RFP_id Description: RF cavity physics parameters block.
--     * Slot: BendP_id Description: Dipole/bend physics parameters block.
--     * Slot: MagneticMultipoleP_id Description: Magnetic multipole physics parameters block.
--     * Slot: SolenoidP_id Description: Solenoid physics parameters block.
--     * Slot: narad_id
--     * Slot: facility_params_id Description: Facility-specific element parameters block.
-- # Class: ElementNaradRef Description: NARAD semantic reference block attached to a beamline element.
--     * Slot: id
--     * Slot: capability_profile_family Description: Cross-reference to the control profile family for this element.
--     * Slot: capability_profile Description: Cross-reference to the specific capability profile applied to this element.
-- # Class: PVBinding Description: A concrete PV (Process Variable) binding for one semantic signal on a beamline element.
--     * Slot: name Description: Name/identifier of the entity.
--     * Slot: facility
--     * Slot: control_system
--     * Slot: pv Description: The EPICS Process Variable name (e.g. MBHK101H.S).
--     * Slot: ElementNaradRef_id Description: Autocreated FK slot
-- # Class: RFParams Description: RF cavity physics parameters (frequency, voltage, phase).
--     * Slot: id
--     * Slot: frequency Description: RF frequency in Hz.
--     * Slot: voltage Description: RF voltage in volts.
--     * Slot: phase Description: RF phase in degrees.
-- # Class: BendParams Description: Dipole/bend physics parameters (entry angle, exit edge angles).
--     * Slot: id
--     * Slot: angle_ref Description: Reference bend angle in radians.
--     * Slot: e1 Description: Entry edge angle in radians.
--     * Slot: e2 Description: Exit edge angle in radians.
-- # Class: MagneticMultipoleParams Description: Magnetic multipole physics parameters.
--     * Slot: id
--     * Slot: Kn1 Description: First-order magnetic multipole coefficient (quadrupole strength).
-- # Class: SolenoidParams Description: Solenoid physics parameters.
--     * Slot: id
--     * Slot: Ksol Description: Solenoid integrated field strength.
-- # Class: Beamline Description: An ordered sequence of beamline elements defining a beam path.
--     * Slot: beamline_name Description: Name of the beamline.
--     * Slot: kind Description: Generic kind/type label. Used for Beamline entries (e.g. BeamLine). For ControlProfileFamily device domain use device_domain: DeviceDomainEnum. For CapabilityProfile device type use device_type: ElementKindEnum.
--     * Slot: NaradModel_id Description: Autocreated FK slot
-- # Class: FacilityParams Description: Facility-specific element parameters: type designation, accelerator model name, and open property map.
--     * Slot: id
--     * Slot: facility_element_type Description: Facility-specific element type designation (e.g. WarmCavity, QW, HCorrector). named facility_element_type here to avoid conflict with the LinkML metamodel 'type' designator used for polymorphic class selection.
--     * Slot: modeled_as Description: Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).
--     * Slot: properties_id Description: Open-ended key-value property map for element-specific parameters.
-- # Class: Facility_identifier
--     * Slot: Facility_name Description: Autocreated FK slot
--     * Slot: identifier_id Description: Globally unique identifier for the facility, with specified type and value.
-- # Class: CapabilityProfile_inherits_shared_capabilities
--     * Slot: CapabilityProfile_name Description: Autocreated FK slot
--     * Slot: inherits_shared_capabilities_name Description: Shared capabilities inherited by this profile, cross-referenced by name. The validator checks that referenced names exist in the parent family's shared_capabilities.
-- # Class: Relationship_subproperty_of
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: subproperty_of_id Description: Parent relationships of which this is a more specific sub-relation.
-- # Class: Beamline_line
--     * Slot: Beamline_beamline_name Description: Autocreated FK slot
--     * Slot: line Description: Ordered sequence of cross-referenced element names forming a beamline.

CREATE TABLE "SignalLayer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SignalLayer_id" ON "SignalLayer" (id);
CREATE TABLE "SignalDefinitions" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SignalDefinitions_id" ON "SignalDefinitions" (id);
CREATE TABLE "CapabilityMixin" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CapabilityMixin_id" ON "CapabilityMixin" (id);
CREATE TABLE "NodeLabels" (
	id INTEGER NOT NULL,
	capability_family TEXT,
	profile TEXT,
	capability TEXT,
	signal TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NodeLabels_id" ON "NodeLabels" (id);
CREATE TABLE "Identifier" (
	id INTEGER NOT NULL,
	identifier_type VARCHAR(6),
	identifier_value TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Identifier_id" ON "Identifier" (id);
CREATE TABLE "AnyValue" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_AnyValue_id" ON "AnyValue" (id);
CREATE TABLE "RFParams" (
	id INTEGER NOT NULL,
	frequency FLOAT,
	voltage FLOAT,
	phase FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RFParams_id" ON "RFParams" (id);
CREATE TABLE "BendParams" (
	id INTEGER NOT NULL,
	angle_ref FLOAT,
	e1 FLOAT,
	e2 FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_BendParams_id" ON "BendParams" (id);
CREATE TABLE "MagneticMultipoleParams" (
	id INTEGER NOT NULL,
	"Kn1" FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MagneticMultipoleParams_id" ON "MagneticMultipoleParams" (id);
CREATE TABLE "SolenoidParams" (
	id INTEGER NOT NULL,
	"Ksol" FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SolenoidParams_id" ON "SolenoidParams" (id);
CREATE TABLE "Facility" (
	name TEXT NOT NULL,
	control_system TEXT,
	naming_convention TEXT,
	"SignalLayer_id" INTEGER,
	signal_definitions_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalLayer_id") REFERENCES "SignalLayer" (id),
	FOREIGN KEY(signal_definitions_id) REFERENCES "SignalDefinitions" (id)
);CREATE INDEX "ix_Facility_name" ON "Facility" (name);
CREATE TABLE "DeviceTypeSignalSet" (
	name TEXT NOT NULL,
	"SignalDefinitions_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("SignalDefinitions_id") REFERENCES "SignalDefinitions" (id)
);CREATE INDEX "ix_DeviceTypeSignalSet_name" ON "DeviceTypeSignalSet" (name);
CREATE TABLE "GraphProjection" (
	id INTEGER NOT NULL,
	node_labels_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(node_labels_id) REFERENCES "NodeLabels" (id)
);CREATE INDEX "ix_GraphProjection_id" ON "GraphProjection" (id);
CREATE TABLE "FacilityParams" (
	id INTEGER NOT NULL,
	facility_element_type TEXT,
	modeled_as TEXT,
	properties_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(properties_id) REFERENCES "AnyValue" (id)
);CREATE INDEX "ix_FacilityParams_id" ON "FacilityParams" (id);
CREATE TABLE "CapabilityLayer" (
	id INTEGER NOT NULL,
	default_graph_projection_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(default_graph_projection_id) REFERENCES "GraphProjection" (id)
);CREATE INDEX "ix_CapabilityLayer_id" ON "CapabilityLayer" (id);
CREATE TABLE "SignalBinding" (
	name TEXT NOT NULL,
	epics_suffix TEXT,
	description TEXT,
	"DeviceTypeSignalSet_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("DeviceTypeSignalSet_name") REFERENCES "DeviceTypeSignalSet" (name)
);CREATE INDEX "ix_SignalBinding_name" ON "SignalBinding" (name);
CREATE TABLE "Relationship" (
	id TEXT NOT NULL,
	domain VARCHAR(22),
	range VARCHAR(22) NOT NULL,
	inverse_of TEXT,
	symmetric BOOLEAN,
	transitive BOOLEAN,
	asymmetric BOOLEAN,
	irreflexive BOOLEAN,
	"GraphProjection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(inverse_of) REFERENCES "Relationship" (id),
	FOREIGN KEY("GraphProjection_id") REFERENCES "GraphProjection" (id)
);CREATE INDEX "ix_Relationship_id" ON "Relationship" (id);
CREATE TABLE "Facility_identifier" (
	"Facility_name" TEXT,
	identifier_id INTEGER,
	PRIMARY KEY ("Facility_name", identifier_id),
	FOREIGN KEY("Facility_name") REFERENCES "Facility" (name),
	FOREIGN KEY(identifier_id) REFERENCES "Identifier" (id)
);CREATE INDEX "ix_Facility_identifier_Facility_name" ON "Facility_identifier" ("Facility_name");CREATE INDEX "ix_Facility_identifier_identifier_id" ON "Facility_identifier" (identifier_id);
CREATE TABLE "NaradConfig" (
	id INTEGER NOT NULL,
	schema_version TEXT,
	intent TEXT,
	facility TEXT,
	control_system TEXT,
	capability_layer_id INTEGER,
	signal_layer_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(capability_layer_id) REFERENCES "CapabilityLayer" (id),
	FOREIGN KEY(signal_layer_id) REFERENCES "SignalLayer" (id)
);CREATE INDEX "ix_NaradConfig_id" ON "NaradConfig" (id);
CREATE TABLE "ControlProfileFamily" (
	name TEXT NOT NULL,
	device_domain VARCHAR(10),
	description TEXT,
	"CapabilityLayer_id" INTEGER,
	graph_projection_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("CapabilityLayer_id") REFERENCES "CapabilityLayer" (id),
	FOREIGN KEY(graph_projection_id) REFERENCES "GraphProjection" (id)
);CREATE INDEX "ix_ControlProfileFamily_name" ON "ControlProfileFamily" (name);
CREATE TABLE "Relationship_subproperty_of" (
	"Relationship_id" TEXT,
	subproperty_of_id TEXT,
	PRIMARY KEY ("Relationship_id", subproperty_of_id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY(subproperty_of_id) REFERENCES "Relationship" (id)
);CREATE INDEX "ix_Relationship_subproperty_of_subproperty_of_id" ON "Relationship_subproperty_of" (subproperty_of_id);CREATE INDEX "ix_Relationship_subproperty_of_Relationship_id" ON "Relationship_subproperty_of" ("Relationship_id");
CREATE TABLE "NaradModel" (
	id INTEGER NOT NULL,
	narad_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(narad_id) REFERENCES "NaradConfig" (id)
);CREATE INDEX "ix_NaradModel_id" ON "NaradModel" (id);
CREATE TABLE "Capability" (
	name TEXT NOT NULL,
	description TEXT,
	"ControlProfileFamily_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlProfileFamily_name") REFERENCES "ControlProfileFamily" (name)
);CREATE INDEX "ix_Capability_name" ON "Capability" (name);
CREATE TABLE "CapabilityProfile" (
	name TEXT NOT NULL,
	device_type VARCHAR(10),
	description TEXT,
	is_abstract BOOLEAN,
	"ControlProfileFamily_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("ControlProfileFamily_name") REFERENCES "ControlProfileFamily" (name)
);CREATE INDEX "ix_CapabilityProfile_name" ON "CapabilityProfile" (name);
CREATE TABLE "TypeSpecificCapability" (
	id TEXT NOT NULL,
	capability_class TEXT,
	class_curie TEXT,
	description TEXT,
	"CapabilityProfile_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapabilityProfile_name") REFERENCES "CapabilityProfile" (name)
);CREATE INDEX "ix_TypeSpecificCapability_id" ON "TypeSpecificCapability" (id);
CREATE TABLE "ElementNaradRef" (
	id INTEGER NOT NULL,
	capability_profile_family TEXT,
	capability_profile TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(capability_profile_family) REFERENCES "ControlProfileFamily" (name),
	FOREIGN KEY(capability_profile) REFERENCES "CapabilityProfile" (name)
);CREATE INDEX "ix_ElementNaradRef_id" ON "ElementNaradRef" (id);
CREATE TABLE "Beamline" (
	beamline_name TEXT NOT NULL,
	kind TEXT,
	"NaradModel_id" INTEGER,
	PRIMARY KEY (beamline_name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id)
);CREATE INDEX "ix_Beamline_beamline_name" ON "Beamline" (beamline_name);
CREATE TABLE "CapabilityProfile_inherits_shared_capabilities" (
	"CapabilityProfile_name" TEXT,
	inherits_shared_capabilities_name TEXT,
	PRIMARY KEY ("CapabilityProfile_name", inherits_shared_capabilities_name),
	FOREIGN KEY("CapabilityProfile_name") REFERENCES "CapabilityProfile" (name),
	FOREIGN KEY(inherits_shared_capabilities_name) REFERENCES "Capability" (name)
);CREATE INDEX "ix_CapabilityProfile_inherits_shared_capabilities_CapabilityProfile_name" ON "CapabilityProfile_inherits_shared_capabilities" ("CapabilityProfile_name");CREATE INDEX "ix_CapabilityProfile_inherits_shared_capabilities_inherits_shared_capabilities_name" ON "CapabilityProfile_inherits_shared_capabilities" (inherits_shared_capabilities_name);
CREATE TABLE "Signal" (
	name TEXT NOT NULL,
	role VARCHAR(10),
	data_type VARCHAR(16),
	units TEXT,
	units_uri TEXT,
	description TEXT,
	"CapabilityMixin_id" INTEGER,
	"Capability_name" TEXT,
	"TypeSpecificCapability_id" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("CapabilityMixin_id") REFERENCES "CapabilityMixin" (id),
	FOREIGN KEY("Capability_name") REFERENCES "Capability" (name),
	FOREIGN KEY("TypeSpecificCapability_id") REFERENCES "TypeSpecificCapability" (id)
);CREATE INDEX "ix_Signal_name" ON "Signal" (name);
CREATE TABLE "BeamlineElement" (
	name TEXT NOT NULL,
	kind VARCHAR(10),
	length FLOAT,
	"NaradModel_id" INTEGER,
	"RFP_id" INTEGER,
	"BendP_id" INTEGER,
	"MagneticMultipoleP_id" INTEGER,
	"SolenoidP_id" INTEGER,
	narad_id INTEGER,
	facility_params_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("NaradModel_id") REFERENCES "NaradModel" (id),
	FOREIGN KEY("RFP_id") REFERENCES "RFParams" (id),
	FOREIGN KEY("BendP_id") REFERENCES "BendParams" (id),
	FOREIGN KEY("MagneticMultipoleP_id") REFERENCES "MagneticMultipoleParams" (id),
	FOREIGN KEY("SolenoidP_id") REFERENCES "SolenoidParams" (id),
	FOREIGN KEY(narad_id) REFERENCES "ElementNaradRef" (id),
	FOREIGN KEY(facility_params_id) REFERENCES "FacilityParams" (id)
);CREATE INDEX "ix_BeamlineElement_name" ON "BeamlineElement" (name);
CREATE TABLE "PVBinding" (
	name TEXT NOT NULL,
	facility TEXT,
	control_system TEXT,
	pv TEXT,
	"ElementNaradRef_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("ElementNaradRef_id") REFERENCES "ElementNaradRef" (id)
);CREATE INDEX "ix_PVBinding_name" ON "PVBinding" (name);
CREATE TABLE "Beamline_line" (
	"Beamline_beamline_name" TEXT,
	line TEXT,
	PRIMARY KEY ("Beamline_beamline_name", line),
	FOREIGN KEY("Beamline_beamline_name") REFERENCES "Beamline" (beamline_name)
);CREATE INDEX "ix_Beamline_line_Beamline_beamline_name" ON "Beamline_line" ("Beamline_beamline_name");CREATE INDEX "ix_Beamline_line_line" ON "Beamline_line" (line);
