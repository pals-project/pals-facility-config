

# Slot: z_rot 


_Rotation around the Z-axis in the facility floor plan._





URI: [pals:z_rot](https://pals-project.readthedocs.io/z_rot)
Alias: z_rot

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BodyShiftParamGroup](BodyShiftParamGroup.md) | Mixin class for floor plan shift parameters that are aligned with PALS BodySh... |  no  |






## Properties

* Range: [Float](Float.md)



## Aliases


* delta_psi
* psi_shift
* GlobalOffsetPsi


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:z_rot |
| native | pals:z_rot |




## LinkML Source

<details>
```yaml
name: z_rot
description: Rotation around the Z-axis in the facility floor plan.
from_schema: https://w3id.org/accelerator-core
aliases:
- delta_psi
- psi_shift
- GlobalOffsetPsi
rank: 1000
slot_uri: pals:z_rot
alias: z_rot
owner: BodyShiftParamGroup
domain_of:
- BodyShiftParamGroup
range: float

```
</details>