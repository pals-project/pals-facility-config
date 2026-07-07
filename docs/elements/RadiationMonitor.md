
# Class: RadiationMonitor

A diagnostic device used to monitor radiation dose or dose rate.

URI: [narad:RadiationMonitor](https://example.org/narad/RadiationMonitor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;function(i):PhysicalFunctionEnum;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[BodyShiftP],[DiagnosticDevice]^-[RadiationMonitor],[MetadataEntry],[DiagnosticDevice],[BodyShiftP])](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;function(i):PhysicalFunctionEnum;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[BodyShiftP],[DiagnosticDevice]^-[RadiationMonitor],[MetadataEntry],[DiagnosticDevice],[BodyShiftP])

## Parents

 *  is_a: [DiagnosticDevice](DiagnosticDevice.md) - An accelerator device used to measure beam or machine state.

## Uses Mixin

 *  mixin: [BodyShiftP](BodyShiftP.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

## Attributes


### Inherited from DiagnosticDevice:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞function](physicalComponent__function.md)  <sub>1..1</sub>
     * Description: The function of the physical component,  which can be used to identify the component across different source systems.
     * Range: [PhysicalFunctionEnum](PhysicalFunctionEnum.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

### Mixed in from BodyShiftP:

 * [➞x_offset](bodyShiftP__x_offset.md)  <sub>0..1</sub>
     * Description: Shift in the X direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞y_offset](bodyShiftP__y_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Y direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞z_offset](bodyShiftP__z_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Z direction in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞x_rot](bodyShiftP__x_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞y_rot](bodyShiftP__y_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from BodyShiftP:

 * [➞z_rot](bodyShiftP__z_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Instrument |
