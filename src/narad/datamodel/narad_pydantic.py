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


linkml_meta = LinkMLMeta({'default_prefix': 'narad',
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
                  'acc': {'prefix_prefix': 'acc',
                          'prefix_reference': 'https://w3id.org/accelerator-core/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'narad': {'prefix_prefix': 'narad',
                            'prefix_reference': 'https://example.org/narad/'},
                  'pals': {'prefix_prefix': 'pals',
                           'prefix_reference': 'https://pals-project.readthedocs.io/'},
                  'quantitykind': {'prefix_prefix': 'quantitykind',
                                   'prefix_reference': 'http://qudt.org/vocab/quantitykind/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'saref': {'prefix_prefix': 'saref',
                            'prefix_reference': 'https://saref.etsi.org/core/v4.1.1/'},
                  'sosa': {'prefix_prefix': 'sosa',
                           'prefix_reference': 'http://www.w3.org/ns/sosa/'},
                  'ssn': {'prefix_prefix': 'ssn',
                          'prefix_reference': 'http://www.w3.org/ns/ssn/'},
                  'ssn-system': {'prefix_prefix': 'ssn-system',
                                 'prefix_reference': 'http://www.w3.org/ns/ssn/systems/'},
                  'unit': {'prefix_prefix': 'unit',
                           'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/narad/schema/narad.yaml',
     'title': 'Accelerator Core Ontology'} )

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
    NearBeamline = "NearBeamline"
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
    AssociatedWithBeamline = "AssociatedWithBeamline"
    """
    Not inline with the beamline but still operationally associated with it.  Used for virtual components that are important for understanding the beamline structure and function but don't have a direct physical relationship to the beam path,  such as BeamlineSections or Markers that are not inline with the beam.
    """
    NotAssociatedWithBeamline = "NotAssociatedWithBeamline"
    """
    Not inline with the beamline and not operationally associated with it.  Used for virtual components that are more abstract and don't have a specific relationship  to the beamline, such as a virtual component representing a control system function  or role that is important for understanding the overall accelerator system but doesn't have a direct relationship to the beamline structure.
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
    BeamlineSection = "BeamlineSection"
    """
    A section of the beamline used for organizational or functional grouping of components, such as a linac section, transfer line, or ring sector.
    """
    Mark = "Mark"
    """
    A virtual component representing an important location on the beamline,  such as a reference point for beam-based alignment, a location of a known aperture restriction,  or a location of a critical diagnostic device.
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
    Limit = "Limit"
    """
    Minimum, maximum, or other constraints for an allowed signal value.
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
    mm = "mm"
    """
    millimeter
    """
    m = "m"
    """
    meter
    """
    A = "A"
    """
    ampere
    """
    T_m = "T_m"
    """
    tesla meter
    """
    Pa = "Pa"
    """
    pascal
    """
    Torr = "Torr"
    """
    torr
    """
    rem_per_h = "rem_per_h"
    """
    rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary.
    """
    mrem_per_h = "mrem_per_h"
    """
    millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary.
    """
    V = "V"
    """
    volt
    """
    kW = "kW"
    """
    kilowatt
    """
    degree = "degree"
    """
    degree
    """
    MV_per_m = "MV_per_m"
    """
    megavolt per meter
    """
    G_per_cm = "G_per_cm"
    """
    gauss per centimeter
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


class ComponentRelationPredicateEnum(str, Enum):
    precedes = "precedes"
    """
    Subject occurs immediately before object in the sequence/beamline order.
    """
    follows = "follows"
    """
    Subject occurs after object in the sequence/beamline order.
    """
    contains = "contains"
    """
    Subject spatially or mereologically contains object.
    """
    contained_in = "contained_in"
    """
    Subject is spatially or mereologically contained in object.
    """
    connected_to = "connected_to"
    """
    Subject and object are physically connected. a is connected to b if and only if a and b are discrete structure,  and there exists some connecting structure c, such that c connects a and b
    """
    controls = "controls"
    """
    Subject controls the state or behavior of object.
    """
    is_controlled_by = "is_controlled_by"
    """
    Subject is controlled by object.
    """
    is_part_of = "is_part_of"
    """
    Subject is a part of object.
    """
    has_part = "has_part"
    """
    Subject has part object.
    """
    adjacent_to = "adjacent_to"
    """
    Subject and object are spatially adjacent, without overlapping.
    """
    overlaps = "overlaps"
    """
    Subject and object share at least one part in common.
    """
    mounted_on = "mounted_on"
    """
    Subject is mounted on object.
    """
    intersects = "intersects"
    """
    Subject intersects with object.
    """
    nearest_to = "nearest_to"
    """
    Subject is nearest to object.
    """


class SignalBindingPredicateEnum(str, Enum):
    """
    Controlled predicates for Component-to-Signal bindings.
    """
    has_signal = "has_signal"
    """
    Generic association between a component and one of its signals. The specific role (setpoint, readback, status, etc.) is carried by the Signal's own signal_role field, not the predicate.
    """
    has_status_signal = "has_status_signal"
    """
    Subject has the given signal as its status indicator.
    """
    has_setpoint_signal = "has_setpoint_signal"
    """
    Subject has the given signal as its setpoint.
    """
    has_readback_signal = "has_readback_signal"
    """
    Subject has the given signal as its readback.
    """
    has_command_signal = "has_command_signal"
    """
    Subject has the given signal as a command trigger.
    """
    has_limit_signal = "has_limit_signal"
    """
    Subject has the given signal as a limit/constraint value.
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


class AxisEnum(str, Enum):
    x = "x"
    y = "y"
    z = "z"
    s = "s"


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



class NARAD(ConfiguredBaseModel):
    """
    Root container for accelerator core components, semantic signals, and local bindings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core', 'tree_root': True})

    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    description: Optional[str] = Field(default=None, description="""Human-readable description for the representation of a particle accelerator and its operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP']} })
    physical_components: Optional[list[PhysicalComponent]] = Field(default=[], description="""A list of physical components in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })
    virtual_components: Optional[list[VirtualComponent]] = Field(default=[], description="""A list of virtual components in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })
    beamlines: Optional[list[Beamline]] = Field(default=[], description="""A list of beamlines in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })
    supporting_facility_components: Optional[list[SupportingFacilityComponent]] = Field(default=[], description="""A list of supporting facility components in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })
    signals: Optional[list[Signal]] = Field(default=[], description="""A list of signals in the accelerator system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })
    signal_bindings: Optional[list[SignalBinding]] = Field(default=[], description="""A list of signal bindings in the accelerator system (Component <-> Signal relationships).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })
    component_relations: Optional[list[ComponentRelation]] = Field(default=[], description="""A list of component relations in the accelerator system (Component <-> Component relationships).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD']} })


class MetaP(ConfiguredBaseModel):
    """
    Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:MetaP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class FloorP(ConfiguredBaseModel):
    """
    Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:FloorP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })


