
# Class: Solenoid

A magnet with a primarily longitudinal magnetic field used for focusing.
A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis.

URI: [pals:Solenoid](https://pals-project.readthedocs.io/Solenoid)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[SolenoidParamGroup],[Solenoid&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasSolenoidP],[Magnet]^-[Solenoid],[ReferenceParamGroup],[MetaParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[HasSolenoidP],[FloorParamGroup],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[SolenoidParamGroup],[Solenoid&#124;functions(i):PhysicalFunctionEnum%20%2B;beamline_relation(i):PhysicalRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasSolenoidP],[Magnet]^-[Solenoid],[ReferenceParamGroup],[MetaParamGroup],[Magnet],[LongitudinalPlacementParamGroup],[HasSolenoidP],[FloorParamGroup],[BodyShiftParamGroup])

## Parents

 *  is_a: [Magnet](Magnet.md) - An accelerator device that produces a magnetic field for beam control.

## Uses Mixin

 *  mixin: [HasSolenoidP](HasSolenoidP.md)

## Attributes


### Inherited from Magnet:

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

### Mixed in from HasSolenoidP:

 * [➞SolenoidP](hasSolenoidP__SolenoidP.md)  <sub>0..1</sub>
     * Description: A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [SolenoidParamGroup](SolenoidParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:Solenoid |
