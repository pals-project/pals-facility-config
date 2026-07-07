
# Class: SignalBinding

Association between a PhysicalComponent and one of its Signals, e.g. QUAD1.QUAD1_STATUS_binding.

URI: [narad:SignalBinding](https://example.org/narad/SignalBinding)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Signal]<object%201..1-%20[SignalBinding&#124;predicate:SignalBindingPredicateEnum;id(i):string],[PhysicalComponent]<subject%201..1-%20[SignalBinding],[NARAD]++-%20signal_bindings%200..*>[SignalBinding],[Relationship]^-[SignalBinding],[Signal],[Relationship],[PhysicalComponent],[NARAD])](https://yuml.me/diagram/nofunky;dir:TB/class/[Signal]<object%201..1-%20[SignalBinding&#124;predicate:SignalBindingPredicateEnum;id(i):string],[PhysicalComponent]<subject%201..1-%20[SignalBinding],[NARAD]++-%20signal_bindings%200..*>[SignalBinding],[Relationship]^-[SignalBinding],[Signal],[Relationship],[PhysicalComponent],[NARAD])

## Parents

 *  is_a: [Relationship](Relationship.md) - Abstract base for subject-predicate-object associations.

## Referenced by Class

 *  **None** *[➞signal_bindings](nARAD__signal_bindings.md)*  <sub>0..\*</sub>  **[SignalBinding](SignalBinding.md)**

## Attributes


### Own

 * [SignalBinding➞subject](SignalBinding_subject.md)  <sub>1..1</sub>
     * Range: [PhysicalComponent](PhysicalComponent.md)
 * [SignalBinding➞predicate](SignalBinding_predicate.md)  <sub>1..1</sub>
     * Range: [SignalBindingPredicateEnum](SignalBindingPredicateEnum.md)
 * [SignalBinding➞object](SignalBinding_object.md)  <sub>1..1</sub>
     * Range: [Signal](Signal.md)

### Inherited from Relationship:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
