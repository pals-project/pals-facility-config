

# Slot: alpha_a 


_Twiss alpha parameter in the horizontal plane._





URI: [pals:alpha_a](https://pals-project.readthedocs.io/alpha_a)
Alias: alpha_a

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
| Slot URI | [pals:alpha_a](https://pals-project.readthedocs.io/alpha_a) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TwissParamGroup](../classes/TwissParamGroup.md) |









## Aliases


* alpha_x
* alphax




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:alpha_a |
| native | pals:alpha_a |




## LinkML Source

<details>
```yaml
name: alpha_a
description: Twiss alpha parameter in the horizontal plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- alpha_x
- alphax
rank: 1000
slot_uri: pals:alpha_a
alias: alpha_a
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float

```
</details>