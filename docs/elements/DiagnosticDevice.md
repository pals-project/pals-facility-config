

# Class: DiagnosticDevice 


_An accelerator device used to measure beam or machine state._





URI: [pals:DiagnosticDevice](https://pals-project.readthedocs.io/DiagnosticDevice)





```mermaid
 classDiagram
    class DiagnosticDevice
    click DiagnosticDevice href "../DiagnosticDevice/"
      PhysicalComponent <|-- DiagnosticDevice
        click PhysicalComponent href "../PhysicalComponent/"
      

      DiagnosticDevice <|-- BeamProfileMonitor
        click BeamProfileMonitor href "../BeamProfileMonitor/"
      DiagnosticDevice <|-- BeamPositionMonitor
        click BeamPositionMonitor href "../BeamPositionMonitor/"
      DiagnosticDevice <|-- RadiationMonitor
        click RadiationMonitor href "../RadiationMonitor/"
      

      DiagnosticDevice : beamline_relation
        
          
    
        
        
        DiagnosticDevice --> "1" PhysicalRelationEnum : beamline_relation
        click PhysicalRelationEnum href "../PhysicalRelationEnum/"
    

        
      DiagnosticDevice : FloorP
        
          
    
        
        
        DiagnosticDevice --> "0..1" FloorParamGroup : FloorP
        click FloorParamGroup href "../FloorParamGroup/"
    

        
      DiagnosticDevice : functions
        
          
    
        
        
        DiagnosticDevice --> "1..*" PhysicalFunctionEnum : functions
        click PhysicalFunctionEnum href "../PhysicalFunctionEnum/"
    

        
      DiagnosticDevice : id
        
      DiagnosticDevice : kind
        
      DiagnosticDevice : LongitudinalPlacementP
        
          
    
        
        
        DiagnosticDevice --> "0..1" LongitudinalPlacementParamGroup : LongitudinalPlacementP
        click LongitudinalPlacementParamGroup href "../LongitudinalPlacementParamGroup/"
    

        
      DiagnosticDevice : MetaP
        
          
    
        
        
        DiagnosticDevice --> "0..1" MetaParamGroup : MetaP
        click MetaParamGroup href "../MetaParamGroup/"
    

        
      DiagnosticDevice : native_types
        
      
```





## Inheritance
* [Component](Component.md) [ [HasMetaP](HasMetaP.md)]
    * [PhysicalComponent](PhysicalComponent.md) [ [HasFloorP](HasFloorP.md) [HasLongitudinalPlacementP](HasLongitudinalPlacementP.md)]
        * **DiagnosticDevice**
            * [BeamProfileMonitor](BeamProfileMonitor.md) [ [HasReferenceP](HasReferenceP.md) [HasBodyShiftP](HasBodyShiftP.md) [HasTwissP](HasTwissP.md)]
            * [BeamPositionMonitor](BeamPositionMonitor.md) [ [HasReferenceP](HasReferenceP.md) [HasBodyShiftP](HasBodyShiftP.md) [HasTwissP](HasTwissP.md)]
            * [RadiationMonitor](RadiationMonitor.md) [ [HasBodyShiftP](HasBodyShiftP.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
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
| self | pals:DiagnosticDevice |
| native | pals:DiagnosticDevice |
| broad | pals:Instrument |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiagnosticDevice
description: An accelerator device used to measure beam or machine state.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:Instrument
is_a: PhysicalComponent

```
</details>

### Induced

<details>
```yaml
name: DiagnosticDevice
description: An accelerator device used to measure beam or machine state.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:Instrument
is_a: PhysicalComponent
attributes:
  functions:
    name: functions
    description: The function of the physical component,  which can be used to identify
      the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:physical_function
    alias: functions
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
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
    owner: DiagnosticDevice
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>