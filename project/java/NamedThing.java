package None;

import java.util.List;
import lombok.*;






/**
  Abstract base class providing identity and human-readable metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedThing  {

  private String name;
  private String description;

}