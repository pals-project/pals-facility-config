# Auto generated from narad.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-14T12:50:21
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

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
ACC = CurieNamespace('acc', 'https://w3id.org/accelerator-core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NARAD = CurieNamespace('narad', 'https://example.org/narad/')
PALS = CurieNamespace('pals', 'https://pals-project.readthedocs.io/')
QUANTITYKIND = CurieNamespace('quantitykind', 'http://qudt.org/vocab/quantitykind/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SAREF = CurieNamespace('saref', 'https://saref.etsi.org/core/v4.1.1/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
UNIT = CurieNamespace('unit', 'http://qudt.org/vocab/unit/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NARAD


# Types

# Class references
class ComponentId(extended_str):
    pass


class PhysicalComponentId(ComponentId):
    pass


class VirtualComponentId(ComponentId):
    pass


class BeamlineId(VirtualComponentId):
    pass


class SignalId(extended_str):
    pass


class MagnetId(PhysicalComponentId):
    pass


class SolenoidId(MagnetId):
    pass


class MultipoleId(MagnetId):
    pass


class DipoleId(MultipoleId):
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


class BeamPositionMonitorId(DiagnosticDeviceId):
    pass


class RadiationMonitorId(DiagnosticDeviceId):
    pass


class CavityId(PhysicalComponentId):
    pass


class CrabCavityId(CavityId):
    pass


class RFCavityId(CavityId):
    pass


class SuperconductingRFCavityId(RFCavityId):
    pass


class SupportingFacilityComponentId(PhysicalComponentId):
    pass


class BookkeepingComponentId(VirtualComponentId):
    pass


class MarkerId(BookkeepingComponentId):
    pass


class BeamlineSectionId(BookkeepingComponentId):
    pass


class MetadataEntryKey(extended_str):
    pass


class RelationshipId(extended_str):
    pass


class SignalBindingId(RelationshipId):
    pass


class ComponentRelationId(RelationshipId):
    pass


@dataclass(repr=False)
class NARAD(YAMLRoot):
    """
    Root container for accelerator core components, semantic signals, and local bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["NARAD"]
    class_class_curie: ClassVar[str] = "narad:NARAD"
    class_name: ClassVar[str] = "NARAD"
    class_model_uri: ClassVar[URIRef] = NARAD.NARAD

    type: str = None
    description: Optional[str] = None
    physical_components: Optional[Union[dict[Union[str, PhysicalComponentId], Union[dict, "PhysicalComponent"]], list[Union[dict, "PhysicalComponent"]]]] = empty_dict()
    virtual_components: Optional[Union[dict[Union[str, VirtualComponentId], Union[dict, "VirtualComponent"]], list[Union[dict, "VirtualComponent"]]]] = empty_dict()
    beamlines: Optional[Union[dict[Union[str, BeamlineId], Union[dict, "Beamline"]], list[Union[dict, "Beamline"]]]] = empty_dict()
    supporting_facility_components: Optional[Union[dict[Union[str, SupportingFacilityComponentId], Union[dict, "SupportingFacilityComponent"]], list[Union[dict, "SupportingFacilityComponent"]]]] = empty_dict()
    signals: Optional[Union[dict[Union[str, SignalId], Union[dict, "Signal"]], list[Union[dict, "Signal"]]]] = empty_dict()
    signal_bindings: Optional[Union[dict[Union[str, SignalBindingId], Union[dict, "SignalBinding"]], list[Union[dict, "SignalBinding"]]]] = empty_dict()
    component_relations: Optional[Union[dict[Union[str, ComponentRelationId], Union[dict, "ComponentRelation"]], list[Union[dict, "ComponentRelation"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="physical_components", slot_type=PhysicalComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="virtual_components", slot_type=VirtualComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="beamlines", slot_type=Beamline, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="supporting_facility_components", slot_type=SupportingFacilityComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signal_bindings", slot_type=SignalBinding, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="component_relations", slot_type=ComponentRelation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetaP(YAMLRoot):
    """
    Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability
    with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["MetaP"]
    class_class_curie: ClassVar[str] = "narad:MetaP"
    class_name: ClassVar[str] = "MetaP"
    class_model_uri: ClassVar[URIRef] = NARAD.MetaP

    description: Optional[str] = None
    label: Optional[str] = None
    alias: Optional[str] = None
    additional_metadata: Optional[Union[dict[Union[str, MetadataEntryKey], Union[dict, "MetadataEntry"]], list[Union[dict, "MetadataEntry"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        self._normalize_inlined_as_list(slot_name="additional_metadata", slot_type=MetadataEntry, key_name="key", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FloorP(YAMLRoot):
    """
    Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for
    interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["FloorP"]
    class_class_curie: ClassVar[str] = "narad:FloorP"
    class_name: ClassVar[str] = "FloorP"
    class_model_uri: ClassVar[URIRef] = NARAD.FloorP

    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    theta: Optional[float] = None
    phi: Optional[float] = None
    psi: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
class BodyShiftP(YAMLRoot):
    """
    Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)
    for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BodyShiftP"]
    class_class_curie: ClassVar[str] = "narad:BodyShiftP"
    class_name: ClassVar[str] = "BodyShiftP"
    class_model_uri: ClassVar[URIRef] = NARAD.BodyShiftP

    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
class HasLongitudinalPlacement(YAMLRoot):
    """
    Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.
    Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
    One (or both) `length` or `s_position` must be present.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["HasLongitudinalPlacement"]
    class_class_curie: ClassVar[str] = "narad:HasLongitudinalPlacement"
    class_name: ClassVar[str] = "HasLongitudinalPlacement"
    class_model_uri: ClassVar[URIRef] = NARAD.HasLongitudinalPlacement

    length: Optional[float] = None
    s_position: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.s_position is not None and not isinstance(self.s_position, float):
            self.s_position = float(self.s_position)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceP(YAMLRoot):
    """
    Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability
    with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ReferenceP"]
    class_class_curie: ClassVar[str] = "narad:ReferenceP"
    class_name: ClassVar[str] = "ReferenceP"
    class_model_uri: ClassVar[URIRef] = NARAD.ReferenceP

    species_ref: Optional[str] = None
    pc_ref: Optional[float] = None
    E_tot_ref: Optional[float] = None
    time_ref: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
class SolenoidP(YAMLRoot):
    """
    Mixin for solenoid-specific parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SolenoidP"]
    class_class_curie: ClassVar[str] = "narad:SolenoidP"
    class_name: ClassVar[str] = "SolenoidP"
    class_model_uri: ClassVar[URIRef] = NARAD.SolenoidP

    Ksol: Optional[float] = None
    Bsol: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Ksol is not None and not isinstance(self.Ksol, float):
            self.Ksol = float(self.Ksol)

        if self.Bsol is not None and not isinstance(self.Bsol, float):
            self.Bsol = float(self.Bsol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TwissP(YAMLRoot):
    """
    Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["TwissP"]
    class_class_curie: ClassVar[str] = "narad:TwissP"
    class_name: ClassVar[str] = "TwissP"
    class_model_uri: ClassVar[URIRef] = NARAD.TwissP

    alpha_a: Optional[float] = None
    alpha_b: Optional[float] = None
    beta_a: Optional[float] = None
    beta_b: Optional[float] = None
    eta_x: Optional[float] = None
    eta_y: Optional[float] = None
    etap_x: Optional[float] = None
    etap_y: Optional[float] = None
    phi_a: Optional[float] = None
    phi_b: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.alpha_a is not None and not isinstance(self.alpha_a, float):
            self.alpha_a = float(self.alpha_a)

        if self.alpha_b is not None and not isinstance(self.alpha_b, float):
            self.alpha_b = float(self.alpha_b)

        if self.beta_a is not None and not isinstance(self.beta_a, float):
            self.beta_a = float(self.beta_a)

        if self.beta_b is not None and not isinstance(self.beta_b, float):
            self.beta_b = float(self.beta_b)

        if self.eta_x is not None and not isinstance(self.eta_x, float):
            self.eta_x = float(self.eta_x)

        if self.eta_y is not None and not isinstance(self.eta_y, float):
            self.eta_y = float(self.eta_y)

        if self.etap_x is not None and not isinstance(self.etap_x, float):
            self.etap_x = float(self.etap_x)

        if self.etap_y is not None and not isinstance(self.etap_y, float):
            self.etap_y = float(self.etap_y)

        if self.phi_a is not None and not isinstance(self.phi_a, float):
            self.phi_a = float(self.phi_a)

        if self.phi_b is not None and not isinstance(self.phi_b, float):
            self.phi_b = float(self.phi_b)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectricMultipoleP(YAMLRoot):
    """
    Mixin for electric multipole parameters,
    which can be used to describe the electric field components of an accelerator element.
    This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language
    Standard (PALS).
    Example with three multipole components (N=0,1,2): ```yaml components: - order: 7
    tilt: 0.7
    - order: 3
    En: 27.3
    - order: 2
    EnL: 3.47e1
    ```
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ElectricMultipoleP"]
    class_class_curie: ClassVar[str] = "narad:ElectricMultipoleP"
    class_name: ClassVar[str] = "ElectricMultipoleP"
    class_model_uri: ClassVar[URIRef] = NARAD.ElectricMultipoleP

    components: Optional[Union[Union[dict, "MultipoleComponent"], list[Union[dict, "MultipoleComponent"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, MultipoleComponent) else MultipoleComponent(**as_dict(v)) for v in self.components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MagneticMultipoleP(YAMLRoot):
    """
    Mixin for magnetic multipole parameters,
    which can be used to describe the magnetic field components of an accelerator element.
    This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language
    Standard (PALS).
    Example with three multipole components (N=0,1,2): ```yaml components: - order: 7
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

    class_class_uri: ClassVar[URIRef] = NARAD["MagneticMultipoleP"]
    class_class_curie: ClassVar[str] = "narad:MagneticMultipoleP"
    class_name: ClassVar[str] = "MagneticMultipoleP"
    class_model_uri: ClassVar[URIRef] = NARAD.MagneticMultipoleP

    components: Optional[Union[Union[dict, "MultipoleComponent"], list[Union[dict, "MultipoleComponent"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, MultipoleComponent) else MultipoleComponent(**as_dict(v)) for v in self.components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BendP(YAMLRoot):
    """
    Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.
    This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BendP"]
    class_class_curie: ClassVar[str] = "narad:BendP"
    class_name: ClassVar[str] = "BendP"
    class_model_uri: ClassVar[URIRef] = NARAD.BendP

    angle_ref: Optional[float] = None
    bend_field_ref: Optional[float] = None
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
    L_chord: Optional[float] = None
    L_sagitta: Optional[float] = None
    L_rectangle: Optional[float] = None
    multipole_geometry: Optional[Union[str, "MultipoleGeometryEnum"]] = None
    ref_geometry: Optional[Union[str, "ReferenceGeometryEnum"]] = None
    rho_ref: Optional[float] = None
    tilt_ref: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.angle_ref is not None and not isinstance(self.angle_ref, float):
            self.angle_ref = float(self.angle_ref)

        if self.bend_field_ref is not None and not isinstance(self.bend_field_ref, float):
            self.bend_field_ref = float(self.bend_field_ref)

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

        if self.rho_ref is not None and not isinstance(self.rho_ref, float):
            self.rho_ref = float(self.rho_ref)

        if self.tilt_ref is not None and not isinstance(self.tilt_ref, float):
            self.tilt_ref = float(self.tilt_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultipoleComponent(YAMLRoot):
    """
    A single order's electric (or magnetic) multipole component.
    Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.
    Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual
    multipole components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["MultipoleComponent"]
    class_class_curie: ClassVar[str] = "narad:MultipoleComponent"
    class_name: ClassVar[str] = "MultipoleComponent"
    class_model_uri: ClassVar[URIRef] = NARAD.MultipoleComponent

    order: int = None
    tilt: Optional[float] = None
    En: Optional[float] = None
    Es: Optional[float] = None
    EnL: Optional[float] = None
    EsL: Optional[float] = None
    Bn: Optional[float] = None
    Bs: Optional[float] = None
    Kn: Optional[float] = None
    Ks: Optional[float] = None

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

        if self.Kn is not None and not isinstance(self.Kn, float):
            self.Kn = float(self.Kn)

        if self.Ks is not None and not isinstance(self.Ks, float):
            self.Ks = float(self.Ks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Component(YAMLRoot):
    """
    A general class for accelerator components, which can be specialized into more specific types like
    AcceleratorDevice, Magnet, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Component"]
    class_class_curie: ClassVar[str] = "narad:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = NARAD.Component

    id: Union[str, ComponentId] = None
    type: str = None
    native_types: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    label: Optional[str] = None
    alias: Optional[str] = None
    additional_metadata: Optional[Union[dict[Union[str, MetadataEntryKey], Union[dict, "MetadataEntry"]], list[Union[dict, "MetadataEntry"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.native_types, list):
            self.native_types = [self.native_types] if self.native_types is not None else []
        self.native_types = [v if isinstance(v, str) else str(v) for v in self.native_types]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        self._normalize_inlined_as_list(slot_name="additional_metadata", slot_type=MetadataEntry, key_name="key", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalComponent(Component):
    """
    A physical item that participates in or supports accelerator operation. This can be used to capture physical
    components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding
    the structure and function of the accelerator system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["PhysicalComponent"]
    class_class_curie: ClassVar[str] = "narad:PhysicalComponent"
    class_name: ClassVar[str] = "PhysicalComponent"
    class_model_uri: ClassVar[URIRef] = NARAD.PhysicalComponent

    id: Union[str, PhysicalComponentId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    theta: Optional[float] = None
    phi: Optional[float] = None
    psi: Optional[float] = None
    length: Optional[float] = None
    s_position: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalComponentId):
            self.id = PhysicalComponentId(self.id)

        if self._is_empty(self.functions):
            self.MissingRequiredField("functions")
        if not isinstance(self.functions, list):
            self.functions = [self.functions] if self.functions is not None else []
        self.functions = [v if isinstance(v, PhysicalFunctionEnum) else PhysicalFunctionEnum(v) for v in self.functions]

        if self._is_empty(self.beamline_relation):
            self.MissingRequiredField("beamline_relation")
        if not isinstance(self.beamline_relation, PhysicalRelationEnum):
            self.beamline_relation = PhysicalRelationEnum(self.beamline_relation)

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

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.s_position is not None and not isinstance(self.s_position, float):
            self.s_position = float(self.s_position)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirtualComponent(Component):
    """
    A virtual or logical component that represents a concept, function, or role in the accelerator beamline operation
    but does not have a physical instantiation. This can be used to capture abstract components, such as Markers,
    BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the
    accelerator system but are not physical devices.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["VirtualComponent"]
    class_class_curie: ClassVar[str] = "narad:VirtualComponent"
    class_name: ClassVar[str] = "VirtualComponent"
    class_model_uri: ClassVar[URIRef] = NARAD.VirtualComponent

    id: Union[str, VirtualComponentId] = None
    type: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    theta: Optional[float] = None
    phi: Optional[float] = None
    psi: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirtualComponentId):
            self.id = VirtualComponentId(self.id)

        if self._is_empty(self.functions):
            self.MissingRequiredField("functions")
        if not isinstance(self.functions, list):
            self.functions = [self.functions] if self.functions is not None else []
        self.functions = [v if isinstance(v, VirtualFunctionEnum) else VirtualFunctionEnum(v) for v in self.functions]

        if self._is_empty(self.beamline_relation):
            self.MissingRequiredField("beamline_relation")
        if not isinstance(self.beamline_relation, VirtualRelationEnum):
            self.beamline_relation = VirtualRelationEnum(self.beamline_relation)

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
class Beamline(VirtualComponent):
    """
    A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Beamline"]
    class_class_curie: ClassVar[str] = "narad:Beamline"
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = NARAD.Beamline

    id: Union[str, BeamlineId] = None
    type: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    multipass: Optional[Union[bool, Bool]] = None
    length: Optional[float] = None
    zero_point: Optional[str] = None
    periodic: Optional[Union[bool, Bool]] = None
    repeat: Optional[int] = None
    direction: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineId):
            self.id = BeamlineId(self.id)

        if self.multipass is not None and not isinstance(self.multipass, Bool):
            self.multipass = Bool(self.multipass)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.zero_point is not None and not isinstance(self.zero_point, str):
            self.zero_point = str(self.zero_point)

        if self.periodic is not None and not isinstance(self.periodic, Bool):
            self.periodic = Bool(self.periodic)

        if self.repeat is not None and not isinstance(self.repeat, int):
            self.repeat = int(self.repeat)

        if self.direction is not None and not isinstance(self.direction, int):
            self.direction = int(self.direction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signal(YAMLRoot):
    """
    Semantic meaning of a control-system signal associated with a component.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Signal"]
    class_class_curie: ClassVar[str] = "narad:Signal"
    class_name: ClassVar[str] = "Signal"
    class_model_uri: ClassVar[URIRef] = NARAD.Signal

    id: Union[str, SignalId] = None
    type: str = None
    signal_role: Union[str, "SignalRoleEnum"] = None
    source_system: Union[str, "SourceSystemEnum"] = None
    canonical_signal_type: Union[str, "CanonicalSignalTypeEnum"] = None
    quantity_kind: Union[str, "QuantityKindEnum"] = None
    native_data_type: Union[str, "DataTypeEnum"] = None
    native_unit: Union[str, "UnitEnum"] = None
    native_description: Optional[str] = None
    access_protocol: Optional[str] = None
    archive_identifier: Optional[str] = None
    description: Optional[str] = None
    label: Optional[str] = None
    alias: Optional[str] = None
    additional_metadata: Optional[Union[dict[Union[str, MetadataEntryKey], Union[dict, "MetadataEntry"]], list[Union[dict, "MetadataEntry"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignalId):
            self.id = SignalId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

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

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        self._normalize_inlined_as_list(slot_name="additional_metadata", slot_type=MetadataEntry, key_name="key", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Magnet(PhysicalComponent):
    """
    An accelerator device that produces a magnetic field for beam control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Magnet"]
    class_class_curie: ClassVar[str] = "narad:Magnet"
    class_name: ClassVar[str] = "Magnet"
    class_model_uri: ClassVar[URIRef] = NARAD.Magnet

    id: Union[str, MagnetId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    species_ref: Optional[str] = None
    pc_ref: Optional[float] = None
    E_tot_ref: Optional[float] = None
    time_ref: Optional[float] = None
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None
    alpha_a: Optional[float] = None
    alpha_b: Optional[float] = None
    beta_a: Optional[float] = None
    beta_b: Optional[float] = None
    eta_x: Optional[float] = None
    eta_y: Optional[float] = None
    etap_x: Optional[float] = None
    etap_y: Optional[float] = None
    phi_a: Optional[float] = None
    phi_b: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.species_ref is not None and not isinstance(self.species_ref, str):
            self.species_ref = str(self.species_ref)

        if self.pc_ref is not None and not isinstance(self.pc_ref, float):
            self.pc_ref = float(self.pc_ref)

        if self.E_tot_ref is not None and not isinstance(self.E_tot_ref, float):
            self.E_tot_ref = float(self.E_tot_ref)

        if self.time_ref is not None and not isinstance(self.time_ref, float):
            self.time_ref = float(self.time_ref)

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

        if self.alpha_a is not None and not isinstance(self.alpha_a, float):
            self.alpha_a = float(self.alpha_a)

        if self.alpha_b is not None and not isinstance(self.alpha_b, float):
            self.alpha_b = float(self.alpha_b)

        if self.beta_a is not None and not isinstance(self.beta_a, float):
            self.beta_a = float(self.beta_a)

        if self.beta_b is not None and not isinstance(self.beta_b, float):
            self.beta_b = float(self.beta_b)

        if self.eta_x is not None and not isinstance(self.eta_x, float):
            self.eta_x = float(self.eta_x)

        if self.eta_y is not None and not isinstance(self.eta_y, float):
            self.eta_y = float(self.eta_y)

        if self.etap_x is not None and not isinstance(self.etap_x, float):
            self.etap_x = float(self.etap_x)

        if self.etap_y is not None and not isinstance(self.etap_y, float):
            self.etap_y = float(self.etap_y)

        if self.phi_a is not None and not isinstance(self.phi_a, float):
            self.phi_a = float(self.phi_a)

        if self.phi_b is not None and not isinstance(self.phi_b, float):
            self.phi_b = float(self.phi_b)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Solenoid(Magnet):
    """
    A magnet with a primarily longitudinal magnetic field used for focusing.
    A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic
    axis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Solenoid"]
    class_class_curie: ClassVar[str] = "narad:Solenoid"
    class_name: ClassVar[str] = "Solenoid"
    class_model_uri: ClassVar[URIRef] = NARAD.Solenoid

    id: Union[str, SolenoidId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    Ksol: Optional[float] = None
    Bsol: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolenoidId):
            self.id = SolenoidId(self.id)

        if self.Ksol is not None and not isinstance(self.Ksol, float):
            self.Ksol = float(self.Ksol)

        if self.Bsol is not None and not isinstance(self.Bsol, float):
            self.Bsol = float(self.Bsol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Multipole(Magnet):
    """
    A general magnet with a higher-order multipole field, such as a sextupole or octupole.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Multipole"]
    class_class_curie: ClassVar[str] = "narad:Multipole"
    class_name: ClassVar[str] = "Multipole"
    class_model_uri: ClassVar[URIRef] = NARAD.Multipole

    id: Union[str, MultipoleId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    components: Optional[Union[Union[dict, MultipoleComponent], list[Union[dict, MultipoleComponent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MultipoleId):
            self.id = MultipoleId(self.id)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, MultipoleComponent) else MultipoleComponent(**as_dict(v)) for v in self.components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dipole(Multipole):
    """
    A magnet primarily used to bend the beam. 2 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Dipole"]
    class_class_curie: ClassVar[str] = "narad:Dipole"
    class_name: ClassVar[str] = "Dipole"
    class_model_uri: ClassVar[URIRef] = NARAD.Dipole

    id: Union[str, DipoleId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DipoleId):
            self.id = DipoleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bend(Multipole):
    """
    Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical
    elements is that with a Bend the curvilinear coordinate system is an arc with finite curvature and for the other
    elements the curvilinear coordinate system is straight.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Bend"]
    class_class_curie: ClassVar[str] = "narad:Bend"
    class_name: ClassVar[str] = "Bend"
    class_model_uri: ClassVar[URIRef] = NARAD.Bend

    id: Union[str, BendId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BendId):
            self.id = BendId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quadrupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 4 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Quadrupole"]
    class_class_curie: ClassVar[str] = "narad:Quadrupole"
    class_name: ClassVar[str] = "Quadrupole"
    class_model_uri: ClassVar[URIRef] = NARAD.Quadrupole

    id: Union[str, QuadrupoleId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuadrupoleId):
            self.id = QuadrupoleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Octupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 8 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Octupole"]
    class_class_curie: ClassVar[str] = "narad:Octupole"
    class_name: ClassVar[str] = "Octupole"
    class_model_uri: ClassVar[URIRef] = NARAD.Octupole

    id: Union[str, OctupoleId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OctupoleId):
            self.id = OctupoleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sextupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 6 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Sextupole"]
    class_class_curie: ClassVar[str] = "narad:Sextupole"
    class_name: ClassVar[str] = "Sextupole"
    class_model_uri: ClassVar[URIRef] = NARAD.Sextupole

    id: Union[str, SextupoleId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SextupoleId):
            self.id = SextupoleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kicker(Magnet):
    """
    A magnet primarily used to steer the beam.
    Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the
    kicker.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Kicker"]
    class_class_curie: ClassVar[str] = "narad:Kicker"
    class_name: ClassVar[str] = "Kicker"
    class_model_uri: ClassVar[URIRef] = NARAD.Kicker

    id: Union[str, KickerId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    plane: Optional[Union[str, "PlaneEnum"]] = None
    components: Optional[Union[Union[dict, MultipoleComponent], list[Union[dict, MultipoleComponent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KickerId):
            self.id = KickerId(self.id)

        if self.plane is not None and not isinstance(self.plane, PlaneEnum):
            self.plane = PlaneEnum(self.plane)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, MultipoleComponent) else MultipoleComponent(**as_dict(v)) for v in self.components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ACKicker(Kicker):
    """
    An ACKicker element simulates a time-dependent kicker. It is like a Kicker element except that the field varies in
    time. This element requires a user supplied time-dependent expression.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ACKicker"]
    class_class_curie: ClassVar[str] = "narad:ACKicker"
    class_name: ClassVar[str] = "ACKicker"
    class_model_uri: ClassVar[URIRef] = NARAD.ACKicker

    id: Union[str, ACKickerId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ACKickerId):
            self.id = ACKickerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiagnosticDevice(PhysicalComponent):
    """
    An accelerator device used to measure beam or machine state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["DiagnosticDevice"]
    class_class_curie: ClassVar[str] = "narad:DiagnosticDevice"
    class_name: ClassVar[str] = "DiagnosticDevice"
    class_model_uri: ClassVar[URIRef] = NARAD.DiagnosticDevice

    id: Union[str, DiagnosticDeviceId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiagnosticDeviceId):
            self.id = DiagnosticDeviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamPositionMonitor(DiagnosticDevice):
    """
    A diagnostic device used to measure transverse beam position.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BeamPositionMonitor"]
    class_class_curie: ClassVar[str] = "narad:BeamPositionMonitor"
    class_name: ClassVar[str] = "BeamPositionMonitor"
    class_model_uri: ClassVar[URIRef] = NARAD.BeamPositionMonitor

    id: Union[str, BeamPositionMonitorId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    species_ref: Optional[str] = None
    pc_ref: Optional[float] = None
    E_tot_ref: Optional[float] = None
    time_ref: Optional[float] = None
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None
    alpha_a: Optional[float] = None
    alpha_b: Optional[float] = None
    beta_a: Optional[float] = None
    beta_b: Optional[float] = None
    eta_x: Optional[float] = None
    eta_y: Optional[float] = None
    etap_x: Optional[float] = None
    etap_y: Optional[float] = None
    phi_a: Optional[float] = None
    phi_b: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamPositionMonitorId):
            self.id = BeamPositionMonitorId(self.id)

        if self.species_ref is not None and not isinstance(self.species_ref, str):
            self.species_ref = str(self.species_ref)

        if self.pc_ref is not None and not isinstance(self.pc_ref, float):
            self.pc_ref = float(self.pc_ref)

        if self.E_tot_ref is not None and not isinstance(self.E_tot_ref, float):
            self.E_tot_ref = float(self.E_tot_ref)

        if self.time_ref is not None and not isinstance(self.time_ref, float):
            self.time_ref = float(self.time_ref)

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

        if self.alpha_a is not None and not isinstance(self.alpha_a, float):
            self.alpha_a = float(self.alpha_a)

        if self.alpha_b is not None and not isinstance(self.alpha_b, float):
            self.alpha_b = float(self.alpha_b)

        if self.beta_a is not None and not isinstance(self.beta_a, float):
            self.beta_a = float(self.beta_a)

        if self.beta_b is not None and not isinstance(self.beta_b, float):
            self.beta_b = float(self.beta_b)

        if self.eta_x is not None and not isinstance(self.eta_x, float):
            self.eta_x = float(self.eta_x)

        if self.eta_y is not None and not isinstance(self.eta_y, float):
            self.eta_y = float(self.eta_y)

        if self.etap_x is not None and not isinstance(self.etap_x, float):
            self.etap_x = float(self.etap_x)

        if self.etap_y is not None and not isinstance(self.etap_y, float):
            self.etap_y = float(self.etap_y)

        if self.phi_a is not None and not isinstance(self.phi_a, float):
            self.phi_a = float(self.phi_a)

        if self.phi_b is not None and not isinstance(self.phi_b, float):
            self.phi_b = float(self.phi_b)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RadiationMonitor(DiagnosticDevice):
    """
    A diagnostic device used to monitor radiation dose or dose rate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["RadiationMonitor"]
    class_class_curie: ClassVar[str] = "narad:RadiationMonitor"
    class_name: ClassVar[str] = "RadiationMonitor"
    class_model_uri: ClassVar[URIRef] = NARAD.RadiationMonitor

    id: Union[str, RadiationMonitorId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RadiationMonitorId):
            self.id = RadiationMonitorId(self.id)

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
class Cavity(PhysicalComponent):
    """
    A cavity used for beam acceleration or manipulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Cavity"]
    class_class_curie: ClassVar[str] = "narad:Cavity"
    class_name: ClassVar[str] = "Cavity"
    class_model_uri: ClassVar[URIRef] = NARAD.Cavity

    id: Union[str, CavityId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    species_ref: Optional[str] = None
    pc_ref: Optional[float] = None
    E_tot_ref: Optional[float] = None
    time_ref: Optional[float] = None
    components: Optional[Union[Union[dict, MultipoleComponent], list[Union[dict, MultipoleComponent]]]] = empty_list()
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None
    alpha_a: Optional[float] = None
    alpha_b: Optional[float] = None
    beta_a: Optional[float] = None
    beta_b: Optional[float] = None
    eta_x: Optional[float] = None
    eta_y: Optional[float] = None
    etap_x: Optional[float] = None
    etap_y: Optional[float] = None
    phi_a: Optional[float] = None
    phi_b: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CavityId):
            self.id = CavityId(self.id)

        if self.species_ref is not None and not isinstance(self.species_ref, str):
            self.species_ref = str(self.species_ref)

        if self.pc_ref is not None and not isinstance(self.pc_ref, float):
            self.pc_ref = float(self.pc_ref)

        if self.E_tot_ref is not None and not isinstance(self.E_tot_ref, float):
            self.E_tot_ref = float(self.E_tot_ref)

        if self.time_ref is not None and not isinstance(self.time_ref, float):
            self.time_ref = float(self.time_ref)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, MultipoleComponent) else MultipoleComponent(**as_dict(v)) for v in self.components]

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

        if self.alpha_a is not None and not isinstance(self.alpha_a, float):
            self.alpha_a = float(self.alpha_a)

        if self.alpha_b is not None and not isinstance(self.alpha_b, float):
            self.alpha_b = float(self.alpha_b)

        if self.beta_a is not None and not isinstance(self.beta_a, float):
            self.beta_a = float(self.beta_a)

        if self.beta_b is not None and not isinstance(self.beta_b, float):
            self.beta_b = float(self.beta_b)

        if self.eta_x is not None and not isinstance(self.eta_x, float):
            self.eta_x = float(self.eta_x)

        if self.eta_y is not None and not isinstance(self.eta_y, float):
            self.eta_y = float(self.eta_y)

        if self.etap_x is not None and not isinstance(self.etap_x, float):
            self.etap_x = float(self.etap_x)

        if self.etap_y is not None and not isinstance(self.etap_y, float):
            self.etap_y = float(self.etap_y)

        if self.phi_a is not None and not isinstance(self.phi_a, float):
            self.phi_a = float(self.phi_a)

        if self.phi_b is not None and not isinstance(self.phi_b, float):
            self.phi_b = float(self.phi_b)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrabCavity(Cavity):
    """
    A cavity used for transverse beam manipulation, such as crabbing or deflecting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["CrabCavity"]
    class_class_curie: ClassVar[str] = "narad:CrabCavity"
    class_name: ClassVar[str] = "CrabCavity"
    class_model_uri: ClassVar[URIRef] = NARAD.CrabCavity

    id: Union[str, CrabCavityId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrabCavityId):
            self.id = CrabCavityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RFCavity(Cavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["RFCavity"]
    class_class_curie: ClassVar[str] = "narad:RFCavity"
    class_name: ClassVar[str] = "RFCavity"
    class_model_uri: ClassVar[URIRef] = NARAD.RFCavity

    id: Union[str, RFCavityId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RFCavityId):
            self.id = RFCavityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SuperconductingRFCavity(RFCavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SuperconductingRFCavity"]
    class_class_curie: ClassVar[str] = "narad:SuperconductingRFCavity"
    class_name: ClassVar[str] = "SuperconductingRFCavity"
    class_model_uri: ClassVar[URIRef] = NARAD.SuperconductingRFCavity

    id: Union[str, SuperconductingRFCavityId] = None
    type: str = None
    functions: Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]] = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SuperconductingRFCavityId):
            self.id = SuperconductingRFCavityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingFacilityComponent(PhysicalComponent):
    """
    A physical component that supports accelerator operation
    without a specific beam-pipe placement,
    such as a power supply, control rack, or radiation detector.
    These can include Girders, Racks, Power Supplies,
    and other physical infrastructure components that are important for understanding
    the structure and function of the accelerator system but are not inline with the beamline.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SupportingFacilityComponent"]
    class_class_curie: ClassVar[str] = "narad:SupportingFacilityComponent"
    class_name: ClassVar[str] = "SupportingFacilityComponent"
    class_model_uri: ClassVar[URIRef] = NARAD.SupportingFacilityComponent

    id: Union[str, SupportingFacilityComponentId] = None
    type: str = None
    beamline_relation: Union[str, "PhysicalRelationEnum"] = None
    functions: Union[Union[str, "FacilityFunctionEnum"], list[Union[str, "FacilityFunctionEnum"]]] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    theta: Optional[float] = None
    phi: Optional[float] = None
    psi: Optional[float] = None
    length: Optional[float] = None
    s_position: Optional[float] = None
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None

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

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.s_position is not None and not isinstance(self.s_position, float):
            self.s_position = float(self.s_position)

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
class BookkeepingComponent(VirtualComponent):
    """
    A virtual component that represents a bookkeeping or organizational role in the accelerator system,
    such as a BeamlineSection, Marker or a Fork.
    These can include BeamlineSections, Markers, Forks,
    and other virtual components that are important for understanding
    the structure and function of the accelerator system but are not physical devices.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BookkeepingComponent"]
    class_class_curie: ClassVar[str] = "narad:BookkeepingComponent"
    class_name: ClassVar[str] = "BookkeepingComponent"
    class_model_uri: ClassVar[URIRef] = NARAD.BookkeepingComponent

    id: Union[str, BookkeepingComponentId] = None
    type: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    x_offset: Optional[float] = None
    y_offset: Optional[float] = None
    z_offset: Optional[float] = None
    x_rot: Optional[float] = None
    y_rot: Optional[float] = None
    z_rot: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookkeepingComponentId):
            self.id = BookkeepingComponentId(self.id)

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
class Marker(BookkeepingComponent):
    """
    A virtual component used as a reference point or marker in the beamline structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Marker"]
    class_class_curie: ClassVar[str] = "narad:Marker"
    class_name: ClassVar[str] = "Marker"
    class_model_uri: ClassVar[URIRef] = NARAD.Marker

    id: Union[str, MarkerId] = None
    type: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None
    alpha_a: Optional[float] = None
    alpha_b: Optional[float] = None
    beta_a: Optional[float] = None
    beta_b: Optional[float] = None
    eta_x: Optional[float] = None
    eta_y: Optional[float] = None
    etap_x: Optional[float] = None
    etap_y: Optional[float] = None
    phi_a: Optional[float] = None
    phi_b: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarkerId):
            self.id = MarkerId(self.id)

        if self.alpha_a is not None and not isinstance(self.alpha_a, float):
            self.alpha_a = float(self.alpha_a)

        if self.alpha_b is not None and not isinstance(self.alpha_b, float):
            self.alpha_b = float(self.alpha_b)

        if self.beta_a is not None and not isinstance(self.beta_a, float):
            self.beta_a = float(self.beta_a)

        if self.beta_b is not None and not isinstance(self.beta_b, float):
            self.beta_b = float(self.beta_b)

        if self.eta_x is not None and not isinstance(self.eta_x, float):
            self.eta_x = float(self.eta_x)

        if self.eta_y is not None and not isinstance(self.eta_y, float):
            self.eta_y = float(self.eta_y)

        if self.etap_x is not None and not isinstance(self.etap_x, float):
            self.etap_x = float(self.etap_x)

        if self.etap_y is not None and not isinstance(self.etap_y, float):
            self.etap_y = float(self.etap_y)

        if self.phi_a is not None and not isinstance(self.phi_a, float):
            self.phi_a = float(self.phi_a)

        if self.phi_b is not None and not isinstance(self.phi_b, float):
            self.phi_b = float(self.phi_b)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamlineSection(BookkeepingComponent):
    """
    A virtual component used to represent a section of the beamline for organizational
    or functional grouping of components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["BeamlineSection"]
    class_class_curie: ClassVar[str] = "narad:BeamlineSection"
    class_name: ClassVar[str] = "BeamlineSection"
    class_model_uri: ClassVar[URIRef] = NARAD.BeamlineSection

    id: Union[str, BeamlineSectionId] = None
    type: str = None
    functions: Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]] = None
    beamline_relation: Union[str, "VirtualRelationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineSectionId):
            self.id = BeamlineSectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetadataEntry(YAMLRoot):
    """
    A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any)
    field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["MetadataEntry"]
    class_class_curie: ClassVar[str] = "narad:MetadataEntry"
    class_name: ClassVar[str] = "MetadataEntry"
    class_model_uri: ClassVar[URIRef] = NARAD.MetadataEntry

    key: Union[str, MetadataEntryKey] = None
    value: str = None
    datatype: Optional[Union[str, "DataTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, MetadataEntryKey):
            self.key = MetadataEntryKey(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.datatype is not None and not isinstance(self.datatype, DataTypeEnum):
            self.datatype = DataTypeEnum(self.datatype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    Abstract base for subject-predicate-object associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["Relationship"]
    class_class_curie: ClassVar[str] = "narad:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = NARAD.Relationship

    id: Union[str, RelationshipId] = None
    subject: str = None
    predicate: str = None
    object: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipId):
            self.id = RelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalBinding(Relationship):
    """
    Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["SignalBinding"]
    class_class_curie: ClassVar[str] = "narad:SignalBinding"
    class_name: ClassVar[str] = "SignalBinding"
    class_model_uri: ClassVar[URIRef] = NARAD.SignalBinding

    id: Union[str, SignalBindingId] = None
    subject: Union[str, PhysicalComponentId] = None
    predicate: Union[str, "SignalBindingPredicateEnum"] = None
    object: Union[str, SignalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignalBindingId):
            self.id = SignalBindingId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, PhysicalComponentId):
            self.subject = PhysicalComponentId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, SignalBindingPredicateEnum):
            self.predicate = SignalBindingPredicateEnum(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, SignalId):
            self.object = SignalId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentRelation(Relationship):
    """
    Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about
    how and where the relationship holds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NARAD["ComponentRelation"]
    class_class_curie: ClassVar[str] = "narad:ComponentRelation"
    class_name: ClassVar[str] = "ComponentRelation"
    class_model_uri: ClassVar[URIRef] = NARAD.ComponentRelation

    id: Union[str, ComponentRelationId] = None
    subject: Union[str, ComponentId] = None
    predicate: Union[str, "ComponentRelationPredicateEnum"] = None
    object: Union[str, ComponentId] = None
    context: Optional[Union[str, "RelationContextEnum"]] = None
    beamline_context: Optional[Union[str, BeamlineId]] = None
    reference_frame: Optional[Union[str, "ReferenceFrameEnum"]] = None
    distance_value: Optional[float] = None
    distance_unit: Optional[Union[str, "UnitEnum"]] = None
    axis: Optional[Union[str, "AxisEnum"]] = None
    direction: Optional[Union[str, "DirectionEnum"]] = None
    tolerance_value: Optional[float] = None
    tolerance_unit: Optional[Union[str, "UnitEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentRelationId):
            self.id = ComponentRelationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentId):
            self.subject = ComponentId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, ComponentRelationPredicateEnum):
            self.predicate = ComponentRelationPredicateEnum(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        if self.context is not None and not isinstance(self.context, RelationContextEnum):
            self.context = RelationContextEnum(self.context)

        if self.beamline_context is not None and not isinstance(self.beamline_context, BeamlineId):
            self.beamline_context = BeamlineId(self.beamline_context)

        if self.reference_frame is not None and not isinstance(self.reference_frame, ReferenceFrameEnum):
            self.reference_frame = ReferenceFrameEnum(self.reference_frame)

        if self.distance_value is not None and not isinstance(self.distance_value, float):
            self.distance_value = float(self.distance_value)

        if self.distance_unit is not None and not isinstance(self.distance_unit, UnitEnum):
            self.distance_unit = UnitEnum(self.distance_unit)

        if self.axis is not None and not isinstance(self.axis, AxisEnum):
            self.axis = AxisEnum(self.axis)

        if self.direction is not None and not isinstance(self.direction, DirectionEnum):
            self.direction = DirectionEnum(self.direction)

        if self.tolerance_value is not None and not isinstance(self.tolerance_value, float):
            self.tolerance_value = float(self.tolerance_value)

        if self.tolerance_unit is not None and not isinstance(self.tolerance_unit, UnitEnum):
            self.tolerance_unit = UnitEnum(self.tolerance_unit)

        super().__post_init__(**kwargs)


# Enumerations
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
    NearBeamline = PermissibleValue(
        text="NearBeamline",
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
    AssociatedWithBeamline = PermissibleValue(
        text="AssociatedWithBeamline",
        description="""Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the beamline structure and function but don't have a direct physical relationship to the beam path,  such as BeamlineSections or Markers that are not inline with the beam.""")
    NotAssociatedWithBeamline = PermissibleValue(
        text="NotAssociatedWithBeamline",
        description="""Not inline with the beamline and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the beamline, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the beamline structure.""")

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
    BeamlineSection = PermissibleValue(
        text="BeamlineSection",
        description="""A section of the beamline used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector.""",
        meaning=PALS["Beamline"])
    Mark = PermissibleValue(
        text="Mark",
        description="""A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device.""",
        meaning=PALS["Marker"])
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
    Limit = PermissibleValue(
        text="Limit",
        description="Minimum, maximum, or other constraints for an allowed signal value.")

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
    mm = PermissibleValue(
        text="mm",
        description="millimeter",
        meaning=UNIT["MilliM"])
    m = PermissibleValue(
        text="m",
        description="meter",
        meaning=UNIT["M"])
    A = PermissibleValue(
        text="A",
        description="ampere",
        meaning=UNIT["A"])
    T_m = PermissibleValue(
        text="T_m",
        description="tesla meter",
        meaning=UNIT["T-M"])
    Pa = PermissibleValue(
        text="Pa",
        description="pascal",
        meaning=UNIT["PA"])
    Torr = PermissibleValue(
        text="Torr",
        description="torr",
        meaning=UNIT["TORR"])
    rem_per_h = PermissibleValue(
        text="rem_per_h",
        description="""rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary.""",
        meaning=UNIT["REM-PER-H"])
    mrem_per_h = PermissibleValue(
        text="mrem_per_h",
        description="""millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary.""",
        meaning=UNIT["MREM-PER-H"])
    V = PermissibleValue(
        text="V",
        description="volt",
        meaning=UNIT["V"])
    kW = PermissibleValue(
        text="kW",
        description="kilowatt",
        meaning=UNIT["KiloW"])
    degree = PermissibleValue(
        text="degree",
        description="degree",
        meaning=UNIT["DEG"])
    MV_per_m = PermissibleValue(
        text="MV_per_m",
        description="megavolt per meter",
        meaning=UNIT["MegaV-PER-M"])
    G_per_cm = PermissibleValue(
        text="G_per_cm",
        description="gauss per centimeter")
    unitless = PermissibleValue(
        text="unitless",
        description="dimensionless numeric value",
        meaning=UNIT["NUM"])
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

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Data types for parameter values.",
    )

class ComponentRelationPredicateEnum(EnumDefinitionImpl):

    precedes = PermissibleValue(
        text="precedes",
        description="Subject occurs immediately before object in the sequence/beamline order.",
        meaning=BFO["0000063"])
    follows = PermissibleValue(
        text="follows",
        description="Subject occurs after object in the sequence/beamline order.",
        meaning=BFO["0000062"])
    contains = PermissibleValue(
        text="contains",
        description="Subject spatially or mereologically contains object.",
        meaning=BFO["0000051"])
    contained_in = PermissibleValue(
        text="contained_in",
        description="Subject is spatially or mereologically contained in object.",
        meaning=BFO["0000050"])
    connected_to = PermissibleValue(
        text="connected_to",
        description="""Subject and object are physically connected. a is connected to b if and only if a and b are discrete structure,  and there exists some connecting structure c, such that c connects a and b""",
        meaning=RO["0002170"])
    controls = PermissibleValue(
        text="controls",
        description="Subject controls the state or behavior of object.",
        meaning=SAREF["controls"])
    is_controlled_by = PermissibleValue(
        text="is_controlled_by",
        description="Subject is controlled by object.",
        meaning=SAREF["isControlledBy"])
    is_part_of = PermissibleValue(
        text="is_part_of",
        description="Subject is a part of object.",
        meaning=BFO["0000050"])
    has_part = PermissibleValue(
        text="has_part",
        description="Subject has part object.",
        meaning=BFO["0000051"])
    adjacent_to = PermissibleValue(
        text="adjacent_to",
        description="Subject and object are spatially adjacent, without overlapping.",
        meaning=RO["0002220"])
    overlaps = PermissibleValue(
        text="overlaps",
        description="Subject and object share at least one part in common.",
        meaning=RO["0002131"])
    mounted_on = PermissibleValue(
        text="mounted_on",
        description="Subject is mounted on object.",
        meaning=NARAD["mounted_on"])
    intersects = PermissibleValue(
        text="intersects",
        description="Subject intersects with object.",
        meaning=NARAD["intersects"])
    nearest_to = PermissibleValue(
        text="nearest_to",
        description="Subject is nearest to object.",
        meaning=NARAD["nearest_to"])

    _defn = EnumDefinition(
        name="ComponentRelationPredicateEnum",
    )

class SignalBindingPredicateEnum(EnumDefinitionImpl):
    """
    Controlled predicates for Component-to-Signal bindings.
    """
    has_signal = PermissibleValue(
        text="has_signal",
        description="""Generic association between a component and one of its signals. The specific role (setpoint, readback, status, etc.) is carried by the Signal's own signal_role field, not the predicate.""")
    has_status_signal = PermissibleValue(
        text="has_status_signal",
        description="Subject has the given signal as its status indicator.")
    has_setpoint_signal = PermissibleValue(
        text="has_setpoint_signal",
        description="Subject has the given signal as its setpoint.")
    has_readback_signal = PermissibleValue(
        text="has_readback_signal",
        description="Subject has the given signal as its readback.")
    has_command_signal = PermissibleValue(
        text="has_command_signal",
        description="Subject has the given signal as a command trigger.")
    has_limit_signal = PermissibleValue(
        text="has_limit_signal",
        description="Subject has the given signal as a limit/constraint value.")

    _defn = EnumDefinition(
        name="SignalBindingPredicateEnum",
        description="Controlled predicates for Component-to-Signal bindings.",
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

class AxisEnum(EnumDefinitionImpl):

    x = PermissibleValue(text="x")
    y = PermissibleValue(text="y")
    z = PermissibleValue(text="z")
    s = PermissibleValue(text="s")

    _defn = EnumDefinition(
        name="AxisEnum",
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

# Slots
class slots:
    pass

slots.id = Slot(uri=NARAD.id, name="id", curie=NARAD.curie('id'),
                   model_uri=NARAD.id, domain=None, range=URIRef)

slots.type = Slot(uri=NARAD.type, name="type", curie=NARAD.curie('type'),
                   model_uri=NARAD.type, domain=None, range=str)

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=NARAD.subject, domain=None, range=str)

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=NARAD.predicate, domain=None, range=str)

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=NARAD.object, domain=None, range=str)

slots.nARAD__description = Slot(uri=NARAD.description, name="nARAD__description", curie=NARAD.curie('description'),
                   model_uri=NARAD.nARAD__description, domain=None, range=Optional[str])

slots.nARAD__physical_components = Slot(uri=NARAD.physical_components, name="nARAD__physical_components", curie=NARAD.curie('physical_components'),
                   model_uri=NARAD.nARAD__physical_components, domain=None, range=Optional[Union[dict[Union[str, PhysicalComponentId], Union[dict, PhysicalComponent]], list[Union[dict, PhysicalComponent]]]])

slots.nARAD__virtual_components = Slot(uri=NARAD.virtual_components, name="nARAD__virtual_components", curie=NARAD.curie('virtual_components'),
                   model_uri=NARAD.nARAD__virtual_components, domain=None, range=Optional[Union[dict[Union[str, VirtualComponentId], Union[dict, VirtualComponent]], list[Union[dict, VirtualComponent]]]])

slots.nARAD__beamlines = Slot(uri=NARAD.beamlines, name="nARAD__beamlines", curie=NARAD.curie('beamlines'),
                   model_uri=NARAD.nARAD__beamlines, domain=None, range=Optional[Union[dict[Union[str, BeamlineId], Union[dict, Beamline]], list[Union[dict, Beamline]]]])

slots.nARAD__supporting_facility_components = Slot(uri=NARAD.supporting_facility_components, name="nARAD__supporting_facility_components", curie=NARAD.curie('supporting_facility_components'),
                   model_uri=NARAD.nARAD__supporting_facility_components, domain=None, range=Optional[Union[dict[Union[str, SupportingFacilityComponentId], Union[dict, SupportingFacilityComponent]], list[Union[dict, SupportingFacilityComponent]]]])

slots.nARAD__signals = Slot(uri=NARAD.signals, name="nARAD__signals", curie=NARAD.curie('signals'),
                   model_uri=NARAD.nARAD__signals, domain=None, range=Optional[Union[dict[Union[str, SignalId], Union[dict, Signal]], list[Union[dict, Signal]]]])

slots.nARAD__signal_bindings = Slot(uri=NARAD.signal_bindings, name="nARAD__signal_bindings", curie=NARAD.curie('signal_bindings'),
                   model_uri=NARAD.nARAD__signal_bindings, domain=None, range=Optional[Union[dict[Union[str, SignalBindingId], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.nARAD__component_relations = Slot(uri=NARAD.component_relations, name="nARAD__component_relations", curie=NARAD.curie('component_relations'),
                   model_uri=NARAD.nARAD__component_relations, domain=None, range=Optional[Union[dict[Union[str, ComponentRelationId], Union[dict, ComponentRelation]], list[Union[dict, ComponentRelation]]]])

slots.metaP__description = Slot(uri=PALS.description, name="metaP__description", curie=PALS.curie('description'),
                   model_uri=NARAD.metaP__description, domain=None, range=Optional[str])

slots.metaP__label = Slot(uri=PALS.label, name="metaP__label", curie=PALS.curie('label'),
                   model_uri=NARAD.metaP__label, domain=None, range=Optional[str])

slots.metaP__alias = Slot(uri=PALS.alias, name="metaP__alias", curie=PALS.curie('alias'),
                   model_uri=NARAD.metaP__alias, domain=None, range=Optional[str])

slots.metaP__additional_metadata = Slot(uri=NARAD.additional_metadata, name="metaP__additional_metadata", curie=NARAD.curie('additional_metadata'),
                   model_uri=NARAD.metaP__additional_metadata, domain=None, range=Optional[Union[dict[Union[str, MetadataEntryKey], Union[dict, MetadataEntry]], list[Union[dict, MetadataEntry]]]])

slots.floorP__x = Slot(uri=PALS.x, name="floorP__x", curie=PALS.curie('x'),
                   model_uri=NARAD.floorP__x, domain=None, range=Optional[float])

slots.floorP__y = Slot(uri=PALS.y, name="floorP__y", curie=PALS.curie('y'),
                   model_uri=NARAD.floorP__y, domain=None, range=Optional[float])

slots.floorP__z = Slot(uri=PALS.z, name="floorP__z", curie=PALS.curie('z'),
                   model_uri=NARAD.floorP__z, domain=None, range=Optional[float])

slots.floorP__theta = Slot(uri=PALS.theta, name="floorP__theta", curie=PALS.curie('theta'),
                   model_uri=NARAD.floorP__theta, domain=None, range=Optional[float])

slots.floorP__phi = Slot(uri=PALS.phi, name="floorP__phi", curie=PALS.curie('phi'),
                   model_uri=NARAD.floorP__phi, domain=None, range=Optional[float])

slots.floorP__psi = Slot(uri=PALS.psi, name="floorP__psi", curie=PALS.curie('psi'),
                   model_uri=NARAD.floorP__psi, domain=None, range=Optional[float])

slots.bodyShiftP__x_offset = Slot(uri=PALS.x_offset, name="bodyShiftP__x_offset", curie=PALS.curie('x_offset'),
                   model_uri=NARAD.bodyShiftP__x_offset, domain=None, range=Optional[float])

slots.bodyShiftP__y_offset = Slot(uri=PALS.y_offset, name="bodyShiftP__y_offset", curie=PALS.curie('y_offset'),
                   model_uri=NARAD.bodyShiftP__y_offset, domain=None, range=Optional[float])

slots.bodyShiftP__z_offset = Slot(uri=PALS.z_offset, name="bodyShiftP__z_offset", curie=PALS.curie('z_offset'),
                   model_uri=NARAD.bodyShiftP__z_offset, domain=None, range=Optional[float])

slots.bodyShiftP__x_rot = Slot(uri=PALS.x_rot, name="bodyShiftP__x_rot", curie=PALS.curie('x_rot'),
                   model_uri=NARAD.bodyShiftP__x_rot, domain=None, range=Optional[float])

slots.bodyShiftP__y_rot = Slot(uri=PALS.y_rot, name="bodyShiftP__y_rot", curie=PALS.curie('y_rot'),
                   model_uri=NARAD.bodyShiftP__y_rot, domain=None, range=Optional[float])

slots.bodyShiftP__z_rot = Slot(uri=PALS.z_rot, name="bodyShiftP__z_rot", curie=PALS.curie('z_rot'),
                   model_uri=NARAD.bodyShiftP__z_rot, domain=None, range=Optional[float])

slots.hasLongitudinalPlacement__length = Slot(uri=PALS.length, name="hasLongitudinalPlacement__length", curie=PALS.curie('length'),
                   model_uri=NARAD.hasLongitudinalPlacement__length, domain=None, range=Optional[float])

slots.hasLongitudinalPlacement__s_position = Slot(uri=PALS.s_position, name="hasLongitudinalPlacement__s_position", curie=PALS.curie('s_position'),
                   model_uri=NARAD.hasLongitudinalPlacement__s_position, domain=None, range=Optional[float])

slots.referenceP__species_ref = Slot(uri=PALS.species_ref, name="referenceP__species_ref", curie=PALS.curie('species_ref'),
                   model_uri=NARAD.referenceP__species_ref, domain=None, range=Optional[str])

slots.referenceP__pc_ref = Slot(uri=PALS.pc_ref, name="referenceP__pc_ref", curie=PALS.curie('pc_ref'),
                   model_uri=NARAD.referenceP__pc_ref, domain=None, range=Optional[float])

slots.referenceP__E_tot_ref = Slot(uri=PALS.E_tot_ref, name="referenceP__E_tot_ref", curie=PALS.curie('E_tot_ref'),
                   model_uri=NARAD.referenceP__E_tot_ref, domain=None, range=Optional[float])

slots.referenceP__time_ref = Slot(uri=PALS.time_ref, name="referenceP__time_ref", curie=PALS.curie('time_ref'),
                   model_uri=NARAD.referenceP__time_ref, domain=None, range=Optional[float])

slots.solenoidP__Ksol = Slot(uri=PALS.Ksol, name="solenoidP__Ksol", curie=PALS.curie('Ksol'),
                   model_uri=NARAD.solenoidP__Ksol, domain=None, range=Optional[float])

slots.solenoidP__Bsol = Slot(uri=PALS.Bsol, name="solenoidP__Bsol", curie=PALS.curie('Bsol'),
                   model_uri=NARAD.solenoidP__Bsol, domain=None, range=Optional[float])

slots.twissP__alpha_a = Slot(uri=PALS.alpha_a, name="twissP__alpha_a", curie=PALS.curie('alpha_a'),
                   model_uri=NARAD.twissP__alpha_a, domain=None, range=Optional[float])

slots.twissP__alpha_b = Slot(uri=PALS.alpha_b, name="twissP__alpha_b", curie=PALS.curie('alpha_b'),
                   model_uri=NARAD.twissP__alpha_b, domain=None, range=Optional[float])

slots.twissP__beta_a = Slot(uri=PALS.beta_a, name="twissP__beta_a", curie=PALS.curie('beta_a'),
                   model_uri=NARAD.twissP__beta_a, domain=None, range=Optional[float])

slots.twissP__beta_b = Slot(uri=PALS.beta_b, name="twissP__beta_b", curie=PALS.curie('beta_b'),
                   model_uri=NARAD.twissP__beta_b, domain=None, range=Optional[float])

slots.twissP__eta_x = Slot(uri=PALS.eta_x, name="twissP__eta_x", curie=PALS.curie('eta_x'),
                   model_uri=NARAD.twissP__eta_x, domain=None, range=Optional[float])

slots.twissP__eta_y = Slot(uri=PALS.eta_y, name="twissP__eta_y", curie=PALS.curie('eta_y'),
                   model_uri=NARAD.twissP__eta_y, domain=None, range=Optional[float])

slots.twissP__etap_x = Slot(uri=PALS.etap_x, name="twissP__etap_x", curie=PALS.curie('etap_x'),
                   model_uri=NARAD.twissP__etap_x, domain=None, range=Optional[float])

slots.twissP__etap_y = Slot(uri=PALS.etap_y, name="twissP__etap_y", curie=PALS.curie('etap_y'),
                   model_uri=NARAD.twissP__etap_y, domain=None, range=Optional[float])

slots.twissP__phi_a = Slot(uri=PALS.phi_a, name="twissP__phi_a", curie=PALS.curie('phi_a'),
                   model_uri=NARAD.twissP__phi_a, domain=None, range=Optional[float])

slots.twissP__phi_b = Slot(uri=PALS.phi_b, name="twissP__phi_b", curie=PALS.curie('phi_b'),
                   model_uri=NARAD.twissP__phi_b, domain=None, range=Optional[float])

slots.electricMultipoleP__components = Slot(uri=NARAD.components, name="electricMultipoleP__components", curie=NARAD.curie('components'),
                   model_uri=NARAD.electricMultipoleP__components, domain=None, range=Optional[Union[Union[dict, MultipoleComponent], list[Union[dict, MultipoleComponent]]]])

slots.magneticMultipoleP__components = Slot(uri=NARAD.components, name="magneticMultipoleP__components", curie=NARAD.curie('components'),
                   model_uri=NARAD.magneticMultipoleP__components, domain=None, range=Optional[Union[Union[dict, MultipoleComponent], list[Union[dict, MultipoleComponent]]]])

slots.bendP__angle_ref = Slot(uri=PALS.angle_ref, name="bendP__angle_ref", curie=PALS.curie('angle_ref'),
                   model_uri=NARAD.bendP__angle_ref, domain=None, range=Optional[float])

slots.bendP__bend_field_ref = Slot(uri=PALS.bend_field_ref, name="bendP__bend_field_ref", curie=PALS.curie('bend_field_ref'),
                   model_uri=NARAD.bendP__bend_field_ref, domain=None, range=Optional[float])

slots.bendP__bend_field_actual = Slot(uri=PALS.bend_field_actual, name="bendP__bend_field_actual", curie=PALS.curie('bend_field_actual'),
                   model_uri=NARAD.bendP__bend_field_actual, domain=None, range=Optional[float])

slots.bendP__e1 = Slot(uri=PALS.e1, name="bendP__e1", curie=PALS.curie('e1'),
                   model_uri=NARAD.bendP__e1, domain=None, range=Optional[float])

slots.bendP__e2 = Slot(uri=PALS.e2, name="bendP__e2", curie=PALS.curie('e2'),
                   model_uri=NARAD.bendP__e2, domain=None, range=Optional[float])

slots.bendP__e1_rect = Slot(uri=PALS.e1_rect, name="bendP__e1_rect", curie=PALS.curie('e1_rect'),
                   model_uri=NARAD.bendP__e1_rect, domain=None, range=Optional[float])

slots.bendP__e2_rect = Slot(uri=PALS.e2_rect, name="bendP__e2_rect", curie=PALS.curie('e2_rect'),
                   model_uri=NARAD.bendP__e2_rect, domain=None, range=Optional[float])

slots.bendP__edge1_int = Slot(uri=PALS.edge1_int, name="bendP__edge1_int", curie=PALS.curie('edge1_int'),
                   model_uri=NARAD.bendP__edge1_int, domain=None, range=Optional[float])

slots.bendP__edge2_int = Slot(uri=PALS.edge2_int, name="bendP__edge2_int", curie=PALS.curie('edge2_int'),
                   model_uri=NARAD.bendP__edge2_int, domain=None, range=Optional[float])

slots.bendP__g_ref = Slot(uri=PALS.g_ref, name="bendP__g_ref", curie=PALS.curie('g_ref'),
                   model_uri=NARAD.bendP__g_ref, domain=None, range=Optional[float])

slots.bendP__g_actual = Slot(uri=PALS.g_actual, name="bendP__g_actual", curie=PALS.curie('g_actual'),
                   model_uri=NARAD.bendP__g_actual, domain=None, range=Optional[float])

slots.bendP__h1 = Slot(uri=PALS.h1, name="bendP__h1", curie=PALS.curie('h1'),
                   model_uri=NARAD.bendP__h1, domain=None, range=Optional[float])

slots.bendP__h2 = Slot(uri=PALS.h2, name="bendP__h2", curie=PALS.curie('h2'),
                   model_uri=NARAD.bendP__h2, domain=None, range=Optional[float])

slots.bendP__L_chord = Slot(uri=PALS.L_chord, name="bendP__L_chord", curie=PALS.curie('L_chord'),
                   model_uri=NARAD.bendP__L_chord, domain=None, range=Optional[float])

slots.bendP__L_sagitta = Slot(uri=PALS.L_sagitta, name="bendP__L_sagitta", curie=PALS.curie('L_sagitta'),
                   model_uri=NARAD.bendP__L_sagitta, domain=None, range=Optional[float])

slots.bendP__L_rectangle = Slot(uri=PALS.L_rectangle, name="bendP__L_rectangle", curie=PALS.curie('L_rectangle'),
                   model_uri=NARAD.bendP__L_rectangle, domain=None, range=Optional[float])

slots.bendP__multipole_geometry = Slot(uri=PALS.multipole_geometry, name="bendP__multipole_geometry", curie=PALS.curie('multipole_geometry'),
                   model_uri=NARAD.bendP__multipole_geometry, domain=None, range=Optional[Union[str, "MultipoleGeometryEnum"]])

slots.bendP__ref_geometry = Slot(uri=PALS.ref_geometry, name="bendP__ref_geometry", curie=PALS.curie('ref_geometry'),
                   model_uri=NARAD.bendP__ref_geometry, domain=None, range=Optional[Union[str, "ReferenceGeometryEnum"]])

slots.bendP__rho_ref = Slot(uri=PALS.rho_ref, name="bendP__rho_ref", curie=PALS.curie('rho_ref'),
                   model_uri=NARAD.bendP__rho_ref, domain=None, range=Optional[float])

slots.bendP__tilt_ref = Slot(uri=PALS.tilt_ref, name="bendP__tilt_ref", curie=PALS.curie('tilt_ref'),
                   model_uri=NARAD.bendP__tilt_ref, domain=None, range=Optional[float])

slots.multipoleComponent__order = Slot(uri=NARAD.order, name="multipoleComponent__order", curie=NARAD.curie('order'),
                   model_uri=NARAD.multipoleComponent__order, domain=None, range=int)

slots.multipoleComponent__tilt = Slot(uri=NARAD.tilt, name="multipoleComponent__tilt", curie=NARAD.curie('tilt'),
                   model_uri=NARAD.multipoleComponent__tilt, domain=None, range=Optional[float])

slots.multipoleComponent__En = Slot(uri=NARAD.En, name="multipoleComponent__En", curie=NARAD.curie('En'),
                   model_uri=NARAD.multipoleComponent__En, domain=None, range=Optional[float])

slots.multipoleComponent__Es = Slot(uri=NARAD.Es, name="multipoleComponent__Es", curie=NARAD.curie('Es'),
                   model_uri=NARAD.multipoleComponent__Es, domain=None, range=Optional[float])

slots.multipoleComponent__EnL = Slot(uri=NARAD.EnL, name="multipoleComponent__EnL", curie=NARAD.curie('EnL'),
                   model_uri=NARAD.multipoleComponent__EnL, domain=None, range=Optional[float])

slots.multipoleComponent__EsL = Slot(uri=NARAD.EsL, name="multipoleComponent__EsL", curie=NARAD.curie('EsL'),
                   model_uri=NARAD.multipoleComponent__EsL, domain=None, range=Optional[float])

slots.multipoleComponent__Bn = Slot(uri=NARAD.Bn, name="multipoleComponent__Bn", curie=NARAD.curie('Bn'),
                   model_uri=NARAD.multipoleComponent__Bn, domain=None, range=Optional[float])

slots.multipoleComponent__Bs = Slot(uri=NARAD.Bs, name="multipoleComponent__Bs", curie=NARAD.curie('Bs'),
                   model_uri=NARAD.multipoleComponent__Bs, domain=None, range=Optional[float])

slots.multipoleComponent__Kn = Slot(uri=NARAD.Kn, name="multipoleComponent__Kn", curie=NARAD.curie('Kn'),
                   model_uri=NARAD.multipoleComponent__Kn, domain=None, range=Optional[float])

slots.multipoleComponent__Ks = Slot(uri=NARAD.Ks, name="multipoleComponent__Ks", curie=NARAD.curie('Ks'),
                   model_uri=NARAD.multipoleComponent__Ks, domain=None, range=Optional[float])

slots.component__native_types = Slot(uri=NARAD.native_types, name="component__native_types", curie=NARAD.curie('native_types'),
                   model_uri=NARAD.component__native_types, domain=None, range=Optional[Union[str, list[str]]])

slots.physicalComponent__functions = Slot(uri=NARAD.physical_function, name="physicalComponent__functions", curie=NARAD.curie('physical_function'),
                   model_uri=NARAD.physicalComponent__functions, domain=None, range=Union[Union[str, "PhysicalFunctionEnum"], list[Union[str, "PhysicalFunctionEnum"]]])

slots.physicalComponent__beamline_relation = Slot(uri=NARAD.physical_beamline_relation, name="physicalComponent__beamline_relation", curie=NARAD.curie('physical_beamline_relation'),
                   model_uri=NARAD.physicalComponent__beamline_relation, domain=None, range=Union[str, "PhysicalRelationEnum"])

slots.virtualComponent__functions = Slot(uri=NARAD.virtual_function, name="virtualComponent__functions", curie=NARAD.curie('virtual_function'),
                   model_uri=NARAD.virtualComponent__functions, domain=None, range=Union[Union[str, "VirtualFunctionEnum"], list[Union[str, "VirtualFunctionEnum"]]])

slots.virtualComponent__beamline_relation = Slot(uri=NARAD.virtual_beamline_relation, name="virtualComponent__beamline_relation", curie=NARAD.curie('virtual_beamline_relation'),
                   model_uri=NARAD.virtualComponent__beamline_relation, domain=None, range=Union[str, "VirtualRelationEnum"])

slots.beamline__multipass = Slot(uri=PALS.multipass, name="beamline__multipass", curie=PALS.curie('multipass'),
                   model_uri=NARAD.beamline__multipass, domain=None, range=Optional[Union[bool, Bool]])

slots.beamline__length = Slot(uri=PALS.length, name="beamline__length", curie=PALS.curie('length'),
                   model_uri=NARAD.beamline__length, domain=None, range=Optional[float])

slots.beamline__zero_point = Slot(uri=NARAD.zero_point, name="beamline__zero_point", curie=NARAD.curie('zero_point'),
                   model_uri=NARAD.beamline__zero_point, domain=None, range=Optional[str])

slots.beamline__periodic = Slot(uri=PALS.periodic, name="beamline__periodic", curie=PALS.curie('periodic'),
                   model_uri=NARAD.beamline__periodic, domain=None, range=Optional[Union[bool, Bool]])

slots.beamline__repeat = Slot(uri=PALS.repeat, name="beamline__repeat", curie=PALS.curie('repeat'),
                   model_uri=NARAD.beamline__repeat, domain=None, range=Optional[int])

slots.beamline__direction = Slot(uri=PALS.direction, name="beamline__direction", curie=PALS.curie('direction'),
                   model_uri=NARAD.beamline__direction, domain=None, range=Optional[int])

slots.signal__signal_role = Slot(uri=NARAD.signal_role, name="signal__signal_role", curie=NARAD.curie('signal_role'),
                   model_uri=NARAD.signal__signal_role, domain=None, range=Union[str, "SignalRoleEnum"])

slots.signal__source_system = Slot(uri=NARAD.source_system, name="signal__source_system", curie=NARAD.curie('source_system'),
                   model_uri=NARAD.signal__source_system, domain=None, range=Union[str, "SourceSystemEnum"])

slots.signal__native_description = Slot(uri=NARAD.native_description, name="signal__native_description", curie=NARAD.curie('native_description'),
                   model_uri=NARAD.signal__native_description, domain=None, range=Optional[str])

slots.signal__canonical_signal_type = Slot(uri=NARAD.canonical_signal_type, name="signal__canonical_signal_type", curie=NARAD.curie('canonical_signal_type'),
                   model_uri=NARAD.signal__canonical_signal_type, domain=None, range=Union[str, "CanonicalSignalTypeEnum"])

slots.signal__quantity_kind = Slot(uri=NARAD.quantity_kind, name="signal__quantity_kind", curie=NARAD.curie('quantity_kind'),
                   model_uri=NARAD.signal__quantity_kind, domain=None, range=Union[str, "QuantityKindEnum"])

slots.signal__native_data_type = Slot(uri=NARAD.native_data_type, name="signal__native_data_type", curie=NARAD.curie('native_data_type'),
                   model_uri=NARAD.signal__native_data_type, domain=None, range=Union[str, "DataTypeEnum"])

slots.signal__native_unit = Slot(uri=NARAD.native_unit, name="signal__native_unit", curie=NARAD.curie('native_unit'),
                   model_uri=NARAD.signal__native_unit, domain=None, range=Union[str, "UnitEnum"])

slots.signal__access_protocol = Slot(uri=NARAD.access_protocol, name="signal__access_protocol", curie=NARAD.curie('access_protocol'),
                   model_uri=NARAD.signal__access_protocol, domain=None, range=Optional[str])

slots.signal__archive_identifier = Slot(uri=NARAD.archive_identifier, name="signal__archive_identifier", curie=NARAD.curie('archive_identifier'),
                   model_uri=NARAD.signal__archive_identifier, domain=None, range=Optional[str])

slots.kicker__plane = Slot(uri=NARAD.plane, name="kicker__plane", curie=NARAD.curie('plane'),
                   model_uri=NARAD.kicker__plane, domain=None, range=Optional[Union[str, "PlaneEnum"]])

slots.supportingFacilityComponent__functions = Slot(uri=NARAD.supporting_facility_function, name="supportingFacilityComponent__functions", curie=NARAD.curie('supporting_facility_function'),
                   model_uri=NARAD.supportingFacilityComponent__functions, domain=None, range=Union[Union[str, "FacilityFunctionEnum"], list[Union[str, "FacilityFunctionEnum"]]])

slots.metadataEntry__key = Slot(uri=NARAD.key, name="metadataEntry__key", curie=NARAD.curie('key'),
                   model_uri=NARAD.metadataEntry__key, domain=None, range=URIRef)

slots.metadataEntry__value = Slot(uri=NARAD.value, name="metadataEntry__value", curie=NARAD.curie('value'),
                   model_uri=NARAD.metadataEntry__value, domain=None, range=str)

slots.metadataEntry__datatype = Slot(uri=NARAD.datatype, name="metadataEntry__datatype", curie=NARAD.curie('datatype'),
                   model_uri=NARAD.metadataEntry__datatype, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.componentRelation__context = Slot(uri=NARAD.context, name="componentRelation__context", curie=NARAD.curie('context'),
                   model_uri=NARAD.componentRelation__context, domain=None, range=Optional[Union[str, "RelationContextEnum"]])

slots.componentRelation__beamline_context = Slot(uri=NARAD.beamline_context, name="componentRelation__beamline_context", curie=NARAD.curie('beamline_context'),
                   model_uri=NARAD.componentRelation__beamline_context, domain=None, range=Optional[Union[str, BeamlineId]])

slots.componentRelation__reference_frame = Slot(uri=NARAD.reference_frame, name="componentRelation__reference_frame", curie=NARAD.curie('reference_frame'),
                   model_uri=NARAD.componentRelation__reference_frame, domain=None, range=Optional[Union[str, "ReferenceFrameEnum"]])

slots.componentRelation__distance_value = Slot(uri=NARAD.distance_value, name="componentRelation__distance_value", curie=NARAD.curie('distance_value'),
                   model_uri=NARAD.componentRelation__distance_value, domain=None, range=Optional[float])

slots.componentRelation__distance_unit = Slot(uri=NARAD.distance_unit, name="componentRelation__distance_unit", curie=NARAD.curie('distance_unit'),
                   model_uri=NARAD.componentRelation__distance_unit, domain=None, range=Optional[Union[str, "UnitEnum"]])

slots.componentRelation__axis = Slot(uri=NARAD.axis, name="componentRelation__axis", curie=NARAD.curie('axis'),
                   model_uri=NARAD.componentRelation__axis, domain=None, range=Optional[Union[str, "AxisEnum"]])

slots.componentRelation__direction = Slot(uri=NARAD.direction, name="componentRelation__direction", curie=NARAD.curie('direction'),
                   model_uri=NARAD.componentRelation__direction, domain=None, range=Optional[Union[str, "DirectionEnum"]])

slots.componentRelation__tolerance_value = Slot(uri=NARAD.tolerance_value, name="componentRelation__tolerance_value", curie=NARAD.curie('tolerance_value'),
                   model_uri=NARAD.componentRelation__tolerance_value, domain=None, range=Optional[float])

slots.componentRelation__tolerance_unit = Slot(uri=NARAD.tolerance_unit, name="componentRelation__tolerance_unit", curie=NARAD.curie('tolerance_unit'),
                   model_uri=NARAD.componentRelation__tolerance_unit, domain=None, range=Optional[Union[str, "UnitEnum"]])

slots.SignalBinding_subject = Slot(uri=RDF.subject, name="SignalBinding_subject", curie=RDF.curie('subject'),
                   model_uri=NARAD.SignalBinding_subject, domain=SignalBinding, range=Union[str, PhysicalComponentId])

slots.SignalBinding_predicate = Slot(uri=RDF.predicate, name="SignalBinding_predicate", curie=RDF.curie('predicate'),
                   model_uri=NARAD.SignalBinding_predicate, domain=SignalBinding, range=Union[str, "SignalBindingPredicateEnum"])

slots.SignalBinding_object = Slot(uri=RDF.object, name="SignalBinding_object", curie=RDF.curie('object'),
                   model_uri=NARAD.SignalBinding_object, domain=SignalBinding, range=Union[str, SignalId])

slots.ComponentRelation_subject = Slot(uri=RDF.subject, name="ComponentRelation_subject", curie=RDF.curie('subject'),
                   model_uri=NARAD.ComponentRelation_subject, domain=ComponentRelation, range=Union[str, ComponentId])

slots.ComponentRelation_predicate = Slot(uri=RDF.predicate, name="ComponentRelation_predicate", curie=RDF.curie('predicate'),
                   model_uri=NARAD.ComponentRelation_predicate, domain=ComponentRelation, range=Union[str, "ComponentRelationPredicateEnum"])

slots.ComponentRelation_object = Slot(uri=RDF.object, name="ComponentRelation_object", curie=RDF.curie('object'),
                   model_uri=NARAD.ComponentRelation_object, domain=ComponentRelation, range=Union[str, ComponentId])
