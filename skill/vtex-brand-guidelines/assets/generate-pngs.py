#!/usr/bin/env python3
"""Generate high-res PNG logo variants from the bundled SVGs.

PNGs are needed for python-pptx (which cannot embed SVG).
Requires: pip install cairosvg
"""
import os

import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
VARIANTS = ["rebel-pink", "serious-black", "white"]

for name in VARIANTS:
    src = os.path.join(HERE, f"vtex-logo-{name}.svg")
    dst = os.path.join(HERE, f"vtex-logo-{name}.png")
    cairosvg.svg2png(url=src, write_to=dst, output_width=960)
    print(f"wrote {dst}")
