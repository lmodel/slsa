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
  The base of every predicate this schema models; predicate_kind names the concrete kind.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class SlsaPredicate  {

  private String predicateKind;


}