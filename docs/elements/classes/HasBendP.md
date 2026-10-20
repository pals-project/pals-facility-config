

# Class: HasBendP 



URI: [pals:class/HasBendP](https://pals-project.readthedocs.io/class/HasBendP)


```mermaid
erDiagram
BendParamGroup {
    float L_chord  
    float L_rectangle  
    float L_sagitta  
    float angle_ref  
    float bend_field_actual  
    float bend_field_ref  
    float e1  
    float e1_rect  
    float e2  
    float e2_rect  
    float edge1_int  
    float edge2_int  
    float g_actual  
    float g_ref  
    float h1  
    float h2  
    MultipoleGeometryEnum multipole_geometry  
    ReferenceGeometryEnum ref_geometry  
    float rho_ref  
    float tilt_ref  
}
HasBendP {

}

HasBendP ||--|o BendParamGroup : "BendP"

```



<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [BendP](../slots/BendP.md) | 0..1 <br/> [BendParamGroup](../classes/BendParamGroup.md) | A mixin for bend parameters that are aligned with PALS BendP (Bend Parameters) for interoperability with the Particle Accelerator Language Standard (PALS). | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Bend](../classes/Bend.md) | Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight. |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:HasBendP |
| native | pals:HasBendP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasBendP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  BendP:
    name: BendP
    description: A mixin for bend parameters that are aligned with PALS BendP (Bend
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - HasBendP
    range: BendParamGroup
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HasBendP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  BendP:
    name: BendP
    description: A mixin for bend parameters that are aligned with PALS BendP (Bend
      Parameters) for interoperability with the Particle Accelerator Language Standard
      (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: BendP
    owner: HasBendP
    domain_of:
    - HasBendP
    range: BendParamGroup
    inlined: true

```
</details>