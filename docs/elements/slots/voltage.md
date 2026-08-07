

# Slot: voltage 


_RF voltage._





URI: [pals:voltage](https://pals-project.readthedocs.io/voltage)
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
| Slot URI | [pals:voltage](https://pals-project.readthedocs.io/voltage) |

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
| self | pals:voltage |
| native | pals:voltage |




## LinkML Source

<details>
```yaml
name: voltage
description: RF voltage.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:voltage
alias: voltage
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float

```
</details>