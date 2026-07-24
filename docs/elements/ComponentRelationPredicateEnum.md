# Enum: ComponentRelationPredicateEnum 



URI: [pals:ComponentRelationPredicateEnum](https://pals-project.readthedocs.io/ComponentRelationPredicateEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| precedes | BFO:0000063 | Subject occurs immediately before object in the sequence/beamline order |
| follows | BFO:0000062 | Subject occurs after object in the sequence/beamline order |
| contains | BFO:0000051 | Subject spatially or mereologically contains object |
| contained_in | BFO:0000050 | Subject is spatially or mereologically contained in object |
| connected_to | RO:0002170 | Subject and object are physically connected |
| controls | saref:controls | Subject controls the state or behavior of object |
| is_controlled_by | saref:isControlledBy | Subject is controlled by object |
| is_part_of | BFO:0000050 | Subject is a part of object |
| has_part | BFO:0000051 | Subject has part object |
| adjacent_to | RO:0002220 | Subject and object are spatially adjacent, without overlapping |
| overlaps | RO:0002131 | Subject and object share at least one part in common |
| mounted_on | pals:mounted_on | Subject is mounted on object |
| intersects | pals:intersects | Subject intersects with object |
| nearest_to | pals:nearest_to | Subject is nearest to object |




## Slots

| Name | Description |
| ---  | --- |
| [predicate](predicate.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: ComponentRelationPredicateEnum
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  precedes:
    text: precedes
    description: Subject occurs immediately before object in the sequence/beamline
      order.
    meaning: BFO:0000063
  follows:
    text: follows
    description: Subject occurs after object in the sequence/beamline order.
    meaning: BFO:0000062
  contains:
    text: contains
    description: Subject spatially or mereologically contains object.
    meaning: BFO:0000051
  contained_in:
    text: contained_in
    description: Subject is spatially or mereologically contained in object.
    meaning: BFO:0000050
  connected_to:
    text: connected_to
    description: Subject and object are physically connected. a is connected to b
      if and only if a and b are discrete structure,  and there exists some connecting
      structure c, such that c connects a and b
    meaning: RO:0002170
  controls:
    text: controls
    description: Subject controls the state or behavior of object.
    meaning: saref:controls
  is_controlled_by:
    text: is_controlled_by
    description: Subject is controlled by object.
    meaning: saref:isControlledBy
  is_part_of:
    text: is_part_of
    description: Subject is a part of object.
    meaning: BFO:0000050
  has_part:
    text: has_part
    description: Subject has part object.
    meaning: BFO:0000051
  adjacent_to:
    text: adjacent_to
    description: Subject and object are spatially adjacent, without overlapping.
    meaning: RO:0002220
  overlaps:
    text: overlaps
    description: Subject and object share at least one part in common.
    meaning: RO:0002131
  mounted_on:
    text: mounted_on
    description: Subject is mounted on object.
    meaning: pals:mounted_on
  intersects:
    text: intersects
    description: Subject intersects with object.
    meaning: pals:intersects
  nearest_to:
    text: nearest_to
    description: Subject is nearest to object.
    meaning: pals:nearest_to

```
</details>