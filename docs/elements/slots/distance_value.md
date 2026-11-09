

# Slot: distance_value 


_Distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship._





URI: [pals_config:slot/distance_value](https://w3id.org/pals-config/slot/distance_value)
Alias: distance_value

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
| Range | [Float](../types/Float.md) |
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
| self | pals_config:distance_value |
| native | pals_config:distance_value |
| exact | quantitykind:Distance |




## LinkML Source

<details>
```yaml
name: distance_value
description: Distance value between two components in a relationship. Only an edge-property
  slot for edges that require a distance value between two components in a relationship.
from_schema: https://w3id.org/pals-config
exact_mappings:
- quantitykind:Distance
rank: 1000
alias: distance_value
domain_of:
- AdjacentTo
- NearestTo
range: float

```
</details>