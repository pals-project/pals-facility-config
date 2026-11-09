

# Class: Intersects 


_A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device._





URI: [pals_config:class/Intersects](https://w3id.org/pals-config/class/Intersects)


```mermaid
erDiagram
Component {
    stringList native_types  
    string id  
    stringList alias  
    string kind  
}
Intersects {
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
Intersects ||--|| Component : "object, subject"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"

```




## Inheritance
* [Edge](../classes/Edge.md)
    * [ComponentRelation](../classes/ComponentRelation.md)
        * **Intersects**


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
| rdf_predicate | pals_config:intersects |




### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Intersects |
| native | pals_config:Intersects |
| related | RO:0015011 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Intersects
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:intersects
description: A relationship indicating that the subject component intersects the object
  component in a specified context,  such as a beamline and a diagnostic device.
from_schema: https://w3id.org/pals-config
related_mappings:
- RO:0015011
is_a: ComponentRelation
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
    equals_string: Intersects

```
</details>

### Induced

<details>
```yaml
name: Intersects
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:intersects
description: A relationship indicating that the subject component intersects the object
  component in a specified context,  such as a beamline and a diagnostic device.
from_schema: https://w3id.org/pals-config
related_mappings:
- RO:0015011
is_a: ComponentRelation
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
    equals_string: Intersects
attributes:
  context:
    name: context
    description: The frame of reference / domain in which this relationship is asserted
      to hold.
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: context
    owner: Intersects
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
    owner: Intersects
    domain_of:
    - ComponentRelation
    range: DirectionEnum
  reference_frame:
    name: reference_frame
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: reference_frame
    owner: Intersects
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
    owner: Intersects
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
    owner: Intersects
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
    owner: Intersects
    domain_of:
    - Edge
    range: string
    required: true
    equals_string: Intersects
  object:
    name: object
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:object
    alias: object
    owner: Intersects
    domain_of:
    - Edge
    range: Component
    required: true

```
</details>