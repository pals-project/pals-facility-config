

# Slot: periodic 


_Indicates whether orbit and Twiss parameters periodic. If not provided, the default assumption is that the BeamLine is not periodic._





URI: [pals:periodic](https://pals-project.readthedocs.io/periodic)
Alias: periodic

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:periodic |
| native | pals:periodic |




## LinkML Source

<details>
```yaml
name: periodic
description: Indicates whether orbit and Twiss parameters periodic. If not provided,
  the default assumption is that the BeamLine is not periodic.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:periodic
alias: periodic
owner: BeamLine
domain_of:
- BeamLine
range: boolean

```
</details>