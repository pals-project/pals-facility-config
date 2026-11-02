

# Slot: beamline_context 


_The specific BeamLine this relationship is defined with respect to (relevant when context=beamline_order). Only an edge-property slot for edges that are defined with respect to a specific BeamLine._





URI: [acc:slot/beamline_context](https://example.org/accelerator-core/slot/beamline_context)
Alias: beamline_context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contains](../classes/Contains.md) | A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping. |  yes  |
| [Precedes](../classes/Precedes.md) | A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline. |  no  |
| [HasConnectingBranch](../classes/HasConnectingBranch.md) | A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch. |  no  |
| [IsPartOf](../classes/IsPartOf.md) | A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BeamLine](../classes/BeamLine.md) |
| Domain Of | [Precedes](../classes/Precedes.md), [Contains](../classes/Contains.md), [IsPartOf](../classes/IsPartOf.md), [HasConnectingBranch](../classes/HasConnectingBranch.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:beamline_context |
| native | acc:beamline_context |




## LinkML Source

<details>
```yaml
name: beamline_context
description: The specific BeamLine this relationship is defined with respect to (relevant
  when context=beamline_order). Only an edge-property slot for edges that are defined
  with respect to a specific BeamLine.
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: beamline_context
domain_of:
- Precedes
- Contains
- IsPartOf
- HasConnectingBranch
range: BeamLine
required: false

```
</details>