

# Class: NodeLabels 


_Static node-type label strings for the graph projection, covering all node categories except Device. The device label is derived from ControlProfileFamily.device_domain and need not be repeated here._





URI: [https://w3id.org/narad_linkml/schema/narad/NodeLabels](https://w3id.org/narad_linkml/schema/narad/NodeLabels)





```mermaid
 classDiagram
    class NodeLabels
    click NodeLabels href "../NodeLabels/"
      NodeLabels : capability
        
      NodeLabels : capability_family
        
      NodeLabels : profile
        
      NodeLabels : signal
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [capability_family](capability_family.md) | 0..1 <br/> [String](String.md) |  | direct |
| [profile](profile.md) | 0..1 <br/> [String](String.md) |  | direct |
| [capability](capability.md) | 0..1 <br/> [String](String.md) |  | direct |
| [signal](signal.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GraphProjection](GraphProjection.md) | [node_labels](node_labels.md) | range | [NodeLabels](NodeLabels.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/NodeLabels |
| native | https://w3id.org/narad_linkml/schema/narad/NodeLabels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NodeLabels
description: Static node-type label strings for the graph projection, covering all
  node categories except Device. The device label is derived from ControlProfileFamily.device_domain
  and need not be repeated here.
from_schema: https://w3id.org/narad_linkml/schema/narad/
slots:
- capability_family
- profile
- capability
- signal

```
</details>

### Induced

<details>
```yaml
name: NodeLabels
description: Static node-type label strings for the graph projection, covering all
  node categories except Device. The device label is derived from ControlProfileFamily.device_domain
  and need not be repeated here.
from_schema: https://w3id.org/narad_linkml/schema/narad/
attributes:
  capability_family:
    name: capability_family
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: capability_family
    owner: NodeLabels
    domain_of:
    - NodeLabels
    range: string
  profile:
    name: profile
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: profile
    owner: NodeLabels
    domain_of:
    - NodeLabels
    range: string
  capability:
    name: capability
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: capability
    owner: NodeLabels
    domain_of:
    - NodeLabels
    range: string
  signal:
    name: signal
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: signal
    owner: NodeLabels
    domain_of:
    - NodeLabels
    range: string

```
</details>