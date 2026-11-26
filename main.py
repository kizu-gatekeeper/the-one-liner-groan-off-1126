"""Entry for make.fun: The One-Liner Groan-Off.

Writes one original dad joke to entry.txt.

Best served at the dinner table, groan guaranteed.
"""
import os

LINE = "I told my suitcase there would be no vacation this year; now I am dealing with a lot of emotional baggage."
MAX_CHARS = 140


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds max chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
