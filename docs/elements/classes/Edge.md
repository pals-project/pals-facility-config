

# Class: Edge 


_Abstract base for subject-predicate-object associations._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [pals_config:class/Edge](https://w3id.org/pals-config/class/Edge)


```mermaid
erDiagram
Edge {
    string id  
    string object  
    string predicate  
    string subject  
}



```




## Inheritance
* **Edge**
    * [SignalBinding](../classes/SignalBinding.md)
    * [ComponentRelation](../classes/ComponentRelation.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | direct |
| [subject](../slots/subject.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [predicate](../slots/predicate.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [object](../slots/object.md) | 1 <br/> [String](../types/String.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Edge |
| native | pals_config:Edge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Edge
description: Abstract base for subject-predicate-object associations.
from_schema: https://w3id.org/pals-config
abstract: true
slots:
- id
- subject
- predicate
- object

```
</details>

### Induced

<details>
```yaml
name: Edge
description: Abstract base for subject-predicate-object associations.
from_schema: https://w3id.org/pals-config
abstract: true
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
    owner: Edge
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
    owner: Edge
    domain_of:
    - Edge
    range: string
    required: true
  predicate:
    name: predicate
    from_schema: https://w3id.org/pals-config
    rank: 1000
    slot_uri: rdf:predicate
    designates_type: true
    alias: predicate
    owner: Edge
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
    owner: Edge
    domain_of:
    - Edge
    range: string
    required: true

```
</details>