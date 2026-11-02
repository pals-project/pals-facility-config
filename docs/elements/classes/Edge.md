

# Class: Edge 


_Abstract base for subject-predicate-object associations._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement)


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


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | direct |
| [subject](../slots/subject.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [predicate](../slots/predicate.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [object](../slots/object.md) | 1 <br/> [String](../types/String.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:Statement |
| native | acc:Edge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Edge
description: Abstract base for subject-predicate-object associations.
from_schema: https://w3id.org/accelerator-core
abstract: true
slots:
- id
- subject
- predicate
- object
class_uri: rdf:Statement

```
</details>

### Induced

<details>
```yaml
name: Edge
description: Abstract base for subject-predicate-object associations.
from_schema: https://w3id.org/accelerator-core
abstract: true
attributes:
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
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
    from_schema: https://w3id.org/accelerator-core
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
    from_schema: https://w3id.org/accelerator-core
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
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: rdf:object
    alias: object
    owner: Edge
    domain_of:
    - Edge
    range: string
    required: true
class_uri: rdf:Statement

```
</details>