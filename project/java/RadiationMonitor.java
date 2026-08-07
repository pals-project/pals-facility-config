package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A diagnostic device used to monitor radiation dose or dose rate.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RadiationMonitor extends DiagnosticDevice {

  private BodyShiftParamGroup bodyShiftP;

}