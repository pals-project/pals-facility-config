
# Class: HasTwissP



URI: [pals:HasTwissP](https://pals-project.readthedocs.io/HasTwissP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[TwissParamGroup]<TwissP%200..1-++[HasTwissP],[Marker]uses%20-.->[HasTwissP],[Magnet]uses%20-.->[HasTwissP],[Cavity]uses%20-.->[HasTwissP],[BeamProfileMonitor]uses%20-.->[HasTwissP],[BeamPositionMonitor]uses%20-.->[HasTwissP],[Aperture]uses%20-.->[HasTwissP],[Marker],[Magnet],[Cavity],[BeamProfileMonitor],[BeamPositionMonitor],[Aperture])](https://yuml.me/diagram/nofunky;dir:TB/class/[TwissParamGroup],[TwissParamGroup]<TwissP%200..1-++[HasTwissP],[Marker]uses%20-.->[HasTwissP],[Magnet]uses%20-.->[HasTwissP],[Cavity]uses%20-.->[HasTwissP],[BeamProfileMonitor]uses%20-.->[HasTwissP],[BeamPositionMonitor]uses%20-.->[HasTwissP],[Aperture]uses%20-.->[HasTwissP],[Marker],[Magnet],[Cavity],[BeamProfileMonitor],[BeamPositionMonitor],[Aperture])

## Mixin for

 * [Aperture](Aperture.md) (mixin)  - A diagnostic or limiting aperture element used to constrain or characterize beam passage.
 * [BeamPositionMonitor](BeamPositionMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam position.
 * [BeamProfileMonitor](BeamProfileMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam profile.
 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Magnet](Magnet.md) (mixin)  - An accelerator device that produces a magnetic field for beam control.
 * [Marker](Marker.md) (mixin)  - A virtual component used as a reference point or marker in the beamline structure.

## Referenced by Class


## Attributes


### Own

 * [➞TwissP](hasTwissP__TwissP.md)  <sub>0..1</sub>
     * Description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [TwissParamGroup](TwissParamGroup.md)
