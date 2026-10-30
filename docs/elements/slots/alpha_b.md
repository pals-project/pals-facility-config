

# Slot: alpha_b 


_Twiss alpha parameter in the vertical plane._





URI: [acc:slot/alpha_b](https://example.org/accelerator-core/slot/alpha_b)
Alias: alpha_b

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


* alpha_y
* alphay




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:alpha_b |
| native | acc:alpha_b |
| close | pals:alpha_b |




## LinkML Source

<details>
```yaml
name: alpha_b
description: Twiss alpha parameter in the vertical plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- alpha_y
- alphay
close_mappings:
- pals:alpha_b
rank: 1000
alias: alpha_b
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float

```
</details>