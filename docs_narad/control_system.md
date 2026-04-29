

# Slot: control_system 



URI: [https://w3id.org/narad_linkml/schema/narad/control_system](https://w3id.org/narad_linkml/schema/narad/control_system)
Alias: control_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](Facility.md) | A facility with specific signal bindings |  no  |
| [NaradConfig](NaradConfig.md) | NARAD configuration block containing the capability layer |  no  |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/control_system |
| native | https://w3id.org/narad_linkml/schema/narad/control_system |




## LinkML Source

<details>
```yaml
name: control_system
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: control_system
domain_of:
- NaradConfig
- Facility
- PVBinding
range: string

```
</details>