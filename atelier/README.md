# LEINWERK — Lookbook-Website

Eine ruhige, statische Lookbook-Website für handgemachte Kleidung.
**Kein Onlineshop:** Kundinnen sehen die Teile und stellen eine unverbindliche
Anfrage (Formular + WhatsApp). Reines HTML/CSS/JavaScript, kein Build-Schritt,
direkt bei **Netlify** oder **Cloudflare Pages** hochladbar.

> Alle Namen, Texte, Bilder und Kontaktdaten sind **Platzhalter** und leicht
> austauschbar. Suche im Zweifel nach `[` (eckige Klammern) und `PLATZHALTER`/
> `XXXX`, um alle offenen Stellen zu finden.

---

## Ordnerinhalt

```
atelier/
├─ index.html        ← die Website (One-Pager)
├─ impressum.html    ┐
├─ datenschutz.html  │  Rechtsseiten (Platzhaltertext, bitte anpassen/prüfen)
├─ widerruf.html     │
├─ agb.html          ┘
├─ styles.css        ← Design (Farben, Schriften, Layout)
├─ products.js       ← DEINE TEILE  ← hier pflegst du die Kollektion
├─ app.js            ← Technik (Anfrage-Formular, Detailansicht)
├─ fonts/            ← Schriften, lokal gespeichert (DSGVO)
├─ images/           ← Bilder (aktuell graue Platzhalter im Format 4:5)
└─ README.md         ← diese Anleitung
```

---

## Ein neues Teil eintragen (Datei `products.js`)

1. Öffne **`products.js`** in einem einfachen Texteditor (z. B. TextEdit,
   Editor, VS Code).
2. Kopiere einen bestehenden Block — alles von `{` bis `},` — und füge ihn
   direkt darunter wieder ein.
3. Passe die Werte an. Ein Teil sieht so aus:

   ```js
   {
     id: "leinenkleid-oat",
     titel: "Leinenkleid „Hafer“",
     bilder: ["images/placeholder-1", "images/placeholder-4"],
     preis: 189,
     groesse: "36 / S",
     material: "100 % Leinen, vorgewaschen",
     beschreibung: "Ein bis drei Sätze über das Teil.",
     pflege: "30 °C Feinwäsche, liegend trocknen.",
     status: "verfügbar",
   },
   ```

### Die Felder

| Feld           | Bedeutung |
|----------------|-----------|
| `id`           | Eindeutige Kennung, klein und ohne Leerzeichen (z. B. `sommerrock-2`). |
| `titel`        | Name des Teils. |
| `bilder`       | Liste von Bildern **ohne Dateiendung** (siehe unten). Das erste Bild ist das Titelbild. |
| `preis`        | Zahl in Euro, **ohne** €-Zeichen (z. B. `189`). Wird als Endpreis angezeigt. |
| `groesse`      | z. B. `"38 / M"` oder `"Maßanfertigung"`. |
| `material`     | z. B. `"100 % Leinen, vorgewaschen"`. |
| `beschreibung` | Ein bis drei Sätze. |
| `pflege`       | Pflegehinweis. |
| `status`       | `"verfügbar"`, `"verkauft"` oder `"auf Anfrage"`. |

**Wichtig:** Texte immer in `"Anführungszeichen"`, und am Ende jeder Zeile das
Komma nicht vergessen. Nach dem letzten `}` in der Liste steht ebenfalls ein
Komma — das ist in Ordnung.

Ein **verkauftes** Teil (`status: "verkauft"`) bleibt sichtbar, wird aber
ausgegraut und bekommt automatisch das Badge „Verkauft“.

---

## Bilder ersetzen (Ordner `images/`)

Die Bilder sind aktuell **graue Platzhalter**. So tauschst du sie gegen echte
Fotos:

1. Lege deine Fotos im **Format 4:5** an (Hochformat, z. B. 800 × 1000 Pixel).
   Das feste Format verhindert „springende“ Layouts beim Laden.
2. Speichere jedes Foto **zweimal** in den Ordner `images/`:
   - einmal als **`.webp`** (klein und schnell) und
   - einmal als **`.jpg`** (Sicherheits-Fallback für ältere Browser).

   Beispiel: `leinenkleid.webp` **und** `leinenkleid.jpg`.

   > Kein WebP zur Hand? Es reicht auch, nur die `.jpg`-Datei bereitzustellen —
   > die Seite zeigt dann automatisch das JPG.

3. Trage in `products.js` unter `bilder` den Pfad **ohne Endung** ein:

   ```js
   bilder: ["images/leinenkleid"],
   ```

   Für mehrere Fotos eines Teils einfach mehrere Namen angeben — sie erscheinen
   als kleine Vorschaubilder in der Detailansicht:

   ```js
   bilder: ["images/leinenkleid-vorne", "images/leinenkleid-detail"],
   ```

