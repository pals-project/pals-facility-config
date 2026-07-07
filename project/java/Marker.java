package None;

import java.util.List;
import lombok.*;






/**
  A virtual component used as a reference point or marker in the beamline structure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Marker extends BookkeepingComponent {

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