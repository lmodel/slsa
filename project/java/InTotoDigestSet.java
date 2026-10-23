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
  A set of digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoDigestSet  {

  private String sha256;
  private String sha512;
  private String gitCommit;
  private String gitTree;
  private String dirHash;


}