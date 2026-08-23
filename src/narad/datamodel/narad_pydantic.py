from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'pals',
     'default_range': 'string',
     'description': 'A lightweight LinkML schema for facility-agnostic accelerator '
                    'components, their beamline relationships, and associated '
                    'control-system signals.',
     'id': 'https://w3id.org/accelerator-core',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'accelerator_core',
     'prefixes': {'BFO': {'prefix_prefix': 'BFO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BFO_'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  '_base': {'prefix_prefix': '_base',
                            'prefix_reference': 'https://pals-project.readthedocs.io/'},
                  'acc': {'prefix_prefix': 'acc',
                          'prefix_reference': 'https://example.org/accelerator-core/'},
                  'inst': {'prefix_prefix': 'inst',
                           'prefix_reference': 'https://example.org/pals-instance/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'om': {'prefix_prefix': 'om',
                         'prefix_reference': 'http://www.ontology-of-units-of-measure.org/resource/om-2/'},
                  'pals': {'prefix_prefix': 'pals',
                           'prefix_reference': 'https://pals-project.readthedocs.io/'},
                  'quantitykind': {'prefix_prefix': 'quantitykind',
                                   'prefix_reference': 'http://qudt.org/vocab/quantitykind/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'saref': {'prefix_prefix': 'saref',
                            'prefix_reference': 'https://saref.etsi.org/core/v4.1.1/'},
                  'sosa': {'prefix_prefix': 'sosa',
                           'prefix_reference': 'http://www.w3.org/ns/sosa/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/narad/schema/narad.yaml',
     'title': 'Accelerator Core Ontology'} )

class IdentifierTypeEnum(str, Enum):
    """
    Controlled values for identifier types.
    """
    DOI = "DOI"
    """
    Digital Object Identifier.
    """
    PURL = "PURL"
    """
    Persistent Uniform Resource Locator.
    """
    ROR = "ROR"
    """
    Research Organization Registry identifier.
    """
    LOCAL = "LOCAL"
    """
    Local identifier, specific to the facility or source system.
    """
    URL = "URL"
    """
    Uniform Resource Locator.
    """
    ARK = "ARK"
    """
    Archival Resource Key.
    """


class SourceSystemEnum(str, Enum):
    """
    Controlled values for facility-local source systems.
    """
    EPICS = "EPICS"
    """
    EPICS control system.
    """
    EPICS_ChannelAccess = "EPICS_ChannelAccess"
    """
    EPICS Channel Access source.
    """
    PALS_Ext = "PALS_Ext"
    """
    PALS-Ext or middle-layer channel/export system.
    """
    MYA = "MYA"
    """
    MYA archive or historical channel service.
    """
    ElementDatabase = "ElementDatabase"
    """
    Facility element database.
    """
    ChannelDatabase = "ChannelDatabase"
    """
    Facility channel database.
    """
    Simulation = "Simulation"
    """
    Simulation or model-derived signal source.
    """
    Other = "Other"
    """
    Other source system.
    """


class PhysicalRelationEnum(str, Enum):
    """
    Controlled values for physical relation to the beamline.
    """
    Inline = "Inline"
    """
    Beam passes through the physical component or beamline aperture. The physical component is physically on the beamline.
    """
    AttachedToPipe = "AttachedToPipe"
    """
    Mechanically attached to the beam pipe or vacuum envelope.
    """
    NearBeamLine = "NearBeamLine"
    """
    Near and operationally associated with the beamline.
    """
    SupportingFacility = "SupportingFacility"
    """
    Supports accelerator operation without a specific beam-pipe placement.
    """


class VirtualRelationEnum(str, Enum):
    """
    Controlled values for virtual relation to the beamline.
    """
    Inline = "Inline"
    """
    Beam passes through the virtual component. Used for virtual components like Markers that represent important locations on the beamline but don't have a physical instantiation.
    """
    AssociatedWithBeamLine = "AssociatedWithBeamLine"
    """
    Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the BeamLine structure and function but don't have a direct physical relationship to the beam path,  such as BeamLineSections or Markers that are not inline with the beam.
    """
    NotAssociatedWithBeamLine = "NotAssociatedWithBeamLine"
    """
    Not inline with the BeamLine and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the BeamLine, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the BeamLine structure.
    """


class PhysicalFunctionEnum(str, Enum):
    """
    Broad device-level functions.
    """
    Focusing = "Focusing"
    """
    Focuses or defocuses the beam.
    """
    Steering = "Steering"
    """
    Steers the beam in a transverse plane.
    """
    BeamPositionMeasurement = "BeamPositionMeasurement"
    """
    Measures transverse beam position.
    """
    VacuumGeneration = "VacuumGeneration"
    """
    Generates or maintains vacuum.
    """
    RadiationMonitoring = "RadiationMonitoring"
    """
    Monitors radiation dose or dose rate.
    """
    Measurement = "Measurement"
    """
    Measures beam or machine state.
    """
    BeamAcceleration = "BeamAcceleration"
    """
    Accelerates the beam.
    """
    BeamLossDetection = "BeamLossDetection"
    """
    Detects beam loss.
    """
    BeamCurrentMeasurement = "BeamCurrentMeasurement"
    """
    Measures beam current or intensity.
    """
    BeamProfileMeasurement = "BeamProfileMeasurement"
    """
    Measures beam profile.
    """
    MachineProtection = "MachineProtection"
    """
    Supports machine protection.
    """
    TimingSynchronization = "TimingSynchronization"
    """
    Supports timing or synchronization.
    """


class FacilityFunctionEnum(str, Enum):
    """
    Broad structural or support functions.
    """
    Support = "Support"
    """
    Provides mechanical support for accelerator operations.
    """
    Alignment = "Alignment"
    """
    Supports alignment of accelerator components.
    """
    PowerSupply = "PowerSupply"
    """
    Provides electrical power to accelerator components.
    """
    ControlRack = "ControlRack"
    """
    Houses control electronics for accelerator components.
    """
    Cooling = "Cooling"
    """
    Provides cooling for accelerator components.
    """
    Diagnostics = "Diagnostics"
    """
    Provides diagnostic capabilities for accelerator components, such as monitoring or measurement.
    """
    Detection = "Detection"
    """
    Provides detection capabilities for accelerator components, such as radiation or particle detection.
    """


class VirtualFunctionEnum(str, Enum):
    """
    Broad virtual component functions or roles.
    """
    BeamLineSection = "BeamLineSection"
    """
    A section of the BeamLine used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector.
    """
    Mark = "Mark"
    """
    A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device.
    """
    DriftSpace = "DriftSpace"
    """
    A field-free longitudinal interval separating beamline components.
    """
    Fork = "Fork"
    """
    A virtual component representing a branching point in the beamline,  such as a beamline fork or switchyard.
    """
    Control = "Control"
    """
    A virtual component representing a control system function or role that is important for understanding the overall accelerator system  but doesn't have a direct relationship to the beamline structure,  such as the EPICS control system that manages device process variables across the accelerator.
    """


class PlaneEnum(str, Enum):
    """
    Controlled values for transverse plane.
    """
    Horizontal = "Horizontal"
    """
    Horizontal transverse plane.
    """
    Vertical = "Vertical"
    """
    Vertical transverse plane.
    """


class SignalRoleEnum(str, Enum):
    """
    Roles for control-system signals.
    """
    Setpoint = "Setpoint"
    """
    Requested or configured value.
    """
    Readback = "Readback"
    """
    Measured or reported value.
    """
    Status = "Status"
    """
    State or condition indicator.
    """
    Command = "Command"
    """
    Command or action trigger.
    """
    MinimumLimit = "MinimumLimit"
    """
    Minimum allowed signal value.
    """
    MaximumLimit = "MaximumLimit"
    """
    Maximum allowed signal value.
    """
    RangeLimit = "RangeLimit"
    """
    A signal containing both upper and lower allowed limits.
    """


class CanonicalSignalTypeEnum(str, Enum):
    """
    Portable semantic meanings for important signals.
    """
    HorizontalBeamPosition = "HorizontalBeamPosition"
    """
    Horizontal beam position signal.
    """
    VerticalBeamPosition = "VerticalBeamPosition"
    """
    Vertical beam position signal.
    """
    HorizontalBeamPositionOffset = "HorizontalBeamPositionOffset"
    """
    Horizontal beam position offset signal.
    """
    VerticalBeamPositionOffset = "VerticalBeamPositionOffset"
    """
    Vertical beam position offset signal.
    """
    BeamIntensity = "BeamIntensity"
    """
    Beam intensity or current signal.
    """
    DeviceStatus = "DeviceStatus"
    """
    Device status signal.
    """
    GradientSetpoint = "GradientSetpoint"
    """
    Cavity accelerating gradient setpoint signal.
    """
    GradientReadback = "GradientReadback"
    """
    Cavity accelerating gradient readback signal.
    """
    MagnetCurrentSetpoint = "MagnetCurrentSetpoint"
    """
    Magnet current setpoint signal.
    """
    MagnetCurrentReadback = "MagnetCurrentReadback"
    """
    Magnet current readback signal.
    """
    MagnetFieldSetpoint = "MagnetFieldSetpoint"
    """
    Magnet field setpoint signal.
    """
    MagnetCurrentRange = "MagnetCurrentRange"
    """
    Magnet current range signal.
    """
    IntegratedFieldSetpoint = "IntegratedFieldSetpoint"
    """
    Integrated magnetic field setpoint signal.
    """
    IntegratedFieldReadback = "IntegratedFieldReadback"
    """
    Integrated magnetic field readback signal.
    """
    VacuumPressure = "VacuumPressure"
    """
    Vacuum pressure signal.
    """
    IonPumpCurrent = "IonPumpCurrent"
    """
    Ion pump current signal.
    """
    IonPumpVoltage = "IonPumpVoltage"
    """
    Ion pump voltage signal.
    """
    GammaDoseRate = "GammaDoseRate"
    """
    Gamma radiation dose-rate signal.
    """
    NeutronDoseRate = "NeutronDoseRate"
    """
    Neutron radiation dose-rate signal.
    """
    Status = "Status"
    """
    Generic status signal for a device.
    """


class QuantityKindEnum(str, Enum):
    """
    Physical quantity kinds for signals.
    """
    BeamPosition = "BeamPosition"
    """
    Beam transverse position.
    """
    State = "State"
    """
    Device state or condition.
    """
    ElectricCurrent = "ElectricCurrent"
    """
    Electric current.
    """
    IntegratedMagneticField = "IntegratedMagneticField"
    """
    Integrated magnetic field.
    """
    MagneticField = "MagneticField"
    """
    Magnetic field.
    """
    Pressure = "Pressure"
    """
    Gas or vacuum pressure.
    """
    DoseRate = "DoseRate"
    """
    Radiation dose rate.
    """
    Voltage = "Voltage"
    """
    Electric potential difference.
    """
    Power = "Power"
    """
    Power.
    """
    CavityPhase = "CavityPhase"
    """
    Cavity phase.
    """
    CavityGradient = "CavityGradient"
    """
    Cavity accelerating gradient.
    """


class UnitEnum(str, Enum):
    """
    Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available.
    """
    A = "A"
    """
    ampere
    """
    degree = "degree"
    """
    degree
    """
    eV = "eV"
    """
    electron volt
    """
    eV_per_c = "eV_per_c"
    """
    momentum in electron volts per speed of light
    """
    eV_per_c2 = "eV_per_c2"
    """
    mass in electron volts per speed of light squared
    """
    fundamental_charge = "fundamental_charge"
    """
    fundamental charge
    """
    G_per_cm = "G_per_cm"
    """
    gauss per centimeter
    """
    Hz = "Hz"
    """
    hertz
    """
    kW = "kW"
    """
    kilowatt
    """
    m = "m"
    """
    meter
    """
    mm = "mm"
    """
    millimeter
    """
    mrem_per_h = "mrem_per_h"
    """
    millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary.
    """
    MV_per_m = "MV_per_m"
    """
    megavolt per meter
    """
    PA = "PA"
    """
    pascal
    """
    randians_pi2 = "randians_pi2"
    """
    radians divided by 2 pi - angles and phases
    """
    rem_per_h = "rem_per_h"
    """
    rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary.
    """
    seconds = "seconds"
    """
    second
    """
    T = "T"
    """
    tesla
    """
    T_M = "T_M"
    """
    tesla meter
    """
    Torr = "Torr"
    """
    torr
    """
    V = "V"
    """
    volt
    """
    V_per_m = "V_per_m"
    """
    volt per meter
    """
    unitless = "unitless"
    """
    dimensionless numeric value
    """
    none = "none"
    """
    no unit or not applicable
    """


class DataTypeEnum(str, Enum):
    """
    Data types for parameter values.
    """
    String = "String"
    """
    string data type
    """
    Integer = "Integer"
    """
    integer data type
    """
    Float = "Float"
    """
    floating-point data type
    """
    Boolean = "Boolean"
    """
    boolean data type
    """
    FloatArray = "FloatArray"
    """
    An array of floating-point values.
    """


class CoordinateSystemEnum(str, Enum):
    """
    Coordinate systems for spatial relationships.
    """
    Cartesian = "Cartesian"
    """
    Cartesian coordinate system (x, y, z).
    """
    Cylindrical = "Cylindrical"
    """
    Cylindrical coordinate system (r, theta, z).
    """
    Spherical = "Spherical"
    """
    Spherical coordinate system (r, theta, phi).
    """


class RelationContextEnum(str, Enum):
    beamline_order = "beamline_order"
    Euclidean_3D = "Euclidean_3D"
    Euclidean_2D = "Euclidean_2D"
    floorplan = "floorplan"
    containment = "containment"
    installation_mounting = "installation_mounting"


class ReferenceFrameEnum(str, Enum):
    beam_direction = "beam_direction"
    facility_coordinates = "facility_coordinates"
    local_component_frame = "local_component_frame"
    tunnel_stationing = "tunnel_stationing"


class DirectionEnum(str, Enum):
    upstream = "upstream"
    downstream = "downstream"
    positive = "positive"
    negative = "negative"


class MultipoleGeometryEnum(str, Enum):
    """
    The geometric configuration of the multipole field.  Sets the geometry used to calculate multipoles.
    """
    follows_ref_geometry = "follows_ref_geometry"
    """
    Use geometry equivalent to the setting of `ref_geometry`.
    """
    vertically_pure = "vertically_pure"
    """
    Vertically pure multipoles with arc geometry.
    """
    horizontally_pure = "horizontally_pure"
    """
    Horizontally pure multipoles with arc geometry.
    """
    chord = "chord"
    """
    Z-axis is the chord connecting the entrance origin point to the exit origin point.
    """
    entrance_coords = "entrance_coords"
    """
    Rectangular coordinates commensurate with the entrance coordinates.
    """
    exit_coords = "exit_coords"
    """
    Rectangular coordinates commensurate with the exit coordinates.
    """


class ReferenceGeometryEnum(str, Enum):
    """
    The reference geometry used to calculate multipoles.  Sets the geometry used to calculate multipoles.
    """
    arc = "arc"
    """
    Default. Reference are the curvelinear arc coordinates.
    """
    chord = "chord"
    """
    Z-axis is the chord connecting the entrance origin point to the exit origin point.
    """
    entrance_coords = "entrance_coords"
    """
    Rectangular coordinates commensurate with the entrance coordinates.
    """
    exit_coords = "exit_coords"
    """
    Rectangular coordinates commensurate with the exit coordinates.
    """


class CavityTypeEnum(str, Enum):
    """
    The type of cavity, which determines the field configuration and mode structure.
    """
    STANDING_WAVE = "STANDING_WAVE"
    """
    Default. A cavity that supports standing wave modes, typically with fixed geometry and resonant frequencies.
    """
    TRAVELING_WAVE = "TRAVELING_WAVE"
    """
    A cavity that supports traveling wave modes, typically with a waveguide structure and phase velocity matching the beam.
    """


class ZeroPhaseEnum(str, Enum):
    """
    The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity.
    """
    ACCELERATING = "ACCELERATING"
    """
    Default. The zero phase is the maximum accelerating phase, where the beam gains energy.
    """
    BELOW_TRANSITION = "BELOW_TRANSITION"
    """
    Zero phase is at the stable zero crossing for particles below transition.
    """
    ABOVE_TRANSITION = "ABOVE_TRANSITION"
    """
    Zero phase is at the stable zero crossing for particles above transition..
    """



class Node(ConfiguredBaseModel):
    """
    Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/accelerator-core'})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Node"] = Field(default="Node", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class PALSAccelerator(ConfiguredBaseModel):
    """
    Root container for accelerator core components, semantic signals, and local bindings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'tree_root': True})

    kind: Literal["PALSAccelerator"] = Field(default="PALSAccelerator", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description of the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator', 'MetaParamGroup', 'BeamLine']} })
    affiliation: Optional[Affiliation] = Field(default=None, description="""The affiliation of the author or component, as a ROR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator', 'Author']} })
    version: Optional[str] = Field(default=None, description="""Version of the representation of a particle accelerator and its operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator']} })
    authors: Optional[list[Author]] = Field(default=[], description="""Contains the authorship information for this representation of an accelerator facility and its operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator']} })
    notes: Optional[list[str]] = Field(default=[], description="""Additional notes or comments about the representation of a particle accelerator and its operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator']} })
    facility: Optional[Facility] = Field(default=None, description="""A facility that contains lattice elements (physical and virtual), beamlines, parameter set commands, signals, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator']} })

    @field_validator('version')
    def pattern_version(cls, v):
        pattern=re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid version format: {v}"
            raise ValueError(err_msg)
        return v


class Author(ConfiguredBaseModel):
    """
    Contains authorship information for a representation of an accelerator facility and its operations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    name: Optional[str] = Field(default=None, description="""The name of the entity. For example, the name of the person or organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Author', 'Affiliation']} })
    affiliation: Optional[Affiliation] = Field(default=None, description="""The affiliation of the author or component, as a ROR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator', 'Author']} })
    email: Optional[str] = Field(default=None, description="""The email address of the author.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Author']} })
    orcid: Optional[str] = Field(default=None, description="""The ORCID identifier of the author.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Author']} })

    @field_validator('email')
    def pattern_email(cls, v):
        pattern=re.compile(r"^[^@]+@[^@]+\.[^@]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid email format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid email format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('orcid')
    def pattern_orcid(cls, v):
        pattern=re.compile(r"^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[\dX]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid orcid format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid orcid format: {v}"
            raise ValueError(err_msg)
        return v


class Facility(ConfiguredBaseModel):
    """
    A facility that houses one or more accelerators.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    identifiers: Optional[list[Identifier]] = Field(default=[], description="""A unique and ideally persistent identifier for the facility, such as a DOI or ROR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility', 'Affiliation']} })
    components: Optional[list[Union[Component,PhysicalComponent,VirtualComponent,BeamLine,BookkeepingComponent,Drift,Marker,BeginningEle,BeamLineSection,Magnet,DiagnosticDevice,Cavity,SupportingFacilityComponent,CrabCavity,RFCavity,NormalConductingRFCavity,SuperConductingRFCavity,BeamProfileMonitor,BeamPositionMonitor,Aperture,RadiationMonitor,Solenoid,Multipole,Kicker,ACKicker,Bend,Quadrupole,Octupole,Sextupole]]] = Field(default=[], description="""A list of physical components in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })
    beamlines: Optional[list[BeamLine]] = Field(default=[], description="""A list of beamlines in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })
    signals: Optional[list[Signal]] = Field(default=[], description="""A list of signals in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })
    signal_bindings: Optional[list[Union[SignalBinding,HasSignal,HasSetpointSignal,HasReadbackSignal,HasCommandSignal,HasLimitSignal]]] = Field(default=[], description="""A list of signal bindings in the accelerator system (Component <-> Signal relationships).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })
    component_relations: Optional[list[Union[ComponentRelation,Precedes,Contains,Controls,IsPartOf,AdjacentTo,Overlaps,HasConnectingBranch,MountedOn,Intersects,NearestTo]]] = Field(default=[], description="""A list of component relations in the accelerator system (Component <-> Component relationships).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })


class Affiliation(ConfiguredBaseModel):
    """
    Contains affiliation information for an author or component, such as a ROR.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    name: Optional[str] = Field(default=None, description="""The name of the entity. For example, the name of the person or organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Author', 'Affiliation']} })
    identifiers: Optional[list[Identifier]] = Field(default=[], description="""A unique and ideally persistent identifier for the facility, such as a DOI or ROR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility', 'Affiliation']} })


class Identifier(ConfiguredBaseModel):
    """
    A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    identifier_type: Optional[IdentifierTypeEnum] = Field(default=None, description="""The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Identifier']} })
    identifier_value: Optional[str] = Field(default=None, description="""The value of the identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Identifier']} })


class ParamGroup(ConfiguredBaseModel):
    """
    Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/accelerator-core'})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasMetaP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })


class MetaParamGroup(ParamGroup):
    """
    Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:MetaP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    description: Optional[str] = Field(default=None, description="""A human-readable description of the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator', 'MetaParamGroup', 'BeamLine']} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaParamGroup'], 'slot_uri': 'pals:label'} })
    additional_metadata: Optional[list[AdditionalMetadata]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaParamGroup']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasFloorP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })


class FloorParamGroup(ParamGroup):
    """
    Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:FloorP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorParamGroup'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorParamGroup'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorParamGroup'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorParamGroup'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorParamGroup'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorParamGroup'],
         'slot_uri': 'pals:psi'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasBodyShiftP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })


class BodyShiftParamGroup(ParamGroup):
    """
    Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:BodyShiftP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftParamGroup'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftParamGroup'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftParamGroup'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftParamGroup'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftParamGroup'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftParamGroup'],
         'slot_uri': 'pals:z_rot'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasLongitudinalPlacementP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })


class LongitudinalPlacementParamGroup(ParamGroup):
    """
    Mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core',
         'rules': [{'description': 'An element must have a length and/or a position '
                                   'along the beamline.',
                    'postconditions': {'any_of': [{'slot_conditions': {'length': {'name': 'length',
                                                                                  'value_presence': 'PRESENT'}}},
                                                  {'slot_conditions': {'s_position': {'name': 's_position',
                                                                                      'value_presence': 'PRESENT'}}}]},
                    'preconditions': {'slot_conditions': {'id': {'name': 'id',
                                                                 'value_presence': 'PRESENT'}}}}]})

    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LongitudinalPlacementParamGroup', 'BeamLine'],
         'slot_uri': 'pals:length'} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LongitudinalPlacementParamGroup'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasReferenceP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })


class ReferenceParamGroup(ParamGroup):
    """
    Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:ReferenceP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceParamGroup'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceParamGroup'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceParamGroup'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceParamGroup'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasSolenoidP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    SolenoidP: Optional[SolenoidParamGroup] = Field(default=None, description="""A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasSolenoidP']} })


class SolenoidParamGroup(ParamGroup):
    """
    Mixin for solenoid-specific parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:SolenoidP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'rules': [{'description': 'A solenoid must have one of, and exactly one of, '
                                   'Ksol or Bsol.',
                    'postconditions': {'exactly_one_of': [{'slot_conditions': {'Ksol': {'name': 'Ksol',
                                                                                        'value_presence': 'PRESENT'}}},
                                                          {'slot_conditions': {'Bsol': {'name': 'Bsol',
                                                                                        'value_presence': 'PRESENT'}}}]},
                    'preconditions': {'slot_conditions': {'id': {'name': 'id',
                                                                 'value_presence': 'PRESENT'}}}}]})

    Ksol: Optional[float] = Field(default=None, description="""Normalized solenoid strength.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidParamGroup'], 'slot_uri': 'pals:Ksol'} })
    Bsol: Optional[float] = Field(default=None, description="""Solenoid field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidParamGroup'],
         'slot_uri': 'pals:Bsol',
         'unit': {'ucum_code': 'T'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasTwissP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })


class TwissParamGroup(ParamGroup):
    """
    Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:TwissP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissParamGroup'],
         'slot_uri': 'pals:phi_b'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasRFP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    RFP: Optional[RFParamGroup] = Field(default=None, description="""A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasRFP']} })


class RFParamGroup(ParamGroup):
    """
    Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:RFP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    frequency: Optional[float] = Field(default=None, description="""RF frequency.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'],
         'slot_uri': 'pals:frequency',
         'unit': {'ucum_code': 'Hz'}} })
    harmon: Optional[int] = Field(default=None, description="""RF harmonic number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'], 'slot_uri': 'pals:harmon'} })
    voltage: Optional[float] = Field(default=None, description="""RF voltage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'],
         'slot_uri': 'pals:voltage',
         'unit': {'ucum_code': 'V'}} })
    phase: Optional[float] = Field(default=None, description="""RF phase. rad/2pi RF phase in 0 to 2*pi""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'], 'slot_uri': 'pals:phase'} })
    multipass_phase: Optional[float] = Field(default=None, description="""rad/2pi RF Phase added to multipass elements""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'], 'slot_uri': 'pals:multipass_phase'} })
    cavity_type: Optional[CavityTypeEnum] = Field(default=None, description="""Cavity type""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'], 'slot_uri': 'pals:cavity_type'} })
    num_cells: Optional[int] = Field(default=None, description="""Number of cells in the cavity""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'], 'slot_uri': 'pals:num_cells'} })
    zero_phase: Optional[ZeroPhaseEnum] = Field(default=None, description="""Sets what phase = 0 means.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'], 'slot_uri': 'pals:zero_phase'} })
    L_active: Optional[float] = Field(default=None, description="""Active acceleration length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'],
         'slot_uri': 'pals:L_active',
         'unit': {'ucum_code': 'm'}} })
    dE_ref: Optional[float] = Field(default=None, description="""Reference energy gain.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParamGroup'],
         'slot_uri': 'pals:dE_ref',
         'unit': {'ucum_code': 'eV'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasElectricMultipoleP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })


class ElectricMultipoleParamGroup(ParamGroup):
    """
    Mixin for electric multipole parameters,  which can be used to describe the electric field components of an accelerator element. This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7
      tilt: 0.7
    - order: 3
      En: 27.3
    - order: 2
      EnL: 3.47e1
    ```
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:ElectricMultipoleP'],
         'exact_mappings': ['pals:ElectricMultipoleP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    elec_components: Optional[list[MultipoleParameterGroup]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleParamGroup']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasMagneticMultipoleP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })


class MagneticMultipoleParamGroup(ParamGroup):
    """
    Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7
      tilt: 0.7
    - order: 3
      Bn: 27.3
    - order: 2
      BnL: 3.47e1
    - order: 1
      Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength
    ```
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:MagneticMultipoleP'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    mag_components: Optional[list[MultipoleParameterGroup]] = Field(default=[], description="""Magnetic multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MagneticMultipoleParamGroup']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class HasBendP(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'mixin': True})

    BendP: Optional[BendParamGroup] = Field(default=None, description="""A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBendP']} })


class BendParamGroup(ParamGroup):
    """
    Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BendP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'rules': [{'description': 'multipole_geometry must be follows_ref_geometry',
                    'postconditions': {'slot_conditions': {'multipole_geometry': {'equals_expression': 'follows_ref_geometry',
                                                                                  'name': 'multipole_geometry'}}},
                    'preconditions': {'slot_conditions': {'multipole_geometry': {'name': 'multipole_geometry',
                                                                                 'value_presence': 'PRESENT'}}}},
                   {'description': 'ref_geometry must be arc',
                    'postconditions': {'slot_conditions': {'ref_geometry': {'equals_expression': 'arc',
                                                                            'name': 'ref_geometry'}}},
                    'preconditions': {'slot_conditions': {'ref_geometry': {'name': 'ref_geometry',
                                                                           'value_presence': 'PRESENT'}}}}]})

    angle_ref: Optional[float] = Field(default=None, description="""Reference bend angle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:angle_ref',
         'unit': {'ucum_code': 'rad'}} })
    bend_field_ref: Optional[float] = Field(default=None, description="""Reference bend field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:bend_field_ref',
         'unit': {'ucum_code': 'T'}} })
    bend_field_actual: Optional[float] = Field(default=None, description="""Actual bend field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:bend_field_actual',
         'unit': {'ucum_code': 'T'}} })
    e1: Optional[float] = Field(default=None, description="""Entrance end pole face rotation with respect to a sector geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:e1',
         'unit': {'ucum_code': 'rad'}} })
    e2: Optional[float] = Field(default=None, description="""Exit end pole face rotation with respect to a sector geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:e2',
         'unit': {'ucum_code': 'rad'}} })
    e1_rect: Optional[float] = Field(default=None, description="""Entrance end pole face rotation with respect to a rectangular geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:e1_rect',
         'unit': {'ucum_code': 'rad'}} })
    e2_rect: Optional[float] = Field(default=None, description="""Exit end pole face rotation with respect to a rectangular geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:e2_rect',
         'unit': {'ucum_code': 'rad'}} })
    edge1_int: Optional[float] = Field(default=None, description="""Entrance end fringe field integral.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:edge1_int',
         'unit': {'ucum_code': 'T.m'}} })
    edge2_int: Optional[float] = Field(default=None, description="""Exit end fringe field integral.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:edge2_int',
         'unit': {'ucum_code': 'T.m'}} })
    g_ref: Optional[float] = Field(default=None, description="""Reference bend strength = 1/radius_ref""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:g_ref',
         'unit': {'ucum_code': '1/m'}} })
    g_actual: Optional[float] = Field(default=None, description="""Actual bend strength = 1/radius_actual""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:g_actual',
         'unit': {'ucum_code': '1/m'}} })
    h1: Optional[float] = Field(default=None, description="""Entrance end pole face curvature""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:h1',
         'unit': {'ucum_code': '1/m'}} })
    h2: Optional[float] = Field(default=None, description="""Exit end pole face curvature""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:h2',
         'unit': {'ucum_code': '1/m'}} })
    L_chord: Optional[float] = Field(default=None, description="""Chord length of the bend.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:L_chord',
         'unit': {'ucum_code': 'm'}} })
    L_sagitta: Optional[float] = Field(default=None, description="""Output parameter. Sagitta length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:L_sagitta',
         'unit': {'ucum_code': 'm'}} })
    L_rectangle: Optional[float] = Field(default=None, description="""Rectangular length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:L_rectangle',
         'unit': {'ucum_code': 'm'}} })
    multipole_geometry: Optional[MultipoleGeometryEnum] = Field(default=None, description="""Multipole geometry type. Must be `follows_ref_geometry`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'], 'slot_uri': 'pals:multipole_geometry'} })
    ref_geometry: Optional[ReferenceGeometryEnum] = Field(default=None, description="""Reference geometry type. Must be `arc`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'], 'slot_uri': 'pals:ref_geometry'} })
    rho_ref: Optional[float] = Field(default=None, description="""Reference bend radius.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:rho_ref',
         'unit': {'ucum_code': 'm'}} })
    tilt_ref: Optional[float] = Field(default=None, description="""Reference tilt of the bend.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParamGroup'],
         'slot_uri': 'pals:tilt_ref',
         'unit': {'ucum_code': 'rad'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })


class MultipoleParameterGroup(ConfiguredBaseModel):
    """
    A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core',
         'rules': [{'description': 'If Es is present, then Bn, Bs, Kn, Ks should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'Bn': {'name': 'Bn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Bs': {'name': 'Bs',
                                                                  'value_presence': 'ABSENT'},
                                                           'Kn': {'name': 'Kn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Ks': {'name': 'Ks',
                                                                  'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'Es': {'name': 'Es',
                                                                 'value_presence': 'PRESENT'}}}},
                   {'description': 'If En is present, then Bn, Bs, Kn, Ks should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'Bn': {'name': 'Bn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Bs': {'name': 'Bs',
                                                                  'value_presence': 'ABSENT'},
                                                           'Kn': {'name': 'Kn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Ks': {'name': 'Ks',
                                                                  'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'En': {'name': 'En',
                                                                 'value_presence': 'PRESENT'}}}},
                   {'description': 'If EnL is present, then Bn, Bs, Kn, Ks should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'Bn': {'name': 'Bn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Bs': {'name': 'Bs',
                                                                  'value_presence': 'ABSENT'},
                                                           'Kn': {'name': 'Kn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Ks': {'name': 'Ks',
                                                                  'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'EnL': {'name': 'EnL',
                                                                  'value_presence': 'PRESENT'}}}},
                   {'description': 'If EsL is present, then Bn, Bs, Kn, Ks should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'Bn': {'name': 'Bn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Bs': {'name': 'Bs',
                                                                  'value_presence': 'ABSENT'},
                                                           'Kn': {'name': 'Kn',
                                                                  'value_presence': 'ABSENT'},
                                                           'Ks': {'name': 'Ks',
                                                                  'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'EsL': {'name': 'EsL',
                                                                  'value_presence': 'PRESENT'}}}},
                   {'description': 'If Bn is present, then En, Es, EnL, EsL should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'En': {'name': 'En',
                                                                  'value_presence': 'ABSENT'},
                                                           'EnL': {'name': 'EnL',
                                                                   'value_presence': 'ABSENT'},
                                                           'Es': {'name': 'Es',
                                                                  'value_presence': 'ABSENT'},
                                                           'EsL': {'name': 'EsL',
                                                                   'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'Bn': {'name': 'Bn',
                                                                 'value_presence': 'PRESENT'}}}},
                   {'description': 'If Bs is present, then En, Es, EnL, EsL should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'En': {'name': 'En',
                                                                  'value_presence': 'ABSENT'},
                                                           'EnL': {'name': 'EnL',
                                                                   'value_presence': 'ABSENT'},
                                                           'Es': {'name': 'Es',
                                                                  'value_presence': 'ABSENT'},
                                                           'EsL': {'name': 'EsL',
                                                                   'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'Bs': {'name': 'Bs',
                                                                 'value_presence': 'PRESENT'}}}},
                   {'description': 'If Kn is present, then En, Es, EnL, EsL should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'En': {'name': 'En',
                                                                  'value_presence': 'ABSENT'},
                                                           'EnL': {'name': 'EnL',
                                                                   'value_presence': 'ABSENT'},
                                                           'Es': {'name': 'Es',
                                                                  'value_presence': 'ABSENT'},
                                                           'EsL': {'name': 'EsL',
                                                                   'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'Kn': {'name': 'Kn',
                                                                 'value_presence': 'PRESENT'}}}},
                   {'description': 'If Ks is present, then En, Es, EnL, EsL should NOT '
                                   'be present',
                    'postconditions': {'slot_conditions': {'En': {'name': 'En',
                                                                  'value_presence': 'ABSENT'},
                                                           'EnL': {'name': 'EnL',
                                                                   'value_presence': 'ABSENT'},
                                                           'Es': {'name': 'Es',
                                                                  'value_presence': 'ABSENT'},
                                                           'EsL': {'name': 'EsL',
                                                                   'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'Ks': {'name': 'Ks',
                                                                 'value_presence': 'PRESENT'}}}}]})

    order: int = Field(default=..., description="""Multipole order N (0 = dipole, 1 = quadrupole, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultipoleParameterGroup']} })
    tilt: Optional[float] = Field(default=None, description="""Tilt of the Nth multipole.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:tilt'],
         'domain_of': ['MultipoleParameterGroup'],
         'unit': {'ucum_code': 'rad'}} })
    En: Optional[float] = Field(default=None, description="""Normal component of the field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EnN'], 'domain_of': ['MultipoleParameterGroup']} })
    Es: Optional[float] = Field(default=None, description="""Skew component of the field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EsN'], 'domain_of': ['MultipoleParameterGroup']} })
    EnL: Optional[float] = Field(default=None, description="""Length-integrated normal component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EnNL'], 'domain_of': ['MultipoleParameterGroup']} })
    EsL: Optional[float] = Field(default=None, description="""Length-integrated skew component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EsNL'], 'domain_of': ['MultipoleParameterGroup']} })
    Bn: Optional[float] = Field(default=None, description="""Normal component of the magnetic field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:BnN'], 'domain_of': ['MultipoleParameterGroup']} })
    Bs: Optional[float] = Field(default=None, description="""Skew component of the magnetic field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:BsN'], 'domain_of': ['MultipoleParameterGroup']} })
    Kn: Optional[float] = Field(default=None, description="""Normalized normal component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:KnN'], 'domain_of': ['MultipoleParameterGroup']} })
    Ks: Optional[float] = Field(default=None, description="""Normalized skew component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:KsN'], 'domain_of': ['MultipoleParameterGroup']} })


class Component(HasMetaP, Node):
    """
    A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasMetaP']})

    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Component"] = Field(default="Component", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class PhysicalComponent(Component, HasLongitudinalPlacementP, HasFloorP):
    """
    A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasFloorP', 'HasLongitudinalPlacementP']})

    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["PhysicalComponent"] = Field(default="PhysicalComponent", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class VirtualComponent(Component, HasFloorP):
    """
    A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Element', 'pals:BookkeepingElement'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasFloorP']})

    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["VirtualComponent"] = Field(default="VirtualComponent", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class BeamLine(VirtualComponent):
    """
    PALS element for an ordered sequence of beamline elements defining a beam path.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BeamLine'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'length': {'description': 'The total length of the BeamLine. '
                                                  'For pals interoperability, use m as '
                                                  'the unit of length.',
                                   'name': 'length'}}})

    length: Optional[float] = Field(default=None, description="""The total length of the BeamLine. For pals interoperability, use m as the unit of length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LongitudinalPlacementParamGroup', 'BeamLine'],
         'slot_uri': 'pals:length'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description of the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PALSAccelerator', 'MetaParamGroup', 'BeamLine']} })
    multipass: Optional[bool] = Field(default=None, description="""Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamLine'], 'slot_uri': 'pals:multipass'} })
    periodic: Optional[bool] = Field(default=None, description="""Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamLine'], 'slot_uri': 'pals:periodic'} })
    repeat: Optional[int] = Field(default=None, description="""Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
If value is greater than 1, the beamline is repeated that many times.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamLine'], 'slot_uri': 'pals:repeat'} })
    direction: Optional[int] = Field(default=None, description="""Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamLine'], 'slot_uri': 'pals:direction'} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["BeamLine"] = Field(default="BeamLine", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Signal(HasMetaP, Node):
    """
    Semantic meaning of a control-system signal associated with a component.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['sosa:Sensor', 'sosa:Actuator'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasMetaP']})

    signal_role: SignalRoleEnum = Field(default=..., description="""The role of the signal in the control system, such as setpoint, readback, status, command, or limit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    source_system: SourceSystemEnum = Field(default=..., description="""The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    native_description: Optional[str] = Field(default=None, description="""A human-readable description of the signal in the source system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    canonical_signal_type: CanonicalSignalTypeEnum = Field(default=..., description="""The canonical semantic meaning of the signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    quantity_kind: QuantityKindEnum = Field(default=..., description="""The physical quantity kind of the signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    native_data_type: DataTypeEnum = Field(default=..., description="""The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    native_unit: UnitEnum = Field(default=..., description="""The native unit of the signal in the source system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    access_protocol: Optional[str] = Field(default=None, description="""The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    archive_identifier: Optional[str] = Field(default=None, description="""The identifier used to reference the signal in an archival system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Signal"] = Field(default="Signal", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Magnet(PhysicalComponent, HasTwissP, HasReferenceP, HasBodyShiftP):
    """
    An accelerator device that produces a magnetic field for beam control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasReferenceP', 'HasBodyShiftP', 'HasTwissP']})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Magnet"] = Field(default="Magnet", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Solenoid(Magnet, HasSolenoidP):
    """
    A magnet with a primarily longitudinal magnetic field used for focusing.
    A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. 
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Solenoid'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasSolenoidP']})

    SolenoidP: Optional[SolenoidParamGroup] = Field(default=None, description="""A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasSolenoidP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Solenoid"] = Field(default="Solenoid", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Multipole(Magnet, HasMagneticMultipoleP, HasElectricMultipoleP):
    """
    A general magnet with a higher-order multipole field, such as a sextupole or octupole.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Multipole'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasElectricMultipoleP', 'HasMagneticMultipoleP']})

    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Multipole"] = Field(default="Multipole", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Bend(Multipole, HasBendP):
    """
    Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Dipole'],
         'exact_mappings': ['pals:Bend'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasBendP']})

    BendP: Optional[BendParamGroup] = Field(default=None, description="""A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBendP']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Bend"] = Field(default="Bend", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Quadrupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 4 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Quadrupole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Quadrupole"] = Field(default="Quadrupole", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Octupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 8 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Octupole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Octupole"] = Field(default="Octupole", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Sextupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 6 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Sextupole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Sextupole"] = Field(default="Sextupole", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Kicker(Magnet, HasMagneticMultipoleP, HasElectricMultipoleP):
    """
    A magnet primarily used to steer the beam.
    Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. 
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Corrector',
                     'HCorrector',
                     'VCorrector',
                     'VDiagKicker',
                     'HDiagKicker'],
         'broad_mappings': ['pals:Kicker'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasElectricMultipoleP', 'HasMagneticMultipoleP']})

    plane: Optional[PlaneEnum] = Field(default=None, description="""The transverse plane in which the kicker operates, either horizontal or vertical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Kicker']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Kicker"] = Field(default="Kicker", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class ACKicker(Kicker):
    """
    An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:ACKicker'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    plane: Optional[PlaneEnum] = Field(default=None, description="""The transverse plane in which the kicker operates, either horizontal or vertical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Kicker']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["ACKicker"] = Field(default="ACKicker", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class DiagnosticDevice(PhysicalComponent):
    """
    An accelerator device used to measure beam or machine state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["DiagnosticDevice"] = Field(default="DiagnosticDevice", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class BeamProfileMonitor(DiagnosticDevice, HasTwissP, HasReferenceP, HasBodyShiftP):
    """
    A diagnostic device used to measure transverse beam profile.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasReferenceP', 'HasBodyShiftP', 'HasTwissP']})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["BeamProfileMonitor"] = Field(default="BeamProfileMonitor", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class BeamPositionMonitor(DiagnosticDevice, HasTwissP, HasReferenceP, HasBodyShiftP):
    """
    A diagnostic device used to measure transverse beam position.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasReferenceP', 'HasBodyShiftP', 'HasTwissP']})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["BeamPositionMonitor"] = Field(default="BeamPositionMonitor", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Aperture(DiagnosticDevice, HasTwissP, HasReferenceP):
    """
    A diagnostic or limiting aperture element used to constrain or characterize beam passage.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasReferenceP', 'HasTwissP']})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Aperture"] = Field(default="Aperture", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class RadiationMonitor(DiagnosticDevice, HasBodyShiftP):
    """
    A diagnostic device used to monitor radiation dose or dose rate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasBodyShiftP']})

    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["RadiationMonitor"] = Field(default="RadiationMonitor", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Cavity(PhysicalComponent, HasMagneticMultipoleP, HasElectricMultipoleP, HasTwissP, HasReferenceP, HasBodyShiftP):
    """
    A cavity used for beam acceleration or manipulation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasReferenceP',
                    'HasElectricMultipoleP',
                    'HasMagneticMultipoleP',
                    'HasBodyShiftP',
                    'HasTwissP']})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Cavity"] = Field(default="Cavity", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class CrabCavity(Cavity):
    """
    A cavity used for transverse beam manipulation, such as crabbing or deflecting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:CrabCavity'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["CrabCavity"] = Field(default="CrabCavity", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class RFCavity(Cavity, HasRFP):
    """
    A cavity used for RF acceleration or longitudinal manipulation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'exact_mappings': ['pals:RFCavity'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasRFP']})

    RFP: Optional[RFParamGroup] = Field(default=None, description="""A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasRFP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["RFCavity"] = Field(default="RFCavity", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class NormalConductingRFCavity(RFCavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation, which is normal conducting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:RFCavity'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    RFP: Optional[RFParamGroup] = Field(default=None, description="""A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasRFP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["NormalConductingRFCavity"] = Field(default="NormalConductingRFCavity", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class SuperConductingRFCavity(RFCavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:RFCavity'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    RFP: Optional[RFParamGroup] = Field(default=None, description="""A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasRFP']} })
    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    ElectricMultipoleP: Optional[ElectricMultipoleParamGroup] = Field(default=None, description="""A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasElectricMultipoleP']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParamGroup] = Field(default=None, description="""A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMagneticMultipoleP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["SuperConductingRFCavity"] = Field(default="SuperConductingRFCavity", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class SupportingFacilityComponent(PhysicalComponent, HasLongitudinalPlacementP, HasBodyShiftP, HasFloorP):
    """
    A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:StructuralElement'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasFloorP', 'HasLongitudinalPlacementP', 'HasBodyShiftP']})

    functions: list[FacilityFunctionEnum] = Field(default=..., description="""The function of the supporting facility component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:supporting_facility_function'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:physical_beamline_relation'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["SupportingFacilityComponent"] = Field(default="SupportingFacilityComponent", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class BookkeepingComponent(VirtualComponent, HasBodyShiftP):
    """
    A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:BookkeepingElement'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasBodyShiftP']})

    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["BookkeepingComponent"] = Field(default="BookkeepingComponent", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Marker(BookkeepingComponent, HasTwissP):
    """
    A virtual component used as a reference point or marker in the beamline structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Marker'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasTwissP']})

    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Marker"] = Field(default="Marker", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class BeginningEle(BookkeepingComponent, HasTwissP, HasReferenceP):
    """
    Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference parameters; otherwise it is expected to be the first element in the branch.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BeginningEle'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasReferenceP', 'HasTwissP']})

    ReferenceP: Optional[ReferenceParamGroup] = Field(default=None, description="""A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasReferenceP']} })
    TwissP: Optional[TwissParamGroup] = Field(default=None, description="""A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasTwissP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["BeginningEle"] = Field(default="BeginningEle", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class Drift(VirtualComponent, HasLongitudinalPlacementP):
    """
    A field-free space between beamline components. A Drift is a virtual beamline component whose longitudinal extent preserves the separation between adjacent physical or virtual components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Drift'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasLongitudinalPlacementP']})

    LongitudinalPlacementP: Optional[LongitudinalPlacementParamGroup] = Field(default=None, description="""A mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacementP']} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["Drift"] = Field(default="Drift", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class BeamLineSection(BookkeepingComponent, HasFloorP):
    """
    A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BeamLineSection'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['HasFloorP']})

    FloorP: Optional[FloorParamGroup] = Field(default=None, description="""A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasFloorP']} })
    BodyShiftP: Optional[BodyShiftParamGroup] = Field(default=None, description="""A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasBodyShiftP']} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'pals:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'pals:virtual_beamline_relation'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    MetaP: Optional[MetaParamGroup] = Field(default=None, description="""A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMetaP']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    kind: Literal["BeamLineSection"] = Field(default="BeamLineSection", description="""The LinkML class name of this instance in uri/curie form, e.g. `pals:Quadrupole` or `pals:BeamProfileMonitor`.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Node', 'PALSAccelerator'],
         'slot_uri': 'rdf:type'} })
    alias: Optional[list[str]] = Field(default=[], description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'MetaParamGroup'], 'slot_uri': 'pals:alias'} })


