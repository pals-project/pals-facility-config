

# Slot: tolerance_unit 


_Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship._





URI: [acc:slot/tolerance_unit](https://example.org/accelerator-core/slot/tolerance_unit)
Alias: tolerance_unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NearestTo](../classes/NearestTo.md) | A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet. |  no  |
| [AdjacentTo](../classes/AdjacentTo.md) | A relationship indicating that the subject component is adjacent to the object component and not overlapping<br> in a specified context, such as radiation detector and a magnet. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [UnitEnum](../enums/UnitEnum.md) |
| Domain Of | [AdjacentTo](../classes/AdjacentTo.md), [NearestTo](../classes/NearestTo.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:tolerance_unit |
| native | acc:tolerance_unit |




## LinkML Source

<details>
```yaml
name: tolerance_unit
description: Unit of the tolerance value for the distance between two components in
  a relationship. Only an edge-property slot for edges that require a tolerance value
  between two components in a relationship.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: tolerance_unit
domain_of:
- AdjacentTo
- NearestTo
range: UnitEnum

```
</details>