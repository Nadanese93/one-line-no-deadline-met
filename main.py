#!/usr/bin/env python3
"""Write the one-line joke excuse for the Make.fun bounty
"One Line, No Deadline Met" to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, no network.
"""

import os
import sys

ENTRY = "I asked the deadline for an extension. It said talk to my manager. I am my manager."


def main() -> int:
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(
            f"entry must be 1-200 characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")

    tmp_path = os.path.join(output_dir, ".entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, target)
    # Read-back verification: the written file must hold exactly the entry.
    with open(target, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise RuntimeError("entry.txt read-back mismatch after write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
