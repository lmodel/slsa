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
  An in-toto statement with the fields this schema adds: where the signed attestation is stored, the tool that signed it and the transparency log entry that records the signature.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaStatement extends InTotoStatement {

  private URI attestationStorageUri;
  private URI signingTool;
  private URI transparencyLogEntry;


}