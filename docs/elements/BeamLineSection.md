
# Class: BeamLineSection

A virtual component used to represent a section of the BeamLine for organizational or functional grouping of components.

URI: [pals:BeamLineSection](https://pals-project.readthedocs.io/BeamLineSection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MetaParamGroup],[HasFloorP],[FloorParamGroup],[BookkeepingComponent],[BodyShiftParamGroup],[BeamLineSection&#124;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasFloorP],[BookkeepingComponent]^-[BeamLineSection])](https://yuml.me/diagram/nofunky;dir:TB/class/[MetaParamGroup],[HasFloorP],[FloorParamGroup],[BookkeepingComponent],[BodyShiftParamGroup],[BeamLineSection&#124;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*]uses%20-.->[HasFloorP],[BookkeepingComponent]^-[BeamLineSection])

## Parents

 *  is_a: [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.

## Uses Mixin

 *  mixin: [HasFloorP](HasFloorP.md)

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

### Mixed in from HasFloorP:

 * [➞FloorP](hasFloorP__FloorP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [FloorParamGroup](FloorParamGroup.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:BeamLineSection |
