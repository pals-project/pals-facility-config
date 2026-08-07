

# Slot: phase 


_RF phase. rad/2pi RF phase in 0 to 2*pi_





URI: [pals:phase](https://pals-project.readthedocs.io/phase)
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
| Slot URI | [pals:phase](https://pals-project.readthedocs.io/phase) |

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
| self | pals:phase |
| native | pals:phase |




## LinkML Source

<details>
```yaml
name: phase
description: RF phase. rad/2pi RF phase in 0 to 2*pi
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:phase
alias: phase
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float

```
</details>