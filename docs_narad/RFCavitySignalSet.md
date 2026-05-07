

# Class: RFCavitySignalSet 


_RF cavity-specific signal bindings._





URI: [narad:RFCavitySignalSet](https://w3id.org/narad_linkml/schema/narad/RFCavitySignalSet)





```mermaid
 classDiagram
    class RFCavitySignalSet
    click RFCavitySignalSet href "../RFCavitySignalSet/"
      RFCavitySignalSet : gradient_readback
        
          
    
        
        
        RFCavitySignalSet --> "0..1" SignalBinding : gradient_readback
        click SignalBinding href "../SignalBinding/"
    

        
      RFCavitySignalSet : gradient_setpoint
        
          
    
        
        
        RFCavitySignalSet --> "0..1" SignalBinding : gradient_setpoint
        click SignalBinding href "../SignalBinding/"
    

        
      RFCavitySignalSet : status
        
          
    
        
        
        RFCavitySignalSet --> "0..1" SignalBinding : status
        click SignalBinding href "../SignalBinding/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [gradient_setpoint](gradient_setpoint.md) | 0..1 <br/> [SignalBinding](SignalBinding.md) |  | direct |
| [gradient_readback](gradient_readback.md) | 0..1 <br/> [SignalBinding](SignalBinding.md) |  | direct |
| [status](status.md) | 0..1 <br/> [SignalBinding](SignalBinding.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TypeSignalSet](TypeSignalSet.md) | [rfcavity_signals](rfcavity_signals.md) | range | [RFCavitySignalSet](RFCavitySignalSet.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:RFCavitySignalSet |
| native | narad:RFCavitySignalSet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RFCavitySignalSet
description: RF cavity-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- gradient_setpoint
- gradient_readback
- status

```
</details>

### Induced

<details>
```yaml
name: RFCavitySignalSet
description: RF cavity-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  gradient_setpoint:
    name: gradient_setpoint
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: gradient_setpoint
    owner: RFCavitySignalSet
    domain_of:
    - RFCavitySignalSet
    range: SignalBinding
    inlined: true
  gradient_readback:
    name: gradient_readback
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: gradient_readback
    owner: RFCavitySignalSet
    domain_of:
    - RFCavitySignalSet
    range: SignalBinding
    inlined: true
  status:
    name: status
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: status
    owner: RFCavitySignalSet
    domain_of:
    - MagnetSignalSet
    - BPMSignalSet
    - RFCavitySignalSet
    range: SignalBinding
    inlined: true

```
</details>