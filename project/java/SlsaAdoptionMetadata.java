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
  The adoption challenges a deployment meets and the strategies it applies, from the study's taxonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaAdoptionMetadata  {

  private List<String> challenges;
  private List<String> strategies;


}