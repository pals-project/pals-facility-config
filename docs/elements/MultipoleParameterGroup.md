
# Class: MultipoleParameterGroup

A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.

URI: [pals:MultipoleParameterGroup](https://pals-project.readthedocs.io/MultipoleParameterGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ElectricMultipoleParamGroup]++-%20elec_components%200..*>[MultipoleParameterGroup&#124;order:integer;tilt:float%20%3F;En:float%20%3F;Es:float%20%3F;EnL:float%20%3F;EsL:float%20%3F;Bn:float%20%3F;Bs:float%20%3F;Kn:float%20%3F;Ks:float%20%3F],[MagneticMultipoleParamGroup]++-%20mag_components%200..*>[MultipoleParameterGroup],[MagneticMultipoleParamGroup],[ElectricMultipoleParamGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[ElectricMultipoleParamGroup]++-%20elec_components%200..*>[MultipoleParameterGroup&#124;order:integer;tilt:float%20%3F;En:float%20%3F;Es:float%20%3F;EnL:float%20%3F;EsL:float%20%3F;Bn:float%20%3F;Bs:float%20%3F;Kn:float%20%3F;Ks:float%20%3F],[MagneticMultipoleParamGroup]++-%20mag_components%200..*>[MultipoleParameterGroup],[MagneticMultipoleParamGroup],[ElectricMultipoleParamGroup])

## Referenced by Class

 *  **None** *[➞elec_components](electricMultipoleParamGroup__elec_components.md)*  <sub>0..\*</sub>  **[MultipoleParameterGroup](MultipoleParameterGroup.md)**
 *  **None** *[➞mag_components](magneticMultipoleParamGroup__mag_components.md)*  <sub>0..\*</sub>  **[MultipoleParameterGroup](MultipoleParameterGroup.md)**

## Attributes


### Own

 * [➞order](multipoleParameterGroup__order.md)  <sub>1..1</sub>
     * Description: Multipole order N (0 = dipole, 1 = quadrupole, etc.)
     * Range: [Integer](types/Integer.md)
 * [➞tilt](multipoleParameterGroup__tilt.md)  <sub>0..1</sub>
     * Description: Tilt of the Nth multipole.
     * Range: [Float](types/Float.md)
 * [➞En](multipoleParameterGroup__En.md)  <sub>0..1</sub>
     * Description: Normal component of the field.
     * Range: [Float](types/Float.md)
 * [➞Es](multipoleParameterGroup__Es.md)  <sub>0..1</sub>
     * Description: Skew component of the field.
     * Range: [Float](types/Float.md)
 * [➞EnL](multipoleParameterGroup__EnL.md)  <sub>0..1</sub>
     * Description: Length-integrated normal component.
     * Range: [Float](types/Float.md)
 * [➞EsL](multipoleParameterGroup__EsL.md)  <sub>0..1</sub>
     * Description: Length-integrated skew component.
     * Range: [Float](types/Float.md)
 * [➞Bn](multipoleParameterGroup__Bn.md)  <sub>0..1</sub>
     * Description: Normal component of the magnetic field.
     * Range: [Float](types/Float.md)
 * [➞Bs](multipoleParameterGroup__Bs.md)  <sub>0..1</sub>
     * Description: Skew component of the magnetic field.
     * Range: [Float](types/Float.md)
 * [➞Kn](multipoleParameterGroup__Kn.md)  <sub>0..1</sub>
     * Description: Normalized normal component.
     * Range: [Float](types/Float.md)
 * [➞Ks](multipoleParameterGroup__Ks.md)  <sub>0..1</sub>
     * Description: Normalized skew component.
     * Range: [Float](types/Float.md)
