

# Slot: phase 


_RF phase. rad/2pi RF phase in 0 to 2*pi_





URI: [acc:slot/phase](https://example.org/accelerator-core/slot/phase)
Alias: phase

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












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:phase |
| native | acc:phase |
| close | pals:phase |




## LinkML Source

<details>
```yaml
name: phase
description: RF phase. rad/2pi RF phase in 0 to 2*pi
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:phase
rank: 1000
alias: phase
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float

```
</details>