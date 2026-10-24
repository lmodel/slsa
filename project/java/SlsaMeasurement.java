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
  The digest of one component or state of a build environment, to compare with its reference value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaMeasurement  {

  private InTotoDigestSet digest;
  private String measuredComponent;


}