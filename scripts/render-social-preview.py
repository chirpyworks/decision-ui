#!/usr/bin/env python3
"""Render canonical social SVG assets to compact PNGs."""

from pathlib import Path
from io import BytesIO

import cairosvg
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ("social-preview.svg", "social-preview.png", 1280, 640),
    ("instagram-launch.svg", "instagram-launch.png", 1080, 1080),
]


def render(source_name: str, target_name: str, width: int, height: int) -> None:
    source = ROOT / "assets" / source_name
    target = ROOT / "assets" / target_name
    png_bytes = cairosvg.svg2png(url=str(source), output_width=width, output_height=height)
    image = Image.open(BytesIO(png_bytes)).convert("RGB")
    image = image.convert("P", palette=Image.Palette.ADAPTIVE, colors=32)
    image.save(target, optimize=True)
    print(f"Rendered {target.relative_to(ROOT)} ({target.stat().st_size} bytes)")


def main() -> None:
    for spec in TARGETS:
        render(*spec)


if __name__ == "__main__":
    main()
