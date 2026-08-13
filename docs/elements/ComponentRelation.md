
# Class: ComponentRelation

Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.

URI: [pals:ComponentRelation](https://pals-project.readthedocs.io/ComponentRelation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Precedes],[Overlaps],[NearestTo],[MountedOn],[IsPartOf],[Intersects],[HasConnectingBranch],[Edge],[Controls],[Contains],[Component]<object%201..1-%20[ComponentRelation&#124;context:RelationContextEnum;component_direction:DirectionEnum%20%3F;reference_frame:ReferenceFrameEnum%20%3F;id(i):string;predicate(i):uriorcurie],[Component]<subject%201..1-%20[ComponentRelation],[Facility]++-%20component_relations%200..*>[ComponentRelation],[ComponentRelation]^-[Precedes],[ComponentRelation]^-[Overlaps],[ComponentRelation]^-[NearestTo],[ComponentRelation]^-[MountedOn],[ComponentRelation]^-[IsPartOf],[ComponentRelation]^-[Intersects],[ComponentRelation]^-[HasConnectingBranch],[ComponentRelation]^-[Controls],[ComponentRelation]^-[Contains],[ComponentRelation]^-[AdjacentTo],[Edge]^-[ComponentRelation],[Facility],[Component],[AdjacentTo])](https://yuml.me/diagram/nofunky;dir:TB/class/[Precedes],[Overlaps],[NearestTo],[MountedOn],[IsPartOf],[Intersects],[HasConnectingBranch],[Edge],[Controls],[Contains],[Component]<object%201..1-%20[ComponentRelation&#124;context:RelationContextEnum;component_direction:DirectionEnum%20%3F;reference_frame:ReferenceFrameEnum%20%3F;id(i):string;predicate(i):uriorcurie],[Component]<subject%201..1-%20[ComponentRelation],[Facility]++-%20component_relations%200..*>[ComponentRelation],[ComponentRelation]^-[Precedes],[ComponentRelation]^-[Overlaps],[ComponentRelation]^-[NearestTo],[ComponentRelation]^-[MountedOn],[ComponentRelation]^-[IsPartOf],[ComponentRelation]^-[Intersects],[ComponentRelation]^-[HasConnectingBranch],[ComponentRelation]^-[Controls],[ComponentRelation]^-[Contains],[ComponentRelation]^-[AdjacentTo],[Edge]^-[ComponentRelation],[Facility],[Component],[AdjacentTo])

## Parents

 *  is_a: [Edge](Edge.md) - Abstract base for subject-predicate-object associations.

## Children

 * [AdjacentTo](AdjacentTo.md) - A relationship indicating that the subject component is adjacent to the object component and not overlapping
 * [Contains](Contains.md) - A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping.
 * [Controls](Controls.md) - A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet.
 * [HasConnectingBranch](HasConnectingBranch.md) - A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch.
 * [Intersects](Intersects.md) - A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device.
 * [IsPartOf](IsPartOf.md) - A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection.
 * [MountedOn](MountedOn.md) - A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet.
 * [NearestTo](NearestTo.md) - A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet.
 * [Overlaps](Overlaps.md) - A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device.
 * [Precedes](Precedes.md) - A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline.

## Referenced by Class

 *  **None** *[➞component_relations](facility__component_relations.md)*  <sub>0..\*</sub>  **[ComponentRelation](ComponentRelation.md)**

## Attributes


### Own

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

### Inherited from Edge:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
