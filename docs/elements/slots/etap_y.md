

# Slot: etap_y 


_Twiss dispersion slope parameter in the vertical plane._





URI: [pals_config:slot/etap_y](https://w3id.org/pals-config/slot/etap_y)
Alias: etap_y

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
**Unit:** `1` (dimensionless)

</details>








## Aliases


* etapy




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:etap_y |
| native | pals_config:etap_y |
| close | pals:etap_y |




## LinkML Source

<details>
```yaml
name: etap_y
description: Twiss dispersion slope parameter in the vertical plane.
from_schema: https://w3id.org/pals-config
aliases:
- etapy
close_mappings:
- pals:etap_y
rank: 1000
alias: etap_y
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
unit:
  descriptive_name: dimensionless
  ucum_code: '1'

```
</details>