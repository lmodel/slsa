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
  A party that provides software or services to the other roles, such as a package registry's or a build platform's maintainers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaInfrastructureProvider extends SlsaParty {



}