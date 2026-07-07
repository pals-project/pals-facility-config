
# Class: BodyShiftP

Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [narad:BodyShiftP](https://example.org/narad/BodyShiftP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent]uses%20-.->[BodyShiftP&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F],[RadiationMonitor]uses%20-.->[BodyShiftP],[Magnet]uses%20-.->[BodyShiftP],[Cavity]uses%20-.->[BodyShiftP],[BookkeepingComponent]uses%20-.->[BodyShiftP],[BeamPositionMonitor]uses%20-.->[BodyShiftP],[SupportingFacilityComponent],[RadiationMonitor],[Magnet],[Cavity],[BookkeepingComponent],[BeamPositionMonitor])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent]uses%20-.->[BodyShiftP&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F],[RadiationMonitor]uses%20-.->[BodyShiftP],[Magnet]uses%20-.->[BodyShiftP],[Cavity]uses%20-.->[BodyShiftP],[BookkeepingComponent]uses%20-.->[BodyShiftP],[BeamPositionMonitor]uses%20-.->[BodyShiftP],[SupportingFacilityComponent],[RadiationMonitor],[Magnet],[Cavity],[BookkeepingComponent],[BeamPositionMonitor])

## Mixin for

 * [BeamPositionMonitor](BeamPositionMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam position.
 * [BookkeepingComponent](BookkeepingComponent.md) (mixin)  - A virtual component that represents a bookkeeping or organizational role in the accelerator system,
 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Magnet](Magnet.md) (mixin)  - An accelerator device that produces a magnetic field for beam control.
 * [RadiationMonitor](RadiationMonitor.md) (mixin)  - A diagnostic device used to monitor radiation dose or dose rate.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) (mixin)  - A physical component that supports accelerator operation

## Referenced by Class


## Attributes


### Own

 * [➞x_offset](bodyShiftP__x_offset.md)  <sub>0..1</sub>
     * Description: Shift in the X direction in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞y_offset](bodyShiftP__y_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Y direction in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞z_offset](bodyShiftP__z_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Z direction in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞x_rot](bodyShiftP__x_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞y_rot](bodyShiftP__y_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞z_rot](bodyShiftP__z_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:BodyShiftP |
