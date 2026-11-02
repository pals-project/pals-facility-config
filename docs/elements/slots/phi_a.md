

# Slot: phi_a 


_Twiss phase advance parameter in the horizontal plane._





URI: [acc:slot/phi_a](https://example.org/accelerator-core/slot/phi_a)
Alias: phi_a

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


* phi_x
* phix
* psi_x
* psix




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:phi_a |
| native | acc:phi_a |
| close | pals:phi_a |




## LinkML Source

<details>
```yaml
name: phi_a
description: Twiss phase advance parameter in the horizontal plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- phi_x
- phix
- psi_x
- psix
close_mappings:
- pals:phi_a
rank: 1000
alias: phi_a
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
unit:
  ucum_code: rad

```
</details>