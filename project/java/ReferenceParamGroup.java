package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mixin for reference parameters that are aligned with PALS ReferenceP (Reference Parameters)  for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReferenceParamGroup  {

  private String speciesRef;
  private Float pcRef;
  private Float eTotRef;
  private Float timeRef;

}