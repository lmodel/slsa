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
  A party that inspects provenance or other attestations and decides whether an artifact is authentic.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaVerifier extends SlsaParty {

  private List<SlsaComponentVersion> componentVersions;
  private URI verifierId;


}