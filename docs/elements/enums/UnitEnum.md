# Enum: UnitEnum 




_Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available._



URI: [acc:enum/UnitEnum](https://example.org/accelerator-core/enum/UnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| A | None | ampere |
| degree | None | degree |
| eV | None | electron volt |
| eV_per_c | None | momentum in electron volts per speed of light |
| eV_per_c2 | None | mass in electron volts per speed of light squared |
| fundamental_charge | None | fundamental charge |
| Gauss | None | gauss (magnetic flux density) |
| G_cm | None | gauss centimeter, a magnetic field integral. 1 G.cm = 1e-6 T.m |
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
| [distance_unit](../slots/distance_unit.md) | Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship. |
| [tolerance_unit](../slots/tolerance_unit.md) | Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship. |
| [native_unit](../slots/native_unit.md) | The native unit of the signal in the source system. |










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
    exact_mappings:
    - qudt:A
  degree:
    text: degree
    description: degree
    exact_mappings:
    - qudt:DEG
  eV:
    text: eV
    description: electron volt
    exact_mappings:
    - qudt:EV
  eV_per_c:
    text: eV_per_c
    description: momentum in electron volts per speed of light
  eV_per_c2:
    text: eV_per_c2
    description: mass in electron volts per speed of light squared
  fundamental_charge:
    text: fundamental_charge
    description: fundamental charge
  Gauss:
    text: Gauss
    description: gauss (magnetic flux density)
  G_cm:
    text: G_cm
    description: gauss centimeter, a magnetic field integral. 1 G.cm = 1e-6 T.m
    unit:
      ucum_code: G.cm
  Hz:
    text: Hz
    description: hertz
    exact_mappings:
    - qudt:HZ
  kW:
    text: kW
    description: kilowatt
    related_mappings:
    - qudt:KiloW
  m:
    text: m
    description: meter
    exact_mappings:
    - qudt:M
  mm:
    text: mm
    description: millimeter
    exact_mappings:
    - qudt:MilliM
  mrem_per_h:
    text: mrem_per_h
    description: millirem per hour. Kept as a local accelerator unit value because
      QUDT publishes related radiation units but no exact millirem-per-hour unit in
      the checked vocabulary.
    exact_mappings:
    - qudt:MREM-PER-H
  MV_per_m:
    text: MV_per_m
    description: megavolt per meter
    exact_mappings:
    - qudt:MegaV-PER-M
  PA:
    text: PA
    description: pascal
    exact_mappings:
    - qudt:PA
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
    exact_mappings:
    - qudt:SEC
  T:
    text: T
    description: tesla
    exact_mappings:
    - qudt:T
  T_M:
    text: T_M
    description: tesla meter
    exact_mappings:
    - qudt:T-M
  Torr:
    text: Torr
    description: torr
    exact_mappings:
    - qudt:TORR
  V:
    text: V
    description: volt
    exact_mappings:
    - qudt:V
  V_per_m:
    text: V_per_m
    description: volt per meter
    exact_mappings:
    - qudt:V-PER-M
  unitless:
    text: unitless
    description: dimensionless numeric value
    exact_mappings:
    - qudt:NUM
  none:
    text: none
    description: no unit or not applicable

```
</details>