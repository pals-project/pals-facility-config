package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An ACKicker element simulates a time-dependent kicker.  It is like a Kicker element except that the field varies in time.  This element requires a user supplied time-dependent expression.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ACKicker extends Kicker {


}