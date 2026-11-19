

# Slot: cavity_type 


_Cavity type_





URI: [pals_config:slot/cavity_type](https://w3id.org/pals-config/slot/cavity_type)
Alias: cavity_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RFParamGroup](../classes/RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CavityTypeEnum](../enums/CavityTypeEnum.md) |
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
| self | pals_config:cavity_type |
| native | pals_config:cavity_type |
| close | pals:cavity_type |




## LinkML Source

<details>
```yaml
name: cavity_type
description: Cavity type
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:cavity_type
rank: 1000
alias: cavity_type
owner: RFParamGroup
domain_of:
- RFParamGroup
range: CavityTypeEnum

```
</details>