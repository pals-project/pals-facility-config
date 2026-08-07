

# Class: PALSAccelerator 


_Root container for accelerator core components, semantic signals, and local bindings._





URI: [pals:PALSAccelerator](https://pals-project.readthedocs.io/PALSAccelerator)





```mermaid
 classDiagram
    class PALSAccelerator
    click PALSAccelerator href "../PALSAccelerator/"
      PALSAccelerator : affiliation
        
          
    
        
        
        PALSAccelerator --> "0..1" Affiliation : affiliation
        click Affiliation href "../Affiliation/"
    

        
      PALSAccelerator : authors
        
          
    
        
        
        PALSAccelerator --> "*" Author : authors
        click Author href "../Author/"
    

        
      PALSAccelerator : description
        
      PALSAccelerator : facility
        
          
    
        
        
        PALSAccelerator --> "0..1" Facility : facility
        click Facility href "../Facility/"
    

        
      PALSAccelerator : kind
        
      PALSAccelerator : notes
        
      PALSAccelerator : version
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [kind](kind.md) | 1 <br/> [String](String.md) | The LinkML class name of this instance | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description of the instance | direct |
| [affiliation](affiliation.md) | 0..1 <br/> [Affiliation](Affiliation.md) | The affiliation of the author or component, as a ROR | direct |
| [version](version.md) | 0..1 <br/> [String](String.md) | Version of the representation of a particle accelerator and its operations | direct |
| [authors](authors.md) | * <br/> [Author](Author.md) | Contains the authorship information for this representation of an accelerator... | direct |
| [notes](notes.md) | * <br/> [String](String.md) | Additional notes or comments about the representation of a particle accelerat... | direct |
| [facility](facility.md) | 0..1 <br/> [Facility](Facility.md) | A facility that contains lattice elements (physical and virtual), beamlines, ... | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:PALSAccelerator |
| native | pals:PALSAccelerator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PALSAccelerator
description: Root container for accelerator core components, semantic signals, and
  local bindings.
from_schema: https://w3id.org/accelerator-core
slots:
- kind
- description
- affiliation
attributes:
  version:
    name: version
    description: Version of the representation of a particle accelerator and its operations.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - PALSAccelerator
    range: string
    pattern: ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$
  authors:
    name: authors
    description: Contains the authorship information for this representation of an
      accelerator facility and its operations.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - PALSAccelerator
    range: Author
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    description: Additional notes or comments about the representation of a particle
      accelerator and its operations.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - PALSAccelerator
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  facility:
    name: facility
    description: A facility that contains lattice elements (physical and virtual),
      beamlines, parameter set commands, signals, etc.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    domain_of:
    - PALSAccelerator
    range: Facility
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: PALSAccelerator
description: Root container for accelerator core components, semantic signals, and
  local bindings.
from_schema: https://w3id.org/accelerator-core
attributes:
  version:
    name: version
    description: Version of the representation of a particle accelerator and its operations.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: version
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    range: string
    pattern: ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$
  authors:
    name: authors
    description: Contains the authorship information for this representation of an
      accelerator facility and its operations.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: authors
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    range: Author
    multivalued: true
    inlined_as_list: true
  notes:
    name: notes
    description: Additional notes or comments about the representation of a particle
      accelerator and its operations.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: notes
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    range: string
    multivalued: true
    inlined_as_list: true
  facility:
    name: facility
    description: A facility that contains lattice elements (physical and virtual),
      beamlines, parameter set commands, signals, etc.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: facility
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    range: Facility
  kind:
    name: kind
    description: The LinkML class name of this instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    slot_uri: pals:kind
    designates_type: true
    alias: kind
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    - Component
    - Signal
    range: string
    required: true
  description:
    name: description
    description: A human-readable description of the instance.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: description
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    - MetaParamGroup
    - BeamLine
    range: string
  affiliation:
    name: affiliation
    description: The affiliation of the author or component, as a ROR.
    from_schema: https://w3id.org/accelerator-core
    rank: 1000
    alias: affiliation
    owner: PALSAccelerator
    domain_of:
    - PALSAccelerator
    - Author
    range: Affiliation
    inlined: true
tree_root: true

```
</details>