# Gestaltung: Format, Raster, Typografie, Farbe

Inhalt:
1. Format wählen
2. Satzspiegel und Raster
3. Typografie
4. Farbe
5. Bild- und Grafiksprache
6. Wiederkehrende Elemente
7. Fertige Gestaltungsrichtungen

---

## 1. Format wählen

| Nutzung | Format | Maße | Hinweis |
|---|---|---|---|
| Am Laptop/Tablet gelesen | 16:10 quer | 1600 × 1000 px (≈ 423 × 264 mm bei 96 dpi) | Wirkt modern, keine Zoomerei, sehr gut für viel Weißraum und Grafik |
| Klassischer Ratgeber, evtl. ausgedruckt | A4 hoch | 210 × 297 mm | Sicherste Wahl im deutschen Markt |
| Workbook, Arbeitsblätter, Checklisten | A4 hoch | 210 × 297 mm | Pflicht — Leute drucken das aus |
| Buchhaft, edel | 6 × 9 in | 152 × 229 mm | Wirkt wie ein echtes Buch, wenig Text pro Seite |

Ein Format pro Produkt. Keine gemischten Seitengrößen im selben PDF.

## 2. Satzspiegel und Raster

**A4 hoch:**
- Rand außen 22 mm, innen 22 mm, oben 20 mm, unten 22 mm
- Textspalte dadurch ~166 mm — bei 11 pt sind das ca. 80 Zeichen, also eher zu breit. Lösung: Textspalte auf 118–130 mm begrenzen und die restlichen ~40 mm als Marginalspalte für Randnotizen, kleine Hinweise, Kapitelmarken oder einfach als Luft.
- Grundlinienraster: alle Abstände als Vielfaches von 6 pt oder 8 pt. Das ist der unauffälligste Grund, warum professionelle Seiten ruhig wirken.

**16:10 quer:**
- Rand 60–80 px rundum bei 1600 px Breite
- Zweispaltig arbeiten oder Text auf maximal 55 % der Breite setzen, Rest Bild/Weißraum
- Eine Idee pro Seite. Querformat verführt zum Vollstopfen — widerstehen.

**12-Spalten-Denken:** Auch ohne Framework hilft es, die Fläche gedanklich in 12 Spalten zu teilen und Elemente an Spaltenkanten auszurichten. Nichts steht "ungefähr" irgendwo.

## 3. Typografie

**Größen (A4, Bildschirmlesung):**

| Element | Größe | Zeilenhöhe |
|---|---|---|
| Fließtext | 10,5–12 pt | 1,5–1,6 |
| Zwischenüberschrift (H3) | 13–15 pt | 1,3 |
| Kapitelüberschrift (H2) | 20–26 pt | 1,15 |
| Kapitelnummer auf Auftaktseite | 60–120 pt | — |
| Bildunterschrift, Marginalie | 8–9 pt | 1,4 |
| Kolumnentitel/Seitenzahl | 8 pt | — |

Im Querformat (1600 px) alles in px denken: Fließtext 19–22 px, H2 40–56 px, Kapitelnummer 140–220 px.

**Skala:** Nutze eine feste Stufenfolge (z. B. Faktor 1,25 oder 1,333) statt willkürlicher Größen. Vier bis fünf Stufen reichen für ein ganzes Buch.

**Schriftpaarungen** (alle über npm `@fontsource/...` verfügbar):

| Richtung | Überschrift | Fließtext |
|---|---|---|
| Redaktionell, warm | Fraunces oder Playfair Display | Source Sans 3 oder Inter |
| Klar, modern | Space Grotesk oder Sora | Inter oder IBM Plex Sans |
| Buchhaft, ruhig | Cormorant Garamond | EB Garamond oder Lora |
| Kraftvoll, direkt | Archivo Black oder Anton | Work Sans |
| Technisch, sachlich | IBM Plex Sans (Bold) | IBM Plex Serif |

Regeln: Fließtext nie unter 400er Schnitt, nie in Versalien über mehr als drei Wörter, Laufweite bei großen Überschriften leicht negativ (−0,02 em), bei kleinen Versalien-Labels positiv (+0,08 em).

**Deutsch:** Silbentrennung ist Pflicht bei Blocksatz (`lang="de"` + `hyphens: auto` — vorher testen, ob Chromium im Container die Trennmuster hat; wenn nicht, Flattersatz). Lange Komposita brechen Überschriften unschön — Überschriften manuell mit `&shy;` oder Zeilenumbruch steuern.

## 4. Farbe

