

# Class: TwissParamGroup 


_Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element._





URI: [pals:class/TwissParamGroup](https://pals-project.readthedocs.io/class/TwissParamGroup)


```mermaid
erDiagram
TwissParamGroup {
    float alpha_a  
    float alpha_b  
    float beta_a  
    float beta_b  
    float eta_x  
    float eta_y  
    float etap_x  
    float etap_y  
    float phi_a  
    float phi_b  
}



```



<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alpha_a](../slots/alpha_a.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss alpha parameter in the horizontal plane. | direct |
| [alpha_b](../slots/alpha_b.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss alpha parameter in the vertical plane. | direct |
| [beta_a](../slots/beta_a.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss beta parameter in the horizontal plane. | direct |
| [beta_b](../slots/beta_b.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss beta parameter in the vertical plane. | direct |
| [eta_x](../slots/eta_x.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss dispersion parameter in the horizontal plane. | direct |
| [eta_y](../slots/eta_y.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss dispersion parameter in the vertical plane. | direct |
| [etap_x](../slots/etap_x.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss dispersion slope parameter in the horizontal plane. | direct |
| [etap_y](../slots/etap_y.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss dispersion slope parameter in the vertical plane. | direct |
| [phi_a](../slots/phi_a.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss phase advance parameter in the horizontal plane. | direct |
| [phi_b](../slots/phi_b.md) | 0..1 <br/> [Float](../types/Float.md) | Twiss phase advance parameter in the vertical plane. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasTwissP](../classes/HasTwissP.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Magnet](../classes/Magnet.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Solenoid](../classes/Solenoid.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Multipole](../classes/Multipole.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Bend](../classes/Bend.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Quadrupole](../classes/Quadrupole.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Octupole](../classes/Octupole.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Sextupole](../classes/Sextupole.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Kicker](../classes/Kicker.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [ACKicker](../classes/ACKicker.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Aperture](../classes/Aperture.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Cavity](../classes/Cavity.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [CrabCavity](../classes/CrabCavity.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [RFCavity](../classes/RFCavity.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |
| [Marker](../classes/Marker.md) | [TwissP](../slots/TwissP.md) | range | [TwissParamGroup](../classes/TwissParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:TwissParamGroup |
| native | pals:TwissParamGroup |
| broad | pals:TwissP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TwissParamGroup
description: Mixin for Twiss parameters, which can be used to describe the beam optics
  of an accelerator element.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:TwissP
attributes:
  alpha_a:
    name: alpha_a
    description: Twiss alpha parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - alpha_x
    - alphax
    rank: 1000
    slot_uri: pals:alpha_a
    domain_of:
    - TwissParamGroup
    range: float
  alpha_b:
    name: alpha_b
    description: Twiss alpha parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - alpha_y
    - alphay
    rank: 1000
    slot_uri: pals:alpha_b
    domain_of:
    - TwissParamGroup
    range: float
  beta_a:
    name: beta_a
    description: Twiss beta parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - beta_x
    - betax
    rank: 1000
    slot_uri: pals:beta_a
    domain_of:
    - TwissParamGroup
    range: float
  beta_b:
    name: beta_b
    description: Twiss beta parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - beta_y
    - betay
    rank: 1000
    slot_uri: pals:beta_b
    domain_of:
    - TwissParamGroup
    range: float
  eta_x:
    name: eta_x
    description: Twiss dispersion parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etax
    rank: 1000
    slot_uri: pals:eta_x
    domain_of:
    - TwissParamGroup
    range: float
  eta_y:
    name: eta_y
    description: Twiss dispersion parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etay
    rank: 1000
    slot_uri: pals:eta_y
    domain_of:
    - TwissParamGroup
    range: float
  etap_x:
    name: etap_x
    description: Twiss dispersion slope parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etapx
    rank: 1000
    slot_uri: pals:etap_x
    domain_of:
    - TwissParamGroup
    range: float
  etap_y:
    name: etap_y
    description: Twiss dispersion slope parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etapy
    rank: 1000
    slot_uri: pals:etap_y
    domain_of:
    - TwissParamGroup
    range: float
  phi_a:
    name: phi_a
    description: Twiss phase advance parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - phi_x
    - phix
    - psi_x
    - psix
    rank: 1000
    slot_uri: pals:phi_a
    domain_of:
    - TwissParamGroup
    range: float
  phi_b:
    name: phi_b
    description: Twiss phase advance parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - phi_y
    - phiy
    - psi_y
    - psiy
    rank: 1000
    slot_uri: pals:phi_b
    domain_of:
    - TwissParamGroup
    range: float

```
</details>

### Induced

<details>
```yaml
name: TwissParamGroup
description: Mixin for Twiss parameters, which can be used to describe the beam optics
  of an accelerator element.
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:TwissP
attributes:
  alpha_a:
    name: alpha_a
    description: Twiss alpha parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - alpha_x
    - alphax
    rank: 1000
    slot_uri: pals:alpha_a
    alias: alpha_a
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  alpha_b:
    name: alpha_b
    description: Twiss alpha parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - alpha_y
    - alphay
    rank: 1000
    slot_uri: pals:alpha_b
    alias: alpha_b
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  beta_a:
    name: beta_a
    description: Twiss beta parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - beta_x
    - betax
    rank: 1000
    slot_uri: pals:beta_a
    alias: beta_a
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  beta_b:
    name: beta_b
    description: Twiss beta parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - beta_y
    - betay
    rank: 1000
    slot_uri: pals:beta_b
    alias: beta_b
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  eta_x:
    name: eta_x
    description: Twiss dispersion parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etax
    rank: 1000
    slot_uri: pals:eta_x
    alias: eta_x
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  eta_y:
    name: eta_y
    description: Twiss dispersion parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etay
    rank: 1000
    slot_uri: pals:eta_y
    alias: eta_y
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  etap_x:
    name: etap_x
    description: Twiss dispersion slope parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etapx
    rank: 1000
    slot_uri: pals:etap_x
    alias: etap_x
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  etap_y:
    name: etap_y
    description: Twiss dispersion slope parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - etapy
    rank: 1000
    slot_uri: pals:etap_y
    alias: etap_y
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  phi_a:
    name: phi_a
    description: Twiss phase advance parameter in the horizontal plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - phi_x
    - phix
    - psi_x
    - psix
    rank: 1000
    slot_uri: pals:phi_a
    alias: phi_a
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float
  phi_b:
    name: phi_b
    description: Twiss phase advance parameter in the vertical plane.
    from_schema: https://w3id.org/accelerator-core
    aliases:
    - phi_y
    - phiy
    - psi_y
    - psiy
    rank: 1000
    slot_uri: pals:phi_b
    alias: phi_b
    owner: TwissParamGroup
    domain_of:
    - TwissParamGroup
    range: float

```
</details>