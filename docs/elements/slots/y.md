

# Slot: y 


_Global Y coordinate in the facility floor plan._





URI: [pals_config:slot/y](https://w3id.org/pals-config/slot/y)
Alias: y

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FloorParamGroup](../classes/FloorParamGroup.md) | Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [FloorParamGroup](../classes/FloorParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FloorParamGroup](../classes/FloorParamGroup.md) |









## Aliases


* y_coordinate
* ModelY
* y coordinate




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:y |
| native | pals_config:y |
| close | pals:y |




## LinkML Source

<details>
```yaml
name: y
description: Global Y coordinate in the facility floor plan.
from_schema: https://w3id.org/pals-config
aliases:
- y_coordinate
- ModelY
- y coordinate
close_mappings:
- pals:y
rank: 1000
alias: y
owner: FloorParamGroup
domain_of:
- FloorParamGroup
range: float

```
</details>