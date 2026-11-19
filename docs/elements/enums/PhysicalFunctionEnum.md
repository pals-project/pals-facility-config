# Enum: PhysicalFunctionEnum 




_Broad device-level functions._



URI: [pals_config:enum/PhysicalFunctionEnum](https://w3id.org/pals-config/enum/PhysicalFunctionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Focusing | None | Focuses or defocuses the beam. |
| Steering | None | Steers the beam in a transverse plane. |
| BeamPositionMeasurement | None | Measures transverse beam position. |
| VacuumGeneration | None | Generates or maintains vacuum. |
| RadiationMonitoring | None | Monitors radiation dose or dose rate. |
| Measurement | None | Measures beam or machine state. |
| BeamAcceleration | None | Accelerates the beam. |
| BeamLossDetection | None | Detects beam loss. |
| BeamCurrentMeasurement | None | Measures beam current or intensity. |
| BeamProfileMeasurement | None | Measures beam profile. |
| MachineProtection | None | Supports machine protection. |
| TimingSynchronization | None | Supports timing or synchronization. |




## Slots

| Name | Description |
| ---  | --- |
| [functions](../slots/functions.md) | The function of the physical component,  which can be used to identify the component across different source systems. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config






## LinkML Source

<details>
```yaml
name: PhysicalFunctionEnum
description: Broad device-level functions.
from_schema: https://w3id.org/pals-config
rank: 1000
permissible_values:
  Focusing:
    text: Focusing
    description: Focuses or defocuses the beam.
  Steering:
    text: Steering
    description: Steers the beam in a transverse plane.
  BeamPositionMeasurement:
    text: BeamPositionMeasurement
    description: Measures transverse beam position.
  VacuumGeneration:
    text: VacuumGeneration
    description: Generates or maintains vacuum.
  RadiationMonitoring:
    text: RadiationMonitoring
    description: Monitors radiation dose or dose rate.
  Measurement:
    text: Measurement
    description: Measures beam or machine state.
  BeamAcceleration:
    text: BeamAcceleration
    description: Accelerates the beam.
  BeamLossDetection:
    text: BeamLossDetection
    description: Detects beam loss.
  BeamCurrentMeasurement:
    text: BeamCurrentMeasurement
    description: Measures beam current or intensity.
  BeamProfileMeasurement:
    text: BeamProfileMeasurement
    description: Measures beam profile.
  MachineProtection:
    text: MachineProtection
    description: Supports machine protection.
  TimingSynchronization:
    text: TimingSynchronization
    description: Supports timing or synchronization.

```
</details>