

# Slot: additional_metadata 


_Additional metadata or annotations for the instance._





URI: [pals:slot/additional_metadata](https://pals-project.readthedocs.io/slot/additional_metadata)
Alias: additional_metadata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetaParamGroup](../classes/MetaParamGroup.md) | Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AdditionalMetadata](../classes/AdditionalMetadata.md) |
| Domain Of | [MetaParamGroup](../classes/MetaParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | pals:additional_metadata |
| native | pals:additional_metadata |




## LinkML Source

<details>
```yaml
name: additional_metadata
description: Additional metadata or annotations for the instance.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: additional_metadata
owner: MetaParamGroup
domain_of:
- MetaParamGroup
range: AdditionalMetadata
multivalued: true
inlined: true
inlined_as_list: true

```
</details>