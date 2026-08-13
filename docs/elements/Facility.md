
# Class: Facility

A facility that houses one or more accelerators.

URI: [pals:Facility](https://pals-project.readthedocs.io/Facility)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Signal],[Identifier],[ComponentRelation]<component_relations%200..*-++[Facility],[SignalBinding]<signal_bindings%200..*-++[Facility],[Signal]<signals%200..*-++[Facility],[BeamLine]<beamlines%200..*-++[Facility],[Component]<components%200..*-++[Facility],[Identifier]<identifiers%200..*-++[Facility],[PALSAccelerator]++-%20facility%200..1>[Facility],[PALSAccelerator],[ComponentRelation],[Component],[BeamLine])](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Signal],[Identifier],[ComponentRelation]<component_relations%200..*-++[Facility],[SignalBinding]<signal_bindings%200..*-++[Facility],[Signal]<signals%200..*-++[Facility],[BeamLine]<beamlines%200..*-++[Facility],[Component]<components%200..*-++[Facility],[Identifier]<identifiers%200..*-++[Facility],[PALSAccelerator]++-%20facility%200..1>[Facility],[PALSAccelerator],[ComponentRelation],[Component],[BeamLine])

## Referenced by Class

 *  **None** *[➞facility](pALSAccelerator__facility.md)*  <sub>0..1</sub>  **[Facility](Facility.md)**

## Attributes


### Own

 * [identifiers](identifiers.md)  <sub>0..\*</sub>
     * Description: A unique and ideally persistent identifier for the facility, such as a DOI or ROR.
     * Range: [Identifier](Identifier.md)
 * [➞components](facility__components.md)  <sub>0..\*</sub>
     * Description: A list of physical components in the accelerator system.
     * Range: [Component](Component.md)
 * [➞beamlines](facility__beamlines.md)  <sub>0..\*</sub>
     * Description: A list of beamlines in the accelerator system.
     * Range: [BeamLine](BeamLine.md)
 * [➞signals](facility__signals.md)  <sub>0..\*</sub>
     * Description: A list of signals in the accelerator system.
     * Range: [Signal](Signal.md)
 * [➞signal_bindings](facility__signal_bindings.md)  <sub>0..\*</sub>
     * Description: A list of signal bindings in the accelerator system (Component <-> Signal relationships).
     * Range: [SignalBinding](SignalBinding.md)
 * [➞component_relations](facility__component_relations.md)  <sub>0..\*</sub>
     * Description: A list of component relations in the accelerator system (Component <-> Component relationships).
     * Range: [ComponentRelation](ComponentRelation.md)
