# Übergabe: Umzug auf einen neuen Claude-Account

Stand: 24.09.2026. Dieses Dokument sammelt alles, was du brauchst, um auf einem
neuen Claude-Account dort weiterzuarbeiten, wo wir aufgehört haben.

## 1. Was schon sicher ist (liegt auf GitHub, nicht im Claude-Account)

Das Repo `ordeshop/Claude-test` gehört deinem **GitHub**-Konto, nicht dem
Claude-Account. Beim Wechsel geht davon nichts verloren:

| Was | Wo |
|---|---|
| Showcase-Startseite | `index.html` → https://ordeshop.github.io/Claude-test/ |
| LEINWERK (Schneiderin-Lookbook) | `atelier/` (inkl. `CLAUDE.md` mit Lehren + offenen Punkten) |
| Studio Nové (Salon) | `salon/` |
| MØRK (Café, mehrseitig) | `cafe/` |
| FORGE (Fitness) | `fitness/` |
| KOMLA (Fotograf) | `komla/` |
| Thumbnails für Shopify-Einbettung | `assets/thumb-*.jpg` |
| Plugin „orde-design“ (60+ Skills) | `plugins/orde-design/`, Installation siehe `README.md` |
| Auto-Sync `main` → `mode` | `.github/workflows/sync-mode.yml` |

Auch der **Shopify-Shop** (ordeshop.net, inkl. `/pages/web-design` und den
Branchenseiten `/pages/website-<branche>`) hängt an deinem Shopify-Konto, nicht an Claude.

## 2. Was NUR im alten Claude-Account lag – jetzt hier gesichert

Deine **drei eigenen Skills** liegen jetzt in diesem Ordner:

- `skills/orde-digital-shop/`: ORDÉ als Digital-Products-Store (Listings, Preise, Recht)
- `skills/ebook-design/`: verkaufsfertige Ebooks als PDF
- `skills/ugc-ad-scripts/`: UGC-/TikTok-Skripte mit Kling-Prompts

Zum Hochladen gibt es fertige ZIPs unter `zips/`.

## 3. Checkliste für den neuen Account

1. **GitHub verbinden:** claude.ai → Einstellungen → Connectors → GitHub, dann
   die Claude-GitHub-App für `ordeshop/Claude-test` erlauben.
2. **Skills hochladen:** claude.ai → Einstellungen → Capabilities/Skills →
   „Skill hochladen“ → nacheinander die drei ZIPs aus `account-backup/zips/`.
3. **Connectors neu verbinden** (jeweils einmal einloggen):
   Shopify (ordeshop.net), Notion, Gmail, Kling. Die Logins selbst sind
   nicht übertragbar, das musst du einmal selbst machen.
4. **Claude-Code-Umgebung** (claude.ai/code) neu anlegen: Repo `ordeshop/Claude-test`
   wählen und dieselbe Netzwerk-Einstellung wie bisher nehmen.
5. **Plugin optional** in Claude Code installieren:
   `/plugin marketplace add ordeshop/Claude-test` und dann
   `/plugin install orde-design@orde-skills`.
6. **Erste Nachricht im neuen Account**, damit Claude sofort im Bild ist:
   > Lies `account-backup/UEBERGABE.md` und `atelier/CLAUDE.md` im Repo
   > ordeshop/Claude-test, dann machen wir weiter.

## 4. Was NICHT mitkommt

- **Chat-Verläufe:** Wenn du alte Chats behalten willst, exportiere sie im alten
  Account unter Einstellungen → Datenschutz → „Daten exportieren“. Die wichtigen
  Erkenntnisse stehen aber schon in `atelier/CLAUDE.md`.
- **Claude-Memory/Projekte** im alten Account: bei Bedarf dort exportieren und im
  neuen Account über den Skill „import-memory“ einspielen.
- **Artifacts** (veröffentlichte claude.ai-Seiten) bleiben im alten Account.
- **Kling-Credits/Abo, Claude-Abo:** sind an das jeweilige Konto gebunden.

## 5. Wo wir aufgehört haben / offen

- LEINWERK: `WEB3FORMS_KEY` und WhatsApp-Nummer in `atelier/app.js` sowie Instagram
  und E-Mail in `atelier/index.html` sind noch Platzhalter, die der Kunde füllen muss
  (siehe `atelier/CLAUDE.md`).
- Neue Demo nach Muster: (a) Ordner + Showcase-Card im Repo, (b) Card auf
  Shopify `/pages/web-design`, (c) eigene Branchenseite `/pages/website-<branche>`.
- Der alte Branch `claude/lookbook-website-schneiderin-gupuhl` ist veraltet: alles
  daraus steckt schon in `main` und er kann gelöscht werden.
