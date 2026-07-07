package None;

import java.util.List;
import lombok.*;






/**
  Semantic meaning of a control-system signal associated with a component.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Signal  {

  private String id;
  private String type;
  private String signalRole;
  private String sourceSystem;
  private String nativeDescription;
  private String canonicalSignalType;
  private String quantityKind;
  private String nativeDataType;
  private String nativeUnit;
  private String accessProtocol;
  private String archiveIdentifier;
  private String description;
  private String label;
  private String alias;
  private List<MetadataEntry> additionalMetadata;

}