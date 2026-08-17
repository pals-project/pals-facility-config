package None;

import java.util.List;
import lombok.*;






/**
  Abstract base for inlined PALS parameter-group objects, giving each an identifier so it resolves to a stable node/IRI rather than a blank node when exported to RDF.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ParamGroup  {

  private String id;

}