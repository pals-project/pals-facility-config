
# Class: BendParamGroup

Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [pals:BendParamGroup](https://pals-project.readthedocs.io/BendParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasBendP]++-%20BendP%200..1>[BendParamGroup&#124;angle_ref:float%20%3F;bend_field_ref:float%20%3F;bend_field_actual:float%20%3F;e1:float%20%3F;e2:float%20%3F;e1_rect:float%20%3F;e2_rect:float%20%3F;edge1_int:float%20%3F;edge2_int:float%20%3F;g_ref:float%20%3F;g_actual:float%20%3F;h1:float%20%3F;h2:float%20%3F;L_chord:float%20%3F;L_sagitta:float%20%3F;L_rectangle:float%20%3F;multipole_geometry:MultipoleGeometryEnum%20%3F;ref_geometry:ReferenceGeometryEnum%20%3F;rho_ref:float%20%3F;tilt_ref:float%20%3F;id(i):string],[ParamGroup]^-[BendParamGroup],[HasBendP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasBendP]++-%20BendP%200..1>[BendParamGroup&#124;angle_ref:float%20%3F;bend_field_ref:float%20%3F;bend_field_actual:float%20%3F;e1:float%20%3F;e2:float%20%3F;e1_rect:float%20%3F;e2_rect:float%20%3F;edge1_int:float%20%3F;edge2_int:float%20%3F;g_ref:float%20%3F;g_actual:float%20%3F;h1:float%20%3F;h2:float%20%3F;L_chord:float%20%3F;L_sagitta:float%20%3F;L_rectangle:float%20%3F;multipole_geometry:MultipoleGeometryEnum%20%3F;ref_geometry:ReferenceGeometryEnum%20%3F;rho_ref:float%20%3F;tilt_ref:float%20%3F;id(i):string],[ParamGroup]^-[BendParamGroup],[HasBendP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞BendP](hasBendP__BendP.md)*  <sub>0..1</sub>  **[BendParamGroup](BendParamGroup.md)**

## Attributes


### Own

 * [➞angle_ref](bendParamGroup__angle_ref.md)  <sub>0..1</sub>
     * Description: Reference bend angle.
     * Range: [Float](types/Float.md)
 * [➞bend_field_ref](bendParamGroup__bend_field_ref.md)  <sub>0..1</sub>
     * Description: Reference bend field.
     * Range: [Float](types/Float.md)
 * [➞bend_field_actual](bendParamGroup__bend_field_actual.md)  <sub>0..1</sub>
     * Description: Actual bend field.
     * Range: [Float](types/Float.md)
 * [➞e1](bendParamGroup__e1.md)  <sub>0..1</sub>
     * Description: Entrance end pole face rotation with respect to a sector geometry.
     * Range: [Float](types/Float.md)
 * [➞e2](bendParamGroup__e2.md)  <sub>0..1</sub>
     * Description: Exit end pole face rotation with respect to a sector geometry.
     * Range: [Float](types/Float.md)
 * [➞e1_rect](bendParamGroup__e1_rect.md)  <sub>0..1</sub>
     * Description: Entrance end pole face rotation with respect to a rectangular geometry.
     * Range: [Float](types/Float.md)
 * [➞e2_rect](bendParamGroup__e2_rect.md)  <sub>0..1</sub>
     * Description: Exit end pole face rotation with respect to a rectangular geometry.
     * Range: [Float](types/Float.md)
 * [➞edge1_int](bendParamGroup__edge1_int.md)  <sub>0..1</sub>
     * Description: Entrance end fringe field integral.
     * Range: [Float](types/Float.md)
 * [➞edge2_int](bendParamGroup__edge2_int.md)  <sub>0..1</sub>
     * Description: Exit end fringe field integral.
     * Range: [Float](types/Float.md)
 * [➞g_ref](bendParamGroup__g_ref.md)  <sub>0..1</sub>
     * Description: Reference bend strength = 1/radius_ref
     * Range: [Float](types/Float.md)
 * [➞g_actual](bendParamGroup__g_actual.md)  <sub>0..1</sub>
     * Description: Actual bend strength = 1/radius_actual
     * Range: [Float](types/Float.md)
 * [➞h1](bendParamGroup__h1.md)  <sub>0..1</sub>
     * Description: Entrance end pole face curvature
     * Range: [Float](types/Float.md)
 * [➞h2](bendParamGroup__h2.md)  <sub>0..1</sub>
     * Description: Exit end pole face curvature
     * Range: [Float](types/Float.md)
 * [➞L_chord](bendParamGroup__L_chord.md)  <sub>0..1</sub>
     * Description: Chord length of the bend.
     * Range: [Float](types/Float.md)
 * [➞L_sagitta](bendParamGroup__L_sagitta.md)  <sub>0..1</sub>
     * Description: Output parameter. Sagitta length.
     * Range: [Float](types/Float.md)
 * [➞L_rectangle](bendParamGroup__L_rectangle.md)  <sub>0..1</sub>
     * Description: Rectangular length.
     * Range: [Float](types/Float.md)
 * [➞multipole_geometry](bendParamGroup__multipole_geometry.md)  <sub>0..1</sub>
     * Description: Multipole geometry type. Must be `follows_ref_geometry`.
     * Range: [MultipoleGeometryEnum](MultipoleGeometryEnum.md)
 * [➞ref_geometry](bendParamGroup__ref_geometry.md)  <sub>0..1</sub>
     * Description: Reference geometry type. Must be `arc`.
     * Range: [ReferenceGeometryEnum](ReferenceGeometryEnum.md)
 * [➞rho_ref](bendParamGroup__rho_ref.md)  <sub>0..1</sub>
     * Description: Reference bend radius.
     * Range: [Float](types/Float.md)
 * [➞tilt_ref](bendParamGroup__tilt_ref.md)  <sub>0..1</sub>
     * Description: Reference tilt of the bend.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:BendP |
