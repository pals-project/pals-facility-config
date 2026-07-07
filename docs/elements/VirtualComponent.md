
# Class: VirtualComponent

A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

URI: [narad:VirtualComponent](https://example.org/narad/VirtualComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NARAD]++-%20virtual_components%200..*>[VirtualComponent&#124;function:VirtualFunctionEnum;beamline_relation:VirtualRelationEnum;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[VirtualComponent]uses%20-.->[FloorP],[VirtualComponent]^-[BookkeepingComponent],[VirtualComponent]^-[Beamline],[Component]^-[VirtualComponent],[NARAD],[MetadataEntry],[FloorP],[Component],[BookkeepingComponent],[Beamline])](https://yuml.me/diagram/nofunky;dir:TB/class/[NARAD]++-%20virtual_components%200..*>[VirtualComponent&#124;function:VirtualFunctionEnum;beamline_relation:VirtualRelationEnum;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F;id(i):string;type(i):string;native_types(i):string%20*;description(i):string%20%3F;label(i):string%20%3F;alias(i):string%20%3F],[VirtualComponent]uses%20-.->[FloorP],[VirtualComponent]^-[BookkeepingComponent],[VirtualComponent]^-[Beamline],[Component]^-[VirtualComponent],[NARAD],[MetadataEntry],[FloorP],[Component],[BookkeepingComponent],[Beamline])

## Parents

 *  is_a: [Component](Component.md) - A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.

## Uses Mixin

 *  mixin: [FloorP](FloorP.md) - Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

## Children

 * [Beamline](Beamline.md) - A top-level NARAD-system for an ordered sequence of beamline elements defining a beam path.
 * [BookkeepingComponent](BookkeepingComponent.md) - A virtual component that represents a bookkeeping or organizational role in the accelerator system,

## Referenced by Class

 *  **None** *[➞virtual_components](nARAD__virtual_components.md)*  <sub>0..\*</sub>  **[VirtualComponent](VirtualComponent.md)**

## Attributes


### Own

 * [➞function](virtualComponent__function.md)  <sub>1..1</sub>
     * Description: The function of the virtual component,  which can be used to identify the component across different source systems.
     * Range: [VirtualFunctionEnum](VirtualFunctionEnum.md)
 * [➞beamline_relation](virtualComponent__beamline_relation.md)  <sub>1..1</sub>
     * Description: The relationship of the virtual component to the beamline,  which can be used to identify the component across different source systems.
     * Range: [VirtualRelationEnum](VirtualRelationEnum.md)

### Inherited from Component:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [String](types/String.md)
 * [➞native_types](component__native_types.md)  <sub>0..\*</sub>
     * Description: The native type of the component in the source system, which can be used to identify the component across different source systems.
     * Range: [String](types/String.md)

### Mixed in from FloorP:

 * [➞x](floorP__x.md)  <sub>0..1</sub>
     * Description: Global X coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞y](floorP__y.md)  <sub>0..1</sub>
     * Description: Global Y coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞z](floorP__z.md)  <sub>0..1</sub>
     * Description: Global Z coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞theta](floorP__theta.md)  <sub>0..1</sub>
     * Description: Orientation angle around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞phi](floorP__phi.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Mixed in from FloorP:

 * [➞psi](floorP__psi.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:Element |
|  | | pals:BookkeepingElement |
