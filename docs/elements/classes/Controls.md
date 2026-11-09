

# Class: Controls 


_A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet._





URI: [pals_config:class/Controls](https://w3id.org/pals-config/class/Controls)


```mermaid
erDiagram
Component {
    stringList native_types  
    string id  
    stringList alias  
    string kind  
}
Controls {
    string predicate  
    string id  
    DirectionEnum component_direction  
    RelationContextEnum context  
    ReferenceFrameEnum reference_frame  
}
MetaParamGroup {
    string description  
    stringList alias  
    string label  
    string id  
}

Component ||--|o MetaParamGroup : "MetaP"
Controls ||--|| Component : "object, subject"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"

```




## Inheritance
* [Edge](../classes/Edge.md)
    * [ComponentRelation](../classes/ComponentRelation.md)
        * **Controls**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [context](../slots/context.md) | 1 <br/> [RelationContextEnum](../enums/RelationContextEnum.md) | The frame of reference / domain in which this relationship is asserted to hold. | [ComponentRelation](../classes/ComponentRelation.md) |
| [component_direction](../slots/component_direction.md) | 0..1 <br/> [DirectionEnum](../enums/DirectionEnum.md) |  | [ComponentRelation](../classes/ComponentRelation.md) |
| [reference_frame](../slots/reference_frame.md) | 0..1 _recommended_ <br/> [ReferenceFrameEnum](../enums/ReferenceFrameEnum.md) |  | [ComponentRelation](../classes/ComponentRelation.md) |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [Edge](../classes/Edge.md) |
| [subject](../slots/subject.md) | 1 <br/> [Component](../classes/Component.md) |  | [Edge](../classes/Edge.md) |
| [predicate](../slots/predicate.md) | 1 <br/> [String](../types/String.md) | The predicate of the relationship, which can be used to identify the relationship across different source systems. | [Edge](../classes/Edge.md) |
| [object](../slots/object.md) | 1 <br/> [Component](../classes/Component.md) |  | [Edge](../classes/Edge.md) |















## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| rdf_predicate | pals_config:controls |




### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Controls |
| native | pals_config:Controls |
| related | saref:targets#saref-controls |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Controls
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:controls
description: A relationship indicating that the subject component controls the object
  component in a specified context,  such as a power supply controlling a magnet.
from_schema: https://w3id.org/pals-config
related_mappings:
- saref:targets#saref-controls
is_a: ComponentRelation
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
    equals_string: Controls

```
</details>

### Induced

<details>
```yaml
name: Controls
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:controls
description: A relationship indicating that the subject component controls the object
  component in a specified context,  such as a power supply controlling a magnet.
from_schema: https://w3id.org/pals-config
related_mappings:
- saref:targets#saref-controls
is_a: ComponentRelation
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
    equals_string: Controls
attributes:
  context:
    name: context
    description: The frame of reference / domain in which this relationship is asserted
      to hold.
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: context
    owner: Controls
    domain_of:
    - ComponentRelation
    - IsPartOf
    range: RelationContextEnum
    required: true
  component_direction:
    name: component_direction
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: component_direction
    owner: Controls
    domain_of:
    - ComponentRelation
    range: DirectionEnum
  reference_frame:
    name: reference_frame
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: reference_frame
    owner: Controls
    domain_of:
    - ComponentRelation
    range: ReferenceFrameEnum
    recommended: true
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: Controls
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true
  subject:
    name: subject
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:subject
    alias: subject
    owner: Controls
    domain_of:
    - Edge
    range: Component
    required: true
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:predicate
    designates_type: true
    alias: predicate
    owner: Controls
    domain_of:
    - Edge
    range: string
    required: true
    equals_string: Controls
  object:
    name: object
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:object
    alias: object
    owner: Controls
    domain_of:
    - Edge
    range: Component
    required: true

```
</details>