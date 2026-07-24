# Enum: UnitEnum 




_Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available._



URI: [pals:UnitEnum](https://pals-project.readthedocs.io/UnitEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| A | unit:A | ampere |
| degree | unit:DEG | degree |
| eV | unit:EV | electron volt |
| eV_per_c | None | momentum in electron volts per speed of light |
| eV_per_c2 | None | mass in electron volts per speed of light squared |
| fundamental_charge | unit:???? | fundamental charge |
| G_per_cm | None | gauss per centimeter |
| Hz | unit:HZ | hertz |
| kW | unit:KiloW | kilowatt |
| m | unit:M | meter |
| mm | unit:MilliM | millimeter |
| mrem_per_h | unit:MREM-PER-H | millirem per hour |
| MV_per_m | unit:MegaV-PER-M | megavolt per meter |
| PA | unit:PA | pascal |
| randians_pi2 | None | radians divided by 2 pi - angles and phases |
| rem_per_h | None | rem per hour |
| seconds | unit:SEC | second |
| T | unit:T | tesla |
| T_M | unit:T-M | tesla meter |
| Torr | unit:TORR | torr |
| V | unit:V | volt |
| V_per_m | unit:V-PER-M | volt per meter |
| unitless | unit:NUM | dimensionless numeric value |
| none | None | no unit or not applicable |




## Slots

| Name | Description |
| ---  | --- |
| [native_unit](native_unit.md) | The native unit of the signal in the source system |
| [distance_unit](distance_unit.md) |  |
| [tolerance_unit](tolerance_unit.md) |  |





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
    meaning: unit:A
  degree:
    text: degree
    description: degree
    meaning: unit:DEG
  eV:
    text: eV
    description: electron volt
    meaning: unit:EV
  eV_per_c:
    text: eV_per_c
    description: momentum in electron volts per speed of light
  eV_per_c2:
    text: eV_per_c2
    description: mass in electron volts per speed of light squared
  fundamental_charge:
    text: fundamental_charge
    description: fundamental charge
    meaning: unit:????
  G_per_cm:
    text: G_per_cm
    description: gauss per centimeter
  Hz:
    text: Hz
    description: hertz
    meaning: unit:HZ
  kW:
    text: kW
    description: kilowatt
    meaning: unit:KiloW
  m:
    text: m
    description: meter
    meaning: unit:M
  mm:
    text: mm
    description: millimeter
    meaning: unit:MilliM
  mrem_per_h:
    text: mrem_per_h
    description: millirem per hour. Kept as a local accelerator unit value because
      QUDT publishes related radiation units but no exact millirem-per-hour unit in
      the checked vocabulary.
    meaning: unit:MREM-PER-H
  MV_per_m:
    text: MV_per_m
    description: megavolt per meter
    meaning: unit:MegaV-PER-M
  PA:
    text: PA
    description: pascal
    meaning: unit:PA
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
    meaning: unit:SEC
  T:
    text: T
    description: tesla
    meaning: unit:T
  T_M:
    text: T_M
    description: tesla meter
    meaning: unit:T-M
  Torr:
    text: Torr
    description: torr
    meaning: unit:TORR
  V:
    text: V
    description: volt
    meaning: unit:V
  V_per_m:
    text: V_per_m
    description: volt per meter
    meaning: unit:V-PER-M
  unitless:
    text: unitless
    description: dimensionless numeric value
    meaning: unit:NUM
  none:
    text: none
    description: no unit or not applicable

```
</details>