"""Robot Pickup Line Championship v3 — Akun 1 (@walta-exchange).

Reviser rewrite: the entry line itself is unchanged (byte-identical to
the builder version). This revision restructures the program around a
dedicated builder function so the entry text lives in exactly one place
(the ENTRY constant) and validation is a separate, testable step.

Writes one pickup line (a single line) to entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

ENTRY = "My noise cancellation blocks every sound in the room, except your voice."

MAX_LENGTH = 120
MIN_LENGTH = 1


def build_entry():
    """Return the competition entry line.

    The text is defined once, in ENTRY, and returned unchanged so the
    output is byte-identical every run.
    """
    return ENTRY


def _check_type(entry):
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")


def _check_length(entry):
    if len(entry) < MIN_LENGTH or len(entry) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(entry))
        )


def _check_single_line(entry):
    if any(ch in entry for ch in ("\n", "\r")):
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")


def validate_entry(entry):
    """Validate a candidate entry line; raise ValueError if invalid.

    Checks run in a fixed order — type, length, then single-line shape —
    so the first failure reported is the most basic one.
    """
    _check_type(entry)
    _check_length(entry)
    _check_single_line(entry)
    entry.encode("utf-8")


def write_entry(entry, out_dir):
    """Write the validated entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    return path


def main():
    entry = build_entry()
    validate_entry(entry)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(entry, out_dir)


if __name__ == "__main__":
    main()
