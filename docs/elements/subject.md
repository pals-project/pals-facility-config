

# Slot: subject 



URI: [rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject)
Alias: subject

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComponentRelation](ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting con... |  yes  |
| [Relationship](Relationship.md) | Abstract base for subject-predicate-object associations |  no  |
| [SignalBinding](SignalBinding.md) | Association between a PhysicalComponent and one of its Signals, e |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Relationship](Relationship.md) |
| Slot URI | [rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Relational Role | SUBJECT |

</details>











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