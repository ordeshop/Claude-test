---
name: ebook-design
description: >-
  Erstellt verkaufsfertige, professionell gestaltete Ebooks als PDF (deutsch oder
  englisch) — von der Produktstruktur über Typografie, Layout und Cover bis zur
  druck- und shopfertigen Datei. Nutze diesen Skill immer, wenn es um ein Ebook,
  einen Guide, ein Workbook, ein digitales Produkt zum Verkauf, einen Ratgeber als
  PDF, ein Rezeptbuch, ein Kursbegleitheft oder ein Lead-Magnet-PDF geht — auch dann,
  wenn der Nutzer nur "schreib mir ein Ebook über X", "mach ein PDF-Produkt daraus"
  oder "gestalte das schöner" sagt. Also use when the user wants to create an ebook,
  design a PDF guide, a digital product, a workbook or a sellable PDF.
---

# Ebook Design

Ziel: PDFs, die aussehen, als hätte sie ein Buchgestalter gesetzt — und die man ohne schlechtes Gewissen für 19–49 € verkaufen kann. Nicht "Word-Dokument mit Bildern".

Der häufigste Fehler ist, sofort Text zu schreiben und ihn danach zu "verschönern". Ein verkaufbares Ebook wird andersherum gebaut: erst Produkt und Struktur, dann Gestaltungssystem, dann Inhalt im System.

## Ablauf

0. **Problem und Nische klären** — wofür zahlen Menschen hier, wie sprechen die Betroffenen, was machen die Besten (siehe `references/nischen-und-probleme.md`)
1. **Produkt klären** (kurz, max. 4 Fragen)
2. **Struktur festlegen** — Seitenarchitektur, nicht nur Kapitelliste
3. **Gestaltungssystem definieren** — Format, Raster, Schriften, Farben (siehe `references/gestaltung.md`)
4. **Inhalt schreiben** — im System, nicht daneben
5. **Bauen** — HTML/CSS → PDF (siehe `references/technik.md`)
6. **Visuell prüfen** — Seiten als Bilder rendern und wirklich ansehen
7. **Verkaufsfertig machen** — Rechtliches, Metadaten, Cover-Mockup (siehe `references/verkaufsfertig.md`)

## 0. Problem und Nische klären

**Zuerst das Problem, dann das Thema.** Menschen zahlen nicht für Information — die ist gratis — sondern für Gewissheit, Kompression und ein fertiges System. Prüfe, ob mindestens eines zutrifft: akuter Druck (Frist, Ablehnung, Prüfung), Scham (man will nicht öffentlich fragen), teures Fehlerrisiko, oder verstreute widersprüchliche Quellen. Trifft nichts davon zu, wird das Produkt schwer verkäuflich — egal wie gut es gestaltet ist.

Dann die Nische ansehen: die zehn erfolgreichsten Produkte zum selben Thema (Websuche, Etsy, Gumroad, Amazon-Kategorie). Notieren, welche Farbwelten, Titelmuster und Bildsprachen dort dominieren, was preislich verlangt wird und was im Lieferumfang steht. Der Konvention folgen, damit Käufer das Produkt einordnen — und an genau einer Stelle abweichen, damit es auffällt.

**Sammle die Sprache der Betroffenen**, bevor du den Titel schreibst: echte Formulierungen aus Bewertungen und Foren. Die stärksten Sätze gehören fast wörtlich in Titel, Untertitel und Einleitung. Dabei gilt: englische Käufer belohnen emotionale Bestätigung, deutsche Käufer Struktur und Kontrolle — deshalb wird nicht übersetzt, sondern je Sprache neu geschrieben.

Zahlungsstarke Felder, ihre Schreib- und Designkonventionen, Preisspannen, Pflicht-Disclaimer und die Felder, die man ohne Qualifikation meiden sollte: `references/nischen-und-probleme.md`. Wettbewerbs- und Verkaufsmuster: `references/vorbilder.md`.

**Lieferumfang gleich mitplanen.** Bestseller verkaufen nie eine einzelne Datei, sondern ein Bündel: Hauptdatei, Druckversion, einseitige Anleitung, ein Bonus (Checkliste, Vorlage, Spickzettel). Gleicher Aufwand im Layout, deutlich höherer wahrgenommener Wert — und die Anleitung verhindert die häufigsten schlechten Bewertungen.

## 1. Produkt klären

Ohne diese Antworten wird das Ebook beliebig. Frage kompakt (gerne als Auswahl), rate nicht:

- **Wer liest das und was kann die Person danach, was sie vorher nicht konnte?** Ein Ebook verkauft eine Transformation, kein Thema.
- **Umfang und Preisklasse?** Faustregel: 15–25 Seiten = kompakter Guide (9–19 €), 30–60 Seiten = vollwertiges Produkt (19–49 €), 80+ Seiten = nur sinnvoll, wenn es wirklich Referenzwerk-Charakter hat. Seitenzahl ist kein Qualitätsmerkmal — Dichte ist es.
- **Nutzungssituation?** Am Bildschirm gelesen, auf dem Handy überflogen, oder ausgedruckt und beschrieben (Workbook)? Das entscheidet über Format und Schriftgröße.
- **Marke vorhanden?** Farben, Logo, Schriften, Tonalität — wenn ja, übernehmen; wenn nein, im Gestaltungssystem definieren und dokumentieren, damit Folgeprodukte gleich aussehen.

