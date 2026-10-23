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
  The platform or services that host a source repository and enforce its organization's policies on authentication, authorization and change management.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaSourceControlSystem  {

  private URI scsUri;


}