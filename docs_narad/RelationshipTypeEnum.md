# Enum: RelationshipTypeEnum 




_Allowed relationship types in the NARAD graph projection; each corresponds to an RO (Relation Ontology)-inspired directed edge._



URI: [https://w3id.org/narad_linkml/schema/narad/RelationshipTypeEnum](https://w3id.org/narad_linkml/schema/narad/RelationshipTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| has_shared_capability | None | A profile family has a shared capability available to all its member profiles |
| has_type_profile | None | A profile family has a device-type profile (e |
| inherits_capability | None | A type-specific profile inherits a named shared capability from its family |
| has_type_specific_capability | None | A type profile has a locally-declared type-specific capability |
| has_signal | None | A capability has a semantic signal (EPICS PV or equivalent) |
| implemented_by | None | A semantic signal or capability is implemented by a concrete facility binding |
| binds_to | None | A PV signal binding is bound to a physical beamline element |
| located_in | None | A element is contained in an element |
| controlled_by | None | An entity is controlled by a control system element |
| before | None | A beamline element is upstream of another in the beam path |
| after | None | A beamline element is downstream of another in the beam path |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/






## LinkML Source

<details>
```yaml
name: RelationshipTypeEnum
description: Allowed relationship types in the NARAD graph projection; each corresponds
  to an RO (Relation Ontology)-inspired directed edge.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
permissible_values:
  has_shared_capability:
    text: has_shared_capability
    description: A profile family has a shared capability available to all its member
      profiles. Analogous to ro:has_part for capability composition.
    broad_mappings:
    - ro:0001019
  has_type_profile:
    text: has_type_profile
    description: A profile family has a device-type profile (e.g. Quadrupole, BPM).
  inherits_capability:
    text: inherits_capability
    description: A type-specific profile inherits a named shared capability from its
      family. Sub-relation of has_shared_capability.
  has_type_specific_capability:
    text: has_type_specific_capability
    description: A type profile has a locally-declared type-specific capability.
  has_signal:
    text: has_signal
    description: A capability has a semantic signal (EPICS PV or equivalent). Broad
      mapping to sosa:hasResult.
    broad_mappings:
    - ro:0002234
  implemented_by:
    text: implemented_by
    description: A semantic signal or capability is implemented by a concrete facility
      binding.
    broad_mappings:
    - swo:0000085
  binds_to:
    text: binds_to
    description: A PV signal binding is bound to a physical beamline element.
  located_in:
    text: located_in
    description: A element is contained in an element.
    broad_mappings:
    - ro:0001025
  controlled_by:
    text: controlled_by
    description: An entity is controlled by a control system element.
    broad_mappings:
    - ro:0002334
  before:
    text: before
    description: A beamline element is upstream of another in the beam path.
    broad_mappings:
    - ro:0002411
  after:
    text: after
    description: A beamline element is downstream of another in the beam path.
    broad_mappings:
    - ro:0002412

```
</details>