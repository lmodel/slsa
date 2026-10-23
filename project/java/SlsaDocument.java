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