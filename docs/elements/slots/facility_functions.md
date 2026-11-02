

# Slot: facility_functions 


_The function of the supporting facility component,  which can be used to identify the component across different source systems._





URI: [acc:slot/facility_functions](https://example.org/accelerator-core/slot/facility_functions)
Alias: facility_functions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) | A physical component that supports accelerator operation  without a specific beam-pipe placement,  such as a power supply, control rack, or radiation detector. These can include Girders, Racks, Power Supplies,  and other physical infrastructure components that are important for understanding  the structure and function of the accelerator system but are not inline with the beamline. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FacilityFunctionEnum](../enums/FacilityFunctionEnum.md) |
| Domain Of | [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:facility_functions |
| native | acc:facility_functions |
| close | pals:supporting_facility_function |




## LinkML Source

<details>
```yaml
name: facility_functions
description: The function of the supporting facility component,  which can be used
  to identify the component across different source systems.
from_schema: https://w3id.org/accelerator-core
close_mappings:
- pals:supporting_facility_function
rank: 1000
alias: facility_functions
owner: SupportingFacilityComponent
domain_of:
- SupportingFacilityComponent
range: FacilityFunctionEnum
required: true
multivalued: true

```
</details>