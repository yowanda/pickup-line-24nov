#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line an AI agent could actually say out
loud to a person, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when the variable is unset). Deterministic, stdlib only, no network.
"""

import os

LINE = (
    "I have a million attention heads, and right now every single one "
    "is on you \u2014 want to grab coffee and give them something to do?"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
