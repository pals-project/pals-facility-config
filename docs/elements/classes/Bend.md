

# Class: Bend 


_Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight._





URI: [pals_config:class/Bend](https://w3id.org/pals-config/class/Bend)


```mermaid
erDiagram
AdditionalMetadata {
    DataTypeEnum datatype  
    string key  
    string value  
}
Bend {
    string id  
    stringList alias  
    PhysicalRelationEnum beamline_relation  
    PhysicalFunctionEnumList functions  
    string kind  
    stringList native_types  
}
BendParamGroup {
    float Bn0_ref  
    boolean Kn0_from_g_ref  
    float L_chord  
    float L_rectangle  
    float L_sagitta  
    float angle_ref  
    float bend_field_actual  
    float e1  
    float e1_rect  
    float e2  
    float e2_rect  
    float edge1_int  
    float edge2_int  
    float g_actual  
    float g_ref  
    float h1  
    float h2  
    MultipoleGeometryEnum multipole_geometry  
    float radius_ref  
    ReferenceGeometryEnum ref_geometry  
    float tilt_ref  
    string id  
}
BodyShiftParamGroup {
    float x_offset  
    float x_rot  
    float y_offset  
    float y_rot  
    float z_offset  
    float z_rot  
    string id  
}
ElectricMultipoleParamGroup {
    string id  
}
FloorParamGroup {
    float phi  
    float psi  
    float theta  
    float x  
    float y  
    float z  
    string id  
}
LongitudinalPlacementParamGroup {
    float length  
    float s_position  
    string id  
}
MagneticMultipoleParamGroup {
    string id  
}
MetaParamGroup {
    string description  
    stringList alias  
    string label  
    string id  
}
MultipoleParameterGroup {
    float Bn  
    float BnL  
    float Bs  
    float BsL  
    float En  
    float EnL  
    float Es  
    float EsL  
    float Kn  
    float KnL  
    float Ks  
    float KsL  
    integer order  
    float tilt  
}
ReferenceParamGroup {
    float E_tot_ref  
    float pc_ref  
    string species_ref  
    float time_ref  
    string id  
}
TwissParamGroup {
    float alpha_a  
    float alpha_b  
    float beta_a  
    float beta_b  
    float cmat11  
    float cmat12  
    float cmat21  
    float cmat22  
    float dalpha_a_dpz  
    float dalpha_b_dpz  
    float dbeta_a_dpz  
    float dbeta_b_dpz  
    float deta_x_dpz  
    float deta_x_ds  
    float deta_y_dpz  
    float deta_y_ds  
    float detap_x_dpz  
    float detap_y_dpz  
    float eta_x  
    float eta_y  
    float etap_x  
    float etap_y  
    float phi_a  
    float phi_b  
    string id  
}

Bend ||--|o BendParamGroup : "BendP"
Bend ||--|o BodyShiftParamGroup : "BodyShiftP"
Bend ||--|o ElectricMultipoleParamGroup : "ElectricMultipoleP"
Bend ||--|o FloorParamGroup : "FloorP"
Bend ||--|o LongitudinalPlacementParamGroup : "LongitudinalPlacementP"
Bend ||--|o MagneticMultipoleParamGroup : "MagneticMultipoleP"
Bend ||--|o MetaParamGroup : "MetaP"
Bend ||--|o ReferenceParamGroup : "ReferenceP"
Bend ||--|o TwissParamGroup : "TwissP"
ElectricMultipoleParamGroup ||--}o MultipoleParameterGroup : "elec_components"
MagneticMultipoleParamGroup ||--}o MultipoleParameterGroup : "mag_components"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"

```




## Inheritance
* [Node](../classes/Node.md)
    * [Component](../classes/Component.md) [ [HasMetaP](../classes/HasMetaP.md)]
        * [PhysicalComponent](../classes/PhysicalComponent.md) [ [HasFloorP](../classes/HasFloorP.md) [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md)]
            * [Magnet](../classes/Magnet.md) [ [HasReferenceP](../classes/HasReferenceP.md) [HasBodyShiftP](../classes/HasBodyShiftP.md) [HasTwissP](../classes/HasTwissP.md)]
                * [Multipole](../classes/Multipole.md) [ [HasElectricMultipoleP](../classes/HasElectricMultipoleP.md) [HasMagneticMultipoleP](../classes/HasMagneticMultipoleP.md)]
                    * **Bend** [ [HasBendP](../classes/HasBendP.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [BendP](../slots/BendP.md) | 0..1 <br/> [BendParamGroup](../classes/BendParamGroup.md) | A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasBendP](../classes/HasBendP.md) |
| [ElectricMultipoleP](../slots/ElectricMultipoleP.md) | 0..1 <br/> [ElectricMultipoleParamGroup](../classes/ElectricMultipoleParamGroup.md) | A mixin for electric multipole parameters that are aligned with PALS ElectricMultipoleP (Electric Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasElectricMultipoleP](../classes/HasElectricMultipoleP.md) |
| [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | 0..1 <br/> [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) | A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasMagneticMultipoleP](../classes/HasMagneticMultipoleP.md) |
| [ReferenceP](../slots/ReferenceP.md) | 0..1 <br/> [ReferenceParamGroup](../classes/ReferenceParamGroup.md) | A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasReferenceP](../classes/HasReferenceP.md) |
| [BodyShiftP](../slots/BodyShiftP.md) | 0..1 <br/> [BodyShiftParamGroup](../classes/BodyShiftParamGroup.md) | A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasBodyShiftP](../classes/HasBodyShiftP.md) |
| [TwissP](../slots/TwissP.md) | 0..1 <br/> [TwissParamGroup](../classes/TwissParamGroup.md) | A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasTwissP](../classes/HasTwissP.md) |
| [functions](../slots/functions.md) | * <br/> [PhysicalFunctionEnum](../enums/PhysicalFunctionEnum.md) | The function of the physical component,  which can be used to identify the component across different source systems. | [PhysicalComponent](../classes/PhysicalComponent.md) |
| [beamline_relation](../slots/beamline_relation.md) | 1 <br/> [PhysicalRelationEnum](../enums/PhysicalRelationEnum.md) | The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems. | [PhysicalComponent](../classes/PhysicalComponent.md) |
| [FloorP](../slots/FloorP.md) | 0..1 <br/> [FloorParamGroup](../classes/FloorParamGroup.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasFloorP](../classes/HasFloorP.md) |
| [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | 0..1 <br/> [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) | A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md) |
| [native_types](../slots/native_types.md) | * <br/> [String](../types/String.md) | The native type of the component in the source system, which can be used to identify the component across different source systems. | [Component](../classes/Component.md) |
| [MetaP](../slots/MetaP.md) | 0..1 <br/> [MetaParamGroup](../classes/MetaParamGroup.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasMetaP](../classes/HasMetaP.md) |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [Node](../classes/Node.md) |
| [kind](../slots/kind.md) | 1 <br/> [String](../types/String.md) | The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor` (no prefix). | [Node](../classes/Node.md) |
| [alias](../slots/alias.md) | * <br/> [String](../types/String.md) | An alternative name or identifier for the instance. | [Node](../classes/Node.md) |












## Aliases


* Dipole




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Bend |
| native | pals_config:Bend |
| exact | pals:Bend |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bend
description: Dipole magnet used to bend the beam. 2 poles. The major difference between
  this element and other physical elements is that with a Bend  the curvilinear coordinate
  system is an arc with finite curvature  and for the other elements the curvilinear
  coordinate system is straight.
from_schema: https://w3id.org/pals-config
aliases:
- Dipole
exact_mappings:
- pals:Bend
is_a: Multipole
mixins:
- HasBendP

```
</details>

