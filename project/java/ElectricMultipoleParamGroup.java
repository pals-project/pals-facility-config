package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mixin for electric multipole parameters, 
which can be used to describe the electric field components of an accelerator element.
This mixin is aligned with PALS ElectricMultipoleP for interoperability with the Particle Accelerator Language Standard (PALS).
Example with three multipole components (N=0,1,2): ```yaml elec_components: - order: 7
  tilt: 0.7
- order: 3
  En: 27.3
- order: 2
  EnL: 3.47e1
```
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElectricMultipoleParamGroup  {

  private List<MultipoleParameterGroup> elecComponents;

}