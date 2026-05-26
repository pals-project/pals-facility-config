

# Class: NamingConventionExample 


_An example of a control system naming convention, illustrating how the template is used to generate full control system PV names from semantic signal names and device instance information.  This can be used to provide concrete examples of the expected PV naming convention for different device types and signals based on the defined NamingConvention template._

__





URI: [narad:NamingConventionExample](https://example.org/narad_linkml/schema/narad/NamingConventionExample)





```mermaid
 classDiagram
    class NamingConventionExample
    click NamingConventionExample href "../NamingConventionExample/"
      NamingConventionExample : description
        
      NamingConventionExample : example
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [example](example.md) | 1 <br/> [String](String.md) | A single example of how this naming convention is applied to a specific devic... | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | Detailed description of the entity | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NamingConvention](NamingConvention.md) | [examples](examples.md) | range | [NamingConventionExample](NamingConventionExample.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | narad:NamingConventionExample |
| native | narad:NamingConventionExample |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamingConventionExample
description: 'An example of a control system naming convention, illustrating how the
  template is used to generate full control system PV names from semantic signal names
  and device instance information.  This can be used to provide concrete examples
  of the expected PV naming convention for different device types and signals based
  on the defined NamingConvention template.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slots:
- example
- description
slot_usage:
  example:
    name: example
    identifier: true

```
</details>

### Induced

<details>
```yaml
name: NamingConventionExample
description: 'An example of a control system naming convention, illustrating how the
  template is used to generate full control system PV names from semantic signal names
  and device instance information.  This can be used to provide concrete examples
  of the expected PV naming convention for different device types and signals based
  on the defined NamingConvention template.

  '
from_schema: https://w3id.org/narad_linkml/schema/narad/system
slot_usage:
  example:
    name: example
    identifier: true
attributes:
  example:
    name: example
    description: A single example of how this naming convention is applied to a specific
      device instance and signal.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    identifier: true
    alias: example
    owner: NamingConventionExample
    domain_of:
    - NamingConventionExample
    - TemplateExample
    range: string
  description:
    name: description
    description: Detailed description of the entity.
    in_subset:
    - label
    from_schema: https://w3id.org/narad_linkml/schema/narad/system
    rank: 1000
    alias: description
    owner: NamingConventionExample
    domain_of:
    - NamedThing
    - NamingConventionExample
    - TemplateExample
    range: string

```
</details>