

# Slot: periodic 


_For a beamline, indicates whether the orbit and Twiss parameters are periodic (true) or non-periodic (false)._





URI: [narad:periodic](https://w3id.org/narad_linkml/schema/narad/periodic)
Alias: periodic

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Beamline](Beamline.md) | A top-level NARAD-system for an ordered sequence of beamline elements definin... |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:periodic |
| native | narad:periodic |




## LinkML Source

<details>
```yaml
name: periodic
description: For a beamline, indicates whether the orbit and Twiss parameters are
  periodic (true) or non-periodic (false).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: periodic
domain_of:
- Beamline
range: boolean

```
</details>