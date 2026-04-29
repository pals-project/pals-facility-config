# Enum: IdentifierTypeEnum 




_Allowed identifier types for facilities and other entities._



URI: [https://w3id.org/narad_linkml/schema/narad/IdentifierTypeEnum](https://w3id.org/narad_linkml/schema/narad/IdentifierTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| doi | None | Digital Object Identifier (DOI) |
| ark | None | Archival Resource Key (ARK) |
| handle | None | Handle System identifier |
| url | None | Uniform Resource Locator (URL) |
| local | None | Local identifier unique within a specific context or namespace |
| other | None | Any other type of identifier not covered by the above categories |




## Slots

| Name | Description |
| ---  | --- |
| [identifier_type](identifier_type.md) | The type of identifier used in the identifier slot (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/






## LinkML Source

<details>
```yaml
name: IdentifierTypeEnum
description: Allowed identifier types for facilities and other entities.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
permissible_values:
  doi:
    text: doi
    description: Digital Object Identifier (DOI).
  ark:
    text: ark
    description: Archival Resource Key (ARK).
  handle:
    text: handle
    description: Handle System identifier.
  url:
    text: url
    description: Uniform Resource Locator (URL).
  local:
    text: local
    description: Local identifier unique within a specific context or namespace.
  other:
    text: other
    description: Any other type of identifier not covered by the above categories.

```
</details>