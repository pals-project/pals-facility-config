

# Class: BookkeepingComponent 


_A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices._





URI: [pals:BookkeepingComponent](https://pals-project.readthedocs.io/BookkeepingComponent)





```mermaid
 classDiagram
    class BookkeepingComponent
    click BookkeepingComponent href "../BookkeepingComponent/"
      HasBodyShiftP <|-- BookkeepingComponent
        click HasBodyShiftP href "../HasBodyShiftP/"
      VirtualComponent <|-- BookkeepingComponent
        click VirtualComponent href "../VirtualComponent/"
      

      BookkeepingComponent <|-- Marker
        click Marker href "../Marker/"
      BookkeepingComponent <|-- BeamLineSection
        click BeamLineSection href "../BeamLineSection/"
      

      BookkeepingComponent : beamline_relation
        
          
    
        
        
        BookkeepingComponent --> "1" VirtualRelationEnum : beamline_relation
        click VirtualRelationEnum href "../VirtualRelationEnum/"
    

        
      BookkeepingComponent : BodyShiftP
        
          
    
        
        
        BookkeepingComponent --> "0..1" BodyShiftParamGroup : BodyShiftP
        click BodyShiftParamGroup href "../BodyShiftParamGroup/"
    

        
      BookkeepingComponent : FloorP
        
          
    
        
        
        BookkeepingComponent --> "0..1" FloorParamGroup : FloorP
        click FloorParamGroup href "../FloorParamGroup/"
    

        
      BookkeepingComponent : functions
        
          
    
        
        
        BookkeepingComponent --> "1..*" VirtualFunctionEnum : functions
        click VirtualFunctionEnum href "../VirtualFunctionEnum/"
    

        
      BookkeepingComponent : id
        
      BookkeepingComponent : kind
        
      BookkeepingComponent : MetaP
        
          
    
        
        
        BookkeepingComponent --> "0..1" MetaParamGroup : MetaP
        click MetaParamGroup href "../MetaParamGroup/"
    

        
      BookkeepingComponent : native_types
        
      
```





## Inheritance
* [Component](Component.md) [ [HasMetaP](HasMetaP.md)]
    * [VirtualComponent](VirtualComponent.md) [ [HasFloorP](HasFloorP.md)]
        * **BookkeepingComponent** [ [HasBodyShiftP](HasBodyShiftP.md)]
            * [Marker](Marker.md) [ [HasTwissP](HasTwissP.md)]
            * [BeamLineSection](BeamLineSection.md) [ [HasFloorP](HasFloorP.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [BodyShiftP](BodyShiftP.md) | 0..1 <br/> [BodyShiftParamGroup](BodyShiftParamGroup.md) | A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP... | [HasBodyShiftP](HasBodyShiftP.md) |
| [functions](functions.md) | 1..* <br/> [VirtualFunctionEnum](VirtualFunctionEnum.md) | The function of the virtual component,  which can be used to identify the com... | [VirtualComponent](VirtualComponent.md) |
| [beamline_relation](beamline_relation.md) | 1 <br/> [VirtualRelationEnum](VirtualRelationEnum.md) | The relationship of the virtual component to the beamline,  which can be used... | [VirtualComponent](VirtualComponent.md) |
| [FloorP](FloorP.md) | 0..1 <br/> [FloorParamGroup](FloorParamGroup.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Pl... | [HasFloorP](HasFloorP.md) |
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
| self | pals:BookkeepingComponent |
| native | pals:BookkeepingComponent |
| broad | pals:BookkeepingElement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BookkeepingComponent
description: A virtual component that represents a bookkeeping or organizational role
  in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can
  include BeamLineSections, Markers, Forks, and other virtual components that are
  important for understanding  the structure and function of the accelerator system
  but are not physical devices.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:BookkeepingElement
is_a: VirtualComponent
mixins:
- HasBodyShiftP

```
</details>

### Induced

<details>
```yaml
name: BookkeepingComponent
description: A virtual component that represents a bookkeeping or organizational role
  in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can
  include BeamLineSections, Markers, Forks, and other virtual components that are
  important for understanding  the structure and function of the accelerator system
  but are not physical devices.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:BookkeepingElement
is_a: VirtualComponent
mixins:
- HasBodyShiftP
attributes:
  BodyShiftP:
    name: BodyShiftP
    description: A mixin for floor plan shift parameters that are aligned with PALS
      BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle
      Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: BodyShiftP
    owner: BookkeepingComponent
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
    owner: BookkeepingComponent
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
    owner: BookkeepingComponent
    domain_of:
    - PhysicalComponent
    - VirtualComponent
    range: VirtualRelationEnum
    required: true
  FloorP:
    name: FloorP
    description: A mixin for floor plan parameters that are aligned with PALS FloorP
      (Floor Plan Parameters) for interoperability with the Particle Accelerator Language
      Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: FloorP
    owner: BookkeepingComponent
    domain_of:
    - HasFloorP
    range: FloorParamGroup
    inlined: true
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:id
    identifier: true
    alias: id
    owner: BookkeepingComponent
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
    owner: BookkeepingComponent
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
    owner: BookkeepingComponent
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
    owner: BookkeepingComponent
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>