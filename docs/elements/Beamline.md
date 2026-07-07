
# Class: Beamline

A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.

URI: [narad:Beamline](https://example.org/narad/Beamline)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[MetadataEntry],[ComponentRelation]-%20beamline_context%200..1>[Beamline&#124;multipass:boolean%20%3F;length:float%20%3F;zero_point:string%20%3F;periodic:boolean%20%3F;repeat:integer%20%3F;direction:integer%20%3F;function(i):VirtualFunctionEnum;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[NARAD]++-%20beamlines%200..*>[Beamline],[VirtualComponent]^-[Beamline],[NARAD],[ComponentRelation])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[MetadataEntry],[ComponentRelation]-%20beamline_context%200..1>[Beamline&#124;multipass:boolean%20%3F;length:float%20%3F;zero_point:string%20%3F;periodic:boolean%20%3F;repeat:integer%20%3F;direction:integer%20%3F;function(i):VirtualFunctionEnum;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[NARAD]++-%20beamlines%200..*>[Beamline],[VirtualComponent]^-[Beamline],[NARAD],[ComponentRelation])

## Parents

 *  is_a: [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Referenced by Class

 *  **None** *[➞beamline_context](componentRelation__beamline_context.md)*  <sub>0..1</sub>  **[Beamline](Beamline.md)**
 *  **None** *[➞beamlines](nARAD__beamlines.md)*  <sub>0..\*</sub>  **[Beamline](Beamline.md)**

## Attributes


### Own

 * [➞multipass](beamline__multipass.md)  <sub>0..1</sub>
     * Description: Indicates whether the beamline is a multipass beamline, where the beam passes through the same physical elements multiple times.
If not provided, the default assumption is that the beamline is single-pass.
     * Range: [Boolean](types/Boolean.md)
 * [➞length](beamline__length.md)  <sub>0..1</sub>
     * Description: The total length of the beamline.
For pals interoperability, use m as the unit of length.
     * Range: [Float](types/Float.md)
 * [➞zero_point](beamline__zero_point.md)  <sub>0..1</sub>
     * Description: Name of a line item used as a reference point when the BeamLine is used as a subline.
     * Range: [String](types/String.md)
 * [➞periodic](beamline__periodic.md)  <sub>0..1</sub>
     * Description: Indicates whether orbit and Twiss parameters periodic.
If not provided, the default assumption is that the beamline is not periodic.
     * Range: [Boolean](types/Boolean.md)
 * [➞repeat](beamline__repeat.md)  <sub>0..1</sub>
     * Description: Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
If value is greater than 1, the beamline is repeated that many times.
     * Range: [Integer](types/Integer.md)
 * [➞direction](beamline__direction.md)  <sub>0..1</sub>
     * Description: Beam direction along the beamline: +1 or -1. 
Longitudinal orientation. Default is +1.
     * Range: [Integer](types/Integer.md)

### Inherited from VirtualComponent:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)
 * [➞function](virtualComponent__function.md)  <sub>1..1</sub>
     * Description: The function of the virtual component,  which can be used to identify the component across different source systems.
     * Range: [VirtualFunctionEnum](VirtualFunctionEnum.md)
 * [➞beamline_relation](virtualComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [VirtualRelationEnum](VirtualRelationEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:BeamLine |
