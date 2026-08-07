

# Slot: predicate 



URI: [rdf:predicate](http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate)
Alias: predicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SignalBinding](../classes/SignalBinding.md) | Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding. |  yes  |
| [Relationship](../classes/Relationship.md) | Abstract base for subject-predicate-object associations. |  no  |
| [ComponentRelation](../classes/ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Relationship](../classes/Relationship.md) |
| Slot URI | [rdf:predicate](http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Relational Role | PREDICATE |

</details>











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