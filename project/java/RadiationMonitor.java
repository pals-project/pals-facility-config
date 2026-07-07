package None;

import java.util.List;
import lombok.*;






/**
  A diagnostic device used to monitor radiation dose or dose rate.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RadiationMonitor extends DiagnosticDevice {

  private Float xOffset;
  private Float yOffset;
  private Float zOffset;
  private Float xRot;
  private Float yRot;
  private Float zRot;

}