class AdditionalMetadata(ConfiguredBaseModel):
    """
    A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    key: str = Field(default=..., description="""The metadata field name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdditionalMetadata']} })
    value: str = Field(default=..., description="""The metadata value, serialized as a string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdditionalMetadata']} })
    datatype: Optional[DataTypeEnum] = Field(default=None, description="""Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdditionalMetadata']} })


class Edge(ConfiguredBaseModel):
    """
    Abstract base for subject-predicate-object associations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'rdf:Statement',
         'from_schema': 'https://w3id.org/accelerator-core'})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["Edge"] = Field(default="Edge", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Edge'], 'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class SignalBinding(Edge):
    """
    Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'object': {'name': 'object', 'range': 'Signal'},
                        'subject': {'name': 'subject', 'range': 'PhysicalComponent'}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["SignalBinding"] = Field(default="SignalBinding", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Edge'], 'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class HasSignal(SignalBinding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:has_signal'}},
         'class_uri': 'pals:HasSignalRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'SignalBinding',
                                      'name': 'predicate',
                                      'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["HasSignal"] = Field(default="HasSignal", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'SignalBinding',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class HasSetpointSignal(SignalBinding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:has_setpoint_signal'}},
         'class_uri': 'pals:HasSetpointSignalRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'HasSetpointSignal',
                                      'name': 'predicate',
                                      'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["HasSetpointSignal"] = Field(default="HasSetpointSignal", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'HasSetpointSignal',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class HasReadbackSignal(SignalBinding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:has_readback_signal'}},
         'class_uri': 'pals:HasReadbackSignalRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'HasReadbackSignal',
                                      'name': 'predicate',
                                      'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["HasReadbackSignal"] = Field(default="HasReadbackSignal", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'HasReadbackSignal',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class HasCommandSignal(SignalBinding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:has_command_signal'}},
         'class_uri': 'pals:HasCommandSignalRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'HasCommandSignal',
                                      'name': 'predicate',
                                      'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["HasCommandSignal"] = Field(default="HasCommandSignal", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'HasCommandSignal',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class HasLimitSignal(SignalBinding):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:has_limit_signal'}},
         'class_uri': 'pals:HasLimitSignalRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'HasLimitSignal',
                                      'name': 'predicate',
                                      'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["HasLimitSignal"] = Field(default="HasLimitSignal", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'HasLimitSignal',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class ComponentRelation(Edge):
    """
    Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'object': {'name': 'object', 'range': 'Component'},
                        'subject': {'name': 'subject', 'range': 'Component'}}})

    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["ComponentRelation"] = Field(default="ComponentRelation", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Edge'], 'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class Precedes(ComponentRelation):
    """
    A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:precedes'}},
         'class_uri': 'pals:PrecedesRelation',
         'exact_mappings': ['BFO:0000063'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'context': {'description': 'The frame of reference / domain in '
                                                   'which this relationship is '
                                                   'asserted to hold. For '
                                                   'pals:precedes, this is the '
                                                   'Beamline context = '
                                                   'beamline_context.',
                                    'equals_expression': 'beamline_context',
                                    'name': 'context',
                                    'required': True},
                        'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'Precedes',
                                      'name': 'predicate',
                                      'required': True}}})

    beamline_context: str = Field(default=..., description="""The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Precedes', 'HasConnectingBranch']} })
    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold. For pals:precedes, this is the Beamline context = beamline_context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'equals_expression': 'beamline_context'} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["Precedes"] = Field(default="Precedes", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'Precedes',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class Contains(ComponentRelation):
    """
    A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:contains'}},
         'class_uri': 'pals:ContainsRelation',
         'exact_mappings': ['BFO:0000051'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'Contains',
                                      'name': 'predicate',
                                      'required': True}}})

    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["Contains"] = Field(default="Contains", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'Contains',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class Controls(ComponentRelation):
    """
    A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:controls'}},
         'class_uri': 'pals:ControlsRelation',
         'exact_mappings': ['saref:controls'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'Controls',
                                      'name': 'predicate',
                                      'required': True}}})

    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["Controls"] = Field(default="Controls", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'Controls',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class IsPartOf(ComponentRelation):
    """
    A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:is_part_of'}},
         'class_uri': 'pals:IsPartOfRelation',
         'exact_mappings': ['BFO:0000050'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'IsPartOf',
                                      'name': 'predicate',
                                      'required': True}}})

    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["IsPartOf"] = Field(default="IsPartOf", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'IsPartOf',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class AdjacentTo(ComponentRelation):
    """
    A relationship indicating that the subject component is adjacent to the object component and not overlapping
     in a specified context, such as radiation detector and a magnet.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:adjacent_to'}},
         'class_uri': 'pals:AdjacentToRelation',
         'exact_mappings': ['RO:0002220'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'AdjacentTo',
                                      'name': 'predicate',
                                      'required': True}}})

    distance_value: Optional[float] = Field(default=None, description="""Distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo'], 'slot_uri': 'om:Distance'} })
    distance_unit: Optional[UnitEnum] = Field(default=None, description="""Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo']} })
    tolerance_value: Optional[float] = Field(default=None, description="""Tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo']} })
    tolerance_unit: Optional[UnitEnum] = Field(default=None, description="""Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo']} })
    coordinates: Optional[CoordinateSet] = Field(default=None, description="""A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'Overlaps', 'MountedOn', 'NearestTo'],
         'recommended': True} })
    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["AdjacentTo"] = Field(default="AdjacentTo", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'AdjacentTo',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class Overlaps(ComponentRelation):
    """
    A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:overlaps'}},
         'class_uri': 'pals:OverlapsRelation',
         'exact_mappings': ['RO:0002131'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'Overlaps',
                                      'name': 'predicate',
                                      'required': True}}})

    coordinates: Optional[CoordinateSet] = Field(default=None, description="""A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'Overlaps', 'MountedOn', 'NearestTo'],
         'recommended': True} })
    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["Overlaps"] = Field(default="Overlaps", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'Overlaps',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class HasConnectingBranch(ComponentRelation):
    """
    A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:has_connecting_branch'}},
         'class_uri': 'pals:HasConnectingBranchRelation',
         'exact_mappings': ['RO:0002253'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'context': {'description': 'The frame of reference / domain in '
                                                   'which this relationship is '
                                                   'asserted to hold. For '
                                                   'pals:has_connecting_branch, this '
                                                   'is the Beamline context = '
                                                   'beamline_context.',
                                    'equals_expression': 'beamline_context',
                                    'name': 'context',
                                    'required': True},
                        'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'HasConnectingBranch',
                                      'name': 'predicate',
                                      'required': True}}})

    beamline_context: str = Field(default=..., description="""The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Precedes', 'HasConnectingBranch']} })
    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold. For pals:has_connecting_branch, this is the Beamline context = beamline_context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'equals_expression': 'beamline_context'} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["HasConnectingBranch"] = Field(default="HasConnectingBranch", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'HasConnectingBranch',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class MountedOn(ComponentRelation):
    """
    A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:mounted_on'}},
         'broad_mappings': ['RO:0002371'],
         'class_uri': 'pals:MountedOnRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'MountedOn',
                                      'name': 'predicate',
                                      'required': True}}})

    coordinates: Optional[CoordinateSet] = Field(default=None, description="""A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'Overlaps', 'MountedOn', 'NearestTo'],
         'recommended': True} })
    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["MountedOn"] = Field(default="MountedOn", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'MountedOn',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class Intersects(ComponentRelation):
    """
    A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:intersects'}},
         'broad_mappings': ['RO:0015011'],
         'class_uri': 'pals:IntersectsRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'Intersects',
                                      'name': 'predicate',
                                      'required': True}}})

    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["Intersects"] = Field(default="Intersects", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'Intersects',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class NearestTo(ComponentRelation):
    """
    A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdf_predicate': {'tag': 'rdf_predicate',
                                           'value': 'pals:nearest_to'}},
         'broad_mappings': ['RO:0002325'],
         'class_uri': 'pals:NearestToRelation',
         'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'predicate': {'description': 'The predicate of the '
                                                     'relationship, which can be used '
                                                     'to identify the relationship '
                                                     'across different source systems.',
                                      'equals_expression': 'NearestTo',
                                      'name': 'predicate',
                                      'required': True}}})

    distance_value: Optional[float] = Field(default=None, description="""Distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo'], 'slot_uri': 'om:Distance'} })
    distance_unit: Optional[UnitEnum] = Field(default=None, description="""Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo']} })
    tolerance_value: Optional[float] = Field(default=None, description="""Tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo']} })
    tolerance_unit: Optional[UnitEnum] = Field(default=None, description="""Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'NearestTo']} })
    coordinates: Optional[CoordinateSet] = Field(default=None, description="""A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdjacentTo', 'Overlaps', 'MountedOn', 'NearestTo'],
         'recommended': True} })
    context: RelationContextEnum = Field(default=..., description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    component_direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation'], 'recommended': True} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'Affiliation', 'ParamGroup', 'Edge'],
         'slot_uri': 'pals:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:subject'} })
    predicate: Literal["NearestTo"] = Field(default="NearestTo", description="""The predicate of the relationship, which can be used to identify the relationship across different source systems.""", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Edge'],
         'equals_expression': 'NearestTo',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Edge'], 'slot_uri': 'rdf:object'} })


class CoordinateSet(ConfiguredBaseModel):
    """
    A set of coordinates that define the spatial relationship between two components. This can include Cartesian coordinates, cylindrical coordinates, or other coordinate systems as needed. Useful for defining the spatial relationship where the relationship is not strictly linear or where the components are not aligned along a single axis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    coordinate_system: Optional[CoordinateSystemEnum] = Field(default=None, description="""The coordinate system used for the coordinates (e.g., Cartesian, Cylindrical).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })
    x_coord: Optional[float] = Field(default=None, description="""The x-coordinate in the specified coordinate system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })
    y_coord: Optional[float] = Field(default=None, description="""The y-coordinate in the specified coordinate system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })
    z_coord: Optional[float] = Field(default=None, description="""The z-coordinate in the specified coordinate system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })
    r_coord: Optional[float] = Field(default=None, description="""The radial distance in cylindrical coordinates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })
    theta_coord: Optional[float] = Field(default=None, description="""The angular coordinate in cylindrical coordinates (in radians).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })
    phi_coord: Optional[float] = Field(default=None, description="""The azimuthal angle in spherical coordinates (in radians).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoordinateSet']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Node.model_rebuild()
PALSAccelerator.model_rebuild()
Author.model_rebuild()
Facility.model_rebuild()
Affiliation.model_rebuild()
Identifier.model_rebuild()
ParamGroup.model_rebuild()
HasMetaP.model_rebuild()
MetaParamGroup.model_rebuild()
HasFloorP.model_rebuild()
FloorParamGroup.model_rebuild()
HasBodyShiftP.model_rebuild()
BodyShiftParamGroup.model_rebuild()
HasLongitudinalPlacementP.model_rebuild()
LongitudinalPlacementParamGroup.model_rebuild()
HasReferenceP.model_rebuild()
ReferenceParamGroup.model_rebuild()
HasSolenoidP.model_rebuild()
SolenoidParamGroup.model_rebuild()
HasTwissP.model_rebuild()
TwissParamGroup.model_rebuild()
HasRFP.model_rebuild()
RFParamGroup.model_rebuild()
HasElectricMultipoleP.model_rebuild()
ElectricMultipoleParamGroup.model_rebuild()
HasMagneticMultipoleP.model_rebuild()
MagneticMultipoleParamGroup.model_rebuild()
HasBendP.model_rebuild()
BendParamGroup.model_rebuild()
MultipoleParameterGroup.model_rebuild()
Component.model_rebuild()
PhysicalComponent.model_rebuild()
VirtualComponent.model_rebuild()
BeamLine.model_rebuild()
Signal.model_rebuild()
Magnet.model_rebuild()
Solenoid.model_rebuild()
Multipole.model_rebuild()
Bend.model_rebuild()
Quadrupole.model_rebuild()
Octupole.model_rebuild()
Sextupole.model_rebuild()
Kicker.model_rebuild()
ACKicker.model_rebuild()
DiagnosticDevice.model_rebuild()
BeamProfileMonitor.model_rebuild()
BeamPositionMonitor.model_rebuild()
Aperture.model_rebuild()
RadiationMonitor.model_rebuild()
Cavity.model_rebuild()
CrabCavity.model_rebuild()
RFCavity.model_rebuild()
NormalConductingRFCavity.model_rebuild()
SuperConductingRFCavity.model_rebuild()
SupportingFacilityComponent.model_rebuild()
BookkeepingComponent.model_rebuild()
Marker.model_rebuild()
BeginningEle.model_rebuild()
Drift.model_rebuild()
BeamLineSection.model_rebuild()
AdditionalMetadata.model_rebuild()
Edge.model_rebuild()
SignalBinding.model_rebuild()
HasSignal.model_rebuild()
HasSetpointSignal.model_rebuild()
HasReadbackSignal.model_rebuild()
HasCommandSignal.model_rebuild()
HasLimitSignal.model_rebuild()
ComponentRelation.model_rebuild()
Precedes.model_rebuild()
Contains.model_rebuild()
Controls.model_rebuild()
IsPartOf.model_rebuild()
AdjacentTo.model_rebuild()
Overlaps.model_rebuild()
HasConnectingBranch.model_rebuild()
MountedOn.model_rebuild()
Intersects.model_rebuild()
NearestTo.model_rebuild()
CoordinateSet.model_rebuild()
