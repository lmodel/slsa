package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The middle layer of an in-toto software attestation (Statement v1). Binds an authenticated predicate to one or more subject artifacts, allowing predicate-agnostic processing and storage.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Statement  {

  private String type;
  private List<ResourceDescriptor> subject;
  private String predicateType;
  private String predicate;
  private String attestationStorageUri;
  private String signingTool;
  private String sigstoreLogEntry;

}