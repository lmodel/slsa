package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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