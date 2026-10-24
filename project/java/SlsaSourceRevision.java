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
  A logically immutable snapshot of a repository's tracked files, with its version-control metadata: author, time and parent revisions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SlsaSourceRevision  {

  private SlsaSourceRepository repository;
  private String revisionId;
  private String authoredBy;
  private ZonedDateTime authoredAt;
  private List<SlsaSourceRevision> parentRevisions;
  private String sourceLevel;
  private String reviewType;


}