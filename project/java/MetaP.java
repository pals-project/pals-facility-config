package None;

import java.util.List;
import lombok.*;






/**
  Mixin class for metadata parameters that are aligned with PALS MetaP (Metadata Parameters) for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MetaP  {

  private String description;
  private String label;
  private String alias;
  private List<MetadataEntry> additionalMetadata;

}