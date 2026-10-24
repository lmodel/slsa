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
  The predicate that says how a build platform produced a set of artifacts, so that consumers can verify the build met their expectations and others can rebuild it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildProvenance extends SlsaPredicate {

  private SlsaBuildDefinition buildDefinition;
  private SlsaRunDetails runDetails;


}