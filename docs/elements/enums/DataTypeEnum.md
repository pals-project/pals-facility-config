# Enum: DataTypeEnum 




_Data types for parameter values._



URI: [pals:enum/DataTypeEnum](https://pals-project.readthedocs.io/enum/DataTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| String | xsd:string | string data type |
| Integer | xsd:integer | integer data type |
| Float | xsd:float | floating-point data type |
| Boolean | xsd:boolean | boolean data type |




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
    meaning: xsd:string
  Integer:
    text: Integer
    description: integer data type
    meaning: xsd:integer
  Float:
    text: Float
    description: floating-point data type
    meaning: xsd:float
  Boolean:
    text: Boolean
    description: boolean data type
    meaning: xsd:boolean

```
</details>