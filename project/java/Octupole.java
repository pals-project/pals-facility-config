package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A magnet primarily used to focus or defocus the beam. 8 poles.
Only one of the electric or magnetic multipole components should be present, not both.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Octupole extends Multipole {


}