# Enum: IdentifierTypeEnum 




_Controlled values for identifier types._



URI: [acc:enum/IdentifierTypeEnum](https://example.org/accelerator-core/enum/IdentifierTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| DOI | None | Digital Object Identifier. |
| PURL | None | Persistent Uniform Resource Locator. |
| ROR | None | Research Organization Registry identifier. |
| LOCAL | None | Local identifier, specific to the facility or source system. |
| URL | None | Uniform Resource Locator. |
| ARK | None | Archival Resource Key. |




## Slots

| Name | Description |
| ---  | --- |
| [identifier_type](../slots/identifier_type.md) | The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: IdentifierTypeEnum
description: Controlled values for identifier types.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  DOI:
    text: DOI
    description: Digital Object Identifier.
    exact_mappings:
    - http://purl.org/spar/datacite/doi
  PURL:
    text: PURL
    description: Persistent Uniform Resource Locator.
    exact_mappings:
    - http://purl.org/spar/datacite/purl
  ROR:
    text: ROR
    description: Research Organization Registry identifier.
    exact_mappings:
    - http://purl.org/spar/datacite/ror
  LOCAL:
    text: LOCAL
    description: Local identifier, specific to the facility or source system.
    exact_mappings:
    - http://purl.org/spar/datacite/local-resource-identifier-scheme
  URL:
    text: URL
    description: Uniform Resource Locator.
    exact_mappings:
    - http://purl.org/spar/datacite/url
  ARK:
    text: ARK
    description: Archival Resource Key.
    exact_mappings:
    - http://purl.org/spar/datacite/ark

```
</details>