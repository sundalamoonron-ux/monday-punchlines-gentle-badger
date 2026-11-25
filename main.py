#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings to /output/entry.txt.
"""

from pathlib import Path

JOKE = (
    "I told Monday I'd see it in court. "
    "It showed up early, in a suit, with my calendar as a witness."
)
# 96 characters. Winner of the pairwise test in candidates.md: a courtroom
# scene with a three-part payoff (early, in a suit, calendar as witness) —
# fresh angle, no alarm/coffee/snooze cliche.


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = Path("/output")
    if not out_dir.is_dir():
        out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
