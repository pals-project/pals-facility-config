

# Class: CrabCavity 


_A cavity used for transverse beam manipulation, such as crabbing or deflecting._





URI: [pals:CrabCavity](https://pals-project.readthedocs.io/CrabCavity)





```mermaid
 classDiagram
    class CrabCavity
    click CrabCavity href "../CrabCavity/"
      Cavity <|-- CrabCavity
        click Cavity href "../Cavity/"
      
      CrabCavity : beamline_relation
        
          
    
        
        
        CrabCavity --> "1" PhysicalRelationEnum : beamline_relation
        click PhysicalRelationEnum href "../PhysicalRelationEnum/"
    

        
      CrabCavity : BodyShiftP
        
          
    
        
        
        CrabCavity --> "0..1" BodyShiftParamGroup : BodyShiftP
        click BodyShiftParamGroup href "../BodyShiftParamGroup/"
    

        
      CrabCavity : ElectricMultipoleP
        
          
    
        
        
        CrabCavity --> "0..1" ElectricMultipoleParamGroup : ElectricMultipoleP
        click ElectricMultipoleParamGroup href "../ElectricMultipoleParamGroup/"
    

        
      CrabCavity : FloorP
        
          
    
        
        
        CrabCavity --> "0..1" FloorParamGroup : FloorP
        click FloorParamGroup href "../FloorParamGroup/"
    

        
      CrabCavity : functions
        
          
    
        
        
        CrabCavity --> "1..*" PhysicalFunctionEnum : functions
        click PhysicalFunctionEnum href "../PhysicalFunctionEnum/"
    

        
      CrabCavity : id
        
      CrabCavity : kind
        
      CrabCavity : LongitudinalPlacementP
        
          
    
        
        
        CrabCavity --> "0..1" LongitudinalPlacementParamGroup : LongitudinalPlacementP
        click LongitudinalPlacementParamGroup href "../LongitudinalPlacementParamGroup/"
    

        
      CrabCavity : MagneticMultipoleP
        
          
    
        
        
        CrabCavity --> "0..1" MagneticMultipoleParamGroup : MagneticMultipoleP
        click MagneticMultipoleParamGroup href "../MagneticMultipoleParamGroup/"
    

        
      CrabCavity : MetaP
        
          
    
        
        
        CrabCavity --> "0..1" MetaParamGroup : MetaP
        click MetaParamGroup href "../MetaParamGroup/"
    

        
      CrabCavity : native_types
        
      CrabCavity : ReferenceP
        
          
    
        
        
        CrabCavity --> "0..1" ReferenceParamGroup : ReferenceP
        click ReferenceParamGroup href "../ReferenceParamGroup/"
    

        
      CrabCavity : TwissP
        
          
    
        
        
        CrabCavity --> "0..1" TwissParamGroup : TwissP
        click TwissParamGroup href "../TwissParamGroup/"
    

        
      
```





## Inheritance
* [Component](Component.md) [ [HasMetaP](HasMetaP.md)]
    * [PhysicalComponent](PhysicalComponent.md) [ [HasFloorP](HasFloorP.md) [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md)]
        * [Cavity](Cavity.md) [ [HasReferenceP](HasReferenceP.md) [HasElectricMultipoleP](HasElectricMultipoleP.md) [HasMagneticMultipoleP](HasMagneticMultipoleP.md) [HasBodyShiftP](HasBodyShiftP.md) [HasTwissP](HasTwissP.md)]
            * **CrabCavity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ReferenceP](ReferenceP.md) | 0..1 <br/> [ReferenceParamGroup](ReferenceParamGroup.md) | A mixin for reference parameters that are aligned with PALS ReferenceP (Refer... | [HasReferenceP](HasReferenceP.md) |
| [ElectricMultipoleP](ElectricMultipoleP.md) | 0..1 <br/> [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md) | A mixin for electric multipole parameters that are aligned with PALS Electric... | [HasElectricMultipoleP](HasElectricMultipoleP.md) |
| [MagneticMultipoleP](MagneticMultipoleP.md) | 0..1 <br/> [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md) | A mixin for magnetic multipole parameters that are aligned with PALS Magnetic... | [HasMagneticMultipoleP](HasMagneticMultipoleP.md) |
| [BodyShiftP](BodyShiftP.md) | 0..1 <br/> [BodyShiftParamGroup](BodyShiftParamGroup.md) | A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP... | [HasBodyShiftP](HasBodyShiftP.md) |
| [TwissP](TwissP.md) | 0..1 <br/> [TwissParamGroup](TwissParamGroup.md) | A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Paramet... | [HasTwissP](HasTwissP.md) |
| [functions](functions.md) | 1..* <br/> [PhysicalFunctionEnum](PhysicalFunctionEnum.md) | The function of the physical component,  which can be used to identify the co... | [PhysicalComponent](PhysicalComponent.md) |
| [beamline_relation](beamline_relation.md) | 1 <br/> [PhysicalRelationEnum](PhysicalRelationEnum.md) | The relationship of the physical component to the beamline,  which can be use... | [PhysicalComponent](PhysicalComponent.md) |
| [FloorP](FloorP.md) | 0..1 <br/> [FloorParamGroup](FloorParamGroup.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Pl... | [HasFloorP](HasFloorP.md) |
| [LongitudinalPlacementP](LongitudinalPlacementP.md) | 0..1 <br/> [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md) | A mixin for an element's extent and position along the longitudinal (beam-dir... | [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md) |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the instance | [Component](Component.md) |
| [kind](kind.md) | 1 <br/> [String](String.md) | The LinkML class name of this instance | [Component](Component.md) |
| [native_types](native_types.md) | * <br/> [String](String.md) | The native type of the component in the source system, which can be used to i... | [Component](Component.md) |
| [MetaP](MetaP.md) | 0..1 <br/> [MetaParamGroup](MetaParamGroup.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Pa... | [HasMetaP](HasMetaP.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:CrabCavity |
| native | pals:CrabCavity |
| exact | pals:CrabCavity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrabCavity
description: A cavity used for transverse beam manipulation, such as crabbing or deflecting.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:CrabCavity
is_a: Cavity

```
</details>

### Induced

<details>
```yaml
name: CrabCavity
description: A cavity used for transverse beam manipulation, such as crabbing or deflecting.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:CrabCavity
is_a: Cavity
attributes:
  ReferenceP:
    name: ReferenceP
    description: A mixin for reference parameters that are aligned with PALS ReferenceP
      (Reference Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: ReferenceP
    owner: CrabCavity
    domain_of:
    - HasReferenceP
    range: ReferenceParamGroup
    inlined: true
  ElectricMultipoleP:
    name: ElectricMultipoleP
    description: A mixin for electric multipole parameters that are aligned with PALS
      ElectricMultipoleP (Electric Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: ElectricMultipoleP
    owner: CrabCavity
    domain_of:
    - HasElectricMultipoleP
    range: ElectricMultipoleParamGroup
    inlined: true
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: A mixin for magnetic multipole parameters that are aligned with PALS
      MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: MagneticMultipoleP
    owner: CrabCavity
    domain_of:
    - HasMagneticMultipoleP
    range: MagneticMultipoleParamGroup
    inlined: true
  BodyShiftP:
    name: BodyShiftP
    description: A mixin for floor plan shift parameters that are aligned with PALS
      BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle
      Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: BodyShiftP
    owner: CrabCavity
    domain_of:
    - HasBodyShiftP
    range: BodyShiftParamGroup
    inlined: true
  TwissP:
    name: TwissP
    description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: TwissP
    owner: CrabCavity
    domain_of:
    - HasTwissP
    range: TwissParamGroup
    inlined: true
  functions:
    name: functions
    description: The function of the physical component,  which can be used to identify
      the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:physical_function
    alias: functions
    owner: CrabCavity
    domain_of:
    - PhysicalComponent
    - VirtualComponent
    - SupportingFacilityComponent
    range: PhysicalFunctionEnum
    required: true
    multivalued: true
  beamline_relation:
    name: beamline_relation
    description: The relationship of the physical component to the beamline,  which
      can be used to identify the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:physical_beamline_relation
    alias: beamline_relation
    owner: CrabCavity
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
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: FloorP
    owner: CrabCavity
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
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: LongitudinalPlacementP
    owner: CrabCavity
    domain_of:
    - HasLongitudinalPlacementP
    range: LongitudinalPlacementParamGroup
    inlined: true
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:id
    identifier: true
    alias: id
    owner: CrabCavity
    domain_of:
    - Affiliation
    - Component
    - Signal
    - Relationship
    range: string
    required: true
  kind:
    name: kind
    description: The LinkML class name of this instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:kind
    alias: kind
    owner: CrabCavity
    domain_of:
    - PALS
    - Component
    - Signal
    range: string
    required: true
  native_types:
    name: native_types
    description: The native type of the component in the source system, which can
      be used to identify the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: native_types
    owner: CrabCavity
    domain_of:
    - Component
    range: string
    multivalued: true
  MetaP:
    name: MetaP
    description: A mixin for metadata parameters that are aligned with PALS MetaP
      (Metadata Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: MetaP
    owner: CrabCavity
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>