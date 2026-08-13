
# Class: HasReadbackSignal



URI: [pals:HasReadbackSignal](https://pals-project.readthedocs.io/HasReadbackSignal)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Signal],[PhysicalComponent],[SignalBinding]^-[HasReadbackSignal&#124;predicate:uriorcurie;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Signal],[PhysicalComponent],[SignalBinding]^-[HasReadbackSignal&#124;predicate:uriorcurie;id(i):string])

## Parents

 *  is_a: [SignalBinding](SignalBinding.md) - Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.

## Referenced by Class


## Attributes


### Own

 * [HasReadbackSignal➞predicate](HasReadbackSignal_predicate.md)  <sub>1..1</sub>
     * Description: The predicate of the relationship, which can be used to identify the relationship across different source systems.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from SignalBinding:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [SignalBinding➞subject](SignalBinding_subject.md)  <sub>1..1</sub>
     * Range: [PhysicalComponent](PhysicalComponent.md)
 * [SignalBinding➞object](SignalBinding_object.md)  <sub>1..1</sub>
     * Range: [Signal](Signal.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | pals:has_readback_signal |
