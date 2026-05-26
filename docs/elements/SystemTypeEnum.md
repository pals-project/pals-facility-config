# Enum: SystemTypeEnum 




_High-level system type for classification and querying. This is a broad categorization that can be used for filtering or grouping systems without needing to traverse the has_sub_system and has_system_capability edges._



URI: [narad:SystemTypeEnum](https://example.org/narad_linkml/schema/narad/SystemTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Facility | None | A physical facility or installation (e |
| ControlSystem | None | A control system (e |
| Magnet | None | A powered magnet device/system (generic supertype for all magnet kinds) |




## Slots

| Name | Description |
| ---  | --- |
| [system_type](system_type.md) | High-level system type for classification and querying |
| [system_type](system_type.md) | High-level system type for classification and querying - set to Facility for ... |
| [system_type](system_type.md) | High-level system type for classification and querying - set to ControlSystem... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system






## LinkML Source

<details>
```yaml
name: SystemTypeEnum
description: High-level system type for classification and querying. This is a broad
  categorization that can be used for filtering or grouping systems without needing
  to traverse the has_sub_system and has_system_capability edges.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
permissible_values:
  Facility:
    text: Facility
    description: A physical facility or installation (e.g. BTA, CEBAF, or UITF).
  ControlSystem:
    text: ControlSystem
    description: A control system (e.g. epics) that manages device process variables.
  Magnet:
    text: Magnet
    description: A powered magnet device/system (generic supertype for all magnet
      kinds).
inherits:
- ElementKindEnum

```
</details>