

# Class: CapabilityLayer 


_Capability-layer container for control profile families._





URI: [narad:CapabilityLayer](https://w3id.org/narad_linkml/schema/narad/CapabilityLayer)





```mermaid
 classDiagram
    class CapabilityLayer
    click CapabilityLayer href "../CapabilityLayer/"
      CapabilityLayer : control_capabilities
        
          
    
        
        
        CapabilityLayer --> "*" ControlCapability : control_capabilities
        click ControlCapability href "../ControlCapability/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [control_capabilities](control_capabilities.md) | * <br/> [ControlCapability](ControlCapability.md) |  | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:CapabilityLayer |
| native | narad:CapabilityLayer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CapabilityLayer
description: Capability-layer container for control profile families.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- control_capabilities

```
</details>

### Induced

<details>
```yaml
name: CapabilityLayer
description: Capability-layer container for control profile families.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  control_capabilities:
    name: control_capabilities
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: control_capabilities
    owner: CapabilityLayer
    domain_of:
    - CapabilityLayer
    range: ControlCapability
    multivalued: true
    inlined: true

```
</details>