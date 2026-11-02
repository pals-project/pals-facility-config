# Enum: ZeroPhaseEnum 




_The zero phase reference for the cavity, which determines the phase of the RF field at the entrance of the cavity._



URI: [acc:enum/ZeroPhaseEnum](https://example.org/accelerator-core/enum/ZeroPhaseEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ACCELERATING | None | Default. The zero phase is the maximum accelerating phase, where the beam gains energy. |
| BELOW_TRANSITION | None | Zero phase is at the stable zero crossing for particles below transition. |
| ABOVE_TRANSITION | None | Zero phase is at the stable zero crossing for particles above transition.. |




## Slots

| Name | Description |
| ---  | --- |
| [zero_phase](../slots/zero_phase.md) | Sets what phase = 0 means. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: ZeroPhaseEnum
description: The zero phase reference for the cavity, which determines the phase of
  the RF field at the entrance of the cavity.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  ACCELERATING:
    text: ACCELERATING
    description: Default. The zero phase is the maximum accelerating phase, where
      the beam gains energy.
  BELOW_TRANSITION:
    text: BELOW_TRANSITION
    description: Zero phase is at the stable zero crossing for particles below transition.
  ABOVE_TRANSITION:
    text: ABOVE_TRANSITION
    description: Zero phase is at the stable zero crossing for particles above transition..

```
</details>