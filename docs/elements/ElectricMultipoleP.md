
# Class: ElectricMultipoleP

Mixin for electric multipole parameters, 
which can be used to describe the electric field components of an accelerator element.
This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).
Example with three multipole components (N=0,1,2): ```yaml components: - order: 7
  tilt: 0.7
- order: 3
  En: 27.3
- order: 2
  EnL: 3.47e1
```

URI: [narad:ElectricMultipoleP](https://example.org/narad/ElectricMultipoleP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MultipoleComponent],[MultipoleComponent]<components%200..*-++[ElectricMultipoleP],[Multipole]uses%20-.->[ElectricMultipoleP],[Kicker]uses%20-.->[ElectricMultipoleP],[Cavity]uses%20-.->[ElectricMultipoleP],[Multipole],[Kicker],[Cavity])](https://yuml.me/diagram/nofunky;dir:TB/class/[MultipoleComponent],[MultipoleComponent]<components%200..*-++[ElectricMultipoleP],[Multipole]uses%20-.->[ElectricMultipoleP],[Kicker]uses%20-.->[ElectricMultipoleP],[Cavity]uses%20-.->[ElectricMultipoleP],[Multipole],[Kicker],[Cavity])

## Mixin for

 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Kicker](Kicker.md) (mixin)  - A magnet primarily used to steer the beam.
 * [Multipole](Multipole.md) (mixin)  - A general magnet with a higher-order multipole field, such as a sextupole or octupole.

## Referenced by Class


## Attributes


### Own

 * [➞components](electricMultipoleP__components.md)  <sub>0..\*</sub>
     * Description: Electric multipole components, one per order N.
     * Range: [MultipoleComponent](MultipoleComponent.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | pals:ElectricMultipoleP |
| **Broad Mappings:** | | pals:ElectricMultipoleP |
