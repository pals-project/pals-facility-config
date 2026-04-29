

# Slot: id 


_Unique identifier for the entity._





URI: [https://w3id.org/narad_linkml/schema/narad/id](https://w3id.org/narad_linkml/schema/narad/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |  no  |
| [Relationship](Relationship.md) | A directed edge type in the NARAD graph projection, modelled after the OBO Re... |  yes  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/id |
| native | https://w3id.org/narad_linkml/schema/narad/id |




## LinkML Source

<details>
```yaml
name: id
description: Unique identifier for the entity.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
identifier: true
alias: id
domain_of:
- TypeSpecificCapability
- Relationship
range: string
required: true

```
</details>