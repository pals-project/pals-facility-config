

# Slot: distance_unit 


_Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship._





URI: [pals_config:slot/distance_unit](https://w3id.org/pals-config/slot/distance_unit)
Alias: distance_unit

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


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:distance_unit |
| native | pals_config:distance_unit |
| related | saref:UnitOfMeasure |




## LinkML Source

<details>
```yaml
name: distance_unit
description: Unit of the distance value between two components in a relationship.
  Only an edge-property slot for edges that require a distance value between two components
  in a relationship.
from_schema: https://w3id.org/pals-config
related_mappings:
- saref:UnitOfMeasure
rank: 1000
alias: distance_unit
domain_of:
- AdjacentTo
- NearestTo
range: UnitEnum

```
</details>