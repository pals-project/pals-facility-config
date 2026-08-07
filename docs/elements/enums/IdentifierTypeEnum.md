# Enum: IdentifierTypeEnum 




_Controlled values for identifier types._



URI: [pals:enum/IdentifierTypeEnum](https://pals-project.readthedocs.io/enum/IdentifierTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| DOI | http://purl.org/spar/datacite/doi | Digital Object Identifier. |
| PURL | http://purl.org/spar/datacite/purl | Persistent Uniform Resource Locator. |
| ROR | http://purl.org/spar/datacite/ror | Research Organization Registry identifier. |
| LOCAL | http://purl.org/spar/datacite/local-resource-identifier-scheme | Local identifier, specific to the facility or source system. |
| URL | http://purl.org/spar/datacite/url | Uniform Resource Locator. |
| ARK | http://purl.org/spar/datacite/ark | Archival Resource Key. |




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
    meaning: http://purl.org/spar/datacite/doi
  PURL:
    text: PURL
    description: Persistent Uniform Resource Locator.
    meaning: http://purl.org/spar/datacite/purl
  ROR:
    text: ROR
    description: Research Organization Registry identifier.
    meaning: http://purl.org/spar/datacite/ror
  LOCAL:
    text: LOCAL
    description: Local identifier, specific to the facility or source system.
    meaning: http://purl.org/spar/datacite/local-resource-identifier-scheme
  URL:
    text: URL
    description: Uniform Resource Locator.
    meaning: http://purl.org/spar/datacite/url
  ARK:
    text: ARK
    description: Archival Resource Key.
    meaning: http://purl.org/spar/datacite/ark

```
</details>