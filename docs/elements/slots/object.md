

# Slot: object 



URI: [rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object)
Alias: object

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MountedOn](../classes/MountedOn.md) | A relationship indicating that the subject component is mounted on the object component in a specified context,  such as a diagnostic device mounted on a magnet. |  no  |
| [Precedes](../classes/Precedes.md) | A relationship indicating that the subject component precedes the object component in a specified context,  such as along a beamline. |  no  |
| [HasSetpointSignal](../classes/HasSetpointSignal.md) |  |  no  |
| [Contains](../classes/Contains.md) | A relationship indicating that the subject component contains the object component in a specified context,  such as within a BeamLineSection or other organizational grouping. |  no  |
| [Intersects](../classes/Intersects.md) | A relationship indicating that the subject component intersects the object component in a specified context,  such as a beamline and a diagnostic device. |  no  |
| [NearestTo](../classes/NearestTo.md) | A relationship indicating that the subject component is nearest to the object component in a specified context,  such as a diagnostic device nearest to a magnet. |  no  |
| [HasSignal](../classes/HasSignal.md) |  |  no  |
| [AdjacentTo](../classes/AdjacentTo.md) | A relationship indicating that the subject component is adjacent to the object component and not overlapping<br> in a specified context, such as radiation detector and a magnet. |  no  |
| [Edge](../classes/Edge.md) | Abstract base for subject-predicate-object associations. |  no  |
| [HasReadbackSignal](../classes/HasReadbackSignal.md) |  |  no  |
| [SignalBinding](../classes/SignalBinding.md) | Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal. |  yes  |
| [Overlaps](../classes/Overlaps.md) | A relationship indicating that the subject component overlaps the object component in a specified context,  such as a magnet and a diagnostic device. |  no  |
| [HasConnectingBranch](../classes/HasConnectingBranch.md) | A relationship indicating that the subject component has a connecting branch to the object component in a specified context,  such as a beamline section having a fork as a connecting branch. |  no  |
| [HasCommandSignal](../classes/HasCommandSignal.md) |  |  no  |
| [HasLimitSignal](../classes/HasLimitSignal.md) |  |  no  |
| [IsPartOf](../classes/IsPartOf.md) | A relationship indicating that the subject component is part of the object component in a specified context,  such as a magnet being part of a BeamLineSection. |  no  |
| [ComponentRelation](../classes/ComponentRelation.md) | Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds. |  yes  |
| [Controls](../classes/Controls.md) | A relationship indicating that the subject component controls the object component in a specified context,  such as a power supply controlling a magnet. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Edge](../classes/Edge.md) |
| Slot URI | [rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:object |
| native | acc:object |




## LinkML Source

<details>
```yaml
name: object
from_schema: https://w3id.org/accelerator-core
rank: 1000
slot_uri: rdf:object
alias: object
domain_of:
- Edge
range: string
required: true

```
</details>