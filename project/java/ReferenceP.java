package None;

import java.util.List;
import lombok.*;






/**
  Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReferenceP  {

  private String speciesRef;
  private Float pcRef;
  private Float eTotRef;
  private Float timeRef;

}