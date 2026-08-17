package None;

import java.util.List;
import lombok.*;






/**
  A general class for accelerator components, which can be specialized into more specific types like AcceleratorDevice, Magnet, etc.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Component extends Node {

  private List<String> nativeTypes;
  private MetaParamGroup metaP;

}