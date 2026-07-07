
# Class: FloorP

Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [narad:FloorP](https://example.org/narad/FloorP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent]uses%20-.->[FloorP&#124;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F],[SupportingFacilityComponent]uses%20-.->[FloorP],[PhysicalComponent]uses%20-.->[FloorP],[VirtualComponent],[SupportingFacilityComponent],[PhysicalComponent])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent]uses%20-.->[FloorP&#124;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F],[SupportingFacilityComponent]uses%20-.->[FloorP],[PhysicalComponent]uses%20-.->[FloorP],[VirtualComponent],[SupportingFacilityComponent],[PhysicalComponent])

## Mixin for

 * [PhysicalComponent](PhysicalComponent.md) (mixin)  - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) (mixin)  - A physical component that supports accelerator operation
 * [VirtualComponent](VirtualComponent.md) (mixin)  - A virtual or logical component that represents a concept, function, or role in the accelerator  beamline operation but does not have a physical instantiation.  This can be used to capture abstract components, such as Markers, BeamlineSections, and FacilitySpaces that are important for understanding the structure and function of the accelerator system but are not physical devices.

## Referenced by Class


## Attributes


### Own

 * [➞x](floorP__x.md)  <sub>0..1</sub>
     * Description: Global X coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞y](floorP__y.md)  <sub>0..1</sub>
     * Description: Global Y coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞z](floorP__z.md)  <sub>0..1</sub>
     * Description: Global Z coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞theta](floorP__theta.md)  <sub>0..1</sub>
     * Description: Orientation angle around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞phi](floorP__phi.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞psi](floorP__psi.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:FloorP |
