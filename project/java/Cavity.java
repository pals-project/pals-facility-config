package None;

import java.util.List;
import lombok.*;






/**
  A cavity used for beam acceleration or manipulation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Cavity extends PhysicalComponent {

  private ReferenceParamGroup referenceP;
  private ElectricMultipoleParamGroup electricMultipoleP;
  private MagneticMultipoleParamGroup magneticMultipoleP;
  private BodyShiftParamGroup bodyShiftP;
  private TwissParamGroup twissP;

}