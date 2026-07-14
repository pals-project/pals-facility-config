
# Enum: ComponentRelationPredicateEnum



URI: [narad:ComponentRelationPredicateEnum](https://example.org/narad/ComponentRelationPredicateEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| precedes | Subject occurs immediately before object in the sequence/beamline order. | BFO:0000063 |  |
| follows | Subject occurs after object in the sequence/beamline order. | BFO:0000062 |  |
| contains | Subject spatially or mereologically contains object. | BFO:0000051 |  |
| contained_in | Subject is spatially or mereologically contained in object. | BFO:0000050 |  |
| connected_to | Subject and object are physically connected. a is connected to b if and only if a and b are discrete structure,  and there exists some connecting structure c, such that c connects a and b | RO:0002170 |  |
| controls | Subject controls the state or behavior of object. | saref:controls |  |
| is_controlled_by | Subject is controlled by object. | saref:isControlledBy |  |
| is_part_of | Subject is a part of object. | BFO:0000050 |  |
| has_part | Subject has part object. | BFO:0000051 |  |
| adjacent_to | Subject and object are spatially adjacent, without overlapping. | RO:0002220 |  |
| overlaps | Subject and object share at least one part in common. | RO:0002131 |  |
| mounted_on | Subject is mounted on object. | narad:mounted_on |  |
| intersects | Subject intersects with object. | narad:intersects |  |
| nearest_to | Subject is nearest to object. | narad:nearest_to |  |
