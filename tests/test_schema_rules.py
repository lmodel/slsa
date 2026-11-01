"""Checks that rules the schema states in more than one place agree."""

import itertools
import re
from pathlib import Path

import yaml
from linkml_runtime.utils.schemaview import SchemaView

SCHEMA = Path(__file__).parent.parent / "src" / "slsa" / "schema" / "slsa.yaml"

# The digest set's fields whose key in the attestation's JSON is camelCase.
JSON_KEYS = {
    "dir_hash": "dirHash",
    "git_commit": "gitCommit",
    "git_tree": "gitTree",
    "git_blob": "gitBlob",
    "git_tag": "gitTag",
}


def test_digest_set_rules_name_every_algorithm():
    """The at-least-one rule and the reserved names cover every named algorithm."""
    sv = SchemaView(str(SCHEMA))
    digest_set = sv.get_class("InTotoDigestSet")
    algorithms = set(digest_set.attributes) - {"additional_digests"}
    in_any_of = {name for rule in digest_set.any_of for name in rule.slot_conditions}
    assert in_any_of == algorithms | {"additional_digests"}

    algorithm = sv.get_class("InTotoAdditionalDigest").attributes["algorithm"]
    reserved = set(algorithm.none_of[0].equals_string_in)
    assert reserved == {JSON_KEYS.get(name, name) for name in algorithms} | algorithms


def test_result_pattern_admits_slsa_results_and_safe_values_of_an_issuer():
    """The result type takes each SlsaResult value and only safe values of its own."""
    sv = SchemaView(str(SCHEMA))
    pattern = re.compile(sv.get_type("slsa_result_value").pattern)
    slsa_values = set(sv.get_enum("SlsaResult").permissible_values)
    for cls, slot in (
        ("SlsaVerificationSummary", "verified_levels"),
        ("SlsaDependencyLevelCount", "verified_level"),
    ):
        assert sv.induced_slot(slot, cls).pattern == pattern.pattern

    def admitted(value):
        if value in slsa_values:
            return True
        printable = value != "" and all("!" <= c <= "~" for c in value)
        return printable and not value.upper().startswith("SLSA_")

    samples = slsa_values | {
        "",
        "acme-fips",
        "ORG_SOURCE_STATIC_ANALYSIS",
        "slsa_build_level_3",
        " SLSA_BUILD_LEVEL_3",
        "ЅLSA_BUILD_LEVEL_3",
        "SLSA_BUILD_LEVEL_",
        "SLSA_BUILD_LEVEL_4",
        "SLSA_SOURCE_LEVEL_5",
        "SLSA_BUILD_REPRODUCEDX",
    }
    # Every string of up to six characters over letters that spell SLSA_ in
    # either case, another letter and a space.
    samples |= {
        "".join(chars)
        for length in range(1, 7)
        for chars in itertools.product("SLAsla_X ", repeat=length)
    }
    for value in samples:
        assert bool(pattern.search(value)) == admitted(value), repr(value)


SCHEMA_DIR = SCHEMA.parent
SPEC = SCHEMA_DIR / "spec"
MODULES = sorted(SCHEMA_DIR.glob("slsa*.yaml"))
MAPPING_KEYS = (
    "exact_mappings",
    "close_mappings",
    "narrow_mappings",
    "broad_mappings",
    "related_mappings",
)

