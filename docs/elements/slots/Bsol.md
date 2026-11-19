

# Slot: Bsol 


_Solenoid field._





URI: [pals_config:slot/Bsol](https://w3id.org/pals-config/slot/Bsol)
Alias: Bsol

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SolenoidParamGroup](../classes/SolenoidParamGroup.md) | Mixin for solenoid-specific parameters. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [SolenoidParamGroup](../classes/SolenoidParamGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SolenoidParamGroup](../classes/SolenoidParamGroup.md) |


<details>
<summary>Additional Constraints</summary>
**Unit:** `T`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:Bsol |
| native | pals_config:Bsol |
| close | pals:Bsol |




## LinkML Source

<details>
```yaml
name: Bsol
description: Solenoid field.
from_schema: https://w3id.org/pals-config
close_mappings:
- pals:Bsol
rank: 1000
alias: Bsol
owner: SolenoidParamGroup
domain_of:
- SolenoidParamGroup
range: float
unit:
  ucum_code: T

```
</details>