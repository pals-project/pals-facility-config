

# Slot: frequency 


_RF frequency._





URI: [acc:slot/frequency](https://example.org/accelerator-core/slot/frequency)
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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:frequency |
| native | acc:frequency |
| close | pals:frequency |




## LinkML Source

<details>
```yaml
name: frequency
description: RF frequency.
from_schema: https://w3id.org/accelerator-core
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