4. **Hero-Foto** (großes Bild ganz oben) und **Porträtfoto** heißen fest
   `hero` bzw. `portrait`. Ersetze `images/hero.jpg` / `images/hero.webp` und
   `images/portrait.jpg` / `images/portrait.webp` durch deine eigenen Fotos
   (Hero gern im Querformat, Porträt im 4:5-Hochformat).

Denk an **aussagekräftige Alt-Texte**? Die Produkt-Alt-Texte werden automatisch
aus dem Titel erzeugt. Hero- und Porträt-Alt-Text stehen in `index.html`
(Attribut `alt="…"`) und dürfen angepasst werden.

---

## Kontaktdaten & Anfrage-Versand einrichten

Damit Anfragen bei dir ankommen, müssen ein paar Platzhalter ersetzt werden:

### 1. Formular-Versand (Web3Forms) — Datei `app.js`, ganz oben
- Erstelle einen kostenlosen Access Key auf **web3forms.com** (nur deine
  E-Mail-Adresse nötig).
- Ersetze in `app.js`:
  ```js
  var WEB3FORMS_KEY = "WEB3FORMS_KEY";   // ← hier deinen Key eintragen
  ```
- Ohne gültigen Key wird das Formular abgeschickt, aber Web3Forms lehnt es ab;
  die Website zeigt dann eine freundliche Fehlermeldung mit Hinweis auf
  E-Mail/WhatsApp.

### 2. WhatsApp-Nummer — Datei `app.js` **und** `index.html`
- In `app.js`:
  ```js
  var WHATSAPP_NUMBER = "49XXXXXXXXXX";  // Ländervorwahl ohne + und ohne Leerzeichen
  ```
  Beispiel für eine deutsche Nummer `0151 12345678` → `4915112345678`.
- In `index.html` steht ganz unten der gleiche Platzhalter `49XXXXXXXXXX` für
  den WhatsApp-Link im Kontaktbereich — dort ebenfalls ersetzen.

### 3. Instagram & E-Mail — Datei `index.html` (Abschnitt „Kontakt“)
- Instagram-Link/Handle: `@leinwerk.atelier` → dein Handle.
- E-Mail: `hallo@leinwerk-atelier.de` → deine Adresse (an zwei Stellen:
  Link-Text und `mailto:`).

### 4. Markenname & Texte
- Markenname **LEINWERK** und der Name **Marlen Voss** stehen in `index.html`
  (Kopf, Hero, „Über mich“, Footer) sowie in den Rechtsseiten. Per Suchen &
  Ersetzen bequem austauschbar.

---

## Rechtsseiten

`impressum.html`, `datenschutz.html`, `widerruf.html`, `agb.html` enthalten
**Platzhaltertext**. Alle offenen Stellen sind mit `[…]` markiert und farbig
hervorgehoben. Bitte durch deine echten Angaben ersetzen und im Zweifel
rechtlich prüfen lassen — insbesondere Impressum, Datenschutz und das
Widerrufsrecht bei Maßanfertigungen.

Der **Kleinunternehmerhinweis nach § 19 UStG** ist im Impressum, im Footer und
in den AGB vorgesehen. Nur verwenden, wenn die Regelung auf dich zutrifft.

---

## Veröffentlichen (Netlify / Cloudflare Pages)

Es ist kein Build nötig. Lade einfach den **gesamten Ordner `atelier/`** hoch:

- **Netlify:** Ordner auf app.netlify.com/drop ziehen — fertig.
- **Cloudflare Pages:** neues Projekt → „Direct Upload“ → Ordner auswählen.

Lokal ansehen kannst du die Seite mit einem kleinen Webserver (nötig, damit
`products.js` geladen wird):

```bash
cd atelier
python3 -m http.server 8000
# dann im Browser: http://localhost:8000
```

---

## Datenschutz / DSGVO

- Keine externen Tracker, kein Analytics.
- Schriften werden **lokal** aus `fonts/` geladen (keine Google-Fonts-CDN).
- Es werden keine Cookies zu Marketingzwecken gesetzt → **kein Cookie-Banner
  nötig**.
- Das Anfrageformular übermittelt deine Eingaben über Web3Forms; das ist in der
  Datenschutzerklärung beschrieben (bitte Anbieterangaben ergänzen).

Die Schriften (Fraunces, Hanken Grotesk) stehen unter der SIL Open Font License;
die Lizenztexte liegen in `fonts/` bei.
