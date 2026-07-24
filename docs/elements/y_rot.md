

# Slot: y_rot 


_Rotation around the Y-axis in the facility floor plan._





URI: [pals:y_rot](https://pals-project.readthedocs.io/y_rot)
Alias: y_rot

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BodyShiftParamGroup](BodyShiftParamGroup.md) | Mixin class for floor plan shift parameters that are aligned with PALS BodySh... |  no  |






## Properties

* Range: [Float](Float.md)



## Aliases


* delta_theta
* theta_shift
* GlobalOffsetTheta


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:y_rot |
| native | pals:y_rot |




## LinkML Source

<details>
```yaml
name: y_rot
description: Rotation around the Y-axis in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- delta_theta
- theta_shift
- GlobalOffsetTheta
rank: 1000
slot_uri: pals:y_rot
alias: y_rot
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>