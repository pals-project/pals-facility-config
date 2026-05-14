package None;

import java.util.List;
import lombok.*;






/**
  Signal-layer container for facility-specific signal bindings.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SignalLayer  {

  private List<FacilitySystem> facilities;

}