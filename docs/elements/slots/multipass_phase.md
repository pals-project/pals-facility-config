

# Slot: multipass_phase 


_rad/2pi RF Phase added to multipass elements_





URI: [pals:multipass_phase](https://pals-project.readthedocs.io/multipass_phase)
Alias: multipass_phase

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
| Slot URI | [pals:multipass_phase](https://pals-project.readthedocs.io/multipass_phase) |

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
| self | pals:multipass_phase |
| native | pals:multipass_phase |




## LinkML Source

<details>
```yaml
name: multipass_phase
description: rad/2pi RF Phase added to multipass elements
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:multipass_phase
alias: multipass_phase
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float

```
</details>