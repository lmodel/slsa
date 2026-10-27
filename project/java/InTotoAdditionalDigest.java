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
  One digest under an algorithm that InTotoDigestSet does not name, such as an SCS's own revision type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoAdditionalDigest  {

  private String algorithm;
  private String value;


}