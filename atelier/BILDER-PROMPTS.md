# Bilder für LEINWERK erzeugen (Kling) — Anleitung & fertige Prompts

Die Website nutzt aktuell **graue Platzhalter**. Diese Datei enthält alles, um
sie durch echte, stimmige Bilder zu ersetzen — erzeugt mit **Kling
`text_to_image`** in einer **interaktiven** Claude-Code-Session (Terminal oder
Desktop-App), wo die Tool-Freigabe funktioniert (in der Web-/Remote-Session
wird jeder Kling-Aufruf leider mit „requires approval" blockiert).

> Kurzfassung: 16 Bilder erzeugen → herunterladen → mit dem beiliegenden
> Skript auf 4:5 bzw. 16:9 bringen und als `.webp` **und** `.jpg` in `images/`
> speichern → fertig. `products.js` ist unten schon passend vorbereitet.

---

## 1. Einstellungen für alle Bilder

- **Modell:** `gemini-3-pro-image` (Nano Banana Pro)
- **`img_resolution`:** `2k`
- **`aspect_ratio`:** `4:5` für Teile/Detail/Porträt, `16:9` für den Hero
- **`image_count`:** `1`
- **Wasserzeichen:** Bei manchen Konten liegt oben links ein „AI Generated"-
  Hinweis. In den Kling-Web-Einstellungen abschaltbar (danach ~30 s warten und
  das fertige Bild erneut abrufen).

Gemeinsamer Stil (steckt in jedem Prompt schon drin): weiches Tageslicht,
warm-neutraler Hintergrund (Knochen/Hafer), Naturleinen mit sichtbarer Textur
und natürlichen Falten, keine Personen/Gesichter, kein Text/Logo/Wasserzeichen,
ruhige Editorial-Produktfotografie.

In einer interaktiven Session genügt sinngemäß: „Erzeuge mit Kling
`text_to_image`, Modell `gemini-3-pro-image`, `img_resolution=2k`, das folgende
Bild … (Prompt einsetzen), `aspect_ratio=…`." Danach `query_tasks` pollen und
die Bild-URL herunterladen.

---

## 2. Die 16 Prompts → Zieldateien

| Zieldatei (ohne Endung) | aspect_ratio | Prompt |
|---|---|---|
| `images/hero` | 16:9 | Several natural linen garments — a dress, a blouse, wide trousers — hanging calmly and evenly spaced on a wooden clothing rail in a bright, airy atelier. Lots of negative space, soft diffused daylight from a side window, warm neutral bone and oat tones. Minimalist editorial fashion mood, natural linen with visible weave and gentle wrinkles. No people, no faces, no text, no logo, no watermark. |
| `images/portrait` | 4:5 | Close-up of a pair of hands hand-sewing natural linen fabric with needle and thread on a wooden atelier table. Wooden spools of thread, fabric scissors and a folded stack of linen nearby. Soft daylight, warm neutral bone and oat tones, calm handcraft mood, shallow depth of field. Only hands visible, no face, no text, no logo, no watermark. |
| `images/produkt-leinenkleid-oat` | 4:5 | Flat-lay of an oatmeal beige linen summer dress with cut-on short sleeves and a thin waist tie, neatly arranged on a bone-colored linen surface. Soft natural daylight, warm neutral palette, natural linen with visible weave and gentle wrinkles, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-hemdbluse-natur` | 4:5 | Undyed natural linen-cotton shirt blouse with mother-of-pearl buttons, hanging on a simple wooden hanger against a warm off-white plaster wall. Soft daylight, warm neutral palette, visible linen weave, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenrock-lehm` | 4:5 | Clay terracotta plant-dyed linen wrap skirt with deep pleats, flat-lay neatly arranged on a warm neutral bone linen background. Soft natural daylight, muted earthy palette, visible linen weave and gentle folds, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenjacke-stein` | 4:5 | Stone grey coarse linen unstructured summer jacket with patch pockets, on a wooden hanger against a warm neutral off-white wall. Soft daylight, muted palette, visible coarse linen texture, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenhose-asche` | 4:5 | Ash grey wide-leg linen palazzo trousers with a soft elastic waistband, neatly folded flat-lay on a bone linen surface. Soft natural daylight, warm neutral palette, visible linen weave, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenkleid-abend` | 4:5 | Long fine semi-sheer linen slip dress with thin straps in soft greige, hanging elegantly on a slim wooden hanger against a warm neutral wall. Soft daylight, delicate drape, muted palette, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-schuerzenkleid` | 4:5 | Heavy natural flax linen pinafore apron dress with a large front pocket and shoulder straps, on a wooden hanger against a warm neutral wall. Soft daylight, sturdy linen drill texture, muted palette, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenbluse-kragen` | 4:5 | Minimal natural beige linen blouse with a small stand-up collar and a half button placket, flat-lay neatly arranged on a warm neutral surface. Soft daylight, visible linen weave, muted palette, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinentop-traeger` | 4:5 | Short soft linen jersey camisole top with tie straps in warm cream, flat-lay on a bone linen surface. Soft natural daylight, warm neutral palette, soft fabric drape, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenmantel-lang` | 4:5 | Light knee-length open linen coat without closure in soft taupe, hanging on a wooden hanger against a warm neutral wall, falling in soft folds. Soft daylight, double-woven linen texture, muted palette, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenkleid-tunika` | 4:5 | Warm terracotta madder plant-dyed straight linen tunic dress with side slits, flat-lay neatly arranged on a warm neutral bone background. Soft natural daylight, earthy muted palette with subtle dye variation, visible linen weave, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/produkt-leinenschal` | 4:5 | Large fine natural flax linen scarf/wrap with a hand-rolled hem and a thin stripe at the ends, softly draped and folded flat on a warm neutral surface. Soft daylight, delicate airy linen, muted palette, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/detail-knopf` | 4:5 | Extreme close-up detail of mother-of-pearl buttons and a neat button placket on a natural linen blouse, soft daylight raking across the visible linen weave, warm neutral tones, shallow depth of field, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |
| `images/detail-saum` | 4:5 | Extreme close-up of a hand-rolled hem and fine even stitching on natural flax linen fabric, soft daylight, visible weave and thread detail, warm neutral tones, shallow depth of field, calm minimalist editorial product photography. No people, no text, no logo, no watermark. |

---

## 3. Bilder aufbereiten (WebP + JPG, richtige Maße)

Lege die von Kling heruntergeladenen Dateien in einen Ordner (z. B.
`roh/hero.png`, `roh/produkt-leinenkleid-oat.png`, …) und starte das
beiliegende Skript:

```bash
cd atelier
python3 -m pip install Pillow      # falls noch nicht vorhanden
python3 scripts/bilder-vorbereiten.py roh/
```

Das Skript beschneidet jedes Bild mittig auf das richtige Seitenverhältnis
(Hero 16:9 → 1600×900, alle anderen 4:5 → 800×1000) und schreibt je Bild
`images/<name>.webp` **und** `images/<name>.jpg`. Bestehende graue Platzhalter
werden dabei überschrieben.

---

## 4. `products.js` auf die neuen Bilder umstellen

`products.js` zeigt aktuell auf `images/placeholder-*`. Sobald die echten
Bilder liegen, die `bilder`-Zeilen so setzen (Detailbilder sorgen für die
Galerie mit Vorschau):

| Teil (`id`) | `bilder` |
|---|---|
| leinenkleid-oat | `["images/produkt-leinenkleid-oat", "images/detail-saum"]` |
| hemdbluse-natur | `["images/produkt-hemdbluse-natur", "images/detail-knopf"]` |
| leinenrock-lehm | `["images/produkt-leinenrock-lehm"]` |
| leinenjacke-stein | `["images/produkt-leinenjacke-stein"]` |
| leinenhose-asche | `["images/produkt-leinenhose-asche"]` |
| leinenkleid-abend | `["images/produkt-leinenkleid-abend"]` |
| schuerzenkleid | `["images/produkt-schuerzenkleid"]` |
| leinenbluse-kragen | `["images/produkt-leinenbluse-kragen", "images/detail-knopf"]` |
| leinentop-traeger | `["images/produkt-leinentop-traeger"]` |
| leinenmantel-lang | `["images/produkt-leinenmantel-lang"]` |
| leinenkleid-tunika | `["images/produkt-leinenkleid-tunika"]` |
| leinenschal | `["images/produkt-leinenschal", "images/detail-saum"]` |

`hero` und `portrait` behalten ihre Namen — nichts weiter zu ändern.

Danach die alten `images/placeholder-1..6.*` löschen. Fertig.
