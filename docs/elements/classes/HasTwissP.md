

# Class: HasTwissP 



URI: [pals_config:class/HasTwissP](https://w3id.org/pals-config/class/HasTwissP)


```mermaid
erDiagram
HasTwissP {

}
TwissParamGroup {
    float alpha_a  
    float alpha_b  
    float beta_a  
    float beta_b  
    float cmat11  
    float cmat12  
    float cmat21  
    float cmat22  
    float dalpha_a_dpz  
    float dalpha_b_dpz  
    float dbeta_a_dpz  
    float dbeta_b_dpz  
    float deta_x_dpz  
    float deta_x_ds  
    float deta_y_dpz  
    float deta_y_ds  
    float detap_x_dpz  
    float detap_y_dpz  
    float eta_x  
    float eta_y  
    float etap_x  
    float etap_y  
    float phi_a  
    float phi_b  
    string id  
}

HasTwissP ||--|o TwissParamGroup : "TwissP"

```



<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TwissP](../slots/TwissP.md) | 0..1 <br/> [TwissParamGroup](../classes/TwissParamGroup.md) | A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Magnet](../classes/Magnet.md) | An accelerator device that produces a magnetic field for beam control. |
| [BeamProfileMonitor](../classes/BeamProfileMonitor.md) | A diagnostic device used to measure transverse beam profile. |
| [BeamPositionMonitor](../classes/BeamPositionMonitor.md) | A diagnostic device used to measure transverse beam position. |
| [Aperture](../classes/Aperture.md) | A diagnostic or limiting aperture element used to constrain or characterize beam passage. |
| [Cavity](../classes/Cavity.md) | A cavity used for beam acceleration or manipulation. |
| [Marker](../classes/Marker.md) | A virtual component used as a reference point or marker in the beamline structure. |
| [BeginningEle](../classes/BeginningEle.md) | Initial element at the start of a beamline branch. It holds the initial reference and Twiss parameters for the branch. A BeginningEle may be omitted when the branch is reached through a Fork that propagates its reference parameters; otherwise it is expected to be the first element in the branch. |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:HasTwissP |
| native | pals_config:HasTwissP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasTwissP
from_schema: https://w3id.org/pals-config
mixin: true
attributes:
  TwissP:
    name: TwissP
    description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    domain_of:
    - HasTwissP
    range: TwissParamGroup
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HasTwissP
from_schema: https://w3id.org/pals-config
mixin: true
attributes:
  TwissP:
    name: TwissP
    description: A mixin for Twiss parameters that are aligned with PALS TwissP (Twiss
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/pals-config
    rank: 1000
    alias: TwissP
    owner: HasTwissP
    domain_of:
    - HasTwissP
    range: TwissParamGroup
    inlined: true

```
</details>