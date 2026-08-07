package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Abstract base for subject-predicate-object associations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Relationship  {

  private String id;
  private String subject;
  private String predicate;
  private String object;

}