
# Class: RadiationMonitor

A diagnostic device used to monitor radiation dose or dose rate.

URI: [pals:RadiationMonitor](https://pals-project.readthedocs.io/RadiationMonitor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasBodyShiftP],[DiagnosticDevice]^-[RadiationMonitor],[MetaParamGroup],[LongitudinalPlacementParamGroup],[HasBodyShiftP],[FloorParamGroup],[DiagnosticDevice],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[RadiationMonitor&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasBodyShiftP],[DiagnosticDevice]^-[RadiationMonitor],[MetaParamGroup],[LongitudinalPlacementParamGroup],[HasBodyShiftP],[FloorParamGroup],[DiagnosticDevice],[BodyShiftParamGroup])

## Parents

 *  is_a: [DiagnosticDevice](DiagnosticDevice.md) - An accelerator device used to measure beam or machine state.

## Uses Mixin

 *  mixin: [HasBodyShiftP](HasBodyShiftP.md)

## Attributes


### Inherited from DiagnosticDevice:

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

### Mixed in from HasBodyShiftP:

 * [➞BodyShiftP](hasBodyShiftP__BodyShiftP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [BodyShiftParamGroup](BodyShiftParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Instrument |
