

# Class: DipoleSignalSet 


_Dipole-specific signal bindings._





URI: [narad:DipoleSignalSet](https://w3id.org/narad_linkml/schema/narad/DipoleSignalSet)





```mermaid
 classDiagram
    class DipoleSignalSet
    click DipoleSignalSet href "../DipoleSignalSet/"
      DipoleSignalSet : field_setpoint
        
          
    
        
        
        DipoleSignalSet --> "0..1" SignalBinding : field_setpoint
        click SignalBinding href "../SignalBinding/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [field_setpoint](field_setpoint.md) | 0..1 <br/> [SignalBinding](SignalBinding.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TypeSignalSet](TypeSignalSet.md) | [dipole_signals](dipole_signals.md) | range | [DipoleSignalSet](DipoleSignalSet.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:DipoleSignalSet |
| native | narad:DipoleSignalSet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DipoleSignalSet
description: Dipole-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- field_setpoint

```
</details>

### Induced

<details>
```yaml
name: DipoleSignalSet
description: Dipole-specific signal bindings.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  field_setpoint:
    name: field_setpoint
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: field_setpoint
    owner: DipoleSignalSet
    domain_of:
    - DipoleSignalSet
    range: SignalBinding
    inlined: true

```
</details>