# Schriften selbst hosten — Anleitung

Die Website lädt **keine** Schriften mehr von Google. Damit ist das
Datenschutzproblem (IP-Übertragung an Google) erledigt.

Bis du die Schriftdateien eingelegt hast, zeigt die Seite die
Systemschrift. Sie funktioniert, sieht aber schlichter aus.

## Die vier Dateien holen

Gehe auf **gwfh.mranftl.com** (Google Webfonts Helper). Dort brauchst du
kein Konto und lädst die Dateien direkt herunter.

Für jede Schrift:
1. Schrift oben suchen
2. Bei "Select charsets" **latin** und **latin-ext** anhaken
3. Bei "Select styles" **regular** (400), **medium/semibold** (500/600)
   und **bold** (700) anhaken
4. Unten auf "Download files" klicken

Diese vier brauchst du:

| Schrift | wofür |
|---|---|
| Fraunces | Überschriften auf der ganzen Seite |
| Inter | Fließtext auf der Hauptseite |
| Hanken Grotesk | Fließtext in den Demos Café, Salon, Fitness |
| Bricolage Grotesque | Demo Fotograf (KOMLA) |

## Dateien einlegen und umbenennen

Aus dem Download nimmst du jeweils die **.woff2**-Datei, legst sie in den
Ordner `assets/fonts/` und benennst sie so um:

```
assets/fonts/fraunces-variable.woff2
assets/fonts/inter-variable.woff2
assets/fonts/hanken-grotesk-variable.woff2
assets/fonts/bricolage-grotesque-variable.woff2
```

Die Namen müssen genau so lauten, sonst findet `fonts.css` sie nicht.

Falls der Download mehrere Dateien je Schrift enthält (400, 500, 700),
nimm die 400er-Datei für den Namen oben. Für den Anfang reicht das; wenn
du es genauer willst, sag Bescheid, dann schreibe ich `fonts.css` auf die
einzelnen Schnitte um.

## Prüfen, ob es geklappt hat

Seite im Browser öffnen, Rechtsklick → Untersuchen → Reiter "Netzwerk",
dann neu laden. Es darf **kein** Eintrag mit `fonts.googleapis.com` oder
`fonts.gstatic.com` auftauchen.
