

# Slot: time_ref 


_[s] Reference time_





URI: [acc:slot/time_ref](https://example.org/accelerator-core/slot/time_ref)
Alias: time_ref

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
**Unit:** `s`

</details>








## Aliases


* tRef




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:time_ref |
| native | acc:time_ref |
| close | pals:time_ref |




## LinkML Source

<details>
```yaml
name: time_ref
description: '[s] Reference time'
from_schema: https://w3id.org/accelerator-core
aliases:
- tRef
close_mappings:
- pals:time_ref
rank: 1000
alias: time_ref
owner: ReferenceParamGroup
domain_of:
- ReferenceParamGroup
range: float
unit:
  ucum_code: s

```
</details>