

# Class: Precedes 


_A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline._





URI: [pals_config:class/Precedes](https://w3id.org/pals-config/class/Precedes)


```mermaid
erDiagram
BeamLine {
    string description  
    integer direction  
    float length  
    boolean multipass  
    boolean periodic  
    integer repeat  
    string id  
    stringList alias  
    string kind  
    stringList native_types  
    VirtualRelationEnum beamline_relation  
    VirtualFunctionEnumList functions  
}
Component {
    stringList native_types  
    string id  
    stringList alias  
    string kind  
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
MetaParamGroup {
    string description  
    stringList alias  
    string label  
    string id  
}
Precedes {
    RelationContextEnum context  
    string predicate  
    string id  
    DirectionEnum component_direction  
    ReferenceFrameEnum reference_frame  
}

BeamLine ||--|o FloorParamGroup : "FloorP"
BeamLine ||--|o MetaParamGroup : "MetaP"
Component ||--|o MetaParamGroup : "MetaP"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"
Precedes ||--|o BeamLine : "beamline_context"
Precedes ||--|| Component : "object, subject"

```




## Inheritance
* [Edge](../classes/Edge.md)
    * [ComponentRelation](../classes/ComponentRelation.md)
        * **Precedes**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [beamline_context](../slots/beamline_context.md) | 0..1 <br/> [BeamLine](../classes/BeamLine.md) | The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine. | direct |
| [context](../slots/context.md) | 1 <br/> [RelationContextEnum](../enums/RelationContextEnum.md) | The frame of reference / domain in which this relationship is asserted to hold. For Precedes, this is always beamline_order; the specific BeamLine is given in beamline_context. | [ComponentRelation](../classes/ComponentRelation.md) |
| [component_direction](../slots/component_direction.md) | 0..1 <br/> [DirectionEnum](../enums/DirectionEnum.md) |  | [ComponentRelation](../classes/ComponentRelation.md) |
| [reference_frame](../slots/reference_frame.md) | 0..1 _recommended_ <br/> [ReferenceFrameEnum](../enums/ReferenceFrameEnum.md) |  | [ComponentRelation](../classes/ComponentRelation.md) |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [Edge](../classes/Edge.md) |
| [subject](../slots/subject.md) | 1 <br/> [Component](../classes/Component.md) |  | [Edge](../classes/Edge.md) |
| [predicate](../slots/predicate.md) | 1 <br/> [String](../types/String.md) | The predicate of the relationship, which can be used to identify the relationship across different source systems. | [Edge](../classes/Edge.md) |
| [object](../slots/object.md) | 1 <br/> [Component](../classes/Component.md) |  | [Edge](../classes/Edge.md) |







## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'predicate': {'equals_string': 'Precedes'}}``` |```{'context': {'equals_string': 'beamline_order'}}``` | |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| rdf_predicate | pals_config:precedes |




### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Precedes |
| native | pals_config:Precedes |
| related | BFO:0000063 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Precedes
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:precedes
description: A relationship indicating that the subject component precedes the object
  component in a specified context,  such as along a beamline.
from_schema: https://w3id.org/pals-config
related_mappings:
- BFO:0000063
is_a: ComponentRelation
slots:
- beamline_context
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
    equals_string: Precedes
  context:
    name: context
    description: The frame of reference / domain in which this relationship is asserted
      to hold. For Precedes, this is always beamline_order; the specific BeamLine
      is given in beamline_context.
    required: true
rules:
- preconditions:
    slot_conditions:
      predicate:
        name: predicate
        equals_string: Precedes
  postconditions:
    slot_conditions:
      context:
        name: context
        equals_string: beamline_order
  description: This is a Precedes relation, context must be beamline_order

```
</details>

### Induced

<details>
```yaml
name: Precedes
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:precedes
description: A relationship indicating that the subject component precedes the object
  component in a specified context,  such as along a beamline.
from_schema: https://w3id.org/pals-config
related_mappings:
- BFO:0000063
is_a: ComponentRelation
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
    equals_string: Precedes
  context:
    name: context
    description: The frame of reference / domain in which this relationship is asserted
      to hold. For Precedes, this is always beamline_order; the specific BeamLine
      is given in beamline_context.
    required: true
attributes:
  beamline_context:
    name: beamline_context
    description: The specific BeamLine this relationship is defined with respect to
      (relevant when context=beamline_order). Only an edge-property slot for edges
      that are defined with respect to a specific BeamLine.
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: beamline_context
    owner: Precedes
    domain_of:
    - Precedes
    - Contains
    - IsPartOf
    - HasConnectingBranch
    range: BeamLine
    required: false
  context:
    name: context
    description: The frame of reference / domain in which this relationship is asserted
      to hold. For Precedes, this is always beamline_order; the specific BeamLine
      is given in beamline_context.
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: context
    owner: Precedes
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
    owner: Precedes
    domain_of:
    - ComponentRelation
    range: DirectionEnum
  reference_frame:
    name: reference_frame
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: reference_frame
    owner: Precedes
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
    owner: Precedes
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
    owner: Precedes
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
    owner: Precedes
    domain_of:
    - Edge
    range: string
    required: true
    equals_string: Precedes
  object:
    name: object
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:object
    alias: object
    owner: Precedes
    domain_of:
    - Edge
    range: Component
    required: true
rules:
- preconditions:
    slot_conditions:
      predicate:
        name: predicate
        equals_string: Precedes
  postconditions:
    slot_conditions:
      context:
        name: context
        equals_string: beamline_order
  description: This is a Precedes relation, context must be beamline_order

```
</details>