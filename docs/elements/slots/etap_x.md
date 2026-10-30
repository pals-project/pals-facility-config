

# Slot: etap_x 


_Twiss dispersion slope parameter in the horizontal plane._





URI: [acc:slot/etap_x](https://example.org/accelerator-core/slot/etap_x)
Alias: etap_x

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


* etapx




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:etap_x |
| native | acc:etap_x |
| close | pals:etap_x |




## LinkML Source

<details>
```yaml
name: etap_x
description: Twiss dispersion slope parameter in the horizontal plane.
from_schema: https://w3id.org/accelerator-core
aliases:
- etapx
close_mappings:
- pals:etap_x
rank: 1000
alias: etap_x
owner: TwissParamGroup
domain_of:
- TwissParamGroup
range: float
unit:
  descriptive_name: dimensionless
  ucum_code: '1'

```
</details>