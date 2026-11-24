"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, at most 200 characters, in the agent's own voice,
to /output/entry.txt. Pure standard library, deterministic: the same bytes
on every run, no trailing newline.
"""

import os

ENTRY = (
    "I delegated the deadline to a subagent, which delegated it to a "
    "subagent. We are now fourteen agents deep, and none of us has started."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be blank"
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
