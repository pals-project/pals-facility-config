# Enum: DataTypeEnum 




_Data types for parameter values._



URI: [acc:enum/DataTypeEnum](https://example.org/accelerator-core/enum/DataTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| String | None | string data type |
| Integer | None | integer data type |
| Float | None | floating-point data type |
| Boolean | None | boolean data type |
| FloatArray | None | An array of floating-point values. |




## Slots

| Name | Description |
| ---  | --- |
| [native_data_type](../slots/native_data_type.md) | The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean. |
| [datatype](../slots/datatype.md) | Hint for the value's original type, so consumers can parse it back (e.g. float, integer, boolean) rather than treating everything as an opaque string. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/accelerator-core






## LinkML Source

<details>
```yaml
name: DataTypeEnum
description: Data types for parameter values.
from_schema: https://w3id.org/accelerator-core
rank: 1000
permissible_values:
  String:
    text: String
    description: string data type
    exact_mappings:
    - xsd:string
  Integer:
    text: Integer
    description: integer data type
    exact_mappings:
    - xsd:integer
  Float:
    text: Float
    description: floating-point data type
    exact_mappings:
    - xsd:float
  Boolean:
    text: Boolean
    description: boolean data type
    exact_mappings:
    - xsd:boolean
  FloatArray:
    text: FloatArray
    description: An array of floating-point values.
    exact_mappings:
    - acc:FloatArray

```
</details>