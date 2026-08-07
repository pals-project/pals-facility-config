

# Class: BeamLine 


_PALS element for an ordered sequence of beamline elements defining a beam path._





URI: [pals:class/BeamLine](https://pals-project.readthedocs.io/class/BeamLine)


```mermaid
erDiagram
AdditionalMetadata {
    DataTypeEnum datatype  
    string key  
    string value  
}
BeamLine {
    string description  
    integer direction  
    float length  
    boolean multipass  
    boolean periodic  
    integer repeat  
    string id  
    string kind  
    stringList native_types  
    VirtualRelationEnum beamline_relation  
    VirtualFunctionEnumList functions  
}
FloorParamGroup {
    float phi  
    float psi  
    float theta  
    float x  
    float y  
    float z  
}
MetaParamGroup {
    string description  
    string alias  
    string label  
}

BeamLine ||--|o FloorParamGroup : "FloorP"
BeamLine ||--|o MetaParamGroup : "MetaP"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"

```




## Inheritance
* [Component](../classes/Component.md) [ [HasMetaP](../classes/HasMetaP.md)]
    * [VirtualComponent](../classes/VirtualComponent.md) [ [HasFloorP](../classes/HasFloorP.md)]
        * **BeamLine**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [length](../slots/length.md) | 0..1 <br/> [Float](../types/Float.md) | The total length of the BeamLine. For pals interoperability, use m as the unit of length. | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) | A human-readable description of the instance. | direct |
| [multipass](../slots/multipass.md) | 0..1 <br/> [Boolean](../types/Boolean.md) | Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass. | direct |
| [periodic](../slots/periodic.md) | 0..1 <br/> [Boolean](../types/Boolean.md) | Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic. | direct |
| [repeat](../slots/repeat.md) | 0..1 <br/> [Integer](../types/Integer.md) | Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.<br>If value is greater than 1, the beamline is repeated that many times. | direct |
| [direction](../slots/direction.md) | 0..1 <br/> [Integer](../types/Integer.md) | Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1. | direct |
| [functions](../slots/functions.md) | 1..* <br/> [VirtualFunctionEnum](../enums/VirtualFunctionEnum.md) | The function of the virtual component,  which can be used to identify the component across different source systems. | [VirtualComponent](../classes/VirtualComponent.md) |
| [beamline_relation](../slots/beamline_relation.md) | 1 <br/> [VirtualRelationEnum](../enums/VirtualRelationEnum.md) | The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems. | [VirtualComponent](../classes/VirtualComponent.md) |
| [FloorP](../slots/FloorP.md) | 0..1 <br/> [FloorParamGroup](../classes/FloorParamGroup.md) | A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasFloorP](../classes/HasFloorP.md) |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [Component](../classes/Component.md) |
| [kind](../slots/kind.md) | 1 <br/> [String](../types/String.md) | The LinkML class name of this instance. | [Component](../classes/Component.md) |
| [native_types](../slots/native_types.md) | * <br/> [String](../types/String.md) | The native type of the component in the source system, which can be used to identify the component across different source systems. | [Component](../classes/Component.md) |
| [MetaP](../slots/MetaP.md) | 0..1 <br/> [MetaParamGroup](../classes/MetaParamGroup.md) | A mixin for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | [HasMetaP](../classes/HasMetaP.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Facility](../classes/Facility.md) | [beamlines](../slots/beamlines.md) | range | [BeamLine](../classes/BeamLine.md) |
| [ComponentRelation](../classes/ComponentRelation.md) | [beamline_context](../slots/beamline_context.md) | range | [BeamLine](../classes/BeamLine.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:BeamLine |
| native | pals:BeamLine |
| exact | pals:BeamLine |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BeamLine
description: PALS element for an ordered sequence of beamline elements defining a
  beam path.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:BeamLine
is_a: VirtualComponent
slots:
- length
- description
slot_usage:
  length:
    name: length
    description: The total length of the BeamLine. For pals interoperability, use
      m as the unit of length.
attributes:
  multipass:
    name: multipass
    description: Indicates whether the BeamLine is a multipass BeamLine, where the
      beam passes through the same physical elements multiple times. If not provided,
      the default assumption is that the BeamLine is single-pass.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:multipass
    domain_of:
    - BeamLine
    range: boolean
  periodic:
    name: periodic
    description: Indicates whether orbit and Twiss parameters periodic. If not provided,
      the default assumption is that the BeamLine is not periodic.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:periodic
    domain_of:
    - BeamLine
    range: boolean
  repeat:
    name: repeat
    description: 'Repetition count. If not provided, the default assumption is that
      the beamline is not repeated and the value is 1.

      If value is greater than 1, the beamline is repeated that many times.'
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:repeat
    domain_of:
    - BeamLine
    range: integer
  direction:
    name: direction
    description: 'Beam direction along the BeamLine: +1 or -1. Longitudinal orientation.
      Default is +1.'
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:direction
    domain_of:
    - BeamLine
    range: integer

```
</details>

### Induced

<details>
```yaml
name: BeamLine
description: PALS element for an ordered sequence of beamline elements defining a
  beam path.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:BeamLine
is_a: VirtualComponent
slot_usage:
  length:
    name: length
    description: The total length of the BeamLine. For pals interoperability, use
      m as the unit of length.
attributes:
  multipass:
    name: multipass
    description: Indicates whether the BeamLine is a multipass BeamLine, where the
      beam passes through the same physical elements multiple times. If not provided,
      the default assumption is that the BeamLine is single-pass.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:multipass
    alias: multipass
    owner: BeamLine
    domain_of:
    - BeamLine
    range: boolean
  periodic:
    name: periodic
    description: Indicates whether orbit and Twiss parameters periodic. If not provided,
      the default assumption is that the BeamLine is not periodic.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:periodic
    alias: periodic
    owner: BeamLine
    domain_of:
    - BeamLine
    range: boolean
  repeat:
    name: repeat
    description: 'Repetition count. If not provided, the default assumption is that
      the beamline is not repeated and the value is 1.

      If value is greater than 1, the beamline is repeated that many times.'
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:repeat
    alias: repeat
    owner: BeamLine
    domain_of:
    - BeamLine
    range: integer
  direction:
    name: direction
    description: 'Beam direction along the BeamLine: +1 or -1. Longitudinal orientation.
      Default is +1.'
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:direction
    alias: direction
    owner: BeamLine
    domain_of:
    - BeamLine
    range: integer
  length:
    name: length
    description: The total length of the BeamLine. For pals interoperability, use
      m as the unit of length.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:length
    alias: length
    owner: BeamLine
    domain_of:
    - LongitudinalPlacementParamGroup
    - BeamLine
    range: float
  description:
    name: description
    description: A human-readable description of the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: description
    owner: BeamLine
    domain_of:
    - PALSAccelerator
    - MetaParamGroup
    - BeamLine
    range: string
  functions:
    name: functions
    description: The function of the virtual component,  which can be used to identify
      the component across different source systems.
    from_schema: https://w3id.org/accelerator-core
    slot_uri: pals:virtual_function
    alias: functions
    owner: BeamLine
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
    owner: BeamLine
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
    owner: BeamLine
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
    owner: BeamLine
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
    owner: BeamLine
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
    owner: BeamLine
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
    owner: BeamLine
    domain_of:
    - HasMetaP
    range: MetaParamGroup
    inlined: true

```
</details>