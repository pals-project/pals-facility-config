# Enum: DataTypeEnum 




_Allowed data types for signal values._



URI: [narad:DataTypeEnum](https://w3id.org/narad_linkml/schema/narad/DataTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| int | ncit:C47840 | Integer |
| float | ncit:C48150 | Single-precision floating-point |
| double | ncit:C48870 | Double-precision floating-point |
| string | ncit:C45253 | Text string |
| boolean | ncit:C45254 | True/false value |
| coded_value | ncit:C95637 | A code referenced from an external coding system |




## Slots

| Name | Description |
| ---  | --- |
| [data_type](data_type.md) | The data type of the signal's value |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/system






## LinkML Source

<details>
```yaml
name: DataTypeEnum
description: Allowed data types for signal values.
from_schema: https://w3id.org/narad_linkml/schema/narad/system
rank: 1000
permissible_values:
  int:
    text: int
    description: Integer.
    meaning: ncit:C47840
  float:
    text: float
    description: Single-precision floating-point.
    meaning: ncit:C48150
  double:
    text: double
    description: Double-precision floating-point.
    meaning: ncit:C48870
  string:
    text: string
    description: Text string.
    meaning: ncit:C45253
  boolean:
    text: boolean
    description: True/false value.
    meaning: ncit:C45254
  coded_value:
    text: coded_value
    description: A code referenced from an external coding system.
    meaning: ncit:C95637

```
</details>