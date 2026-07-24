

# Slot: subject 



URI: [rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject)
Alias: subject

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
| self | rdf:subject |
| native | pals:subject |




## LinkML Source

<details>
```yaml
name: subject
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: rdf:subject
alias: subject
domain_of:
- Relationship
relational_role: SUBJECT
range: string
required: true

```
</details>