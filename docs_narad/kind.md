

# Slot: kind 


_Generic kind/type label. Used for Beamline entries (e.g. BeamLine). For ControlProfileFamily device domain use device_domain: DeviceDomainEnum. For CapabilityProfile device type use device_type: ElementKindEnum._





URI: [https://w3id.org/narad_linkml/schema/narad/kind](https://w3id.org/narad_linkml/schema/narad/kind)
Alias: kind

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Beamline](Beamline.md) | An ordered sequence of beamline elements defining a beam path |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |  yes  |






## Properties

* Range: [String](String.md)



## Aliases


* type
* profile_type


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/kind |
| native | https://w3id.org/narad_linkml/schema/narad/kind |




## LinkML Source

<details>
```yaml
name: kind
description: 'Generic kind/type label. Used for Beamline entries (e.g. BeamLine).
  For ControlProfileFamily device domain use device_domain: DeviceDomainEnum. For
  CapabilityProfile device type use device_type: ElementKindEnum.'
from_schema: https://w3id.org/narad_linkml/schema/narad/
aliases:
- type
- profile_type
rank: 1000
alias: kind
domain_of:
- BeamlineElement
- Beamline
range: string

```
</details>