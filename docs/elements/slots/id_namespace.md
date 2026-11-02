

# Slot: id_namespace 


_Base IRI for this facility's instance identifiers. Identifiers in the data (id, subject, object, beamline_context) are written bare, e.g. RF_LASER, and are made absolute by prefixing this value on export to RDF or Neo4j, e.g. tag:jlab.org,2026:uitf/ + RF_LASER. Required, with no schema-wide default, so that facilities cannot silently share a namespace and collide. Any absolute IRI is accepted, resolvable (https://...) or not (tag:..., urn:...). It must end in '/', '#' or ':' so that simple concatenation yields a well-formed IRI._





URI: [acc:slot/id_namespace](https://example.org/accelerator-core/slot/id_namespace)
Alias: id_namespace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Facility](../classes/Facility.md) | A facility that houses one or more accelerators. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](../types/Uri.md) |
| Domain Of | [Facility](../classes/Facility.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Facility](../classes/Facility.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Za-z][A-Za-z0-9+.\-]*:[^\s<>"{}|\\^`]*[/#:]$` |











## Examples

| Value |
| --- |
| https://example.org/accelerator-core/facility/01gq9xj92/ |
| tag:jlab.org,2026:uitf/ |
| urn:example:facility/01gq9xj92 |
| http://example.org/facility/01gq9xj92 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acc:id_namespace |
| native | acc:id_namespace |




## LinkML Source

<details>
```yaml
name: id_namespace
description: Base IRI for this facility's instance identifiers. Identifiers in the
  data (id, subject, object, beamline_context) are written bare, e.g. RF_LASER, and
  are made absolute by prefixing this value on export to RDF or Neo4j, e.g. tag:jlab.org,2026:uitf/
  + RF_LASER. Required, with no schema-wide default, so that facilities cannot silently
  share a namespace and collide. Any absolute IRI is accepted, resolvable (https://...)
  or not (tag:..., urn:...). It must end in '/', '#' or ':' so that simple concatenation
  yields a well-formed IRI.
examples:
- value: https://example.org/accelerator-core/facility/01gq9xj92/
- value: tag:jlab.org,2026:uitf/
- value: urn:example:facility/01gq9xj92
- value: http://example.org/facility/01gq9xj92
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: id_namespace
owner: Facility
domain_of:
- Facility
range: uri
required: true
pattern: ^[A-Za-z][A-Za-z0-9+.\-]*:[^\s<>"{}|\\^`]*[/#:]$

```
</details>