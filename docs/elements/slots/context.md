

# Slot: context 


_The frame of reference / domain in which this relationship is asserted to hold._





URI: [pals:slot/context](https://pals-project.readthedocs.io/slot/context)
Alias: context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComponentRelation](../classes/ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelationContextEnum](../enums/RelationContextEnum.md) |
| Domain Of | [ComponentRelation](../classes/ComponentRelation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ComponentRelation](../classes/ComponentRelation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:context |
| native | pals:context |




## LinkML Source

<details>
```yaml
name: context
description: The frame of reference / domain in which this relationship is asserted
  to hold.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: context
owner: ComponentRelation
domain_of:
- ComponentRelation
range: RelationContextEnum

```
</details>