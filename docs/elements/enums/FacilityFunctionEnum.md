# Enum: FacilityFunctionEnum 




_Broad structural or support functions._



URI: [pals_config:enum/FacilityFunctionEnum](https://w3id.org/pals-config/enum/FacilityFunctionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Support | None | Provides mechanical support for accelerator operations. |
| Alignment | None | Supports alignment of accelerator components. |
| PowerSupply | None | Provides electrical power to accelerator components. |
| ControlRack | None | Houses control electronics for accelerator components. |
| Cooling | None | Provides cooling for accelerator components. |
| Diagnostics | None | Provides diagnostic capabilities for accelerator components, such as monitoring or measurement. |
| Detection | None | Provides detection capabilities for accelerator components, such as radiation or particle detection. |




## Slots

| Name | Description |
| ---  | --- |
| [facility_functions](../slots/facility_functions.md) | The function of the supporting facility component,  which can be used to identify the component across different source systems. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config






## LinkML Source

<details>
```yaml
name: FacilityFunctionEnum
description: Broad structural or support functions.
from_schema: https://w3id.org/pals-config
rank: 1000
permissible_values:
  Support:
    text: Support
    description: Provides mechanical support for accelerator operations.
  Alignment:
    text: Alignment
    description: Supports alignment of accelerator components.
  PowerSupply:
    text: PowerSupply
    description: Provides electrical power to accelerator components.
  ControlRack:
    text: ControlRack
    description: Houses control electronics for accelerator components.
  Cooling:
    text: Cooling
    description: Provides cooling for accelerator components.
  Diagnostics:
    text: Diagnostics
    description: Provides diagnostic capabilities for accelerator components, such
      as monitoring or measurement.
  Detection:
    text: Detection
    description: Provides detection capabilities for accelerator components, such
      as radiation or particle detection.

```
</details>