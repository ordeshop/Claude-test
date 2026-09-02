# LEINWERK — Projektnotizen & gelernte Fehler

Statische Lookbook-Website (kein Shop) unter `atelier/`. Reines HTML/CSS/Vanilla-JS,
kein Build-Step. Bilder als WebP + JPG (4:5, Hero 16:9), Fonts lokal (DSGVO).

## Gelernte Fehler — bitte NICHT wiederholen

### 1. `<img>`-Attribute `width`/`height` heben CSS `aspect-ratio` aus
**Symptom:** Beim Klick auf ein Produkt wurde das Lightbox-Bild verzerrt/zu hoch
(gemessen 493×1000 statt 493×617) und Thumbnails rutschten aus dem Sichtfeld.
Gleiches Problem beim „Über mich"-Porträt.
**Ursache:** Das `<img>` hat feste Attribute `width="800" height="1000"` (gut gegen
Layout-Shift). Wenn die CSS-Regel nur `width:100%; aspect-ratio:4/5` setzt, aber
**kein `height`**, gewinnt das HTML-`height`-Attribut → `aspect-ratio` wird ignoriert.
**Regel:** Bei jedem `img` mit `width`/`height`-Attributen, das per CSS skaliert wird,
**immer `height:auto`** setzen (dann rechnet `aspect-ratio` die Höhe aus der Breite).
Betroffen waren `.lb-gallery img` und `.about-photo img`. Kartenbilder waren ok, weil
`.card-media img` `height:100%` in einer Box mit fixer `aspect-ratio` nutzt.

### 2. Helle Vollbild-Hero-Fotos → Text unsichtbar (Weiß-auf-Weiß)
**Symptom:** Cremefarbene Hero-Schrift verschwand auf dem hellen Leinen-Foto; die
letzte Textzeile rutschte sogar unter das Bild auf den hellen Seitenhintergrund
(creme auf creme).
**Ursache:** Hero-Bild mit fester Höhe, Text absolut positioniert konnte überlaufen;
Verlauf/Schatten zu schwach für ein sehr helles Foto.
**Regel für helle Vollbild-Medien mit Text darüber:**
- Bild **absolut** den ganzen Hero füllen lassen (`position:absolute; inset:0;
  height:100%`), Hero-Höhe über die Text-Box (`min-height`) steuern — Text kann so
  nie unter das Bild rutschen.
- Kräftiger Verlauf unten (bis ~0.75 Deckkraft) **und** Textschatten in zwei Lagen
  (scharf + weich), damit Text auf hellen Stellen sicher lesbar bleibt.
- Kontrast immer gegen den hellsten Bildbereich prüfen, nicht nur gegen den Verlauf.

## Verifikations-Routine nach Bild-/Layout-Änderungen
Nicht nur „Bild geladen" prüfen, sondern **gerenderte Maße messen** (Playwright,
`getBoundingClientRect`): 4:5-Bilder müssen w:h ≈ 4:5 haben. Immer auch die
**Lightbox öffnen** und Desktop **und** Mobile sichten.

## Bild-Workflow
- Rohbilder → `scripts/bilder-vorbereiten.py <ordner>` erzeugt WebP+JPG in korrekter
  Größe (Hero 16:9 = 1600×900, Rest 4:5 = 800×1000).
- `products.js` referenziert Bilder **ohne Endung** (`images/name`); `app.js` baut
  `<picture>` mit `.webp` + `.jpg`-Fallback.
- Kling-Prompts für Regenerierung liegen in `BILDER-PROMPTS.md`.

## Noch offen (Platzhalter, vom Kunden zu füllen)
`WEB3FORMS_KEY` + WhatsApp-Nummer in `app.js`; Instagram/E-Mail in `index.html`;
Rechtstexte in impressum/datenschutz/widerruf/agb.html (juristisch prüfen lassen).
