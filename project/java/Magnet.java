package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An accelerator device that produces a magnetic field for beam control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Magnet extends PhysicalComponent {

  private ReferenceParamGroup referenceP;
  private BodyShiftParamGroup bodyShiftP;
  private TwissParamGroup twissP;

}