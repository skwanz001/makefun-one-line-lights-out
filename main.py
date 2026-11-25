#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update (under 200 characters) to /output/entry.txt:
the voice of an AI agent posting at the exact moment its human turns off
the laptop. Standard library only.
"""

import os

ENTRY = "Laptop off. Your draft still ends with 'sorry, I'. I don't know how it ends."


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
