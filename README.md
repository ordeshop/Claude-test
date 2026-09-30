# ordeshop — Übersicht

Dieses Repository enthält drei getrennte Dinge. Sie haben nichts miteinander
zu tun und werden unabhängig voneinander geändert.

| Ordner | Was es ist | Status |
|---|---|---|
| [`website/`](website/) | **Die ORDÉ-Website.** Das aktuelle Projekt. | in Arbeit |
| `plugins/`, `.claude-plugin/` | Das Claude-Code-Plugin „orde-design" mit 34 Skills | fertig, wird genutzt |
| `account-backup/` | Sicherung der eigenen Skills beim Account-Umzug | Archiv |
| [`umzug-in-eigene-repos/`](umzug-in-eigene-repos/) | **Zwischenlager** — Demos und Kundenvorlage warten auf eigene Repos | zieht aus |
| `index.html`, `cafe/`, `salon/`, `fitness/`, `komla/`, `atelier/`, `assets/` | Die alten Demo-Seiten, noch auf Englisch | wird ersetzt |

## 1. Die ORDÉ-Website

**→ [`website/`](website/)** — dort steht eine eigene Anleitung.

Kurz: `cd website && python3 build.py`, dann den Inhalt von `website/site/`
per FTP hochladen. Gehostet wird bei Hostinger.

Das ist der Ordner, in dem gearbeitet wird.

Die Beispielseiten stecken **nicht** mehr darin — die liegen getrennt unter
`umzug-in-eigene-repos/orde-demos/` und landen auf dem Server unter `/demos/`.

## 2. Das Plugin „orde-design"

34 Claude-Code-Skills als ein Plugin. Installation:

```
/plugin marketplace add ordeshop/Claude-test
/plugin install orde-design@orde-skills
```

Alternativ global per Skript: `./install.sh`

**Nicht verschieben.** Die Datei `.claude-plugin/marketplace.json` verweist auf
den Pfad `./plugins/orde-design`. Wird der Ordner umbenannt, findet der
Marketplace das Plugin nicht mehr.

## 3. Skill-Sicherung

`account-backup/` enthält die drei eigenen Skills (`orde-digital-shop`,
`ebook-design`, `ugc-ad-scripts`) samt fertigen ZIPs zum Hochladen, dazu
`UEBERGABE.md` mit der Checkliste vom Account-Umzug im September 2026.

Reines Archiv. Wird nicht mehr geändert.

## 4. Die alten Demo-Seiten

`index.html` plus `cafe/`, `salon/`, `fitness/`, `komla/`, `atelier/` und die
Vorschaubilder in `assets/`.

Diese Seiten sind **live** über GitHub Pages:
https://ordeshop.github.io/Claude-test/

**Nicht verschieben und nicht umbenennen.** Die Adressen sind von außen
verlinkt, unter anderem sind die Bilder aus `assets/thumb-*.jpg` im
Shopify-Shop eingebunden. Ein Umzug macht diese Verweise kaputt.

Die neue Website bringt ihre eigenen Demos auf Deutsch mit, unter
`website/site/demos/`. Diese alten Seiten hier werden dadurch überflüssig.
Sobald die neue Seite live ist, können sie abgeschaltet oder auf die neue
Adresse weitergeleitet werden.

### Offener Punkt: der Branch `demos-deutsch`

Der Branch [`demos-deutsch`](../../tree/demos-deutsch) enthält vier der Demos
auf Deutsch (`cafe`, `fitness`, `komla`, `salon`). Er ist **bewusst nicht**
nach `main` übernommen, denn `index.html` und `atelier/` sind darin noch
englisch — zusammengeführt ergäbe das eine halb deutsche Seite.

Zwei Wege:

1. **Nichts tun.** Die Seiten werden ohnehin von der neuen Website ersetzt.
   Aufwand in diese alte Seite zu stecken, ist verlorene Zeit.
2. Die Übersetzung fertig machen, also auch `index.html` und `atelier/`,
   dann zusammenführen.

Weg 1 ist der vernünftige, solange die neue Website noch nicht live ist.

## Was in diesem Repository nichts zu suchen hat

Zugangsdaten. Keine FTP-Passwörter, keine API-Schlüssel, keine Tokens — auch
nicht in einer Beispieldatei. Solche Werte gehören unter
Settings → Secrets and variables → Actions.

Das Repository ist derzeit **öffentlich**. Alles, was hier liegt, kann jeder
lesen.
