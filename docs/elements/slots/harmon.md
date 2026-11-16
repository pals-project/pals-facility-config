

# Slot: harmon 


_RF harmonic number._





URI: [pals_config:slot/harmon](https://w3id.org/pals-config/slot/harmon)
Alias: harmon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RFParamGroup](../classes/RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [RFParamGroup](../classes/RFParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RFParamGroup](../classes/RFParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:harmon |
| native | pals_config:harmon |
| close | pals:harmon |




## LinkML Source

<details>
```yaml
name: harmon
description: RF harmonic number.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:harmon
rank: 1000
alias: harmon
owner: RFParamGroup
domain_of:
- RFParamGroup
range: integer

```
</details>