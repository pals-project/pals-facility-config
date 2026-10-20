

# Slot: component_relations 


_A list of component relations in the accelerator system (Component <-> Component relationships)._





URI: [pals:slot/component_relations](https://pals-project.readthedocs.io/slot/component_relations)
Alias: component_relations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ComponentRelation](../classes/ComponentRelation.md) |
| Domain Of | [Facility](../classes/Facility.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Facility](../classes/Facility.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:component_relations |
| native | pals:component_relations |




## LinkML Source

<details>
```yaml
name: component_relations
description: A list of component relations in the accelerator system (Component <->
  Component relationships).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: component_relations
owner: Facility
domain_of:
- Facility
range: ComponentRelation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>