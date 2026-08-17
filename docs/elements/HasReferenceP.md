
# Class: HasReferenceP



URI: [pals:HasReferenceP](https://pals-project.readthedocs.io/HasReferenceP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferenceParamGroup],[ReferenceParamGroup]<ReferenceP%200..1-++[HasReferenceP],[Magnet]uses%20-.->[HasReferenceP],[Cavity]uses%20-.->[HasReferenceP],[BeamProfileMonitor]uses%20-.->[HasReferenceP],[BeamPositionMonitor]uses%20-.->[HasReferenceP],[Aperture]uses%20-.->[HasReferenceP],[Magnet],[Cavity],[BeamProfileMonitor],[BeamPositionMonitor],[Aperture])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferenceParamGroup],[ReferenceParamGroup]<ReferenceP%200..1-++[HasReferenceP],[Magnet]uses%20-.->[HasReferenceP],[Cavity]uses%20-.->[HasReferenceP],[BeamProfileMonitor]uses%20-.->[HasReferenceP],[BeamPositionMonitor]uses%20-.->[HasReferenceP],[Aperture]uses%20-.->[HasReferenceP],[Magnet],[Cavity],[BeamProfileMonitor],[BeamPositionMonitor],[Aperture])

## Mixin for

 * [Aperture](Aperture.md) (mixin)  - A diagnostic or limiting aperture element used to constrain or characterize beam passage.
 * [BeamPositionMonitor](BeamPositionMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam position.
 * [BeamProfileMonitor](BeamProfileMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam profile.
 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Magnet](Magnet.md) (mixin)  - An accelerator device that produces a magnetic field for beam control.

## Referenced by Class


## Attributes


### Own

 * [➞ReferenceP](hasReferenceP__ReferenceP.md)  <sub>0..1</sub>
     * Description: A mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [ReferenceParamGroup](ReferenceParamGroup.md)
