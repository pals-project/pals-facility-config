
# Class: HasBodyShiftP



URI: [pals:HasBodyShiftP](https://pals-project.readthedocs.io/HasBodyShiftP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BodyShiftParamGroup]<BodyShiftP%200..1-++[HasBodyShiftP],[SupportingFacilityComponent]uses%20-.->[HasBodyShiftP],[RadiationMonitor]uses%20-.->[HasBodyShiftP],[Magnet]uses%20-.->[HasBodyShiftP],[Cavity]uses%20-.->[HasBodyShiftP],[BookkeepingComponent]uses%20-.->[HasBodyShiftP],[BeamProfileMonitor]uses%20-.->[HasBodyShiftP],[BeamPositionMonitor]uses%20-.->[HasBodyShiftP],[SupportingFacilityComponent],[RadiationMonitor],[Magnet],[Cavity],[BookkeepingComponent],[BodyShiftParamGroup],[BeamProfileMonitor],[BeamPositionMonitor])](https://yuml.me/diagram/nofunky;dir:TB/class/[BodyShiftParamGroup]<BodyShiftP%200..1-++[HasBodyShiftP],[SupportingFacilityComponent]uses%20-.->[HasBodyShiftP],[RadiationMonitor]uses%20-.->[HasBodyShiftP],[Magnet]uses%20-.->[HasBodyShiftP],[Cavity]uses%20-.->[HasBodyShiftP],[BookkeepingComponent]uses%20-.->[HasBodyShiftP],[BeamProfileMonitor]uses%20-.->[HasBodyShiftP],[BeamPositionMonitor]uses%20-.->[HasBodyShiftP],[SupportingFacilityComponent],[RadiationMonitor],[Magnet],[Cavity],[BookkeepingComponent],[BodyShiftParamGroup],[BeamProfileMonitor],[BeamPositionMonitor])

## Mixin for

 * [BeamPositionMonitor](BeamPositionMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam position.
 * [BeamProfileMonitor](BeamProfileMonitor.md) (mixin)  - A diagnostic device used to measure transverse beam profile.
 * [BookkeepingComponent](BookkeepingComponent.md) (mixin)  - A virtual component that represents a bookkeeping or organizational role in the accelerator system,  such as a BeamLineSection, Marker or a Fork. These can include BeamLineSections, Markers, Forks, and other virtual components that are important for understanding  the structure and function of the accelerator system but are not physical devices.
 * [Cavity](Cavity.md) (mixin)  - A cavity used for beam acceleration or manipulation.
 * [Magnet](Magnet.md) (mixin)  - An accelerator device that produces a magnetic field for beam control.
 * [RadiationMonitor](RadiationMonitor.md) (mixin)  - A diagnostic device used to monitor radiation dose or dose rate.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) (mixin)  - A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.

## Referenced by Class


## Attributes


### Own

 * [➞BodyShiftP](hasBodyShiftP__BodyShiftP.md)  <sub>0..1</sub>
     * Description: A mixin for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [BodyShiftParamGroup](BodyShiftParamGroup.md)
