# Enum: NodeTypeEnum 




_Node types in the NARAD graph projection; used as domain/range values for Relationship._



URI: [https://w3id.org/narad_linkml/schema/narad/NodeTypeEnum](https://w3id.org/narad_linkml/schema/narad/NodeTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Device | None | A physical beamline element (BeamlineElement) |
| CapabilityFamily | None | A control profile family (ControlProfileFamily) |
| Profile | None | A device-type capability profile (CapabilityProfile) |
| Capability | None | A shared capability grouping signals |
| TypeSpecificCapability | None | A profile-local type-specific capability |
| Signal | None | An individual semantic signal (EPICS PV or equivalent) |
| Facility | None | A physical accelerator facility |
| ControlSystem | None | The control system (e |
| SignalBinding | None | A concrete facility-specific PV binding for a semantic signal |




## Slots

| Name | Description |
| ---  | --- |
| [domain](domain.md) | The node type that can appear as the subject (source) of this relationship |
| [range](range.md) | The node type that can appear as the object (target) of this relationship |
| [range](range.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/






## LinkML Source

<details>
```yaml
name: NodeTypeEnum
description: Node types in the NARAD graph projection; used as domain/range values
  for Relationship.
from_schema: https://w3id.org/narad_linkml/schema/narad/
rank: 1000
permissible_values:
  Device:
    text: Device
    description: A physical beamline element (BeamlineElement).
  CapabilityFamily:
    text: CapabilityFamily
    description: A control profile family (ControlProfileFamily).
  Profile:
    text: Profile
    description: A device-type capability profile (CapabilityProfile).
  Capability:
    text: Capability
    description: A shared capability grouping signals.
  TypeSpecificCapability:
    text: TypeSpecificCapability
    description: A profile-local type-specific capability.
  Signal:
    text: Signal
    description: An individual semantic signal (EPICS PV or equivalent).
  Facility:
    text: Facility
    description: A physical accelerator facility.
  ControlSystem:
    text: ControlSystem
    description: The control system (e.g. EPICS) managing device PVs.
  SignalBinding:
    text: SignalBinding
    description: A concrete facility-specific PV binding for a semantic signal.

```
</details>