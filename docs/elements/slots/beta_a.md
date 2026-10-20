

# Slot: beta_a 


_Twiss beta parameter in the horizontal plane._





URI: [pals:beta_a](https://pals-project.readthedocs.io/beta_a)
Alias: beta_a

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
| Slot URI | [pals:beta_a](https://pals-project.readthedocs.io/beta_a) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TwissParamGroup](../classes/TwissParamGroup.md) |









## Aliases


* beta_x
* betax




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:beta_a |
| native | pals:beta_a |




## LinkML Source

<details>
```yaml
name: beta_a
description: Twiss beta parameter in the horizontal plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- beta_x
- betax
rank: 1000
slot_uri: pals:beta_a
alias: beta_a
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float

```
</details>