Aufbau einer Palette:
- 1 Hintergrund (nie #FFFFFF — z. B. #FAF8F4, #F7F6F3, #FDFCFA)
- 1 Textfarbe (nie #000000 — z. B. #1A1A18, #22201C)
- 1 Akzent (Kapitelnummern, Linien, Callout-Rahmen, Hervorhebungen)
- 1 gedämpfte Sekundärfarbe für Flächen (z. B. Akzent auf 10–15 % Deckkraft)

Bewährte Kombinationen:
- Terrakotta #C4633F auf Creme #FAF6F0, Text #241F1B
- Tiefgrün #1F3D31 auf Warmweiß #F7F5EF, Akzent Messing #B08D4F
- Tinte #16213A auf Papierweiß #F8F8F5, Akzent Koralle #E2614A
- Anthrazit #232323 auf Off-White #F4F4F2, Akzent Limette #C8E24A (für technische Themen)

Kontrast prüfen: Fließtext mindestens 7:1 gegen den Hintergrund. Akzentfarbe nie für längeren Fließtext.

Farbige Vollflächen sparsam einsetzen — eine farbige Kapitelauftaktseite wirkt stark, zehn wirken laut.

## 5. Bild- und Grafiksprache

Reihenfolge der Präferenz:
1. **Eigene Fotos** (bei Produkt-Ebooks fast immer die stärkste Option)
2. **Selbst gebaute Grafiken**: Diagramme, Ablaufskizzen, Vorher/Nachher, Vergleichstabellen — als SVG direkt im HTML, in Akzentfarbe
3. **Typografische Seiten**: ein großes Zitat, eine große Zahl, ein Kapitelwort als Bildfläche
4. **Abstrakte Flächen und Formen**: Kreissegmente, Raster, Linien in Akzentfarbe

Vermeide generische Stockfotos. Wenn Fotos verwendet werden: einheitlich behandeln (gleicher Farbstich, gleiche Sättigung, gerne Duotone in der Akzentfarbe), immer randabfallend oder exakt auf dem Raster — nie "ungefähr eingefügt".

Nur lizenzfreie oder eigene Bilder verwenden und die Herkunft dokumentieren. Bei Verkaufsprodukten ist die Lizenz relevant, nicht optional.

## 6. Wiederkehrende Elemente

Definiere diese einmal und benutze sie konsequent:

- **Callout / Merkkasten**: farbige Fläche oder linker Balken in Akzentfarbe, Label in Versalien ("MERKE", "FEHLER", "PROFI-TIPP")
- **Checkliste**: leere Kästchen ☐ als gezeichnetes Quadrat, nicht als Unicode-Zeichen
- **Zitat/Kernaussage**: große Schrift, viel Weißraum, ohne Anführungszeichen-Grafikkitsch
- **Tabellen**: keine vollen Gitternetze, nur horizontale Haarlinien, Kopfzeile in Versalien-Klein
- **Aufgabenfeld** (Workbook): Linien oder gepunktete Fläche zum Beschreiben, mindestens 30 mm hoch
- **Kolumnentitel**: Kapitelname klein außen oder unten, Seitenzahl gegenüber
- **Kapitelauftakt**: große Nummer, Kapiteltitel, ein Satz worum es geht, viel Leerraum

Cover, Titel, Impressum und Inhaltsverzeichnis bekommen keine Seitenzahl.

## 7. Fertige Gestaltungsrichtungen

Wenn keine Marke vorgegeben ist, wähle eine davon und halte sie durch:

**Editorial Calm** — Fraunces + Source Sans, Creme/Terrakotta, breite Ränder, Marginalspalte, große Kapitelzahlen. Passt für Ratgeber, Lifestyle, Food, Achtsamkeit.

**Studio Grid** — Space Grotesk + Inter, Off-White/Anthrazit/Limette, striktes Raster, Linien als Gestaltungsmittel, kleine Versalien-Labels. Passt für Business, Technik, E-Commerce, Marketing.

**Quiet Book** — Cormorant + EB Garamond, Papierweiß/Tinte, sehr viel Weißraum, kaum Farbe, alles über Typografie. Passt für Essays, Persönlichkeitsthemen, Premium-Positionierung.

**Bold Practical** — Archivo Black + Work Sans, Weiß/Schwarz/eine laute Akzentfarbe, große Zahlen, klare Kästen. Passt für Workbooks, Challenges, Schritt-für-Schritt-Systeme.

Dokumentiere die getroffene Wahl (Schriften, Hex-Werte, Größenskala) am Ende in einer kurzen `stilrichtlinie.md`, damit das nächste Produkt derselben Reihe identisch aussieht.
