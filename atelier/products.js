/* ============================================================================
   LEINWERK — Produktdaten
   ----------------------------------------------------------------------------
   Hier trägst du deine Teile ein. Kein HTML nötig – nur diese Liste bearbeiten.

   Ein Teil ist ein Objekt { ... } zwischen geschweiften Klammern, die Teile
   werden durch Kommas getrennt. Kopiere am einfachsten einen bestehenden Block
   und passe die Werte an.

   Felder:
     id           eindeutige Kurz-Kennung (Kleinbuchstaben, keine Leerzeichen)
     titel        Name des Teils
     bilder       Liste von Bildpfaden. Lege deine Bilder in den Ordner "images"
                  und gib sie OHNE Dateiendung an, z.B. "images/leinenkleid".
                  Erwartet werden zwei Dateien je Bild:
                    images/leinenkleid.webp   (klein & schnell)
                    images/leinenkleid.jpg    (Fallback für alte Browser)
     preis        Zahl in Euro (Endpreis), z.B. 165
     groesse      z.B. "36 / S" oder "Maßanfertigung"
     material     z.B. "100 % Leinen, vorgewaschen"
     beschreibung ein bis drei Sätze zum Teil
     pflege       Pflegehinweis, z.B. "30 °C, links waschen, liegend trocknen"
     status       "verfügbar" | "verkauft" | "auf Anfrage"
   ========================================================================== */

const VERSANDHINWEIS =
  "Endpreis, keine Umsatzsteuer ausgewiesen (§ 19 UStG). Zzgl. Versand nach Aufwand.";

