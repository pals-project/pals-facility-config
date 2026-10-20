package None;

import java.util.List;
import lombok.*;






/**
  Abstract base class for all node entities in the accelerator core ontology. This differentiates nodes from edges (relationships) in the ontology. This class is not intended to be instantiated directly, but serves as a common ancestor for all other classes. Allows for the use of kind: as a discriminator for the type of node in the ontology.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Node  {

  private String id;
  private String kind;
  private List<String> alias;

}