package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mixin for solenoid-specific parameters.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SolenoidParamGroup  {

  private Float ksol;
  private Float bsol;

}