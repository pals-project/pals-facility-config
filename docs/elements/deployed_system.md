

# Slot: deployed_system 


_Identifier of the deployed system this configuration describes._





URI: [narad:deployed_system](https://example.org/narad_linkml/schema/narad/deployed_system)
Alias: deployed_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradConfig](NaradConfig.md) | A top-level NARAD-system container for the: capability layer + signal layer |  yes  |






## Properties

* Range: [DeployedSystem](DeployedSystem.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:deployed_system |
| native | narad:deployed_system |




## LinkML Source

<details>
```yaml
name: deployed_system
description: Identifier of the deployed system this configuration describes.
in_subset:
- instance
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: deployed_system
domain_of:
- NaradConfig
range: DeployedSystem
required: true
multivalued: false

```
</details>