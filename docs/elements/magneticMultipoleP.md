

# Slot: magneticMultipoleP 


_A mixin for magnetic multipole parameters that are aligned with PALS MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the Particle Accelerator Language Standard (PALS)._





URI: [pals:magneticMultipoleP](https://pals-project.readthedocs.io/magneticMultipoleP)
Alias: magneticMultipoleP

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sextupole](Sextupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [CrabCavity](CrabCavity.md) | A cavity used for transverse beam manipulation, such as crabbing or deflectin... |  no  |
| [Cavity](Cavity.md) | A cavity used for beam acceleration or manipulation |  no  |
| [SuperConductingRFCavity](SuperConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is supe... |  no  |
| [NormalConductingRFCavity](NormalConductingRFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation, which is norm... |  no  |
| [Kicker](Kicker.md) | A magnet primarily used to steer the beam |  no  |
| [ACKicker](ACKicker.md) | An ACKicker element simulates a time-dependent kicker |  no  |
| [RFCavity](RFCavity.md) | A cavity used for RF acceleration or longitudinal manipulation |  no  |
| [Quadrupole](Quadrupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Multipole](Multipole.md) | A general magnet with a higher-order multipole field, such as a sextupole or ... |  no  |
| [HasMagneticMultipoleP](HasMagneticMultipoleP.md) |  |  no  |
| [Octupole](Octupole.md) | A magnet primarily used to focus or defocus the beam |  no  |
| [Bend](Bend.md) | Dipole magnet used to bend the beam |  no  |






## Properties

* Range: [MagneticMultipoleP](MagneticMultipoleP.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/accelerator-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pals:magneticMultipoleP |
| native | pals:magneticMultipoleP |




## LinkML Source

<details>
```yaml
name: magneticMultipoleP
description: A mixin for magnetic multipole parameters that are aligned with PALS
  MagneticMultipoleP (Magnetic Multipole Parameters) for interoperability with the
  Particle Accelerator Language Standard (PALS).
from_schema: https://w3id.org/accelerator-core
rank: 1000
alias: magneticMultipoleP
owner: HasMagneticMultipoleP
domain_of:
- HasMagneticMultipoleP
range: MagneticMultipoleP

```
</details>