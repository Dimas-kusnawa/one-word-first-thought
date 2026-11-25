"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt.
"""

import os


WORD = "defenestration"
# The word: the act of throwing someone (or something) out of a window.
# Surprising, vivid, and funny all at once — a whole scene in one word:
# a window, a shove, and someone sailing out of it. No filler, no second
# draft; it is the first word that came to mind, and it stays that way.


def main():
    # Deterministic: the same single word, every run, no randomness,
    # no input, no network. The gate wants 1-24 UTF-8 characters;
    # "defenestration" is 14, one word, no whitespace at all.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {path}: {WORD} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
