

# Slot: units 


_Conventional unit symbol (e.g. A, MV/m, T*m, G/cm)._





URI: [https://w3id.org/narad_linkml/schema/narad/units](https://w3id.org/narad_linkml/schema/narad/units)
Alias: units

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/units |
| native | https://w3id.org/narad_linkml/schema/narad/units |
| broad | si-unit:Unit |




## LinkML Source

<details>
```yaml
name: units
description: Conventional unit symbol (e.g. A, MV/m, T*m, G/cm).
from_schema: https://w3id.org/narad_linkml/schema/narad/
broad_mappings:
- si-unit:Unit
rank: 1000
alias: units
domain_of:
- Signal
range: string

```
</details>