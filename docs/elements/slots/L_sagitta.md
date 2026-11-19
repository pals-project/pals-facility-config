

# Slot: L_sagitta 


_Output parameter. Sagitta length._





URI: [pals_config:slot/L_sagitta](https://w3id.org/pals-config/slot/L_sagitta)
Alias: L_sagitta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BendParamGroup](../classes/BendParamGroup.md) | Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [BendParamGroup](../classes/BendParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BendParamGroup](../classes/BendParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `m`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:L_sagitta |
| native | pals_config:L_sagitta |
| close | pals:L_sagitta |




## LinkML Source

<details>
```yaml
name: L_sagitta
description: Output parameter. Sagitta length.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:L_sagitta
rank: 1000
alias: L_sagitta
owner: BendParamGroup
domain_of:
- BendParamGroup
range: float
unit:
  ucum_code: m

```
</details>