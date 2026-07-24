
# Class: BeamlineSection

A virtual component used to represent a section of the beamline for organizational 
or functional grouping of components.

URI: [narad:BeamlineSection](https://example.org/narad/BeamlineSection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MetadataEntry],[Component],[BookkeepingComponent],[BookkeepingComponent]^-[BeamlineSection&#124;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[MetadataEntry],[Component],[BookkeepingComponent],[BookkeepingComponent]^-[BeamlineSection&#124;x_offset(i):float%20%3F;y_offset(i):float%20%3F;z_offset(i):float%20%3F;x_rot(i):float%20%3F;y_rot(i):float%20%3F;z_rot(i):float%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F])

## Parents

 *  is_a: [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,

## Attributes


### Inherited from BookkeepingComponent:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [Component](Component.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞functions](virtualComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the virtual component,  which can be used to identify the component across different source systems.
     * Range: [VirtualFunctionEnum](VirtualFunctionEnum.md)
 * [➞beamline_relation](virtualComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [VirtualRelationEnum](VirtualRelationEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:BeamlineSection |
