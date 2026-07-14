
# Class: BookkeepingComponent

A virtual component that represents a bookkeeping or organizational role in the accelerator system, 
such as a BeamlineSection, Marker or a Fork.
These can include BeamlineSections, Markers, Forks, 
and other virtual components that are important for understanding 
the structure and function of the accelerator system but are not physical devices.

URI: [narad:BookkeepingComponent](https://example.org/narad/BookkeepingComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[MetadataEntry],[Marker],[BookkeepingComponent&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[BodyShiftP],[BookkeepingComponent]^-[Marker],[BookkeepingComponent]^-[BeamlineSection],[VirtualComponent]^-[BookkeepingComponent],[BodyShiftP],[BeamlineSection])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[MetadataEntry],[Marker],[BookkeepingComponent&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;functions(i):VirtualFunctionEnum%20%2B;beamline_relation(i):VirtualRelationEnum;x(i):float%20%3F;y(i):float%20%3F;z(i):float%20%3F;theta(i):float%20%3F;phi(i):float%20%3F;psi(i):float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F]uses%20-.->[BodyShiftP],[BookkeepingComponent]^-[Marker],[BookkeepingComponent]^-[BeamlineSection],[VirtualComponent]^-[BookkeepingComponent],[BodyShiftP],[BeamlineSection])

## Parents

 *  is_a: [VirtualComponent](VirtualComponent.md) - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Uses Mixin

 *  mixin: [BodyShiftP](BodyShiftP.md) - Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

## Children

 * [BeamlineSection](BeamlineSection.md) - A virtual component used to represent a section of the beamline for organizational
 * [Marker](Marker.md) - A virtual component used as a reference point or marker in the beamline structure.

## Referenced by Class


## Attributes


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
 * [➞functions](virtualComponent__functions.md)  <sub>1..\*</sub>
     * Description: The function of the virtual component,  which can be used to identify the component across different source systems.
     * Range: [VirtualFunctionEnum](VirtualFunctionEnum.md)
 * [➞beamline_relation](virtualComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [VirtualRelationEnum](VirtualRelationEnum.md)

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
| **Broad Mappings:** | | pals:BookkeepingElement |
