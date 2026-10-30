

# Class: LongitudinalPlacementParamGroup 


_Mixin for an element's extent and position along the longitudinal (beam-direction, "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`. One (or both) `length` or `s_position` must be present._





URI: [acc:class/LongitudinalPlacementParamGroup](https://example.org/accelerator-core/class/LongitudinalPlacementParamGroup)


```mermaid
erDiagram
LongitudinalPlacementParamGroup {
    float length  
    float s_position  
    string id  
}



```




## Inheritance
* [ParamGroup](../classes/ParamGroup.md)
    * **LongitudinalPlacementParamGroup**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [length](../slots/length.md) | 0..1 <br/> [Float](../types/Float.md) | Length of the element (arc length for bends). | direct |
| [s_position](../slots/s_position.md) | 0..1 <br/> [Float](../types/Float.md) | Longitudinal position of the element along the beamline. | direct |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [ParamGroup](../classes/ParamGroup.md) |





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
| [Drift](../classes/Drift.md) | [LongitudinalPlacementP](../slots/LongitudinalPlacementP.md) | range | [LongitudinalPlacementParamGroup](../classes/LongitudinalPlacementParamGroup.md) |




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
| self | acc:LongitudinalPlacementParamGroup |
| native | acc:LongitudinalPlacementParamGroup |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LongitudinalPlacementParamGroup
description: Mixin for an element's extent and position along the longitudinal (beam-direction,
  "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
  One (or both) `length` or `s_position` must be present.
from_schema: https://w3id.org/accelerator-core
is_a: ParamGroup
slots:
- length
attributes:
  s_position:
    name: s_position
    description: Longitudinal position of the element along the beamline.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:s_position
    rank: 1000
    domain_of:
    - LongitudinalPlacementParamGroup
    range: float
    unit:
      ucum_code: m
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
description: Mixin for an element's extent and position along the longitudinal (beam-direction,
  "s") axis.  Corresponds to PALS's ungrouped element parameters `length` and `s_position`.
  One (or both) `length` or `s_position` must be present.
from_schema: https://w3id.org/accelerator-core
is_a: ParamGroup
attributes:
  s_position:
    name: s_position
    description: Longitudinal position of the element along the beamline.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:s_position
    rank: 1000
    alias: s_position
    owner: LongitudinalPlacementParamGroup
    domain_of:
    - LongitudinalPlacementParamGroup
    range: float
    unit:
      ucum_code: m
  length:
    name: length
    description: Length of the element (arc length for bends).
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:length
    rank: 1000
    alias: length
    owner: LongitudinalPlacementParamGroup
    domain_of:
    - LongitudinalPlacementParamGroup
    - BeamLine
    range: float
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: LongitudinalPlacementParamGroup
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true
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