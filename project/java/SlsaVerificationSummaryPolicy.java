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
  The policy a verification summary applied: a resource descriptor that names the policy by URI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaVerificationSummaryPolicy extends InTotoResourceDescriptor {



}