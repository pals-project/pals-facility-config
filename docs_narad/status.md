

# Slot: status 



URI: [narad:status](https://w3id.org/narad_linkml/schema/narad/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BPMSignalSet](BPMSignalSet.md) | BPM-specific signal bindings |  no  |
| [RFCavitySignalSet](RFCavitySignalSet.md) | RF cavity-specific signal bindings |  no  |
| [MagnetSignalSet](MagnetSignalSet.md) | Shared magnet signal bindings |  no  |






## Properties

* Range: [SignalBinding](SignalBinding.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:status |
| native | narad:status |




## LinkML Source

<details>
```yaml
name: status
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: status
domain_of:
- MagnetSignalSet
- BPMSignalSet
- RFCavitySignalSet
range: SignalBinding
inlined: true

```
</details>