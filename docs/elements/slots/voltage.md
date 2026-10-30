

# Slot: voltage 


_RF voltage._





URI: [acc:slot/voltage](https://example.org/accelerator-core/slot/voltage)
Alias: voltage

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
**Unit:** `V`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:voltage |
| native | acc:voltage |
| close | pals:voltage |




## LinkML Source

<details>
```yaml
name: voltage
description: RF voltage.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:voltage
rank: 1000
alias: voltage
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float
unit:
  ucum_code: V

```
</details>