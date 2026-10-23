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
  The party that creates and distributes build images; the hosted build platform itself, or a third party in a bring-your-own-image setting.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaBuildImageProducer extends SlsaParty {



}