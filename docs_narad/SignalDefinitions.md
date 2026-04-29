

# Class: SignalDefinitions 


_EPICS signal suffix templates keyed by device type or device domain. Use a domain-level key (e.g. Magnet, RFCavity) for signals shared across all types in that domain; use a device-type key (e.g. Quadrupole, BPM) for type-specific signals. New device types require no schema changes._





URI: [https://w3id.org/narad_linkml/schema/narad/SignalDefinitions](https://w3id.org/narad_linkml/schema/narad/SignalDefinitions)





```mermaid
 classDiagram
    class SignalDefinitions
    click SignalDefinitions href "../SignalDefinitions/"
      SignalDefinitions : type_signal_sets
        
          
    
        
        
        SignalDefinitions --> "*" DeviceTypeSignalSet : type_signal_sets
        click DeviceTypeSignalSet href "../DeviceTypeSignalSet/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type_signal_sets](type_signal_sets.md) | * <br/> [DeviceTypeSignalSet](DeviceTypeSignalSet.md) | Signal suffix groups keyed by device type or device domain name | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Facility](Facility.md) | [signal_definitions](signal_definitions.md) | range | [SignalDefinitions](SignalDefinitions.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/SignalDefinitions |
| native | https://w3id.org/narad_linkml/schema/narad/SignalDefinitions |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SignalDefinitions
description: EPICS signal suffix templates keyed by device type or device domain.
  Use a domain-level key (e.g. Magnet, RFCavity) for signals shared across all types
  in that domain; use a device-type key (e.g. Quadrupole, BPM) for type-specific signals.
  New device types require no schema changes.
from_schema: https://w3id.org/narad_linkml/schema/narad/
slots:
- type_signal_sets

```
</details>

### Induced

<details>
```yaml
name: SignalDefinitions
description: EPICS signal suffix templates keyed by device type or device domain.
  Use a domain-level key (e.g. Magnet, RFCavity) for signals shared across all types
  in that domain; use a device-type key (e.g. Quadrupole, BPM) for type-specific signals.
  New device types require no schema changes.
from_schema: https://w3id.org/narad_linkml/schema/narad/
attributes:
  type_signal_sets:
    name: type_signal_sets
    description: Signal suffix groups keyed by device type or device domain name.
      Domain-level keys (e.g. Magnet, RFCavity) represent signals shared across all
      types in that domain; device-type keys (e.g. Quadrupole, BPM) are type-specific.
      New device types require no schema changes.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: type_signal_sets
    owner: SignalDefinitions
    domain_of:
    - SignalDefinitions
    range: DeviceTypeSignalSet
    multivalued: true
    inlined: true

```
</details>