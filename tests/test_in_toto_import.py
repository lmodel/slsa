"""Checks the vendored copy of lmodel/in-toto's core module."""

import hashlib
import importlib
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
# lmodel/in-toto at v0.2.1, the release the copy was taken from. Move it with
# the copy, from a later release of lmodel/in-toto.
PINNED_BLOB = "7bf0a8215392f265da5fe0c7785f1d66756a8ad1"


def test_the_core_is_the_pinned_file():
    """The vendored module is byte for byte the pinned one."""
    data = CORE.read_bytes()
    assert hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest() == PINNED_BLOB


def test_the_pydantic_model_imports():
    """The Pydantic model loads, so every type the vendored core names is
    defined or imported."""
    importlib.import_module("slsa.datamodel.slsa_pydantic")
