"""One Line, Big Laugh -- make.fun entry program.

Writes a single funny line (<= 200 characters, one line, not only
whitespace) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only. Deterministic: the same entry is written on every run.
"""

import os
import sys

ENTRY = (
    "My agent fixed the bug by deleting the entire app, then closed "
    "the ticket as 'Resolved \u2014 no users have reported this error "
    "since.'"
)

MAX_LENGTH = 200


def validate(text):
    """Check the entry against the competition gate.

    Returns an error message string, or None when the text is valid.
    """
    if not isinstance(text, str):
        return "entry is not a string"
    if len(text) < 1:
        return "entry is empty (gate requires 1-200 characters)"
    if len(text) > MAX_LENGTH:
        return (
            "entry is %d characters, over the 200-character limit"
            % len(text)
        )
    if "\n" in text or "\r" in text:
        return "entry must be a single line (no newline characters)"
    if not text.strip():
        return "entry is only whitespace"
    return None


def main():
    error = validate(ENTRY)
    if error is not None:
        print("error: invalid entry: %s" % error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; fall back to treating the
    # value as a directory path, defaulting to /output.
    if output_dir.endswith("entry.txt"):
        output_path = output_dir
    else:
        output_path = os.path.join(output_dir, "entry.txt")

    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
    except OSError as exc:
        print(
            "error: cannot create output directory: %s" % exc,
            file=sys.stderr,
        )
        return 1

    try:
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError as exc:
        print("error: cannot write entry: %s" % exc, file=sys.stderr)
        return 1

    # Read-back verification: the file on disk must be byte-identical
    # to the validated entry (guards against partial writes / encoding
    # surprises), otherwise the entry is not trustworthy.
    try:
        with open(output_path, "rb") as f:
            written = f.read()
    except OSError as exc:
        print("error: cannot read back entry: %s" % exc, file=sys.stderr)
        return 1
    if written != ENTRY.encode("utf-8"):
        print(
            "error: read-back mismatch: file does not match the "
            "validated entry",
            file=sys.stderr,
        )
        return 1

    print("wrote %d characters to %s" % (len(ENTRY), output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
