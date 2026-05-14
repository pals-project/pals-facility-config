package None;

import java.util.List;
import lombok.*;






/**
  A NARAD signal that can be commanded, set, or acted upon. Examples: current_setpoint, strength_setpoint, kick_setpoint, field_setpoint, current_min, current_max, gradient_setpoint. Aligned to sosa:ActuatableProperty.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ActuatableSignal extends Signal {


}