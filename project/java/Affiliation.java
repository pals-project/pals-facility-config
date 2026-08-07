package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Contains affiliation information for an author or component, such as a ROR.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Affiliation  {

  private String id;
  private String name;
  private List<Identifier> identifiers;

}