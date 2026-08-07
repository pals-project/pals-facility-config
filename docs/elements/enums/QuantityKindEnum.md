# Enum: QuantityKindEnum 




_Physical quantity kinds for signals._



URI: [pals:enum/QuantityKindEnum](https://pals-project.readthedocs.io/enum/QuantityKindEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| BeamPosition | None | Beam transverse position. |
| State | sosa:ObservableProperty | Device state or condition. |
| ElectricCurrent | quantitykind:ElectricCurrent | Electric current. |
| IntegratedMagneticField | quantitykind:MagneticFluxPerLength | Integrated magnetic field. |
| MagneticField | quantitykind:MagneticFluxDensity | Magnetic field. |
| Pressure | quantitykind:Pressure | Gas or vacuum pressure. |
| DoseRate | quantitykind:AbsorbedDoseRate | Radiation dose rate. |
| Voltage | quantitykind:Voltage | Electric potential difference. |
| Power | quantitykind:Power | Power. |
| CavityPhase | quantitykind:PhaseAngle | Cavity phase. |
| CavityGradient | quantitykind:ElectricFieldStrength | Cavity accelerating gradient. |




## Slots

| Name | Description |
| ---  | --- |
| [quantity_kind](../slots/quantity_kind.md) | The physical quantity kind of the signal. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: QuantityKindEnum
description: Physical quantity kinds for signals.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  BeamPosition:
    text: BeamPosition
    description: Beam transverse position.
  State:
    text: State
    description: Device state or condition.
    meaning: sosa:ObservableProperty
  ElectricCurrent:
    text: ElectricCurrent
    description: Electric current.
    meaning: quantitykind:ElectricCurrent
  IntegratedMagneticField:
    text: IntegratedMagneticField
    description: Integrated magnetic field.
    meaning: quantitykind:MagneticFluxPerLength
  MagneticField:
    text: MagneticField
    description: Magnetic field.
    meaning: quantitykind:MagneticFluxDensity
  Pressure:
    text: Pressure
    description: Gas or vacuum pressure.
    meaning: quantitykind:Pressure
  DoseRate:
    text: DoseRate
    description: Radiation dose rate.
    meaning: quantitykind:AbsorbedDoseRate
  Voltage:
    text: Voltage
    description: Electric potential difference.
    meaning: quantitykind:Voltage
  Power:
    text: Power
    description: Power.
    meaning: quantitykind:Power
  CavityPhase:
    text: CavityPhase
    description: Cavity phase.
    meaning: quantitykind:PhaseAngle
  CavityGradient:
    text: CavityGradient
    description: Cavity accelerating gradient.
    meaning: quantitykind:ElectricFieldStrength

```
</details>