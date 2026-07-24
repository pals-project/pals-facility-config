

# Class: HasSolenoidP 



URI: [pals:HasSolenoidP](https://pals-project.readthedocs.io/HasSolenoidP)





```mermaid
 classDiagram
    class HasSolenoidP
    click HasSolenoidP href "../HasSolenoidP/"
      HasSolenoidP <|-- Solenoid
        click Solenoid href "../Solenoid/"
      
      HasSolenoidP : SolenoidP
        
          
    
        
        
        HasSolenoidP --> "0..1" SolenoidParamGroup : SolenoidP
        click SolenoidParamGroup href "../SolenoidParamGroup/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [SolenoidP](SolenoidP.md) | 0..1 <br/> [SolenoidParamGroup](SolenoidParamGroup.md) | A mixin for solenoid-specific parameters that are aligned with PALS SolenoidP... | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Solenoid](Solenoid.md) | A magnet with a primarily longitudinal magnetic field used for focusing |









## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:HasSolenoidP |
| native | pals:HasSolenoidP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasSolenoidP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  SolenoidP:
    name: SolenoidP
    description: A mixin for solenoid-specific parameters that are aligned with PALS
      SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator
      Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - HasSolenoidP
    range: SolenoidParamGroup
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HasSolenoidP
from_schema: https://w3id.org/accelerator-core
mixin: true
attributes:
  SolenoidP:
    name: SolenoidP
    description: A mixin for solenoid-specific parameters that are aligned with PALS
      SolenoidP (Solenoid Parameters) for interoperability with the Particle Accelerator
      Language Standard (PALS).
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: SolenoidP
    owner: HasSolenoidP
    domain_of:
    - HasSolenoidP
    range: SolenoidParamGroup
    inlined: true

```
</details>