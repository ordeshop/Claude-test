# ordeshop / Claude-test

Dieses Repository ist ein **Archiv**. Hier wird nicht mehr gearbeitet.

## Wo jetzt gearbeitet wird

Alles Aktuelle liegt in eigenen, privaten Repositories:

| Repo | Was drin ist |
|---|---|
| [`orde-website`](https://github.com/ordeshop/orde-website) | Die eigene Website von ORDÉ — ordeshop.net |
| [`orde-demos`](https://github.com/ordeshop/orde-demos) | Die sechs Beispielseiten, auf Deutsch |
| [`orde-vorlage`](https://github.com/ordeshop/orde-vorlage) | Startgerüst für Kundenprojekte |
| `orde-kunde-<name>` | Pro Kunde ein eigenes Repo, wird bei Auftragsbeginn angelegt |

## Was hier noch liegt und warum

### Das frühere Plugin „orde-design" (eingefroren)

Seit 25.10.2026 **kein Plugin mehr**. Alle Design-Werkzeuge liegen zentral in
`ordeshop/Business-Handbuch` → `werkzeuge/website/`, Video-Werkzeuge in
`werkzeuge/video/`. Was hier unter `plugins/orde-design/` liegt, ist ein alter
Stand und wird nicht mehr gepflegt (siehe `plugins/orde-design/EINGEFROREN.md`).
Kann gelöscht werden, sobald das Plugin im Account entfernt ist.

### Die alten englischen Demo-Seiten

`index.html` plus `cafe/`, `salon/`, `fitness/`, `komla/`, `atelier/` und die
Vorschaubilder in `assets/`.

Live über GitHub Pages: https://ordeshop.github.io/Claude-test/

**Nicht verschieben.** Die Bilder aus `assets/thumb-*.jpg` sind im
Shopify-Shop eingebunden, und die Demo-Adressen sind von außen verlinkt.
Ein Umzug macht das kaputt.

Ersetzt werden sie durch die deutschen Demos in `orde-demos`, die unter
`ordeshop.net/demos/` liegen. Sobald die neue Website live ist und der
Shopify-Shop nicht mehr gebraucht wird, können diese Seiten abgeschaltet
oder weitergeleitet werden. Dann kann auch dieses Repo umbenannt werden.

### Skill-Sicherung

`account-backup/` enthält die drei eigenen Skills (`orde-digital-shop`,
`ebook-design`, `ugc-ad-scripts`) samt ZIPs zum Hochladen und `UEBERGABE.md`
mit der Checkliste vom Account-Umzug im September 2026. Reines Archiv.

### Der Branch `demos-deutsch`

Enthält vier der alten Demos auf Deutsch. Wurde bewusst **nicht** nach `main`
übernommen: `index.html` und `atelier/` sind darin noch englisch, das ergäbe
eine halb deutsche Seite. Da die deutschen Demos jetzt in `orde-demos`
liegen, hat der Branch sich erledigt.

## Was hier nicht hingehört

Zugangsdaten. Keine FTP-Passwörter, keine Schlüssel, keine Tokens.
Das Repository ist **öffentlich** — alles hier kann jeder lesen.
