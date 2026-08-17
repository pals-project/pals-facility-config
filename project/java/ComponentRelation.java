package None;

import java.util.List;
import lombok.*;






/**
  Association between two Components (Physical or Virtual), with supporting contextual/qualifying information about how and where the relationship holds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ComponentRelation extends Edge {

  private String context;
  private String componentDirection;
  private String referenceFrame;

}