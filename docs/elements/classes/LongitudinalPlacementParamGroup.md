

# Class: LongitudinalPlacementParamGroup 


_Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis. _

_Corresponds to PALS's ungrouped element parameters `length` and `s_position`._

_One (or both) `length` or `s_position` must be present._





URI: [pals:class/LongitudinalPlacementParamGroup](https://pals-project.readthedocs.io/class/LongitudinalPlacementParamGroup)


```mermaid
erDiagram
LongitudinalPlacementParamGroup {
    float length  
    float s_position  
}



```



<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [length](../slots/length.md) | 0..1 <br/> [Float](../types/Float.md) | Length of the element (arc length for bends). | direct |
| [s_position](../slots/s_position.md) | 0..1 <br/> [Float](../types/Float.md) | Longitudinal position of the element along the beamline. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasLongitudinalPlacementP](../classes/HasLongitudinalPlacementP.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [PhysicalComponent](../classes/PhysicalComponent.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Magnet](../classes/Magnet.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Solenoid](../classes/Solenoid.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Multipole](../classes/Multipole.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Bend](../classes/Bend.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Quadrupole](../classes/Quadrupole.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Octupole](../classes/Octupole.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Sextupole](../classes/Sextupole.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Kicker](../classes/Kicker.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [ACKicker](../classes/ACKicker.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [DiagnosticDevice](../classes/DiagnosticDevice.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Aperture](../classes/Aperture.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [RadiationMonitor](../classes/RadiationMonitor.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [Cavity](../classes/Cavity.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [CrabCavity](../classes/CrabCavity.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [RFCavity](../classes/RFCavity.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |
| [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'id': {'value_presence': 'PRESENT'}}``` | | |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:LongitudinalPlacementParamGroup |
| native | pals:LongitudinalPlacementParamGroup |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LongitudinalPlacementParamGroup
description: "Mixin for an element's extent and position along the longitudinal (beam-direction,\
  \ \"s\") axis. \nCorresponds to PALS's ungrouped element parameters `length` and\
  \ `s_position`.\nOne (or both) `length` or `s_position` must be present."
from_schema: https://w3id.org/accelerator-core
slots:
- length
attributes:
  s_position:
    name: s_position
    description: Longitudinal position of the element along the beamline.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:s_position
    domain_of:
    - LongitudinalPlacementParamGroup
    range: float
rules:
- preconditions:
    slot_conditions:
      id:
        name: id
        value_presence: PRESENT
  postconditions:
    any_of:
    - slot_conditions:
        length:
          name: length
          value_presence: PRESENT
    - slot_conditions:
        s_position:
          name: s_position
          value_presence: PRESENT
  description: An element must have a length and/or a position along the beamline.

```
</details>

### Induced

<details>
```yaml
name: LongitudinalPlacementParamGroup
description: "Mixin for an element's extent and position along the longitudinal (beam-direction,\
  \ \"s\") axis. \nCorresponds to PALS's ungrouped element parameters `length` and\
  \ `s_position`.\nOne (or both) `length` or `s_position` must be present."
from_schema: https://w3id.org/accelerator-core
attributes:
  s_position:
    name: s_position
    description: Longitudinal position of the element along the beamline.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:s_position
    alias: s_position
    owner: LongitudinalPlacementParamGroup
    domain_of:
    - LongitudinalPlacementParamGroup
    range: float
  length:
    name: length
    description: Length of the element (arc length for bends).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:length
    alias: length
    owner: LongitudinalPlacementParamGroup
    domain_of:
    - LongitudinalPlacementParamGroup
    - BeamLine
    range: float
rules:
- preconditions:
    slot_conditions:
      id:
        name: id
        value_presence: PRESENT
  postconditions:
    any_of:
    - slot_conditions:
        length:
          name: length
          value_presence: PRESENT
    - slot_conditions:
        s_position:
          name: s_position
          value_presence: PRESENT
  description: An element must have a length and/or a position along the beamline.

```
</details>