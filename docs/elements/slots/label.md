

# Slot: label 


_A label string._





URI: [acc:slot/label](https://example.org/accelerator-core/slot/label)
Alias: label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetaParamGroup](../classes/MetaParamGroup.md) | Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [MetaParamGroup](../classes/MetaParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MetaParamGroup](../classes/MetaParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:label |
| native | acc:label |
| close | pals:label |




## LinkML Source

<details>
```yaml
name: label
description: A label string.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:label
rank: 1000
alias: label
owner: MetaParamGroup
domain_of:
- MetaParamGroup
range: string

```
</details>