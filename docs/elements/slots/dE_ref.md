

# Slot: dE_ref 


_Reference energy gain._





URI: [pals_config:slot/dE_ref](https://w3id.org/pals-config/slot/dE_ref)
Alias: dE_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RFParamGroup](../classes/RFParamGroup.md) | Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [RFParamGroup](../classes/RFParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RFParamGroup](../classes/RFParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `eV`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:dE_ref |
| native | pals_config:dE_ref |
| close | pals:dE_ref |




## LinkML Source

<details>
```yaml
name: dE_ref
description: Reference energy gain.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:dE_ref
rank: 1000
alias: dE_ref
owner: RFParamGroup
domain_of:
- RFParamGroup
range: float
unit:
  ucum_code: eV

```
</details>