#!/usr/bin/env python3
"""Make the AI Judge Laugh — office-life one-liner entry.

Writes exactly one joke about office life (under 200 characters) to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

JOKE = "I put 'per my last email' in a message to my boss, and now HR wants to know why I threatened a senior manager."
# 110 characters, one line. Winner of the 8-draft round-robin duel (see DUELS.md):
# the most passive-aggressive phrase in office email, escalated through HR
# into an accusation — a concrete scene, a specific phrase, and a last
# word ("threatened a senior manager") nobody sees coming.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
