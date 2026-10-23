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
  The entity that performed verification of an artifact and issued a Verification Summary Attestation. Consumers MUST accept only specific (signer, verifier) pairs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Verifier  {

  private String id;
  private String version;


}