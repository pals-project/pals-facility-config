package None;

import java.util.List;
import lombok.*;






/**
  A single order's electric (or magnetic) multipole component. Only the fields supporting Electric Multipoles  OR the fields for Magnetic Multipoles should be present, not both. Not a mixin, but a class used in the ElectricMultipoleP and MagneticMultipoleP mixins to represent individual multipole components.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MultipoleParameterGroup  {

  private int order;
  private Float tilt;
  private Float en;
  private Float es;
  private Float enL;
  private Float esL;
  private Float bn;
  private Float bs;
  private Float kn;
  private Float ks;

}