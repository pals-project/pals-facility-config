

# Class: BeamlineElement 


_A single element in a beamline with optional physics parameter blocks._





URI: [https://w3id.org/narad_linkml/schema/narad/BeamlineElement](https://w3id.org/narad_linkml/schema/narad/BeamlineElement)





```mermaid
 classDiagram
    class BeamlineElement
    click BeamlineElement href "../BeamlineElement/"
      BeamlineElement : BendP
        
          
    
        
        
        BeamlineElement --> "0..1" BendParams : BendP
        click BendParams href "../BendParams/"
    

        
      BeamlineElement : facility_params
        
          
    
        
        
        BeamlineElement --> "0..1" FacilityParams : facility_params
        click FacilityParams href "../FacilityParams/"
    

        
      BeamlineElement : kind
        
          
    
        
        
        BeamlineElement --> "0..1" ElementKindEnum : kind
        click ElementKindEnum href "../ElementKindEnum/"
    

        
      BeamlineElement : length
        
      BeamlineElement : MagneticMultipoleP
        
          
    
        
        
        BeamlineElement --> "0..1" MagneticMultipoleParams : MagneticMultipoleP
        click MagneticMultipoleParams href "../MagneticMultipoleParams/"
    

        
      BeamlineElement : name
        
      BeamlineElement : narad
        
          
    
        
        
        BeamlineElement --> "0..1" ElementNaradRef : narad
        click ElementNaradRef href "../ElementNaradRef/"
    

        
      BeamlineElement : RFP
        
          
    
        
        
        BeamlineElement --> "0..1" RFParams : RFP
        click RFParams href "../RFParams/"
    

        
      BeamlineElement : SolenoidP
        
          
    
        
        
        BeamlineElement --> "0..1" SolenoidParams : SolenoidP
        click SolenoidParams href "../SolenoidParams/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Name/identifier of the entity | direct |
| [kind](kind.md) | 0..1 <br/> [ElementKindEnum](ElementKindEnum.md) | Generic kind/type label | direct |
| [length](length.md) | 0..1 <br/> [Float](Float.md) | Physical length of the element in meters | direct |
| [RFP](RFP.md) | 0..1 <br/> [RFParams](RFParams.md) | RF cavity physics parameters block | direct |
| [BendP](BendP.md) | 0..1 <br/> [BendParams](BendParams.md) | Dipole/bend physics parameters block | direct |
| [MagneticMultipoleP](MagneticMultipoleP.md) | 0..1 <br/> [MagneticMultipoleParams](MagneticMultipoleParams.md) | Magnetic multipole physics parameters block | direct |
| [SolenoidP](SolenoidP.md) | 0..1 <br/> [SolenoidParams](SolenoidParams.md) | Solenoid physics parameters block | direct |
| [narad](narad.md) | 0..1 <br/> [ElementNaradRef](ElementNaradRef.md) |  | direct |
| [facility_params](facility_params.md) | 0..1 <br/> [FacilityParams](FacilityParams.md) | Facility-specific element parameters block | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaradModel](NaradModel.md) | [elements](elements.md) | range | [BeamlineElement](BeamlineElement.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/BeamlineElement |
| native | https://w3id.org/narad_linkml/schema/narad/BeamlineElement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BeamlineElement
description: A single element in a beamline with optional physics parameter blocks.
from_schema: https://w3id.org/narad_linkml/schema/narad/
slots:
- name
- kind
- length
- RFP
- BendP
- MagneticMultipoleP
- SolenoidP
- narad
- facility_params
slot_usage:
  name:
    name: name
    required: true
  kind:
    name: kind
    range: ElementKindEnum
  narad:
    name: narad
    range: ElementNaradRef

```
</details>

### Induced

<details>
```yaml
name: BeamlineElement
description: A single element in a beamline with optional physics parameter blocks.
from_schema: https://w3id.org/narad_linkml/schema/narad/
slot_usage:
  name:
    name: name
    required: true
  kind:
    name: kind
    range: ElementKindEnum
  narad:
    name: narad
    range: ElementNaradRef
attributes:
  name:
    name: name
    description: Name/identifier of the entity.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    identifier: true
    alias: name
    owner: BeamlineElement
    domain_of:
    - Facility
    - SignalBinding
    - DeviceTypeSignalSet
    - Signal
    - Capability
    - CapabilityProfile
    - ControlProfileFamily
    - BeamlineElement
    - PVBinding
    range: string
    required: true
  kind:
    name: kind
    description: 'Generic kind/type label. Used for Beamline entries (e.g. BeamLine).
      For ControlProfileFamily device domain use device_domain: DeviceDomainEnum.
      For CapabilityProfile device type use device_type: ElementKindEnum.'
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    aliases:
    - type
    - profile_type
    rank: 1000
    alias: kind
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    - Beamline
    range: ElementKindEnum
  length:
    name: length
    description: Physical length of the element in meters.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: length
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    range: float
  RFP:
    name: RFP
    description: RF cavity physics parameters block.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: RFP
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    range: RFParams
    inlined: true
  BendP:
    name: BendP
    description: Dipole/bend physics parameters block.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: BendP
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    range: BendParams
    inlined: true
  MagneticMultipoleP:
    name: MagneticMultipoleP
    description: Magnetic multipole physics parameters block.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: MagneticMultipoleP
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    range: MagneticMultipoleParams
    inlined: true
  SolenoidP:
    name: SolenoidP
    description: Solenoid physics parameters block.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: SolenoidP
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    range: SolenoidParams
    inlined: true
  narad:
    name: narad
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: narad
    owner: BeamlineElement
    domain_of:
    - NaradModel
    - BeamlineElement
    range: ElementNaradRef
    inlined: true
  facility_params:
    name: facility_params
    description: Facility-specific element parameters block.
    from_schema: https://w3id.org/narad_linkml/schema/narad/
    rank: 1000
    alias: facility_params
    owner: BeamlineElement
    domain_of:
    - BeamlineElement
    range: FacilityParams
    inlined: true

```
</details>