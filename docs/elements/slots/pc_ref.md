

# Slot: pc_ref 


_[MeV] Reference momentum times speed of light, i.e. beam momentum in MeV/c._





URI: [pals_config:slot/pc_ref](https://w3id.org/pals-config/slot/pc_ref)
Alias: pc_ref

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
**Unit:** `MeV`

</details>








## Aliases


* pCentral




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:pc_ref |
| native | pals_config:pc_ref |
| close | pals:pc_ref |




## LinkML Source

<details>
```yaml
name: pc_ref
description: '[MeV] Reference momentum times speed of light, i.e. beam momentum in
  MeV/c.'
from_schema: https://w3id.org/pals-config
aliases:
- pCentral
close_mappings:
- pals:pc_ref
rank: 1000
alias: pc_ref
owner: ReferenceParamGroup
domain_of:
- ReferenceParamGroup
range: float
unit:
  ucum_code: MeV

```
</details>