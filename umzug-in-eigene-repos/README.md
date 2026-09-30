# Zwischenlager — diese zwei Projekte ziehen aus

Hier liegen zwei fertige Projekte, die **eigene Repositories bekommen sollen**.
Sie liegen nur so lange hier, bis die Repos angelegt sind — damit die Arbeit
nicht verloren geht.

| Ordner | Zielrepo | Was es ist |
|---|---|---|
| `orde-demos/` | `orde-demos` (privat) | die sechs Beispielseiten samt Vorschaubildern |
| `orde-vorlage/` | `orde-vorlage` (privat) | Startgerüst für Kundenprojekte |

## Was zu tun ist

1. Auf github.com/new zwei **private, leere** Repos anlegen: `orde-demos` und
   `orde-vorlage` — kein README, keine .gitignore, keine Lizenz ankreuzen
2. Den jeweiligen Ordner in sein Repo schieben
3. Diesen Ordner `umzug-in-eigene-repos/` hier löschen

## Warum die Workflow-Dateien `.wartet` heißen

GitHub führt jede Datei unter `.github/workflows/` aus, egal in welchem
Unterordner sie liegt. Damit diese zwei Uploads nicht schon hier aus dem
falschen Repo loslaufen, ist die Endung vorübergehend auf `.yml.wartet`
geändert.

**Beim Umzug zurückbenennen** auf `.yml`, sonst passiert im neuen Repo nichts:

```
orde-demos/.github/workflows/demos-hochladen.yml.wartet  →  .yml
orde-vorlage/.github/workflows/seite-hochladen.yml.wartet →  .yml
```
