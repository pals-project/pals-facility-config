

# Class: BeamLineSection 


_A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components._





URI: [pals:BeamLineSection](https://pals-project.readthedocs.io/BeamLineSection)





```mermaid
 classDiagram
    class BeamLineSection
    click BeamLineSection href "../BeamLineSection/"
      HasFloorP <|-- BeamLineSection
        click HasFloorP href "../HasFloorP/"
      BookkeepingComponent <|-- BeamLineSection
        click BookkeepingComponent href "../BookkeepingComponent/"
      
      BeamLineSection : beamline_relation
        
          
    
        
        
        BeamLineSection --> "1" VirtualRelationEnum : beamline_relation
        click VirtualRelationEnum href "../VirtualRelationEnum/"
    

        
      BeamLineSection : BodyShiftP
        
          
    
        
        
        BeamLineSection --> "0..1" BodyShiftParamGroup : BodyShiftP
        click BodyShiftParamGroup href "../BodyShiftParamGroup/"
    

        
      BeamLineSection : FloorP
        
          
    
        
        
        BeamLineSection --> "0..1" FloorParamGroup : FloorP
        click FloorParamGroup href "../FloorParamGroup/"
    

        
      BeamLineSection : functions
        
          
    
        
        
        BeamLineSection --> "1..*" VirtualFunctionEnum : functions
        click VirtualFunctionEnum href "../VirtualFunctionEnum/"
    

        
      BeamLineSection : id
        
      BeamLineSection : kind
        
      BeamLineSection : MetaP
        
          
    
        
        
        BeamLineSection --> "0..1" MetaParamGroup : MetaP
        click MetaParamGroup href "../MetaParamGroup/"
    

        
      BeamLineSection : native_types
        
      
```





## Inheritance
* [Component](Component.md) [ [HasMetaP](HasMetaP.md)]
    * [VirtualComponent](VirtualComponent.md) [ [HasFloorP](HasFloorP.md)]
        * [BookkeepingComponent](BookkeepingComponent.md) [ [HasBodyShiftP](HasBodyShiftP.md)]
            * **BeamLineSection** [ [HasFloorP](HasFloorP.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [FloorP](FloorP.md) | 0..1 <br/> [FloorParamGroup](FloorParamGroup.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Pl... | [HasFloorP](HasFloorP.md) |
| [BodyShiftP](BodyShiftP.md) | 0..1 <br/> [BodyShiftParamGroup](BodyShiftParamGroup.md) | A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP... | [HasBodyShiftP](HasBodyShiftP.md) |
| [functions](functions.md) | 1..* <br/> [VirtualFunctionEnum](VirtualFunctionEnum.md) | The function of the virtual component,  which can be used to identify the com... | [VirtualComponent](VirtualComponent.md) |
| [beamline_relation](beamline_relation.md) | 1 <br/> [VirtualRelationEnum](VirtualRelationEnum.md) | The relationship of the virtual component to the beamline,  which can be used... | [VirtualComponent](VirtualComponent.md) |
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
| self | pals:BeamLineSection |
| native | pals:BeamLineSection |
| exact | pals:BeamLineSection |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BeamLineSection
description: A virtual component used to represent a section of the BeamLine for organizational
  or functional grouping of components.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:BeamLineSection
is_a: BookkeepingComponent
mixins:
- HasFloorP

```
</details>

### Induced

<details>
```yaml
name: BeamLineSection
description: A virtual component used to represent a section of the BeamLine for organizational
  or functional grouping of components.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:BeamLineSection
is_a: BookkeepingComponent
mixins:
- HasFloorP
attributes:
  FloorP:
    name: FloorP
    description: A mixin for floor plan parameters that are aligned with PALS FloorP
      (Floor Plan Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: FloorP
    owner: BeamLineSection
    domain_of:
    - HasFloorP
    range: FloorParamGroup
    inlined: true
  BodyShiftP:
    name: BodyShiftP
    description: A mixin for floor plan shift parameters that are aligned with PALS
      BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle
      Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: BodyShiftP
    owner: BeamLineSection
    domain_of:
    - HasBodyShiftP
    range: BodyShiftParamGroup
    inlined: true
  functions:
    name: functions
    description: The function of the virtual component,  which can be used to identify
      the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    slot_uri: pals:virtual_function
    alias: functions
    owner: BeamLineSection
    domain_of:
    - PhysicalComponent
    - VirtualComponent
    - SupportingFacilityComponent
    range: VirtualFunctionEnum
    required: true
    multivalued: true
  beamline_relation:
    name: beamline_relation
    description: The relationship of the virtual component to the beamline,  which
      can be used to identify the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    slot_uri: pals:virtual_beamline_relation
    alias: beamline_relation
    owner: BeamLineSection
    domain_of:
    - PhysicalComponent
    - VirtualComponent
    range: VirtualRelationEnum
    required: true
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:id
    identifier: true
    alias: id
    owner: BeamLineSection
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
    designates_type: true
    alias: kind
    owner: BeamLineSection
    domain_of:
    - PALSAccelerator
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
    owner: BeamLineSection
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
    owner: BeamLineSection
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>