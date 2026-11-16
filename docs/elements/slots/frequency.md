

# Slot: frequency 


_RF frequency._





URI: [pals_config:slot/frequency](https://w3id.org/pals-config/slot/frequency)
Alias: frequency

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
**Unit:** `Hz`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:frequency |
| native | pals_config:frequency |
| close | pals:frequency |




## LinkML Source

<details>
```yaml
name: frequency
description: RF frequency.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:frequency
rank: 1000
alias: frequency
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float
unit:
  ucum_code: Hz

```
</details>