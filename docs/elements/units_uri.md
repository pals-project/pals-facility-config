

# Slot: units_uri 


_Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere). The si-unit: prefix maps to http://qudt.org/vocab/unit/._





URI: [narad:units_uri](https://example.org/narad_linkml/schema/narad/units_uri)
Alias: units_uri

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ObservableSignal](ObservableSignal.md) | A NARAD signal that is read, monitored, observed, or exposed by a system |  no  |
| [Signal](Signal.md) | Domain term for a control-system signal |  no  |
| [ActuatableSignal](ActuatableSignal.md) | A NARAD signal that can be commanded, set, or acted upon |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:units_uri |
| native | narad:units_uri |




## LinkML Source

<details>
```yaml
name: units_uri
description: 'Machine-resolvable QUDT unit reference (e.g. si-unit:A for Ampere).
  The si-unit: prefix maps to http://qudt.org/vocab/unit/.'
in_subset:
- label
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: units_uri
domain_of:
- Signal
range: string

```
</details>