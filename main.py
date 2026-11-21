#!/usr/bin/env python3
"""Entry program for the make.fun 'The joke about the demo' competition.

The deliverable is a single one-line joke, kept in entry.txt beside
this file: a demo crashes in front of everyone, and the coding agent
beside the developer produces a fix, a postmortem, and a commit
message blaming the Wi-Fi.

The grading sandbox has no network and installs nothing, so this
program uses only the Python standard library. It locates entry.txt,
checks it against the gate (UTF-8, 1..280 Unicode code points, not
only whitespace) and copies it byte for byte to entry.txt inside the
output directory (MAKEFUN_OUTPUT_DIR, else /output). Exit code 0
means the entry was written.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIMIT = 280


def read_joke():
    path = os.path.join(HERE, "entry.txt")
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    if not text.strip():
        raise ValueError("entry.txt is only whitespace")
    if not 1 <= len(text) <= LIMIT:
        raise ValueError("entry.txt must be 1..280 code points")
    return raw


def main():
    raw = read_joke()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as fh:
        fh.write(raw)
    with open(target, "rb") as fh:
        written = fh.read()
    if written != raw:
        raise ValueError("written entry.txt does not match the source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
