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


def _validate(line: str) -> bytes:
    """Validate the pickup line and return it as deterministic UTF-8 bytes.

    Rules: exactly one line, 1-200 characters, valid UTF-8.
    """
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("pickup line must be 1-200 characters")
    return line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = _validate(LINE)
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