class BodyShiftP(ConfiguredBaseModel):
    """
    Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:BodyShiftP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })


class HasLongitudinalPlacement(ConfiguredBaseModel):
    """
    Mixin for an element's extent and position along the longitudinal (beam-direction, \"s\") axis. 
    Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
    One (or both) `length` or `s_position` must be present.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True,
         'rules': [{'description': 'An element must have a length and/or a position '
                                   'along the beamline.',
                    'postconditions': {'any_of': [{'slot_conditions': {'length': {'name': 'length',
                                                                                  'value_presence': 'PRESENT'}}},
                                                  {'slot_conditions': {'s_position': {'name': 's_position',
                                                                                      'value_presence': 'PRESENT'}}}]},
                    'preconditions': {'slot_conditions': {'id': {'name': 'id',
                                                                 'value_presence': 'PRESENT'}}}}]})

    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })


class ReferenceP(ConfiguredBaseModel):
    """
    Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:ReferenceP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })


class SolenoidP(ConfiguredBaseModel):
    """
    Mixin for solenoid-specific parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:SolenoidP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True,
         'rules': [{'description': 'A solenoid must have one of, and exactly one of, '
                                   'Ksol or Bsol.',
                    'postconditions': {'exactly_one_of': [{'slot_conditions': {'Ksol': {'name': 'Ksol',
                                                                                        'value_presence': 'PRESENT'}}},
                                                          {'slot_conditions': {'Bsol': {'name': 'Bsol',
                                                                                        'value_presence': 'PRESENT'}}}]},
                    'preconditions': {'slot_conditions': {'id': {'name': 'id',
                                                                 'value_presence': 'PRESENT'}}}}]})

    Ksol: Optional[float] = Field(default=None, description="""Normalized solenoid strength.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidP'], 'slot_uri': 'pals:Ksol'} })
    Bsol: Optional[float] = Field(default=None, description="""Solenoid field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidP'],
         'slot_uri': 'pals:Bsol',
         'unit': {'ucum_code': 'T'}} })


