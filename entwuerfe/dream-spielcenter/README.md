# Entwurf Dream Spielcenter

Gestaltungsvorschlag (Demo) für dream-spielcenter.de. Noch kein Auftrag: kein
Briefing, keine Anzahlung. Wird es einer, zieht das Projekt nach
`ordeshop/orde-kunde-dream-spielcenter` um.

## Seiten

Start, Angebot, Standorte (mit Öffnungszeiten), Jobs (mit Bewerbung),
Spielerschutz, Kontakt, Impressum und Datenschutz (Platzhalter).

## Bauen

    python3 _bau/build.py      # Seiten aus _bau/seiten/ + Layout
    python3 _bau/vorschau.py   # dream-demo.html: alles in einer Datei, fürs Handy

Inhalte nur in `_bau/seiten/` ändern, Kopf und Fuß in `_bau/build.py`,
Öffnungszeiten in `STANDORTE` in `_bau/build.py`. Die HTML-Dateien im Ordner
werden überschrieben.

## Technik

GSAP 3.12.5, Tabler Icons 3.19.0, Barlow, Barlow Condensed und Lobster liegen
lokal unter `assets/`. Nichts wird von Google oder CDNs geladen (DSGVO).

## Offen (vom Betreiber)

- Original-Logo als Datei (jetzt SVG-Nachbau)
- Fotos: außen, innen, Geräte, Team
- alle Standorte mit Adresse und Zeiten (bekannt nur Kaufering, aus Branchenverzeichnis)
- Telefon, E-Mail, Betreiber laut Impressum, Social-Links
- echte offene Stellen (jetzt Beispiele)
- Altersgrenze 21 bestätigen, Ausstattung (Parken, Getränke, Klima, Nichtraucher)
- Impressum und Datenschutzerklärung (vom Betreiber, nicht von ORDÉ)
- Formulare sind Attrappen; für den Live-Gang Versand per PHP bauen
