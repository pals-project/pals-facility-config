

# Slot: E_tot_ref 


_[eV] Reference total energy_





URI: [pals_config:slot/E_tot_ref](https://w3id.org/pals-config/slot/E_tot_ref)
Alias: E_tot_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceParamGroup](../classes/ReferenceParamGroup.md) | Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `eV`

</details>








## Aliases


* ETotal




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:E_tot_ref |
| native | pals_config:E_tot_ref |
| close | pals:E_tot_ref |




## LinkML Source

<details>
```yaml
name: E_tot_ref
description: '[eV] Reference total energy'
from_schema: https://w3id.org/pals-config
aliases:
- ETotal
close_mappings:
- pals:E_tot_ref
rank: 1000
alias: E_tot_ref
owner: ReferenceParamGroup
domain_of:
- ReferenceParamGroup
range: float
unit:
  ucum_code: eV

```
</details>