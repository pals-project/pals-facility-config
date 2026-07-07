
# Class: MultipoleComponent

A single order's electric (or magnetic) multipole component.
Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both.
Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.

URI: [narad:MultipoleComponent](https://example.org/narad/MultipoleComponent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ElectricMultipoleP]++-%20components%200..*>[MultipoleComponent&#124;order:integer;tilt:float%20%3F;En:float%20%3F;Es:float%20%3F;EnL:float%20%3F;EsL:float%20%3F;Bn:float%20%3F;Bs:float%20%3F;Kn:float%20%3F;Ks:float%20%3F],[MagneticMultipoleP]++-%20components%200..*>[MultipoleComponent],[MagneticMultipoleP],[ElectricMultipoleP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ElectricMultipoleP]++-%20components%200..*>[MultipoleComponent&#124;order:integer;tilt:float%20%3F;En:float%20%3F;Es:float%20%3F;EnL:float%20%3F;EsL:float%20%3F;Bn:float%20%3F;Bs:float%20%3F;Kn:float%20%3F;Ks:float%20%3F],[MagneticMultipoleP]++-%20components%200..*>[MultipoleComponent],[MagneticMultipoleP],[ElectricMultipoleP])

## Referenced by Class

 *  **None** *[➞components](electricMultipoleP__components.md)*  <sub>0..\*</sub>  **[MultipoleComponent](MultipoleComponent.md)**
 *  **None** *[➞components](magneticMultipoleP__components.md)*  <sub>0..\*</sub>  **[MultipoleComponent](MultipoleComponent.md)**

## Attributes


### Own

 * [➞order](multipoleComponent__order.md)  <sub>1..1</sub>
     * Description: Multipole order N (0 = dipole, 1 = quadrupole, etc.)
     * Range: [Integer](types/Integer.md)
 * [➞tilt](multipoleComponent__tilt.md)  <sub>0..1</sub>
     * Description: Tilt of the Nth multipole.
     * Range: [Float](types/Float.md)
 * [➞En](multipoleComponent__En.md)  <sub>0..1</sub>
     * Description: Normal component of the field.
     * Range: [Float](types/Float.md)
 * [➞Es](multipoleComponent__Es.md)  <sub>0..1</sub>
     * Description: Skew component of the field.
     * Range: [Float](types/Float.md)
 * [➞EnL](multipoleComponent__EnL.md)  <sub>0..1</sub>
     * Description: Length-integrated normal component.
     * Range: [Float](types/Float.md)
 * [➞EsL](multipoleComponent__EsL.md)  <sub>0..1</sub>
     * Description: Length-integrated skew component.
     * Range: [Float](types/Float.md)
 * [➞Bn](multipoleComponent__Bn.md)  <sub>0..1</sub>
     * Description: Normal component of the magnetic field.
     * Range: [Float](types/Float.md)
 * [➞Bs](multipoleComponent__Bs.md)  <sub>0..1</sub>
     * Description: Skew component of the magnetic field.
     * Range: [Float](types/Float.md)
 * [➞Kn](multipoleComponent__Kn.md)  <sub>0..1</sub>
     * Description: Normalized normal component.
     * Range: [Float](types/Float.md)
 * [➞Ks](multipoleComponent__Ks.md)  <sub>0..1</sub>
     * Description: Normalized skew component.
     * Range: [Float](types/Float.md)
