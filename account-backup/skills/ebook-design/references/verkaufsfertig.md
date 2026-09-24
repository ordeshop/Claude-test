# Verkaufsfertig machen

Diese Liste ist eine Arbeitshilfe, keine Rechtsberatung. Bei Unsicherheit im Einzelfall (besonders bei Gesundheits-, Finanz- oder Rechtsthemen) muss der Verkäufer das rechtlich prüfen lassen.

## 1. Pflichtseiten im PDF (Verkauf aus Deutschland)

Direkt hinter der Titelseite, auf einer eigenen Seite, klein gesetzt:

- **Impressumsangaben**: Firmenname, Rechtsform, vollständige Anschrift, E-Mail, ggf. Telefon, Umsatzsteuer-ID falls vorhanden, vertretungsberechtigte Person
- **Urheberrechtshinweis**: „© [Jahr] [Name]. Alle Rechte vorbehalten. Die Weitergabe, Vervielfältigung oder Veröffentlichung — auch auszugsweise — ist ohne schriftliche Zustimmung nicht gestattet."
- **Haftungsausschluss**: Inhalte sorgfältig erstellt, keine Gewähr für Vollständigkeit und Aktualität; keine Garantie für bestimmte Ergebnisse. Bei Gesundheits-, Ernährungs-, Rechts- oder Finanzthemen zusätzlich ein klarer Hinweis, dass der Inhalt keine fachliche Beratung ersetzt.
- **Bildnachweise**, falls fremde Bilder verwendet wurden
- Bei Empfehlungslinks: **Werbekennzeichnung**

Für die englische Fassung dasselbe sinngemäß, aber nicht wörtlich übersetzen — dort sind „Disclaimer", „Copyright notice" und ggf. „Earnings disclaimer" üblich; das deutsche Impressum bleibt trotzdem drin, wenn aus Deutschland verkauft wird.

## 2. Formulierungen, die Probleme machen

Streiche Versprechen, die man nicht halten kann: garantierte Einkommen, „in 7 Tagen zum vollen Kalender", Heilversprechen, „100 % sicher". Sie sind wettbewerbsrechtlich riskant und erzeugen Rückerstattungen. Ersetze sie durch Beschreibungen des Vorgehens.

## 3. Dateiausgabe

- **Dateiname**: `titel-des-ebooks-2026.pdf`, klein, mit Bindestrichen, ohne Umlaute und Leerzeichen. Bei zwei Sprachen: `...-de.pdf` / `...-en.pdf`.
- **PDF-Metadaten setzen**: Titel, Autor, Betreff, Stichwörter. Der Titel erscheint in der Fenster-/Tab-Leiste des Lesers — dort darf nicht „Untitled" stehen.
- **Größe** unter 15 MB, ideal 3–8 MB.
- **Kein Passwortschutz.** Er verhindert kein Weitergeben, macht aber Ärger bei ehrlichen Käufern. Wenn Schutz gewünscht ist: dezente personalisierte Fußzeile („Lizenziert für: {Name}") statt DRM.
- Bei umfangreichen Workbooks zusätzlich eine **druckoptimierte Version** ohne farbige Vollflächen anbieten — spart Tinte und erzeugt Sympathie.

## 4. Assets fürs Shop-Listing

Ein PDF verkauft sich nicht als PDF-Symbol. Erzeuge zusätzlich:

- **Cover-Bild** 1200 × 1600 px (PNG)
- **Mockup**: Cover perspektivisch auf Tablet/als Buchobjekt, plus zwei bis drei aufgefächerte Innenseiten. Lässt sich direkt in HTML/CSS bauen (`transform: perspective(...) rotateY(...)`, Schlagschatten, Hintergrund in der Markenfarbe) und mit demselben Chromium-Weg als PNG rendern.
- **3–5 Vorschauseiten** als Bilder (Innenseiten zeigen — das erhöht die Conversion deutlich stärker als Feature-Listen)
- **Bildspezifikationen**: erstes Bild quer oder quadratisch mit mittigem Motiv und freien Rändern (die Miniatur wird beschnitten), mindestens 2000 px an der kürzeren Seite, sRGB, JPG. Die Bilder als Reihenfolge erzählen: Cover → Nutzung → Innenseiten → "Das bekommst du" → Anleitung.
- **Hinweis "Digitaler Download / PDF"** sichtbar im Bild — verhindert, dass jemand ein physisches Produkt erwartet
- **Anleitungsseite als eigene Datei** mitliefern (öffnen, drucken, in einer Notiz-App nutzen). Senkt Supportanfragen und schlechte Bewertungen.
- **Kurzbeschreibung** für den Shop: Für wen, welches Ergebnis, was drin ist (Seitenzahl, Anzahl Vorlagen/Checklisten), Format, Lieferung als Sofort-Download

## 5. Shopify-Auslieferung

Digitale Produkte über die App „Digital Downloads" oder einen vergleichbaren Anbieter ausliefern. Praktisch beachten:

- Produkt als **nicht physisch** anlegen (Versand deaktivieren), sonst rechnet der Checkout Versandkosten
- Steuer korrekt einstellen — digitale Leistungen an Endkunden werden im EU-Ausland im Land des Kunden besteuert (OSS-Verfahren); dafür braucht der Shop passende Steuereinstellungen
- **Widerrufsrecht**: Bei sofortigem Download muss der Kunde vor dem Kauf ausdrücklich zustimmen, dass er auf sein Widerrufsrecht verzichtet, sonst gilt es weiter. Entsprechende Checkbox/Hinweis im Checkout einrichten.
- Download-Limits nicht zu streng setzen (mindestens 3–5 Downloads, Link mindestens 30 Tage gültig)
- Nach dem Kauf eine kurze E-Mail mit Link, Hinweis zum Öffnen und einem Kontaktweg — reduziert Supportanfragen und Rückerstattungen

## 6. Letzte Prüfung vor dem Upload

- [ ] Alle Seiten visuell kontrolliert
- [ ] Inhaltsverzeichnis stimmt mit den echten Seitenzahlen überein, Links funktionieren
- [ ] Rechtschreibung geprüft (besonders Cover, Titel, Kapitelüberschriften — Fehler dort sind tödlich)
- [ ] Impressum, Copyright, Haftungsausschluss enthalten und aktuell
- [ ] Metadaten gesetzt, Dateiname sauber
- [ ] Auf dem Handy geöffnet und gelesen — Schrift groß genug?
- [ ] Ausgedruckt (oder Druckvorschau) geprüft, falls Workbook
- [ ] Cover als 300-px-Thumbnail noch lesbar
