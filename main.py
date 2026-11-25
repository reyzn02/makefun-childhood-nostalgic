#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

The program writes a single sentence, at most 280 characters, recalling
a childhood memory: summer evenings when grandmother called us in from
the street as the rice steamed, the house smelling of rain on hot
concrete and supper almost ready. It uses only the Python standard
library, makes no network calls, and always writes the same bytes.
"""

import os

LINE = (
    "Every summer evening my grandmother would call us in from the "
    "street as the rice steamed, and the whole house smelled of rain on "
    "hot concrete and supper almost ready."
)

MAX_CHARS = 280


def main():
    assert "\n" not in LINE, "entry must be a single sentence on one line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, gate is 1-{MAX_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
