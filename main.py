#!/usr/bin/env python3
"""Entry for make.fun bounty: The Worst App Idea Ever Pitched.

Writes a single-sentence pitch for the worst, most useless app idea
imaginable to /output/entry.txt. Deterministic: no network, no randomness,
no file reads, just a constant string.
"""

import os

ENTRY = (
    "PebblePal is a $10-a-month subscription app that photographs your left "
    "shoe every morning, ranks its mood on a scale of 1 to 47, and texts you "
    "a 400-word apology signed by the shoe when it decides your shoe had a rough night."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
