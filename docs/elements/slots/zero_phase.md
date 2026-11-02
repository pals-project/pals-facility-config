

# Slot: zero_phase 


_Sets what phase = 0 means._





URI: [acc:slot/zero_phase](https://example.org/accelerator-core/slot/zero_phase)
Alias: zero_phase

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RFParamGroup](../classes/RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ZeroPhaseEnum](../enums/ZeroPhaseEnum.md) |
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
| self | acc:zero_phase |
| native | acc:zero_phase |
| close | pals:zero_phase |




## LinkML Source

<details>
```yaml
name: zero_phase
description: Sets what phase = 0 means.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:zero_phase
rank: 1000
alias: zero_phase
owner: RFParamGroup
domain_of:
- RFParamGroup
range: ZeroPhaseEnum

```
</details>