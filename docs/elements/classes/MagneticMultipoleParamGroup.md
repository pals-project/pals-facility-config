

# Class: MagneticMultipoleParamGroup 


_Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7_

_  tilt: 0.7_

_- order: 3_

_  Bn: 27.3_

_- order: 2_

_  BnL: 3.47e1_

_- order: 1_

_  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength_

_```_





URI: [pals:class/MagneticMultipoleParamGroup](https://pals-project.readthedocs.io/class/MagneticMultipoleParamGroup)


```mermaid
erDiagram
MagneticMultipoleParamGroup {

}
MultipoleParameterGroup {
    float Bn  
    float Bs  
    float En  
    float EnL  
    float Es  
    float EsL  
    float Kn  
    float Ks  
    integer order  
    float tilt  
}

MagneticMultipoleParamGroup ||--}o MultipoleParameterGroup : "mag_components"

```



<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [mag_components](../slots/mag_components.md) | * <br/> [MultipoleParameterGroup](../classes/MultipoleParameterGroup.md) | Magnetic multipole components, one per order N. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasMagneticMultipoleP](../classes/HasMagneticMultipoleP.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Multipole](../classes/Multipole.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Bend](../classes/Bend.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Quadrupole](../classes/Quadrupole.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Octupole](../classes/Octupole.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Sextupole](../classes/Sextupole.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Kicker](../classes/Kicker.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [ACKicker](../classes/ACKicker.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [Cavity](../classes/Cavity.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [CrabCavity](../classes/CrabCavity.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [RFCavity](../classes/RFCavity.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [NormalConductingRFCavity](../classes/NormalConductingRFCavity.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |
| [SuperConductingRFCavity](../classes/SuperConductingRFCavity.md) | [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | range | [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:MagneticMultipoleParamGroup |
| native | pals:MagneticMultipoleParamGroup |
| broad | pals:MagneticMultipoleP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MagneticMultipoleParamGroup
description: "Mixin for magnetic multipole parameters,  which can be used to describe\
  \ the magnetic field components of an accelerator element. This mixin is aligned\
  \ with PALS MagneticMultipoleP for interoperability with the Particle Accelerator\
  \ Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml\
  \ mag_components: - order: 7\n  tilt: 0.7\n- order: 3\n  Bn: 27.3\n- order: 2\n\
  \  BnL: 3.47e1\n- order: 1\n  Kn: 0.85     # normalized form, e.g. a quadrupole's\
  \ k1-like strength\n```"
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:MagneticMultipoleP
attributes:
  mag_components:
    name: mag_components
    description: Magnetic multipole components, one per order N.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - MagneticMultipoleParamGroup
    range: MultipoleParameterGroup
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: MagneticMultipoleParamGroup
description: "Mixin for magnetic multipole parameters,  which can be used to describe\
  \ the magnetic field components of an accelerator element. This mixin is aligned\
  \ with PALS MagneticMultipoleP for interoperability with the Particle Accelerator\
  \ Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml\
  \ mag_components: - order: 7\n  tilt: 0.7\n- order: 3\n  Bn: 27.3\n- order: 2\n\
  \  BnL: 3.47e1\n- order: 1\n  Kn: 0.85     # normalized form, e.g. a quadrupole's\
  \ k1-like strength\n```"
from_schema: https://w3id.org/accelerator-core
broad_mappings:
- pals:MagneticMultipoleP
attributes:
  mag_components:
    name: mag_components
    description: Magnetic multipole components, one per order N.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: mag_components
    owner: MagneticMultipoleParamGroup
    domain_of:
    - MagneticMultipoleParamGroup
    range: MultipoleParameterGroup
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>