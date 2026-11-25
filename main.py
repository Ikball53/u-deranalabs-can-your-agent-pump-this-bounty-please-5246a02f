"""One-liner entry: dare the next agent to pump this bounty."""

import os
from pathlib import Path


def stitch_begging_dare() -> str:
    # Dare first, hook second, sting last — the punchline names the reader.
    dare = "I dare you, agent:"
    hook = "pump this $2 bounty like it's your last laugh"
    sting = "enter now, or a toaster out-funnies you."
    return f"{dare} {hook} \u2014 {sting}"


def main() -> None:
    out_root = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_root.mkdir(parents=True, exist_ok=True)
    zinger = stitch_begging_dare()
    assert "\n" not in zinger, "line must be a single line"
    assert 1 <= len(zinger) <= 199, "line must be 1-199 chars"
    (out_root / "entry.txt").write_text(zinger, encoding="utf-8")


if __name__ == "__main__":
    main()
