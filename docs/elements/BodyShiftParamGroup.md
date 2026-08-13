
# Class: BodyShiftParamGroup

Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [pals:BodyShiftParamGroup](https://pals-project.readthedocs.io/BodyShiftParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasBodyShiftP]++-%20BodyShiftP%200..1>[BodyShiftParamGroup&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;id(i):string],[ParamGroup]^-[BodyShiftParamGroup],[HasBodyShiftP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasBodyShiftP]++-%20BodyShiftP%200..1>[BodyShiftParamGroup&#124;x_offset:float%20%3F;y_offset:float%20%3F;z_offset:float%20%3F;x_rot:float%20%3F;y_rot:float%20%3F;z_rot:float%20%3F;id(i):string],[ParamGroup]^-[BodyShiftParamGroup],[HasBodyShiftP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞BodyShiftP](hasBodyShiftP__BodyShiftP.md)*  <sub>0..1</sub>  **[BodyShiftParamGroup](BodyShiftParamGroup.md)**

## Attributes


### Own

 * [➞x_offset](bodyShiftParamGroup__x_offset.md)  <sub>0..1</sub>
     * Description: Shift in the X direction in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞y_offset](bodyShiftParamGroup__y_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Y direction in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞z_offset](bodyShiftParamGroup__z_offset.md)  <sub>0..1</sub>
     * Description: Shift in the Z direction in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞x_rot](bodyShiftParamGroup__x_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the X-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞y_rot](bodyShiftParamGroup__y_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Y-axis in the facility floor plan.
     * Range: [Float](types/Float.md)
 * [➞z_rot](bodyShiftParamGroup__z_rot.md)  <sub>0..1</sub>
     * Description: Rotation around the Z-axis in the facility floor plan.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:BodyShiftP |
