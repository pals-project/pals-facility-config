

# Slot: num_cells 


_Number of cells in the cavity_





URI: [pals:num_cells](https://pals-project.readthedocs.io/num_cells)
Alias: num_cells

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
| Slot URI | [pals:num_cells](https://pals-project.readthedocs.io/num_cells) |

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
| self | pals:num_cells |
| native | pals:num_cells |




## LinkML Source

<details>
```yaml
name: num_cells
description: Number of cells in the cavity
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:num_cells
alias: num_cells
owner: RFParamGroup
domain_of:
- RFParamGroup
range: integer

```
</details>