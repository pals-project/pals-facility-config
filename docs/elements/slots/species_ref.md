

# Slot: species_ref 


_A reference to a species or particle type, such as an ion, electron, or proton._





URI: [pals_config:slot/species_ref](https://w3id.org/pals-config/slot/species_ref)
Alias: species_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceParamGroup](../classes/ReferenceParamGroup.md) | Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:species_ref |
| native | pals_config:species_ref |
| close | pals:species_ref |




## LinkML Source

<details>
```yaml
name: species_ref
description: A reference to a species or particle type, such as an ion, electron,
  or proton.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:species_ref
rank: 1000
alias: species_ref
owner: ReferenceParamGroup
domain_of:
- ReferenceParamGroup
range: string

```
</details>