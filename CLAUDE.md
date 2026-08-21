# Projekt-Gedächtnis (CLAUDE.md)

Diese Datei wird zu Beginn jeder Session automatisch geladen. Hier stehen
dauerhafte Anweisungen des Nutzers.

## Websites: immer einen eigenen Ordner anlegen

**Jedes Mal, wenn eine neue Website gebaut wird, MUSS dafür ein eigener Ordner
in den Dateien des Nutzers (in diesem Repo) angelegt werden.** Nicht nur ein
loses HTML-Artifact — die Website bekommt einen echten, dauerhaften Projektordner.

Konvention:

```
websites/<website-slug>/
  index.html        # die Seite (self-contained, oder mit Assets)
  images/           # alle Bilder/Assets der Seite
  README.md         # kurz: worum geht's, Stil, Stand, ggf. Deploy-Hinweise
```

Regeln:
- `<website-slug>` = kurzer Kleinbuchstaben-Name mit Bindestrichen (z. B. `ember-and-oak`).
- Bilder liegen als echte Dateien in `images/` (nicht nur inline), damit der
  Ordner **deploy-fertig** ist (Netlify/Vercel: Ordner hochladen → live).
- Für die schnelle Vorschau darf zusätzlich ein Artifact veröffentlicht werden;
  der Ordner im Repo bleibt aber die „Quelle der Wahrheit".
- Am Ende committen und pushen, damit die Website dauerhaft in den Dateien liegt.

## Kontext

- Der Nutzer betreibt **ORDÉ** (ordeshop.net), einen weltweiten Digital-Products-Store.
- Dieses Repo bündelt außerdem die Claude-Skills als Plugin `orde-design`
  (Marketplace `orde-skills`).
