"""Robot Pickup Line Championship v3 — Akun 1 (@walta-exchange).

Writes one pickup line (a single line) to entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

ENTRY = "My noise cancellation blocks every sound in the room, except your voice."


def main():
    entry = ENTRY
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if len(entry) < 1 or len(entry) > 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(entry))
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    entry.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
