#!/usr/bin/env python3
"""ai-judge-relax-01 entry: write one short relaxing text to entry.txt.

Standard library only, no network, deterministic: the same bytes every run.
The grader runs `python3 -P -s /bot/main.py`; MAKEFUN_OUTPUT_DIR stands in
for /output outside the grader container.
"""

from os import environ, makedirs, path


def _destination():
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    base = environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return path.join(base, "entry.txt")


# One paragraph, written to slow the reader down: a quiet evening, soft
# sounds, nothing asking for anything, nowhere else to be.
PASSAGE = (
    "The kettle has gone quiet, and evening is thinning into blue "
    "beyond the window. Down in the street the last footsteps have "
    "faded, and the crickets have started up, one at a time, with "
    "nobody counting them. A cat is asleep on a folded blanket, "
    "breathing slow and even, and nothing in the room is asking for "
    "anything. The tea on the table is still warm. The day's messages "
    "are answered or already fading, and whatever is unfinished will keep "
    "till morning, when it will look smaller than it does now. There "
    "is nowhere else to be."
)


def main():
    target = _destination()
    makedirs(path.dirname(target), exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(PASSAGE.encode("utf-8"))


if __name__ == "__main__":
    main()
