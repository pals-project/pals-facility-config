package None;

import java.util.List;
import lombok.*;






/**
  Mixin for bend parameters, which can be used to describe the bending properties of an accelerator element. This mixin is aligned with PALS BendP for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BendParamGroup extends ParamGroup {

  private Float angleRef;
  private Float bendFieldRef;
  private Float bendFieldActual;
  private Float e1;
  private Float e2;
  private Float e1Rect;
  private Float e2Rect;
  private Float edge1Int;
  private Float edge2Int;
  private Float gRef;
  private Float gActual;
  private Float h1;
  private Float h2;
  private Float lChord;
  private Float lSagitta;
  private Float lRectangle;
  private String multipoleGeometry;
  private String refGeometry;
  private Float rhoRef;
  private Float tiltRef;

}