package None;

import java.util.List;
import lombok.*;






/**
  Mixin for magnetic multipole parameters,  which can be used to describe the magnetic field components of an accelerator element. This mixin is aligned with PALS MagneticMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS). Example with three multipole components (N=0,1,2): ```yaml mag_components: - order: 7
  tilt: 0.7
- order: 3
  Bn: 27.3
- order: 2
  BnL: 3.47e1
- order: 1
  Kn: 0.85     # normalized form, e.g. a quadrupole's k1-like strength
```
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MagneticMultipoleParamGroup extends ParamGroup {

  private List<MultipoleParameterGroup> magComponents;

}