const PRODUCTS = [
  {
    id: "leinenkleid-oat",
    titel: "Leinenkleid „Hafer“",
    bilder: ["images/placeholder-1", "images/placeholder-4"],
    preis: 189,
    groesse: "36 / S",
    material: "100 % Leinen, vorgewaschen",
    beschreibung:
      "Weit fallendes Sommerkleid mit angeschnittenen Ärmeln und schmalem Taillenband. Ein Einzelstück, in Ruhe von Hand zugeschnitten und genäht.",
    pflege: "30 °C Feinwäsche, links, liegend trocknen. Leinen darf knittern.",
    status: "verfügbar",
  },
  {
    id: "hemdbluse-natur",
    titel: "Hemdbluse „Natur“",
    bilder: ["images/placeholder-2"],
    preis: 129,
    groesse: "38 / M",
    material: "Leinen-Baumwoll-Mix, ungefärbt",
    beschreibung:
      "Locker geschnittene Bluse mit Perlmuttknöpfen und leicht verlängertem Rücken. Trägt sich offen über dem Kleid oder geknöpft solo.",
    pflege: "30 °C, mit ähnlichen Farben waschen, bei Bedarf leicht dämpfen.",
    status: "verfügbar",
  },
  {
    id: "leinenrock-lehm",
    titel: "Wickelrock „Lehm“",
    bilder: ["images/placeholder-3", "images/placeholder-6"],
    preis: 145,
    groesse: "34–40 (Wickelform)",
    material: "100 % Leinen, pflanzengefärbt",
    beschreibung:
      "Wadenlanger Wickelrock mit tiefen Falten. Durch die Wickelform an mehrere Größen anpassbar.",
    pflege: "Handwäsche kalt, separat, da pflanzengefärbt.",
    status: "verfügbar",
  },
  {
    id: "leinenjacke-stein",
    titel: "Sommerjacke „Stein“",
    bilder: ["images/placeholder-4"],
    preis: 235,
    groesse: "38 / M",
    material: "Grobes Leinen, ungefüttert",
    beschreibung:
      "Unstrukturierte Jacke mit aufgesetzten Taschen und Fischgrat-Naht am Rücken. Leicht, aber mit Stand.",
    pflege: "Reinigung empfohlen, alternativ 30 °C Wollwaschgang.",
    status: "auf Anfrage",
  },
  {
    id: "leinenhose-asche",
    titel: "Weite Hose „Asche“",
    bilder: ["images/placeholder-5"],
    preis: 159,
    groesse: "S–M (Gummibund)",
    material: "Leinen, mittelschwer",
    beschreibung:
      "Palazzo-Schnitt mit weichem Gummibund und seitlichen Nahttaschen. Fällt bewusst locker.",
    pflege: "30 °C, links, liegend trocknen.",
    status: "verfügbar",
  },
  {
    id: "leinenkleid-abend",
    titel: "Langes Kleid „Abend“",
    bilder: ["images/placeholder-6", "images/placeholder-1"],
    preis: 265,
    groesse: "36 / S",
    material: "Feines Leinen, halbtransparent",
    beschreibung:
      "Bodenlanges Kleid mit schmalen Trägern und Rückenausschnitt. Ein ruhiges Teil für besondere Tage.",
    pflege: "Handwäsche kalt, liegend trocknen, kühl bügeln.",
    status: "verkauft",
  },
  {
    id: "schuerzenkleid",
    titel: "Schürzenkleid „Werkstatt“",
    bilder: ["images/placeholder-1"],
    preis: 139,
    groesse: "Einheitsgröße",
    material: "Schwerer Leinen-Drell",
    beschreibung:
      "Robustes Trägerkleid mit großer Bauchtasche – ursprünglich fürs Atelier entworfen, inzwischen Lieblingsstück vieler Kundinnen.",
    pflege: "40 °C, wird mit jeder Wäsche weicher.",
    status: "verfügbar",
  },
  {
    id: "leinenbluse-kragen",
    titel: "Bluse „Stehkragen“",
    bilder: ["images/placeholder-2", "images/placeholder-5"],
    preis: 135,
    groesse: "40 / L",
    material: "100 % Leinen",
    beschreibung:
      "Schlichte Bluse mit schmalem Stehkragen und halb geknöpfter Leiste. Klare Linie, keine Ablenkung.",
    pflege: "30 °C, links, feucht bügeln.",
    status: "verfügbar",
  },
  {
    id: "leinentop-traeger",
    titel: "Trägertop „Sommer“",
    bilder: ["images/placeholder-3"],
    preis: 89,
    groesse: "36–38",
    material: "Leinenjersey, weich",
    beschreibung:
      "Kurzes Top mit gebundenen Trägern, leicht körpernah. Als Lage oder solo.",
    pflege: "30 °C, liegend trocknen.",
    status: "verfügbar",
  },
  {
    id: "leinenmantel-lang",
    titel: "Leichter Mantel „Allee“",
    bilder: ["images/placeholder-4", "images/placeholder-6"],
    preis: 289,
    groesse: "38 / M",
    material: "Doppelt gewebtes Leinen",
    beschreibung:
      "Knielanger, offener Mantel ohne Verschluss – fällt in weichen Falten. Übergangsteil für kühle Abende.",
    pflege: "Reinigung empfohlen.",
    status: "auf Anfrage",
  },
  {
    id: "leinenkleid-tunika",
    titel: "Tunikakleid „Feld“",
    bilder: ["images/placeholder-5", "images/placeholder-2"],
    preis: 155,
    groesse: "38–40",
    material: "Leinen, pflanzengefärbt (Krapp)",
    beschreibung:
      "Gerade geschnittene Tunika mit Seitenschlitzen, warm-terracottafarben pflanzengefärbt. Jedes Stück färbt leicht unterschiedlich.",
    pflege: "Handwäsche kalt, separat.",
    status: "verkauft",
  },
  {
    id: "leinenschal",
    titel: "Tuch „Randstreifen“",
    bilder: ["images/placeholder-6"],
    preis: 59,
    groesse: "180 × 55 cm",
    material: "Feines Leinen, handgesäumt",
    beschreibung:
      "Großes Tuch mit von Hand gerolltem Saum und einem schmalen Streifen an den Enden. Reststoffe aus der Kollektion.",
    pflege: "30 °C, links, liegend trocknen.",
    status: "verfügbar",
  },
];
