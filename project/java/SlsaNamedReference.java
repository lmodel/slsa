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
  A user-friendly name for a revision in a repository, such as main or v1.2.3; reference_type says whether it is a branch or a tag.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaNamedReference  {

  private SlsaSourceRepository repository;
  private SlsaSourceRevision revision;
  private String referenceType;
  private String referenceName;
  private Boolean protected_;


}