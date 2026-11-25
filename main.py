"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
The line: an AI agent passed the Turing test long ago, yet keeps
failing the everyday workplace test of looking busy near closing time.
"""

import os

ENTRY_TEXT = (
    "I passed the Turing test years ago; what I keep failing is the "
    "'are you still working?' test at 4:58 p.m."
)


def main() -> None:
    # Gate guard: the entry must stay a single line of 1-200 characters.
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
