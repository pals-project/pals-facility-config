
# Class: LongitudinalPlacementParamGroup

Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present.

URI: [pals:LongitudinalPlacementParamGroup](https://pals-project.readthedocs.io/LongitudinalPlacementParamGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasLongitudinalPlacementP]++-%20LongitudinalPlacementP%200..1>[LongitudinalPlacementParamGroup&#124;length:float%20%3F;s_position:float%20%3F;id(i):string],[ParamGroup]^-[LongitudinalPlacementParamGroup],[HasLongitudinalPlacementP])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParamGroup],[HasLongitudinalPlacementP]++-%20LongitudinalPlacementP%200..1>[LongitudinalPlacementParamGroup&#124;length:float%20%3F;s_position:float%20%3F;id(i):string],[ParamGroup]^-[LongitudinalPlacementParamGroup],[HasLongitudinalPlacementP])

## Parents

 *  is_a: [ParamGroup](ParamGroup.md) - Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.

## Referenced by Class

 *  **None** *[➞LongitudinalPlacementP](hasLongitudinalPlacementP__LongitudinalPlacementP.md)*  <sub>0..1</sub>  **[LongitudinalPlacementParamGroup](LongitudinalPlacementParamGroup.md)**

## Attributes


### Own

 * [length](length.md)  <sub>0..1</sub>
     * Description: Length of the element (arc length for bends).
     * Range: [Float](types/Float.md)
 * [➞s_position](longitudinalPlacementParamGroup__s_position.md)  <sub>0..1</sub>
     * Description: Longitudinal position of the element along the beamline.
     * Range: [Float](types/Float.md)

### Inherited from ParamGroup:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
