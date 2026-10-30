

# Slot: phi_b 


_Twiss phase advance parameter in the vertical plane._





URI: [acc:slot/phi_b](https://example.org/accelerator-core/slot/phi_b)
Alias: phi_b

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


<details>
<summary>Additional Constraints</summary>
**Unit:** `rad`

</details>








## Aliases


* phi_y
* phiy
* psi_y
* psiy




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:phi_b |
| native | acc:phi_b |
| close | pals:phi_b |




## LinkML Source

<details>
```yaml
name: phi_b
description: Twiss phase advance parameter in the vertical plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- phi_y
- phiy
- psi_y
- psiy
close_mappings:
- pals:phi_b
rank: 1000
alias: phi_b
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
unit:
  ucum_code: rad

```
</details>