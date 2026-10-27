"""Checks that rules the schema states in more than one place agree."""

import itertools
import re
from pathlib import Path

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
