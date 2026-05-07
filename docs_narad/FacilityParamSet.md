

# Class: FacilityParamSet 


_Facility-specific element parameters block for beamline elements. Differs from an ElementParamSet in that it captures facility-specific metadata about the element (e.g. type designation, model name) rather than physics parameters._





URI: [narad:FacilityParamSet](https://w3id.org/narad_linkml/schema/narad/FacilityParamSet)





```mermaid
 classDiagram
    class FacilityParamSet
    click FacilityParamSet href "../FacilityParamSet/"
      FacilityParamSet : facility_element_type
        
      FacilityParamSet : modeled_as
        
      FacilityParamSet : properties
        
          
    
        
        
        FacilityParamSet --> "0..1" AnyValue : properties
        click AnyValue href "../AnyValue/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [facility_element_type](facility_element_type.md) | 0..1 <br/> [String](String.md) | Facility-specific element type designation (e | direct |
| [modeled_as](modeled_as.md) | 0..1 <br/> [String](String.md) | Accelerator physics code model element type (e | direct |
| [properties](properties.md) | 0..1 <br/> [AnyValue](AnyValue.md) | Intentionally open-ended key-value property map for element-specific or facil... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BeamlineElement](BeamlineElement.md) | [facility_param_set](facility_param_set.md) | range | [FacilityParamSet](FacilityParamSet.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:FacilityParamSet |
| native | narad:FacilityParamSet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FacilityParamSet
description: Facility-specific element parameters block for beamline elements. Differs
  from an ElementParamSet in that it captures facility-specific metadata about the
  element (e.g. type designation, model name) rather than physics parameters.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- facility_element_type
- modeled_as
- properties

```
</details>

### Induced

<details>
```yaml
name: FacilityParamSet
description: Facility-specific element parameters block for beamline elements. Differs
  from an ElementParamSet in that it captures facility-specific metadata about the
  element (e.g. type designation, model name) rather than physics parameters.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
attributes:
  facility_element_type:
    name: facility_element_type
    description: Facility-specific element type designation (e.g. WarmCavity, QW,
      HCorrector). named facility_element_type here to avoid conflict with the LinkML
      metamodel 'type'  designator used for polymorphic class selection.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    aliases:
    - type
    rank: 1000
    alias: facility_element_type
    owner: FacilityParamSet
    domain_of:
    - FacilityParamSet
    range: string
  modeled_as:
    name: modeled_as
    description: Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: modeled_as
    owner: FacilityParamSet
    domain_of:
    - FacilityParamSet
    range: string
  properties:
    name: properties
    description: Intentionally open-ended key-value property map for element-specific
      or facility-specific parameters.
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: properties
    owner: FacilityParamSet
    domain_of:
    - FacilityParamSet
    range: AnyValue

```
</details>