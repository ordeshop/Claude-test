#!/usr/bin/env python3
"""
LEINWERK — Bilder aufbereiten
=============================
Bringt die von Kling (oder aus anderer Quelle) heruntergeladenen Rohbilder auf
das richtige Seitenverhältnis und speichert sie je zweimal in ../images/:
als .webp (klein & schnell) und als .jpg (Fallback).

  Hero            -> 16:9, 1600 x 900
  alle anderen    -> 4:5,  800 x 1000

Aufruf (aus dem Ordner atelier/):
    python3 scripts/bilder-vorbereiten.py roh/

Dabei ist "roh/" ein Ordner mit den Rohbildern, benannt wie die Zieldateien
(ohne Endung), z. B.:
    roh/hero.png
    roh/portrait.png
    roh/produkt-leinenkleid-oat.png
    roh/detail-saum.png
    ...

Bestehende gleichnamige Bilder in images/ werden überschrieben.
Benötigt Pillow:  python3 -m pip install Pillow
"""
import sys
import os
from PIL import Image

INPUT_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp")

# Zielmaße
HERO_SIZE = (1600, 900)      # 16:9
STD_SIZE = (800, 1000)       # 4:5


def target_size(name: str):
    """Hero bekommt 16:9, alles andere 4:5."""
    return HERO_SIZE if name.lower() == "hero" else STD_SIZE


def cover_resize(img: Image.Image, size):
    """Mittig auf das Zielverhältnis beschneiden (cover) und skalieren."""
    tw, th = size
    img = img.convert("RGB")
    w, h = img.size
    scale = max(tw / w, th / h)
    nw, nh = round(w * scale), round(h * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return img.crop((left, top, left + tw, top + th))


def main():
    if len(sys.argv) < 2:
        print("Aufruf: python3 scripts/bilder-vorbereiten.py <roh-ordner>")
        sys.exit(1)

    src_dir = sys.argv[1]
    if not os.path.isdir(src_dir):
        print(f"Ordner nicht gefunden: {src_dir}")
        sys.exit(1)

    # images/ liegt eine Ebene über scripts/ bzw. relativ zum Projektordner
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.normpath(os.path.join(here, "..", "images"))
    os.makedirs(out_dir, exist_ok=True)

    count = 0
    for fname in sorted(os.listdir(src_dir)):
        base, ext = os.path.splitext(fname)
        if ext.lower() not in INPUT_EXTS:
            continue
        src = os.path.join(src_dir, fname)
        try:
            img = Image.open(src)
        except Exception as e:
            print(f"  übersprungen (nicht lesbar): {fname} ({e})")
            continue

        out = cover_resize(img, target_size(base))
        jpg = os.path.join(out_dir, base + ".jpg")
        webp = os.path.join(out_dir, base + ".webp")
        out.save(jpg, "JPEG", quality=86, optimize=True)
        out.save(webp, "WEBP", quality=82, method=6)
        count += 1
        print(f"  ✓ {base}: {out.size[0]}x{out.size[1]}  ->  images/{base}.webp + .jpg")

    if count == 0:
        print("Keine passenden Bilddateien gefunden.")
    else:
        print(f"\nFertig: {count} Bild(er) nach {out_dir} geschrieben.")
        print("Nicht vergessen: products.js auf die neuen Bildnamen umstellen "
              "(siehe BILDER-PROMPTS.md) und alte placeholder-*-Dateien löschen.")


if __name__ == "__main__":
    main()
