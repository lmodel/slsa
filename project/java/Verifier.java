package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
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