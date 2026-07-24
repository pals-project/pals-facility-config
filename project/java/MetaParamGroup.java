package None;

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