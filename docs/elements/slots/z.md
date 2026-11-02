

# Slot: z 


_Global Z coordinate in the facility floor plan._





URI: [acc:slot/z](https://example.org/accelerator-core/slot/z)
Alias: z

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


* z_coordinate
* ModelZ
* z coordinate




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:z |
| native | acc:z |
| close | pals:z |




## LinkML Source

<details>
```yaml
name: z
description: Global Z coordinate in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- z_coordinate
- ModelZ
- z coordinate
close_mappings:
- pals:z
rank: 1000
alias: z
owner: FloorParamGroup
domain_of:
- FloorParamGroup
range: float

```
</details>