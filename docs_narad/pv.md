

# Slot: pv 


_The EPICS Process Variable name (e.g. MBHK101H.S)._





URI: [https://w3id.org/narad_linkml/schema/narad/pv](https://w3id.org/narad_linkml/schema/narad/pv)
Alias: pv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/pv |
| native | https://w3id.org/narad_linkml/schema/narad/pv |




## LinkML Source

<details>
```yaml
name: pv
description: The EPICS Process Variable name (e.g. MBHK101H.S).
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: pv
domain_of:
- PVBinding
range: string

```
</details>