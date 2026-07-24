

# Slot: repeat 


_Repetition count. If not provided, the default assumption is that the beamline is not repeated and the value is 1._

_If value is greater than 1, the beamline is repeated that many times._





URI: [pals:repeat](https://pals-project.readthedocs.io/repeat)
Alias: repeat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamLine](BeamLine.md) | PALS element for an ordered sequence of beamline elements defining a beam pat... |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:repeat |
| native | pals:repeat |




## LinkML Source

<details>
```yaml
name: repeat
description: 'Repetition count. If not provided, the default assumption is that the
  beamline is not repeated and the value is 1.

  If value is greater than 1, the beamline is repeated that many times.'
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: pals:repeat
alias: repeat
owner: BeamLine
domain_of:
- BeamLine
range: integer

```
</details>