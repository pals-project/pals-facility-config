

# Class: SignalBinding 


_A named control system suffix definition for one semantic signal. The suffix is used within in a template naming convention to construct the full control system PV name for a given device instance._





URI: [narad:SignalBinding](https://w3id.org/narad_linkml/schema/narad/SignalBinding)





```mermaid
 classDiagram
    class SignalBinding
    click SignalBinding href "../SignalBinding/"
      NamedThing <|-- SignalBinding
        click NamedThing href "../NamedThing/"
      
      SignalBinding : control_system_suffix
        
      SignalBinding : description
        
      SignalBinding : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **SignalBinding**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [control_system_suffix](control_system_suffix.md) | 0..1 <br/> [String](String.md) | Facility-specific control-system (e | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name or local string key for the entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SignalDefinitions](SignalDefinitions.md) | [signal_bindings](signal_bindings.md) | range | [SignalBinding](SignalBinding.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:SignalBinding |
| native | narad:SignalBinding |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SignalBinding
description: A named control system suffix definition for one semantic signal. The
  suffix is used within in a template naming convention to construct the full control
  system PV name for a given device instance.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: NamedThing
slots:
- control_system_suffix

```
</details>

### Induced

<details>
```yaml
name: SignalBinding
description: A named control system suffix definition for one semantic signal. The
  suffix is used within in a template naming convention to construct the full control
  system PV name for a given device instance.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
is_a: NamedThing
attributes:
  control_system_suffix:
    name: control_system_suffix
    description: 'Facility-specific control-system (e.g. EPICS) naming suffix used
      to derive or interpret the signal binding, e.g. .S, M, :GSET.

      '
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: control_system_suffix
    owner: SignalBinding
    domain_of:
    - SignalBinding
    range: string
  name:
    name: name
    description: Human-readable name or local string key for the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: name
    owner: SignalBinding
    domain_of:
    - NamedThing
    range: string
    required: true
  description:
    name: description
    description: Detailed description of the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: description
    owner: SignalBinding
    domain_of:
    - NamedThing
    range: string

```
</details>