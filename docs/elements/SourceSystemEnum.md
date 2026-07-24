# Enum: SourceSystemEnum 




_Controlled values for facility-local source systems._



URI: [pals:SourceSystemEnum](https://pals-project.readthedocs.io/SourceSystemEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EPICS | None | EPICS control system |
| EPICS_ChannelAccess | None | EPICS Channel Access source |
| PALS_Ext | None | PALS-Ext or middle-layer channel/export system |
| MYA | None | MYA archive or historical channel service |
| ElementDatabase | None | Facility element database |
| ChannelDatabase | None | Facility channel database |
| Simulation | None | Simulation or model-derived signal source |
| Other | None | Other source system |




## Slots

| Name | Description |
| ---  | --- |
| [source_system](source_system.md) | The source system from which the signal originates, such as EPICS, PALS-Ext, ... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: SourceSystemEnum
description: Controlled values for facility-local source systems.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  EPICS:
    text: EPICS
    description: EPICS control system.
  EPICS_ChannelAccess:
    text: EPICS_ChannelAccess
    description: EPICS Channel Access source.
  PALS_Ext:
    text: PALS_Ext
    description: PALS-Ext or middle-layer channel/export system.
  MYA:
    text: MYA
    description: MYA archive or historical channel service.
  ElementDatabase:
    text: ElementDatabase
    description: Facility element database.
  ChannelDatabase:
    text: ChannelDatabase
    description: Facility channel database.
  Simulation:
    text: Simulation
    description: Simulation or model-derived signal source.
  Other:
    text: Other
    description: Other source system.

```
</details>