
# Class: Edge

Abstract base for subject-predicate-object associations.

URI: [pals:Edge](https://pals-project.readthedocs.io/Edge)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Edge&#124;id:string;subject:string;predicate:uriorcurie;object:string]^-[SignalBinding],[Edge]^-[ComponentRelation],[ComponentRelation])](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Edge&#124;id:string;subject:string;predicate:uriorcurie;object:string]^-[SignalBinding],[Edge]^-[ComponentRelation],[ComponentRelation])

## Children

 * [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
 * [SignalBinding](SignalBinding.md) - Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [object](object.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | rdf:Statement |
