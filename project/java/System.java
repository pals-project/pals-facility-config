package None;

import java.util.List;
import lombok.*;






/**
  A physical, logical, or cyber-physical system involved in sensing, monitoring, control, or actuation. Broadly aligned to ssn:System.

**/
@Data
@EqualsAndHashCode(callSuper=false)
public class System extends NamedThing {

  private String systemType;
  private List<System> hasSubSystem;
  private List<SystemCapability> hasSystemCapability;

}