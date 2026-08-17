
# Class: AdjacentTo

A relationship indicating that the subject component is adjacent to the object component and not overlapping
 in a specified context, such as radiation detector and a magnet.

URI: [pals:AdjacentTo](https://pals-project.readthedocs.io/AdjacentTo)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateSet],[ComponentRelation],[Component],[CoordinateSet]<coordinates%200..1-++[AdjacentTo&#124;distance_value:float%20%3F;distance_unit:UnitEnum%20%3F;tolerance_value:float%20%3F;tolerance_unit:UnitEnum%20%3F;predicate:uriorcurie;context(i):RelationContextEnum;component_direction(i):DirectionEnum%20%3F;reference_frame(i):ReferenceFrameEnum%20%3F;id(i):string],[ComponentRelation]^-[AdjacentTo])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateSet],[ComponentRelation],[Component],[CoordinateSet]<coordinates%200..1-++[AdjacentTo&#124;distance_value:float%20%3F;distance_unit:UnitEnum%20%3F;tolerance_value:float%20%3F;tolerance_unit:UnitEnum%20%3F;predicate:uriorcurie;context(i):RelationContextEnum;component_direction(i):DirectionEnum%20%3F;reference_frame(i):ReferenceFrameEnum%20%3F;id(i):string],[ComponentRelation]^-[AdjacentTo])

## Parents

 *  is_a: [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.

## Referenced by Class


## Attributes


### Own

 * [distance_value](distance_value.md)  <sub>0..1</sub>
     * Description: Distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.
     * Range: [Float](types/Float.md)
 * [distance_unit](distance_unit.md)  <sub>0..1</sub>
     * Description: Unit of the distance value between two components in a relationship. Only an edge-property slot for edges that require a distance value between two components in a relationship.
     * Range: [UnitEnum](UnitEnum.md)
 * [tolerance_value](tolerance_value.md)  <sub>0..1</sub>
     * Description: Tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.
     * Range: [Float](types/Float.md)
 * [tolerance_unit](tolerance_unit.md)  <sub>0..1</sub>
     * Description: Unit of the tolerance value for the distance between two components in a relationship. Only an edge-property slot for edges that require a tolerance value between two components in a relationship.
     * Range: [UnitEnum](UnitEnum.md)
 * [coordinates](coordinates.md)  <sub>0..1</sub>
     * Description: A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.
     * Range: [CoordinateSet](CoordinateSet.md)
 * [AdjacentTo➞predicate](AdjacentTo_predicate.md)  <sub>1..1</sub>
     * Description: The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from ComponentRelation:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [context](context.md)  <sub>1..1</sub>
     * Description: The frame of reference / domain in which this relationship is asserted to hold.
     * Range: [RelationContextEnum](RelationContextEnum.md)
 * [➞component_direction](componentRelation__component_direction.md)  <sub>0..1</sub>
     * Range: [DirectionEnum](DirectionEnum.md)
 * [➞reference_frame](componentRelation__reference_frame.md)  <sub>0..1</sub>
     * Range: [ReferenceFrameEnum](ReferenceFrameEnum.md)
 * [ComponentRelation➞subject](ComponentRelation_subject.md)  <sub>1..1</sub>
     * Range: [Component](Component.md)
 * [ComponentRelation➞object](ComponentRelation_object.md)  <sub>1..1</sub>
     * Range: [Component](Component.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | pals:adjacent_to |
| **Exact Mappings:** | | RO:0002220 |
