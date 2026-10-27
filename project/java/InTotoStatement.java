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
  The statement layer of an in-toto attestation: the subjects it is about, the type of its predicate and the predicate itself.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoStatement  {

  private URI statementType;
  private List<InTotoStatementSubject> subject;
  private URI predicateType;
  private SlsaPredicate predicate;
  private URI attestationStorageUri;
  private URI signingTool;
  private URI transparencyLogEntry;


}