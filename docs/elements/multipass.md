

# Slot: multipass 


_Indicates whether the BeamLine is a multipass BeamLine, where the beam passes through the same physical elements multiple times. If not provided, the default assumption is that the BeamLine is single-pass._





URI: [pals:multipass](https://pals-project.readthedocs.io/multipass)
Alias: multipass

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
| self | pals:multipass |
| native | pals:multipass |




## LinkML Source

<details>
```yaml
name: multipass
description: Indicates whether the BeamLine is a multipass BeamLine, where the beam
  passes through the same physical elements multiple times. If not provided, the default
  assumption is that the BeamLine is single-pass.
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:multipass
alias: multipass
owner: BeamLine
domain_of:
- BeamLine
range: boolean

```
</details>