# Enum: QuantityKindEnum 




_Physical quantity kinds for signals._



URI: [acc:enum/QuantityKindEnum](https://example.org/accelerator-core/enum/QuantityKindEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| BeamPosition | None | Beam transverse position. |
| State | None | Device state or condition. |
| ElectricCurrent | None | Electric current. |
| IntegratedMagneticField | None | Integrated magnetic field. |
| IntegratedMagneticFieldGradient | None | Integrated magnetic field gradient. |
| MagneticField | None | Magnetic field. |
| Pressure | None | Gas or vacuum pressure. |
| DoseRate | None | Radiation dose rate. |
| Voltage | None | Electric potential difference. |
| Power | None | Power. |
| CavityPhase | None | Cavity phase. |
| CavityGradient | None | Cavity accelerating gradient. |




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
    exact_mappings:
    - sosa:ObservableProperty
  ElectricCurrent:
    text: ElectricCurrent
    description: Electric current.
    exact_mappings:
    - quantitykind:ElectricCurrent
  IntegratedMagneticField:
    text: IntegratedMagneticField
    description: Integrated magnetic field.
    exact_mappings:
    - quantitykind:MagneticFluxPerLength
  IntegratedMagneticFieldGradient:
    text: IntegratedMagneticFieldGradient
    description: Integrated magnetic field gradient.
  MagneticField:
    text: MagneticField
    description: Magnetic field.
    exact_mappings:
    - quantitykind:MagneticFluxDensity
  Pressure:
    text: Pressure
    description: Gas or vacuum pressure.
    exact_mappings:
    - quantitykind:Pressure
  DoseRate:
    text: DoseRate
    description: Radiation dose rate.
    exact_mappings:
    - quantitykind:AbsorbedDoseRate
  Voltage:
    text: Voltage
    description: Electric potential difference.
    exact_mappings:
    - quantitykind:Voltage
  Power:
    text: Power
    description: Power.
    exact_mappings:
    - quantitykind:Power
  CavityPhase:
    text: CavityPhase
    description: Cavity phase.
    exact_mappings:
    - quantitykind:PhaseAngle
  CavityGradient:
    text: CavityGradient
    description: Cavity accelerating gradient.
    exact_mappings:
    - quantitykind:ElectricFieldStrength

```
</details>