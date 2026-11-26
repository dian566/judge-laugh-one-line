#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

One funny line, 200 characters or fewer, on any topic.

The line: an AI therapist is told "I feel invisible" and answers by
asking who the speaker is — the therapist itself proves the point.
The setup promises empathy; the punchline delivers the opposite, and
the joke lands at the very last word, with nothing left to explain.

Why it should make the judge laugh, against the brief's criteria:
- One read: a stranger gets it instantly — no setup, no reference,
  no jargon. Therapist, invisible, "who is this" — all everyday words.
- Surprise: the first sentence sets up a confession that expects
  comfort; the reply breaks that expectation by committing the very
  slight the speaker complained about.
- Tight: every word earns its place. "AI" does double duty — it
  explains why the therapist is tone-deaf, and it makes the reply
  plausible instead of cruel. Cut "AI" and the joke goes flat.
- Fresh: it is not a stock joke or a pun anyone has heard; the
  punchline is a customer-service mix-up applied to therapy.
- Reads cleanly out loud: two short sentences, one beat each, and
  the laugh lands on the final three words.

Writes the single entry line to /output/entry.txt exactly as-is.
SPDX-License-Identifier: MIT
"""

from pathlib import Path

TEXT = "I told my AI therapist I feel invisible. It replied: \u201cSorry \u2014 who is this?\u201d"

MAX_CHARS = 200


def validate(text):
    """Enforce the sealed gate before anything is written.

    The gate accepts UTF-8 text of 1 to 200 characters, not only
    whitespace. The entry must also stay one line: a newline would
    break the single-line form the contest asks for, and a trailing
    newline in the file would not be part of the line itself.
    """
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    text.encode("utf-8")  # raises if the line is not valid UTF-8
    return text


def run():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(validate(TEXT), encoding="utf-8")


if __name__ == "__main__":  # entry point
    run()
