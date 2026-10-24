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
  One vendor-specific annotation on a resource descriptor, with a key and one or more values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoAnnotation  {

  private String annotationKey;
  private List<String> annotationValues;


}