package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MetaParamGroup  {

  private String description;
  private String alias;
  private String label;
  private List<AdditionalMetadata> additionalMetadata;

}