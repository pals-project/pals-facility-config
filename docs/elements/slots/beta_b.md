

# Slot: beta_b 


_Twiss beta parameter in the vertical plane. Must be strictly positive (> 0)._





URI: [pals_config:slot/beta_b](https://w3id.org/pals-config/slot/beta_b)
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

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TwissParamGroup](../classes/TwissParamGroup.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |


<details>
<summary>Additional Constraints</summary>
**Unit:** `m`

</details>

<details>
<summary>Expressions & Logic</summary>
#### None Of

Value must not satisfy any of:
- AnonymousSlotExpression({'equals_number': 0})

</details>








## Aliases


* beta_y
* betay




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:beta_b |
| native | pals_config:beta_b |
| close | pals:beta_b |




## LinkML Source

<details>
```yaml
name: beta_b
description: Twiss beta parameter in the vertical plane. Must be strictly positive
  (> 0).
from_schema: https://w3id.org/pals-config
aliases:
- beta_y
- betay
close_mappings:
- pals:beta_b
rank: 1000
alias: beta_b
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
minimum_value: 0
unit:
  ucum_code: m
none_of:
- equals_number: 0

```
</details>