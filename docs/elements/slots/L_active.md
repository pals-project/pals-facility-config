

# Slot: L_active 


_Active acceleration length._





URI: [pals_config:slot/L_active](https://w3id.org/pals-config/slot/L_active)
Alias: L_active

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RFParamGroup](../classes/RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [RFParamGroup](../classes/RFParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RFParamGroup](../classes/RFParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:L_active |
| native | pals_config:L_active |
| close | pals:L_active |




## LinkML Source

<details>
```yaml
name: L_active
description: Active acceleration length.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:L_active
rank: 1000
alias: L_active
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float
unit:
  ucum_code: m

```
</details>