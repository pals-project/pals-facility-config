

# Slot: pv_name 


_Fully-resolved facility-specific process variable name, e.g. MQWK202:STAT or MQWK202:BDL._

__





URI: [narad:pv_name](https://w3id.org/narad_linkml/schema/narad/pv_name)
Alias: pv_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InstanceSignalBinding](InstanceSignalBinding.md) | A facility-specific binding between a NARAD Signal and an implementation inte... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:pv_name |
| native | narad:pv_name |




## LinkML Source

<details>
```yaml
name: pv_name
description: 'Fully-resolved facility-specific process variable name, e.g. MQWK202:STAT
  or MQWK202:BDL.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: pv_name
domain_of:
- InstanceSignalBinding
range: string

```
</details>