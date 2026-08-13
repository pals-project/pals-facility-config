
# Class: HasMagneticMultipoleP



URI: [pals:HasMagneticMultipoleP](https://pals-project.readthedocs.io/HasMagneticMultipoleP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MagneticMultipoleParamGroup],[MagneticMultipoleParamGroup]<MagneticMultipoleP%200..1-++[HasMagneticMultipoleP],[Multipole]uses%20-.->[HasMagneticMultipoleP],[Kicker]uses%20-.->[HasMagneticMultipoleP],[Cavity]uses%20-.->[HasMagneticMultipoleP],[Multipole],[Kicker],[Cavity])](https://yuml.me/diagram/nofunky;dir:TB/class/[MagneticMultipoleParamGroup],[MagneticMultipoleParamGroup]<MagneticMultipoleP%200..1-++[HasMagneticMultipoleP],[Multipole]uses%20-.->[HasMagneticMultipoleP],[Kicker]uses%20-.->[HasMagneticMultipoleP],[Cavity]uses%20-.->[HasMagneticMultipoleP],[Multipole],[Kicker],[Cavity])

## Mixin for

 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Kicker](Kicker.md) (mixin)  - A magnet primarily used to steer the beam.
 * [Multipole](Multipole.md) (mixin)  - A general magnet with a higher-order multipole field, such as a sextupole or octupole.

## Referenced by Class


## Attributes


### Own

 * [➞MagneticMultipoleP](hasMagneticMultipoleP__MagneticMultipoleP.md)  <sub>0..1</sub>
     * Description: A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md)
