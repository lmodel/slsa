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
  A party that creates software and provides it to others, choosing a build platform and distributing provenance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaProducer extends SlsaParty {

  private SlsaBuildPlatform buildPlatform;


}