# ORDÉ Vorlage für Kundenprojekte

Startgerüst für eine neue Kundenseite. Wird nicht direkt bearbeitet, sondern
für jedes Projekt einmal kopiert.

## Neues Kundenprojekt anlegen

1. Auf GitHub ein **privates** Repo anlegen: `orde-kunde-<name>`
   (kleingeschrieben, Bindestriche, zum Beispiel `orde-kunde-cafe-mork`)
2. Diese Vorlage hineinkopieren
3. `unterlagen/BRIEFING.md` ausfüllen — **zuerst**, bevor irgendetwas gebaut wird
4. Als Ausgangspunkt die Demo nehmen, die zur Branche passt, aus `orde-demos`

**Ein Repo pro Kunde.** Nicht mehrere Kunden in einem Repo. Zwei Gründe:
Am Ende wird laut AGB § 9 Abs. 4 alles übergeben, und mit einem eigenen Repo
ist das ein Knopfdruck. Und kein Kunde soll die Seiten der anderen sehen
können.

## Aufbau

```
build.py              erzeugt die Seite   (kommt aus dem passenden Projekt)
quelle/
  style.css           Aussehen — die Farben stehen ganz oben
  script.js           Menü, Animationen
  fonts/              Schriftdateien
  bilder/             was der Kunde geliefert hat
site/                 Ergebnis, nur das geht auf den Server
unterlagen/
  BRIEFING.md         alles zum Auftrag — Kontakt, Umfang, Ablauf, Betreuung
```

## Farben anpassen

In `quelle/style.css` stehen die Farben ganz oben unter `:root`. Für einen
neuen Kunden reicht es meistens, diese Werte zu ändern:

```css
--bg      Hintergrund
--ink     Textfarbe
--accent  Hauptfarbe, meist aus dem Logo
--accent-2 hellere Variante davon
```

## Was in ein Kundenrepo nicht gehört

- **Zugangsdaten.** Keine FTP-Passwörter, keine Hoster-Logins, keine
  Mailpasswörter. Auch nicht in `BRIEFING.md`. Die gehören in einen
  Passwortmanager, und für den Upload in die GitHub Secrets des Repos.
- Rechnungen und Zahlungsdaten des Kunden.
- Originaldateien, die der Kunde nur zur Ansicht geschickt hat.

## Rechtliches, das in jedem Projekt gilt

| Was | Wer |
|---|---|
| Impressum, Datenschutz, AGB, Widerruf | stellt der Kunde, wird unverändert eingebunden |
| Rechte an Texten und Bildern | sichert der Kunde zu (§ 7) |
| Hosting und Domain | bucht und zahlt der Kunde (§ 5) |
| Rechte am fertigen Code | gehen mit voller Zahlung an den Kunden über (§ 10) |
| Allgemeine Bausteine und Layoutteile | bleiben bei ORDÉ und dürfen wiederverwendet werden (§ 10 Abs. 2) |
| Referenznennung | erlaubt, solange der Kunde nicht widerspricht (§ 10 Abs. 4) |

Deshalb steht in dieser Vorlage nur Allgemeines. Alles, was speziell für
einen Kunden gebaut wird, bleibt in dessen Repo.

## Beim Abschluss

Nicht vergessen, sonst fehlt es später:

- [ ] Alle Dateien und Zugänge an den Kunden übergeben
- [ ] Den Kunden fragen, ob er als **Referenz** genannt werden darf — und
      wenn ja, einen Satz von ihm erbitten. Das ist der wertvollste Teil
      des ganzen Auftrags.
- [ ] Startdatum der zwölf Monate Betreuung in `BRIEFING.md` eintragen

## Verwandte Projekte

- **`orde-website`** — die eigene Website von ORDÉ
- **`orde-demos`** — die Beispielseiten, Ausgangspunkt für neue Projekte
