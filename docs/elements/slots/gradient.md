

# Slot: gradient 


_RF accelerating gradient._





URI: [pals_config:slot/gradient](https://w3id.org/pals-config/slot/gradient)
Alias: gradient

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
**Unit:** `V/m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:gradient |
| native | pals_config:gradient |
| close | pals:gradient |




## LinkML Source

<details>
```yaml
name: gradient
description: RF accelerating gradient.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:gradient
rank: 1000
alias: gradient
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float
unit:
  ucum_code: V/m

```
</details>