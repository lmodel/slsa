package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Root wrapper for any SLSA attestation payload. Acts as the entry point for schema validation and tools.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaDocument  {

  private BuildDefinition buildDefinition;
  private RunDetails runDetails;
  private Verifier verifier;
  private String verificationResult;
  private List<String> verifiedLevels;
  private AdoptionMetadata adoptionMetadata;

}