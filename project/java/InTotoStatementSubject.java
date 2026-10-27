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
  One artifact an in-toto statement is about: a resource descriptor that carries a digest.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoStatementSubject extends InTotoResourceDescriptor {



}