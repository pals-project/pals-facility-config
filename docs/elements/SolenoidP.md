

# Slot: SolenoidP 


_A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:SolenoidP](https://pals-project.readthedocs.io/SolenoidP)
Alias: SolenoidP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |  no  |
| [HasSolenoidP](HasSolenoidP.md) |  |  no  |






## Properties

* Range: [SolenoidParamGroup](SolenoidParamGroup.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:SolenoidP |
| native | pals:SolenoidP |




## LinkML Source

<details>
```yaml
name: SolenoidP
description: A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP
  (Solenoid Parameters) for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: SolenoidP
owner: HasSolenoidP
domain_of:
- HasSolenoidP
range: SolenoidParamGroup
inlined: true

```
</details>