# The terms of other vocabularies that the mappings name, each checked in the
# file that defines it: SPDX 3.0.1's spdx-model.ttl (as lmodel/spdx vendors
# it), DOAP's schema/doap.rdf at d164b82 and W3C's prov-o.ttl. Add a term here
# only after finding it there.
EXTERNAL_TERMS = {
    "https://spdx.org/rdf/3.0.1/terms/Build/Build",
    "https://spdx.org/rdf/3.0.1/terms/Build/buildType",
    "https://spdx.org/rdf/3.0.1/terms/Build/buildId",
    "https://spdx.org/rdf/3.0.1/terms/Build/buildStartTime",
    "https://spdx.org/rdf/3.0.1/terms/Build/buildEndTime",
    "https://spdx.org/rdf/3.0.1/terms/Build/parameter",
    "https://spdx.org/rdf/3.0.1/terms/Core/Agent",
    "https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry",
    "https://spdx.org/rdf/3.0.1/terms/Core/key",
    "https://spdx.org/rdf/3.0.1/terms/Core/value",
    "https://spdx.org/rdf/3.0.1/terms/Software/Package",
    "http://usefulinc.com/ns/doap#Repository",
    "http://usefulinc.com/ns/doap#location",
    "http://usefulinc.com/ns/doap#GitBranch",
    "http://www.w3.org/ns/prov#Agent",
}

# The vendored specification file that names each predicate type.
PREDICATE_TYPE_PAGES = {
    "https://slsa.dev/provenance/v1": "build-provenance.md",
    "https://slsa.dev/verification_summary/v1": "verification_summary.md",
}


def _elements(doc):
    """Yield each class, slot, attribute and enum of a module with its name."""
    for kind in ("classes", "slots", "enums", "types"):
        for name, element in (doc.get(kind) or {}).items():
            element = element or {}
            yield name, element
            for attr, value in (element.get("attributes") or {}).items():
                yield f"{name}.{attr}", value or {}


def _mappings():
    """Yield the module, element and expanded IRI of every mapping."""
    for module in MODULES:
        doc = yaml.safe_load(module.read_text())
        prefixes = doc.get("prefixes") or {}
        for name, element in _elements(doc):
            for key in MAPPING_KEYS:
                values = element.get(key) or []
                for curie in [values] if isinstance(values, str) else values:
                    prefix, _, local = curie.partition(":")
                    assert prefix in prefixes, (module.name, name, curie)
                    yield module.name, name, prefixes[prefix] + local


def test_mappings_use_a_bound_prefix_and_a_known_term():
    """Every mapping expands through its own module's prefixes to a term that
    exists: a predicate type SLSA's pages name, or a checked external term."""
    seen = set()
    for module, name, iri in _mappings():
        seen.add(iri)
        if iri in PREDICATE_TYPE_PAGES:
            page = (SPEC / PREDICATE_TYPE_PAGES[iri]).read_text()
            assert f'"predicateType": "{iri}"' in page, (module, name, iri)
        else:
            assert iri in EXTERNAL_TERMS, (module, name, iri)
    assert EXTERNAL_TERMS | set(PREDICATE_TYPE_PAGES) == seen


def _aliases(class_names):
    sv = SchemaView(str(SCHEMA))
    for cls in class_names:
        for slot in sv.class_induced_slots(cls):
            for alias in slot.aliases:
                yield cls, slot.name, alias


def test_provenance_aliases_are_keys_of_the_provenance_format():
    """Each alias on the provenance's parts is a key of SLSA's provenance.cue."""
    keys = set(
        re.findall(r'"(\w+)":', (SPEC / "schema" / "provenance.cue").read_text())
    )
    classes = (
        "SlsaBuildProvenance",
        "SlsaBuildDefinition",
        "SlsaRunDetails",
        "SlsaBuildPlatform",
        "SlsaBuildMetadata",
    )
    aliases = list(_aliases(classes))
    assert aliases
    for cls, slot, alias in aliases:
        assert alias in keys, (cls, slot, alias)


def test_summary_aliases_are_keys_of_the_summary_format():
    """Each alias on the VSA's parts is a key of the VSA's schema block."""
    page = (SPEC / "verification_summary.md").read_text()
    keys = set(re.findall(r'"(\w+)":', page))
    aliases = list(_aliases(("SlsaVerificationSummary", "SlsaVerifier")))
    assert aliases
    for cls, slot, alias in aliases:
        assert alias in keys, (cls, slot, alias)
