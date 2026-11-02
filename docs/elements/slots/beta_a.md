

# Slot: beta_a 


_Twiss beta parameter in the horizontal plane. Must be strictly positive (> 0)._





URI: [acc:slot/beta_a](https://example.org/accelerator-core/slot/beta_a)
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


* beta_x
* betax




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:beta_a |
| native | acc:beta_a |
| close | pals:beta_a |




## LinkML Source

<details>
```yaml
name: beta_a
description: Twiss beta parameter in the horizontal plane. Must be strictly positive
  (> 0).
from_schema: https://w3id.org/accelerator-core
aliases:
- beta_x
- betax
close_mappings:
- pals:beta_a
rank: 1000
alias: beta_a
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