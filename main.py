"""One short paragraph meant to slow the reader down, saved as entry.txt.

The text never changes between runs: it is fixed here, and the only
work the program does is check it fits the gate and save it where the
grader looks. Give it a scratch folder with MAKEFUN_OUTPUT_DIR when
you run it by hand.
"""

import os
import sys
from pathlib import Path


def target_file():
    folder = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder).joinpath("entry.txt")


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


def save_entry():
    """Check the text against the gate, then save it."""
    text = PASSAGE
    size = len(text)
    if size < 1 or size > 1000 or text.strip() == "":
        print("entry text does not fit the 1 to 1000 character gate", file=sys.stderr)
        return 1
    spot = target_file()
    spot.parent.mkdir(parents=True, exist_ok=True)
    spot.write_bytes(text.encode("utf-8"))
    print("saved " + str(size) + " characters to " + str(spot))
    return 0


raise SystemExit(save_entry())
