

# Slot: SolenoidP 


_A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals_config:slot/SolenoidP](https://w3id.org/pals-config/slot/SolenoidP)
Alias: SolenoidP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasSolenoidP](../classes/HasSolenoidP.md) |  |  no  |
| [Solenoid](../classes/Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing.<br>A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SolenoidParamGroup](../classes/SolenoidParamGroup.md) |
| Domain Of | [HasSolenoidP](../classes/HasSolenoidP.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HasSolenoidP](../classes/HasSolenoidP.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:SolenoidP |
| native | pals_config:SolenoidP |




## LinkML Source

<details>
```yaml
name: SolenoidP
description: A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP
  (Solenoid Parameters) for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/pals-config
rank: 1000
alias: SolenoidP
owner: HasSolenoidP
domain_of:
- HasSolenoidP
range: SolenoidParamGroup
inlined: true

```
</details>