package None;

import java.util.List;
import lombok.*;






/**
  A single generic key/value metadata entry, used as a GraphQL-compatible replacement for an open-ended (range: Any) field. A list of these represents an arbitrary, extensible bag of program-specific metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AdditionalMetadata  {

  private String key;
  private String value;
  private String datatype;

}