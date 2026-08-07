package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A unique, and ideally persistent, identifier for a facility, such as a DOI or ROR.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Identifier  {

  private String identifierType;
  private String identifierValue;

}