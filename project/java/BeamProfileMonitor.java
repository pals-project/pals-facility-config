package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A diagnostic device used to measure transverse beam profile.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BeamProfileMonitor extends DiagnosticDevice {

  private ReferenceParamGroup referenceP;
  private BodyShiftParamGroup bodyShiftP;
  private TwissParamGroup twissP;

}