class TwissP(ConfiguredBaseModel):
    """
    Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:TwissP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })


class ElectricMultipoleP(ConfiguredBaseModel):
    """
    Mixin for electric multipole parameters, 
    which can be used to describe the electric field components of an accelerator element.
    This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).
    Example with three multipole components (N=0,1,2): ```yaml components: - order: 7
      tilt: 0.7
    - order: 3
      En: 27.3
    - order: 2
      EnL: 3.47e1
    ```
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:ElectricMultipoleP'],
         'exact_mappings': ['pals:ElectricMultipoleP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })


class MagneticMultipoleP(ConfiguredBaseModel):
    """
    Mixin for magnetic multipole parameters, 
    which can be used to describe the magnetic field components of an accelerator element.
    This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).
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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:MagneticMultipoleP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Magnetic multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })


class BendP(ConfiguredBaseModel):
    """
    Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.
    This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BendP'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixin': True,
         'rules': [{'description': 'multipole_geometry must be follows_ref_geometry',
                    'postconditions': {'slot_conditions': {'multipole_geometry': {'equals_expression': 'follows_ref_geometry',
                                                                                  'name': 'multipole_geometry'}}}},
                   {'description': 'ref_geometry must be arc',
                    'postconditions': {'slot_conditions': {'ref_geometry': {'equals_expression': 'arc',
                                                                            'name': 'ref_geometry'}}}}]})

    angle_ref: Optional[float] = Field(default=None, description="""Reference bend angle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:angle_ref',
         'unit': {'ucum_code': 'rad'}} })
    bend_field_ref: Optional[float] = Field(default=None, description="""Reference bend field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:bend_field_ref',
         'unit': {'ucum_code': 'T'}} })
    bend_field_actual: Optional[float] = Field(default=None, description="""Actual bend field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:bend_field_actual',
         'unit': {'ucum_code': 'T'}} })
    e1: Optional[float] = Field(default=None, description="""Entrance end pole face rotation with respect to a sector geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:e1', 'unit': {'ucum_code': 'rad'}} })
    e2: Optional[float] = Field(default=None, description="""Exit end pole face rotation with respect to a sector geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:e2', 'unit': {'ucum_code': 'rad'}} })
    e1_rect: Optional[float] = Field(default=None, description="""Entrance end pole face rotation with respect to a rectangular geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:e1_rect',
         'unit': {'ucum_code': 'rad'}} })
    e2_rect: Optional[float] = Field(default=None, description="""Exit end pole face rotation with respect to a rectangular geometry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:e2_rect',
         'unit': {'ucum_code': 'rad'}} })
    edge1_int: Optional[float] = Field(default=None, description="""Entrance end fringe field integral.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:edge1_int',
         'unit': {'ucum_code': 'T.m'}} })
    edge2_int: Optional[float] = Field(default=None, description="""Exit end fringe field integral.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:edge2_int',
         'unit': {'ucum_code': 'T.m'}} })
    g_ref: Optional[float] = Field(default=None, description="""Reference bend strength = 1/radius_ref""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:g_ref', 'unit': {'ucum_code': '1/m'}} })
    g_actual: Optional[float] = Field(default=None, description="""Actual bend strength = 1/radius_actual""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:g_actual',
         'unit': {'ucum_code': '1/m'}} })
    h1: Optional[float] = Field(default=None, description="""Entrance end pole face curvature""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:h1', 'unit': {'ucum_code': '1/m'}} })
    h2: Optional[float] = Field(default=None, description="""Exit end pole face curvature""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:h2', 'unit': {'ucum_code': '1/m'}} })
    L_chord: Optional[float] = Field(default=None, description="""Chord length of the bend.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:L_chord', 'unit': {'ucum_code': 'm'}} })
    L_sagitta: Optional[float] = Field(default=None, description="""Output parameter. Sagitta length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:L_sagitta',
         'unit': {'ucum_code': 'm'}} })
    L_rectangle: Optional[float] = Field(default=None, description="""Rectangular length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:L_rectangle',
         'unit': {'ucum_code': 'm'}} })
    multipole_geometry: Optional[MultipoleGeometryEnum] = Field(default=None, description="""Multipole geometry type. Must be `follows_ref_geometry`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:multipole_geometry'} })
    ref_geometry: Optional[ReferenceGeometryEnum] = Field(default=None, description="""Reference geometry type. Must be `arc`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:ref_geometry'} })
    rho_ref: Optional[float] = Field(default=None, description="""Reference bend radius.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'], 'slot_uri': 'pals:rho_ref', 'unit': {'ucum_code': 'm'}} })
    tilt_ref: Optional[float] = Field(default=None, description="""Reference tilt of the bend.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendP'],
         'slot_uri': 'pals:tilt_ref',
         'unit': {'ucum_code': 'rad'}} })


