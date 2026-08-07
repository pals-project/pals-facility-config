package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Dipole magnet used to bend the beam. 2 poles. The major difference between this element and other physical elements is that with a Bend  the curvilinear coordinate system is an arc with finite curvature  and for the other elements the curvilinear coordinate system is straight.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bend extends Multipole {

  private BendParamGroup bendP;

}