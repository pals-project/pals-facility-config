package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Contains authorship information for a representation of an accelerator facility and its operations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Author  {

  private String name;
  private Affiliation affiliation;
  private String email;
  private String orcid;

}