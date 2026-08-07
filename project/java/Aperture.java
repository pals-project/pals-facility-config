package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A diagnostic or limiting aperture element used to constrain or characterize beam passage.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Aperture extends DiagnosticDevice {

  private ReferenceParamGroup referenceP;
  private TwissParamGroup twissP;

}