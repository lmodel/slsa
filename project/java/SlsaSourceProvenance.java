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
  Evidence from an SCS of how a revision came to exist and which technical controls were enforced when it did.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaSourceProvenance extends SlsaPredicate {

  private SlsaSourceRevision revision;
  private List<String> controlsEnforced;


}