Wenn der Nutzer zum Inhalt keine eigenen Fakten liefert: recherchiere, bevor du schreibst. Ein verkauftes Ebook mit erfundenen Zahlen ist ein Rückerstattungsantrag mit Ansage.

## 2. Struktur: Seitenarchitektur

Plane Seiten, nicht Absätze. Diese Reihenfolge hat sich bewährt:

| Seite | Zweck |
|---|---|
| Cover | Verkauft im Shop, wirkt als Thumbnail. Siehe unten. |
| Titelseite | Ruhig, nur Titel/Untertitel/Autor |
| Impressum + Haftungsausschluss | Bei Verkauf aus Deutschland Pflicht, siehe `references/verkaufsfertig.md` |
| Inhaltsverzeichnis | Verlinkt, mit Seitenzahlen |
| Einleitung | Kurz: Problem, Versprechen, wie man das Buch benutzt |
| Kapitel | Jedes mit eigener Auftaktseite |
| Praxisteil | Checklisten, Vorlagen, Arbeitsblätter — das, was den Preis rechtfertigt |
| Abschluss | Zusammenfassung + genau ein nächster Schritt (Shop, Newsletter, Folgeprodukt) |

Kapitelrhythmus: Auftaktseite → Fließtext mit Zwischenüberschriften alle 2–4 Absätze → mindestens ein visuelles Element pro Doppelseite (Callout, Zitat, Liste, Tabelle, Grafik) → Kapitelabschluss ("Das Wichtigste in 3 Sätzen" oder eine Mini-Aufgabe).

**Regel gegen Textwüsten:** keine Seite ohne mindestens einen visuellen Ankerpunkt. Und keine Seite, die aussieht wie die vorherige — Abwechslung im Seitenrhythmus ist das, was "gestaltet" von "getippt" unterscheidet.

## 3. Gestaltungssystem

Details und fertige Wertebereiche: `references/gestaltung.md` lesen, bevor du CSS schreibst.

Die nicht verhandelbaren Punkte:

- **Ein Format wählen und durchhalten.** A4 hoch für den deutschen/europäischen Markt, US Letter für den nordamerikanischen (dort die Erwartung bei druckbaren PDFs — bei beiden Märkten einfach beide Größen ausliefern). Für Tablet-/Bildschirmprodukte: 16:10 quer.
- **Großzügige Ränder.** Innen/außen mindestens 18–22 mm bei A4. Enge Ränder sind das sicherste Zeichen für Amateurarbeit.
- **Zeilenlänge 55–75 Zeichen.** Bei A4 heißt das oft: Textspalte schmaler als der Satzspiegel, Rest als Weißraum oder Marginalspalte.
- **Maximal zwei Schriften** (plus optional eine für Zahlen/Akzente). Nie System-Standards wie Arial, Calibri, Times.
- **Eine Akzentfarbe**, dazu Neutraltöne. Nie reines Schwarz auf reinem Weiß — z. B. #1A1A18 auf #FAF8F4 wirkt sofort hochwertiger.
- **Flattersatz (linksbündig)** ist die sichere Wahl, besonders auf Deutsch. Blocksatz nur mit funktionierender Silbentrennung.

## 4. Inhalt schreiben

Das Handwerk steht in `references/schreiben.md` — vor dem ersten Kapitel lesen. Es behandelt das Versprechen, die Wahl der Struktur, den Kapitelbauplan, Rezept- und Anleitungssatz, Übungen, das Überarbeiten in drei Durchgängen und die Muster, an denen Käufer AI-Text erkennen.

Die Punkte, die immer gelten:

- **Ein Versprechen, wörtlich formuliert**, bevor der erste Satz entsteht: bringt [Zielgruppe] von [Zustand] zu [Ergebnis] in [Aufwand]. Alles, was nicht darauf einzahlt, fliegt raus.
- **Der erste schnelle Nutzen gehört nach vorn** — etwas, das in fünf Minuten anwendbar ist, ins erste Kapitel.
- Kurze Absätze (2–5 Zeilen), aktive Verben, zweite Person konsequent. Zwischenüberschriften, die etwas aussagen ("Warum 90 % der Sets im Regal stehen bleiben"), nicht "Kapitel 2".
- Konkret vor allgemein: Zahlen, Temperaturen, Beträge, Beispiele, benannte Fehler mit Lösung. "Zu heiß" ist wertlos, "über 80 °C" ist Anleitung.
- Streiche Ratgeber-Floskeln: "In der heutigen schnelllebigen Welt", "Der Schlüssel zum Erfolg", "Unlock your potential".
- Keine Emojis als Gestaltungsmittel und keine Emojis in Überschriften. Gestaltung macht die Gestaltung.
- Deutsch: „typografische Anführungszeichen", Gedankenstriche als – (Halbgeviert). Englisch: "quotes" und — em dash.
- Zweisprachig heißt neu schreiben, nicht übersetzen — und danach **das Layout neu prüfen** (deutscher Text braucht ca. 15 % mehr Platz, Überschriften brechen anders).

