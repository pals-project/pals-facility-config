
# Class: HasLongitudinalPlacement

Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. 
Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
One (or both) `length` or `s_position` must be present.

URI: [narad:HasLongitudinalPlacement](https://example.org/narad/HasLongitudinalPlacement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacement&#124;length:float%20%3F;s_position:float%20%3F],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacement],[SupportingFacilityComponent],[PhysicalComponent])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFacilityComponent]uses%20-.->[HasLongitudinalPlacement&#124;length:float%20%3F;s_position:float%20%3F],[PhysicalComponent]uses%20-.->[HasLongitudinalPlacement],[SupportingFacilityComponent],[PhysicalComponent])

## Mixin for

 * [PhysicalComponent](PhysicalComponent.md) (mixin)  - A physical item that participates in or supports accelerator operation.  This can be used to capture physical components, such as magnets, cavities, diagnostics, vacuum devices, and racks that are important for understanding the structure and function of the accelerator system.
 * [SupportingFacilityComponent](SupportingFacilityComponent.md) (mixin)  - A physical component that supports accelerator operation

## Referenced by Class


## Attributes


### Own

 * [➞length](hasLongitudinalPlacement__length.md)  <sub>0..1</sub>
     * Description: Length of the element (arc length for bends).
     * Range: [Float](types/Float.md)
 * [➞s_position](hasLongitudinalPlacement__s_position.md)  <sub>0..1</sub>
     * Description: Longitudinal position of the element along the beamline.
     * Range: [Float](types/Float.md)
