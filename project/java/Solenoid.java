package None;

import java.util.List;
import lombok.*;






/**
  A magnet with a primarily longitudinal magnetic field used for focusing.
A solenoid is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis. 
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Solenoid extends Magnet {

  private SolenoidParamGroup solenoidP;

}