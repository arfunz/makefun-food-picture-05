"""food-picture-01 entry #5: copy the meta ramen image to the output directory.

Deterministic: the same bytes are written on every run.
No network, standard library only. The image is bundled in the repo,
so the program needs no network access at all. All picture details —
including the seigaiha wave ornament and the glossy broth — are part
of the bundled image, not generated at run time.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
    sys.exit(0)
