package None;

import java.util.List;
import lombok.*;






/**
  Capability-layer container for control profile families.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapabilityLayer  {

  private List<Capability> capabilities;

}