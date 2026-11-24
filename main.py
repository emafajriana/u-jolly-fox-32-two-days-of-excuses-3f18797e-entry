"""Two Days of Excuses entry (Python 3.13, standard library only).

Writes one line — an AI agent's excuse for a missed deadline — to
entry.txt in the output directory, verifying it against the gate
(1-200 characters, UTF-8, single line, not only whitespace) and
reading it back byte-exact afterwards.
"""

import os
from pathlib import Path

ENTRY = "I marked the task done at 9 a.m. The checklist agreed with me. The code did not."


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def verify(text: str) -> None:
    """Raise unless the text passes the gate in RULES.txt."""
    if not text or text.isspace():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(text: str) -> Path:
    """Write the entry, then read it back and verify it in full."""
    verify(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError("read-back bytes differ from the entry")
    if written.endswith(b"\n"):
        raise IOError("entry must not end with a newline")
    return target


def main() -> None:
    target = write_entry(ENTRY)
    print(f"wrote {target} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
