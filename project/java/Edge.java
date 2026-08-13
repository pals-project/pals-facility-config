package None;

import java.util.List;
import lombok.*;






/**
  Abstract base for subject-predicate-object associations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Edge  {

  private String id;
  private String subject;
  private String predicate;
  private String object;

}