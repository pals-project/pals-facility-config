

# Slot: beta_b 


_Twiss beta parameter in the vertical plane._





URI: [pals:beta_b](https://pals-project.readthedocs.io/beta_b)
Alias: beta_b

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TwissParamGroup](../classes/TwissParamGroup.md) | Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [TwissParamGroup](../classes/TwissParamGroup.md) |
| Slot URI | [pals:beta_b](https://pals-project.readthedocs.io/beta_b) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TwissParamGroup](../classes/TwissParamGroup.md) |









## Aliases


* beta_y
* betay




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:beta_b |
| native | pals:beta_b |




## LinkML Source

<details>
```yaml
name: beta_b
description: Twiss beta parameter in the vertical plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- beta_y
- betay
rank: 1000
slot_uri: pals:beta_b
alias: beta_b
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float

```
</details>