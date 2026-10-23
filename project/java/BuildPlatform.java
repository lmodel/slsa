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
  The infrastructure (software, hardware, people, and organizations) used to transform source code into package artifacts. Responsible for provenance generation and isolation between tenant builds. Often a hosted, multi-tenant build service.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildPlatform  {

  private String id;
  private String buildLevel;
  private Boolean isHosted;


}