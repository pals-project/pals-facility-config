package None;

import java.util.List;
import lombok.*;






/**
  Association between a PhysicalComponent and one of its Signals, e.g. QUAD1 component to QUAD1.STATUS signal.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class SignalBinding extends Edge {


}