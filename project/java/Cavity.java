package None;

import java.util.List;
import lombok.*;






/**
  A cavity used for beam acceleration or manipulation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Cavity extends PhysicalComponent {

  private String speciesRef;
  private Float pcRef;
  private Float eTotRef;
  private Float timeRef;
  private List<MultipoleComponent> components;
  private Float xOffset;
  private Float yOffset;
  private Float zOffset;
  private Float xRot;
  private Float yRot;
  private Float zRot;
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