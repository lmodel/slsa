package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A specific, logically immutable snapshot of a source repository's tracked files. Uniquely identified by a revision identifier such as a cryptographic hash (e.g., git commit SHA) or a path-qualified sequential number (e.g., SVN).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SourceRevision  {

  private String revisionId;
  private SourceRepository repository;
  private String author;
  private String timestamp;
  private List<String> parentRevisions;
  private String reviewType;

}