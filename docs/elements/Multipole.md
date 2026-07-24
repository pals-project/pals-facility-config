

# Class: Multipole 


_A general magnet with a higher-order multipole field, such as a sextupole or octupole._

_Only one of the electric or magnetic multipole components should be present, not both._





URI: [pals:Multipole](https://pals-project.readthedocs.io/Multipole)





```mermaid
 classDiagram
    class Multipole
    click Multipole href "../Multipole/"
      HasElectricMultipoleP <|-- Multipole
        click HasElectricMultipoleP href "../HasElectricMultipoleP/"
      HasMagneticMultipoleP <|-- Multipole
        click HasMagneticMultipoleP href "../HasMagneticMultipoleP/"
      Magnet <|-- Multipole
        click Magnet href "../Magnet/"
      

      Multipole <|-- Bend
        click Bend href "../Bend/"
      Multipole <|-- Quadrupole
        click Quadrupole href "../Quadrupole/"
      Multipole <|-- Octupole
        click Octupole href "../Octupole/"
      Multipole <|-- Sextupole
        click Sextupole href "../Sextupole/"
      

      Multipole : beamline_relation
        
          
    
        
        
        Multipole --> "1" PhysicalRelationEnum : beamline_relation
        click PhysicalRelationEnum href "../PhysicalRelationEnum/"
    

        
      Multipole : BodyShiftP
        
          
    
        
        
        Multipole --> "0..1" BodyShiftParamGroup : BodyShiftP
        click BodyShiftParamGroup href "../BodyShiftParamGroup/"
    

        
      Multipole : ElectricMultipoleP
        
          
    
        
        
        Multipole --> "0..1" ElectricMultipoleParamGroup : ElectricMultipoleP
        click ElectricMultipoleParamGroup href "../ElectricMultipoleParamGroup/"
    

        
      Multipole : FloorP
        
          
    
        
        
        Multipole --> "0..1" FloorParamGroup : FloorP
        click FloorParamGroup href "../FloorParamGroup/"
    

        
      Multipole : functions
        
          
    
        
        
        Multipole --> "1..*" PhysicalFunctionEnum : functions
        click PhysicalFunctionEnum href "../PhysicalFunctionEnum/"
    

        
      Multipole : id
        
      Multipole : kind
        
      Multipole : LongitudinalPlacementP
        
          
    
        
        
        Multipole --> "0..1" LongitudinalPlacementParamGroup : LongitudinalPlacementP
        click LongitudinalPlacementParamGroup href "../LongitudinalPlacementParamGroup/"
    

        
      Multipole : MagneticMultipoleP
        
          
    
        
        
        Multipole --> "0..1" MagneticMultipoleParamGroup : MagneticMultipoleP
        click MagneticMultipoleParamGroup href "../MagneticMultipoleParamGroup/"
    

        
      Multipole : MetaP
        
          
    
        
        
        Multipole --> "0..1" MetaParamGroup : MetaP
        click MetaParamGroup href "../MetaParamGroup/"
    

        
      Multipole : native_types
        
      Multipole : ReferenceP
        
          
    
        
        
        Multipole --> "0..1" ReferenceParamGroup : ReferenceP
        click ReferenceParamGroup href "../ReferenceParamGroup/"
    

        
      Multipole : TwissP
        
          
    
        
        
        Multipole --> "0..1" TwissParamGroup : TwissP
        click TwissParamGroup href "../TwissParamGroup/"
    

        
      
```





## Inheritance
* [Component](Component.md) [ [HasMetaP](HasMetaP.md)]
    * [PhysicalComponent](PhysicalComponent.md) [ [HasFloorP](HasFloorP.md) [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md)]
        * [Magnet](Magnet.md) [ [HasReferenceP](HasReferenceP.md) [HasBodyShiftP](HasBodyShiftP.md) [HasTwissP](HasTwissP.md)]
            * **Multipole** [ [HasElectricMultipoleP](HasElectricMultipoleP.md) [HasMagneticMultipoleP](HasMagneticMultipoleP.md)]
                * [Bend](Bend.md) [ [HasBendP](HasBendP.md)]
                * [Quadrupole](Quadrupole.md)
                * [Octupole](Octupole.md)
                * [Sextupole](Sextupole.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ElectricMultipoleP](ElectricMultipoleP.md) | 0..1 <br/> [ElectricMultipoleParamGroup](ElectricMultipoleParamGroup.md) | A mixin for electric multipole parameters that are aligned with PALS Electric... | [HasElectricMultipoleP](HasElectricMultipoleP.md) |
| [MagneticMultipoleP](MagneticMultipoleP.md) | 0..1 <br/> [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md) | A mixin for magnetic multipole parameters that are aligned with PALS Magnetic... | [HasMagneticMultipoleP](HasMagneticMultipoleP.md) |
| [ReferenceP](ReferenceP.md) | 0..1 <br/> [ReferenceParamGroup](ReferenceParamGroup.md) | A mixin for reference parameters that are aligned with PALS ReferenceP (Refer... | [HasReferenceP](HasReferenceP.md) |
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
| self | pals:Multipole |
| native | pals:Multipole |
| broad | pals:Multipole |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Multipole
description: 'A general magnet with a higher-order multipole field, such as a sextupole
  or octupole.

  Only one of the electric or magnetic multipole components should be present, not
  both.'
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:Multipole
is_a: Magnet
mixins:
- HasElectricMultipoleP
- HasMagneticMultipoleP

```
</details>

### Induced

<details>
```yaml
name: Multipole
description: 'A general magnet with a higher-order multipole field, such as a sextupole
  or octupole.

  Only one of the electric or magnetic multipole components should be present, not
  both.'
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:Multipole
is_a: Magnet
mixins:
- HasElectricMultipoleP
- HasMagneticMultipoleP
attributes:
  ElectricMultipoleP:
    name: ElectricMultipoleP
    description: A mixin for electric multipole parameters that are aligned with PALS
      ElectricMultipoleP (Electric Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: ElectricMultipoleP
    owner: Multipole
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
    owner: Multipole
    domain_of:
    - HasMagneticMultipoleP
    range: MagneticMultipoleParamGroup
    inlined: true
  ReferenceP:
    name: ReferenceP
    description: A mixin for reference parameters that are aligned with PALS ReferenceP
      (Reference Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: ReferenceP
    owner: Multipole
    domain_of:
    - HasReferenceP
    range: ReferenceParamGroup
    inlined: true
  BodyShiftP:
    name: BodyShiftP
    description: A mixin for floor plan shift parameters that are aligned with PALS
      BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle
      Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: BodyShiftP
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
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
    owner: Multipole
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>