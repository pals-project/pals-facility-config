package None;

import java.util.List;
import lombok.*;






/**
  Mixin for solenoid-specific parameters.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SolenoidP  {

  private Float ksol;
  private Float bsol;

}