

# Slot: description 



URI: [https://w3id.org/narad_linkml/schema/narad/description](https://w3id.org/narad_linkml/schema/narad/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |
| [Capability](Capability.md) | A named, shared grouping of semantically related signals for a control aspect |  no  |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |  no  |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |
| [CapabilityMixin](CapabilityMixin.md) | Shared structure common to all capability types: a description and an ordered... |  no  |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/description |
| native | https://w3id.org/narad_linkml/schema/narad/description |




## LinkML Source

<details>
```yaml
name: description
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: description
domain_of:
- SignalBinding
- CapabilityMixin
- Signal
- CapabilityProfile
- ControlProfileFamily
range: string

```
</details>