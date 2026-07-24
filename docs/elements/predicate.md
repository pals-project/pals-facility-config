

# Slot: predicate 



URI: [rdf:predicate](http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate)
Alias: predicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComponentRelation](ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting con... |  yes  |
| [SignalBinding](SignalBinding.md) | Association between a PhysicalComponent and one of its Signals, e |  yes  |
| [Relationship](Relationship.md) | Abstract base for subject-predicate-object associations |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:predicate |
| native | pals:predicate |




## LinkML Source

<details>
```yaml
name: predicate
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: rdf:predicate
alias: predicate
domain_of:
- Relationship
relational_role: PREDICATE
range: string
required: true

```
</details>