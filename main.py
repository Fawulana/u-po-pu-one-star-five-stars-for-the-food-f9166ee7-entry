#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun program/v1 entry.

Writes a single sentence to /output/entry.txt: an alien tourist's
one-star review of planet Earth that grudgingly gives the food five
stars. Standard library only, deterministic, no network, no input.
"""

import os
from pathlib import Path

TEXT = (
    "One star for Earth: my saucer was towed, the rain falls without "
    "permission, and a human held eye contact for nine seconds, but "
    "five stars for the tacos, which reformatted all three of my stomachs."
)


def main() -> None:
    out_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
