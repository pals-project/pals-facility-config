

# Class: HasMagneticMultipoleP 



URI: [pals:HasMagneticMultipoleP](https://pals-project.readthedocs.io/HasMagneticMultipoleP)





```mermaid
 classDiagram
    class HasMagneticMultipoleP
    click HasMagneticMultipoleP href "../HasMagneticMultipoleP/"
      HasMagneticMultipoleP <|-- Multipole
        click Multipole href "../Multipole/"
      HasMagneticMultipoleP <|-- Kicker
        click Kicker href "../Kicker/"
      HasMagneticMultipoleP <|-- Cavity
        click Cavity href "../Cavity/"
      
      HasMagneticMultipoleP : MagneticMultipoleP
        
          
    
        
        
        HasMagneticMultipoleP --> "0..1" MagneticMultipoleParamGroup : MagneticMultipoleP
        click MagneticMultipoleParamGroup href "../MagneticMultipoleParamGroup/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [MagneticMultipoleP](MagneticMultipoleP.md) | 0..1 <br/> [MagneticMultipoleParamGroup](MagneticMultipoleParamGroup.md) | A mixin for magnetic multipole parameters that are aligned with PALS Magnetic... | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |









## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:HasMagneticMultipoleP |
| native | pals:HasMagneticMultipoleP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasMagneticMultipoleP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: A mixin for magnetic multipole parameters that are aligned with PALS
      MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
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
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: A mixin for magnetic multipole parameters that are aligned with PALS
      MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with
      the Particle Accelerator Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: MagneticMultipoleP
    owner: HasMagneticMultipoleP
    domain_of:
    - HasMagneticMultipoleP
    range: MagneticMultipoleParamGroup
    inlined: true

```
</details>