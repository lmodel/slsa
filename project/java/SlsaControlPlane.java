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
  The component of a build platform that orchestrates each build and generates its provenance, outside the tenant's control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaControlPlane  {

  private SlsaBuildPlatform buildPlatform;


}