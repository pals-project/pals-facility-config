

# Slot: num_cells 


_Number of cells in the cavity_





URI: [pals_config:slot/num_cells](https://w3id.org/pals-config/slot/num_cells)
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
| self | pals_config:num_cells |
| native | pals_config:num_cells |
| close | pals:num_cells |




## LinkML Source

<details>
```yaml
name: num_cells
description: Number of cells in the cavity
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:num_cells
rank: 1000
alias: num_cells
owner: RFParamGroup
domain_of:
- RFParamGroup
range: integer

```
</details>