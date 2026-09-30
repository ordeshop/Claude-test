# ORDÉ Website

Die Website von ORDÉ: Startseite, sechs Branchenseiten, Pakete und Preise,
Ablauf, Beispiele, Anfrageformular und alle Rechtsseiten.

Fest gebautes HTML — kein WordPress, kein Baukasten, keine Datenbank.

## Aufbau

```
website/
├── build.py          erzeugt die fertige Seite
├── quelle/           alles Handgemachte
│   ├── style.css     das Aussehen
│   ├── script.js     Menü, Animationen, Intro
│   ├── fonts/        Schriftdateien (fehlen noch, siehe unten)
│   ├── demos/        die sechs Beispielseiten
│   ├── vorschau/     Screenshots der Demos für die Startseite
│   └── marke/        Logo, Favicons, Teilen-Bild
├── site/             ERGEBNIS — nur dieser Ordner geht auf den Server
└── unterlagen/       Notizen, die nicht online gehören
    ├── SCHRIFTEN.md
    ├── AGB-ENTWURF.md
    └── DATENSCHUTZ-ENTWURF.md
```

## Etwas ändern

```bash
cd website
python3 build.py
```

Das ist alles. Der Befehl schreibt die HTML-Seiten neu, kopiert alles aus
`quelle/` an die richtige Stelle und erzeugt `sitemap.xml` und `robots.txt`.

**Der Ordner `site/` ist wegwerfbar.** Er lässt sich jederzeit vollständig aus
`quelle/` und `build.py` neu erzeugen. Man kann ihn löschen und einmal bauen.

Wo man was ändert:

| Was | Wo |
|---|---|
| Texte, Preise, neue Seiten | `build.py` |
| Aussehen, Farben, Schriftgrößen | `quelle/style.css` |
| Menü, Animationen, Intro | `quelle/script.js` |
| Eine Demo | `quelle/demos/<name>/` |
| Logo, Favicon | `quelle/marke/` |

Nie in `site/` bearbeiten — das wird beim nächsten Durchlauf überschrieben.

Ändert sich eine Demo, müssen die Vorschaubilder unter `quelle/vorschau/` neu
erzeugt werden — sonst zeigt die Startseite noch den alten Stand.

## Online stellen

Gehostet wird bei **Hostinger**. Hochgeladen wird per FTP der **Inhalt von
`site/`** in das Web-Verzeichnis (bei Hostinger meist `public_html`).

Nicht den Ordner `site` selbst hochladen, sondern was darin liegt.

Sobald die FTP-Zugangsdaten als GitHub Secrets hinterlegt sind, macht das die
Automatik unter `.github/workflows/` im Repo-Wurzelverzeichnis von selbst:

- `FTP_SERVER` — Serveradresse von Hostinger
- `FTP_USERNAME`
- `FTP_PASSWORD`

Zu finden unter Settings → Secrets and variables → Actions.

**Zugangsdaten gehören niemals in eine Datei im Repository.**

Niemals direkt auf dem Server ändern. Sonst wird die Änderung beim nächsten
Durchlauf überschrieben.

## Das Anfrageformular

`site/kontakt.php` nimmt das Formular entgegen und schickt es als Mail an
`hello@ordeshop.net`. Auf dem Server wird nichts gespeichert.

- Absender ist `formular@ordeshop.net` — dieses Postfach muss bei Hostinger
  angelegt sein, sonst landet die Mail im Spam oder kommt gar nicht an.
- **Reply-To** ist die Adresse des Kunden, ein einfaches „Antworten" genügt also.
- Spamschutz ist ein unsichtbares Feld (`website_url`). Bots füllen es aus,
  Menschen nicht. Wer es ausfüllt, sieht die Danke-Seite, aber es geht keine
  Mail raus.
- Geht etwas schief, landet der Besucher auf `anfrage.html?fehler=1` und sieht
  dort einen Hinweis mit der direkten Mailadresse.
- PHP läuft nur auf dem Server, **nicht** beim lokalen Öffnen der Datei und
  nicht in einer Vorschau. Getestet wird nach dem Hochladen.

## Rechtsseiten

| Seite | Stand |
|---|---|
| `impressum.html` | fertig |
| `widerruf.html` | fertig, mit Muster-Widerrufsformular |
| `datenschutz.html` | Text steht, Hostinger ist als Auftragsverarbeiter genannt |
| `agb.html` | Text steht, **juristisch noch nicht geprüft** |

Die AGB lassen sich über `AGB_ONLINE = False` in `build.py` wieder abschalten,
bis die IHK-Erstberatung durch ist. Die offenen Punkte für den Termin stehen in
`unterlagen/AGB-ENTWURF.md`.

Die Datenschutzerklärung behauptet, dass ein Auftragsverarbeitungsvertrag nach
Art. 28 DSGVO mit Hostinger besteht. Der muss im Hostinger-Kundenkonto
abgeschlossen sein, **bevor** die Seite live geht — sonst steht dort eine
Unwahrheit.

## Noch offen

- [ ] **Hosting bei Hostinger buchen** — dabei **EU-Rechenzentrum** wählen
- [ ] **AV-Vertrag** nach Art. 28 DSGVO im Hostinger-Kundenkonto abschließen
- [ ] **Postfach `formular@ordeshop.net`** anlegen
- [ ] **Schriftdateien** herunterladen, siehe `unterlagen/SCHRIFTEN.md`
- [ ] **Domain** auf den Hoster zeigen lassen
- [ ] **Formular live testen**, sobald die Seite auf dem Server liegt
- [ ] **Über mich** — die zwei bis drei persönlichen Sätze in `build.py` ergänzen
- [ ] **IHK-Erstberatung** zu den AGB
- [ ] Nach dem Live-Gang: Sitemap in der Google Search Console anmelden
- [ ] **Erste echte Referenz** — der größte Unterschied zur Konkurrenz