## 5. Bauen

HTML + CSS → Chromium → PDF. Das gibt volle gestalterische Kontrolle und sieht besser aus als alles, was direkt aus reportlab kommt. Die komplette technische Anleitung inklusive Skript, Schriftbeschaffung und den Chromium-Eigenheiten steht in `references/technik.md` — vor dem ersten Build lesen.

Kurz:
- Schriften über npm (`npm pack @fontsource/<name>`) oder GitHub holen, als Datei einbetten. Keine Google-Fonts-URLs — der Container hat darauf keinen Zugriff.
- Cover und Innenteil getrennt rendern, mit pypdf zusammenführen (Seitenzahlen sollen nicht aufs Cover).
- `scripts/build_pdf.py` erledigt Rendern, Seitenzahlen, Zusammenführen und Vorschaubilder.

## 6. Visuell prüfen — nicht überspringen

Rendere jede Seite als PNG und **sieh sie dir tatsächlich an** (view-Tool). Fast alle peinlichen Fehler sind nur visuell sichtbar:

- Schusterjungen/Hurenkinder (einzelne Zeile allein oben/unten auf der Seite)
- Überschrift am Seitenende, Text auf der nächsten Seite
- Überlappungen, abgeschnittener Text, Elemente über den Rand hinaus
- Leere Restseiten am Kapitelende
- Falsche Seitenzahlen, Inhaltsverzeichnis stimmt nicht mehr
- Farbige Flächen, die im Druck grau werden

Dann ein zweiter Durchgang: nicht mehr hinzufügen, sondern beruhigen — Abstände vereinheitlichen, Schriftgrößen reduzieren, Elemente ausrichten.

## 7. Cover

Das Cover verkauft, oft als 300-px-Thumbnail. Deshalb:

- Der Test: Cover auf 160 px Breite verkleinern und ansehen. So sehen es Käufer zuerst. Titel nicht lesbar = Cover nicht fertig.
- Helles Cover braucht einen dünnen Rahmen, sonst verschwimmt es mit dem weißen Shop-Hintergrund.
- Bei einer Produktreihe: gleiches Gerüst, gleiche Schriften, nur die Farbe wechselt.
- Drei Elemente reichen: großer Titel, kurzer Untertitel mit dem Nutzen, ein visuelles Motiv (Fläche, Form, Foto, Duotone).
- Kein Stockfoto-Klischee (Handschlag, Glühbirne, Person mit Laptop am Strand).
- Cover und Innenteil müssen zusammengehören: gleiche Schrift, gleiche Farbe.
- Zusätzlich ein Mockup fürs Shop-Listing erzeugen (siehe `references/verkaufsfertig.md`).

## Was dieses Ebook von einem AI-PDF unterscheidet

Prüfe am Ende ehrlich gegen diese Liste — wenn drei Punkte zutreffen, nochmal ran:

- Alle Seiten sehen gleich aus
- Überschriften mittig, Text mittig, alles mittig
- Standardschrift, Standard-Blau, Standard-Aufzählungspunkte
- Inhalt hätte auch als Blogartikel funktioniert
- Kein einziges Element, das man ausfüllen, abhaken oder anwenden kann
- Der Text erklärt, was etwas ist, statt zu zeigen, wie man es macht

## Referenzen

- `references/nischen-und-probleme.md` — zahlungsstarke Problemfelder, Käufersprache DE/EN, Konventionen und Disclaimer je Feld, Preislogik
- `references/schreiben.md` — Schreibhandwerk: Versprechen, Struktur, Kapitelbauplan, Rezeptsatz, Übungen, Überarbeiten, AI-Muster vermeiden
- `references/vorbilder.md` — was Bestseller anders machen: Nischenanalyse, Bündel, Navigation, Cover-Thumbnail, Shop-Bilder, Preislogik, Rückerstattungen vermeiden
- `references/gestaltung.md` — Format, Raster, Typografie-Skalen, Farbpaletten, Bildsprache, fertige Kombinationen
- `references/technik.md` — HTML/CSS-Gerüst, Schriften laden, Chromium-Fallstricke, Build-Skript, Seitenzahlen
- `references/verkaufsfertig.md` — Impressum/Haftungsausschluss (DE), Metadaten, Dateigröße, Cover-Mockup, Shop-Upload
- `scripts/build_pdf.py` — Rendern, Zusammenführen, Vorschaubilder
- `assets/starter/` — HTML- und CSS-Gerüst als Startpunkt
