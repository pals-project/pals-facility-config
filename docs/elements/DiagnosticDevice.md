
# Class: DiagnosticDevice

An accelerator device used to measure beam or machine state.

URI: [narad:DiagnosticDevice](https://example.org/narad/DiagnosticDevice)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor],[PhysicalComponent],[MetadataEntry],[DiagnosticDevice&#124;function(i):PhysicalFunctionEnum;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]^-[RadiationMonitor],[DiagnosticDevice]^-[BeamPositionMonitor],[PhysicalComponent]^-[DiagnosticDevice],[BeamPositionMonitor])](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor],[PhysicalComponent],[MetadataEntry],[DiagnosticDevice&#124;function(i):PhysicalFunctionEnum;beamline_relation(i):PhysicalRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;length(i):float%20%3F;s_position(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]^-[RadiationMonitor],[DiagnosticDevice]^-[BeamPositionMonitor],[PhysicalComponent]^-[DiagnosticDevice],[BeamPositionMonitor])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Children

 * [BeamPositionMonitor](BeamPositionMonitor.md) - A diagnostic device used to measure transverse beam position.
 * [RadiationMonitor](RadiationMonitor.md) - A diagnostic device used to monitor radiation dose or dose rate.

## Referenced by Class


## Attributes


### Inherited from PhysicalComponent:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Instrument |
