#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Writes the meme image to the harness output directory as entry.png.

The meme is shipped in this repository as meme.png (a fresh 1024x1024
PNG drawn for this bounty). This program is deterministic: it copies the
shipped bytes verbatim, so every run produces a byte-identical entry.png.
No network, no randomness, no environment secrets.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "meme.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Self-check against the competition gate before reporting success:
    # whole PNG, at most 1 MiB, at most 1024x1024 pixels.
    with open(dest, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        print("error: output is not a PNG", file=sys.stderr)
        return 1
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    size = os.path.getsize(dest)
    if size > 1_048_576 or width > 1024 or height > 1024:
        print(f"error: gate fail size={size} {width}x{height}", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
