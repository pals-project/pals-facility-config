
# Class: SignalBinding

Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.

URI: [pals:SignalBinding](https://pals-project.readthedocs.io/SignalBinding)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Signal]<object%201..1-%20[SignalBinding&#124;id(i):string;predicate(i):uriorcurie],[PhysicalComponent]<subject%201..1-%20[SignalBinding],[Facility]++-%20signal_bindings%200..*>[SignalBinding],[SignalBinding]^-[HasSignal],[SignalBinding]^-[HasSetpointSignal],[SignalBinding]^-[HasReadbackSignal],[SignalBinding]^-[HasLimitSignal],[SignalBinding]^-[HasCommandSignal],[Edge]^-[SignalBinding],[Signal],[PhysicalComponent],[HasSignal],[HasSetpointSignal],[HasReadbackSignal],[HasLimitSignal],[HasCommandSignal],[Facility],[Edge])](https://yuml.me/diagram/nofunky;dir:TB/class/[Signal]<object%201..1-%20[SignalBinding&#124;id(i):string;predicate(i):uriorcurie],[PhysicalComponent]<subject%201..1-%20[SignalBinding],[Facility]++-%20signal_bindings%200..*>[SignalBinding],[SignalBinding]^-[HasSignal],[SignalBinding]^-[HasSetpointSignal],[SignalBinding]^-[HasReadbackSignal],[SignalBinding]^-[HasLimitSignal],[SignalBinding]^-[HasCommandSignal],[Edge]^-[SignalBinding],[Signal],[PhysicalComponent],[HasSignal],[HasSetpointSignal],[HasReadbackSignal],[HasLimitSignal],[HasCommandSignal],[Facility],[Edge])

## Parents

 *  is_a: [Edge](Edge.md) - Abstract base for subject-predicate-object associations.

## Children

 * [HasCommandSignal](HasCommandSignal.md)
 * [HasLimitSignal](HasLimitSignal.md)
 * [HasReadbackSignal](HasReadbackSignal.md)
 * [HasSetpointSignal](HasSetpointSignal.md)
 * [HasSignal](HasSignal.md)

## Referenced by Class

 *  **None** *[➞signal_bindings](facility__signal_bindings.md)*  <sub>0..\*</sub>  **[SignalBinding](SignalBinding.md)**

## Attributes


### Own

 * [SignalBinding➞subject](SignalBinding_subject.md)  <sub>1..1</sub>
     * Range: [PhysicalComponent](PhysicalComponent.md)
 * [SignalBinding➞object](SignalBinding_object.md)  <sub>1..1</sub>
     * Range: [Signal](Signal.md)

### Inherited from Edge:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
