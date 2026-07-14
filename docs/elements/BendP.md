
# Class: BendP

Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element.
This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).

URI: [narad:BendP](https://example.org/narad/BendP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BendP&#124;angle_ref:float%20%3F;bend_field_ref:float%20%3F;bend_field_actual:float%20%3F;e1:float%20%3F;e2:float%20%3F;e1_rect:float%20%3F;e2_rect:float%20%3F;edge1_int:float%20%3F;edge2_int:float%20%3F;g_ref:float%20%3F;g_actual:float%20%3F;h1:float%20%3F;h2:float%20%3F;L_chord:float%20%3F;L_sagitta:float%20%3F;L_rectangle:float%20%3F;multipole_geometry:MultipoleGeometryEnum%20%3F;ref_geometry:ReferenceGeometryEnum%20%3F;rho_ref:float%20%3F;tilt_ref:float%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[BendP&#124;angle_ref:float%20%3F;bend_field_ref:float%20%3F;bend_field_actual:float%20%3F;e1:float%20%3F;e2:float%20%3F;e1_rect:float%20%3F;e2_rect:float%20%3F;edge1_int:float%20%3F;edge2_int:float%20%3F;g_ref:float%20%3F;g_actual:float%20%3F;h1:float%20%3F;h2:float%20%3F;L_chord:float%20%3F;L_sagitta:float%20%3F;L_rectangle:float%20%3F;multipole_geometry:MultipoleGeometryEnum%20%3F;ref_geometry:ReferenceGeometryEnum%20%3F;rho_ref:float%20%3F;tilt_ref:float%20%3F])

## Attributes


### Own

 * [➞angle_ref](bendP__angle_ref.md)  <sub>0..1</sub>
     * Description: Reference bend angle.
     * Range: [Float](types/Float.md)
 * [➞bend_field_ref](bendP__bend_field_ref.md)  <sub>0..1</sub>
     * Description: Reference bend field.
     * Range: [Float](types/Float.md)
 * [➞bend_field_actual](bendP__bend_field_actual.md)  <sub>0..1</sub>
     * Description: Actual bend field.
     * Range: [Float](types/Float.md)
 * [➞e1](bendP__e1.md)  <sub>0..1</sub>
     * Description: Entrance end pole face rotation with respect to a sector geometry.
     * Range: [Float](types/Float.md)
 * [➞e2](bendP__e2.md)  <sub>0..1</sub>
     * Description: Exit end pole face rotation with respect to a sector geometry.
     * Range: [Float](types/Float.md)
 * [➞e1_rect](bendP__e1_rect.md)  <sub>0..1</sub>
     * Description: Entrance end pole face rotation with respect to a rectangular geometry.
     * Range: [Float](types/Float.md)
 * [➞e2_rect](bendP__e2_rect.md)  <sub>0..1</sub>
     * Description: Exit end pole face rotation with respect to a rectangular geometry.
     * Range: [Float](types/Float.md)
 * [➞edge1_int](bendP__edge1_int.md)  <sub>0..1</sub>
     * Description: Entrance end fringe field integral.
     * Range: [Float](types/Float.md)
 * [➞edge2_int](bendP__edge2_int.md)  <sub>0..1</sub>
     * Description: Exit end fringe field integral.
     * Range: [Float](types/Float.md)
 * [➞g_ref](bendP__g_ref.md)  <sub>0..1</sub>
     * Description: Reference bend strength = 1/radius_ref
     * Range: [Float](types/Float.md)
 * [➞g_actual](bendP__g_actual.md)  <sub>0..1</sub>
     * Description: Actual bend strength = 1/radius_actual
     * Range: [Float](types/Float.md)
 * [➞h1](bendP__h1.md)  <sub>0..1</sub>
     * Description: Entrance end pole face curvature
     * Range: [Float](types/Float.md)
 * [➞h2](bendP__h2.md)  <sub>0..1</sub>
     * Description: Exit end pole face curvature
     * Range: [Float](types/Float.md)
 * [➞L_chord](bendP__L_chord.md)  <sub>0..1</sub>
     * Description: Chord length of the bend.
     * Range: [Float](types/Float.md)
 * [➞L_sagitta](bendP__L_sagitta.md)  <sub>0..1</sub>
     * Description: Output parameter. Sagitta length.
     * Range: [Float](types/Float.md)
 * [➞L_rectangle](bendP__L_rectangle.md)  <sub>0..1</sub>
     * Description: Rectangular length.
     * Range: [Float](types/Float.md)
 * [➞multipole_geometry](bendP__multipole_geometry.md)  <sub>0..1</sub>
     * Description: Multipole geometry type. Must be `follows_ref_geometry`.
     * Range: [MultipoleGeometryEnum](MultipoleGeometryEnum.md)
 * [➞ref_geometry](bendP__ref_geometry.md)  <sub>0..1</sub>
     * Description: Reference geometry type. Must be `arc`.
     * Range: [ReferenceGeometryEnum](ReferenceGeometryEnum.md)
 * [➞rho_ref](bendP__rho_ref.md)  <sub>0..1</sub>
     * Description: Reference bend radius.
     * Range: [Float](types/Float.md)
 * [➞tilt_ref](bendP__tilt_ref.md)  <sub>0..1</sub>
     * Description: Reference tilt of the bend.
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:BendP |
