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
  A set of cryptographic digests for an artifact, keyed by algorithm name (e.g., "sha256", "gitCommit"). Provides enough information for consumers to verify artifact integrity using their preferred algorithm.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DigestSet  {

  private String sha256;
  private String sha512;
  private String gitCommit;


}