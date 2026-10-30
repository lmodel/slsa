"""Checks the vendored copy of lmodel/in-toto's core module."""

import hashlib
from pathlib import Path

CORE = (
    Path(__file__).parent.parent
    / "src"
    / "slsa"
    / "schema"
    / "in_toto"
    / "in_toto_core.yaml"
)

# The git object hash of src/in_toto_linkml/schema/in_toto_core.yaml in
# lmodel/in-toto at v0.1.0, the release the copy was taken from. Move it with
# the copy, from a later release of lmodel/in-toto.
PINNED_BLOB = "3ffd841743df241e2948a2150caa8b03a024762f"


def test_the_core_is_the_pinned_file():
    """The vendored module is byte for byte the pinned one."""
    data = CORE.read_bytes()
    assert hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest() == PINNED_BLOB
