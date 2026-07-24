

# Slot: signal_bindings 


_A list of signal bindings in the accelerator system (Component <-> Signal relationships)._





URI: [pals:signal_bindings](https://pals-project.readthedocs.io/signal_bindings)
Alias: signal_bindings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](Facility.md) | A facility that houses one or more accelerators |  no  |






## Properties

* Range: [SignalBinding](SignalBinding.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:signal_bindings |
| native | pals:signal_bindings |




## LinkML Source

<details>
```yaml
name: signal_bindings
description: A list of signal bindings in the accelerator system (Component <-> Signal
  relationships).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: signal_bindings
owner: Facility
domain_of:
- Facility
range: SignalBinding
multivalued: true
inlined: true
inlined_as_list: true

```
</details>