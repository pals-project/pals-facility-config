
# Class: NARAD

Root container for accelerator core components, semantic signals, and local bindings.

URI: [narad:NARAD](https://example.org/narad/NARAD)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[SupportingFacilityComponent],[SignalBinding],[Signal],[PhysicalComponent],[ComponentRelation]<component_relations%200..*-++[NARAD&#124;description:string%20%3F],[SignalBinding]<signal_bindings%200..*-++[NARAD],[Signal]<signals%200..*-++[NARAD],[SupportingFacilityComponent]<supporting_facility_components%200..*-++[NARAD],[Beamline]<beamlines%200..*-++[NARAD],[VirtualComponent]<virtual_components%200..*-++[NARAD],[PhysicalComponent]<physical_components%200..*-++[NARAD],[Component]<type%201..1-%20[NARAD],[ComponentRelation],[Component],[Beamline])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirtualComponent],[SupportingFacilityComponent],[SignalBinding],[Signal],[PhysicalComponent],[ComponentRelation]<component_relations%200..*-++[NARAD&#124;description:string%20%3F],[SignalBinding]<signal_bindings%200..*-++[NARAD],[Signal]<signals%200..*-++[NARAD],[SupportingFacilityComponent]<supporting_facility_components%200..*-++[NARAD],[Beamline]<beamlines%200..*-++[NARAD],[VirtualComponent]<virtual_components%200..*-++[NARAD],[PhysicalComponent]<physical_components%200..*-++[NARAD],[Component]<type%201..1-%20[NARAD],[ComponentRelation],[Component],[Beamline])

## Attributes


### Own

 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [Component](Component.md)
 * [➞description](nARAD__description.md)  <sub>0..1</sub>
     * Description: Human-readable description for the representation of a particle accelerator and its operations.
     * Range: [String](types/String.md)
 * [➞physical_components](nARAD__physical_components.md)  <sub>0..\*</sub>
     * Description: A list of physical components in the accelerator system.
     * Range: [PhysicalComponent](PhysicalComponent.md)
 * [➞virtual_components](nARAD__virtual_components.md)  <sub>0..\*</sub>
     * Description: A list of virtual components in the accelerator system.
     * Range: [VirtualComponent](VirtualComponent.md)
 * [➞beamlines](nARAD__beamlines.md)  <sub>0..\*</sub>
     * Description: A list of beamlines in the accelerator system.
     * Range: [Beamline](Beamline.md)
 * [➞supporting_facility_components](nARAD__supporting_facility_components.md)  <sub>0..\*</sub>
     * Description: A list of supporting facility components in the accelerator system.
     * Range: [SupportingFacilityComponent](SupportingFacilityComponent.md)
 * [➞signals](nARAD__signals.md)  <sub>0..\*</sub>
     * Description: A list of signals in the accelerator system.
     * Range: [Signal](Signal.md)
 * [➞signal_bindings](nARAD__signal_bindings.md)  <sub>0..\*</sub>
     * Description: A list of signal bindings in the accelerator system (Component <-> Signal relationships).
     * Range: [SignalBinding](SignalBinding.md)
 * [➞component_relations](nARAD__component_relations.md)  <sub>0..\*</sub>
     * Description: A list of component relations in the accelerator system (Component <-> Component relationships).
     * Range: [ComponentRelation](ComponentRelation.md)
