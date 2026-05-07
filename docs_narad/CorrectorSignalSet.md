

# Class: CorrectorSignalSet 


_Corrector-specific signal bindings._





URI: [narad:CorrectorSignalSet](https://w3id.org/narad_linkml/schema/narad/CorrectorSignalSet)





```mermaid
 classDiagram
    class CorrectorSignalSet
    click CorrectorSignalSet href "../CorrectorSignalSet/"
      CorrectorSignalSet : kick_setpoint
        
          
    
        
        
        CorrectorSignalSet --> "0..1" SignalBinding : kick_setpoint
        click SignalBinding href "../SignalBinding/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [kick_setpoint](kick_setpoint.md) | 0..1 <br/> [SignalBinding](SignalBinding.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TypeSignalSet](TypeSignalSet.md) | [corrector_signals](corrector_signals.md) | range | [CorrectorSignalSet](CorrectorSignalSet.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:CorrectorSignalSet |
| native | narad:CorrectorSignalSet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CorrectorSignalSet
description: Corrector-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- kick_setpoint

```
</details>

### Induced

<details>
```yaml
name: CorrectorSignalSet
description: Corrector-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  kick_setpoint:
    name: kick_setpoint
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: kick_setpoint
    owner: CorrectorSignalSet
    domain_of:
    - CorrectorSignalSet
    range: SignalBinding
    inlined: true

```
</details>