# Technik: von HTML/CSS zum verkaufsfertigen PDF

## Warum HTML/CSS

Chromium setzt Text besser als reportlab und erlaubt echtes Layout (Raster, Flex, SVG, Duotone-Filter, Webfonts). reportlab nur für rein programmatische Massenerzeugung nutzen.

Pipeline: `content.html` + `styles.css` → Playwright/Chromium → `.pdf` → pypdf für Zusammenführen/Metadaten.

## Schriften beschaffen

Der Container erreicht kein fonts.googleapis.com. Zwei funktionierende Wege:

```bash
# 1) npm — bevorzugt, enthält woff2 und ttf
cd /home/claude/fonts
npm pack @fontsource/fraunces @fontsource/source-sans-3
tar -xzf fontsource-fraunces-*.tgz     # → package/files/*.woff2
```

```bash
# 2) GitHub (google/fonts) für alles, was fontsource nicht hat
curl -sLO https://raw.githubusercontent.com/google/fonts/main/ofl/<familie>/<Datei>.ttf
```

Einbinden mit absolutem `file://`-Pfad oder — sicherer — als Base64 im CSS:

```css
@font-face {
  font-family: "Fraunces";
  src: url("file:///home/claude/fonts/fraunces-latin-700-normal.woff2") format("woff2");
  font-weight: 700;
  font-display: block;
}
```

Prüfe nach dem Rendern, ob die Schrift wirklich greift (Vorschaubild ansehen — Fallback auf DejaVu Sans ist sofort erkennbar).

## Chromium-Fallstricke (wichtig)

- **`@page`-Randboxen wie `@bottom-center { content: counter(page) }` funktionieren nicht.** Chromium ignoriert sie. Seitenzahlen deshalb über Playwrights `footer_template` (mit `<span class="pageNumber">`) oder manuell platzieren.
- `footer_template`/`header_template` brauchen `display_header_footer=True` **und** gesetzte `margin`-Werte, sonst bleibt der Bereich unsichtbar. Schriftgröße im Template explizit setzen (Default ist winzig).
- Hintergrundfarben und -bilder erscheinen nur mit `print_background=True`.
- Seitenumbruch steuern: `break-after: page` / `break-inside: avoid`. Für Überschriften `break-after: avoid` setzen, damit keine Überschrift allein unten steht.
- Schusterjungen/Hurenkinder: `orphans: 3; widows: 3;` im Fließtext — Chromium respektiert das im Druckmodus.
- `hyphens: auto` braucht `lang="de"` am `<html>`. Ob die Trennmuster im Container vorhanden sind, muss man testen: einen langen deutschen Absatz in schmaler Spalte rendern und ansehen. Ohne Trennung: Flattersatz statt Blocksatz.
- Feste Seitengröße im CSS **und** im PDF-Aufruf identisch setzen, sonst skaliert Chromium.
- Gestaltete `.page`-Blöcke brauchen `break-before: page` **und** `break-after: page`. Nur mit `break-after` landet eine gestaltete Seite direkt unter dem vorherigen Fließtext auf derselben Seite (getestet, passiert zuverlässig).
- Die Höhe eines `.page`-Blocks minimal unter die Seitenhöhe setzen (296,6 mm statt 297 mm bei A4). Exakte Gleichheit erzeugt durch Rundung gelegentlich eine leere Folgeseite.
- `prefer_css_page_size=True` verwenden, damit `@page { size: ... }` gewinnt.

## CSS-Grundgerüst (A4 hoch)

```css
@page { size: A4; margin: 0; }

html { font-size: 12pt; }
body {
  margin: 0;
  font-family: "Source Sans 3", sans-serif;
  color: #241F1B;
  background: #FAF6F0;
  -webkit-print-color-adjust: exact;
}

/* Jede Seite als eigenes Element = volle Kontrolle */
.page {
  position: relative;
  width: 210mm;
  height: 297mm;
  padding: 20mm 22mm 22mm 22mm;
  box-sizing: border-box;
  overflow: hidden;
  break-after: page;
}
.page:last-child { break-after: auto; }

/* Fließtext-Kapitel: laufender Satz über mehrere Seiten */
.flow { padding: 20mm 22mm; }
.flow p {
  max-width: 125mm;
  line-height: 1.55;
  orphans: 3;
  widows: 3;
  margin: 0 0 6pt;
  hyphens: auto;
}
h2 { break-after: avoid; break-before: page; }
h3 { break-after: avoid; }
figure, table, .callout { break-inside: avoid; }
```

Zwei Bauweisen, bewusst kombinieren:
- **`.page`-Blöcke** für gestaltete Einzelseiten (Cover, Kapitelauftakt, Arbeitsblatt, Abschluss) — exakte Kontrolle, kein Textfluss.
- **`.flow`-Bereiche** für längeren Fließtext — Chromium bricht selbst um.

## Build

`scripts/build_pdf.py` übernimmt:

```bash
python3 scripts/build_pdf.py \
  --cover cover.html \
  --body  body.html \
  --out   /mnt/user-data/outputs/ebook.pdf \
  --format A4 \
  --first-numbered-page 4 \
  --preview-dir preview/
```

Es rendert Cover ohne und Innenteil mit Seitenzahlen, führt beide mit pypdf zusammen, schreibt Titel/Autor/Stichworte in die PDF-Metadaten und legt PNG-Vorschauen aller Seiten ab.

## Nach dem Build immer

1. Vorschaubilder mit dem view-Tool **ansehen** — jede Seite, nicht stichprobenartig.
2. Seitenzahlen gegen das Inhaltsverzeichnis prüfen und Seitenzahlen im Verzeichnis korrigieren (ggf. zweiter Build).
3. Dateigröße prüfen: unter 15 MB bleiben. Bilder vorher auf 150 dpi und JPEG-Qualität 80 bringen:
   `mogrify -resize 1600x -quality 80 -format jpg bilder/*.png`
4. Links testen: Inhaltsverzeichnis-Anker und Shop-Links müssen klickbar sein (`<a href="#kap3">`, `<a href="https://...">`).
5. Text muss markierbar sein — wenn das PDF nur aus Bildern besteht, ist etwas schiefgelaufen.
