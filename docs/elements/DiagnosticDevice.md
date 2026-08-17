
# Class: DiagnosticDevice

An accelerator device used to measure beam or machine state.

URI: [pals:DiagnosticDevice](https://pals-project.readthedocs.io/DiagnosticDevice)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor],[PhysicalComponent],[MetaParamGroup],[LongitudinalPlacementParamGroup],[FloorParamGroup],[DiagnosticDevice&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]^-[RadiationMonitor],[DiagnosticDevice]^-[BeamProfileMonitor],[DiagnosticDevice]^-[BeamPositionMonitor],[DiagnosticDevice]^-[Aperture],[PhysicalComponent]^-[DiagnosticDevice],[BeamProfileMonitor],[BeamPositionMonitor],[Aperture])](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor],[PhysicalComponent],[MetaParamGroup],[LongitudinalPlacementParamGroup],[FloorParamGroup],[DiagnosticDevice&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]^-[RadiationMonitor],[DiagnosticDevice]^-[BeamProfileMonitor],[DiagnosticDevice]^-[BeamPositionMonitor],[DiagnosticDevice]^-[Aperture],[PhysicalComponent]^-[DiagnosticDevice],[BeamProfileMonitor],[BeamPositionMonitor],[Aperture])

## Parents

 *  is_a: [PhysicalComponent](PhysicalComponent.md) - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.

## Children

 * [Aperture](Aperture.md) - A diagnostic or limiting aperture element used to constrain or characterize beam passage.
 * [BeamPositionMonitor](BeamPositionMonitor.md) - A diagnostic device used to measure transverse beam position.
 * [BeamProfileMonitor](BeamProfileMonitor.md) - A diagnostic device used to measure transverse beam profile.
 * [RadiationMonitor](RadiationMonitor.md) - A diagnostic device used to monitor radiation dose or dose rate.

## Referenced by Class


## Attributes


### Inherited from PhysicalComponent:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [kind](kind.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [alias](alias.md)  <sub>0..\*</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞functions](physicalComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the physical component,  which can be used to identify the component across different source systems.
     * Range: [PhysicalFunctionEnum](PhysicalFunctionEnum.md)
 * [➞beamline_relation](physicalComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the physical component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [PhysicalRelationEnum](PhysicalRelationEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Instrument |
