

# Class: HasSetpointSignal 



URI: [pals_config:class/HasSetpointSignal](https://w3id.org/pals-config/class/HasSetpointSignal)


```mermaid
erDiagram
FloorParamGroup {
    float phi  
    float psi  
    float theta  
    float x  
    float y  
    float z  
    string id  
}
HasSetpointSignal {
    string predicate  
    string id  
}
LongitudinalPlacementParamGroup {
    float length  
    float s_position  
    string id  
}
MetaParamGroup {
    string description  
    stringList alias  
    string label  
    string id  
}
PhysicalComponent {
    PhysicalRelationEnum beamline_relation  
    PhysicalFunctionEnumList functions  
    string id  
    stringList alias  
    string kind  
    stringList native_types  
}
Signal {
    string access_protocol  
    string archive_identifier  
    CanonicalSignalTypeEnum canonical_signal_type  
    DataTypeEnum native_data_type  
    string native_description  
    UnitEnum native_unit  
    QuantityKindEnum quantity_kind  
    SignalRoleEnum signal_role  
    SourceSystemEnum source_system  
    string id  
    stringList alias  
    string kind  
}

HasSetpointSignal ||--|| PhysicalComponent : "subject"
HasSetpointSignal ||--|| Signal : "object"
MetaParamGroup ||--}o AdditionalMetadata : "additional_metadata"
PhysicalComponent ||--|o FloorParamGroup : "FloorP"
PhysicalComponent ||--|o LongitudinalPlacementParamGroup : "LongitudinalPlacementP"
PhysicalComponent ||--|o MetaParamGroup : "MetaP"
Signal ||--|o MetaParamGroup : "MetaP"

```




## Inheritance
* [Edge](../classes/Edge.md)
    * [SignalBinding](../classes/SignalBinding.md)
        * **HasSetpointSignal**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [Edge](../classes/Edge.md) |
| [subject](../slots/subject.md) | 1 <br/> [PhysicalComponent](../classes/PhysicalComponent.md) |  | [Edge](../classes/Edge.md) |
| [predicate](../slots/predicate.md) | 1 <br/> [String](../types/String.md) | The predicate of the relationship, which can be used to identify the relationship across different source systems. | [Edge](../classes/Edge.md) |
| [object](../slots/object.md) | 1 <br/> [Signal](../classes/Signal.md) |  | [Edge](../classes/Edge.md) |















## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| rdf_predicate | pals_config:has_setpoint_signal |




### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:HasSetpointSignal |
| native | pals_config:HasSetpointSignal |
| close | pals:HasSetpointSignalRelation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasSetpointSignal
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:has_setpoint_signal
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:HasSetpointSignalRelation
is_a: SignalBinding
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true

```
</details>

### Induced

<details>
```yaml
name: HasSetpointSignal
annotations:
  rdf_predicate:
    tag: rdf_predicate
    value: pals_config:has_setpoint_signal
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:HasSetpointSignalRelation
is_a: SignalBinding
slot_usage:
  predicate:
    name: predicate
    description: The predicate of the relationship, which can be used to identify
      the relationship across different source systems.
    required: true
attributes:
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: HasSetpointSignal
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
    owner: HasSetpointSignal
    domain_of:
    - Edge
    range: PhysicalComponent
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
    owner: HasSetpointSignal
    domain_of:
    - Edge
    range: string
    required: true
  object:
    name: object
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:object
    alias: object
    owner: HasSetpointSignal
    domain_of:
    - Edge
    range: Signal
    required: true

```
</details>