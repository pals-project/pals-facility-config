
# Class: HasConnectingBranch

A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch.

URI: [pals:HasConnectingBranch](https://pals-project.readthedocs.io/HasConnectingBranch)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BeamLine]<beamline_context%201..1-%20[HasConnectingBranch&#124;predicate:uriorcurie;context:RelationContextEnum;component_direction(i):DirectionEnum%20%3F;reference_frame(i):ReferenceFrameEnum%20%3F;id(i):string],[ComponentRelation]^-[HasConnectingBranch],[ComponentRelation],[Component],[BeamLine])](https://yuml.me/diagram/nofunky;dir:TB/class/[BeamLine]<beamline_context%201..1-%20[HasConnectingBranch&#124;predicate:uriorcurie;context:RelationContextEnum;component_direction(i):DirectionEnum%20%3F;reference_frame(i):ReferenceFrameEnum%20%3F;id(i):string],[ComponentRelation]^-[HasConnectingBranch],[ComponentRelation],[Component],[BeamLine])

## Parents

 *  is_a: [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.

## Referenced by Class


## Attributes


### Own

 * [beamline_context](beamline_context.md)  <sub>1..1</sub>
     * Description: The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine.
     * Range: [BeamLine](BeamLine.md)
 * [HasConnectingBranch➞predicate](HasConnectingBranch_predicate.md)  <sub>1..1</sub>
     * Description: The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [HasConnectingBranch➞context](HasConnectingBranch_context.md)  <sub>1..1</sub>
     * Description: The frame of reference / domain in which this relationship is asserted to hold. For pals:has_connecting_branch, this is the Beamline context = beamline_context.
     * Range: [RelationContextEnum](RelationContextEnum.md)

### Inherited from ComponentRelation:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
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
| **Mappings:** | | pals:has_connecting_branch |
| **Exact Mappings:** | | RO:0002253 |
