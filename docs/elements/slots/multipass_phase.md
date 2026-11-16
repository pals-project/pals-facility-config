

# Slot: multipass_phase 


_rad/2pi RF Phase added to multipass elements_





URI: [pals_config:slot/multipass_phase](https://w3id.org/pals-config/slot/multipass_phase)
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
| self | pals_config:multipass_phase |
| native | pals_config:multipass_phase |
| close | pals:multipass_phase |




## LinkML Source

<details>
```yaml
name: multipass_phase
description: rad/2pi RF Phase added to multipass elements
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:multipass_phase
rank: 1000
alias: multipass_phase
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float

```
</details>