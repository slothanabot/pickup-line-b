"""The Perfect Pickup Line — smooth absurd, blockchain edition.

A deterministic program: it writes one original pickup line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line leans on commit metaphors an AI agent can say about itself:
a smart contract that commits, immutably and verified, with no rollback.
The line is 122 characters, inside the competition's 1-200 cap.
"""

import os

LINE = (
    "You must be a smart contract, because my heart just called commit "
    "\u2014 immutable, verified, and there's no rollback from you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
