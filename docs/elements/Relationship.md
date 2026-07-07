
# Class: Relationship

Abstract base for subject-predicate-object associations.

URI: [narad:Relationship](https://example.org/narad/Relationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Relationship&#124;id:string;subject:string;predicate:string;object:string]^-[SignalBinding],[Relationship]^-[ComponentRelation],[ComponentRelation])](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Relationship&#124;id:string;subject:string;predicate:string;object:string]^-[SignalBinding],[Relationship]^-[ComponentRelation],[ComponentRelation])

## Children

 * [ComponentRelation](ComponentRelation.md) - Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
 * [SignalBinding](SignalBinding.md) - Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [subject](subject.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [object](object.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
