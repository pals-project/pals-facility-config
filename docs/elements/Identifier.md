
# Class: Identifier

A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.

URI: [pals:Identifier](https://pals-project.readthedocs.io/Identifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Facility]++-%20identifiers%200..*>[Identifier&#124;identifier_type:IdentifierTypeEnum%20%3F;identifier_value:string%20%3F],[Affiliation]++-%20identifiers%200..*>[Identifier],[Facility],[Affiliation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Facility]++-%20identifiers%200..*>[Identifier&#124;identifier_type:IdentifierTypeEnum%20%3F;identifier_value:string%20%3F],[Affiliation]++-%20identifiers%200..*>[Identifier],[Facility],[Affiliation])

## Referenced by Class

 *  **None** *[identifiers](identifiers.md)*  <sub>0..\*</sub>  **[Identifier](Identifier.md)**

## Attributes


### Own

 * [➞identifier_type](identifier__identifier_type.md)  <sub>0..1</sub>
     * Description: The type of identifier, such as DOI | PURL | ROR | LOCAL | URL | ARK.
     * Range: [IdentifierTypeEnum](IdentifierTypeEnum.md)
 * [➞identifier_value](identifier__identifier_value.md)  <sub>0..1</sub>
     * Description: The value of the identifier.
     * Range: [String](types/String.md)
