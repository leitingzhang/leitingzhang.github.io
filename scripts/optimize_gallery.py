"""Generate gallery thumbnails and Jekyll metadata without changing originals.

Install dependencies: python -m pip install Pillow PyYAML
Run from any directory: python scripts/optimize_gallery.py
"""

import json
from pathlib import Path

from PIL import Image, ImageOps
import yaml


ROOT = Path(__file__).resolve().parents[1]
WIDTHS = (320, 640)


def main():
    manifest = {}
    original_bytes = thumbnail_bytes = 0
    count = 0
    for category in ("work", "life"):
        pictures = yaml.safe_load(
            (ROOT / "_data" / f"pictures_{category}.yml").read_text(encoding="utf-8")
        ) or []
        manifest[category] = {}
        for picture in pictures:
            filename = picture["image"]
            source = ROOT / "images" / "picpic" / category / filename
            variants = []
            with Image.open(source) as original:
                # Respect phone/camera orientation before discarding metadata.
                image = ImageOps.exif_transpose(original).convert("RGB")
                for width in WIDTHS:
                    thumbnail = image.copy()
                    thumbnail.thumbnail((width, image.height), Image.Resampling.LANCZOS)
                    destination = (
                        ROOT / "images" / "picpic" / "thumbnails" / category
                        / f"{filename}-{width}.webp"
                    )
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    thumbnail.save(destination, "WEBP", quality=82, method=6)
                    variants.append({
                        "src": "/" + destination.relative_to(ROOT).as_posix(),
                        "width": thumbnail.width,
                        "height": thumbnail.height,
                    })
            manifest[category][filename] = {"variants": variants}
            original_bytes += source.stat().st_size
            thumbnail_bytes += destination.stat().st_size
            count += 1
    (ROOT / "_data" / "gallery_thumbnails.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Generated {count} thumbnail pairs; originals unchanged.")
    print(f"Originals: {original_bytes:,} bytes; 640px previews: {thumbnail_bytes:,} bytes")
    if original_bytes:
        print(f"Preview transfer reduction: {1 - thumbnail_bytes / original_bytes:.1%}")


if __name__ == "__main__":
    main()
