
# Class: MountedOn

A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet.

URI: [pals:MountedOn](https://pals-project.readthedocs.io/MountedOn)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateSet]<coordinates%200..1-++[MountedOn&#124;predicate:uriorcurie;context(i):RelationContextEnum;component_direction(i):DirectionEnum%20%3F;reference_frame(i):ReferenceFrameEnum%20%3F;id(i):string],[ComponentRelation]^-[MountedOn],[CoordinateSet],[ComponentRelation],[Component])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateSet]<coordinates%200..1-++[MountedOn&#124;predicate:uriorcurie;context(i):RelationContextEnum;component_direction(i):DirectionEnum%20%3F;reference_frame(i):ReferenceFrameEnum%20%3F;id(i):string],[ComponentRelation]^-[MountedOn],[CoordinateSet],[ComponentRelation],[Component])

## Parents

 *  is_a: [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.

## Referenced by Class


## Attributes


### Own

 * [coordinates](coordinates.md)  <sub>0..1</sub>
     * Description: A set of coordinates that define the spatial relationship between the two components. Only an edge-property slot for edges that require a set of coordinates to define the spatial relationship between two components in a relationship.
     * Range: [CoordinateSet](CoordinateSet.md)
 * [MountedOn➞predicate](MountedOn_predicate.md)  <sub>1..1</sub>
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
| **Mappings:** | | pals:mounted_on |
| **Broad Mappings:** | | RO:0002371 |
