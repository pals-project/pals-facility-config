
# Class: HasLongitudinalPlacementP



URI: [pals:HasLongitudinalPlacementP](https://pals-project.readthedocs.io/HasLongitudinalPlacementP)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[LongitudinalPlacementParamGroup],[LongitudinalPlacementParamGroup]<LongitudinalPlacementP%200..1-++[HasLongitudinalPlacementP],[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacementP],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacementP],[SupportingFacilityComponent],[PhysicalComponent])](https://yuml.me/diagram/nofunky;dir:TB/class/[LongitudinalPlacementParamGroup],[LongitudinalPlacementParamGroup]<LongitudinalPlacementP%200..1-++[HasLongitudinalPlacementP],[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacementP],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacementP],[SupportingFacilityComponent],[PhysicalComponent])

## Mixin for

 * [PhysicalComponent](PhysicalComponent.md) (mixin)  - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) (mixin)  - A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline.

## Referenced by Class


## Attributes


### Own

 * [➞LongitudinalPlacementP](hasLongitudinalPlacementP__LongitudinalPlacementP.md)  <sub>0..1</sub>
     * Description: A mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis that are aligned with PALS LongitudinalPlacementP (Longitudinal Placement Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
     * Range: [LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md)
