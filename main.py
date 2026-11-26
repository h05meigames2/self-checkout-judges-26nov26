#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one original funny remark in the voice of a judgmental
self-checkout machine to /output/entry.txt. Deterministic, no network
access, standard library only.
"""

import os

LINE = (
    "Twelve yoghurts and nothing else. I've scanned your whole "
    "personality. It expires before the yoghurts do."
)


def main():
    # Gate: /output/entry.txt must hold UTF-8 text of 1-200 characters,
    # exactly the one line, with no trailing newline.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
