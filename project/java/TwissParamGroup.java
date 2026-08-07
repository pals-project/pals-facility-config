package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mixin for Twiss parameters, which can be used to describe the beam optics of an accelerator element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TwissParamGroup  {

  private Float alphaA;
  private Float alphaB;
  private Float betaA;
  private Float betaB;
  private Float etaX;
  private Float etaY;
  private Float etapX;
  private Float etapY;
  private Float phiA;
  private Float phiB;

}