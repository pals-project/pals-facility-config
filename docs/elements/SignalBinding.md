

# Class: SignalBinding 


_Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding._





URI: [pals:SignalBinding](https://pals-project.readthedocs.io/SignalBinding)





```mermaid
 classDiagram
    class SignalBinding
    click SignalBinding href "../SignalBinding/"
      Relationship <|-- SignalBinding
        click Relationship href "../Relationship/"
      
      SignalBinding : id
        
      SignalBinding : object
        
          
    
        
        
        SignalBinding --> "1" Signal : object
        click Signal href "../Signal/"
    

        
      SignalBinding : predicate
        
          
    
        
        
        SignalBinding --> "1" SignalBindingPredicateEnum : predicate
        click SignalBindingPredicateEnum href "../SignalBindingPredicateEnum/"
    

        
      SignalBinding : subject
        
          
    
        
        
        SignalBinding --> "1" PhysicalComponent : subject
        click PhysicalComponent href "../PhysicalComponent/"
    

        
      
```





## Inheritance
* [Relationship](Relationship.md)
    * **SignalBinding**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the instance | [Relationship](Relationship.md) |
| [subject](subject.md) | 1 <br/> [PhysicalComponent](PhysicalComponent.md) |  | [Relationship](Relationship.md) |
| [predicate](predicate.md) | 1 <br/> [SignalBindingPredicateEnum](SignalBindingPredicateEnum.md) |  | [Relationship](Relationship.md) |
| [object](object.md) | 1 <br/> [Signal](Signal.md) |  | [Relationship](Relationship.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Facility](Facility.md) | [signal_bindings](signal_bindings.md) | range | [SignalBinding](SignalBinding.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:SignalBinding |
| native | pals:SignalBinding |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SignalBinding
description: Association between a PhysicalComponent and one of its Signals, e.g.
  QUAD1.QUAD1_STATUS_binding.
from_schema: https://w3id.org/accelerator-core
is_a: Relationship
slot_usage:
  subject:
    name: subject
    range: PhysicalComponent
  predicate:
    name: predicate
    range: SignalBindingPredicateEnum
  object:
    name: object
    range: Signal

```
</details>

### Induced

<details>
```yaml
name: SignalBinding
description: Association between a PhysicalComponent and one of its Signals, e.g.
  QUAD1.QUAD1_STATUS_binding.
from_schema: https://w3id.org/accelerator-core
is_a: Relationship
slot_usage:
  subject:
    name: subject
    range: PhysicalComponent
  predicate:
    name: predicate
    range: SignalBindingPredicateEnum
  object:
    name: object
    range: Signal
attributes:
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:id
    identifier: true
    alias: id
    owner: SignalBinding
    domain_of:
    - Affiliation
    - Component
    - Signal
    - Relationship
    range: string
    required: true
  subject:
    name: subject
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: rdf:subject
    alias: subject
    owner: SignalBinding
    domain_of:
    - Relationship
    relational_role: SUBJECT
    range: PhysicalComponent
    required: true
  predicate:
    name: predicate
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: rdf:predicate
    alias: predicate
    owner: SignalBinding
    domain_of:
    - Relationship
    relational_role: PREDICATE
    range: SignalBindingPredicateEnum
    required: true
  object:
    name: object
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: rdf:object
    alias: object
    owner: SignalBinding
    domain_of:
    - Relationship
    relational_role: OBJECT
    range: Signal
    required: true

```
</details>