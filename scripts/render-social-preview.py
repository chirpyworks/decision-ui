#!/usr/bin/env python3
"""Render the canonical social-preview SVG to a compact PNG."""

from pathlib import Path
from io import BytesIO

import cairosvg
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "social-preview.svg"
TARGET = ROOT / "assets" / "social-preview.png"


def main() -> None:
    png_bytes = cairosvg.svg2png(
        url=str(SOURCE),
        output_width=1280,
        output_height=640,
    )
    image = Image.open(BytesIO(png_bytes)).convert("RGB")
    # Flat UI artwork compresses cleanly with an adaptive palette.
    image = image.convert("P", palette=Image.Palette.ADAPTIVE, colors=32)
    image.save(TARGET, optimize=True)
    print(f"Rendered {TARGET.relative_to(ROOT)} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
