package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mixin for RF parameters, which can be used to describe the RF properties of an accelerator element. This mixin is aligned with PALS RFP for interoperability with the Particle Accelerator Language Standard (PALS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RFParamGroup  {

  private Float frequency;
  private Integer harmon;
  private Float voltage;
  private Float phase;
  private Float multipassPhase;
  private String cavityType;
  private Integer numCells;
  private String zeroPhase;
  private Float lActive;
  private Float dERef;

}