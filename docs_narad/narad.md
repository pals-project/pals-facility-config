

# Slot: narad 



URI: [https://w3id.org/narad_linkml/schema/narad/narad](https://w3id.org/narad_linkml/schema/narad/narad)
Alias: narad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |  yes  |






## Properties

* Range: [NaradConfig](NaradConfig.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/narad |
| native | https://w3id.org/narad_linkml/schema/narad/narad |




## LinkML Source

<details>
```yaml
name: narad
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
alias: narad
domain_of:
- NaradModel
- BeamlineElement
range: NaradConfig
inlined: true

```
</details>