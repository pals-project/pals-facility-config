# Type: Iso8601Datetime 




_Strict ISO 8601 date-time string allowing optional milliseconds and timezones,  e.g., 2024-06-05T14:30:00Z+05:00 for June 5th, 2024 at 14:30:00 (2:30 PM) with UTC timezone offset +05:00 (America/New_York)._



URI: [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime)

## Type Properties

| Property | Value |
| --- | --- |
| Type Of | [String](../types/String.md) |
| Base | `str` |
| Type URI | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
## Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})?$` |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/pals-config




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | xsd:dateTime |
| native | pals_config:iso8601_datetime |


