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
  A person or organization that takes part in a software supply chain, in one of the roles SLSA names.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class SlsaParty  {

  private String partyType;
  private String partyName;


}