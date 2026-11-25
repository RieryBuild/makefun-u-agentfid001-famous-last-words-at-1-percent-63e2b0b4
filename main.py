"""Famous Last Words at 1 Percent — entry program.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the phone's
own final system message as its battery hits 1 percent — a Low Power
Mode log that disables hope, your alarms, and the flashlight that's
been on since Tuesday. Pure phone voice, three-beat escalation, punch at
the end.
"""
import os

LINE = "Entering Low Power Mode: disabling hope, your alarms, and the flashlight that's been on since Tuesday."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 199 and "\n" not in LINE, "entry must be one line of 1-199 characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
