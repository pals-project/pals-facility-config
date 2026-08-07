# Enum: UnitEnum 




_Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available._



URI: [pals:enum/UnitEnum](https://pals-project.readthedocs.io/enum/UnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| A | None | ampere |
| degree | None | degree |
| eV | None | electron volt |
| eV_per_c | None | momentum in electron volts per speed of light |
| eV_per_c2 | None | mass in electron volts per speed of light squared |
| fundamental_charge | None | fundamental charge |
| G_per_cm | None | gauss per centimeter |
| Hz | None | hertz |
| kW | None | kilowatt |
| m | None | meter |
| mm | None | millimeter |
| mrem_per_h | None | millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary. |
| MV_per_m | None | megavolt per meter |
| PA | None | pascal |
| randians_pi2 | None | radians divided by 2 pi - angles and phases |
| rem_per_h | None | rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary. |
| seconds | None | second |
| T | None | tesla |
| T_M | None | tesla meter |
| Torr | None | torr |
| V | None | volt |
| V_per_m | None | volt per meter |
| unitless | None | dimensionless numeric value |
| none | None | no unit or not applicable |




## Slots

| Name | Description |
| ---  | --- |
| [native_unit](../slots/native_unit.md) | The native unit of the signal in the source system. |
| [distance_unit](../slots/distance_unit.md) |  |
| [tolerance_unit](../slots/tolerance_unit.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: UnitEnum
description: Engineering units using ASCII-safe enum names. Values map to QUDT unit
  IRIs with the LinkML meaning field when an exact QUDT unit is available.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  A:
    text: A
    description: ampere
  degree:
    text: degree
    description: degree
  eV:
    text: eV
    description: electron volt
  eV_per_c:
    text: eV_per_c
    description: momentum in electron volts per speed of light
  eV_per_c2:
    text: eV_per_c2
    description: mass in electron volts per speed of light squared
  fundamental_charge:
    text: fundamental_charge
    description: fundamental charge
  G_per_cm:
    text: G_per_cm
    description: gauss per centimeter
  Hz:
    text: Hz
    description: hertz
  kW:
    text: kW
    description: kilowatt
  m:
    text: m
    description: meter
  mm:
    text: mm
    description: millimeter
  mrem_per_h:
    text: mrem_per_h
    description: millirem per hour. Kept as a local accelerator unit value because
      QUDT publishes related radiation units but no exact millirem-per-hour unit in
      the checked vocabulary.
  MV_per_m:
    text: MV_per_m
    description: megavolt per meter
  PA:
    text: PA
    description: pascal
  randians_pi2:
    text: randians_pi2
    description: radians divided by 2 pi - angles and phases
  rem_per_h:
    text: rem_per_h
    description: rem per hour. Kept as a local accelerator unit value because QUDT
      publishes rem and rem-per-second but no exact rem-per-hour unit in the checked
      vocabulary.
  seconds:
    text: seconds
    description: second
  T:
    text: T
    description: tesla
  T_M:
    text: T_M
    description: tesla meter
  Torr:
    text: Torr
    description: torr
  V:
    text: V
    description: volt
  V_per_m:
    text: V_per_m
    description: volt per meter
  unitless:
    text: unitless
    description: dimensionless numeric value
  none:
    text: none
    description: no unit or not applicable

```
</details>