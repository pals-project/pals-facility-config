

# Slot: param_set 


_Named physics-parameter blocks for this element (e.g. RFP, BendP, MagneticMultipoleP)._





URI: [narad:param_set](https://w3id.org/narad_linkml/schema/narad/param_set)
Alias: param_set

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with its kind and optional NARAD capability an... |  no  |






## Properties

* Range: [ElementParamSet](ElementParamSet.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:param_set |
| native | narad:param_set |




## LinkML Source

<details>
```yaml
name: param_set
description: Named physics-parameter blocks for this element (e.g. RFP, BendP, MagneticMultipoleP).
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
alias: param_set
domain_of:
- BeamlineElement
range: ElementParamSet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>