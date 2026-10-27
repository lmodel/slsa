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
  A set of one or more digests over one artifact, keyed by algorithm, from which a consumer picks the algorithm it trusts.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InTotoDigestSet  {

  private String sha256;
  private String sha224;
  private String sha384;
  private String sha512;
  private String sha512224;
  private String sha512256;
  private String sha3224;
  private String sha3256;
  private String sha3384;
  private String sha3512;
  private String shake128;
  private String shake256;
  private String blake2b;
  private String blake2s;
  private String ripemd160;
  private String sm3;
  private String gost;
  private String sha1;
  private String md5;
  private String dirHash;
  private String gitCommit;
  private String gitTree;
  private String gitBlob;
  private String gitTag;
  private List<InTotoAdditionalDigest> additionalDigests;


}