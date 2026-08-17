
# Class: FloorParamGroup

Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [pals:FloorParamGroup](https://pals-project.readthedocs.io/FloorParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasFloorP]++-%20FloorP%200..1>[FloorParamGroup&#124;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F;id(i):string],[ParamGroup]^-[FloorParamGroup],[HasFloorP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasFloorP]++-%20FloorP%200..1>[FloorParamGroup&#124;x:float%20%3F;y:float%20%3F;z:float%20%3F;theta:float%20%3F;phi:float%20%3F;psi:float%20%3F;id(i):string],[ParamGroup]^-[FloorParamGroup],[HasFloorP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞FloorP](hasFloorP__FloorP.md)*  <sub>0..1</sub>  **[FloorParamGroup](FloorParamGroup.md)**

## Attributes


### Own

 * [➞x](floorParamGroup__x.md)  <sub>0..1</sub>
     * Description: Global X coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞y](floorParamGroup__y.md)  <sub>0..1</sub>
     * Description: Global Y coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞z](floorParamGroup__z.md)  <sub>0..1</sub>
     * Description: Global Z coordinate in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞theta](floorParamGroup__theta.md)  <sub>0..1</sub>
     * Description: Orientation angle around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞phi](floorParamGroup__phi.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞psi](floorParamGroup__psi.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:FloorP |
