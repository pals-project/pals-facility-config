

# Class: ReferenceParamGroup 


_Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals_config:class/ReferenceParamGroup](https://w3id.org/pals-config/class/ReferenceParamGroup)


```mermaid
erDiagram
ReferenceParamGroup {
    float E_tot_ref  
    float pc_ref  
    string species_ref  
    float time_ref  
    string id  
}



```




## Inheritance
* [ParamGroup](../classes/ParamGroup.md)
    * **ReferenceParamGroup**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [species_ref](../slots/species_ref.md) | 0..1 <br/> [String](../types/String.md) | A reference to a species or particle type, such as an ion, electron, or proton. | direct |
| [pc_ref](../slots/pc_ref.md) | 0..1 <br/> [Float](../types/Float.md) | [MeV] Reference momentum times speed of light, i.e. beam momentum in MeV/c. | direct |
| [E_tot_ref](../slots/E_tot_ref.md) | 0..1 <br/> [Float](../types/Float.md) | [eV] Reference total energy | direct |
| [time_ref](../slots/time_ref.md) | 0..1 <br/> [Float](../types/Float.md) | [s] Reference time | direct |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [ParamGroup](../classes/ParamGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasReferenceP](../classes/HasReferenceP.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Magnet](../classes/Magnet.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Solenoid](../classes/Solenoid.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Multipole](../classes/Multipole.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Bend](../classes/Bend.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Quadrupole](../classes/Quadrupole.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Octupole](../classes/Octupole.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Sextupole](../classes/Sextupole.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Kicker](../classes/Kicker.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [ACKicker](../classes/ACKicker.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Aperture](../classes/Aperture.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [Cavity](../classes/Cavity.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [CrabCavity](../classes/CrabCavity.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [RFCavity](../classes/RFCavity.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |
| [BeginningEle](../classes/BeginningEle.md) | [ReferenceP](../slots/ReferenceP.md) | range | [ReferenceParamGroup](../classes/ReferenceParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:ReferenceParamGroup |
| native | pals_config:ReferenceParamGroup |
| broad | pals:ReferenceP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferenceParamGroup
description: Mixin for reference parameters that are aligned with PALS ReferenceP
  (Reference Parameters)  for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/pals-config
broad_mappings:
- pals:ReferenceP
is_a: ParamGroup
attributes:
  species_ref:
    name: species_ref
    description: A reference to a species or particle type, such as an ion, electron,
      or proton.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:species_ref
    rank: 1000
    domain_of:
    - ReferenceParamGroup
    range: string
  pc_ref:
    name: pc_ref
    description: '[MeV] Reference momentum times speed of light, i.e. beam momentum
      in MeV/c.'
    from_schema: https://w3id.org/pals-config
    aliases:
    - pCentral
    close_mappings:
    - pals:pc_ref
    rank: 1000
    domain_of:
    - ReferenceParamGroup
    range: float
    unit:
      ucum_code: MeV
  E_tot_ref:
    name: E_tot_ref
    description: '[eV] Reference total energy'
    from_schema: https://w3id.org/pals-config
    aliases:
    - ETotal
    close_mappings:
    - pals:E_tot_ref
    rank: 1000
    domain_of:
    - ReferenceParamGroup
    range: float
    unit:
      ucum_code: eV
  time_ref:
    name: time_ref
    description: '[s] Reference time'
    from_schema: https://w3id.org/pals-config
    aliases:
    - tRef
    close_mappings:
    - pals:time_ref
    rank: 1000
    domain_of:
    - ReferenceParamGroup
    range: float
    unit:
      ucum_code: s

```
</details>

### Induced

<details>
```yaml
name: ReferenceParamGroup
description: Mixin for reference parameters that are aligned with PALS ReferenceP
  (Reference Parameters)  for interoperability with the Particle Accelerator Language
  Standard (PALS).
from_schema: https://w3id.org/pals-config
broad_mappings:
- pals:ReferenceP
is_a: ParamGroup
attributes:
  species_ref:
    name: species_ref
    description: A reference to a species or particle type, such as an ion, electron,
      or proton.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:species_ref
    rank: 1000
    alias: species_ref
    owner: ReferenceParamGroup
    domain_of:
    - ReferenceParamGroup
    range: string
  pc_ref:
    name: pc_ref
    description: '[MeV] Reference momentum times speed of light, i.e. beam momentum
      in MeV/c.'
    from_schema: https://w3id.org/pals-config
    aliases:
    - pCentral
    close_mappings:
    - pals:pc_ref
    rank: 1000
    alias: pc_ref
    owner: ReferenceParamGroup
    domain_of:
    - ReferenceParamGroup
    range: float
    unit:
      ucum_code: MeV
  E_tot_ref:
    name: E_tot_ref
    description: '[eV] Reference total energy'
    from_schema: https://w3id.org/pals-config
    aliases:
    - ETotal
    close_mappings:
    - pals:E_tot_ref
    rank: 1000
    alias: E_tot_ref
    owner: ReferenceParamGroup
    domain_of:
    - ReferenceParamGroup
    range: float
    unit:
      ucum_code: eV
  time_ref:
    name: time_ref
    description: '[s] Reference time'
    from_schema: https://w3id.org/pals-config
    aliases:
    - tRef
    close_mappings:
    - pals:time_ref
    rank: 1000
    alias: time_ref
    owner: ReferenceParamGroup
    domain_of:
    - ReferenceParamGroup
    range: float
    unit:
      ucum_code: s
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/pals-config
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: ReferenceParamGroup
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true

```
</details>