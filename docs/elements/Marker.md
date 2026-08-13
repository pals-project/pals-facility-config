
# Class: Marker

A virtual component used as a reference point or marker in the beamline structure.

URI: [pals:Marker](https://pals-project.readthedocs.io/Marker)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[MetaParamGroup],[Marker&#124;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasTwissP],[BookkeepingComponent]^-[Marker],[HasTwissP],[FloorParamGroup],[BookkeepingComponent],[BodyShiftParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[MetaParamGroup],[Marker&#124;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasTwissP],[BookkeepingComponent]^-[Marker],[HasTwissP],[FloorParamGroup],[BookkeepingComponent],[BodyShiftParamGroup])

## Parents

 *  is_a: [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.

## Uses Mixin

 *  mixin: [HasTwissP](HasTwissP.md)

## Attributes


### Inherited from BookkeepingComponent:

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
 * [➞functions](virtualComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the virtual component,  which can be used to identify the component across different source systems.
     * Range: [VirtualFunctionEnum](VirtualFunctionEnum.md)
 * [➞beamline_relation](virtualComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [VirtualRelationEnum](VirtualRelationEnum.md)

### Mixed in from HasTwissP:

 * [➞TwissP](hasTwissP__TwissP.md)  <sub>0..1</sub>
     * Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [TwissParamGroup](TwissParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:Marker |
