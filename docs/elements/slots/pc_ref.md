

# Slot: pc_ref 


_[momentum*c] Reference momentum times speed of light._





URI: [acc:slot/pc_ref](https://example.org/accelerator-core/slot/pc_ref)
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









## Aliases


* pCentral




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:pc_ref |
| native | acc:pc_ref |
| close | pals:pc_ref |




## LinkML Source

<details>
```yaml
name: pc_ref
description: '[momentum*c] Reference momentum times speed of light.'
from_schema: https://w3id.org/accelerator-core
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

```
</details>