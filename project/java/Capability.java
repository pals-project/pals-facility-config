package None;

import java.util.List;
import lombok.*;






/**
  A reusable device-type control profile that extends a generic shared capability with type-specific signals (e.g. QuadrupoleCurrentControlProfile).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Capability extends NamedThing {

  private String deviceType;
  private Capability subclassOf;
  private List<Signal> hasSignal;
  private ControlSystem isPropertyOf;

}