#!/usr/bin/env python3
"""Check the SLSA specification copy against the SLSA Working Group's tags.

Two things can go wrong with ``src/slsa/schema/spec/`` without any change
in this repository:

- the SLSA Working Group tags a newer specification version, so the schema
  falls behind;
- the copied files drift from the tree they were taken from.

The copy has no version in its path, so the tree it was taken from is pinned
below, beside the files known to differ from it (NOTICE lists them too).
This script asks the GitHub API for slsa-framework/slsa's version tags and
for the pinned tree, and compares every copied file with its blob there by
git object hash, so nothing is downloaded but two listings. It prints a
Markdown report and exits 1 when a newer version is tagged or a file differs
in a way not listed below.

Set ``GITHUB_TOKEN`` to raise the API rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "slsa" / "schema" / "spec"
API = "https://api.github.com/repos/slsa-framework/slsa"

# The tag and the folder the copy was taken from. Move both when the copy is
# replaced from a newer version, and empty KNOWN_DIFFERENCES.
PINNED_TAG = "v1.2"
PINNED_PATH = "docs/spec/draft"

# Files that differed from the pinned tree when this check was added: one
# edited link, and three pages that are not in that tree.
KNOWN_DIFFERENCES = {
    "build-requirements.md",
    "attested-build-env-levels.md",
    "levels.md",
    "verifying-systems.md",
}

# A version tag: v1.2 or v1.0.0, not a release candidate or a dated tag.
VERSION_TAG = re.compile(r"^v\d+(\.\d+)+$")


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url, headers={"Accept": "application/vnd.github+json", "User-Agent": "lmodel-slsa-upstream-check"}
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that v1.0 and v1.0.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the trees API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def check() -> tuple[list[str], bool]:
    """Return the report lines and whether anything needs attention."""
    report = [f"- Pinned version: SLSA {PINNED_TAG}, `{PINNED_PATH}/`, copied to `src/slsa/schema/spec/`."]
    attention = False

    tags = [t["name"] for t in json.loads(_get(f"{API}/tags?per_page=100")) if VERSION_TAG.match(t["name"])]
    latest = max(tags, key=_version_key) if tags else PINNED_TAG
    if _version_key(latest) > _version_key(PINNED_TAG):
        attention = True
        report.append(
            f"- **The SLSA Working Group has tagged {latest}.** Replace `src/slsa/schema/spec/` with that "
            f"version's specification pages (https://github.com/slsa-framework/slsa/tree/{latest}), move "
            f"the pin in `scripts/check_upstream_release.py`, update NOTICE and the README's attribution, "
            f"and review the schema against the new pages."
        )
    else:
        report.append(f"- Latest version tag: {latest}, the pinned one.")

    tree = json.loads(_get(f"{API}/git/trees/{PINNED_TAG}?recursive=1"))
    if tree.get("truncated"):
        return report + ["- The pinned tree listing came back truncated; compare the copy by hand."], True
    prefix = PINNED_PATH + "/"
    upstream = {e["path"][len(prefix):]: e["sha"] for e in tree["tree"] if e["type"] == "blob" and e["path"].startswith(prefix)}

    files = sorted(p for p in COPY.rglob("*") if p.is_file())
    matching, known, differing = 0, [], []
    for path in files:
        rel = path.relative_to(COPY).as_posix()
        if upstream.get(rel) == _blob_sha(path):
            matching += 1
        elif rel in KNOWN_DIFFERENCES:
            known.append(rel)
        elif rel in upstream:
            differing.append(f"`{rel}` differs from `{PINNED_PATH}/{rel}` at {PINNED_TAG}")
        else:
            differing.append(f"`{rel}` is not in `{PINNED_PATH}/` at {PINNED_TAG}")
    report.append(f"- {matching} of {len(files)} copied files match the pinned tree byte for byte.")
    if known:
        report.append(f"- Known differences, listed in NOTICE: {', '.join(f'`{k}`' for k in known)}.")
    if differing:
        attention = True
        report.append(f"- **{len(differing)} copied file(s) differ from the pinned tree in a way not listed:**")
        report += [f"  - {d}" for d in differing]
    return report, attention


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--report", type=Path, help="Also write the Markdown report to this file")
    args = parser.parse_args(argv)
    lines, attention = check()
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
