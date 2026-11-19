

# Class: HasMagneticMultipoleP 



URI: [pals_config:class/HasMagneticMultipoleP](https://w3id.org/pals-config/class/HasMagneticMultipoleP)


```mermaid
erDiagram
HasMagneticMultipoleP {

}
MagneticMultipoleParamGroup {
    string id  
}
MultipoleParameterGroup {
    float Bn  
    float BnL  
    float Bs  
    float BsL  
    float En  
    float EnL  
    float Es  
    float EsL  
    float Kn  
    float KnL  
    float Ks  
    float KsL  
    integer order  
    float tilt  
}

HasMagneticMultipoleP ||--|o MagneticMultipoleParamGroup : "MagneticMultipoleP"
MagneticMultipoleParamGroup ||--}o MultipoleParameterGroup : "mag_components"

```



<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [MagneticMultipoleP](../slots/MagneticMultipoleP.md) | 0..1 <br/> [MagneticMultipoleParamGroup](../classes/MagneticMultipoleParamGroup.md) | A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Multipole](../classes/Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or octupole.<br>Only one of the electric or magnetic multipole components should be present, not both. |
| [Kicker](../classes/Kicker.md) | A magnet primarily used to steer the beam.<br>Can deflect the beam transversely in both planes, or a single plane, depending on the design and parameters of the kicker. <br>Only one of the electric or magnetic multipole components should be present, not both. |
| [Cavity](../classes/Cavity.md) | A cavity used for beam acceleration or manipulation. |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:HasMagneticMultipoleP |
| native | pals_config:HasMagneticMultipoleP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasMagneticMultipoleP
from_schema: https://w3id.org/pals-config
mixin: true
attributes:
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: A mixin for magnetic multipole parameters that are aligned with PALS
      MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    domain_of:
    - HasMagneticMultipoleP
    range: MagneticMultipoleParamGroup
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HasMagneticMultipoleP
from_schema: https://w3id.org/pals-config
mixin: true
attributes:
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: A mixin for magnetic multipole parameters that are aligned with PALS
      MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: MagneticMultipoleP
    owner: HasMagneticMultipoleP
    domain_of:
    - HasMagneticMultipoleP
    range: MagneticMultipoleParamGroup
    inlined: true

```
</details>