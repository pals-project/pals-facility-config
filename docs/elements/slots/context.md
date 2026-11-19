

# Slot: context 


_The frame of reference / domain in which this relationship is asserted to hold._





URI: [pals_config:slot/context](https://w3id.org/pals-config/slot/context)
Alias: context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MountedOn](../classes/MountedOn.md) | A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet. |  no  |
| [Contains](../classes/Contains.md) | A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping. |  no  |
| [Precedes](../classes/Precedes.md) | A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline. |  yes  |
| [Intersects](../classes/Intersects.md) | A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device. |  no  |
| [NearestTo](../classes/NearestTo.md) | A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet. |  no  |
| [AdjacentTo](../classes/AdjacentTo.md) | A relationship indicating that the subject component is adjacent to the object component and not overlapping<br> in a specified context, such as radiation detector and a magnet. |  no  |
| [HasConnectingBranch](../classes/HasConnectingBranch.md) | A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch. |  yes  |
| [Overlaps](../classes/Overlaps.md) | A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device. |  no  |
| [IsPartOf](../classes/IsPartOf.md) | A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection. |  yes  |
| [ComponentRelation](../classes/ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds. |  no  |
| [Controls](../classes/Controls.md) | A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelationContextEnum](../enums/RelationContextEnum.md) |
| Domain Of | [ComponentRelation](../classes/ComponentRelation.md), [IsPartOf](../classes/IsPartOf.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals_config:context |
| native | pals_config:context |




## LinkML Source

<details>
```yaml
name: context
description: The frame of reference / domain in which this relationship is asserted
  to hold.
from_schema: https://w3id.org/pals-config
rank: 1000
alias: context
domain_of:
- ComponentRelation
- IsPartOf
range: RelationContextEnum
required: true

```
</details>