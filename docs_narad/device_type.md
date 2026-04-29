

# Slot: device_type 


_The specific device type this capability profile targets (e.g. Quadrupole, Corrector, BPM). Uses ElementKindEnum to stay in sync with BeamlineElement.kind._





URI: [https://w3id.org/narad_linkml/schema/narad/device_type](https://w3id.org/narad_linkml/schema/narad/device_type)
Alias: device_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |






## Properties

* Range: [ElementKindEnum](ElementKindEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/device_type |
| native | https://w3id.org/narad_linkml/schema/narad/device_type |




## LinkML Source

<details>
```yaml
name: device_type
description: The specific device type this capability profile targets (e.g. Quadrupole,
  Corrector, BPM). Uses ElementKindEnum to stay in sync with BeamlineElement.kind.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: device_type
domain_of:
- CapabilityProfile
range: ElementKindEnum

```
</details>