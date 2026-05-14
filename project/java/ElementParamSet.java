package None;

import java.util.List;
import lombok.*;






/**
  Named physics-parameter block for a beamline element. The name identifies the block type (e.g. RFP, BendP, MagneticMultipoleP, SolenoidP).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ElementParamSet  {

  private Float frequency;
  private Float voltage;
  private Float phase;
  private Float angleRef;
  private Float e1;
  private Float e2;
  private Float kn1;
  private Float ksol;
  private FacilityParamSet facilityParamSet;

}