#!/usr/bin/env python3
"""Baut ein verkaufsfertiges Ebook-PDF aus HTML-Dateien.

- rendert Cover (ohne Seitenzahl) und Innenteil (mit Seitenzahl) getrennt
- fuehrt beides zusammen
- setzt PDF-Metadaten
- legt PNG-Vorschauen jeder Seite ab, damit man das Ergebnis wirklich ansehen kann

Beispiel:
  python3 build_pdf.py --cover cover.html --body body.html \
      --out /mnt/user-data/outputs/mein-ebook.pdf \
      --format A4 --title "Titel" --author "Name" --preview-dir preview/
"""

import argparse
import os
import subprocess
import sys
import tempfile

FORMATS = {
    "A4": {"format": "A4"},
    "letter": {"format": "Letter"},
    "6x9": {"width": "6in", "height": "9in"},
    "landscape": {"width": "1600px", "height": "1000px"},
}


def footer_html(accent: str, offset: int) -> str:
    # Chromium ignoriert @page-Randboxen -> Seitenzahl kommt aus diesem Template.
    # Schriftgroesse muss explizit gesetzt werden, sonst rendert Chromium winzig.
    return (
        '<div style="width:100%;font-size:8pt;font-family:sans-serif;'
        f'color:{accent};padding:0 22mm;text-align:right;">'
        '<span class="pageNumber"></span></div>'
        if offset == 0
        else
        '<div style="width:100%;font-size:8pt;font-family:sans-serif;'
        f'color:{accent};padding:0 22mm;text-align:right;">'
        '<span class="pageNumber"></span></div>'
    )


def render(html_path: str, pdf_path: str, fmt: dict, numbered: bool, accent: str,
           margin_bottom: str = "14mm") -> None:
    from playwright.sync_api import sync_playwright

    url = "file://" + os.path.abspath(html_path)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.emulate_media(media="print")
        opts = dict(path=pdf_path, print_background=True, prefer_css_page_size=True)
        opts.update(fmt)
        if numbered:
            opts.update(
                display_header_footer=True,
                header_template="<div></div>",
                footer_template=footer_html(accent, 0),
                margin={"top": "0mm", "bottom": margin_bottom,
                        "left": "0mm", "right": "0mm"},
            )
        page.pdf(**opts)
        browser.close()


def merge(parts, out_path, meta):
    from pypdf import PdfReader, PdfWriter

    writer = PdfWriter()
    for part in parts:
        for pg in PdfReader(part).pages:
            writer.add_page(pg)
    if meta:
        writer.add_metadata({f"/{k}": v for k, v in meta.items() if v})
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "wb") as fh:
        writer.write(fh)


def previews(pdf_path: str, out_dir: str) -> int:
    os.makedirs(out_dir, exist_ok=True)
    subprocess.run(
        ["pdftoppm", "-png", "-r", "70", pdf_path, os.path.join(out_dir, "seite")],
        check=True,
    )
    return len([f for f in os.listdir(out_dir) if f.endswith(".png")])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--body", required=True, help="HTML des Innenteils")
    ap.add_argument("--cover", help="HTML des Covers (wird ohne Seitenzahl gesetzt)")
    ap.add_argument("--front", help="optionales HTML fuer Titel/Impressum/Inhalt, ohne Seitenzahl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--format", default="A4", choices=list(FORMATS))
    ap.add_argument("--accent", default="#666666", help="Farbe der Seitenzahl")
    ap.add_argument("--title", default="")
    ap.add_argument("--author", default="")
    ap.add_argument("--subject", default="")
    ap.add_argument("--keywords", default="")
    ap.add_argument("--preview-dir", default="")
    args = ap.parse_args()

    fmt = FORMATS[args.format]
    tmp = tempfile.mkdtemp(prefix="ebook-")
    parts = []

    for name, path, numbered in (
        ("cover", args.cover, False),
        ("front", args.front, False),
        ("body", args.body, True),
    ):
        if not path:
            continue
        target = os.path.join(tmp, f"{name}.pdf")
        render(path, target, fmt, numbered, args.accent)
        parts.append(target)
        print(f"gerendert: {name}")

    merge(parts, args.out, {
        "Title": args.title, "Author": args.author,
        "Subject": args.subject, "Keywords": args.keywords,
        "Producer": "ebook-design",
    })

    size_mb = os.path.getsize(args.out) / 1_048_576
    print(f"PDF: {args.out} ({size_mb:.1f} MB)")
    if size_mb > 15:
        print("WARNUNG: ueber 15 MB — Bilder verkleinern.")

    if args.preview_dir:
        n = previews(args.out, args.preview_dir)
        print(f"{n} Vorschaubilder in {args.preview_dir} — jetzt ansehen, nicht ueberspringen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
