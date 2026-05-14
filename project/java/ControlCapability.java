package None;

import java.util.List;
import lombok.*;






/**
  A reusable device-type control profile that extends a generic shared capability with type-specific signals (e.g. QuadrupoleCurrentControlProfile).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlCapability extends NamedThing {

  private String deviceType;
  private System subclassOf;
  private List<Signal> signals;

}