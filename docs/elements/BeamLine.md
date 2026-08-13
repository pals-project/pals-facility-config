
# Class: BeamLine

PALS element for an ordered sequence of beamline elements defining a beam path.

URI: [pals:BeamLine](https://pals-project.readthedocs.io/BeamLine)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[MetaParamGroup],[FloorParamGroup],[Precedes]-%20beamline_context%201..1>[BeamLine&#124;length:float%20%3F;description:string%20%3F;multipass:boolean%20%3F;periodic:boolean%20%3F;repeat:integer%20%3F;direction:integer%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*],[HasConnectingBranch]-%20beamline_context%201..1>[BeamLine],[Facility]++-%20beamlines%200..*>[BeamLine],[VirtualComponent]^-[BeamLine],[Precedes],[HasConnectingBranch],[Facility])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[MetaParamGroup],[FloorParamGroup],[Precedes]-%20beamline_context%201..1>[BeamLine&#124;length:float%20%3F;description:string%20%3F;multipass:boolean%20%3F;periodic:boolean%20%3F;repeat:integer%20%3F;direction:integer%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;native_types(i):string%20*;id(i):string;kind(i):string;alias(i):string%20*],[HasConnectingBranch]-%20beamline_context%201..1>[BeamLine],[Facility]++-%20beamlines%200..*>[BeamLine],[VirtualComponent]^-[BeamLine],[Precedes],[HasConnectingBranch],[Facility])

## Parents

 *  is_a: [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamLineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Referenced by Class

 *  **None** *[beamline_context](beamline_context.md)*  <sub>1..1</sub>  **[BeamLine](BeamLine.md)**
 *  **None** *[➞beamlines](facility__beamlines.md)*  <sub>0..\*</sub>  **[BeamLine](BeamLine.md)**

## Attributes


### Own

 * [BeamLine➞length](BeamLine_length.md)  <sub>0..1</sub>
     * Description: The total length of the BeamLine. For pals interoperability, use m as the unit of length.
     * Range: [Float](types/Float.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description of the instance.
     * Range: [String](types/String.md)
 * [➞multipass](beamLine__multipass.md)  <sub>0..1</sub>
     * Description: Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass.
     * Range: [Boolean](types/Boolean.md)
 * [➞periodic](beamLine__periodic.md)  <sub>0..1</sub>
     * Description: Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic.
     * Range: [Boolean](types/Boolean.md)
 * [➞repeat](beamLine__repeat.md)  <sub>0..1</sub>
     * Description: Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1.
If value is greater than 1, the beamline is repeated that many times.
     * Range: [Integer](types/Integer.md)
 * [➞direction](beamLine__direction.md)  <sub>0..1</sub>
     * Description: Beam direction along the BeamLine: +1 or -1. Longitudinal orientation. Default is +1.
     * Range: [Integer](types/Integer.md)

### Inherited from VirtualComponent:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:BeamLine |
