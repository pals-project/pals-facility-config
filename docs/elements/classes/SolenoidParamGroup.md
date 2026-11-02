

# Class: SolenoidParamGroup 


_Mixin for solenoid-specific parameters._





URI: [acc:class/SolenoidParamGroup](https://example.org/accelerator-core/class/SolenoidParamGroup)


```mermaid
erDiagram
SolenoidParamGroup {
    float Bsol  
    float Ksol  
    string id  
}



```




## Inheritance
* [ParamGroup](../classes/ParamGroup.md)
    * **SolenoidParamGroup**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Ksol](../slots/Ksol.md) | 0..1 <br/> [Float](../types/Float.md) | Normalized solenoid strength. | direct |
| [Bsol](../slots/Bsol.md) | 0..1 <br/> [Float](../types/Float.md) | Solenoid field. | direct |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) | A unique identifier for the instance. | [ParamGroup](../classes/ParamGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HasSolenoidP](../classes/HasSolenoidP.md) | [SolenoidP](../slots/SolenoidP.md) | range | [SolenoidParamGroup](../classes/SolenoidParamGroup.md) |
| [Solenoid](../classes/Solenoid.md) | [SolenoidP](../slots/SolenoidP.md) | range | [SolenoidParamGroup](../classes/SolenoidParamGroup.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'id': {'value_presence': 'PRESENT'}}``` | | |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:SolenoidParamGroup |
| native | acc:SolenoidParamGroup |
| exact | pals:SolenoidP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SolenoidParamGroup
description: Mixin for solenoid-specific parameters.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:SolenoidP
is_a: ParamGroup
attributes:
  Ksol:
    name: Ksol
    description: Normalized solenoid strength.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:Ksol
    rank: 1000
    domain_of:
    - SolenoidParamGroup
    range: float
  Bsol:
    name: Bsol
    description: Solenoid field.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:Bsol
    rank: 1000
    domain_of:
    - SolenoidParamGroup
    range: float
    unit:
      ucum_code: T
rules:
- preconditions:
    slot_conditions:
      id:
        name: id
        value_presence: PRESENT
  postconditions:
    exactly_one_of:
    - slot_conditions:
        Ksol:
          name: Ksol
          value_presence: PRESENT
    - slot_conditions:
        Bsol:
          name: Bsol
          value_presence: PRESENT
  description: A solenoid must have one of, and exactly one of, Ksol or Bsol.

```
</details>

### Induced

<details>
```yaml
name: SolenoidParamGroup
description: Mixin for solenoid-specific parameters.
from_schema: https://w3id.org/accelerator-core
exact_mappings:
- pals:SolenoidP
is_a: ParamGroup
attributes:
  Ksol:
    name: Ksol
    description: Normalized solenoid strength.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:Ksol
    rank: 1000
    alias: Ksol
    owner: SolenoidParamGroup
    domain_of:
    - SolenoidParamGroup
    range: float
  Bsol:
    name: Bsol
    description: Solenoid field.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:Bsol
    rank: 1000
    alias: Bsol
    owner: SolenoidParamGroup
    domain_of:
    - SolenoidParamGroup
    range: float
    unit:
      ucum_code: T
  id:
    name: id
    description: A unique identifier for the instance.
    from_schema: https://w3id.org/accelerator-core
    close_mappings:
    - pals:id
    rank: 1000
    identifier: true
    alias: id
    owner: SolenoidParamGroup
    domain_of:
    - Node
    - Affiliation
    - ParamGroup
    - Edge
    range: string
    required: true
rules:
- preconditions:
    slot_conditions:
      id:
        name: id
        value_presence: PRESENT
  postconditions:
    exactly_one_of:
    - slot_conditions:
        Ksol:
          name: Ksol
          value_presence: PRESENT
    - slot_conditions:
        Bsol:
          name: Bsol
          value_presence: PRESENT
  description: A solenoid must have one of, and exactly one of, Ksol or Bsol.

```
</details>