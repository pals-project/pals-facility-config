

# Class: FloorParamGroup 


_Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [acc:class/FloorParamGroup](https://example.org/accelerator-core/class/FloorParamGroup)


```mermaid
erDiagram
FloorParamGroup {
    float phi  
    float psi  
    float theta  
    float x  
    float y  
    float z  
    string id  
}



```




## Inheritance
* [ParamGroup](../classes/ParamGroup.md)
    * **FloorParamGroup**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [x](../slots/x.md) | 0..1 <br/> [Float](../types/Float.md) | Global X coordinate in the facility floor plan. | direct |
| [y](../slots/y.md) | 0..1 <br/> [Float](../types/Float.md) | Global Y coordinate in the facility floor plan. | direct |
| [z](../slots/z.md) | 0..1 <br/> [Float](../types/Float.md) | Global Z coordinate in the facility floor plan. | direct |
| [theta](../slots/theta.md) | 0..1 <br/> [Float](../types/Float.md) | Orientation angle around the Y-axis in the facility floor plan. | direct |
| [phi](../slots/phi.md) | 0..1 <br/> [Float](../types/Float.md) | Rotation around the X-axis in the facility floor plan. | direct |
| [psi](../slots/psi.md) | 0..1 <br/> [Float](../types/Float.md) | Rotation around the Z-axis in the facility floor plan. | direct |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [ParamGroup](../classes/ParamGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasFloorP](../classes/HasFloorP.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [PhysicalComponent](../classes/PhysicalComponent.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [VirtualComponent](../classes/VirtualComponent.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [BeamLine](../classes/BeamLine.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Magnet](../classes/Magnet.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Solenoid](../classes/Solenoid.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Multipole](../classes/Multipole.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Bend](../classes/Bend.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Quadrupole](../classes/Quadrupole.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Octupole](../classes/Octupole.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Sextupole](../classes/Sextupole.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Kicker](../classes/Kicker.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [ACKicker](../classes/ACKicker.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [DiagnosticDevice](../classes/DiagnosticDevice.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Aperture](../classes/Aperture.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [RadiationMonitor](../classes/RadiationMonitor.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Cavity](../classes/Cavity.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [CrabCavity](../classes/CrabCavity.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [RFCavity](../classes/RFCavity.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [SupportingFacilityComponent](../classes/SupportingFacilityComponent.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [BookkeepingComponent](../classes/BookkeepingComponent.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Marker](../classes/Marker.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [BeginningEle](../classes/BeginningEle.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [Drift](../classes/Drift.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |
| [BeamLineSection](../classes/BeamLineSection.md) | [FloorP](../slots/FloorP.md) | range | [FloorParamGroup](../classes/FloorParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:FloorParamGroup |
| native | acc:FloorParamGroup |
| broad | pals:FloorP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FloorParamGroup
description: Mixin class for floor plan parameters that are aligned with PALS FloorP
  (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:FloorP
is_a: ParamGroup
attributes:
  x:
    name: x
    description: Global X coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - x_coordinate
    - ModelX
    - x coordinate
    close_mappings:
    - pals:x
    rank: 1000
    domain_of:
    - FloorParamGroup
    range: float
  y:
    name: y
    description: Global Y coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - y_coordinate
    - ModelY
    - y coordinate
    close_mappings:
    - pals:y
    rank: 1000
    domain_of:
    - FloorParamGroup
    range: float
  z:
    name: z
    description: Global Z coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - z_coordinate
    - ModelZ
    - z coordinate
    close_mappings:
    - pals:z
    rank: 1000
    domain_of:
    - FloorParamGroup
    range: float
  theta:
    name: theta
    description: Orientation angle around the Y-axis in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - theta_angle
    - ModelYaw
    - Model_Yaw
    close_mappings:
    - pals:theta
    rank: 1000
    domain_of:
    - FloorParamGroup
    range: float
  phi:
    name: phi
    description: Rotation around the X-axis in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - phi_angle
    - ModelPitch
    - Model_Pitch
    close_mappings:
    - pals:phi
    rank: 1000
    domain_of:
    - FloorParamGroup
    range: float
  psi:
    name: psi
    description: Rotation around the Z-axis in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - psi_angle
    - Model_Roll
    - Rotation
    close_mappings:
    - pals:psi
    rank: 1000
    domain_of:
    - FloorParamGroup
    range: float

```
</details>

### Induced

<details>
```yaml
name: FloorParamGroup
description: Mixin class for floor plan parameters that are aligned with PALS FloorP
  (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:FloorP
is_a: ParamGroup
attributes:
  x:
    name: x
    description: Global X coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - x_coordinate
    - ModelX
    - x coordinate
    close_mappings:
    - pals:x
    rank: 1000
    alias: x
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
    range: float
  y:
    name: y
    description: Global Y coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - y_coordinate
    - ModelY
    - y coordinate
    close_mappings:
    - pals:y
    rank: 1000
    alias: y
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
    range: float
  z:
    name: z
    description: Global Z coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - z_coordinate
    - ModelZ
    - z coordinate
    close_mappings:
    - pals:z
    rank: 1000
    alias: z
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
    range: float
  theta:
    name: theta
    description: Orientation angle around the Y-axis in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - theta_angle
    - ModelYaw
    - Model_Yaw
    close_mappings:
    - pals:theta
    rank: 1000
    alias: theta
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
    range: float
  phi:
    name: phi
    description: Rotation around the X-axis in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - phi_angle
    - ModelPitch
    - Model_Pitch
    close_mappings:
    - pals:phi
    rank: 1000
    alias: phi
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
    range: float
  psi:
    name: psi
    description: Rotation around the Z-axis in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - psi_angle
    - Model_Roll
    - Rotation
    close_mappings:
    - pals:psi
    rank: 1000
    alias: psi
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
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
    owner: FloorParamGroup
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true

```
</details>