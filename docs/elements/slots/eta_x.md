

# Slot: eta_x 


_Twiss dispersion parameter in the horizontal plane. May be any real value._





URI: [acc:slot/eta_x](https://example.org/accelerator-core/slot/eta_x)
Alias: eta_x

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
**Unit:** `m`

</details>








## Aliases


* etax




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:eta_x |
| native | acc:eta_x |
| close | pals:eta_x |




## LinkML Source

<details>
```yaml
name: eta_x
description: Twiss dispersion parameter in the horizontal plane. May be any real value.
from_schema: https://w3id.org/accelerator-core
aliases:
- etax
close_mappings:
- pals:eta_x
rank: 1000
alias: eta_x
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
unit:
  ucum_code: m

```
</details>