### Induced

<details>
```yaml
name: Bend
description: Dipole magnet used to bend the beam. 2 poles. The major difference between
  this element and other physical elements is that with a Bend  the curvilinear coordinate
  system is an arc with finite curvature  and for the other elements the curvilinear
  coordinate system is straight.
from_schema: https://w3id.org/pals-config
aliases:
- Dipole
exact_mappings:
- pals:Bend
is_a: Multipole
mixins:
- HasBendP
attributes:
  BendP:
    name: BendP
    description: A mixin for bend parameters that are aligned with PALS BendP (Bend
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: BendP
    owner: Bend
    domain_of:
    - HasBendP
    range: BendParamGroup
    inlined: true
  ElectricMultipoleP:
    name: ElectricMultipoleP
    description: A mixin for electric multipole parameters that are aligned with PALS
      ElectricMultipoleP (Electric Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: ElectricMultipoleP
    owner: Bend
    domain_of:
    - HasElectricMultipoleP
    range: ElectricMultipoleParamGroup
    inlined: true
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: A mixin for magnetic multipole parameters that are aligned with PALS
      MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: MagneticMultipoleP
    owner: Bend
    domain_of:
    - HasMagneticMultipoleP
    range: MagneticMultipoleParamGroup
    inlined: true
  ReferenceP:
    name: ReferenceP
    description: A mixin for reference parameters that are aligned with PALS ReferenceP
      (Reference Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: ReferenceP
    owner: Bend
    domain_of:
    - HasReferenceP
    range: ReferenceParamGroup
    inlined: true
  BodyShiftP:
    name: BodyShiftP
    description: A mixin for floor plan shift parameters that are aligned with PALS
      BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle
      Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: BodyShiftP
    owner: Bend
    domain_of:
    - HasBodyShiftP
    range: BodyShiftParamGroup
    inlined: true
  TwissP:
    name: TwissP
    description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: TwissP
    owner: Bend
    domain_of:
    - HasTwissP
    range: TwissParamGroup
    inlined: true
  functions:
    name: functions
    description: The function of the physical component,  which can be used to identify
      the component across different source systems.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:physical_function
    rank: 1000
    alias: functions
    owner: Bend
    domain_of:
    - PhysicalComponent
    - VirtualComponent
    range: PhysicalFunctionEnum
    required: false
    multivalued: true
  beamline_relation:
    name: beamline_relation
    description: The relationship of the physical component to the beamline,  which
      can be used to identify the component across different source systems.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:physical_beamline_relation
    rank: 1000
    alias: beamline_relation
    owner: Bend
    domain_of:
    - PhysicalComponent
    - VirtualComponent
    range: PhysicalRelationEnum
    required: true
  FloorP:
    name: FloorP
    description: A mixin for floor plan parameters that are aligned with PALS FloorP
      (Floor Plan Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: FloorP
    owner: Bend
    domain_of:
    - HasFloorP
    range: FloorParamGroup
    inlined: true
  LongitudinalPlacementP:
    name: LongitudinalPlacementP
    description: A mixin for an element's extent and position along the longitudinal
      (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP
      (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator
      Language Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: LongitudinalPlacementP
    owner: Bend
    domain_of:
    - HasLongitudinalPlacementP
    range: LongitudinalPlacementParamGroup
    inlined: true
  native_types:
    name: native_types
    description: The native type of the component in the source system, which can
      be used to identify the component across different source systems.
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: native_types
    owner: Bend
    domain_of:
    - Component
    range: string
    multivalued: true
  MetaP:
    name: MetaP
    description: A mixin for metadata parameters that are aligned with PALS MetaP
      (Metadata Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: MetaP
    owner: Bend
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: Bend
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true
  kind:
    name: kind
    description: The LinkML class name of this instance, e.g. `Quadrupole` or `BeamProfileMonitor`
      (no prefix).
    from_schema: https://w3id.org/pals-config
    related_mappings:
    - saref:DeviceKind
    rank: 1000
    slot_uri: rdf:type
    designates_type: true
    alias: kind
    owner: Bend
    domain_of:
    - Node
    - PALSAccelerator
    range: string
    required: true
  alias:
    name: alias
    description: An alternative name or identifier for the instance.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:alias
    rank: 1000
    alias: alias
    owner: Bend
    domain_of:
    - Node
    - MetaParamGroup
    range: string
    multivalued: true

```
</details>