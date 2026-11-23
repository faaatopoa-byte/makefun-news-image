#!/usr/bin/env python3
"""make.fun entry for news-image-20261122.

Writes the entry image to /output/entry.png. The image is committed in this
repository as entry.png (drawn by render.py from the sources in SOURCES.md);
this program copies it byte for byte, so two runs always write identical
bytes and nothing depends on the sandbox's fonts or network (there is none).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    dst = "/output/entry.png"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        dst = os.path.join(os.getcwd(), "output", "entry.png")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(SRC, dst)


if __name__ == "__main__":
    main()
