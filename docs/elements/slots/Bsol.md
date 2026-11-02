

# Slot: Bsol 


_Solenoid field._





URI: [acc:slot/Bsol](https://example.org/accelerator-core/slot/Bsol)
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


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:Bsol |
| native | acc:Bsol |
| close | pals:Bsol |




## LinkML Source

<details>
```yaml
name: Bsol
description: Solenoid field.
from_schema: https://w3id.org/accelerator-core
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