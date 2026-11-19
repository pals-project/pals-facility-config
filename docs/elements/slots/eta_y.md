

# Slot: eta_y 


_Twiss dispersion parameter in the vertical plane. May be any real value._





URI: [pals_config:slot/eta_y](https://w3id.org/pals-config/slot/eta_y)
Alias: eta_y

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


* etay




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:eta_y |
| native | pals_config:eta_y |
| close | pals:eta_y |




## LinkML Source

<details>
```yaml
name: eta_y
description: Twiss dispersion parameter in the vertical plane. May be any real value.
from_schema: https://w3id.org/pals-config
aliases:
- etay
close_mappings:
- pals:eta_y
rank: 1000
alias: eta_y
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
unit:
  ucum_code: m

```
</details>