

# Class: FloorParamGroup 


_Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:FloorParamGroup](https://pals-project.readthedocs.io/FloorParamGroup)





```mermaid
 classDiagram
    class FloorParamGroup
    click FloorParamGroup href "../FloorParamGroup/"
      FloorParamGroup : phi
        
      FloorParamGroup : psi
        
      FloorParamGroup : theta
        
      FloorParamGroup : x
        
      FloorParamGroup : y
        
      FloorParamGroup : z
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [x](x.md) | 0..1 <br/> [Float](Float.md) | Global X coordinate in the facility floor plan | direct |
| [y](y.md) | 0..1 <br/> [Float](Float.md) | Global Y coordinate in the facility floor plan | direct |
| [z](z.md) | 0..1 <br/> [Float](Float.md) | Global Z coordinate in the facility floor plan | direct |
| [theta](theta.md) | 0..1 <br/> [Float](Float.md) | Orientation angle around the Y-axis in the facility floor plan | direct |
| [phi](phi.md) | 0..1 <br/> [Float](Float.md) | Rotation around the X-axis in the facility floor plan | direct |
| [psi](psi.md) | 0..1 <br/> [Float](Float.md) | Rotation around the Z-axis in the facility floor plan | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasFloorP](HasFloorP.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [PhysicalComponent](PhysicalComponent.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [VirtualComponent](VirtualComponent.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [BeamLine](BeamLine.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Magnet](Magnet.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Solenoid](Solenoid.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Multipole](Multipole.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Bend](Bend.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Quadrupole](Quadrupole.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Octupole](Octupole.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Sextupole](Sextupole.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Kicker](Kicker.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [ACKicker](ACKicker.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [DiagnosticDevice](DiagnosticDevice.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [BeamProfileMonitor](BeamProfileMonitor.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [BeamPositionMonitor](BeamPositionMonitor.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Aperture](Aperture.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [RadiationMonitor](RadiationMonitor.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Cavity](Cavity.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [CrabCavity](CrabCavity.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [RFCavity](RFCavity.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [SupportingFacilityComponent](SupportingFacilityComponent.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [BookkeepingComponent](BookkeepingComponent.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [Marker](Marker.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |
| [BeamLineSection](BeamLineSection.md) | [FloorP](FloorP.md) | range | [FloorParamGroup](FloorParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:FloorParamGroup |
| native | pals:FloorParamGroup |
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
attributes:
  x:
    name: x
    description: Global X coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - x_coordinate
    - ModelX
    - x coordinate
    rank: 1000
    slot_uri: pals:x
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
    rank: 1000
    slot_uri: pals:y
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
    rank: 1000
    slot_uri: pals:z
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
    rank: 1000
    slot_uri: pals:theta
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
    rank: 1000
    slot_uri: pals:phi
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
    rank: 1000
    slot_uri: pals:psi
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
attributes:
  x:
    name: x
    description: Global X coordinate in the facility floor plan.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - x_coordinate
    - ModelX
    - x coordinate
    rank: 1000
    slot_uri: pals:x
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
    rank: 1000
    slot_uri: pals:y
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
    rank: 1000
    slot_uri: pals:z
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
    rank: 1000
    slot_uri: pals:theta
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
    rank: 1000
    slot_uri: pals:phi
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
    rank: 1000
    slot_uri: pals:psi
    alias: psi
    owner: FloorParamGroup
    domain_of:
    - FloorParamGroup
    range: float

```
</details>