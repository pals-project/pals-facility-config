

# Class: HasRFP 



URI: [acc:class/HasRFP](https://example.org/accelerator-core/class/HasRFP)


```mermaid
erDiagram
HasRFP {

}
RFParamGroup {
    float L_active  
    CavityTypeEnum cavity_type  
    float dE_ref  
    float frequency  
    integer harmon  
    float multipass_phase  
    integer num_cells  
    float phase  
    float voltage  
    ZeroPhaseEnum zero_phase  
    string id  
}

HasRFP ||--|o RFParamGroup : "RFP"

```



<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [RFP](../slots/RFP.md) | 0..1 <br/> [RFParamGroup](../classes/RFParamGroup.md) | A mixin for RF parameters that are aligned with PALS RFP (RF Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [RFCavity](../classes/RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation. |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:HasRFP |
| native | acc:HasRFP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasRFP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  RFP:
    name: RFP
    description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters)
      for interoperability with the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - HasRFP
    range: RFParamGroup
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HasRFP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  RFP:
    name: RFP
    description: A mixin for RF parameters that are aligned with PALS RFP (RF Parameters)
      for interoperability with the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: RFP
    owner: HasRFP
    domain_of:
    - HasRFP
    range: RFParamGroup
    inlined: true

```
</details>