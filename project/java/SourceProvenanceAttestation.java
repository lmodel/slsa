package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An attestation describing how a source revision came to exist: where it was hosted, when it was generated, what process was used, who the contributors were, and which technical controls were enforced by the Source Control System.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SourceProvenanceAttestation extends Statement {

  private SourceRevision revision;
  private String sourceLevel;
  private List<String> controlsEnforced;

}