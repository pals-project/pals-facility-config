
# Enum: UnitEnum

Engineering units using ASCII-safe enum names. Values map to QUDT unit IRIs with the LinkML meaning field when an exact QUDT unit is available.

URI: [narad:UnitEnum](https://example.org/narad/UnitEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| mm | millimeter | unit:MilliM |  |
| m | meter | unit:M |  |
| A | ampere | unit:A |  |
| T_m | tesla meter | unit:T-M |  |
| Pa | pascal | unit:PA |  |
| Torr | torr | unit:TORR |  |
| rem_per_h | rem per hour. Kept as a local accelerator unit value because QUDT publishes rem and rem-per-second but no exact rem-per-hour unit in the checked vocabulary. | unit:REM-PER-H |  |
| mrem_per_h | millirem per hour. Kept as a local accelerator unit value because QUDT publishes related radiation units but no exact millirem-per-hour unit in the checked vocabulary. | unit:MREM-PER-H |  |
| V | volt | unit:V |  |
| kW | kilowatt | unit:KiloW |  |
| degree | degree | unit:DEG |  |
| MV_per_m | megavolt per meter | unit:MegaV-PER-M |  |
| G_per_cm | gauss per centimeter |  |  |
| unitless | dimensionless numeric value | unit:NUM |  |
| none | no unit or not applicable |  |  |
