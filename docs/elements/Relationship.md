# Subset: Relationship 


_Relationships between systems, capabilities, and signals, including system decomposition and capability assignment._



URI: [Relationship](Relationship.md)



## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system































































        



        


        

        

        

        




        

        

        

        




















        



















## Slots in subset

| Slot | Description |
| --- | --- |
| [for_property](for_property.md) | SystemCapability → Signal: the capability can expose, monitor, control, or ac... |
| [has_control_system](has_control_system.md) | Relates a System to one of its control systems (SSN alignment to sub system) |
| [has_signal](has_signal.md) | Signals within a capability, keyed by a semantic signal name |
| [has_sub_system](has_sub_system.md) | Relates a System to one of its subsystems (SSN alignment) |
| [has_system_capability](has_system_capability.md) | Relates a System to a SystemCapability it supports (SSN-System alignment) |
| [hosts_device](hosts_device.md) | Structured container for facility-specific signal suffix templates |
| [is_hosted_by](is_hosted_by.md) | Links an InstanceSignalBinding to the FacilitySystem it belongs to |
| [is_instance_of](is_instance_of.md) | NARAD alias for rdf:type |
| [is_observed_by](is_observed_by.md) | Control-system-specific, e |
| [is_property_of](is_property_of.md) | Inverse of for_property: links the Class Signal to the Class of SignalBinding... |
| [subclass_of](subclass_of.md) | -> NARAD alias for rdfs:subClassOf |


