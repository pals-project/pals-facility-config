

# Class: MagneticMultipoleParams 


_Magnetic multipole physics parameters._





URI: [https://w3id.org/narad_linkml/schema/narad/MagneticMultipoleParams](https://w3id.org/narad_linkml/schema/narad/MagneticMultipoleParams)





```mermaid
 classDiagram
    class MagneticMultipoleParams
    click MagneticMultipoleParams href "../MagneticMultipoleParams/"
      MagneticMultipoleParams : Kn1
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Kn1](Kn1.md) | 0..1 <br/> [Float](Float.md) | First-order magnetic multipole coefficient (quadrupole strength) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BeamlineElement](BeamlineElement.md) | [MagneticMultipoleP](MagneticMultipoleP.md) | range | [MagneticMultipoleParams](MagneticMultipoleParams.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/MagneticMultipoleParams |
| native | https://w3id.org/narad_linkml/schema/narad/MagneticMultipoleParams |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MagneticMultipoleParams
description: Magnetic multipole physics parameters.
from_schema: https://w3id.org/narad_linkml/schema/narad/
slots:
- Kn1

```
</details>

### Induced

<details>
```yaml
name: MagneticMultipoleParams
description: Magnetic multipole physics parameters.
from_schema: https://w3id.org/narad_linkml/schema/narad/
attributes:
  Kn1:
    name: Kn1
    description: First-order magnetic multipole coefficient (quadrupole strength).
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: Kn1
    owner: MagneticMultipoleParams
    domain_of:
    - MagneticMultipoleParams
    range: float

```
</details>