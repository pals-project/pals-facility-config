

# Slot: alpha_a 


_Twiss alpha parameter in the horizontal plane._





URI: [acc:slot/alpha_a](https://example.org/accelerator-core/slot/alpha_a)
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
| self | acc:alpha_a |
| native | acc:alpha_a |
| close | pals:alpha_a |




## LinkML Source

<details>
```yaml
name: alpha_a
description: Twiss alpha parameter in the horizontal plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- alpha_x
- alphax
close_mappings:
- pals:alpha_a
rank: 1000
alias: alpha_a
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float

```
</details>