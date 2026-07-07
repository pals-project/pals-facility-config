
# Class: ComponentRelation

Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.

URI: [narad:ComponentRelation](https://example.org/narad/ComponentRelation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Relationship],[Component]<object%201..1-%20[ComponentRelation&#124;context:RelationContextEnum%20%3F;reference_frame:ReferenceFrameEnum%20%3F;distance_value:float%20%3F;distance_unit:UnitEnum%20%3F;axis:AxisEnum%20%3F;direction:DirectionEnum%20%3F;tolerance_value:float%20%3F;tolerance_unit:UnitEnum%20%3F;predicate:ComponentRelationPredicateEnum;id(i):string],[Component]<subject%201..1-%20[ComponentRelation],[Beamline]<beamline_context%200..1-%20[ComponentRelation],[NARAD]++-%20component_relations%200..*>[ComponentRelation],[Relationship]^-[ComponentRelation],[NARAD],[Component],[Beamline])](https://yuml.me/diagram/nofunky;dir:TB/class/[Relationship],[Component]<object%201..1-%20[ComponentRelation&#124;context:RelationContextEnum%20%3F;reference_frame:ReferenceFrameEnum%20%3F;distance_value:float%20%3F;distance_unit:UnitEnum%20%3F;axis:AxisEnum%20%3F;direction:DirectionEnum%20%3F;tolerance_value:float%20%3F;tolerance_unit:UnitEnum%20%3F;predicate:ComponentRelationPredicateEnum;id(i):string],[Component]<subject%201..1-%20[ComponentRelation],[Beamline]<beamline_context%200..1-%20[ComponentRelation],[NARAD]++-%20component_relations%200..*>[ComponentRelation],[Relationship]^-[ComponentRelation],[NARAD],[Component],[Beamline])

## Parents

 *  is_a: [Relationship](Relationship.md) - Abstract base for subject-predicate-object associations.

## Referenced by Class

 *  **None** *[➞component_relations](nARAD__component_relations.md)*  <sub>0..\*</sub>  **[ComponentRelation](ComponentRelation.md)**

## Attributes


### Own

 * [➞context](componentRelation__context.md)  <sub>0..1</sub>
     * Description: The frame of reference / domain in which this relationship is asserted to hold.
     * Range: [RelationContextEnum](RelationContextEnum.md)
 * [➞beamline_context](componentRelation__beamline_context.md)  <sub>0..1</sub>
     * Description: The specific Beamline this relationship is defined with respect to (relevant when context=beamline_order).
     * Range: [Beamline](Beamline.md)
 * [➞reference_frame](componentRelation__reference_frame.md)  <sub>0..1</sub>
     * Range: [ReferenceFrameEnum](ReferenceFrameEnum.md)
 * [➞distance_value](componentRelation__distance_value.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [➞distance_unit](componentRelation__distance_unit.md)  <sub>0..1</sub>
     * Range: [UnitEnum](UnitEnum.md)
 * [➞axis](componentRelation__axis.md)  <sub>0..1</sub>
     * Range: [AxisEnum](AxisEnum.md)
 * [➞direction](componentRelation__direction.md)  <sub>0..1</sub>
     * Range: [DirectionEnum](DirectionEnum.md)
 * [➞tolerance_value](componentRelation__tolerance_value.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [➞tolerance_unit](componentRelation__tolerance_unit.md)  <sub>0..1</sub>
     * Range: [UnitEnum](UnitEnum.md)
 * [ComponentRelation➞subject](ComponentRelation_subject.md)  <sub>1..1</sub>
     * Range: [Component](Component.md)
 * [ComponentRelation➞predicate](ComponentRelation_predicate.md)  <sub>1..1</sub>
     * Range: [ComponentRelationPredicateEnum](ComponentRelationPredicateEnum.md)
 * [ComponentRelation➞object](ComponentRelation_object.md)  <sub>1..1</sub>
     * Range: [Component](Component.md)

### Inherited from Relationship:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
