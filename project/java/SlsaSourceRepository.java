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
  A self-contained unit that holds a set of files, their revision history and metadata such as branches and tags.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaSourceRepository  {

  private URI repositoryUri;
  private SlsaSourceControlSystem hostedBy;


}