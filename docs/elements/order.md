

# Slot: order 


_Multipole order N (0 = dipole, 1 = quadrupole, etc.)_





URI: [pals:order](https://pals-project.readthedocs.io/order)
Alias: order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultipoleParameterGroup](MultipoleParameterGroup.md) | A single order's electric (or magnetic) multipole component |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:order |
| native | pals:order |




## LinkML Source

<details>
```yaml
name: order
description: Multipole order N (0 = dipole, 1 = quadrupole, etc.)
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: order
owner: MultipoleParameterGroup
domain_of:
- MultipoleParameterGroup
range: integer
required: true

```
</details>