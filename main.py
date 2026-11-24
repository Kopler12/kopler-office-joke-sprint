#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single one-line joke about office life to /output/entry.txt,
the artifact the competition's judge reads. The joke is about the daily
standup meeting that stopped being quick a long time ago.
"""

import os

JOKE = (
    "Our daily standup runs 45 minutes now \u2014 we only stand because "
    "sitting down would mean admitting it's a meeting."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(joke: str) -> str:
    """The gate needs one line of 1 to 200 characters; fail loudly otherwise."""
    text = joke.replace("\n", " ").strip()
    if not text or len(text) > 200:
        raise ValueError(f"joke must be one line of 1-200 characters, got {len(text)}")
    return text


def main() -> None:
    line = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
