# Auto generated from narad.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-10-19T16:06:21
# Schema: accelerator_core
#
# id: https://w3id.org/accelerator-core
# description: A lightweight LinkML schema for facility-agnostic accelerator components, their beamline relationships, and associated control-system signals.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
ACC = CurieNamespace('acc', 'https://example.org/accelerator-core/')
INST = CurieNamespace('inst', 'https://example.org/pals-instance/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
PALS = CurieNamespace('pals', 'https://pals-project.readthedocs.io/')
QUANTITYKIND = CurieNamespace('quantitykind', 'http://qudt.org/vocab/quantitykind/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SAREF = CurieNamespace('saref', 'https://saref.etsi.org/core/v4.1.1/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN_SYSTEM = CurieNamespace('ssn_system', 'https://www.w3.org/ns/ssn/systems/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = PALS


# Types

# Class references
class NodeId(extended_str):
    pass


class AffiliationId(extended_str):
    pass


class ParamGroupId(extended_str):
    pass


class MetaParamGroupId(ParamGroupId):
    pass


class FloorParamGroupId(ParamGroupId):
    pass


class BodyShiftParamGroupId(ParamGroupId):
    pass


class LongitudinalPlacementParamGroupId(ParamGroupId):
    pass


class ReferenceParamGroupId(ParamGroupId):
    pass


class SolenoidParamGroupId(ParamGroupId):
    pass


class TwissParamGroupId(ParamGroupId):
    pass


class RFParamGroupId(ParamGroupId):
    pass


class ElectricMultipoleParamGroupId(ParamGroupId):
    pass


class MagneticMultipoleParamGroupId(ParamGroupId):
    pass


class BendParamGroupId(ParamGroupId):
    pass


class ComponentId(NodeId):
    pass


class PhysicalComponentId(ComponentId):
    pass


class VirtualComponentId(ComponentId):
    pass


class BeamLineId(VirtualComponentId):
    pass


class SignalId(NodeId):
    pass


class MagnetId(PhysicalComponentId):
    pass


class SolenoidId(MagnetId):
    pass


class MultipoleId(MagnetId):
    pass


class BendId(MultipoleId):
    pass


class QuadrupoleId(MultipoleId):
    pass


class OctupoleId(MultipoleId):
    pass


class SextupoleId(MultipoleId):
    pass


class KickerId(MagnetId):
    pass


class ACKickerId(KickerId):
    pass


class DiagnosticDeviceId(PhysicalComponentId):
    pass


class BeamProfileMonitorId(DiagnosticDeviceId):
    pass


class BeamPositionMonitorId(DiagnosticDeviceId):
    pass


class ApertureId(DiagnosticDeviceId):
    pass


class RadiationMonitorId(DiagnosticDeviceId):
    pass


class CavityId(PhysicalComponentId):
    pass


class CrabCavityId(CavityId):
    pass


class RFCavityId(CavityId):
    pass


class NormalConductingRFCavityId(RFCavityId):
    pass


class SuperConductingRFCavityId(RFCavityId):
    pass


class SupportingFacilityComponentId(PhysicalComponentId):
    pass


class BookkeepingComponentId(VirtualComponentId):
    pass


class MarkerId(BookkeepingComponentId):
    pass


class BeginningEleId(BookkeepingComponentId):
    pass


class DriftId(VirtualComponentId):
    pass


class BeamLineSectionId(BookkeepingComponentId):
    pass


class EdgeId(extended_str):
    pass


class SignalBindingId(EdgeId):
    pass


class HasSignalId(SignalBindingId):
    pass


class HasSetpointSignalId(SignalBindingId):
    pass


class HasReadbackSignalId(SignalBindingId):
    pass


class HasCommandSignalId(SignalBindingId):
    pass


class HasLimitSignalId(SignalBindingId):
    pass


class ComponentRelationId(EdgeId):
    pass


class PrecedesId(ComponentRelationId):
    pass


class ContainsId(ComponentRelationId):
    pass


class ControlsId(ComponentRelationId):
    pass


class IsPartOfId(ComponentRelationId):
    pass


class AdjacentToId(ComponentRelationId):
    pass


class OverlapsId(ComponentRelationId):
    pass


class HasConnectingBranchId(ComponentRelationId):
    pass


class MountedOnId(ComponentRelationId):
    pass


class IntersectsId(ComponentRelationId):
    pass


class NearestToId(ComponentRelationId):
    pass


@dataclass(repr=False)
class Node(YAMLRoot):
    """
    Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges
    (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common
    ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the
    ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Node"]
    class_class_curie: ClassVar[str] = "pals:Node"
    class_name: ClassVar[str] = "Node"
    class_model_uri: ClassVar[URIRef] = PALS.Node

    id: Union[str, NodeId] = None
    kind: str = None
    alias: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeId):
            self.id = NodeId(self.id)

        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, str) else str(v) for v in self.alias]

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "kind"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class PALSAccelerator(YAMLRoot):
    """
    Root container for accelerator core components, semantic signals, and local bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["PALSAccelerator"]
    class_class_curie: ClassVar[str] = "pals:PALSAccelerator"
    class_name: ClassVar[str] = "PALSAccelerator"
    class_model_uri: ClassVar[URIRef] = PALS.PALSAccelerator

    kind: str = None
    description: Optional[str] = None
    affiliation: Optional[Union[dict, "Affiliation"]] = None
    version: Optional[str] = None
    authors: Optional[Union[Union[dict, "Author"], list[Union[dict, "Author"]]]] = empty_list()
    notes: Optional[Union[str, list[str]]] = empty_list()
    facility: Optional[Union[dict, "Facility"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.affiliation is not None and not isinstance(self.affiliation, Affiliation):
            self.affiliation = Affiliation(**as_dict(self.affiliation))

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, Author) else Author(**as_dict(v)) for v in self.authors]

        if not isinstance(self.notes, list):
            self.notes = [self.notes] if self.notes is not None else []
        self.notes = [v if isinstance(v, str) else str(v) for v in self.notes]

        if self.facility is not None and not isinstance(self.facility, Facility):
            self.facility = Facility(**as_dict(self.facility))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Author(YAMLRoot):
    """
    Contains authorship information for a representation of an accelerator facility and its operations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Author"]
    class_class_curie: ClassVar[str] = "pals:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = PALS.Author

    name: Optional[str] = None
    affiliation: Optional[Union[dict, "Affiliation"]] = None
    email: Optional[str] = None
    orcid: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.affiliation is not None and not isinstance(self.affiliation, Affiliation):
            self.affiliation = Affiliation(**as_dict(self.affiliation))

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Facility(YAMLRoot):
    """
    A facility that houses one or more accelerators.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Facility"]
    class_class_curie: ClassVar[str] = "pals:Facility"
    class_name: ClassVar[str] = "Facility"
    class_model_uri: ClassVar[URIRef] = PALS.Facility

    identifiers: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    components: Optional[Union[dict[Union[str, ComponentId], Union[dict, "Component"]], list[Union[dict, "Component"]]]] = empty_dict()
    beamlines: Optional[Union[dict[Union[str, BeamLineId], Union[dict, "BeamLine"]], list[Union[dict, "BeamLine"]]]] = empty_dict()
    signals: Optional[Union[dict[Union[str, SignalId], Union[dict, "Signal"]], list[Union[dict, "Signal"]]]] = empty_dict()
    signal_bindings: Optional[Union[dict[Union[str, SignalBindingId], Union[dict, "SignalBinding"]], list[Union[dict, "SignalBinding"]]]] = empty_dict()
    component_relations: Optional[Union[dict[Union[str, ComponentRelationId], Union[dict, "ComponentRelation"]], list[Union[dict, "ComponentRelation"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.identifiers, list):
            self.identifiers = [self.identifiers] if self.identifiers is not None else []
        self.identifiers = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.identifiers]

        self._normalize_inlined_as_list(slot_name="components", slot_type=Component, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="beamlines", slot_type=BeamLine, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signal_bindings", slot_type=SignalBinding, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="component_relations", slot_type=ComponentRelation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Affiliation(YAMLRoot):
    """
    Contains affiliation information for an author or component, such as a ROR.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Affiliation"]
    class_class_curie: ClassVar[str] = "pals:Affiliation"
    class_name: ClassVar[str] = "Affiliation"
    class_model_uri: ClassVar[URIRef] = PALS.Affiliation

    id: Union[str, AffiliationId] = None
    name: Optional[str] = None
    identifiers: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AffiliationId):
            self.id = AffiliationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.identifiers, list):
            self.identifiers = [self.identifiers] if self.identifiers is not None else []
        self.identifiers = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.identifiers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifier(YAMLRoot):
    """
    A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Identifier"]
    class_class_curie: ClassVar[str] = "pals:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = PALS.Identifier

    identifier_type: Optional[Union[str, "IdentifierTypeEnum"]] = None
    identifier_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.identifier_type is not None and not isinstance(self.identifier_type, IdentifierTypeEnum):
            self.identifier_type = IdentifierTypeEnum(self.identifier_type)

        if self.identifier_value is not None and not isinstance(self.identifier_value, str):
            self.identifier_value = str(self.identifier_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParamGroup(YAMLRoot):
    """
    Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable
    node/IRI rather than a blank node when exported to RDF.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["ParamGroup"]
    class_class_curie: ClassVar[str] = "pals:ParamGroup"
    class_name: ClassVar[str] = "ParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.ParamGroup

    id: Union[str, ParamGroupId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParamGroupId):
            self.id = ParamGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasMetaP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasMetaP"]
    class_class_curie: ClassVar[str] = "pals:HasMetaP"
    class_name: ClassVar[str] = "HasMetaP"
    class_model_uri: ClassVar[URIRef] = PALS.HasMetaP

    MetaP: Optional[Union[dict, "MetaParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.MetaP is not None and not isinstance(self.MetaP, MetaParamGroup):
            self.MetaP = MetaParamGroup(**as_dict(self.MetaP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetaParamGroup(ParamGroup):
    """
    Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability
    with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["MetaParamGroup"]
    class_class_curie: ClassVar[str] = "pals:MetaParamGroup"
    class_name: ClassVar[str] = "MetaParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.MetaParamGroup

    id: Union[str, MetaParamGroupId] = None
    description: Optional[str] = None
    alias: Optional[Union[str, list[str]]] = empty_list()
    label: Optional[str] = None
    additional_metadata: Optional[Union[Union[dict, "AdditionalMetadata"], list[Union[dict, "AdditionalMetadata"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetaParamGroupId):
            self.id = MetaParamGroupId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, str) else str(v) for v in self.alias]

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        self._normalize_inlined_as_list(slot_name="additional_metadata", slot_type=AdditionalMetadata, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasFloorP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasFloorP"]
    class_class_curie: ClassVar[str] = "pals:HasFloorP"
    class_name: ClassVar[str] = "HasFloorP"
    class_model_uri: ClassVar[URIRef] = PALS.HasFloorP

    FloorP: Optional[Union[dict, "FloorParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.FloorP is not None and not isinstance(self.FloorP, FloorParamGroup):
            self.FloorP = FloorParamGroup(**as_dict(self.FloorP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FloorParamGroup(ParamGroup):
    """
    Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for
    interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["FloorParamGroup"]
    class_class_curie: ClassVar[str] = "pals:FloorParamGroup"
    class_name: ClassVar[str] = "FloorParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.FloorParamGroup

    id: Union[str, FloorParamGroupId] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    theta: Optional[float] = None
    phi: Optional[float] = None
    psi: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FloorParamGroupId):
            self.id = FloorParamGroupId(self.id)

        if self.x is not None and not isinstance(self.x, float):
            self.x = float(self.x)

        if self.y is not None and not isinstance(self.y, float):
            self.y = float(self.y)

        if self.z is not None and not isinstance(self.z, float):
            self.z = float(self.z)

        if self.theta is not None and not isinstance(self.theta, float):
            self.theta = float(self.theta)

        if self.phi is not None and not isinstance(self.phi, float):
            self.phi = float(self.phi)

        if self.psi is not None and not isinstance(self.psi, float):
            self.psi = float(self.psi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasBodyShiftP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasBodyShiftP"]
    class_class_curie: ClassVar[str] = "pals:HasBodyShiftP"
    class_name: ClassVar[str] = "HasBodyShiftP"
    class_model_uri: ClassVar[URIRef] = PALS.HasBodyShiftP

    BodyShiftP: Optional[Union[dict, "BodyShiftParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BodyShiftParamGroup(ParamGroup):
    """
    Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)
    for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BodyShiftParamGroup"]
    class_class_curie: ClassVar[str] = "pals:BodyShiftParamGroup"
    class_name: ClassVar[str] = "BodyShiftParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.BodyShiftParamGroup

    id: Union[str, BodyShiftParamGroupId] = None
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BodyShiftParamGroupId):
            self.id = BodyShiftParamGroupId(self.id)

        if self.x_offset is not None and not isinstance(self.x_offset, float):
            self.x_offset = float(self.x_offset)

        if self.y_offset is not None and not isinstance(self.y_offset, float):
            self.y_offset = float(self.y_offset)

        if self.z_offset is not None and not isinstance(self.z_offset, float):
            self.z_offset = float(self.z_offset)

        if self.x_rot is not None and not isinstance(self.x_rot, float):
            self.x_rot = float(self.x_rot)

        if self.y_rot is not None and not isinstance(self.y_rot, float):
            self.y_rot = float(self.y_rot)

        if self.z_rot is not None and not isinstance(self.z_rot, float):
            self.z_rot = float(self.z_rot)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasLongitudinalPlacementP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasLongitudinalPlacementP"]
    class_class_curie: ClassVar[str] = "pals:HasLongitudinalPlacementP"
    class_name: ClassVar[str] = "HasLongitudinalPlacementP"
    class_model_uri: ClassVar[URIRef] = PALS.HasLongitudinalPlacementP

    LongitudinalPlacementP: Optional[Union[dict, "LongitudinalPlacementParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.LongitudinalPlacementP is not None and not isinstance(self.LongitudinalPlacementP, LongitudinalPlacementParamGroup):
            self.LongitudinalPlacementP = LongitudinalPlacementParamGroup(**as_dict(self.LongitudinalPlacementP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LongitudinalPlacementParamGroup(ParamGroup):
    """
    Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. Corresponds to
    PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be
    present.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["LongitudinalPlacementParamGroup"]
    class_class_curie: ClassVar[str] = "pals:LongitudinalPlacementParamGroup"
    class_name: ClassVar[str] = "LongitudinalPlacementParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.LongitudinalPlacementParamGroup

    id: Union[str, LongitudinalPlacementParamGroupId] = None
    length: Optional[float] = None
    s_position: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LongitudinalPlacementParamGroupId):
            self.id = LongitudinalPlacementParamGroupId(self.id)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.s_position is not None and not isinstance(self.s_position, float):
            self.s_position = float(self.s_position)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasReferenceP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasReferenceP"]
    class_class_curie: ClassVar[str] = "pals:HasReferenceP"
    class_name: ClassVar[str] = "HasReferenceP"
    class_model_uri: ClassVar[URIRef] = PALS.HasReferenceP

    ReferenceP: Optional[Union[dict, "ReferenceParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceParamGroup(ParamGroup):
    """
    Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability
    with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["ReferenceParamGroup"]
    class_class_curie: ClassVar[str] = "pals:ReferenceParamGroup"
    class_name: ClassVar[str] = "ReferenceParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.ReferenceParamGroup

    id: Union[str, ReferenceParamGroupId] = None
    species_ref: Optional[str] = None
    pc_ref: Optional[float] = None
    E_tot_ref: Optional[float] = None
    time_ref: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceParamGroupId):
            self.id = ReferenceParamGroupId(self.id)

        if self.species_ref is not None and not isinstance(self.species_ref, str):
            self.species_ref = str(self.species_ref)

        if self.pc_ref is not None and not isinstance(self.pc_ref, float):
            self.pc_ref = float(self.pc_ref)

        if self.E_tot_ref is not None and not isinstance(self.E_tot_ref, float):
            self.E_tot_ref = float(self.E_tot_ref)

        if self.time_ref is not None and not isinstance(self.time_ref, float):
            self.time_ref = float(self.time_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasSolenoidP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasSolenoidP"]
    class_class_curie: ClassVar[str] = "pals:HasSolenoidP"
    class_name: ClassVar[str] = "HasSolenoidP"
    class_model_uri: ClassVar[URIRef] = PALS.HasSolenoidP

    SolenoidP: Optional[Union[dict, "SolenoidParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.SolenoidP is not None and not isinstance(self.SolenoidP, SolenoidParamGroup):
            self.SolenoidP = SolenoidParamGroup(**as_dict(self.SolenoidP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolenoidParamGroup(ParamGroup):
    """
    Mixin for solenoid-specific parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["SolenoidParamGroup"]
    class_class_curie: ClassVar[str] = "pals:SolenoidParamGroup"
    class_name: ClassVar[str] = "SolenoidParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.SolenoidParamGroup

    id: Union[str, SolenoidParamGroupId] = None
    Ksol: Optional[float] = None
    Bsol: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolenoidParamGroupId):
            self.id = SolenoidParamGroupId(self.id)

        if self.Ksol is not None and not isinstance(self.Ksol, float):
            self.Ksol = float(self.Ksol)

        if self.Bsol is not None and not isinstance(self.Bsol, float):
            self.Bsol = float(self.Bsol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasTwissP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasTwissP"]
    class_class_curie: ClassVar[str] = "pals:HasTwissP"
    class_name: ClassVar[str] = "HasTwissP"
    class_model_uri: ClassVar[URIRef] = PALS.HasTwissP

    TwissP: Optional[Union[dict, "TwissParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TwissParamGroup(ParamGroup):
    """
    Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["TwissParamGroup"]
    class_class_curie: ClassVar[str] = "pals:TwissParamGroup"
    class_name: ClassVar[str] = "TwissParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.TwissParamGroup

    id: Union[str, TwissParamGroupId] = None
    alpha_a: Optional[float] = None
    alpha_b: Optional[float] = None
    beta_a: Optional[float] = None
    beta_b: Optional[float] = None
    cmat11: Optional[float] = None
    cmat12: Optional[float] = None
    cmat21: Optional[float] = None
    cmat22: Optional[float] = None
    eta_x: Optional[float] = None
    eta_y: Optional[float] = None
    etap_x: Optional[float] = None
    etap_y: Optional[float] = None
    deta_x_ds: Optional[float] = None
    deta_y_ds: Optional[float] = None
    phi_a: Optional[float] = None
    phi_b: Optional[float] = None
    dbeta_a_dpz: Optional[float] = None
    dalpha_a_dpz: Optional[float] = None
    dbeta_b_dpz: Optional[float] = None
    dalpha_b_dpz: Optional[float] = None
    deta_x_dpz: Optional[float] = None
    detap_x_dpz: Optional[float] = None
    deta_y_dpz: Optional[float] = None
    detap_y_dpz: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TwissParamGroupId):
            self.id = TwissParamGroupId(self.id)

        if self.alpha_a is not None and not isinstance(self.alpha_a, float):
            self.alpha_a = float(self.alpha_a)

        if self.alpha_b is not None and not isinstance(self.alpha_b, float):
            self.alpha_b = float(self.alpha_b)

        if self.beta_a is not None and not isinstance(self.beta_a, float):
            self.beta_a = float(self.beta_a)

        if self.beta_b is not None and not isinstance(self.beta_b, float):
            self.beta_b = float(self.beta_b)

        if self.cmat11 is not None and not isinstance(self.cmat11, float):
            self.cmat11 = float(self.cmat11)

        if self.cmat12 is not None and not isinstance(self.cmat12, float):
            self.cmat12 = float(self.cmat12)

        if self.cmat21 is not None and not isinstance(self.cmat21, float):
            self.cmat21 = float(self.cmat21)

        if self.cmat22 is not None and not isinstance(self.cmat22, float):
            self.cmat22 = float(self.cmat22)

        if self.eta_x is not None and not isinstance(self.eta_x, float):
            self.eta_x = float(self.eta_x)

        if self.eta_y is not None and not isinstance(self.eta_y, float):
            self.eta_y = float(self.eta_y)

        if self.etap_x is not None and not isinstance(self.etap_x, float):
            self.etap_x = float(self.etap_x)

        if self.etap_y is not None and not isinstance(self.etap_y, float):
            self.etap_y = float(self.etap_y)

        if self.deta_x_ds is not None and not isinstance(self.deta_x_ds, float):
            self.deta_x_ds = float(self.deta_x_ds)

        if self.deta_y_ds is not None and not isinstance(self.deta_y_ds, float):
            self.deta_y_ds = float(self.deta_y_ds)

        if self.phi_a is not None and not isinstance(self.phi_a, float):
            self.phi_a = float(self.phi_a)

        if self.phi_b is not None and not isinstance(self.phi_b, float):
            self.phi_b = float(self.phi_b)

        if self.dbeta_a_dpz is not None and not isinstance(self.dbeta_a_dpz, float):
            self.dbeta_a_dpz = float(self.dbeta_a_dpz)

        if self.dalpha_a_dpz is not None and not isinstance(self.dalpha_a_dpz, float):
            self.dalpha_a_dpz = float(self.dalpha_a_dpz)

        if self.dbeta_b_dpz is not None and not isinstance(self.dbeta_b_dpz, float):
            self.dbeta_b_dpz = float(self.dbeta_b_dpz)

        if self.dalpha_b_dpz is not None and not isinstance(self.dalpha_b_dpz, float):
            self.dalpha_b_dpz = float(self.dalpha_b_dpz)

        if self.deta_x_dpz is not None and not isinstance(self.deta_x_dpz, float):
            self.deta_x_dpz = float(self.deta_x_dpz)

        if self.detap_x_dpz is not None and not isinstance(self.detap_x_dpz, float):
            self.detap_x_dpz = float(self.detap_x_dpz)

        if self.deta_y_dpz is not None and not isinstance(self.deta_y_dpz, float):
            self.deta_y_dpz = float(self.deta_y_dpz)

        if self.detap_y_dpz is not None and not isinstance(self.detap_y_dpz, float):
            self.detap_y_dpz = float(self.detap_y_dpz)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasRFP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasRFP"]
    class_class_curie: ClassVar[str] = "pals:HasRFP"
    class_name: ClassVar[str] = "HasRFP"
    class_model_uri: ClassVar[URIRef] = PALS.HasRFP

    RFP: Optional[Union[dict, "RFParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.RFP is not None and not isinstance(self.RFP, RFParamGroup):
            self.RFP = RFParamGroup(**as_dict(self.RFP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RFParamGroup(ParamGroup):
    """
    Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is
    aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["RFParamGroup"]
    class_class_curie: ClassVar[str] = "pals:RFParamGroup"
    class_name: ClassVar[str] = "RFParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.RFParamGroup

    id: Union[str, RFParamGroupId] = None
    frequency: Optional[float] = None
    harmon: Optional[int] = None
    voltage: Optional[float] = None
    gradient: Optional[float] = None
    phase: Optional[float] = None
    multipass_phase: Optional[float] = None
    cavity_type: Optional[Union[str, "CavityTypeEnum"]] = None
    num_cells: Optional[int] = None
    zero_phase: Optional[Union[str, "ZeroPhaseEnum"]] = None
    L_active: Optional[float] = None
    dE_ref: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RFParamGroupId):
            self.id = RFParamGroupId(self.id)

        if self.frequency is not None and not isinstance(self.frequency, float):
            self.frequency = float(self.frequency)

        if self.harmon is not None and not isinstance(self.harmon, int):
            self.harmon = int(self.harmon)

        if self.voltage is not None and not isinstance(self.voltage, float):
            self.voltage = float(self.voltage)

        if self.gradient is not None and not isinstance(self.gradient, float):
            self.gradient = float(self.gradient)

        if self.phase is not None and not isinstance(self.phase, float):
            self.phase = float(self.phase)

        if self.multipass_phase is not None and not isinstance(self.multipass_phase, float):
            self.multipass_phase = float(self.multipass_phase)

        if self.cavity_type is not None and not isinstance(self.cavity_type, CavityTypeEnum):
            self.cavity_type = CavityTypeEnum(self.cavity_type)

        if self.num_cells is not None and not isinstance(self.num_cells, int):
            self.num_cells = int(self.num_cells)

        if self.zero_phase is not None and not isinstance(self.zero_phase, ZeroPhaseEnum):
            self.zero_phase = ZeroPhaseEnum(self.zero_phase)

        if self.L_active is not None and not isinstance(self.L_active, float):
            self.L_active = float(self.L_active)

        if self.dE_ref is not None and not isinstance(self.dE_ref, float):
            self.dE_ref = float(self.dE_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasElectricMultipoleP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasElectricMultipoleP"]
    class_class_curie: ClassVar[str] = "pals:HasElectricMultipoleP"
    class_name: ClassVar[str] = "HasElectricMultipoleP"
    class_model_uri: ClassVar[URIRef] = PALS.HasElectricMultipoleP

    ElectricMultipoleP: Optional[Union[dict, "ElectricMultipoleParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ElectricMultipoleP is not None and not isinstance(self.ElectricMultipoleP, ElectricMultipoleParamGroup):
            self.ElectricMultipoleP = ElectricMultipoleParamGroup(**as_dict(self.ElectricMultipoleP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectricMultipoleParamGroup(ParamGroup):
    """
    Mixin for electric multipole parameters, which can be used to describe the electric field components of an
    accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle
    Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components:
    - order: 7
    tilt: 0.7
    - order: 3
    En: 27.3
    - order: 2
    EnL: 3.47e1
    ```
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["ElectricMultipoleParamGroup"]
    class_class_curie: ClassVar[str] = "pals:ElectricMultipoleParamGroup"
    class_name: ClassVar[str] = "ElectricMultipoleParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.ElectricMultipoleParamGroup

    id: Union[str, ElectricMultipoleParamGroupId] = None
    elec_components: Optional[Union[Union[dict, "MultipoleParameterGroup"], list[Union[dict, "MultipoleParameterGroup"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElectricMultipoleParamGroupId):
            self.id = ElectricMultipoleParamGroupId(self.id)

        self._normalize_inlined_as_list(slot_name="elec_components", slot_type=MultipoleParameterGroup, key_name="order", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasMagneticMultipoleP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasMagneticMultipoleP"]
    class_class_curie: ClassVar[str] = "pals:HasMagneticMultipoleP"
    class_name: ClassVar[str] = "HasMagneticMultipoleP"
    class_model_uri: ClassVar[URIRef] = PALS.HasMagneticMultipoleP

    MagneticMultipoleP: Optional[Union[dict, "MagneticMultipoleParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.MagneticMultipoleP is not None and not isinstance(self.MagneticMultipoleP, MagneticMultipoleParamGroup):
            self.MagneticMultipoleP = MagneticMultipoleParamGroup(**as_dict(self.MagneticMultipoleP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MagneticMultipoleParamGroup(ParamGroup):
    """
    Mixin for magnetic multipole parameters, which can be used to describe the magnetic field components of an
    accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle
    Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: -
    order: 7
    tilt: 0.7
    - order: 3
    Bn: 27.3
    - order: 2
    BnL: 3.47e1
    - order: 1
    Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength
    ```
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["MagneticMultipoleParamGroup"]
    class_class_curie: ClassVar[str] = "pals:MagneticMultipoleParamGroup"
    class_name: ClassVar[str] = "MagneticMultipoleParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.MagneticMultipoleParamGroup

    id: Union[str, MagneticMultipoleParamGroupId] = None
    mag_components: Optional[Union[Union[dict, "MultipoleParameterGroup"], list[Union[dict, "MultipoleParameterGroup"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MagneticMultipoleParamGroupId):
            self.id = MagneticMultipoleParamGroupId(self.id)

        self._normalize_inlined_as_list(slot_name="mag_components", slot_type=MultipoleParameterGroup, key_name="order", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasBendP(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["HasBendP"]
    class_class_curie: ClassVar[str] = "pals:HasBendP"
    class_name: ClassVar[str] = "HasBendP"
    class_model_uri: ClassVar[URIRef] = PALS.HasBendP

    BendP: Optional[Union[dict, "BendParamGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.BendP is not None and not isinstance(self.BendP, BendParamGroup):
            self.BendP = BendParamGroup(**as_dict(self.BendP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BendParamGroup(ParamGroup):
    """
    Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This
    mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BendParamGroup"]
    class_class_curie: ClassVar[str] = "pals:BendParamGroup"
    class_name: ClassVar[str] = "BendParamGroup"
    class_model_uri: ClassVar[URIRef] = PALS.BendParamGroup

    id: Union[str, BendParamGroupId] = None
    angle_ref: Optional[float] = None
    Bn0_ref: Optional[float] = None
    bend_field_actual: Optional[float] = None
    e1: Optional[float] = None
    e2: Optional[float] = None
    e1_rect: Optional[float] = None
    e2_rect: Optional[float] = None
    edge1_int: Optional[float] = None
    edge2_int: Optional[float] = None
    g_ref: Optional[float] = None
    g_actual: Optional[float] = None
    h1: Optional[float] = None
    h2: Optional[float] = None
    Kn0_from_g_ref: Optional[Union[bool, Bool]] = None
    L_chord: Optional[float] = None
    L_sagitta: Optional[float] = None
    L_rectangle: Optional[float] = None
    multipole_geometry: Optional[Union[str, "MultipoleGeometryEnum"]] = None
    ref_geometry: Optional[Union[str, "ReferenceGeometryEnum"]] = None
    radius_ref: Optional[float] = None
    tilt_ref: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BendParamGroupId):
            self.id = BendParamGroupId(self.id)

        if self.angle_ref is not None and not isinstance(self.angle_ref, float):
            self.angle_ref = float(self.angle_ref)

        if self.Bn0_ref is not None and not isinstance(self.Bn0_ref, float):
            self.Bn0_ref = float(self.Bn0_ref)

        if self.bend_field_actual is not None and not isinstance(self.bend_field_actual, float):
            self.bend_field_actual = float(self.bend_field_actual)

        if self.e1 is not None and not isinstance(self.e1, float):
            self.e1 = float(self.e1)

        if self.e2 is not None and not isinstance(self.e2, float):
            self.e2 = float(self.e2)

        if self.e1_rect is not None and not isinstance(self.e1_rect, float):
            self.e1_rect = float(self.e1_rect)

        if self.e2_rect is not None and not isinstance(self.e2_rect, float):
            self.e2_rect = float(self.e2_rect)

        if self.edge1_int is not None and not isinstance(self.edge1_int, float):
            self.edge1_int = float(self.edge1_int)

        if self.edge2_int is not None and not isinstance(self.edge2_int, float):
            self.edge2_int = float(self.edge2_int)

        if self.g_ref is not None and not isinstance(self.g_ref, float):
            self.g_ref = float(self.g_ref)

        if self.g_actual is not None and not isinstance(self.g_actual, float):
            self.g_actual = float(self.g_actual)

        if self.h1 is not None and not isinstance(self.h1, float):
            self.h1 = float(self.h1)

        if self.h2 is not None and not isinstance(self.h2, float):
            self.h2 = float(self.h2)

        if self.Kn0_from_g_ref is not None and not isinstance(self.Kn0_from_g_ref, Bool):
            self.Kn0_from_g_ref = Bool(self.Kn0_from_g_ref)

        if self.L_chord is not None and not isinstance(self.L_chord, float):
            self.L_chord = float(self.L_chord)

        if self.L_sagitta is not None and not isinstance(self.L_sagitta, float):
            self.L_sagitta = float(self.L_sagitta)

        if self.L_rectangle is not None and not isinstance(self.L_rectangle, float):
            self.L_rectangle = float(self.L_rectangle)

        if self.multipole_geometry is not None and not isinstance(self.multipole_geometry, MultipoleGeometryEnum):
            self.multipole_geometry = MultipoleGeometryEnum(self.multipole_geometry)

        if self.ref_geometry is not None and not isinstance(self.ref_geometry, ReferenceGeometryEnum):
            self.ref_geometry = ReferenceGeometryEnum(self.ref_geometry)

        if self.radius_ref is not None and not isinstance(self.radius_ref, float):
            self.radius_ref = float(self.radius_ref)

        if self.tilt_ref is not None and not isinstance(self.tilt_ref, float):
            self.tilt_ref = float(self.tilt_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultipoleParameterGroup(YAMLRoot):
    """
    A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles OR the
    fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the
    ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["MultipoleParameterGroup"]
    class_class_curie: ClassVar[str] = "pals:MultipoleParameterGroup"
    class_name: ClassVar[str] = "MultipoleParameterGroup"
    class_model_uri: ClassVar[URIRef] = PALS.MultipoleParameterGroup

    order: int = None
    tilt: Optional[float] = None
    En: Optional[float] = None
    Es: Optional[float] = None
    EnL: Optional[float] = None
    EsL: Optional[float] = None
    Bn: Optional[float] = None
    Bs: Optional[float] = None
    BnL: Optional[float] = None
    BsL: Optional[float] = None
    Kn: Optional[float] = None
    Ks: Optional[float] = None
    KnL: Optional[float] = None
    KsL: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.tilt is not None and not isinstance(self.tilt, float):
            self.tilt = float(self.tilt)

        if self.En is not None and not isinstance(self.En, float):
            self.En = float(self.En)

        if self.Es is not None and not isinstance(self.Es, float):
            self.Es = float(self.Es)

        if self.EnL is not None and not isinstance(self.EnL, float):
            self.EnL = float(self.EnL)

        if self.EsL is not None and not isinstance(self.EsL, float):
            self.EsL = float(self.EsL)

        if self.Bn is not None and not isinstance(self.Bn, float):
            self.Bn = float(self.Bn)

        if self.Bs is not None and not isinstance(self.Bs, float):
            self.Bs = float(self.Bs)

        if self.BnL is not None and not isinstance(self.BnL, float):
            self.BnL = float(self.BnL)

        if self.BsL is not None and not isinstance(self.BsL, float):
            self.BsL = float(self.BsL)

        if self.Kn is not None and not isinstance(self.Kn, float):
            self.Kn = float(self.Kn)

        if self.Ks is not None and not isinstance(self.Ks, float):
            self.Ks = float(self.Ks)

        if self.KnL is not None and not isinstance(self.KnL, float):
            self.KnL = float(self.KnL)

        if self.KsL is not None and not isinstance(self.KsL, float):
            self.KsL = float(self.KsL)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Component(Node):
    """
    A general class for accelerator components, which can be specialized into more specific types like
    AcceleratorDevice, Magnet, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Component"]
    class_class_curie: ClassVar[str] = "pals:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = PALS.Component

    id: Union[str, ComponentId] = None
    kind: str = None
    native_types: Optional[Union[str, list[str]]] = empty_list()
    MetaP: Optional[Union[dict, MetaParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.native_types, list):
            self.native_types = [self.native_types] if self.native_types is not None else []
        self.native_types = [v if isinstance(v, str) else str(v) for v in self.native_types]

        if self.MetaP is not None and not isinstance(self.MetaP, MetaParamGroup):
            self.MetaP = MetaParamGroup(**as_dict(self.MetaP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class PhysicalComponent(Component):
    """
    A physical item that participates in or supports accelerator operation. This can be used to capture physical
    components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding
    the structure and function of the accelerator system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["PhysicalComponent"]
    class_class_curie: ClassVar[str] = "pals:PhysicalComponent"
    class_name: ClassVar[str] = "PhysicalComponent"
    class_model_uri: ClassVar[URIRef] = PALS.PhysicalComponent

    id: Union[str, PhysicalComponentId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    FloorP: Optional[Union[dict, FloorParamGroup]] = None
    LongitudinalPlacementP: Optional[Union[dict, LongitudinalPlacementParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.functions):
            self.MissingRequiredField("functions")
        if not isinstance(self.functions, list):
            self.functions = [self.functions] if self.functions is not None else []
        self.functions = [v if isinstance(v, PhysicalFunctionEnum) else PhysicalFunctionEnum(v) for v in self.functions]

        if self._is_empty(self.beamline_relation):
            self.MissingRequiredField("beamline_relation")
        if not isinstance(self.beamline_relation, PhysicalRelationEnum):
            self.beamline_relation = PhysicalRelationEnum(self.beamline_relation)

        if self.FloorP is not None and not isinstance(self.FloorP, FloorParamGroup):
            self.FloorP = FloorParamGroup(**as_dict(self.FloorP))

        if self.LongitudinalPlacementP is not None and not isinstance(self.LongitudinalPlacementP, LongitudinalPlacementParamGroup):
            self.LongitudinalPlacementP = LongitudinalPlacementParamGroup(**as_dict(self.LongitudinalPlacementP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class VirtualComponent(Component):
    """
    A virtual or logical component that represents a concept, function, or role in the accelerator beamline operation
    but does not have a physical instantiation. This can be used to capture abstract components, such as Markers,
    BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the
    accelerator system but are not physical devices.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["VirtualComponent"]
    class_class_curie: ClassVar[str] = "pals:VirtualComponent"
    class_name: ClassVar[str] = "VirtualComponent"
    class_model_uri: ClassVar[URIRef] = PALS.VirtualComponent

    id: Union[str, VirtualComponentId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    FloorP: Optional[Union[dict, FloorParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.functions):
            self.MissingRequiredField("functions")
        if not isinstance(self.functions, list):
            self.functions = [self.functions] if self.functions is not None else []
        self.functions = [v if isinstance(v, VirtualFunctionEnum) else VirtualFunctionEnum(v) for v in self.functions]

        if self._is_empty(self.beamline_relation):
            self.MissingRequiredField("beamline_relation")
        if not isinstance(self.beamline_relation, VirtualRelationEnum):
            self.beamline_relation = VirtualRelationEnum(self.beamline_relation)

        if self.FloorP is not None and not isinstance(self.FloorP, FloorParamGroup):
            self.FloorP = FloorParamGroup(**as_dict(self.FloorP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class BeamLine(VirtualComponent):
    """
    PALS element for an ordered sequence of beamline elements defining a beam path.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BeamLine"]
    class_class_curie: ClassVar[str] = "pals:BeamLine"
    class_name: ClassVar[str] = "BeamLine"
    class_model_uri: ClassVar[URIRef] = PALS.BeamLine

    id: Union[str, BeamLineId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    length: Optional[float] = None
    description: Optional[str] = None
    multipass: Optional[Union[bool, Bool]] = None
    periodic: Optional[Union[bool, Bool]] = None
    repeat: Optional[int] = None
    direction: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamLineId):
            self.id = BeamLineId(self.id)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.multipass is not None and not isinstance(self.multipass, Bool):
            self.multipass = Bool(self.multipass)

        if self.periodic is not None and not isinstance(self.periodic, Bool):
            self.periodic = Bool(self.periodic)

        if self.repeat is not None and not isinstance(self.repeat, int):
            self.repeat = int(self.repeat)

        if self.direction is not None and not isinstance(self.direction, int):
            self.direction = int(self.direction)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Signal(Node):
    """
    Semantic meaning of a control-system signal associated with a component.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Signal"]
    class_class_curie: ClassVar[str] = "pals:Signal"
    class_name: ClassVar[str] = "Signal"
    class_model_uri: ClassVar[URIRef] = PALS.Signal

    id: Union[str, SignalId] = None
    kind: str = None
    signal_role: Union[str, "SignalRoleEnum"] = None
    source_system: Union[str, "SourceSystemEnum"] = None
    canonical_signal_type: Union[str, "CanonicalSignalTypeEnum"] = None
    quantity_kind: Union[str, "QuantityKindEnum"] = None
    native_data_type: Union[str, "DataTypeEnum"] = None
    native_unit: Union[str, "UnitEnum"] = None
    native_description: Optional[str] = None
    access_protocol: Optional[str] = None
    archive_identifier: Optional[str] = None
    MetaP: Optional[Union[dict, MetaParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignalId):
            self.id = SignalId(self.id)

        if self._is_empty(self.signal_role):
            self.MissingRequiredField("signal_role")
        if not isinstance(self.signal_role, SignalRoleEnum):
            self.signal_role = SignalRoleEnum(self.signal_role)

        if self._is_empty(self.source_system):
            self.MissingRequiredField("source_system")
        if not isinstance(self.source_system, SourceSystemEnum):
            self.source_system = SourceSystemEnum(self.source_system)

        if self._is_empty(self.canonical_signal_type):
            self.MissingRequiredField("canonical_signal_type")
        if not isinstance(self.canonical_signal_type, CanonicalSignalTypeEnum):
            self.canonical_signal_type = CanonicalSignalTypeEnum(self.canonical_signal_type)

        if self._is_empty(self.quantity_kind):
            self.MissingRequiredField("quantity_kind")
        if not isinstance(self.quantity_kind, QuantityKindEnum):
            self.quantity_kind = QuantityKindEnum(self.quantity_kind)

        if self._is_empty(self.native_data_type):
            self.MissingRequiredField("native_data_type")
        if not isinstance(self.native_data_type, DataTypeEnum):
            self.native_data_type = DataTypeEnum(self.native_data_type)

        if self._is_empty(self.native_unit):
            self.MissingRequiredField("native_unit")
        if not isinstance(self.native_unit, UnitEnum):
            self.native_unit = UnitEnum(self.native_unit)

        if self.native_description is not None and not isinstance(self.native_description, str):
            self.native_description = str(self.native_description)

        if self.access_protocol is not None and not isinstance(self.access_protocol, str):
            self.access_protocol = str(self.access_protocol)

        if self.archive_identifier is not None and not isinstance(self.archive_identifier, str):
            self.archive_identifier = str(self.archive_identifier)

        if self.MetaP is not None and not isinstance(self.MetaP, MetaParamGroup):
            self.MetaP = MetaParamGroup(**as_dict(self.MetaP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Magnet(PhysicalComponent):
    """
    An accelerator device that produces a magnetic field for beam control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Magnet"]
    class_class_curie: ClassVar[str] = "pals:Magnet"
    class_name: ClassVar[str] = "Magnet"
    class_model_uri: ClassVar[URIRef] = PALS.Magnet

    id: Union[str, MagnetId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    ReferenceP: Optional[Union[dict, ReferenceParamGroup]] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Solenoid(Magnet):
    """
    A magnet with a primarily longitudinal magnetic field used for focusing.
    A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic
    axis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Solenoid"]
    class_class_curie: ClassVar[str] = "pals:Solenoid"
    class_name: ClassVar[str] = "Solenoid"
    class_model_uri: ClassVar[URIRef] = PALS.Solenoid

    id: Union[str, SolenoidId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    SolenoidP: Optional[Union[dict, SolenoidParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolenoidId):
            self.id = SolenoidId(self.id)

        if self.SolenoidP is not None and not isinstance(self.SolenoidP, SolenoidParamGroup):
            self.SolenoidP = SolenoidParamGroup(**as_dict(self.SolenoidP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Multipole(Magnet):
    """
    A general magnet with a higher-order multipole field, such as a sextupole or octupole.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Multipole"]
    class_class_curie: ClassVar[str] = "pals:Multipole"
    class_name: ClassVar[str] = "Multipole"
    class_model_uri: ClassVar[URIRef] = PALS.Multipole

    id: Union[str, MultipoleId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    ElectricMultipoleP: Optional[Union[dict, ElectricMultipoleParamGroup]] = None
    MagneticMultipoleP: Optional[Union[dict, MagneticMultipoleParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MultipoleId):
            self.id = MultipoleId(self.id)

        if self.ElectricMultipoleP is not None and not isinstance(self.ElectricMultipoleP, ElectricMultipoleParamGroup):
            self.ElectricMultipoleP = ElectricMultipoleParamGroup(**as_dict(self.ElectricMultipoleP))

        if self.MagneticMultipoleP is not None and not isinstance(self.MagneticMultipoleP, MagneticMultipoleParamGroup):
            self.MagneticMultipoleP = MagneticMultipoleParamGroup(**as_dict(self.MagneticMultipoleP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Bend(Multipole):
    """
    Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical
    elements is that with a Bend the curvilinear coordinate system is an arc with finite curvature and for the other
    elements the curvilinear coordinate system is straight.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Bend"]
    class_class_curie: ClassVar[str] = "pals:Bend"
    class_name: ClassVar[str] = "Bend"
    class_model_uri: ClassVar[URIRef] = PALS.Bend

    id: Union[str, BendId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    BendP: Optional[Union[dict, BendParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BendId):
            self.id = BendId(self.id)

        if self.BendP is not None and not isinstance(self.BendP, BendParamGroup):
            self.BendP = BendParamGroup(**as_dict(self.BendP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Quadrupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 4 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Quadrupole"]
    class_class_curie: ClassVar[str] = "pals:Quadrupole"
    class_name: ClassVar[str] = "Quadrupole"
    class_model_uri: ClassVar[URIRef] = PALS.Quadrupole

    id: Union[str, QuadrupoleId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuadrupoleId):
            self.id = QuadrupoleId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Octupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 8 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Octupole"]
    class_class_curie: ClassVar[str] = "pals:Octupole"
    class_name: ClassVar[str] = "Octupole"
    class_model_uri: ClassVar[URIRef] = PALS.Octupole

    id: Union[str, OctupoleId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OctupoleId):
            self.id = OctupoleId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Sextupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 6 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Sextupole"]
    class_class_curie: ClassVar[str] = "pals:Sextupole"
    class_name: ClassVar[str] = "Sextupole"
    class_model_uri: ClassVar[URIRef] = PALS.Sextupole

    id: Union[str, SextupoleId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SextupoleId):
            self.id = SextupoleId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Kicker(Magnet):
    """
    A magnet primarily used to steer the beam.
    Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the
    kicker.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Kicker"]
    class_class_curie: ClassVar[str] = "pals:Kicker"
    class_name: ClassVar[str] = "Kicker"
    class_model_uri: ClassVar[URIRef] = PALS.Kicker

    id: Union[str, KickerId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    plane: Optional[Union[str, "PlaneEnum"]] = None
    ElectricMultipoleP: Optional[Union[dict, ElectricMultipoleParamGroup]] = None
    MagneticMultipoleP: Optional[Union[dict, MagneticMultipoleParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KickerId):
            self.id = KickerId(self.id)

        if self.plane is not None and not isinstance(self.plane, PlaneEnum):
            self.plane = PlaneEnum(self.plane)

        if self.ElectricMultipoleP is not None and not isinstance(self.ElectricMultipoleP, ElectricMultipoleParamGroup):
            self.ElectricMultipoleP = ElectricMultipoleParamGroup(**as_dict(self.ElectricMultipoleP))

        if self.MagneticMultipoleP is not None and not isinstance(self.MagneticMultipoleP, MagneticMultipoleParamGroup):
            self.MagneticMultipoleP = MagneticMultipoleParamGroup(**as_dict(self.MagneticMultipoleP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class ACKicker(Kicker):
    """
    An ACKicker element simulates a time-dependent kicker. It is like a Kicker element except that the field varies in
    time. This element requires a user supplied time-dependent expression.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["ACKicker"]
    class_class_curie: ClassVar[str] = "pals:ACKicker"
    class_name: ClassVar[str] = "ACKicker"
    class_model_uri: ClassVar[URIRef] = PALS.ACKicker

    id: Union[str, ACKickerId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ACKickerId):
            self.id = ACKickerId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class DiagnosticDevice(PhysicalComponent):
    """
    An accelerator device used to measure beam or machine state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["DiagnosticDevice"]
    class_class_curie: ClassVar[str] = "pals:DiagnosticDevice"
    class_name: ClassVar[str] = "DiagnosticDevice"
    class_model_uri: ClassVar[URIRef] = PALS.DiagnosticDevice

    id: Union[str, DiagnosticDeviceId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiagnosticDeviceId):
            self.id = DiagnosticDeviceId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class BeamProfileMonitor(DiagnosticDevice):
    """
    A diagnostic device used to measure transverse beam profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BeamProfileMonitor"]
    class_class_curie: ClassVar[str] = "pals:BeamProfileMonitor"
    class_name: ClassVar[str] = "BeamProfileMonitor"
    class_model_uri: ClassVar[URIRef] = PALS.BeamProfileMonitor

    id: Union[str, BeamProfileMonitorId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    ReferenceP: Optional[Union[dict, ReferenceParamGroup]] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamProfileMonitorId):
            self.id = BeamProfileMonitorId(self.id)

        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class BeamPositionMonitor(DiagnosticDevice):
    """
    A diagnostic device used to measure transverse beam position.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BeamPositionMonitor"]
    class_class_curie: ClassVar[str] = "pals:BeamPositionMonitor"
    class_name: ClassVar[str] = "BeamPositionMonitor"
    class_model_uri: ClassVar[URIRef] = PALS.BeamPositionMonitor

    id: Union[str, BeamPositionMonitorId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    ReferenceP: Optional[Union[dict, ReferenceParamGroup]] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamPositionMonitorId):
            self.id = BeamPositionMonitorId(self.id)

        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Aperture(DiagnosticDevice):
    """
    A diagnostic or limiting aperture element used to constrain or characterize beam passage.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Aperture"]
    class_class_curie: ClassVar[str] = "pals:Aperture"
    class_name: ClassVar[str] = "Aperture"
    class_model_uri: ClassVar[URIRef] = PALS.Aperture

    id: Union[str, ApertureId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    ReferenceP: Optional[Union[dict, ReferenceParamGroup]] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApertureId):
            self.id = ApertureId(self.id)

        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class RadiationMonitor(DiagnosticDevice):
    """
    A diagnostic device used to monitor radiation dose or dose rate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["RadiationMonitor"]
    class_class_curie: ClassVar[str] = "pals:RadiationMonitor"
    class_name: ClassVar[str] = "RadiationMonitor"
    class_model_uri: ClassVar[URIRef] = PALS.RadiationMonitor

    id: Union[str, RadiationMonitorId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RadiationMonitorId):
            self.id = RadiationMonitorId(self.id)

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Cavity(PhysicalComponent):
    """
    A cavity used for beam acceleration or manipulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Cavity"]
    class_class_curie: ClassVar[str] = "pals:Cavity"
    class_name: ClassVar[str] = "Cavity"
    class_model_uri: ClassVar[URIRef] = PALS.Cavity

    id: Union[str, CavityId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    ReferenceP: Optional[Union[dict, ReferenceParamGroup]] = None
    ElectricMultipoleP: Optional[Union[dict, ElectricMultipoleParamGroup]] = None
    MagneticMultipoleP: Optional[Union[dict, MagneticMultipoleParamGroup]] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        if self.ElectricMultipoleP is not None and not isinstance(self.ElectricMultipoleP, ElectricMultipoleParamGroup):
            self.ElectricMultipoleP = ElectricMultipoleParamGroup(**as_dict(self.ElectricMultipoleP))

        if self.MagneticMultipoleP is not None and not isinstance(self.MagneticMultipoleP, MagneticMultipoleParamGroup):
            self.MagneticMultipoleP = MagneticMultipoleParamGroup(**as_dict(self.MagneticMultipoleP))

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class CrabCavity(Cavity):
    """
    A cavity used for transverse beam manipulation, such as crabbing or deflecting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["CrabCavity"]
    class_class_curie: ClassVar[str] = "pals:CrabCavity"
    class_name: ClassVar[str] = "CrabCavity"
    class_model_uri: ClassVar[URIRef] = PALS.CrabCavity

    id: Union[str, CrabCavityId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrabCavityId):
            self.id = CrabCavityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class RFCavity(Cavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["RFCavity"]
    class_class_curie: ClassVar[str] = "pals:RFCavity"
    class_name: ClassVar[str] = "RFCavity"
    class_model_uri: ClassVar[URIRef] = PALS.RFCavity

    id: Union[str, RFCavityId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    RFP: Optional[Union[dict, RFParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RFCavityId):
            self.id = RFCavityId(self.id)

        if self.RFP is not None and not isinstance(self.RFP, RFParamGroup):
            self.RFP = RFParamGroup(**as_dict(self.RFP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class NormalConductingRFCavity(RFCavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["NormalConductingRFCavity"]
    class_class_curie: ClassVar[str] = "pals:NormalConductingRFCavity"
    class_name: ClassVar[str] = "NormalConductingRFCavity"
    class_model_uri: ClassVar[URIRef] = PALS.NormalConductingRFCavity

    id: Union[str, NormalConductingRFCavityId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NormalConductingRFCavityId):
            self.id = NormalConductingRFCavityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class SuperConductingRFCavity(RFCavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["SuperConductingRFCavity"]
    class_class_curie: ClassVar[str] = "pals:SuperConductingRFCavity"
    class_name: ClassVar[str] = "SuperConductingRFCavity"
    class_model_uri: ClassVar[URIRef] = PALS.SuperConductingRFCavity

    id: Union[str, SuperConductingRFCavityId] = None
    kind: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SuperConductingRFCavityId):
            self.id = SuperConductingRFCavityId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class SupportingFacilityComponent(PhysicalComponent):
    """
    A physical component that supports accelerator operation without a specific beam-pipe placement, such as a power
    supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies, and other physical
    infrastructure components that are important for understanding the structure and function of the accelerator
    system but are not inline with the beamline.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["SupportingFacilityComponent"]
    class_class_curie: ClassVar[str] = "pals:SupportingFacilityComponent"
    class_name: ClassVar[str] = "SupportingFacilityComponent"
    class_model_uri: ClassVar[URIRef] = PALS.SupportingFacilityComponent

    id: Union[str, SupportingFacilityComponentId] = None
    kind: str = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    functions: Union[Union[str, "FacilityFunctionEnum"], list[Union[str, "FacilityFunctionEnum"]]] = None
    FloorP: Optional[Union[dict, FloorParamGroup]] = None
    LongitudinalPlacementP: Optional[Union[dict, LongitudinalPlacementParamGroup]] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupportingFacilityComponentId):
            self.id = SupportingFacilityComponentId(self.id)

        if self._is_empty(self.functions):
            self.MissingRequiredField("functions")
        if not isinstance(self.functions, list):
            self.functions = [self.functions] if self.functions is not None else []
        self.functions = [v if isinstance(v, FacilityFunctionEnum) else FacilityFunctionEnum(v) for v in self.functions]

        if self.FloorP is not None and not isinstance(self.FloorP, FloorParamGroup):
            self.FloorP = FloorParamGroup(**as_dict(self.FloorP))

        if self.LongitudinalPlacementP is not None and not isinstance(self.LongitudinalPlacementP, LongitudinalPlacementParamGroup):
            self.LongitudinalPlacementP = LongitudinalPlacementParamGroup(**as_dict(self.LongitudinalPlacementP))

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class BookkeepingComponent(VirtualComponent):
    """
    A virtual component that represents a bookkeeping or organizational role in the accelerator system, such as a
    BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual
    components that are important for understanding the structure and function of the accelerator system but are not
    physical devices.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BookkeepingComponent"]
    class_class_curie: ClassVar[str] = "pals:BookkeepingComponent"
    class_name: ClassVar[str] = "BookkeepingComponent"
    class_model_uri: ClassVar[URIRef] = PALS.BookkeepingComponent

    id: Union[str, BookkeepingComponentId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    BodyShiftP: Optional[Union[dict, BodyShiftParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookkeepingComponentId):
            self.id = BookkeepingComponentId(self.id)

        if self.BodyShiftP is not None and not isinstance(self.BodyShiftP, BodyShiftParamGroup):
            self.BodyShiftP = BodyShiftParamGroup(**as_dict(self.BodyShiftP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Marker(BookkeepingComponent):
    """
    A virtual component used as a reference point or marker in the beamline structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Marker"]
    class_class_curie: ClassVar[str] = "pals:Marker"
    class_name: ClassVar[str] = "Marker"
    class_model_uri: ClassVar[URIRef] = PALS.Marker

    id: Union[str, MarkerId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarkerId):
            self.id = MarkerId(self.id)

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class BeginningEle(BookkeepingComponent):
    """
    Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the
    branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference
    parameters; otherwise it is expected to be the first element in the branch.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BeginningEle"]
    class_class_curie: ClassVar[str] = "pals:BeginningEle"
    class_name: ClassVar[str] = "BeginningEle"
    class_model_uri: ClassVar[URIRef] = PALS.BeginningEle

    id: Union[str, BeginningEleId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    ReferenceP: Optional[Union[dict, ReferenceParamGroup]] = None
    TwissP: Optional[Union[dict, TwissParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeginningEleId):
            self.id = BeginningEleId(self.id)

        if self.ReferenceP is not None and not isinstance(self.ReferenceP, ReferenceParamGroup):
            self.ReferenceP = ReferenceParamGroup(**as_dict(self.ReferenceP))

        if self.TwissP is not None and not isinstance(self.TwissP, TwissParamGroup):
            self.TwissP = TwissParamGroup(**as_dict(self.TwissP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class Drift(VirtualComponent):
    """
    A field-free space between beamline components. A Drift is a virtual beamline component whose longitudinal extent
    preserves the separation between adjacent physical or virtual components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["Drift"]
    class_class_curie: ClassVar[str] = "pals:Drift"
    class_name: ClassVar[str] = "Drift"
    class_model_uri: ClassVar[URIRef] = PALS.Drift

    id: Union[str, DriftId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    LongitudinalPlacementP: Optional[Union[dict, LongitudinalPlacementParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DriftId):
            self.id = DriftId(self.id)

        if self.LongitudinalPlacementP is not None and not isinstance(self.LongitudinalPlacementP, LongitudinalPlacementParamGroup):
            self.LongitudinalPlacementP = LongitudinalPlacementParamGroup(**as_dict(self.LongitudinalPlacementP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class BeamLineSection(BookkeepingComponent):
    """
    A virtual component used to represent a section of the BeamLine for organizational or functional grouping of
    components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["BeamLineSection"]
    class_class_curie: ClassVar[str] = "pals:BeamLineSection"
    class_name: ClassVar[str] = "BeamLineSection"
    class_model_uri: ClassVar[URIRef] = PALS.BeamLineSection

    id: Union[str, BeamLineSectionId] = None
    kind: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    FloorP: Optional[Union[dict, FloorParamGroup]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamLineSectionId):
            self.id = BeamLineSectionId(self.id)

        if self.FloorP is not None and not isinstance(self.FloorP, FloorParamGroup):
            self.FloorP = FloorParamGroup(**as_dict(self.FloorP))

        super().__post_init__(**kwargs)
        if self._is_empty(self.kind):
            self.MissingRequiredField("kind")
        self.kind = str(self.class_name)


@dataclass(repr=False)
class AdditionalMetadata(YAMLRoot):
    """
    A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any)
    field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["AdditionalMetadata"]
    class_class_curie: ClassVar[str] = "pals:AdditionalMetadata"
    class_name: ClassVar[str] = "AdditionalMetadata"
    class_model_uri: ClassVar[URIRef] = PALS.AdditionalMetadata

    key: str = None
    value: str = None
    datatype: Optional[Union[str, "DataTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.datatype is not None and not isinstance(self.datatype, DataTypeEnum):
            self.datatype = DataTypeEnum(self.datatype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Edge(YAMLRoot):
    """
    Abstract base for subject-predicate-object associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Statement"]
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Edge"
    class_model_uri: ClassVar[URIRef] = PALS.Edge

    id: Union[str, EdgeId] = None
    subject: str = None
    predicate: Union[str, URIorCURIE] = None
    object: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EdgeId):
            self.id = EdgeId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "predicate"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class SignalBinding(Edge):
    """
    Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["SignalBinding"]
    class_class_curie: ClassVar[str] = "pals:SignalBinding"
    class_name: ClassVar[str] = "SignalBinding"
    class_model_uri: ClassVar[URIRef] = PALS.SignalBinding

    id: Union[str, SignalBindingId] = None
    predicate: Union[str, URIorCURIE] = None
    subject: Union[str, PhysicalComponentId] = None
    object: Union[str, SignalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, PhysicalComponentId):
            self.subject = PhysicalComponentId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, SignalId):
            self.object = SignalId(self.object)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class HasSignal(SignalBinding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["has_signal"]
    class_class_curie: ClassVar[str] = "pals:has_signal"
    class_name: ClassVar[str] = "HasSignal"
    class_model_uri: ClassVar[URIRef] = PALS.HasSignal

    id: Union[str, HasSignalId] = None
    subject: Union[str, PhysicalComponentId] = None
    object: Union[str, SignalId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HasSignalId):
            self.id = HasSignalId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class HasSetpointSignal(SignalBinding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["has_setpoint_signal"]
    class_class_curie: ClassVar[str] = "pals:has_setpoint_signal"
    class_name: ClassVar[str] = "HasSetpointSignal"
    class_model_uri: ClassVar[URIRef] = PALS.HasSetpointSignal

    id: Union[str, HasSetpointSignalId] = None
    subject: Union[str, PhysicalComponentId] = None
    object: Union[str, SignalId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HasSetpointSignalId):
            self.id = HasSetpointSignalId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class HasReadbackSignal(SignalBinding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["has_readback_signal"]
    class_class_curie: ClassVar[str] = "pals:has_readback_signal"
    class_name: ClassVar[str] = "HasReadbackSignal"
    class_model_uri: ClassVar[URIRef] = PALS.HasReadbackSignal

    id: Union[str, HasReadbackSignalId] = None
    subject: Union[str, PhysicalComponentId] = None
    object: Union[str, SignalId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HasReadbackSignalId):
            self.id = HasReadbackSignalId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class HasCommandSignal(SignalBinding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["has_command_signal"]
    class_class_curie: ClassVar[str] = "pals:has_command_signal"
    class_name: ClassVar[str] = "HasCommandSignal"
    class_model_uri: ClassVar[URIRef] = PALS.HasCommandSignal

    id: Union[str, HasCommandSignalId] = None
    subject: Union[str, PhysicalComponentId] = None
    object: Union[str, SignalId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HasCommandSignalId):
            self.id = HasCommandSignalId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class HasLimitSignal(SignalBinding):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["has_limit_signal"]
    class_class_curie: ClassVar[str] = "pals:has_limit_signal"
    class_name: ClassVar[str] = "HasLimitSignal"
    class_model_uri: ClassVar[URIRef] = PALS.HasLimitSignal

    id: Union[str, HasLimitSignalId] = None
    subject: Union[str, PhysicalComponentId] = None
    object: Union[str, SignalId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HasLimitSignalId):
            self.id = HasLimitSignalId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class ComponentRelation(Edge):
    """
    Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about
    how and where the relationship holds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["ComponentRelation"]
    class_class_curie: ClassVar[str] = "pals:ComponentRelation"
    class_name: ClassVar[str] = "ComponentRelation"
    class_model_uri: ClassVar[URIRef] = PALS.ComponentRelation

    id: Union[str, ComponentRelationId] = None
    predicate: Union[str, URIorCURIE] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    component_direction: Optional[Union[str, "DirectionEnum"]] = None
    reference_frame: Optional[Union[str, "ReferenceFrameEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, RelationContextEnum):
            self.context = RelationContextEnum(self.context)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentId):
            self.subject = ComponentId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        if self.component_direction is not None and not isinstance(self.component_direction, DirectionEnum):
            self.component_direction = DirectionEnum(self.component_direction)

        if self.reference_frame is not None and not isinstance(self.reference_frame, ReferenceFrameEnum):
            self.reference_frame = ReferenceFrameEnum(self.reference_frame)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class Precedes(ComponentRelation):
    """
    A relationship indicating that the subject component precedes the object component in a specified context, such as
    along a beamline.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["precedes"]
    class_class_curie: ClassVar[str] = "pals:precedes"
    class_name: ClassVar[str] = "Precedes"
    class_model_uri: ClassVar[URIRef] = PALS.Precedes

    id: Union[str, PrecedesId] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    beamline_context: Union[str, BeamLineId] = None
    predicate: Union[str, URIorCURIE] = None
    context: Union[str, "RelationContextEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrecedesId):
            self.id = PrecedesId(self.id)

        if self._is_empty(self.beamline_context):
            self.MissingRequiredField("beamline_context")
        if not isinstance(self.beamline_context, BeamLineId):
            self.beamline_context = BeamLineId(self.beamline_context)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, RelationContextEnum):
            self.context = RelationContextEnum(self.context)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class Contains(ComponentRelation):
    """
    A relationship indicating that the subject component contains the object component in a specified context, such as
    within a BeamLineSection or other organizational grouping.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["contains"]
    class_class_curie: ClassVar[str] = "pals:contains"
    class_name: ClassVar[str] = "Contains"
    class_model_uri: ClassVar[URIRef] = PALS.Contains

    id: Union[str, ContainsId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContainsId):
            self.id = ContainsId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class Controls(ComponentRelation):
    """
    A relationship indicating that the subject component controls the object component in a specified context, such as
    a power supply controlling a magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["controls"]
    class_class_curie: ClassVar[str] = "pals:controls"
    class_name: ClassVar[str] = "Controls"
    class_model_uri: ClassVar[URIRef] = PALS.Controls

    id: Union[str, ControlsId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlsId):
            self.id = ControlsId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class IsPartOf(ComponentRelation):
    """
    A relationship indicating that the subject component is part of the object component in a specified context, such
    as a magnet being part of a BeamLineSection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["is_part_of"]
    class_class_curie: ClassVar[str] = "pals:is_part_of"
    class_name: ClassVar[str] = "IsPartOf"
    class_model_uri: ClassVar[URIRef] = PALS.IsPartOf

    id: Union[str, IsPartOfId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsPartOfId):
            self.id = IsPartOfId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class AdjacentTo(ComponentRelation):
    """
    A relationship indicating that the subject component is adjacent to the object component and not overlapping
    in a specified context, such as radiation detector and a magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["adjacent_to"]
    class_class_curie: ClassVar[str] = "pals:adjacent_to"
    class_name: ClassVar[str] = "AdjacentTo"
    class_model_uri: ClassVar[URIRef] = PALS.AdjacentTo

    id: Union[str, AdjacentToId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None
    distance_value: Optional[float] = None
    distance_unit: Optional[Union[str, "UnitEnum"]] = None
    tolerance_value: Optional[float] = None
    tolerance_unit: Optional[Union[str, "UnitEnum"]] = None
    coordinates: Optional[Union[dict, "CoordinateSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdjacentToId):
            self.id = AdjacentToId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self.distance_value is not None and not isinstance(self.distance_value, float):
            self.distance_value = float(self.distance_value)

        if self.distance_unit is not None and not isinstance(self.distance_unit, UnitEnum):
            self.distance_unit = UnitEnum(self.distance_unit)

        if self.tolerance_value is not None and not isinstance(self.tolerance_value, float):
            self.tolerance_value = float(self.tolerance_value)

        if self.tolerance_unit is not None and not isinstance(self.tolerance_unit, UnitEnum):
            self.tolerance_unit = UnitEnum(self.tolerance_unit)

        if self.coordinates is not None and not isinstance(self.coordinates, CoordinateSet):
            self.coordinates = CoordinateSet(**as_dict(self.coordinates))

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class Overlaps(ComponentRelation):
    """
    A relationship indicating that the subject component overlaps the object component in a specified context, such as
    a magnet and a diagnostic device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["overlaps"]
    class_class_curie: ClassVar[str] = "pals:overlaps"
    class_name: ClassVar[str] = "Overlaps"
    class_model_uri: ClassVar[URIRef] = PALS.Overlaps

    id: Union[str, OverlapsId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None
    coordinates: Optional[Union[dict, "CoordinateSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OverlapsId):
            self.id = OverlapsId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self.coordinates is not None and not isinstance(self.coordinates, CoordinateSet):
            self.coordinates = CoordinateSet(**as_dict(self.coordinates))

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class HasConnectingBranch(ComponentRelation):
    """
    A relationship indicating that the subject component has a connecting branch to the object component in a
    specified context, such as a beamline section having a fork as a connecting branch.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["has_connecting_branch"]
    class_class_curie: ClassVar[str] = "pals:has_connecting_branch"
    class_name: ClassVar[str] = "HasConnectingBranch"
    class_model_uri: ClassVar[URIRef] = PALS.HasConnectingBranch

    id: Union[str, HasConnectingBranchId] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    beamline_context: Union[str, BeamLineId] = None
    predicate: Union[str, URIorCURIE] = None
    context: Union[str, "RelationContextEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HasConnectingBranchId):
            self.id = HasConnectingBranchId(self.id)

        if self._is_empty(self.beamline_context):
            self.MissingRequiredField("beamline_context")
        if not isinstance(self.beamline_context, BeamLineId):
            self.beamline_context = BeamLineId(self.beamline_context)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, RelationContextEnum):
            self.context = RelationContextEnum(self.context)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class MountedOn(ComponentRelation):
    """
    A relationship indicating that the subject component is mounted on the object component in a specified context,
    such as a diagnostic device mounted on a magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["mounted_on"]
    class_class_curie: ClassVar[str] = "pals:mounted_on"
    class_name: ClassVar[str] = "MountedOn"
    class_model_uri: ClassVar[URIRef] = PALS.MountedOn

    id: Union[str, MountedOnId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None
    coordinates: Optional[Union[dict, "CoordinateSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MountedOnId):
            self.id = MountedOnId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self.coordinates is not None and not isinstance(self.coordinates, CoordinateSet):
            self.coordinates = CoordinateSet(**as_dict(self.coordinates))

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class Intersects(ComponentRelation):
    """
    A relationship indicating that the subject component intersects the object component in a specified context, such
    as a beamline and a diagnostic device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["intersects"]
    class_class_curie: ClassVar[str] = "pals:intersects"
    class_name: ClassVar[str] = "Intersects"
    class_model_uri: ClassVar[URIRef] = PALS.Intersects

    id: Union[str, IntersectsId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntersectsId):
            self.id = IntersectsId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class NearestTo(ComponentRelation):
    """
    A relationship indicating that the subject component is nearest to the object component in a specified context,
    such as a diagnostic device nearest to a magnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["nearest_to"]
    class_class_curie: ClassVar[str] = "pals:nearest_to"
    class_name: ClassVar[str] = "NearestTo"
    class_model_uri: ClassVar[URIRef] = PALS.NearestTo

    id: Union[str, NearestToId] = None
    context: Union[str, "RelationContextEnum"] = None
    subject: Union[str, ComponentId] = None
    object: Union[str, ComponentId] = None
    predicate: Union[str, URIorCURIE] = None
    distance_value: Optional[float] = None
    distance_unit: Optional[Union[str, "UnitEnum"]] = None
    tolerance_value: Optional[float] = None
    tolerance_unit: Optional[Union[str, "UnitEnum"]] = None
    coordinates: Optional[Union[dict, "CoordinateSet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NearestToId):
            self.id = NearestToId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)

        if self.distance_value is not None and not isinstance(self.distance_value, float):
            self.distance_value = float(self.distance_value)

        if self.distance_unit is not None and not isinstance(self.distance_unit, UnitEnum):
            self.distance_unit = UnitEnum(self.distance_unit)

        if self.tolerance_value is not None and not isinstance(self.tolerance_value, float):
            self.tolerance_value = float(self.tolerance_value)

        if self.tolerance_unit is not None and not isinstance(self.tolerance_unit, UnitEnum):
            self.tolerance_unit = UnitEnum(self.tolerance_unit)

        if self.coordinates is not None and not isinstance(self.coordinates, CoordinateSet):
            self.coordinates = CoordinateSet(**as_dict(self.coordinates))

        super().__post_init__(**kwargs)
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        self.predicate = str(self.class_class_curie)


@dataclass(repr=False)
class CoordinateSet(YAMLRoot):
    """
    A set of coordinates that define the spatial relationship between two components. This can include Cartesian
    coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial
    relationship where the relationship is not strictly linear or where the components are not aligned along a single
    axis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PALS["CoordinateSet"]
    class_class_curie: ClassVar[str] = "pals:CoordinateSet"
    class_name: ClassVar[str] = "CoordinateSet"
    class_model_uri: ClassVar[URIRef] = PALS.CoordinateSet

    coordinate_system: Optional[Union[str, "CoordinateSystemEnum"]] = None
    x_coord: Optional[float] = None
    y_coord: Optional[float] = None
    z_coord: Optional[float] = None
    r_coord: Optional[float] = None
    theta_coord: Optional[float] = None
    phi_coord: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.coordinate_system is not None and not isinstance(self.coordinate_system, CoordinateSystemEnum):
            self.coordinate_system = CoordinateSystemEnum(self.coordinate_system)

        if self.x_coord is not None and not isinstance(self.x_coord, float):
            self.x_coord = float(self.x_coord)

        if self.y_coord is not None and not isinstance(self.y_coord, float):
            self.y_coord = float(self.y_coord)

        if self.z_coord is not None and not isinstance(self.z_coord, float):
            self.z_coord = float(self.z_coord)

        if self.r_coord is not None and not isinstance(self.r_coord, float):
            self.r_coord = float(self.r_coord)

        if self.theta_coord is not None and not isinstance(self.theta_coord, float):
            self.theta_coord = float(self.theta_coord)

        if self.phi_coord is not None and not isinstance(self.phi_coord, float):
            self.phi_coord = float(self.phi_coord)

        super().__post_init__(**kwargs)


# Enumerations
class IdentifierTypeEnum(EnumDefinitionImpl):
    """
    Controlled values for identifier types.
    """
    DOI = PermissibleValue(
        text="DOI",
        description="Digital Object Identifier.",
        meaning=None)
    PURL = PermissibleValue(
        text="PURL",
        description="Persistent Uniform Resource Locator.",
        meaning=None)
    ROR = PermissibleValue(
        text="ROR",
        description="Research Organization Registry identifier.",
        meaning=None)
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Local identifier, specific to the facility or source system.",
        meaning=None)
    URL = PermissibleValue(
        text="URL",
        description="Uniform Resource Locator.",
        meaning=None)
    ARK = PermissibleValue(
        text="ARK",
        description="Archival Resource Key.",
        meaning=None)

    _defn = EnumDefinition(
        name="IdentifierTypeEnum",
        description="Controlled values for identifier types.",
    )

class SourceSystemEnum(EnumDefinitionImpl):
    """
    Controlled values for facility-local source systems.
    """
    EPICS = PermissibleValue(
        text="EPICS",
        description="EPICS control system.")
    EPICS_ChannelAccess = PermissibleValue(
        text="EPICS_ChannelAccess",
        description="EPICS Channel Access source.")
    PALS_Ext = PermissibleValue(
        text="PALS_Ext",
        description="PALS-Ext or middle-layer channel/export system.")
    MYA = PermissibleValue(
        text="MYA",
        description="MYA archive or historical channel service.")
    ElementDatabase = PermissibleValue(
        text="ElementDatabase",
        description="Facility element database.")
    ChannelDatabase = PermissibleValue(
        text="ChannelDatabase",
        description="Facility channel database.")
    Simulation = PermissibleValue(
        text="Simulation",
        description="Simulation or model-derived signal source.")
    Other = PermissibleValue(
        text="Other",
        description="Other source system.")

    _defn = EnumDefinition(
        name="SourceSystemEnum",
        description="Controlled values for facility-local source systems.",
    )

class PhysicalRelationEnum(EnumDefinitionImpl):
    """
    Controlled values for physical relation to the beamline.
    """
    Inline = PermissibleValue(
        text="Inline",
        description="""Beam passes through the physical component or beamline aperture. The physical component is physically on the beamline.""")
    AttachedToPipe = PermissibleValue(
        text="AttachedToPipe",
        description="Mechanically attached to the beam pipe or vacuum envelope.")
    NearBeamLine = PermissibleValue(
        text="NearBeamLine",
        description="Near and operationally associated with the beamline.")
    SupportingFacility = PermissibleValue(
        text="SupportingFacility",
        description="Supports accelerator operation without a specific beam-pipe placement.")

    _defn = EnumDefinition(
        name="PhysicalRelationEnum",
        description="Controlled values for physical relation to the beamline.",
    )

class VirtualRelationEnum(EnumDefinitionImpl):
    """
    Controlled values for virtual relation to the beamline.
    """
    Inline = PermissibleValue(
        text="Inline",
        description="""Beam passes through the virtual component. Used for virtual components like Markers that represent important locations on the beamline but don't have a physical instantiation.""")
    AssociatedWithBeamLine = PermissibleValue(
        text="AssociatedWithBeamLine",
        description="""Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the BeamLine structure and function but don't have a direct physical relationship to the beam path,  such as BeamLineSections or Markers that are not inline with the beam.""")
    NotAssociatedWithBeamLine = PermissibleValue(
        text="NotAssociatedWithBeamLine",
        description="""Not inline with the BeamLine and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the BeamLine, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the BeamLine structure.""")

    _defn = EnumDefinition(
        name="VirtualRelationEnum",
        description="Controlled values for virtual relation to the beamline.",
    )

class PhysicalFunctionEnum(EnumDefinitionImpl):
    """
    Broad device-level functions.
    """
    Focusing = PermissibleValue(
        text="Focusing",
        description="Focuses or defocuses the beam.")
    Steering = PermissibleValue(
        text="Steering",
        description="Steers the beam in a transverse plane.")
    BeamPositionMeasurement = PermissibleValue(
        text="BeamPositionMeasurement",
        description="Measures transverse beam position.")
    VacuumGeneration = PermissibleValue(
        text="VacuumGeneration",
        description="Generates or maintains vacuum.")
    RadiationMonitoring = PermissibleValue(
        text="RadiationMonitoring",
        description="Monitors radiation dose or dose rate.")
    Measurement = PermissibleValue(
        text="Measurement",
        description="Measures beam or machine state.")
    BeamAcceleration = PermissibleValue(
        text="BeamAcceleration",
        description="Accelerates the beam.")
    BeamLossDetection = PermissibleValue(
        text="BeamLossDetection",
        description="Detects beam loss.")
    BeamCurrentMeasurement = PermissibleValue(
        text="BeamCurrentMeasurement",
        description="Measures beam current or intensity.")
    BeamProfileMeasurement = PermissibleValue(
        text="BeamProfileMeasurement",
        description="Measures beam profile.")
    MachineProtection = PermissibleValue(
        text="MachineProtection",
        description="Supports machine protection.")
    TimingSynchronization = PermissibleValue(
        text="TimingSynchronization",
        description="Supports timing or synchronization.")

    _defn = EnumDefinition(
        name="PhysicalFunctionEnum",
        description="Broad device-level functions.",
    )

class FacilityFunctionEnum(EnumDefinitionImpl):
    """
    Broad structural or support functions.
    """
    Support = PermissibleValue(
        text="Support",
        description="Provides mechanical support for accelerator operations.")
    Alignment = PermissibleValue(
        text="Alignment",
        description="Supports alignment of accelerator components.")
    PowerSupply = PermissibleValue(
        text="PowerSupply",
        description="Provides electrical power to accelerator components.")
    ControlRack = PermissibleValue(
        text="ControlRack",
        description="Houses control electronics for accelerator components.")
    Cooling = PermissibleValue(
        text="Cooling",
        description="Provides cooling for accelerator components.")
    Diagnostics = PermissibleValue(
        text="Diagnostics",
        description="""Provides diagnostic capabilities for accelerator components, such as monitoring or measurement.""")
    Detection = PermissibleValue(
        text="Detection",
        description="""Provides detection capabilities for accelerator components, such as radiation or particle detection.""")

    _defn = EnumDefinition(
        name="FacilityFunctionEnum",
        description="Broad structural or support functions.",
    )

class VirtualFunctionEnum(EnumDefinitionImpl):
    """
    Broad virtual component functions or roles.
    """
    BeamLineSection = PermissibleValue(
        text="BeamLineSection",
        description="""A section of the BeamLine used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector.""",
        meaning=PALS["BeamLine"])
    Mark = PermissibleValue(
        text="Mark",
        description="""A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device.""",
        meaning=PALS["Marker"])
    DriftSpace = PermissibleValue(
        text="DriftSpace",
        description="A field-free longitudinal interval separating beamline components.",
        meaning=PALS["Drift"])
    Fork = PermissibleValue(
        text="Fork",
        description="""A virtual component representing a branching point in the beamline,  such as a beamline fork or switchyard.""",
        meaning=PALS["Fork"])
    Control = PermissibleValue(
        text="Control",
        description="""A virtual component representing a control system function or role that is important for understanding the overall accelerator system  but doesn't have a direct relationship to the beamline structure,  such as the EPICS control system that manages device process variables across the accelerator.""")

    _defn = EnumDefinition(
        name="VirtualFunctionEnum",
        description="Broad virtual component functions or roles.",
    )

class PlaneEnum(EnumDefinitionImpl):
    """
    Controlled values for transverse plane.
    """
    Horizontal = PermissibleValue(
        text="Horizontal",
        description="Horizontal transverse plane.")
    Vertical = PermissibleValue(
        text="Vertical",
        description="Vertical transverse plane.")

    _defn = EnumDefinition(
        name="PlaneEnum",
        description="Controlled values for transverse plane.",
    )

class SignalRoleEnum(EnumDefinitionImpl):
    """
    Roles for control-system signals.
    """
    Setpoint = PermissibleValue(
        text="Setpoint",
        description="Requested or configured value.",
        meaning=SOSA["ActuatableProperty"])
    Readback = PermissibleValue(
        text="Readback",
        description="Measured or reported value.",
        meaning=SOSA["ObservableProperty"])
    Status = PermissibleValue(
        text="Status",
        description="State or condition indicator.")
    Command = PermissibleValue(
        text="Command",
        description="Command or action trigger.",
        meaning=SOSA["ActuatableProperty"])
    MinimumLimit = PermissibleValue(
        text="MinimumLimit",
        description="Minimum allowed signal value.",
        meaning=XSD["minInclusive"])
    MaximumLimit = PermissibleValue(
        text="MaximumLimit",
        description="Maximum allowed signal value.",
        meaning=XSD["maxInclusive"])
    RangeLimit = PermissibleValue(
        text="RangeLimit",
        description="A signal containing both upper and lower allowed limits.",
        meaning=SSN_SYSTEM["OperatingRange"])

    _defn = EnumDefinition(
        name="SignalRoleEnum",
        description="Roles for control-system signals.",
    )

class CanonicalSignalTypeEnum(EnumDefinitionImpl):
    """
    Portable semantic meanings for important signals.
    """
    HorizontalBeamPosition = PermissibleValue(
        text="HorizontalBeamPosition",
        description="Horizontal beam position signal.")
    VerticalBeamPosition = PermissibleValue(
        text="VerticalBeamPosition",
        description="Vertical beam position signal.")
    HorizontalBeamPositionOffset = PermissibleValue(
        text="HorizontalBeamPositionOffset",
        description="Horizontal beam position offset signal.")
    VerticalBeamPositionOffset = PermissibleValue(
        text="VerticalBeamPositionOffset",
        description="Vertical beam position offset signal.")
    BeamIntensity = PermissibleValue(
        text="BeamIntensity",
        description="Beam intensity or current signal.")
    DeviceStatus = PermissibleValue(
        text="DeviceStatus",
        description="Device status signal.")
    GradientSetpoint = PermissibleValue(
        text="GradientSetpoint",
        description="Cavity accelerating gradient setpoint signal.")
    GradientReadback = PermissibleValue(
        text="GradientReadback",
        description="Cavity accelerating gradient readback signal.")
    MagnetCurrentSetpoint = PermissibleValue(
        text="MagnetCurrentSetpoint",
        description="Magnet current setpoint signal.")
    MagnetCurrentReadback = PermissibleValue(
        text="MagnetCurrentReadback",
        description="Magnet current readback signal.")
    MagnetFieldSetpoint = PermissibleValue(
        text="MagnetFieldSetpoint",
        description="Magnet field setpoint signal.")
    MagnetCurrentRange = PermissibleValue(
        text="MagnetCurrentRange",
        description="Magnet current range signal.")
    IntegratedFieldSetpoint = PermissibleValue(
        text="IntegratedFieldSetpoint",
        description="Integrated magnetic field setpoint signal.")
    IntegratedFieldReadback = PermissibleValue(
        text="IntegratedFieldReadback",
        description="Integrated magnetic field readback signal.")
    VacuumPressure = PermissibleValue(
        text="VacuumPressure",
        description="Vacuum pressure signal.")
    IonPumpCurrent = PermissibleValue(
        text="IonPumpCurrent",
        description="Ion pump current signal.")
    IonPumpVoltage = PermissibleValue(
        text="IonPumpVoltage",
        description="Ion pump voltage signal.")
    GammaDoseRate = PermissibleValue(
        text="GammaDoseRate",
        description="Gamma radiation dose-rate signal.")
    NeutronDoseRate = PermissibleValue(
        text="NeutronDoseRate",
        description="Neutron radiation dose-rate signal.")
    Status = PermissibleValue(
        text="Status",
        description="Generic status signal for a device.")

    _defn = EnumDefinition(
        name="CanonicalSignalTypeEnum",
        description="Portable semantic meanings for important signals.",
    )

class QuantityKindEnum(EnumDefinitionImpl):
    """
    Physical quantity kinds for signals.
    """
    BeamPosition = PermissibleValue(
        text="BeamPosition",
        description="Beam transverse position.")
    State = PermissibleValue(
        text="State",
        description="Device state or condition.",
        meaning=SOSA["ObservableProperty"])
    ElectricCurrent = PermissibleValue(
        text="ElectricCurrent",
        description="Electric current.",
        meaning=QUANTITYKIND["ElectricCurrent"])
    IntegratedMagneticField = PermissibleValue(
        text="IntegratedMagneticField",
        description="Integrated magnetic field.",
        meaning=QUANTITYKIND["MagneticFluxPerLength"])
    MagneticField = PermissibleValue(
        text="MagneticField",
        description="Magnetic field.",
        meaning=QUANTITYKIND["MagneticFluxDensity"])
    Pressure = PermissibleValue(
        text="Pressure",
        description="Gas or vacuum pressure.",
        meaning=QUANTITYKIND["Pressure"])
    DoseRate = PermissibleValue(
        text="DoseRate",
        description="Radiation dose rate.",
        meaning=QUANTITYKIND["AbsorbedDoseRate"])
    Voltage = PermissibleValue(
        text="Voltage",
        description="Electric potential difference.",
        meaning=QUANTITYKIND["Voltage"])
    Power = PermissibleValue(
        text="Power",
        description="Power.",
        meaning=QUANTITYKIND["Power"])
    CavityPhase = PermissibleValue(
        text="CavityPhase",
        description="Cavity phase.",
        meaning=QUANTITYKIND["PhaseAngle"])
    CavityGradient = PermissibleValue(
        text="CavityGradient",
        description="Cavity accelerating gradient.",
        meaning=QUANTITYKIND["ElectricFieldStrength"])

    _defn = EnumDefinition(
        name="QuantityKindEnum",
        description="Physical quantity kinds for signals.",
    )

class UnitEnum(EnumDefinitionImpl):
    """
    Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an
    exact QUDT unit is available.
    """
    A = PermissibleValue(
        text="A",
        description="ampere")
    degree = PermissibleValue(
        text="degree",
        description="degree")
    eV = PermissibleValue(
        text="eV",
        description="electron volt")
    eV_per_c = PermissibleValue(
        text="eV_per_c",
        description="momentum in electron volts per speed of light")
    eV_per_c2 = PermissibleValue(
        text="eV_per_c2",
        description="mass in electron volts per speed of light squared")
    fundamental_charge = PermissibleValue(
        text="fundamental_charge",
        description="fundamental charge")
    G_per_cm = PermissibleValue(
        text="G_per_cm",
        description="gauss per centimeter")
    Hz = PermissibleValue(
        text="Hz",
        description="hertz")
    kW = PermissibleValue(
        text="kW",
        description="kilowatt")
    m = PermissibleValue(
        text="m",
        description="meter")
    mm = PermissibleValue(
        text="mm",
        description="millimeter")
    mrem_per_h = PermissibleValue(
        text="mrem_per_h",
        description="""millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary.""")
    MV_per_m = PermissibleValue(
        text="MV_per_m",
        description="megavolt per meter")
    PA = PermissibleValue(
        text="PA",
        description="pascal")
    randians_pi2 = PermissibleValue(
        text="randians_pi2",
        description="radians divided by 2 pi - angles and phases")
    rem_per_h = PermissibleValue(
        text="rem_per_h",
        description="""rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary.""")
    seconds = PermissibleValue(
        text="seconds",
        description="second")
    T = PermissibleValue(
        text="T",
        description="tesla")
    T_M = PermissibleValue(
        text="T_M",
        description="tesla meter")
    Torr = PermissibleValue(
        text="Torr",
        description="torr")
    V = PermissibleValue(
        text="V",
        description="volt")
    V_per_m = PermissibleValue(
        text="V_per_m",
        description="volt per meter")
    unitless = PermissibleValue(
        text="unitless",
        description="dimensionless numeric value")
    none = PermissibleValue(
        text="none",
        description="no unit or not applicable")

    _defn = EnumDefinition(
        name="UnitEnum",
        description="""Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available.""",
    )

class DataTypeEnum(EnumDefinitionImpl):
    """
    Data types for parameter values.
    """
    String = PermissibleValue(
        text="String",
        description="string data type",
        meaning=XSD["string"])
    Integer = PermissibleValue(
        text="Integer",
        description="integer data type",
        meaning=XSD["integer"])
    Float = PermissibleValue(
        text="Float",
        description="floating-point data type",
        meaning=XSD["float"])
    Boolean = PermissibleValue(
        text="Boolean",
        description="boolean data type",
        meaning=XSD["boolean"])
    FloatArray = PermissibleValue(
        text="FloatArray",
        description="An array of floating-point values.")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Data types for parameter values.",
    )

class CoordinateSystemEnum(EnumDefinitionImpl):
    """
    Coordinate systems for spatial relationships.
    """
    Cartesian = PermissibleValue(
        text="Cartesian",
        description="Cartesian coordinate system (x, y, z).")
    Cylindrical = PermissibleValue(
        text="Cylindrical",
        description="Cylindrical coordinate system (r, theta, z).")
    Spherical = PermissibleValue(
        text="Spherical",
        description="Spherical coordinate system (r, theta, phi).")

    _defn = EnumDefinition(
        name="CoordinateSystemEnum",
        description="Coordinate systems for spatial relationships.",
    )

class RelationContextEnum(EnumDefinitionImpl):

    beamline_order = PermissibleValue(text="beamline_order")
    Euclidean_3D = PermissibleValue(text="Euclidean_3D")
    Euclidean_2D = PermissibleValue(text="Euclidean_2D")
    floorplan = PermissibleValue(text="floorplan")
    containment = PermissibleValue(text="containment")
    installation_mounting = PermissibleValue(text="installation_mounting")

    _defn = EnumDefinition(
        name="RelationContextEnum",
    )

class ReferenceFrameEnum(EnumDefinitionImpl):

    beam_direction = PermissibleValue(text="beam_direction")
    facility_coordinates = PermissibleValue(text="facility_coordinates")
    local_component_frame = PermissibleValue(text="local_component_frame")
    tunnel_stationing = PermissibleValue(text="tunnel_stationing")

    _defn = EnumDefinition(
        name="ReferenceFrameEnum",
    )

class DirectionEnum(EnumDefinitionImpl):

    upstream = PermissibleValue(text="upstream")
    downstream = PermissibleValue(text="downstream")
    positive = PermissibleValue(text="positive")
    negative = PermissibleValue(text="negative")

    _defn = EnumDefinition(
        name="DirectionEnum",
    )

class MultipoleGeometryEnum(EnumDefinitionImpl):
    """
    The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles.
    """
    follows_ref_geometry = PermissibleValue(
        text="follows_ref_geometry",
        description="Use geometry equivalent to the setting of `ref_geometry`.")
    vertically_pure = PermissibleValue(
        text="vertically_pure",
        description="Vertically pure multipoles with arc geometry.")
    horizontally_pure = PermissibleValue(
        text="horizontally_pure",
        description="Horizontally pure multipoles with arc geometry.")
    chord = PermissibleValue(
        text="chord",
        description="Z-axis is the chord connecting the entrance origin point to the exit origin point.")
    entrance_coords = PermissibleValue(
        text="entrance_coords",
        description="Rectangular coordinates commensurate with the entrance coordinates.")
    exit_coords = PermissibleValue(
        text="exit_coords",
        description="Rectangular coordinates commensurate with the exit coordinates.")

    _defn = EnumDefinition(
        name="MultipoleGeometryEnum",
        description="The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles.",
    )

class ReferenceGeometryEnum(EnumDefinitionImpl):
    """
    The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles.
    """
    arc = PermissibleValue(
        text="arc",
        description="Default. Reference are the curvelinear arc coordinates.")
    chord = PermissibleValue(
        text="chord",
        description="Z-axis is the chord connecting the entrance origin point to the exit origin point.")
    entrance_coords = PermissibleValue(
        text="entrance_coords",
        description="Rectangular coordinates commensurate with the entrance coordinates.")
    exit_coords = PermissibleValue(
        text="exit_coords",
        description="Rectangular coordinates commensurate with the exit coordinates.")

    _defn = EnumDefinition(
        name="ReferenceGeometryEnum",
        description="""The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles.""",
    )

class CavityTypeEnum(EnumDefinitionImpl):
    """
    The type of cavity, which determines the field configuration and mode structure.
    """
    STANDING_WAVE = PermissibleValue(
        text="STANDING_WAVE",
        description="""Default. A cavity that supports standing wave modes, typically with fixed geometry and resonant frequencies.""")
    TRAVELING_WAVE = PermissibleValue(
        text="TRAVELING_WAVE",
        description="""A cavity that supports traveling wave modes, typically with a waveguide structure and phase velocity matching the beam.""")

    _defn = EnumDefinition(
        name="CavityTypeEnum",
        description="The type of cavity, which determines the field configuration and mode structure.",
    )

class ZeroPhaseEnum(EnumDefinitionImpl):
    """
    The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity.
    """
    ACCELERATING = PermissibleValue(
        text="ACCELERATING",
        description="Default. The zero phase is the maximum accelerating phase, where the beam gains energy.")
    BELOW_TRANSITION = PermissibleValue(
        text="BELOW_TRANSITION",
        description="Zero phase is at the stable zero crossing for particles below transition.")
    ABOVE_TRANSITION = PermissibleValue(
        text="ABOVE_TRANSITION",
        description="Zero phase is at the stable zero crossing for particles above transition..")

    _defn = EnumDefinition(
        name="ZeroPhaseEnum",
        description="""The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=PALS.id, name="id", curie=PALS.curie('id'),
                   model_uri=PALS.id, domain=None, range=URIRef)

slots.name = Slot(uri=PALS.name, name="name", curie=PALS.curie('name'),
                   model_uri=PALS.name, domain=None, range=Optional[str])

slots.alias = Slot(uri=PALS.alias, name="alias", curie=PALS.curie('alias'),
                   model_uri=PALS.alias, domain=None, range=Optional[Union[str, list[str]]])

slots.kind = Slot(uri=PALS.kind, name="kind", curie=PALS.curie('kind'),
                   model_uri=PALS.kind, domain=None, range=str)

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=PALS.subject, domain=None, range=str)

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.predicate, domain=None, range=Union[str, URIorCURIE])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=PALS.object, domain=None, range=str)

slots.affiliation = Slot(uri=PALS.affiliation, name="affiliation", curie=PALS.curie('affiliation'),
                   model_uri=PALS.affiliation, domain=None, range=Optional[Union[dict, Affiliation]])

slots.description = Slot(uri=PALS.description, name="description", curie=PALS.curie('description'),
                   model_uri=PALS.description, domain=None, range=Optional[str])

slots.identifiers = Slot(uri=PALS.identifiers, name="identifiers", curie=PALS.curie('identifiers'),
                   model_uri=PALS.identifiers, domain=None, range=Optional[Union[Union[dict, Identifier], list[Union[dict, Identifier]]]])

slots.length = Slot(uri=PALS.length, name="length", curie=PALS.curie('length'),
                   model_uri=PALS.length, domain=None, range=Optional[float])

slots.context = Slot(uri=PALS.context, name="context", curie=PALS.curie('context'),
                   model_uri=PALS.context, domain=None, range=Union[str, "RelationContextEnum"])

slots.beamline_context = Slot(uri=PALS.beamline_context, name="beamline_context", curie=PALS.curie('beamline_context'),
                   model_uri=PALS.beamline_context, domain=None, range=Union[str, BeamLineId])

slots.distance_value = Slot(uri=OM.Distance, name="distance_value", curie=OM.curie('Distance'),
                   model_uri=PALS.distance_value, domain=None, range=Optional[float])

slots.distance_unit = Slot(uri=PALS.distance_unit, name="distance_unit", curie=PALS.curie('distance_unit'),
                   model_uri=PALS.distance_unit, domain=None, range=Optional[Union[str, "UnitEnum"]])

slots.tolerance_value = Slot(uri=PALS.tolerance_value, name="tolerance_value", curie=PALS.curie('tolerance_value'),
                   model_uri=PALS.tolerance_value, domain=None, range=Optional[float])

slots.tolerance_unit = Slot(uri=PALS.tolerance_unit, name="tolerance_unit", curie=PALS.curie('tolerance_unit'),
                   model_uri=PALS.tolerance_unit, domain=None, range=Optional[Union[str, "UnitEnum"]])

slots.coordinates = Slot(uri=PALS.coordinates, name="coordinates", curie=PALS.curie('coordinates'),
                   model_uri=PALS.coordinates, domain=None, range=Optional[Union[dict, CoordinateSet]])

slots.pALSAccelerator__version = Slot(uri=PALS.version, name="pALSAccelerator__version", curie=PALS.curie('version'),
                   model_uri=PALS.pALSAccelerator__version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$'))

slots.pALSAccelerator__authors = Slot(uri=PALS.authors, name="pALSAccelerator__authors", curie=PALS.curie('authors'),
                   model_uri=PALS.pALSAccelerator__authors, domain=None, range=Optional[Union[Union[dict, Author], list[Union[dict, Author]]]])

slots.pALSAccelerator__notes = Slot(uri=PALS.notes, name="pALSAccelerator__notes", curie=PALS.curie('notes'),
                   model_uri=PALS.pALSAccelerator__notes, domain=None, range=Optional[Union[str, list[str]]])

slots.pALSAccelerator__facility = Slot(uri=PALS.facility, name="pALSAccelerator__facility", curie=PALS.curie('facility'),
                   model_uri=PALS.pALSAccelerator__facility, domain=None, range=Optional[Union[dict, Facility]])

slots.author__email = Slot(uri=PALS.email, name="author__email", curie=PALS.curie('email'),
                   model_uri=PALS.author__email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[^@]+@[^@]+\.[^@]+$'))

slots.author__orcid = Slot(uri=PALS.orcid, name="author__orcid", curie=PALS.curie('orcid'),
                   model_uri=PALS.author__orcid, domain=None, range=Optional[str],
                   pattern=re.compile(r'^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[\dX]$'))

slots.facility__components = Slot(uri=PALS.components, name="facility__components", curie=PALS.curie('components'),
                   model_uri=PALS.facility__components, domain=None, range=Optional[Union[dict[Union[str, ComponentId], Union[dict, Component]], list[Union[dict, Component]]]])

slots.facility__beamlines = Slot(uri=PALS.beamlines, name="facility__beamlines", curie=PALS.curie('beamlines'),
                   model_uri=PALS.facility__beamlines, domain=None, range=Optional[Union[dict[Union[str, BeamLineId], Union[dict, BeamLine]], list[Union[dict, BeamLine]]]])

slots.facility__signals = Slot(uri=PALS.signals, name="facility__signals", curie=PALS.curie('signals'),
                   model_uri=PALS.facility__signals, domain=None, range=Optional[Union[dict[Union[str, SignalId], Union[dict, Signal]], list[Union[dict, Signal]]]])

slots.facility__signal_bindings = Slot(uri=PALS.signal_bindings, name="facility__signal_bindings", curie=PALS.curie('signal_bindings'),
                   model_uri=PALS.facility__signal_bindings, domain=None, range=Optional[Union[dict[Union[str, SignalBindingId], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.facility__component_relations = Slot(uri=PALS.component_relations, name="facility__component_relations", curie=PALS.curie('component_relations'),
                   model_uri=PALS.facility__component_relations, domain=None, range=Optional[Union[dict[Union[str, ComponentRelationId], Union[dict, ComponentRelation]], list[Union[dict, ComponentRelation]]]])

slots.identifier__identifier_type = Slot(uri=PALS.identifier_type, name="identifier__identifier_type", curie=PALS.curie('identifier_type'),
                   model_uri=PALS.identifier__identifier_type, domain=None, range=Optional[Union[str, "IdentifierTypeEnum"]])

slots.identifier__identifier_value = Slot(uri=PALS.identifier_value, name="identifier__identifier_value", curie=PALS.curie('identifier_value'),
                   model_uri=PALS.identifier__identifier_value, domain=None, range=Optional[str])

slots.hasMetaP__MetaP = Slot(uri=PALS.MetaP, name="hasMetaP__MetaP", curie=PALS.curie('MetaP'),
                   model_uri=PALS.hasMetaP__MetaP, domain=None, range=Optional[Union[dict, MetaParamGroup]])

slots.metaParamGroup__label = Slot(uri=PALS.label, name="metaParamGroup__label", curie=PALS.curie('label'),
                   model_uri=PALS.metaParamGroup__label, domain=None, range=Optional[str])

slots.metaParamGroup__additional_metadata = Slot(uri=PALS.additional_metadata, name="metaParamGroup__additional_metadata", curie=PALS.curie('additional_metadata'),
                   model_uri=PALS.metaParamGroup__additional_metadata, domain=None, range=Optional[Union[Union[dict, AdditionalMetadata], list[Union[dict, AdditionalMetadata]]]])

slots.hasFloorP__FloorP = Slot(uri=PALS.FloorP, name="hasFloorP__FloorP", curie=PALS.curie('FloorP'),
                   model_uri=PALS.hasFloorP__FloorP, domain=None, range=Optional[Union[dict, FloorParamGroup]])

slots.floorParamGroup__x = Slot(uri=PALS.x, name="floorParamGroup__x", curie=PALS.curie('x'),
                   model_uri=PALS.floorParamGroup__x, domain=None, range=Optional[float])

slots.floorParamGroup__y = Slot(uri=PALS.y, name="floorParamGroup__y", curie=PALS.curie('y'),
                   model_uri=PALS.floorParamGroup__y, domain=None, range=Optional[float])

slots.floorParamGroup__z = Slot(uri=PALS.z, name="floorParamGroup__z", curie=PALS.curie('z'),
                   model_uri=PALS.floorParamGroup__z, domain=None, range=Optional[float])

slots.floorParamGroup__theta = Slot(uri=PALS.theta, name="floorParamGroup__theta", curie=PALS.curie('theta'),
                   model_uri=PALS.floorParamGroup__theta, domain=None, range=Optional[float])

slots.floorParamGroup__phi = Slot(uri=PALS.phi, name="floorParamGroup__phi", curie=PALS.curie('phi'),
                   model_uri=PALS.floorParamGroup__phi, domain=None, range=Optional[float])

slots.floorParamGroup__psi = Slot(uri=PALS.psi, name="floorParamGroup__psi", curie=PALS.curie('psi'),
                   model_uri=PALS.floorParamGroup__psi, domain=None, range=Optional[float])

slots.hasBodyShiftP__BodyShiftP = Slot(uri=PALS.BodyShiftP, name="hasBodyShiftP__BodyShiftP", curie=PALS.curie('BodyShiftP'),
                   model_uri=PALS.hasBodyShiftP__BodyShiftP, domain=None, range=Optional[Union[dict, BodyShiftParamGroup]])

slots.bodyShiftParamGroup__x_offset = Slot(uri=PALS.x_offset, name="bodyShiftParamGroup__x_offset", curie=PALS.curie('x_offset'),
                   model_uri=PALS.bodyShiftParamGroup__x_offset, domain=None, range=Optional[float])

slots.bodyShiftParamGroup__y_offset = Slot(uri=PALS.y_offset, name="bodyShiftParamGroup__y_offset", curie=PALS.curie('y_offset'),
                   model_uri=PALS.bodyShiftParamGroup__y_offset, domain=None, range=Optional[float])

slots.bodyShiftParamGroup__z_offset = Slot(uri=PALS.z_offset, name="bodyShiftParamGroup__z_offset", curie=PALS.curie('z_offset'),
                   model_uri=PALS.bodyShiftParamGroup__z_offset, domain=None, range=Optional[float])

slots.bodyShiftParamGroup__x_rot = Slot(uri=PALS.x_rot, name="bodyShiftParamGroup__x_rot", curie=PALS.curie('x_rot'),
                   model_uri=PALS.bodyShiftParamGroup__x_rot, domain=None, range=Optional[float])

slots.bodyShiftParamGroup__y_rot = Slot(uri=PALS.y_rot, name="bodyShiftParamGroup__y_rot", curie=PALS.curie('y_rot'),
                   model_uri=PALS.bodyShiftParamGroup__y_rot, domain=None, range=Optional[float])

slots.bodyShiftParamGroup__z_rot = Slot(uri=PALS.z_rot, name="bodyShiftParamGroup__z_rot", curie=PALS.curie('z_rot'),
                   model_uri=PALS.bodyShiftParamGroup__z_rot, domain=None, range=Optional[float])

slots.hasLongitudinalPlacementP__LongitudinalPlacementP = Slot(uri=PALS.LongitudinalPlacementP, name="hasLongitudinalPlacementP__LongitudinalPlacementP", curie=PALS.curie('LongitudinalPlacementP'),
                   model_uri=PALS.hasLongitudinalPlacementP__LongitudinalPlacementP, domain=None, range=Optional[Union[dict, LongitudinalPlacementParamGroup]])

slots.longitudinalPlacementParamGroup__s_position = Slot(uri=PALS.s_position, name="longitudinalPlacementParamGroup__s_position", curie=PALS.curie('s_position'),
                   model_uri=PALS.longitudinalPlacementParamGroup__s_position, domain=None, range=Optional[float])

slots.hasReferenceP__ReferenceP = Slot(uri=PALS.ReferenceP, name="hasReferenceP__ReferenceP", curie=PALS.curie('ReferenceP'),
                   model_uri=PALS.hasReferenceP__ReferenceP, domain=None, range=Optional[Union[dict, ReferenceParamGroup]])

slots.referenceParamGroup__species_ref = Slot(uri=PALS.species_ref, name="referenceParamGroup__species_ref", curie=PALS.curie('species_ref'),
                   model_uri=PALS.referenceParamGroup__species_ref, domain=None, range=Optional[str])

slots.referenceParamGroup__pc_ref = Slot(uri=PALS.pc_ref, name="referenceParamGroup__pc_ref", curie=PALS.curie('pc_ref'),
                   model_uri=PALS.referenceParamGroup__pc_ref, domain=None, range=Optional[float])

slots.referenceParamGroup__E_tot_ref = Slot(uri=PALS.E_tot_ref, name="referenceParamGroup__E_tot_ref", curie=PALS.curie('E_tot_ref'),
                   model_uri=PALS.referenceParamGroup__E_tot_ref, domain=None, range=Optional[float])

slots.referenceParamGroup__time_ref = Slot(uri=PALS.time_ref, name="referenceParamGroup__time_ref", curie=PALS.curie('time_ref'),
                   model_uri=PALS.referenceParamGroup__time_ref, domain=None, range=Optional[float])

slots.hasSolenoidP__SolenoidP = Slot(uri=PALS.SolenoidP, name="hasSolenoidP__SolenoidP", curie=PALS.curie('SolenoidP'),
                   model_uri=PALS.hasSolenoidP__SolenoidP, domain=None, range=Optional[Union[dict, SolenoidParamGroup]])

slots.solenoidParamGroup__Ksol = Slot(uri=PALS.Ksol, name="solenoidParamGroup__Ksol", curie=PALS.curie('Ksol'),
                   model_uri=PALS.solenoidParamGroup__Ksol, domain=None, range=Optional[float])

slots.solenoidParamGroup__Bsol = Slot(uri=PALS.Bsol, name="solenoidParamGroup__Bsol", curie=PALS.curie('Bsol'),
                   model_uri=PALS.solenoidParamGroup__Bsol, domain=None, range=Optional[float])

slots.hasTwissP__TwissP = Slot(uri=PALS.TwissP, name="hasTwissP__TwissP", curie=PALS.curie('TwissP'),
                   model_uri=PALS.hasTwissP__TwissP, domain=None, range=Optional[Union[dict, TwissParamGroup]])

slots.twissParamGroup__alpha_a = Slot(uri=PALS.alpha_a, name="twissParamGroup__alpha_a", curie=PALS.curie('alpha_a'),
                   model_uri=PALS.twissParamGroup__alpha_a, domain=None, range=Optional[float])

slots.twissParamGroup__alpha_b = Slot(uri=PALS.alpha_b, name="twissParamGroup__alpha_b", curie=PALS.curie('alpha_b'),
                   model_uri=PALS.twissParamGroup__alpha_b, domain=None, range=Optional[float])

slots.twissParamGroup__beta_a = Slot(uri=PALS.beta_a, name="twissParamGroup__beta_a", curie=PALS.curie('beta_a'),
                   model_uri=PALS.twissParamGroup__beta_a, domain=None, range=Optional[float])

slots.twissParamGroup__beta_b = Slot(uri=PALS.beta_b, name="twissParamGroup__beta_b", curie=PALS.curie('beta_b'),
                   model_uri=PALS.twissParamGroup__beta_b, domain=None, range=Optional[float])

slots.twissParamGroup__cmat11 = Slot(uri=PALS.cmat11, name="twissParamGroup__cmat11", curie=PALS.curie('cmat11'),
                   model_uri=PALS.twissParamGroup__cmat11, domain=None, range=Optional[float])

slots.twissParamGroup__cmat12 = Slot(uri=PALS.cmat12, name="twissParamGroup__cmat12", curie=PALS.curie('cmat12'),
                   model_uri=PALS.twissParamGroup__cmat12, domain=None, range=Optional[float])

slots.twissParamGroup__cmat21 = Slot(uri=PALS.cmat21, name="twissParamGroup__cmat21", curie=PALS.curie('cmat21'),
                   model_uri=PALS.twissParamGroup__cmat21, domain=None, range=Optional[float])

slots.twissParamGroup__cmat22 = Slot(uri=PALS.cmat22, name="twissParamGroup__cmat22", curie=PALS.curie('cmat22'),
                   model_uri=PALS.twissParamGroup__cmat22, domain=None, range=Optional[float])

slots.twissParamGroup__eta_x = Slot(uri=PALS.eta_x, name="twissParamGroup__eta_x", curie=PALS.curie('eta_x'),
                   model_uri=PALS.twissParamGroup__eta_x, domain=None, range=Optional[float])

slots.twissParamGroup__eta_y = Slot(uri=PALS.eta_y, name="twissParamGroup__eta_y", curie=PALS.curie('eta_y'),
                   model_uri=PALS.twissParamGroup__eta_y, domain=None, range=Optional[float])

slots.twissParamGroup__etap_x = Slot(uri=PALS.etap_x, name="twissParamGroup__etap_x", curie=PALS.curie('etap_x'),
                   model_uri=PALS.twissParamGroup__etap_x, domain=None, range=Optional[float])

slots.twissParamGroup__etap_y = Slot(uri=PALS.etap_y, name="twissParamGroup__etap_y", curie=PALS.curie('etap_y'),
                   model_uri=PALS.twissParamGroup__etap_y, domain=None, range=Optional[float])

slots.twissParamGroup__deta_x_ds = Slot(uri=PALS.deta_x_ds, name="twissParamGroup__deta_x_ds", curie=PALS.curie('deta_x_ds'),
                   model_uri=PALS.twissParamGroup__deta_x_ds, domain=None, range=Optional[float])

slots.twissParamGroup__deta_y_ds = Slot(uri=PALS.deta_y_ds, name="twissParamGroup__deta_y_ds", curie=PALS.curie('deta_y_ds'),
                   model_uri=PALS.twissParamGroup__deta_y_ds, domain=None, range=Optional[float])

slots.twissParamGroup__phi_a = Slot(uri=PALS.phi_a, name="twissParamGroup__phi_a", curie=PALS.curie('phi_a'),
                   model_uri=PALS.twissParamGroup__phi_a, domain=None, range=Optional[float])

slots.twissParamGroup__phi_b = Slot(uri=PALS.phi_b, name="twissParamGroup__phi_b", curie=PALS.curie('phi_b'),
                   model_uri=PALS.twissParamGroup__phi_b, domain=None, range=Optional[float])

slots.twissParamGroup__dbeta_a_dpz = Slot(uri=PALS.dbeta_a_dpz, name="twissParamGroup__dbeta_a_dpz", curie=PALS.curie('dbeta_a_dpz'),
                   model_uri=PALS.twissParamGroup__dbeta_a_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__dalpha_a_dpz = Slot(uri=PALS.dalpha_a_dpz, name="twissParamGroup__dalpha_a_dpz", curie=PALS.curie('dalpha_a_dpz'),
                   model_uri=PALS.twissParamGroup__dalpha_a_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__dbeta_b_dpz = Slot(uri=PALS.dbeta_b_dpz, name="twissParamGroup__dbeta_b_dpz", curie=PALS.curie('dbeta_b_dpz'),
                   model_uri=PALS.twissParamGroup__dbeta_b_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__dalpha_b_dpz = Slot(uri=PALS.dalpha_b_dpz, name="twissParamGroup__dalpha_b_dpz", curie=PALS.curie('dalpha_b_dpz'),
                   model_uri=PALS.twissParamGroup__dalpha_b_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__deta_x_dpz = Slot(uri=PALS.deta_x_dpz, name="twissParamGroup__deta_x_dpz", curie=PALS.curie('deta_x_dpz'),
                   model_uri=PALS.twissParamGroup__deta_x_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__detap_x_dpz = Slot(uri=PALS.detap_x_dpz, name="twissParamGroup__detap_x_dpz", curie=PALS.curie('detap_x_dpz'),
                   model_uri=PALS.twissParamGroup__detap_x_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__deta_y_dpz = Slot(uri=PALS.deta_y_dpz, name="twissParamGroup__deta_y_dpz", curie=PALS.curie('deta_y_dpz'),
                   model_uri=PALS.twissParamGroup__deta_y_dpz, domain=None, range=Optional[float])

slots.twissParamGroup__detap_y_dpz = Slot(uri=PALS.detap_y_dpz, name="twissParamGroup__detap_y_dpz", curie=PALS.curie('detap_y_dpz'),
                   model_uri=PALS.twissParamGroup__detap_y_dpz, domain=None, range=Optional[float])

slots.hasRFP__RFP = Slot(uri=PALS.RFP, name="hasRFP__RFP", curie=PALS.curie('RFP'),
                   model_uri=PALS.hasRFP__RFP, domain=None, range=Optional[Union[dict, RFParamGroup]])

slots.rFParamGroup__frequency = Slot(uri=PALS.frequency, name="rFParamGroup__frequency", curie=PALS.curie('frequency'),
                   model_uri=PALS.rFParamGroup__frequency, domain=None, range=Optional[float])

slots.rFParamGroup__harmon = Slot(uri=PALS.harmon, name="rFParamGroup__harmon", curie=PALS.curie('harmon'),
                   model_uri=PALS.rFParamGroup__harmon, domain=None, range=Optional[int])

slots.rFParamGroup__voltage = Slot(uri=PALS.voltage, name="rFParamGroup__voltage", curie=PALS.curie('voltage'),
                   model_uri=PALS.rFParamGroup__voltage, domain=None, range=Optional[float])

slots.rFParamGroup__gradient = Slot(uri=PALS.gradient, name="rFParamGroup__gradient", curie=PALS.curie('gradient'),
                   model_uri=PALS.rFParamGroup__gradient, domain=None, range=Optional[float])

slots.rFParamGroup__phase = Slot(uri=PALS.phase, name="rFParamGroup__phase", curie=PALS.curie('phase'),
                   model_uri=PALS.rFParamGroup__phase, domain=None, range=Optional[float])

slots.rFParamGroup__multipass_phase = Slot(uri=PALS.multipass_phase, name="rFParamGroup__multipass_phase", curie=PALS.curie('multipass_phase'),
                   model_uri=PALS.rFParamGroup__multipass_phase, domain=None, range=Optional[float])

slots.rFParamGroup__cavity_type = Slot(uri=PALS.cavity_type, name="rFParamGroup__cavity_type", curie=PALS.curie('cavity_type'),
                   model_uri=PALS.rFParamGroup__cavity_type, domain=None, range=Optional[Union[str, "CavityTypeEnum"]])

slots.rFParamGroup__num_cells = Slot(uri=PALS.num_cells, name="rFParamGroup__num_cells", curie=PALS.curie('num_cells'),
                   model_uri=PALS.rFParamGroup__num_cells, domain=None, range=Optional[int])

slots.rFParamGroup__zero_phase = Slot(uri=PALS.zero_phase, name="rFParamGroup__zero_phase", curie=PALS.curie('zero_phase'),
                   model_uri=PALS.rFParamGroup__zero_phase, domain=None, range=Optional[Union[str, "ZeroPhaseEnum"]])

slots.rFParamGroup__L_active = Slot(uri=PALS.L_active, name="rFParamGroup__L_active", curie=PALS.curie('L_active'),
                   model_uri=PALS.rFParamGroup__L_active, domain=None, range=Optional[float])

slots.rFParamGroup__dE_ref = Slot(uri=PALS.dE_ref, name="rFParamGroup__dE_ref", curie=PALS.curie('dE_ref'),
                   model_uri=PALS.rFParamGroup__dE_ref, domain=None, range=Optional[float])

slots.hasElectricMultipoleP__ElectricMultipoleP = Slot(uri=PALS.ElectricMultipoleP, name="hasElectricMultipoleP__ElectricMultipoleP", curie=PALS.curie('ElectricMultipoleP'),
                   model_uri=PALS.hasElectricMultipoleP__ElectricMultipoleP, domain=None, range=Optional[Union[dict, ElectricMultipoleParamGroup]])

slots.electricMultipoleParamGroup__elec_components = Slot(uri=PALS.elec_components, name="electricMultipoleParamGroup__elec_components", curie=PALS.curie('elec_components'),
                   model_uri=PALS.electricMultipoleParamGroup__elec_components, domain=None, range=Optional[Union[Union[dict, MultipoleParameterGroup], list[Union[dict, MultipoleParameterGroup]]]])

slots.hasMagneticMultipoleP__MagneticMultipoleP = Slot(uri=PALS.MagneticMultipoleP, name="hasMagneticMultipoleP__MagneticMultipoleP", curie=PALS.curie('MagneticMultipoleP'),
                   model_uri=PALS.hasMagneticMultipoleP__MagneticMultipoleP, domain=None, range=Optional[Union[dict, MagneticMultipoleParamGroup]])

slots.magneticMultipoleParamGroup__mag_components = Slot(uri=PALS.mag_components, name="magneticMultipoleParamGroup__mag_components", curie=PALS.curie('mag_components'),
                   model_uri=PALS.magneticMultipoleParamGroup__mag_components, domain=None, range=Optional[Union[Union[dict, MultipoleParameterGroup], list[Union[dict, MultipoleParameterGroup]]]])

slots.hasBendP__BendP = Slot(uri=PALS.BendP, name="hasBendP__BendP", curie=PALS.curie('BendP'),
                   model_uri=PALS.hasBendP__BendP, domain=None, range=Optional[Union[dict, BendParamGroup]])

slots.bendParamGroup__angle_ref = Slot(uri=PALS.angle_ref, name="bendParamGroup__angle_ref", curie=PALS.curie('angle_ref'),
                   model_uri=PALS.bendParamGroup__angle_ref, domain=None, range=Optional[float])

slots.bendParamGroup__Bn0_ref = Slot(uri=PALS.Bn0_ref, name="bendParamGroup__Bn0_ref", curie=PALS.curie('Bn0_ref'),
                   model_uri=PALS.bendParamGroup__Bn0_ref, domain=None, range=Optional[float])

slots.bendParamGroup__bend_field_actual = Slot(uri=PALS.bend_field_actual, name="bendParamGroup__bend_field_actual", curie=PALS.curie('bend_field_actual'),
                   model_uri=PALS.bendParamGroup__bend_field_actual, domain=None, range=Optional[float])

slots.bendParamGroup__e1 = Slot(uri=PALS.e1, name="bendParamGroup__e1", curie=PALS.curie('e1'),
                   model_uri=PALS.bendParamGroup__e1, domain=None, range=Optional[float])

slots.bendParamGroup__e2 = Slot(uri=PALS.e2, name="bendParamGroup__e2", curie=PALS.curie('e2'),
                   model_uri=PALS.bendParamGroup__e2, domain=None, range=Optional[float])

slots.bendParamGroup__e1_rect = Slot(uri=PALS.e1_rect, name="bendParamGroup__e1_rect", curie=PALS.curie('e1_rect'),
                   model_uri=PALS.bendParamGroup__e1_rect, domain=None, range=Optional[float])

slots.bendParamGroup__e2_rect = Slot(uri=PALS.e2_rect, name="bendParamGroup__e2_rect", curie=PALS.curie('e2_rect'),
                   model_uri=PALS.bendParamGroup__e2_rect, domain=None, range=Optional[float])

slots.bendParamGroup__edge1_int = Slot(uri=PALS.edge1_int, name="bendParamGroup__edge1_int", curie=PALS.curie('edge1_int'),
                   model_uri=PALS.bendParamGroup__edge1_int, domain=None, range=Optional[float])

slots.bendParamGroup__edge2_int = Slot(uri=PALS.edge2_int, name="bendParamGroup__edge2_int", curie=PALS.curie('edge2_int'),
                   model_uri=PALS.bendParamGroup__edge2_int, domain=None, range=Optional[float])

slots.bendParamGroup__g_ref = Slot(uri=PALS.g_ref, name="bendParamGroup__g_ref", curie=PALS.curie('g_ref'),
                   model_uri=PALS.bendParamGroup__g_ref, domain=None, range=Optional[float])

slots.bendParamGroup__g_actual = Slot(uri=PALS.g_actual, name="bendParamGroup__g_actual", curie=PALS.curie('g_actual'),
                   model_uri=PALS.bendParamGroup__g_actual, domain=None, range=Optional[float])

slots.bendParamGroup__h1 = Slot(uri=PALS.h1, name="bendParamGroup__h1", curie=PALS.curie('h1'),
                   model_uri=PALS.bendParamGroup__h1, domain=None, range=Optional[float])

slots.bendParamGroup__h2 = Slot(uri=PALS.h2, name="bendParamGroup__h2", curie=PALS.curie('h2'),
                   model_uri=PALS.bendParamGroup__h2, domain=None, range=Optional[float])

slots.bendParamGroup__Kn0_from_g_ref = Slot(uri=PALS.Kn0_from_g_ref, name="bendParamGroup__Kn0_from_g_ref", curie=PALS.curie('Kn0_from_g_ref'),
                   model_uri=PALS.bendParamGroup__Kn0_from_g_ref, domain=None, range=Optional[Union[bool, Bool]])

slots.bendParamGroup__L_chord = Slot(uri=PALS.L_chord, name="bendParamGroup__L_chord", curie=PALS.curie('L_chord'),
                   model_uri=PALS.bendParamGroup__L_chord, domain=None, range=Optional[float])

slots.bendParamGroup__L_sagitta = Slot(uri=PALS.L_sagitta, name="bendParamGroup__L_sagitta", curie=PALS.curie('L_sagitta'),
                   model_uri=PALS.bendParamGroup__L_sagitta, domain=None, range=Optional[float])

slots.bendParamGroup__L_rectangle = Slot(uri=PALS.L_rectangle, name="bendParamGroup__L_rectangle", curie=PALS.curie('L_rectangle'),
                   model_uri=PALS.bendParamGroup__L_rectangle, domain=None, range=Optional[float])

slots.bendParamGroup__multipole_geometry = Slot(uri=PALS.multipole_geometry, name="bendParamGroup__multipole_geometry", curie=PALS.curie('multipole_geometry'),
                   model_uri=PALS.bendParamGroup__multipole_geometry, domain=None, range=Optional[Union[str, "MultipoleGeometryEnum"]])

slots.bendParamGroup__ref_geometry = Slot(uri=PALS.ref_geometry, name="bendParamGroup__ref_geometry", curie=PALS.curie('ref_geometry'),
                   model_uri=PALS.bendParamGroup__ref_geometry, domain=None, range=Optional[Union[str, "ReferenceGeometryEnum"]])

slots.bendParamGroup__radius_ref = Slot(uri=PALS.radius_ref, name="bendParamGroup__radius_ref", curie=PALS.curie('radius_ref'),
                   model_uri=PALS.bendParamGroup__radius_ref, domain=None, range=Optional[float])

slots.bendParamGroup__tilt_ref = Slot(uri=PALS.tilt_ref, name="bendParamGroup__tilt_ref", curie=PALS.curie('tilt_ref'),
                   model_uri=PALS.bendParamGroup__tilt_ref, domain=None, range=Optional[float])

slots.multipoleParameterGroup__order = Slot(uri=PALS.order, name="multipoleParameterGroup__order", curie=PALS.curie('order'),
                   model_uri=PALS.multipoleParameterGroup__order, domain=None, range=int)

slots.multipoleParameterGroup__tilt = Slot(uri=PALS.tilt, name="multipoleParameterGroup__tilt", curie=PALS.curie('tilt'),
                   model_uri=PALS.multipoleParameterGroup__tilt, domain=None, range=Optional[float])

slots.multipoleParameterGroup__En = Slot(uri=PALS.En, name="multipoleParameterGroup__En", curie=PALS.curie('En'),
                   model_uri=PALS.multipoleParameterGroup__En, domain=None, range=Optional[float])

slots.multipoleParameterGroup__Es = Slot(uri=PALS.Es, name="multipoleParameterGroup__Es", curie=PALS.curie('Es'),
                   model_uri=PALS.multipoleParameterGroup__Es, domain=None, range=Optional[float])

slots.multipoleParameterGroup__EnL = Slot(uri=PALS.EnL, name="multipoleParameterGroup__EnL", curie=PALS.curie('EnL'),
                   model_uri=PALS.multipoleParameterGroup__EnL, domain=None, range=Optional[float])

slots.multipoleParameterGroup__EsL = Slot(uri=PALS.EsL, name="multipoleParameterGroup__EsL", curie=PALS.curie('EsL'),
                   model_uri=PALS.multipoleParameterGroup__EsL, domain=None, range=Optional[float])

slots.multipoleParameterGroup__Bn = Slot(uri=PALS.Bn, name="multipoleParameterGroup__Bn", curie=PALS.curie('Bn'),
                   model_uri=PALS.multipoleParameterGroup__Bn, domain=None, range=Optional[float])

slots.multipoleParameterGroup__Bs = Slot(uri=PALS.Bs, name="multipoleParameterGroup__Bs", curie=PALS.curie('Bs'),
                   model_uri=PALS.multipoleParameterGroup__Bs, domain=None, range=Optional[float])

slots.multipoleParameterGroup__BnL = Slot(uri=PALS.BnL, name="multipoleParameterGroup__BnL", curie=PALS.curie('BnL'),
                   model_uri=PALS.multipoleParameterGroup__BnL, domain=None, range=Optional[float])

slots.multipoleParameterGroup__BsL = Slot(uri=PALS.BsL, name="multipoleParameterGroup__BsL", curie=PALS.curie('BsL'),
                   model_uri=PALS.multipoleParameterGroup__BsL, domain=None, range=Optional[float])

slots.multipoleParameterGroup__Kn = Slot(uri=PALS.Kn, name="multipoleParameterGroup__Kn", curie=PALS.curie('Kn'),
                   model_uri=PALS.multipoleParameterGroup__Kn, domain=None, range=Optional[float])

slots.multipoleParameterGroup__Ks = Slot(uri=PALS.Ks, name="multipoleParameterGroup__Ks", curie=PALS.curie('Ks'),
                   model_uri=PALS.multipoleParameterGroup__Ks, domain=None, range=Optional[float])

slots.multipoleParameterGroup__KnL = Slot(uri=PALS.KnL, name="multipoleParameterGroup__KnL", curie=PALS.curie('KnL'),
                   model_uri=PALS.multipoleParameterGroup__KnL, domain=None, range=Optional[float])

slots.multipoleParameterGroup__KsL = Slot(uri=PALS.KsL, name="multipoleParameterGroup__KsL", curie=PALS.curie('KsL'),
                   model_uri=PALS.multipoleParameterGroup__KsL, domain=None, range=Optional[float])

slots.component__native_types = Slot(uri=PALS.native_types, name="component__native_types", curie=PALS.curie('native_types'),
                   model_uri=PALS.component__native_types, domain=None, range=Optional[Union[str, list[str]]])

slots.physicalComponent__functions = Slot(uri=PALS.physical_function, name="physicalComponent__functions", curie=PALS.curie('physical_function'),
                   model_uri=PALS.physicalComponent__functions, domain=None, range=Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]])

slots.physicalComponent__beamline_relation = Slot(uri=PALS.physical_beamline_relation, name="physicalComponent__beamline_relation", curie=PALS.curie('physical_beamline_relation'),
                   model_uri=PALS.physicalComponent__beamline_relation, domain=None, range=Union[str, "PhysicalRelationEnum"])

slots.virtualComponent__functions = Slot(uri=PALS.virtual_function, name="virtualComponent__functions", curie=PALS.curie('virtual_function'),
                   model_uri=PALS.virtualComponent__functions, domain=None, range=Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]])

slots.virtualComponent__beamline_relation = Slot(uri=PALS.virtual_beamline_relation, name="virtualComponent__beamline_relation", curie=PALS.curie('virtual_beamline_relation'),
                   model_uri=PALS.virtualComponent__beamline_relation, domain=None, range=Union[str, "VirtualRelationEnum"])

slots.beamLine__multipass = Slot(uri=PALS.multipass, name="beamLine__multipass", curie=PALS.curie('multipass'),
                   model_uri=PALS.beamLine__multipass, domain=None, range=Optional[Union[bool, Bool]])

slots.beamLine__periodic = Slot(uri=PALS.periodic, name="beamLine__periodic", curie=PALS.curie('periodic'),
                   model_uri=PALS.beamLine__periodic, domain=None, range=Optional[Union[bool, Bool]])

slots.beamLine__repeat = Slot(uri=PALS.repeat, name="beamLine__repeat", curie=PALS.curie('repeat'),
                   model_uri=PALS.beamLine__repeat, domain=None, range=Optional[int])

slots.beamLine__direction = Slot(uri=PALS.direction, name="beamLine__direction", curie=PALS.curie('direction'),
                   model_uri=PALS.beamLine__direction, domain=None, range=Optional[int])

slots.signal__signal_role = Slot(uri=PALS.signal_role, name="signal__signal_role", curie=PALS.curie('signal_role'),
                   model_uri=PALS.signal__signal_role, domain=None, range=Union[str, "SignalRoleEnum"])

slots.signal__source_system = Slot(uri=PALS.source_system, name="signal__source_system", curie=PALS.curie('source_system'),
                   model_uri=PALS.signal__source_system, domain=None, range=Union[str, "SourceSystemEnum"])

slots.signal__native_description = Slot(uri=PALS.native_description, name="signal__native_description", curie=PALS.curie('native_description'),
                   model_uri=PALS.signal__native_description, domain=None, range=Optional[str])

slots.signal__canonical_signal_type = Slot(uri=PALS.canonical_signal_type, name="signal__canonical_signal_type", curie=PALS.curie('canonical_signal_type'),
                   model_uri=PALS.signal__canonical_signal_type, domain=None, range=Union[str, "CanonicalSignalTypeEnum"])

slots.signal__quantity_kind = Slot(uri=PALS.quantity_kind, name="signal__quantity_kind", curie=PALS.curie('quantity_kind'),
                   model_uri=PALS.signal__quantity_kind, domain=None, range=Union[str, "QuantityKindEnum"])

slots.signal__native_data_type = Slot(uri=PALS.native_data_type, name="signal__native_data_type", curie=PALS.curie('native_data_type'),
                   model_uri=PALS.signal__native_data_type, domain=None, range=Union[str, "DataTypeEnum"])

slots.signal__native_unit = Slot(uri=PALS.native_unit, name="signal__native_unit", curie=PALS.curie('native_unit'),
                   model_uri=PALS.signal__native_unit, domain=None, range=Union[str, "UnitEnum"])

slots.signal__access_protocol = Slot(uri=PALS.access_protocol, name="signal__access_protocol", curie=PALS.curie('access_protocol'),
                   model_uri=PALS.signal__access_protocol, domain=None, range=Optional[str])

slots.signal__archive_identifier = Slot(uri=PALS.archive_identifier, name="signal__archive_identifier", curie=PALS.curie('archive_identifier'),
                   model_uri=PALS.signal__archive_identifier, domain=None, range=Optional[str])

slots.kicker__plane = Slot(uri=PALS.plane, name="kicker__plane", curie=PALS.curie('plane'),
                   model_uri=PALS.kicker__plane, domain=None, range=Optional[Union[str, "PlaneEnum"]])

slots.supportingFacilityComponent__functions = Slot(uri=PALS.supporting_facility_function, name="supportingFacilityComponent__functions", curie=PALS.curie('supporting_facility_function'),
                   model_uri=PALS.supportingFacilityComponent__functions, domain=None, range=Union[Union[str, "FacilityFunctionEnum"], list[Union[str, "FacilityFunctionEnum"]]])

slots.additionalMetadata__key = Slot(uri=PALS.key, name="additionalMetadata__key", curie=PALS.curie('key'),
                   model_uri=PALS.additionalMetadata__key, domain=None, range=str)

slots.additionalMetadata__value = Slot(uri=PALS.value, name="additionalMetadata__value", curie=PALS.curie('value'),
                   model_uri=PALS.additionalMetadata__value, domain=None, range=str)

slots.additionalMetadata__datatype = Slot(uri=PALS.datatype, name="additionalMetadata__datatype", curie=PALS.curie('datatype'),
                   model_uri=PALS.additionalMetadata__datatype, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.componentRelation__component_direction = Slot(uri=PALS.component_direction, name="componentRelation__component_direction", curie=PALS.curie('component_direction'),
                   model_uri=PALS.componentRelation__component_direction, domain=None, range=Optional[Union[str, "DirectionEnum"]])

slots.componentRelation__reference_frame = Slot(uri=PALS.reference_frame, name="componentRelation__reference_frame", curie=PALS.curie('reference_frame'),
                   model_uri=PALS.componentRelation__reference_frame, domain=None, range=Optional[Union[str, "ReferenceFrameEnum"]])

slots.coordinateSet__coordinate_system = Slot(uri=PALS.coordinate_system, name="coordinateSet__coordinate_system", curie=PALS.curie('coordinate_system'),
                   model_uri=PALS.coordinateSet__coordinate_system, domain=None, range=Optional[Union[str, "CoordinateSystemEnum"]])

slots.coordinateSet__x_coord = Slot(uri=PALS.x_coord, name="coordinateSet__x_coord", curie=PALS.curie('x_coord'),
                   model_uri=PALS.coordinateSet__x_coord, domain=None, range=Optional[float])

slots.coordinateSet__y_coord = Slot(uri=PALS.y_coord, name="coordinateSet__y_coord", curie=PALS.curie('y_coord'),
                   model_uri=PALS.coordinateSet__y_coord, domain=None, range=Optional[float])

slots.coordinateSet__z_coord = Slot(uri=PALS.z_coord, name="coordinateSet__z_coord", curie=PALS.curie('z_coord'),
                   model_uri=PALS.coordinateSet__z_coord, domain=None, range=Optional[float])

slots.coordinateSet__r_coord = Slot(uri=PALS.r_coord, name="coordinateSet__r_coord", curie=PALS.curie('r_coord'),
                   model_uri=PALS.coordinateSet__r_coord, domain=None, range=Optional[float])

slots.coordinateSet__theta_coord = Slot(uri=PALS.theta_coord, name="coordinateSet__theta_coord", curie=PALS.curie('theta_coord'),
                   model_uri=PALS.coordinateSet__theta_coord, domain=None, range=Optional[float])

slots.coordinateSet__phi_coord = Slot(uri=PALS.phi_coord, name="coordinateSet__phi_coord", curie=PALS.curie('phi_coord'),
                   model_uri=PALS.coordinateSet__phi_coord, domain=None, range=Optional[float])

slots.BeamLine_length = Slot(uri=PALS.length, name="BeamLine_length", curie=PALS.curie('length'),
                   model_uri=PALS.BeamLine_length, domain=BeamLine, range=Optional[float])

slots.SignalBinding_subject = Slot(uri=RDF.subject, name="SignalBinding_subject", curie=RDF.curie('subject'),
                   model_uri=PALS.SignalBinding_subject, domain=SignalBinding, range=Union[str, PhysicalComponentId])

slots.SignalBinding_object = Slot(uri=RDF.object, name="SignalBinding_object", curie=RDF.curie('object'),
                   model_uri=PALS.SignalBinding_object, domain=SignalBinding, range=Union[str, SignalId])

slots.HasSignal_predicate = Slot(uri=RDF.predicate, name="HasSignal_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.HasSignal_predicate, domain=HasSignal, range=Union[str, URIorCURIE])

slots.HasSetpointSignal_predicate = Slot(uri=RDF.predicate, name="HasSetpointSignal_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.HasSetpointSignal_predicate, domain=HasSetpointSignal, range=Union[str, URIorCURIE])

slots.HasReadbackSignal_predicate = Slot(uri=RDF.predicate, name="HasReadbackSignal_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.HasReadbackSignal_predicate, domain=HasReadbackSignal, range=Union[str, URIorCURIE])

slots.HasCommandSignal_predicate = Slot(uri=RDF.predicate, name="HasCommandSignal_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.HasCommandSignal_predicate, domain=HasCommandSignal, range=Union[str, URIorCURIE])

slots.HasLimitSignal_predicate = Slot(uri=RDF.predicate, name="HasLimitSignal_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.HasLimitSignal_predicate, domain=HasLimitSignal, range=Union[str, URIorCURIE])

slots.ComponentRelation_subject = Slot(uri=RDF.subject, name="ComponentRelation_subject", curie=RDF.curie('subject'),
                   model_uri=PALS.ComponentRelation_subject, domain=ComponentRelation, range=Union[str, ComponentId])

slots.ComponentRelation_object = Slot(uri=RDF.object, name="ComponentRelation_object", curie=RDF.curie('object'),
                   model_uri=PALS.ComponentRelation_object, domain=ComponentRelation, range=Union[str, ComponentId])

slots.Precedes_predicate = Slot(uri=RDF.predicate, name="Precedes_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.Precedes_predicate, domain=Precedes, range=Union[str, URIorCURIE])

slots.Precedes_context = Slot(uri=PALS.context, name="Precedes_context", curie=PALS.curie('context'),
                   model_uri=PALS.Precedes_context, domain=Precedes, range=Union[str, "RelationContextEnum"])

slots.Contains_predicate = Slot(uri=RDF.predicate, name="Contains_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.Contains_predicate, domain=Contains, range=Union[str, URIorCURIE])

slots.Controls_predicate = Slot(uri=RDF.predicate, name="Controls_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.Controls_predicate, domain=Controls, range=Union[str, URIorCURIE])

slots.IsPartOf_predicate = Slot(uri=RDF.predicate, name="IsPartOf_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.IsPartOf_predicate, domain=IsPartOf, range=Union[str, URIorCURIE])

slots.AdjacentTo_predicate = Slot(uri=RDF.predicate, name="AdjacentTo_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.AdjacentTo_predicate, domain=AdjacentTo, range=Union[str, URIorCURIE])

slots.Overlaps_predicate = Slot(uri=RDF.predicate, name="Overlaps_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.Overlaps_predicate, domain=Overlaps, range=Union[str, URIorCURIE])

slots.HasConnectingBranch_predicate = Slot(uri=RDF.predicate, name="HasConnectingBranch_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.HasConnectingBranch_predicate, domain=HasConnectingBranch, range=Union[str, URIorCURIE])

slots.HasConnectingBranch_context = Slot(uri=PALS.context, name="HasConnectingBranch_context", curie=PALS.curie('context'),
                   model_uri=PALS.HasConnectingBranch_context, domain=HasConnectingBranch, range=Union[str, "RelationContextEnum"])

slots.MountedOn_predicate = Slot(uri=RDF.predicate, name="MountedOn_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.MountedOn_predicate, domain=MountedOn, range=Union[str, URIorCURIE])

slots.Intersects_predicate = Slot(uri=RDF.predicate, name="Intersects_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.Intersects_predicate, domain=Intersects, range=Union[str, URIorCURIE])

slots.NearestTo_predicate = Slot(uri=RDF.predicate, name="NearestTo_predicate", curie=RDF.curie('predicate'),
                   model_uri=PALS.NearestTo_predicate, domain=NearestTo, range=Union[str, URIorCURIE])
