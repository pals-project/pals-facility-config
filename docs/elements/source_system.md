

# Slot: source_system 


_The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service._





URI: [pals:source_system](https://pals-project.readthedocs.io/source_system)
Alias: source_system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](Signal.md) | Semantic meaning of a control-system signal associated with a component |  no  |






## Properties

* Range: [SourceSystemEnum](SourceSystemEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:source_system |
| native | pals:source_system |




## LinkML Source

<details>
```yaml
name: source_system
description: The source system from which the signal originates, such as EPICS, PALS-Ext,
  MYA, an element database, a channel database, or a simulation service.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: source_system
owner: Signal
domain_of:
- Signal
range: SourceSystemEnum
required: true

```
</details>