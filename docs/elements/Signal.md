
# Class: Signal

Semantic meaning of a control-system signal associated with a component.

URI: [narad:Signal](https://example.org/narad/Signal)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Component]<type%201..1-%20[Signal&#124;id:string;signal_role:SignalRoleEnum;source_system:SourceSystemEnum;native_description:string%20%3F;canonical_signal_type:CanonicalSignalTypeEnum;quantity_kind:QuantityKindEnum;native_data_type:DataTypeEnum;native_unit:UnitEnum;access_protocol:string%20%3F;archive_identifier:string%20%3F;description:string%20%3F;label:string%20%3F;alias:string%20%3F],[SignalBinding]-%20object%201..1>[Signal],[NARAD]++-%20signals%200..*>[Signal],[Signal]uses%20-.->[MetaP],[NARAD],[MetadataEntry],[MetaP],[Component])](https://yuml.me/diagram/nofunky;dir:TB/class/[SignalBinding],[Component]<type%201..1-%20[Signal&#124;id:string;signal_role:SignalRoleEnum;source_system:SourceSystemEnum;native_description:string%20%3F;canonical_signal_type:CanonicalSignalTypeEnum;quantity_kind:QuantityKindEnum;native_data_type:DataTypeEnum;native_unit:UnitEnum;access_protocol:string%20%3F;archive_identifier:string%20%3F;description:string%20%3F;label:string%20%3F;alias:string%20%3F],[SignalBinding]-%20object%201..1>[Signal],[NARAD]++-%20signals%200..*>[Signal],[Signal]uses%20-.->[MetaP],[NARAD],[MetadataEntry],[MetaP],[Component])

## Uses Mixin

 *  mixin: [MetaP](MetaP.md) - Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).

## Referenced by Class

 *  **[SignalBinding](SignalBinding.md)** *[SignalBinding➞object](SignalBinding_object.md)*  <sub>1..1</sub>  **[Signal](Signal.md)**
 *  **None** *[➞signals](nARAD__signals.md)*  <sub>0..\*</sub>  **[Signal](Signal.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the instance.
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: The LinkML class name of this instance.
     * Range: [Component](Component.md)
 * [➞signal_role](signal__signal_role.md)  <sub>1..1</sub>
     * Description: The role of the signal in the control system, such as setpoint, readback, status, command, or limit.
     * Range: [SignalRoleEnum](SignalRoleEnum.md)
 * [➞source_system](signal__source_system.md)  <sub>1..1</sub>
     * Description: The source system from which the signal originates, such as EPICS, PALS-Ext, MYA, an element database, a channel database, or a simulation service.
     * Range: [SourceSystemEnum](SourceSystemEnum.md)
 * [➞native_description](signal__native_description.md)  <sub>0..1</sub>
     * Description: A human-readable description of the signal in the source system.
     * Range: [String](types/String.md)
 * [➞canonical_signal_type](signal__canonical_signal_type.md)  <sub>1..1</sub>
     * Description: The canonical semantic meaning of the signal.
     * Range: [CanonicalSignalTypeEnum](CanonicalSignalTypeEnum.md)
 * [➞quantity_kind](signal__quantity_kind.md)  <sub>1..1</sub>
     * Description: The physical quantity kind of the signal.
     * Range: [QuantityKindEnum](QuantityKindEnum.md)
 * [➞native_data_type](signal__native_data_type.md)  <sub>1..1</sub>
     * Description: The native data type of the signal in the source system,  such as String, Integer, Float, or Boolean.
     * Range: [DataTypeEnum](DataTypeEnum.md)
 * [➞native_unit](signal__native_unit.md)  <sub>1..1</sub>
     * Description: The native unit of the signal in the source system.
     * Range: [UnitEnum](UnitEnum.md)
 * [➞access_protocol](signal__access_protocol.md)  <sub>0..1</sub>
     * Description: The protocol used to access the signal in the source system,  such as EPICS Channel Access, PALS-Ext, MYA, or a simulation service.
     * Range: [String](types/String.md)
 * [➞archive_identifier](signal__archive_identifier.md)  <sub>0..1</sub>
     * Description: The identifier used to reference the signal in an archival system.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞description](metaP__description.md)  <sub>0..1</sub>
     * Description: Human-readable description.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞label](metaP__label.md)  <sub>0..1</sub>
     * Description: A label string.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞alias](metaP__alias.md)  <sub>0..1</sub>
     * Description: An alternative name or identifier for the instance.
     * Range: [String](types/String.md)

### Mixed in from MetaP:

 * [➞additional_metadata](metaP__additional_metadata.md)  <sub>0..\*</sub>
     * Description: Additional metadata or annotations for the instance.
     * Range: [MetadataEntry](MetadataEntry.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Broad Mappings:** | | sosa:Sensor |
|  | | sosa:Actuator |
