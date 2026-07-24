package None;

import java.util.List;
import lombok.*;






/**
  Mixin class for floor plan parameters that are aligned with PALS FloorP (Floor Plan Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FloorP  {

  private Float x;
  private Float y;
  private Float z;
  private Float theta;
  private Float phi;
  private Float psi;

}