class MultipoleComponent(ConfiguredBaseModel):
    """
    A single order's electric (or magnetic) multipole component.
    Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.
    Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
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

    order: int = Field(default=..., description="""Multipole order N (0 = dipole, 1 = quadrupole, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultipoleComponent']} })
    tilt: Optional[float] = Field(default=None, description="""Tilt of the Nth multipole.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:tilt'],
         'domain_of': ['MultipoleComponent'],
         'unit': {'ucum_code': 'rad'}} })
    En: Optional[float] = Field(default=None, description="""Normal component of the field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EnN'], 'domain_of': ['MultipoleComponent']} })
    Es: Optional[float] = Field(default=None, description="""Skew component of the field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EsN'], 'domain_of': ['MultipoleComponent']} })
    EnL: Optional[float] = Field(default=None, description="""Length-integrated normal component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EnNL'], 'domain_of': ['MultipoleComponent']} })
    EsL: Optional[float] = Field(default=None, description="""Length-integrated skew component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:EsNL'], 'domain_of': ['MultipoleComponent']} })
    Bn: Optional[float] = Field(default=None, description="""Normal component of the magnetic field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:BnN'], 'domain_of': ['MultipoleComponent']} })
    Bs: Optional[float] = Field(default=None, description="""Skew component of the magnetic field.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:BsN'], 'domain_of': ['MultipoleComponent']} })
    Kn: Optional[float] = Field(default=None, description="""Normalized normal component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:KnN'], 'domain_of': ['MultipoleComponent']} })
    Ks: Optional[float] = Field(default=None, description="""Normalized skew component.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['pals:KsN'], 'domain_of': ['MultipoleComponent']} })


class Component(MetaP):
    """
    A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['MetaP']})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class PhysicalComponent(Component, HasLongitudinalPlacement, FloorP):
    """
    A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['FloorP', 'HasLongitudinalPlacement']})

    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class VirtualComponent(Component, FloorP):
    """
    A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Element', 'pals:BookkeepingElement'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['FloorP']})

    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:virtual_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Beamline(VirtualComponent):
    """
    A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BeamLine'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    multipass: Optional[bool] = Field(default=None, description="""Indicates whether the beamline is a multipass beamline, where the beam passes through the same physical elements multiple times.
If not provided, the default assumption is that the beamline is single-pass.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline'], 'slot_uri': 'pals:multipass'} })
    length: Optional[float] = Field(default=None, description="""The total length of the beamline.
For pals interoperability, use m as the unit of length.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length'} })
    zero_point: Optional[str] = Field(default=None, description="""Name of a line item used as a reference point when the BeamLine is used as a subline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline']} })
    periodic: Optional[bool] = Field(default=None, description="""Indicates whether orbit and Twiss parameters periodic.
If not provided, the default assumption is that the beamline is not periodic.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline'], 'slot_uri': 'pals:periodic'} })
    repeat: Optional[int] = Field(default=None, description="""Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
If value is greater than 1, the beamline is repeated that many times.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline'], 'slot_uri': 'pals:repeat'} })
    direction: Optional[int] = Field(default=None, description="""Beam direction along the beamline: +1 or -1. 
Longitudinal orientation. Default is +1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline', 'ComponentRelation'], 'slot_uri': 'pals:direction'} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:virtual_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Signal(MetaP):
    """
    Semantic meaning of a control-system signal associated with a component.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['sosa:Sensor', 'sosa:Actuator'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['MetaP']})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    signal_role: SignalRoleEnum = Field(default=..., description="""The role of the signal in the control system, such as setpoint, readback, status, command, or limit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    source_system: SourceSystemEnum = Field(default=..., description="""The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    native_description: Optional[str] = Field(default=None, description="""A human-readable description of the signal in the source system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    canonical_signal_type: CanonicalSignalTypeEnum = Field(default=..., description="""The canonical semantic meaning of the signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    quantity_kind: QuantityKindEnum = Field(default=..., description="""The physical quantity kind of the signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    native_data_type: DataTypeEnum = Field(default=..., description="""The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    native_unit: UnitEnum = Field(default=..., description="""The native unit of the signal in the source system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    access_protocol: Optional[str] = Field(default=None, description="""The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    archive_identifier: Optional[str] = Field(default=None, description="""The identifier used to reference the signal in an archival system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Magnet(PhysicalComponent, TwissP, ReferenceP, BodyShiftP):
    """
    An accelerator device that produces a magnetic field for beam control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['pals:Element'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['ReferenceP', 'BodyShiftP', 'TwissP']})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Solenoid(Magnet, SolenoidP):
    """
    A magnet with a primarily longitudinal magnetic field used for focusing.
    A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. 
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Solenoid'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['SolenoidP']})

    Ksol: Optional[float] = Field(default=None, description="""Normalized solenoid strength.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidP'], 'slot_uri': 'pals:Ksol'} })
    Bsol: Optional[float] = Field(default=None, description="""Solenoid field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidP'],
         'slot_uri': 'pals:Bsol',
         'unit': {'ucum_code': 'T'}} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Multipole(Magnet, MagneticMultipoleP, ElectricMultipoleP):
    """
    A general magnet with a higher-order multipole field, such as a sextupole or octupole.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Multipole'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['ElectricMultipoleP', 'MagneticMultipoleP']})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Dipole(Multipole):
    """
    A magnet primarily used to bend the beam. 2 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Multipole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Bend(Multipole):
    """
    Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Bend'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Quadrupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 4 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Quadrupole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Octupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 8 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Octupole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Sextupole(Multipole):
    """
    A magnet primarily used to focus or defocus the beam. 6 poles.
    Only one of the electric or magnetic multipole components should be present, not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Sextupole'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Kicker(Magnet, MagneticMultipoleP, ElectricMultipoleP):
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
         'mixins': ['ElectricMultipoleP', 'MagneticMultipoleP']})

    plane: Optional[PlaneEnum] = Field(default=None, description="""The transverse plane in which the kicker operates, either horizontal or vertical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Kicker']} })
    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class ACKicker(Kicker):
    """
    An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:ACKicker'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    plane: Optional[PlaneEnum] = Field(default=None, description="""The transverse plane in which the kicker operates, either horizontal or vertical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Kicker']} })
    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class DiagnosticDevice(PhysicalComponent):
    """
    An accelerator device used to measure beam or machine state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class BeamPositionMonitor(DiagnosticDevice, TwissP, ReferenceP, BodyShiftP):
    """
    A diagnostic device used to measure transverse beam position.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['ReferenceP', 'BodyShiftP', 'TwissP']})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class RadiationMonitor(DiagnosticDevice, BodyShiftP):
    """
    A diagnostic device used to monitor radiation dose or dose rate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:Instrument'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['BodyShiftP']})

    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Cavity(PhysicalComponent, MagneticMultipoleP, ElectricMultipoleP, TwissP, ReferenceP, BodyShiftP):
    """
    A cavity used for beam acceleration or manipulation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['ReferenceP',
                    'ElectricMultipoleP',
                    'MagneticMultipoleP',
                    'BodyShiftP',
                    'TwissP']})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class CrabCavity(Cavity):
    """
    A cavity used for transverse beam manipulation, such as crabbing or deflecting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:CrabCavity'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class RFCavity(Cavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:RFCavity'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class SuperconductingRFCavity(RFCavity):
    """
    A cavity used for RF acceleration or longitudinal manipulation, which is superconducting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:RFCavity'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    species_ref: Optional[str] = Field(default=None, description="""A reference to a species or particle type, such as an ion, electron, or proton.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReferenceP'], 'slot_uri': 'pals:species_ref'} })
    pc_ref: Optional[float] = Field(default=None, description="""[momentum*c] Reference momentum times speed of light.""", json_schema_extra = { "linkml_meta": {'aliases': ['pCentral'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:pc_ref'} })
    E_tot_ref: Optional[float] = Field(default=None, description="""[eV] Reference total energy""", json_schema_extra = { "linkml_meta": {'aliases': ['ETotal'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:E_tot_ref',
         'unit': {'ucum_code': 'eV'}} })
    time_ref: Optional[float] = Field(default=None, description="""[s] Reference time""", json_schema_extra = { "linkml_meta": {'aliases': ['tRef'],
         'domain_of': ['ReferenceP'],
         'slot_uri': 'pals:time_ref',
         'unit': {'ucum_code': 's'}} })
    components: Optional[list[MultipoleComponent]] = Field(default=[], description="""Electric multipole components, one per order N.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectricMultipoleP', 'MagneticMultipoleP']} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    functions: list[PhysicalFunctionEnum] = Field(default=..., description="""The function of the physical component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:physical_function'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class SupportingFacilityComponent(PhysicalComponent, HasLongitudinalPlacement, BodyShiftP, FloorP):
    """
    A physical component that supports accelerator operation 
    without a specific beam-pipe placement, 
    such as a power supply, control rack, or radiation detector.
    These can include Girders, Racks, Power Supplies, 
    and other physical infrastructure components that are important for understanding 
    the structure and function of the accelerator system but are not inline with the beamline.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:StructuralElement'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['FloorP', 'HasLongitudinalPlacement', 'BodyShiftP']})

    functions: list[FacilityFunctionEnum] = Field(default=..., description="""The function of the supporting facility component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:supporting_facility_function'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    length: Optional[float] = Field(default=None, description="""Length of the element (arc length for bends).""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement', 'Beamline'],
         'slot_uri': 'pals:length',
         'unit': {'ucum_code': 'm'}} })
    s_position: Optional[float] = Field(default=None, description="""Longitudinal position of the element along the beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasLongitudinalPlacement'],
         'slot_uri': 'pals:s_position',
         'unit': {'ucum_code': 'm'}} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    beamline_relation: PhysicalRelationEnum = Field(default=..., description="""The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:physical_beamline_relation'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class BookkeepingComponent(VirtualComponent, BodyShiftP):
    """
    A virtual component that represents a bookkeeping or organizational role in the accelerator system, 
    such as a BeamlineSection, Marker or a Fork.
    These can include BeamlineSections, Markers, Forks, 
    and other virtual components that are important for understanding 
    the structure and function of the accelerator system but are not physical devices.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['pals:BookkeepingElement'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['BodyShiftP']})

    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:virtual_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class Marker(BookkeepingComponent, TwissP):
    """
    A virtual component used as a reference point or marker in the beamline structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:Marker'],
         'from_schema': 'https://w3id.org/accelerator-core',
         'mixins': ['TwissP']})

    alpha_a: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_x', 'alphax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_a'} })
    alpha_b: Optional[float] = Field(default=None, description="""Twiss alpha parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['alpha_y', 'alphay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:alpha_b'} })
    beta_a: Optional[float] = Field(default=None, description="""Twiss beta parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_x', 'betax'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_a'} })
    beta_b: Optional[float] = Field(default=None, description="""Twiss beta parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['beta_y', 'betay'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:beta_b'} })
    eta_x: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etax'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_x'} })
    eta_y: Optional[float] = Field(default=None, description="""Twiss dispersion parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etay'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:eta_y'} })
    etap_x: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapx'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_x'} })
    etap_y: Optional[float] = Field(default=None, description="""Twiss dispersion slope parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['etapy'], 'domain_of': ['TwissP'], 'slot_uri': 'pals:etap_y'} })
    phi_a: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the horizontal plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_x', 'phix', 'psi_x', 'psix'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_a'} })
    phi_b: Optional[float] = Field(default=None, description="""Twiss phase advance parameter in the vertical plane.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_y', 'phiy', 'psi_y', 'psiy'],
         'domain_of': ['TwissP'],
         'slot_uri': 'pals:phi_b'} })
    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:virtual_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class BeamlineSection(BookkeepingComponent):
    """
    A virtual component used to represent a section of the beamline for organizational 
    or functional grouping of components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['pals:BeamlineSection'],
         'from_schema': 'https://w3id.org/accelerator-core'})

    x_offset: Optional[float] = Field(default=None, description="""Shift in the X direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_x', 'x_shift', 'GlobalOffsetX'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_offset'} })
    y_offset: Optional[float] = Field(default=None, description="""Shift in the Y direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_y', 'y_shift', 'GlobalOffsetY'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_offset'} })
    z_offset: Optional[float] = Field(default=None, description="""Shift in the Z direction in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_z', 'z_shift', 'GlobalOffsetZ'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_offset'} })
    x_rot: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_phi', 'phi_shift', 'GlobalOffsetPhi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:x_rot'} })
    y_rot: Optional[float] = Field(default=None, description="""Rotation around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_theta', 'theta_shift', 'GlobalOffsetTheta'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:y_rot'} })
    z_rot: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['delta_psi', 'psi_shift', 'GlobalOffsetPsi'],
         'domain_of': ['BodyShiftP'],
         'slot_uri': 'pals:z_rot'} })
    functions: list[VirtualFunctionEnum] = Field(default=..., description="""The function of the virtual component,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent',
                       'VirtualComponent',
                       'SupportingFacilityComponent'],
         'slot_uri': 'narad:virtual_function'} })
    beamline_relation: VirtualRelationEnum = Field(default=..., description="""The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalComponent', 'VirtualComponent'],
         'slot_uri': 'narad:virtual_beamline_relation'} })
    x: Optional[float] = Field(default=None, description="""Global X coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['x_coordinate', 'ModelX', 'x coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:x'} })
    y: Optional[float] = Field(default=None, description="""Global Y coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['y_coordinate', 'ModelY', 'y coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:y'} })
    z: Optional[float] = Field(default=None, description="""Global Z coordinate in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['z_coordinate', 'ModelZ', 'z coordinate'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:z'} })
    theta: Optional[float] = Field(default=None, description="""Orientation angle around the Y-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['theta_angle', 'ModelYaw', 'Model_Yaw'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:theta'} })
    phi: Optional[float] = Field(default=None, description="""Rotation around the X-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['phi_angle', 'ModelPitch', 'Model_Pitch'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:phi'} })
    psi: Optional[float] = Field(default=None, description="""Rotation around the Z-axis in the facility floor plan.""", json_schema_extra = { "linkml_meta": {'aliases': ['psi_angle', 'Model_Roll', 'Rotation'],
         'domain_of': ['FloorP'],
         'slot_uri': 'pals:psi'} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    type: str = Field(default=..., description="""The LinkML class name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'Component', 'Signal'], 'slot_uri': 'narad:type'} })
    native_types: Optional[list[str]] = Field(default=[], description="""The native type of the component in the source system, which can be used to identify the component across different source systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    description: Optional[str] = Field(default=None, description="""Human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NARAD', 'MetaP'], 'slot_uri': 'pals:description'} })
    label: Optional[str] = Field(default=None, description="""A label string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:label'} })
    alias: Optional[str] = Field(default=None, description="""An alternative name or identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP'], 'slot_uri': 'pals:alias'} })
    additional_metadata: Optional[list[MetadataEntry]] = Field(default=[], description="""Additional metadata or annotations for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetaP']} })


class MetadataEntry(ConfiguredBaseModel):
    """
    A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core'})

    key: str = Field(default=..., description="""The metadata field name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetadataEntry']} })
    value: str = Field(default=..., description="""The metadata value, serialized as a string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetadataEntry']} })
    datatype: Optional[DataTypeEnum] = Field(default=None, description="""Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetadataEntry']} })


class Relationship(ConfiguredBaseModel):
    """
    Abstract base for subject-predicate-object associations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/accelerator-core',
         'represents_relationship': True})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'SUBJECT',
         'slot_uri': 'rdf:subject'} })
    predicate: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'PREDICATE',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdf:object'} })


class SignalBinding(Relationship):
    """
    Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'object': {'name': 'object', 'range': 'Signal'},
                        'predicate': {'name': 'predicate',
                                      'range': 'SignalBindingPredicateEnum'},
                        'subject': {'name': 'subject', 'range': 'PhysicalComponent'}}})

    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'SUBJECT',
         'slot_uri': 'rdf:subject'} })
    predicate: SignalBindingPredicateEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'PREDICATE',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdf:object'} })


class ComponentRelation(Relationship):
    """
    Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/accelerator-core',
         'slot_usage': {'object': {'name': 'object', 'range': 'Component'},
                        'predicate': {'name': 'predicate',
                                      'range': 'ComponentRelationPredicateEnum'},
                        'subject': {'name': 'subject', 'range': 'Component'}}})

    context: Optional[RelationContextEnum] = Field(default=None, description="""The frame of reference / domain in which this relationship is asserted to hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    beamline_context: Optional[str] = Field(default=None, description="""The specific Beamline this relationship is defined with respect to (relevant when context=beamline_order).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    reference_frame: Optional[ReferenceFrameEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    distance_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    distance_unit: Optional[UnitEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    axis: Optional[AxisEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    direction: Optional[DirectionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline', 'ComponentRelation']} })
    tolerance_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    tolerance_unit: Optional[UnitEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentRelation']} })
    id: str = Field(default=..., description="""A unique identifier for the instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Signal', 'Relationship'], 'slot_uri': 'narad:id'} })
    subject: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'SUBJECT',
         'slot_uri': 'rdf:subject'} })
    predicate: ComponentRelationPredicateEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'PREDICATE',
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdf:object'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NARAD.model_rebuild()
MetaP.model_rebuild()
FloorP.model_rebuild()
BodyShiftP.model_rebuild()
HasLongitudinalPlacement.model_rebuild()
ReferenceP.model_rebuild()
SolenoidP.model_rebuild()
TwissP.model_rebuild()
ElectricMultipoleP.model_rebuild()
MagneticMultipoleP.model_rebuild()
BendP.model_rebuild()
MultipoleComponent.model_rebuild()
Component.model_rebuild()
PhysicalComponent.model_rebuild()
VirtualComponent.model_rebuild()
Beamline.model_rebuild()
Signal.model_rebuild()
Magnet.model_rebuild()
Solenoid.model_rebuild()
Multipole.model_rebuild()
Dipole.model_rebuild()
Bend.model_rebuild()
Quadrupole.model_rebuild()
Octupole.model_rebuild()
Sextupole.model_rebuild()
Kicker.model_rebuild()
ACKicker.model_rebuild()
DiagnosticDevice.model_rebuild()
BeamPositionMonitor.model_rebuild()
RadiationMonitor.model_rebuild()
Cavity.model_rebuild()
CrabCavity.model_rebuild()
RFCavity.model_rebuild()
SuperconductingRFCavity.model_rebuild()
SupportingFacilityComponent.model_rebuild()
BookkeepingComponent.model_rebuild()
Marker.model_rebuild()
BeamlineSection.model_rebuild()
MetadataEntry.model_rebuild()
Relationship.model_rebuild()
SignalBinding.model_rebuild()
ComponentRelation.model_rebuild()
