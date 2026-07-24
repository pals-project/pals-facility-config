package None;

import java.util.List;
import lombok.*;






/**
  Mixin class for floor plan shift parameters that are aligned with PALS BodyShiftP (Floor Plan Shift Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BodyShiftParamGroup  {

  private Float xOffset;
  private Float yOffset;
  private Float zOffset;
  private Float xRot;
  private Float yRot;
  private Float zRot;

}