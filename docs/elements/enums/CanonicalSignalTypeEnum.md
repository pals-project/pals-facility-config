# Enum: CanonicalSignalTypeEnum 




_Portable semantic meanings for important signals._



URI: [pals:enum/CanonicalSignalTypeEnum](https://pals-project.readthedocs.io/enum/CanonicalSignalTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HorizontalBeamPosition | None | Horizontal beam position signal. |
| VerticalBeamPosition | None | Vertical beam position signal. |
| HorizontalBeamPositionOffset | None | Horizontal beam position offset signal. |
| VerticalBeamPositionOffset | None | Vertical beam position offset signal. |
| BeamIntensity | None | Beam intensity or current signal. |
| DeviceStatus | None | Device status signal. |
| GradientSetpoint | None | Cavity accelerating gradient setpoint signal. |
| GradientReadback | None | Cavity accelerating gradient readback signal. |
| MagnetCurrentSetpoint | None | Magnet current setpoint signal. |
| MagnetCurrentReadback | None | Magnet current readback signal. |
| MagnetFieldSetpoint | None | Magnet field setpoint signal. |
| IntegratedFieldSetpoint | None | Integrated magnetic field setpoint signal. |
| IntegratedFieldReadback | None | Integrated magnetic field readback signal. |
| VacuumPressure | None | Vacuum pressure signal. |
| IonPumpCurrent | None | Ion pump current signal. |
| IonPumpVoltage | None | Ion pump voltage signal. |
| GammaDoseRate | None | Gamma radiation dose-rate signal. |
| NeutronDoseRate | None | Neutron radiation dose-rate signal. |
| Status | None | Generic status signal for a device. |




## Slots

| Name | Description |
| ---  | --- |
| [canonical_signal_type](../slots/canonical_signal_type.md) | The canonical semantic meaning of the signal. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: CanonicalSignalTypeEnum
description: Portable semantic meanings for important signals.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  HorizontalBeamPosition:
    text: HorizontalBeamPosition
    description: Horizontal beam position signal.
  VerticalBeamPosition:
    text: VerticalBeamPosition
    description: Vertical beam position signal.
  HorizontalBeamPositionOffset:
    text: HorizontalBeamPositionOffset
    description: Horizontal beam position offset signal.
  VerticalBeamPositionOffset:
    text: VerticalBeamPositionOffset
    description: Vertical beam position offset signal.
  BeamIntensity:
    text: BeamIntensity
    description: Beam intensity or current signal.
  DeviceStatus:
    text: DeviceStatus
    description: Device status signal.
  GradientSetpoint:
    text: GradientSetpoint
    description: Cavity accelerating gradient setpoint signal.
  GradientReadback:
    text: GradientReadback
    description: Cavity accelerating gradient readback signal.
  MagnetCurrentSetpoint:
    text: MagnetCurrentSetpoint
    description: Magnet current setpoint signal.
  MagnetCurrentReadback:
    text: MagnetCurrentReadback
    description: Magnet current readback signal.
  MagnetFieldSetpoint:
    text: MagnetFieldSetpoint
    description: Magnet field setpoint signal.
  IntegratedFieldSetpoint:
    text: IntegratedFieldSetpoint
    description: Integrated magnetic field setpoint signal.
  IntegratedFieldReadback:
    text: IntegratedFieldReadback
    description: Integrated magnetic field readback signal.
  VacuumPressure:
    text: VacuumPressure
    description: Vacuum pressure signal.
  IonPumpCurrent:
    text: IonPumpCurrent
    description: Ion pump current signal.
  IonPumpVoltage:
    text: IonPumpVoltage
    description: Ion pump voltage signal.
  GammaDoseRate:
    text: GammaDoseRate
    description: Gamma radiation dose-rate signal.
  NeutronDoseRate:
    text: NeutronDoseRate
    description: Neutron radiation dose-rate signal.
  Status:
    text: Status
    description: Generic status signal for a device.

```
</details>