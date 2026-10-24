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
  The number of an artifact's transitive dependencies verified at one level, each counted once per track at its highest level.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaDependencyLevelCount  {

  private String verifiedLevel;
  private int dependencyCount;


}