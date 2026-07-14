
# Class: MagneticMultipoleP

Mixin for magnetic multipole parameters, 
which can be used to describe the magnetic field components of an accelerator element.
This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).
Example with three multipole components (N=0,1,2): ```yaml components: - order: 7
  tilt: 0.7
- order: 3
  Bn: 27.3
- order: 2
  BnL: 3.47e1
- order: 1
  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength
```

URI: [narad:MagneticMultipoleP](https://example.org/narad/MagneticMultipoleP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MultipoleComponent],[MultipoleComponent]<components%200..*-++[MagneticMultipoleP],[Multipole]uses%20-.->[MagneticMultipoleP],[Kicker]uses%20-.->[MagneticMultipoleP],[Cavity]uses%20-.->[MagneticMultipoleP],[Multipole],[Kicker],[Cavity])](https://yuml.me/diagram/nofunky;dir:TB/class/[MultipoleComponent],[MultipoleComponent]<components%200..*-++[MagneticMultipoleP],[Multipole]uses%20-.->[MagneticMultipoleP],[Kicker]uses%20-.->[MagneticMultipoleP],[Cavity]uses%20-.->[MagneticMultipoleP],[Multipole],[Kicker],[Cavity])

## Mixin for

 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Kicker](Kicker.md) (mixin)  - A magnet primarily used to steer the beam.
 * [Multipole](Multipole.md) (mixin)  - A general magnet with a higher-order multipole field, such as a sextupole or octupole.

## Referenced by Class


## Attributes


### Own

 * [➞components](magneticMultipoleP__components.md)  <sub>0..\*</sub>
     * Description: Magnetic multipole components, one per order N.
     * Range: [MultipoleComponent](MultipoleComponent.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | pals:MagneticMultipoleP |
