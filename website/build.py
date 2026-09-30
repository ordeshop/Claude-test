# -*- coding: utf-8 -*-
"""Baut die statische ORDE-Website (HTML/CSS/JS) in den Ordner 'site'."""
import os, shutil, html

OUT = "site"        # Ergebnis. Nur dieser Ordner geht auf den Server.
QUELLE = "quelle"   # handgeschriebene Dateien: CSS, JS, Schriften

MAIL = "hello@ordeshop.net"
TEL_ANZEIGE = "+49 176 34577144"
TEL_LINK = "+4917634577144"
WA_TEXT = "Hallo%20Artur%2C%20ich%20interessiere%20mich%20f%C3%BCr%20eine%20Website%20f%C3%BCr%20meinen%20Betrieb."
WA_LINK = "https://wa.me/4917634577144?text=" + WA_TEXT
TIKTOK = "https://www.tiktok.com/@ordecoms"

NAV = [
    ("index.html", "Start"),
    ("leistungen.html", "Pakete &amp; Preise"),
    ("branchen.html", "Branchen"),
    ("ablauf.html", "So l&auml;uft es ab"),
    ("referenzen.html", "Beispiele"),
    ("ueber-mich.html", "&Uuml;ber mich"),
    ("anfrage.html", "Projekt anfragen"),
]

BRANCHEN = [
    {
        "slug": "website-restaurant",
        "nav": "Restaurants &amp; Caf&eacute;s",
        "short": "Restaurant",
        "title": "Website f&uuml;r Restaurants und Caf&eacute;s erstellen lassen",
        "desc": "Restaurant-Website mit Speisekarte, &Ouml;ffnungszeiten und Reservierung – individuell gebaut, Festpreise ab 890 €. Kein Abo, komplett &uuml;bergeben.",
        "h1": "Website f&uuml;r Restaurants und Caf&eacute;s",
        "intro": "Deine G&auml;ste entscheiden am Handy, ob sie heute Abend zu dir kommen. Speisekarte, &Ouml;ffnungszeiten und der Weg zu dir m&uuml;ssen in drei Sekunden sichtbar sein – nicht als PDF, das erst geladen werden will.",
        "liste": [
            "Speisekarte als echte Webseite – auf dem Handy lesbar und in Minuten &auml;nderbar",
            "&Ouml;ffnungszeiten inklusive Feiertagen und Ruhetag",
            "Reservierung per Anruf, Formular oder Anbindung an dein bestehendes System",
            "Anfahrt, Parken und Google Maps",
            "Bildergalerie von R&auml;umen und Gerichten",
            "Anbindung an dein Google-Unternehmensprofil, damit &Ouml;ffnungszeiten &uuml;berall gleich stehen",
        ],
        "extra_h": "Warum keine Vorlage",
        "extra_p": "Ein italienisches Familienrestaurant und eine Cocktailbar brauchen dieselbe Technik, aber nicht dieselbe Wirkung. Deine Seite wird um deine Karte, deine Bilder und deine G&auml;ste herum gebaut.",
        "preis": "F&uuml;r Restaurants passt meist das Standard-Paket – wenn die Speisekarte als eigene Seite und die Reservierung direkt eingebunden werden soll, das Premium-Paket.",
        "demo": "demos/cafe/index.html",
        "demo_name": "M&Oslash;RK",
        "demo_text": "Hell und editorial, mit Men&uuml;, Galerie und &Ouml;ffnungszeiten – warm und einladend.",
    },
    {
        "slug": "website-friseur",
        "nav": "Friseure &amp; Beauty",
        "short": "Friseur",
        "title": "Website f&uuml;r Friseure und Beauty erstellen lassen",
        "desc": "Friseur-Website mit Leistungen, Preisen und Terminbuchung – individuell gebaut, Festpreise ab 890 €. Kein Abo, komplett &uuml;bergeben.",
        "h1": "Website f&uuml;r Friseure und Beauty",
        "intro": "Wer einen Termin sucht, entscheidet in Sekunden – meist am Handy, oft abends. Deine Seite muss sofort zeigen, was du kannst, was es kostet und wie man einen Termin bekommt.",
        "liste": [
            "Leistungen und Preise klar aufgelistet – Schnitt, Farbe, Styling, Kosmetik",
            "Online-Terminbuchung oder Anfrage, auch au&szlig;erhalb der &Ouml;ffnungszeiten",
            "&Ouml;ffnungszeiten inklusive Ruhetag",
            "Vorher-Nachher- und Portfolio-Galerie deiner Arbeiten",
            "Dein Team mit Fotos, damit Kunden wissen, zu wem sie kommen",
            "Anfahrt, Parken und Anbindung an dein Google-Unternehmensprofil",
        ],
        "extra_h": "Warum keine Vorlage",
        "extra_p": "Ein minimalistischer Coloristen-Salon und ein Barbershop brauchen dieselbe Technik, aber nicht dieselbe Wirkung. Deine Seite wird um deine Handschrift, deine Bilder und deine Kundschaft herum gebaut.",
        "preis": "F&uuml;r Salons und Studios passt meist das Standard-Paket – wenn Preisliste als eigene Seite und Terminbuchung direkt eingebunden werden sollen, das Premium-Paket.",
        "demo": "demos/salon/index.html",
        "demo_name": "STUDIO NOV&Eacute;",
        "demo_text": "Ruhig und modern, mit Leistungen, Team und Portfolio-Galerie – klar auf den Termin ausgerichtet.",
    },
    {
        "slug": "website-fitnessstudio",
        "nav": "Fitness- &amp; Yogastudios",
        "short": "Studio",
        "title": "Website f&uuml;r Fitnessstudios und Yogastudios",
        "desc": "Studio-Website mit Kursplan, Mitgliedschaften und Probetraining-Anfrage – individuell gebaut, Festpreise ab 890 €. Kein Abo.",
        "h1": "Website f&uuml;r Fitness- und Yogastudios",
        "intro": "Wer deine Seite besucht, hat sich meistens schon entschieden, etwas zu &auml;ndern – er sucht nur noch einen Grund, bei dir anzufangen. Die Seite hat genau eine Aufgabe: aus diesem Impuls ein Probetraining zu machen.",
        "liste": [
            "Kursplan, der sich ohne dein Zutun aktuell h&auml;lt",
            "Mitgliedschaften und Preise transparent dargestellt",
            "Probetraining-Anfrage als deutlichster Knopf der Seite",
            "Ausstattung und R&auml;ume in echten Bildern",
            "Trainerteam mit Gesicht und Schwerpunkt",
            "&Ouml;ffnungszeiten und Anfahrt",
        ],
        "extra_h": "Was den Unterschied macht",
        "extra_p": "Preise zu verstecken kostet dich Anfragen. Ich zeige dir, wie du deine Mitgliedschaften so darstellst, dass Interessenten sich melden statt weiterzuklicken.",
        "preis": "F&uuml;r Studios passt meist das Standard-Paket – soll der Kursplan eine eigene Seite bekommen und die Probetraining-Buchung angebunden werden, das Premium-Paket.",
        "demo": "demos/fitness/index.html",
        "demo_name": "FORGE",
        "demo_text": "Kr&auml;ftig und energetisch, mit Programmen, Mitgliedschaften und Probetraining-Anfrage.",
    },
    {
        "slug": "website-praxis",
        "nav": "Arzt- &amp; Therapiepraxen",
        "short": "Praxis",
        "title": "Website f&uuml;r Arztpraxen und Therapiepraxen",
        "desc": "Praxis-Website mit Sprechzeiten, Leistungen und Terminanfrage – individuell gebaut, Festpreise ab 890 €. Kein Abo, komplett &uuml;bergeben.",
        "h1": "Website f&uuml;r Arzt- und Therapiepraxen",
        "intro": "Patienten suchen nach Sprechzeiten, Leistungen und einer M&ouml;glichkeit, einen Termin zu bekommen – meistens au&szlig;erhalb deiner Sprechzeiten. Eine Praxisseite muss diese drei Dinge sofort beantworten und dabei sauber mit Daten umgehen.",
        "liste": [
            "Leistungsspektrum verst&auml;ndlich erkl&auml;rt",
            "Sprechzeiten und Urlaubsvertretung",
            "Terminanfrage &uuml;ber ein datenschutzkonformes Formular oder Anbindung an dein Terminsystem",
            "Vorstellung von Praxis und Team",
            "Anfahrt, Parkm&ouml;glichkeiten und Barrierefreiheit",
            "Notfall- und Vertretungshinweise",
        ],
        "extra_h": "Datenschutz und Werberecht",
        "extra_p": "Praxisseiten haben eigene Regeln: keine Terminw&uuml;nsche &uuml;ber ein unverschl&uuml;sseltes Formular ohne Hinweis, keine Werbeaussagen, die das Heilmittelwerbegesetz nicht zul&auml;sst. Ich baue die Seite technisch sauber – die endg&uuml;ltige Pr&uuml;fung deiner Rechtstexte geh&ouml;rt in die Hand deines Anwalts oder deiner Kammer.",
        "preis": "F&uuml;r Praxen passt meist das Standard-Paket – soll die Terminanfrage an ein bestehendes System angebunden werden, das Premium-Paket.",
        "demo": "demos/praxis/index.html",
        "demo_name": "PRAXIS AM STADTPARK",
        "demo_text": "Sprechzeiten, Leistungen, Notfallnummern und eine Terminanfrage, die keine Gesundheitsdaten abfragt.",
    },
    {
        "slug": "website-fotograf",
        "nav": "Fotografen",
        "short": "Fotograf",
        "title": "Website f&uuml;r Fotografen erstellen lassen",
        "desc": "Fotografen-Website mit Portfolio, Paketen und Anfrageformular – gro&szlig;e Bilder, schnelle Ladezeit, Festpreise ab 890 €.",
        "h1": "Website f&uuml;r Fotografen",
        "intro": "Deine Arbeit verkauft sich selbst – vorausgesetzt, sie wird gro&szlig;, schnell und ohne Ablenkung gezeigt. Die h&auml;ufigsten Fehler auf Fotografenseiten sind zu kleine Bilder, zu lange Ladezeiten und ein Kontaktweg, der drei Klicks entfernt liegt.",
        "liste": [
            "Portfolio nach Bereichen getrennt – Hochzeit, Portrait, Business, Produkt",
            "Bilder in voller Wirkung, technisch so optimiert, dass die Seite trotzdem schnell l&auml;dt",
            "Pakete und Ablauf, damit Anfragen vorqualifiziert ankommen",
            "Anfrageformular mit Termin und Anlass",
            "&Uuml;ber mich – Kunden buchen bei Fotografen einen Menschen, keine Dienstleistung",
        ],
        "extra_h": "Deine Bildrechte",
        "extra_p": "Die Seite geh&ouml;rt nach der &Uuml;bergabe vollst&auml;ndig dir, inklusive aller Dateien. Deine Bilder bleiben deine Bilder – ich verwende sie nur dann als Referenz, wenn du es ausdr&uuml;cklich erlaubst.",
        "preis": "F&uuml;r Fotografen passt meist das Premium-Paket, weil das Portfolio eine eigene Seite braucht und mehr Bildbearbeitung anf&auml;llt.",
        "demo": "demos/komla/index.html",
        "demo_name": "KOMLA",
        "demo_text": "Dunkle Galerie, die die Bilder in den Vordergrund stellt – mit klarem Anfrage-Fokus.",
    },
    {
        "slug": "website-handwerk",
        "nav": "Handwerk &amp; Dienstleister",
        "short": "Handwerk",
        "title": "Website f&uuml;r Handwerk und lokale Dienstleister",
        "desc": "Handwerker-Website mit Leistungen, Einzugsgebiet und Terminanfrage – lokal auffindbar, Festpreise ab 890 €. Kein Abo.",
        "h1": "Website f&uuml;r Handwerk und lokale Dienstleister",
        "intro": "Ob Elektriker, Malerbetrieb oder Gartenbau – deine Kunden suchen lokal und entscheiden schnell. Wer bei &bdquo;Elektriker + Stadt&ldquo; nicht auffindbar ist oder keine anklickbare Telefonnummer auf dem Handy zeigt, verliert den Auftrag an den N&auml;chsten.",
        "liste": [
            "Leistungen klar benannt – in den Worten, mit denen Kunden suchen",
            "Einzugsgebiet, damit keine Anfragen von 200 Kilometer weit kommen",
            "Telefonnummer als anklickbarer Knopf auf jeder Seite",
            "Referenzen mit Vorher-Nachher-Bildern",
            "Terminanfrage oder R&uuml;ckrufbitte",
            "&Ouml;ffnungs- beziehungsweise B&uuml;rozeiten",
        ],
        "extra_h": "Auffindbarkeit von Anfang an",
        "extra_p": "Ich lege die Seite so an, dass Google versteht, was du tust und wo du es tust – Seitentitel, Struktur und Ortsangaben sauber gesetzt. Das ersetzt keine laufende Werbung, ist aber die Grundlage daf&uuml;r, dass du &uuml;berhaupt gefunden wirst.",
        "preis": "F&uuml;r viele Handwerksbetriebe reicht das Basis-Paket mit einer gut gebauten Seite v&ouml;llig aus.",
        "demo": "demos/elektro/index.html",
        "demo_name": "ELEKTRO BRANDL",
        "demo_text": "Notdienst-Nummer ganz oben, Leistungen, Einsatzgebiet und Anfrage &ndash; auf das Wesentliche gebaut.",
    },
]

# Icons (schlichte SVG-Zeichen, keine externen Bilder) und Anzeigename der Demo-Adresse
ICONS = {
    "website-restaurant": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 3v8a2 2 0 0 0 4 0V3M8 11v10"/><path d="M17 3c-1.5 2-2 3.5-2 6 0 1.5.7 2 2 2v10"/></svg>',
    "website-friseur": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="6" cy="18" r="2.6"/><circle cx="18" cy="18" r="2.6"/><path d="M7.8 16.2 18 4M16.2 16.2 6 4"/></svg>',
    "website-fitnessstudio": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 9v6M7 7v10M17 7v10M20 9v6M7 12h10"/></svg>',
    "website-praxis": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 7v10M7 12h10"/><rect x="3" y="3" width="18" height="18" rx="4"/></svg>',
    "website-fotograf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3" y="7" width="18" height="13" rx="3"/><circle cx="12" cy="13.5" r="3.6"/><path d="M9 7l1.4-2.4h3.2L15 7"/></svg>',
    "website-handwerk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M14.5 4.5a4 4 0 0 0 5 5L21 8l-5-5zM13 7 4 16v4h4l9-9"/></svg>',
}
for _b in BRANCHEN:
    _b["icon"] = ICONS[_b["slug"]]
    _b["demo_host"] = "ordeshop.net/" + _b["demo"].replace("/index.html", "") if _b["demo"] else "ordeshop.net"


# ---------------------------------------------------------------- Strukturierte Daten
SCHEMA_BETRIEB = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://ordeshop.net/#betrieb",
  "name": "ORD\u00c9",
  "description": "Individuelle Websites f\u00fcr Restaurants, Friseure, Studios, Praxen, Fotografen und Handwerk in Deutschland, \u00d6sterreich und der Schweiz. Festpreis ab 890 Euro, kein Abo.",
  "url": "https://ordeshop.net/",
  "image": "https://ordeshop.net/assets/marke/teilen.jpg",
  "telephone": "+4917634577144",
  "email": "hello@ordeshop.net",
  "priceRange": "890 - 2390 EUR",
  "address": { "@type": "PostalAddress", "addressCountry": "DE", "addressRegion": "Bayern" },
  "areaServed": [
    { "@type": "Country", "name": "Deutschland" },
    { "@type": "Country", "name": "\u00d6sterreich" },
    { "@type": "Country", "name": "Schweiz" }
  ],
  "sameAs": ["https://www.tiktok.com/@ordecoms"],
  "makesOffer": [
    { "@type": "Offer", "name": "Basis", "price": "890", "priceCurrency": "EUR",
      "description": "Eine Seite mit allem Wichtigen, individuell gebaut." },
    { "@type": "Offer", "name": "Standard", "price": "1590", "priceCurrency": "EUR",
      "description": "Bis zu vier Seiten, Texte \u00fcberarbeitet, Bilder aufbereitet, Google-Grundeinrichtung." },
    { "@type": "Offer", "name": "Premium", "price": "2390", "priceCurrency": "EUR",
      "description": "Bis zu sieben Seiten, alle Texte geschrieben, Terminbuchung eingebunden." }
  ]
}
</script>"""


def schema_faq(paare):
    """Haeufige Fragen fuer Google aufbereiten."""
    import json
    eintraege = [{
        "@type": "Question",
        "name": _klar(f),
        "acceptedAnswer": {"@type": "Answer", "text": _klar(a)}
    } for f, a in paare]
    daten = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": eintraege}
    return '<script type="application/ld+json">\n%s\n</script>' % json.dumps(daten, ensure_ascii=False, indent=1)


def _klar(t):
    """HTML-Eintraege in lesbaren Text zurueckverwandeln."""
    import re, html as _h
    return _h.unescape(re.sub(r"<[^>]+>", "", t)).replace("\u00a0", " ").strip()


def schema_brotkrumen(*stationen):
    """Navigationspfad fuer die Google-Ergebnisse."""
    import json
    liste = [{
        "@type": "ListItem", "position": i + 1, "name": _klar(name),
        "item": "https://ordeshop.net/" + pfad
    } for i, (name, pfad) in enumerate(stationen)]
    daten = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": liste}
    return '<script type="application/ld+json">\n%s\n</script>' % json.dumps(daten, ensure_ascii=False, indent=1)


def head(title, desc, canonical):
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | ORD&Eacute;</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://ordeshop.net/{canonical}">
<meta property="og:title" content="{title} | ORD&Eacute;">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ordeshop.net/{canonical}">
<meta property="og:site_name" content="ORD&Eacute;">
<meta property="og:locale" content="de_DE">
<meta property="og:image" content="https://ordeshop.net/assets/marke/teilen.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://ordeshop.net/assets/marke/teilen.jpg">
<meta name="theme-color" content="#1E3B32">
<link rel="icon" href="assets/marke/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="assets/marke/logo.svg">
<link rel="apple-touch-icon" href="assets/marke/icon-180.png">
<link rel="stylesheet" href="assets/fonts/fonts.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Direkt zum Inhalt</a>
"""


def header(active):
    items = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        extra = ' data-cta="1"' if href == "anfrage.html" else ""
        items += f'<li><a href="{href}"{cls}{extra}>{label}</a></li>\n'
    return f"""<div class="topbar"><div class="wrap">Individuelle Websites f&uuml;r Betriebe in Deutschland, &Ouml;sterreich und der Schweiz &middot; Festpreis, kein Abo</div></div>
<header class="site-head">
  <div class="wrap head-inner">
    <a class="logo" href="index.html"><img src="assets/marke/logo.svg" alt="" width="30" height="30">ORD&Eacute;</a>
    <button class="burger" aria-expanded="false" aria-controls="nav" aria-label="Men&uuml; &ouml;ffnen"><span></span><span></span><span></span></button>
    <nav id="nav"><ul>
{items}    </ul></nav>
  </div>
</header>
<main id="main">
"""


def branch_links(current=""):
    out = '<div class="branchgrid reveal-group">'
    for b in BRANCHEN:
        if b["slug"] == current:
            continue
        out += (f'<a class="branchcard reveal" href="{b["slug"]}.html">'
                f'<span class="bc-icon" aria-hidden="true">{b["icon"]}</span>'
                f'<span class="bc-title">{b["nav"]}</span>'
                f'<span class="bc-go">Ansehen &rarr;</span></a>')
    out += "</div>"
    return out


def demo_card(b, big=False):
    """Vorschau der Demo als Bild im Browser-Rahmen. Klick oeffnet die echte Seite."""
    cls = "demoframe big" if big else "demoframe"
    slug = b["demo"].split("/")[1] if b["demo"] else ""
    return f"""<article class="{cls} reveal">
  <div class="browserbar"><span></span><span></span><span></span><em>{b['demo_host']}</em></div>
  <a class="screen" href="{b['demo']}" aria-label="Demo {b['demo_name']} &ouml;ffnen">
    <img src="demos/vorschau/{slug}.webp" alt="Vorschau der Beispielseite {b['demo_name']}" width="1100" height="705" loading="lazy" decoding="async">
  </a>
  <div class="demometa">
    <span class="demo-kicker">{b['short']}</span>
    <span class="demo-name">{b['demo_name']}</span>
    <span class="demo-text">{b['demo_text']}</span>
    <a class="demo-go" href="{b['demo']}">Live ansehen &rarr;</a>
  </div>
</article>"""


def phone_mockup():
    """Handy-Rahmen im Hero, in dem Vorschaubilder der Demos durchwechseln."""
    slides = ""
    demos = [x for x in BRANCHEN if x["demo"]]
    for i, b in enumerate(demos):
        slug = b["demo"].split("/")[1]
        active = " is-active" if i == 0 else ""
        laden = "eager" if i == 0 else "lazy"
        slides += (f'<img class="pslide{active}" data-label="{b["demo_name"]} &middot; {b["short"]}" '
                   f'src="demos/vorschau/{slug}-handy.webp" alt="" width="640" height="1313" '
                   f'loading="{laden}" decoding="async">')
    return f"""<div class="phone" aria-hidden="true">
  <div class="phone-frame">
    <div class="phone-notch"></div>
    <div class="phone-screen">{slides}</div>
  </div>
  <p class="phone-label"><span id="phoneLabel">{demos[0]['demo_name']}</span></p>
</div>"""


def footer():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV[1:])
    br = "".join(f'<li><a href="{b["slug"]}.html">{b["nav"]}</a></li>' for b in BRANCHEN)
    return f"""</main>
<section class="cta-band">
  <div class="wrap">
    <h2>Noch unsicher?</h2>
    <p>Schreib mir vor der Anfrage. Ich sage dir ehrlich, ob dein Vorhaben zu meinem Angebot passt – auch wenn die Antwort nein lautet.</p>
    <p class="kontaktbtns">
      <a class="btn wa" href="{WA_LINK}" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.02c-.24.68-1.2 1.26-1.97 1.42-.53.11-1.21.2-3.51-.75-2.95-1.22-4.84-4.2-4.99-4.4-.14-.2-1.19-1.58-1.19-3.02s.76-2.14 1.03-2.43c.27-.29.58-.36.78-.36l.56.01c.18.01.42-.07.66.5.24.58.83 2.01.9 2.16.07.14.12.31.02.51-.1.2-.15.32-.29.49-.15.17-.31.38-.44.51-.14.14-.29.3-.13.58.17.29.75 1.23 1.6 2 1.1.98 2.03 1.28 2.32 1.42.29.15.46.12.63-.07.17-.2.72-.84.91-1.13.19-.29.39-.24.65-.14.26.09 1.68.79 1.97.94.29.14.48.22.55.34.07.12.07.69-.17 1.37z"/></svg>WhatsApp schreiben</a>
      <a class="btn ghost" href="tel:{TEL_LINK}">{TEL_ANZEIGE}</a>
    </p>
    <p class="cta-mail"><a href="mailto:{MAIL}">{MAIL}</a><span>Antwort an Werktagen innerhalb von 24&nbsp;Stunden</span></p>
  </div>
</section>
<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <span class="logo">ORD&Eacute;</span>
      <p>Sch&ouml;n geordnet. Individuelle Websites f&uuml;r Restaurants, Salons, Studios, Praxen, Fotografen und Handwerk in Deutschland, &Ouml;sterreich und der Schweiz. Einmal gebaut, komplett &uuml;bergeben.</p>
      <p class="foot-kontakt">
        <a href="{WA_LINK}" rel="noopener">WhatsApp</a> &middot;
        <a href="tel:{TEL_LINK}">{TEL_ANZEIGE}</a><br>
        <a href="mailto:{MAIL}">{MAIL}</a> &middot;
        <a href="{TIKTOK}" rel="noopener">TikTok</a>
      </p>
    </div>
    <div><h3>&Uuml;bersicht</h3><ul>{links}</ul></div>
    <div><h3>Branchen</h3><ul>{br}</ul></div>
    <div><h3>Regionen</h3><ul>
      <li><a href="webdesign-landsberg.html">Landsberg am Lech</a></li>
      <li><a href="webdesign-augsburg.html">Augsburg</a></li>
      <li><a href="webdesign-muenchen.html">M&uuml;nchen</a></li>
      <li><a href="was-kostet-eine-website.html">Was kostet eine Website?</a></li>
    </ul></div>
    <div><h3>Rechtliches</h3><ul>
      <li><a href="impressum.html">Impressum</a></li>
      <li><a href="datenschutz.html">Datenschutz</a></li>
      <li><a href="agb.html">AGB</a></li>\n      <li><a href="widerruf.html">Widerruf</a></li>
    </ul></div>
  </div>
  <div class="wrap foot-base">&copy; 2026 ORD&Eacute; &middot; Kein Ausweis der Umsatzsteuer gem&auml;&szlig; &sect;&nbsp;19 UStG</div>
</footer>
<a class="waFloat" href="{WA_LINK}" rel="noopener" aria-label="Per WhatsApp schreiben">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.02c-.24.68-1.2 1.26-1.97 1.42-.53.11-1.21.2-3.51-.75-2.95-1.22-4.84-4.2-4.99-4.4-.14-.2-1.19-1.58-1.19-3.02s.76-2.14 1.03-2.43c.27-.29.58-.36.78-.36l.56.01c.18.01.42-.07.66.5.24.58.83 2.01.9 2.16.07.14.12.31.02.51-.1.2-.15.32-.29.49-.15.17-.31.38-.44.51-.14.14-.29.3-.13.58.17.29.75 1.23 1.6 2 1.1.98 2.03 1.28 2.32 1.42.29.15.46.12.63-.07.17-.2.72-.84.91-1.13.19-.29.39-.24.65-.14.26.09 1.68.79 1.97.94.29.14.48.22.55.34.07.12.07.69-.17 1.37z"/></svg>
</a>
<script src="assets/script.js"></script>
</body>
</html>
"""


SEITEN = []   # gesammelt fuer die sitemap.xml


def page(filename, title, desc, active, body, schema="", rang=0.6):
    content = head(title, desc, filename) + schema + header(active) + body + footer()
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(content)
    SEITEN.append((filename, rang))


# ---------------------------------------------------------------- Bausteine
PAKETE_KURZ = """
<section class="section">
  <div class="wrap">
    <span class="kicker">Pakete</span>
    <h2>Drei Pakete, feste Preise</h2>
    <div class="cards reveal-group">
      <article class="card reveal">
        <h3>Basis</h3><p class="price">890 &euro;</p>
        <p>Eine Seite mit allem Wichtigen: wer du bist, was du anbietest, wann du da bist, wie man dich erreicht.</p>
      </article>
      <article class="card featured reveal">
        <span class="badge">Meistgew&auml;hlt</span>
        <h3>Standard</h3><p class="price">1.590 &euro;</p>
        <p>Bis zu vier Seiten, deine Texte in Form gebracht, Bilder aufbereitet, plus die Grundlagen f&uuml;r Google.</p>
      </article>
      <article class="card reveal">
        <h3>Premium</h3><p class="price">2.390 &euro;</p>
        <p>Bis zu sieben Seiten, alle Texte von mir geschrieben, Speisekarte oder Portfolio als eigene Seite, Terminbuchung eingebunden.</p>
      </article>
    </div>
    <p class="incl"><strong>In jedem Paket:</strong> 12 Monate &Auml;nderungen inklusive &middot; Domain und Hosting eingerichtet &middot; vollst&auml;ndige &Uuml;bergabe &middot; kein Abo bei mir</p>
    <p><a class="btn" href="anfrage.html">Kostenlosen Entwurf anfordern</a> <a class="btn ghost" href="leistungen.html">Alle Leistungen im Vergleich</a></p>
  </div>
</section>
"""

ABLAUF_BLOCK = """
<section class="section alt">
  <div class="wrap">
    <span class="kicker">So l&auml;uft es ab</span>
    <h2>F&uuml;nf Schritte bis zur fertigen Seite</h2>
    <ol class="steps reveal-group">
      <li class="reveal"><h3>Anfrage</h3><p>Du schilderst kurz, worum es geht, und nennst dein Wunschpaket.</p></li>
      <li class="reveal"><h3>Best&auml;tigung</h3><p>Ich pr&uuml;fe, ob das Paket passt, und best&auml;tige dir den Festpreis. Erst danach beginnt etwas.</p></li>
      <li class="reveal"><h3>Briefing</h3><p>Du f&uuml;llst ein Formular aus, ich sammle Texte und Bilder ein. 15 bis 20 Minuten.</p></li>
      <li class="reveal"><h3>Entwurf</h3><p>Du siehst die Seite live und gibst deine R&uuml;ckmeldungen gesammelt.</p></li>
      <li class="reveal"><h3>&Uuml;bergabe</h3><p>Die Seite geht online, alle Dateien und Zug&auml;nge geh&ouml;ren dir.</p></li>
    </ol>
    <p class="note">50&nbsp;% bei Auftragserteilung, der Rest vor dem Live-Gang.</p>
  </div>
</section>
"""


def faq(items):
    out = '<div class="faq">'
    for q, a in items:
        out += f"<details><summary>{q}</summary><div>{a}</div></details>"
    return out + "</div>"


# ---------------------------------------------------------------- Seiten
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
os.makedirs(os.path.join(OUT, "assets", "fonts"), exist_ok=True)

# Handgeschriebene Dateien aus 'quelle' nach 'site/assets' kopieren.
# Das ersetzt die frueheren Kopierschritte von Hand.
for name in ("style.css", "script.js"):
    quelle = os.path.join(QUELLE, name)
    if os.path.exists(quelle):
        shutil.copy2(quelle, os.path.join(OUT, "assets", name))
    else:
        print("ACHTUNG: %s fehlt in %s" % (name, QUELLE))

schriften_quelle = os.path.join(QUELLE, "fonts")
schriften_ziel = os.path.join(OUT, "assets", "fonts")
if os.path.isdir(schriften_quelle):
    for name in os.listdir(schriften_quelle):
        if name.endswith((".css", ".woff2", ".woff")):
            shutil.copy2(os.path.join(schriften_quelle, name),
                         os.path.join(schriften_ziel, name))

fehlend = [n for n in ("fraunces-variable.woff2", "inter-variable.woff2",
                       "hanken-grotesk-variable.woff2",
                       "bricolage-grotesque-variable.woff2")
           if not os.path.exists(os.path.join(schriften_ziel, n))]
if fehlend:
    print("HINWEIS: %d Schriftdatei(en) fehlen noch, die Seite nutzt vorlaeufig "
          "Systemschriften. Siehe unterlagen/SCHRIFTEN.md" % len(fehlend))

# Markenmaterial mitkopieren (Logo, Favicons, Teilen-Bild).
marke_quelle = os.path.join(QUELLE, "marke")
if os.path.isdir(marke_quelle):
    shutil.copytree(marke_quelle, os.path.join(OUT, "assets", "marke"),
                    dirs_exist_ok=True)
else:
    print("ACHTUNG: Ordner %s fehlt" % marke_quelle)

# Die Beispielseiten liegen im eigenen Projekt 'orde-demos' und werden dort
# gebaut und hochgeladen. Auf dem Server landen sie unter /demos/.
# Hier wird nur geprueft, ob die Startseite ins Leere zeigen wuerde.
if not os.path.isdir(os.path.join(OUT, "demos")):
    print("HINWEIS: Der Ordner site/demos fehlt hier - das ist richtig so. "
          "Die Beispielseiten kommen aus dem Projekt 'orde-demos' und werden "
          "getrennt hochgeladen. Nur in der oertlichen Vorschau fehlen dann "
          "die Vorschaubilder.")

# Startseite
index_body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <span class="kicker">Websites f&uuml;r Restaurants &middot; Salons &middot; Studios &middot; Praxen &middot; Fotografen &middot; Handwerk</span>
      <h1>Deine Website. <em>Fertig gesehen,</em> bevor du dich entscheidest.</h1>
      <p class="lead">Ich baue dir einen echten Entwurf deiner Startseite – kostenlos und unverbindlich. Gef&auml;llt er dir, wird daraus deine Website. Festpreis ab 890&nbsp;&euro;, kein Abo, 12 Monate &Auml;nderungen inklusive.</p>
      <p class="hero-btns"><a class="btn big" href="anfrage.html">Kostenlosen Entwurf anfordern</a> <a class="btn ghost" href="referenzen.html">Beispiele ansehen</a></p>
      <ul class="facts">
        <li><strong>0 &euro;</strong><span>f&uuml;r den Entwurf</span></li>
        <li><strong>ab 890 &euro;</strong><span>Festpreis, einmalig</span></li>
        <li><strong>12 Monate</strong><span>&Auml;nderungen inklusive</span></li>
      </ul>
    </div>
    {phone_mockup()}
  </div>
</section>

<section class="section proof">
  <div class="wrap">
    <span class="kicker">Echte Seiten, kein Bildchen</span>
    <h2>So sieht das aus, was du bekommst</h2>
    <p class="lead-sm">Alles hier unten ist live und anklickbar – auf dem Handy genauso wie am Rechner. Tipp einfach drauf.</p>
    <div class="demogrid reveal-group">
      {"".join(demo_card(b) for b in BRANCHEN if b["demo"])}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <span class="kicker">Branchen</span>
    <h2>Gebaut f&uuml;r deinen Betrieb</h2>
    <p class="lead-sm">Jede Branche hat andere Fragen, die Kunden sofort beantwortet haben wollen. Such dir deine aus.</p>
    {branch_links()}
  </div>
</section>

<section class="section steps-section">
  <div class="wrap">
    <span class="kicker">So einfach geht es</span>
    <h2>Drei Schritte, und du hast sie gesehen</h2>
    <ol class="steps reveal-group">
      <li class="reveal"><h3>Du erz&auml;hlst kurz von deinem Betrieb</h3><p>Ein paar S&auml;tze reichen. Kein Formularmarathon, keine Verpflichtung.</p></li>
      <li class="reveal"><h3>Ich baue deinen Entwurf</h3><p>Eine echte Startseite mit deinem Namen und deinen Inhalten. Du bekommst einen Link zum Anklicken.</p></li>
      <li class="reveal"><h3>Du entscheidest</h3><p>Gef&auml;llt er dir, machen wir weiter. Wenn nicht, war es das – ohne Kosten.</p></li>
    </ol>
  </div>
</section>

{PAKETE_KURZ}

<section class="section alt">
  <div class="wrap">
    <span class="kicker">Warum ORD&Eacute;</span>
    <h2>Was du bekommst – und was nicht</h2>
    <div class="usp reveal-group">
      <div class="reveal"><h3>Du musst nie selbst ran</h3><p>Neue Speisekarte, neue Preise, neues Teamfoto? Schick es mir, ich setze es um. Kein Login, kein Redaktionssystem, keine Updates.</p></div>
      <div class="reveal"><h3>L&auml;dt sofort, kann nicht gehackt werden</h3><p>Deine Seite wird fest gebaut statt bei jedem Aufruf berechnet. Kein WordPress, keine Plugins, nichts, was kaputtgehen kann.</p></div>
      <div class="reveal"><h3>Kein Baukasten-Look</h3><p>Aufbau, Raster, Bildformate und Schriften werden f&uuml;r deinen Betrieb zusammengestellt – nicht nur die Farbe getauscht.</p></div>
      <div class="reveal"><h3>Keine Versprechen zu Umsatz oder Google-Platz</h3><p>Eine gute Website macht es Kunden leichter, dich zu finden und anzurufen. Verkaufen musst du weiterhin selbst.</p></div>
      <div class="reveal"><h3>Nichts erfunden</h3><p>Keine Bewertungen, Zertifikate oder Zahlen, die du mir nicht gegeben hast. Was fehlt, bleibt weg.</p></div>
      <div class="reveal"><h3>Keine Rechtstexte</h3><p>Impressum, Datenschutz und AGB stellst du. Ich binde sie ein, pr&uuml;fe sie aber nicht – das darf ich nicht.</p></div>
    </div>
  </div>
</section>

<section class="section relaunch">
  <div class="wrap narrow">
    <span class="kicker">Du hast schon eine Website?</span>
    <h2>Relaunch statt Neuanfang</h2>
    <p class="lead-sm">Deine Seite ist in die Jahre gekommen, sieht auf dem Handy schlecht aus oder l&auml;dt ewig? Dann bauen wir sie neu – mit denselben Paketen und denselben Festpreisen.</p>
    <ul class="checks">
      <li>Deine Adresse bleibt, niemand muss etwas Neues lernen</li>
      <li>Texte und Bilder &uuml;bernehme ich, du f&auml;ngst nicht bei null an</li>
      <li>Alte Links leite ich um, damit nichts ins Leere l&auml;uft</li>
      <li>Ich sage dir vorher ehrlich, ob sich der Aufwand lohnt</li>
    </ul>
    <p><a class="btn" href="anfrage.html">Seite pr&uuml;fen lassen</a></p>
  </div>
</section>

{ABLAUF_BLOCK}

<section class="section">
  <div class="wrap narrow">
    <span class="kicker">Gut zu wissen</span>
    <h2>H&auml;ufige Fragen</h2>
    {faq([
      ("Ist der Entwurf wirklich kostenlos?", "Ja. Du bekommst eine echte, anklickbare Startseite mit deinen Inhalten und entscheidest danach. Sagst du nein, entstehen dir keine Kosten."),
      ("Kann ich sp&auml;ter selbst etwas &auml;ndern?", "Du musst nicht. Schick mir die &Auml;nderung per Mail oder Nachricht, ich setze sie in zwei bis drei Werktagen um. 12 Monate lang ist das im Preis enthalten, bis zu vier &Auml;nderungen im Monat."),
      ("Geh&ouml;rt mir die Seite wirklich?", "Ja, vollst&auml;ndig – inklusive aller Dateien und Zug&auml;nge. Keinerlei Bindung an mich."),
      ("Was kostet mich das laufend?", "Bei mir nichts. Nur Domain und Hosting bei deinem Anbieter, &uuml;blicherweise zwischen 5 und 15&nbsp;&euro; im Monat."),
      ("Warum kein WordPress?", "Weil du es dann selbst pflegen und aktuell halten m&uuml;sstest. Meine Seiten sind fest gebaut: schneller, sicherer, keine Updates – und die &Auml;nderungen &uuml;bernehme ich."),
      ("Ich habe schon eine Seite, lohnt sich ein Relaunch?", "Sag mir die Adresse, ich schaue sie mir an und sage dir ehrlich, was ich davon halte – auch wenn die Antwort lautet, dass sie so bleiben kann."),
      ("Brauche ich technisches Wissen?", "Nein. Domain und Hosting richte ich ein, danach l&auml;uft alles auf deinen Namen."),
      ("Meine Branche steht nicht in der Liste. Geht das trotzdem?", "Ja. Beschreib deinen Betrieb einfach in der Anfrage."),
    ])}
  </div>
</section>

<section class="section final">
  <div class="wrap narrow center">
    <h2>Willst du sehen, wie deine Seite aussehen k&ouml;nnte?</h2>
    <p class="lead-sm">Kurz beschreiben, worum es geht. Ich melde mich innerhalb eines Werktags – und der Entwurf kostet dich nichts.</p>
    <p><a class="btn big" href="anfrage.html">Kostenlosen Entwurf anfordern</a></p>
  </div>
</section>
"""
INDEX_FAQ = [
  ("Ist der Entwurf wirklich kostenlos?", "Ja. Du bekommst eine echte, anklickbare Startseite mit deinen Inhalten und entscheidest danach. Sagst du nein, entstehen dir keine Kosten."),
  ("Kann ich sp&auml;ter selbst etwas &auml;ndern?", "Du musst nicht. Schick mir die &Auml;nderung per Mail oder Nachricht, ich setze sie in zwei bis drei Werktagen um. 12 Monate lang ist das im Preis enthalten, bis zu vier &Auml;nderungen im Monat."),
  ("Geh&ouml;rt mir die Seite wirklich?", "Ja, vollst&auml;ndig, inklusive aller Dateien und Zug&auml;nge. Keinerlei Bindung an mich."),
  ("Was kostet mich das laufend?", "Bei mir nichts. Nur Domain und Hosting bei deinem Anbieter, &uuml;blicherweise zwischen 5 und 15 Euro im Monat."),
  ("Warum kein WordPress?", "Weil du es dann selbst pflegen und aktuell halten m&uuml;sstest. Meine Seiten sind fest gebaut: schneller, sicherer, keine Updates, und die &Auml;nderungen &uuml;bernehme ich."),
  ("Was kostet eine Website?", "Bei mir 890 Euro f&uuml;r eine Seite, 1.590 Euro f&uuml;r bis zu vier Seiten und 2.390 Euro f&uuml;r bis zu sieben Seiten. Festpreis, einmalig, ohne Abo."),
]

page("index.html", "Website erstellen lassen f&uuml;r Restaurants, Salons und lokale Betriebe",
     "Individuelle Website f&uuml;r Restaurants, Friseure, Studios, Praxen, Fotografen und Handwerk – Festpreise ab 890 €. Kein Baukasten, kein Abo, komplett &uuml;bergeben.",
     "index.html", index_body,
     schema=SCHEMA_BETRIEB + schema_faq(INDEX_FAQ), rang=1.0)

# Branchen-Übersicht
branchen_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Branchen</span>
    <h1>F&uuml;r welche Betriebe ich baue</h1>
    <p class="lead">Jede Seite zeigt, was in deiner Branche auf die Website geh&ouml;rt, welches Paket meist passt – und wo es das schon fertig zu sehen gibt.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {branch_links()}
    <p class="note">Deine Branche ist nicht dabei? <a href="anfrage.html">Frag trotzdem an.</a></p>
  </div>
</section>
{PAKETE_KURZ}
"""
page("branchen.html", "Branchen – Websites f&uuml;r lokale Betriebe",
     "Websites f&uuml;r Restaurants, Friseure, Fitnessstudios, Praxen, Fotografen und Handwerk. Festpreise ab 890 €, individuell gebaut.",
     "branchen.html", branchen_body, rang=0.8)

# Branchenseiten
for b in BRANCHEN:
    liste = "".join(f"<li>{i}</li>" for i in b["liste"])
    demo = ""
    if b["demo"]:
        demo = f"""
<section class="section alt">
  <div class="wrap narrow">
    <span class="kicker">Live-Beispiel</span>
    <h2>So k&ouml;nnte deine Seite aussehen</h2>
    <p class="lead-sm">Komplett gebaut und anklickbar – tipp einfach drauf.</p>
    {demo_card(b, big=True)}
  </div>
</section>"""
    body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Branche &middot; {b['short']}</span>
    <h1>{b['h1']}</h1>
    <p class="lead">{b['intro']}</p>
    <p><a class="btn" href="anfrage.html">Projekt anfragen</a> <a class="btn ghost" href="leistungen.html">Pakete ansehen</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>Was auf deine Seite geh&ouml;rt</h2>
    <ul class="checks">{liste}</ul>
    <h2>{b['extra_h']}</h2>
    <p>{b['extra_p']}</p>
    <h2>Was das kostet</h2>
    <p><strong>Feste Preise: 890&nbsp;&euro;, 1.590&nbsp;&euro; oder 2.390&nbsp;&euro;.</strong> {b['preis']} Einmalig, kein Abo. <a href="leistungen.html">Alle Leistungen im Vergleich</a></p>
    <p><a class="btn" href="anfrage.html">Projekt anfragen</a></p>
  </div>
</section>
{demo}
<section class="section">
  <div class="wrap">
    <span class="kicker">Weitere Branchen</span>
    <h2>Auch daf&uuml;r baue ich</h2>
    {branch_links(b['slug'])}
  </div>
</section>
"""
    page(b["slug"] + ".html", b["title"], b["desc"], "branchen.html", body,
         schema=schema_brotkrumen(("Start", "index.html"), ("Branchen", "branchen.html"),
                                  (b["nav"], b["slug"] + ".html")),
         rang=0.9)

# Leistungen
tabelle_rows = [
    ("Seiten", "1 (Onepager)", "bis 4", "bis 7"),
    ("Individuelles Design, kein Theme von der Stange", "y", "y", "y"),
    ("F&uuml;r Handy, Tablet und Desktop gebaut", "y", "y", "y"),
    ("Kontakt- oder Anfrageformular", "y", "y", "y"),
    ("Karte, &Ouml;ffnungszeiten, Google-Unternehmensprofil", "y", "y", "y"),
    ("Domain und Hosting einrichten, Live-Gang", "y", "y", "y"),
    ("Deine Texte", "eingesetzt", "&uuml;berarbeitet", "komplett geschrieben"),
    ("Bildbearbeitung", "n", "bis 20 Bilder", "bis 30 Bilder"),
    ("Auffindbarkeit bei Google, Grundeinrichtung", "n", "y", "y"),
    ("Speisekarte, Kursplan oder Portfolio als eigene Seite", "n", "n", "y"),
    ("Terminbuchung oder Reservierung angebunden", "n", "n", "y"),
    ("Korrekturrunden", "1", "2", "2"),
    ("&Uuml;bergabe und Einweisung", "y", "y", "y"),
    ("&Auml;nderungen inklusive", "12 Monate", "12 Monate", "12 Monate"),
    ("Lieferzeit ab vollst&auml;ndigem Briefing", "1&ndash;2 Wochen", "2&ndash;3 Wochen", "3&ndash;4 Wochen"),
]
rows_html = ""
for r in tabelle_rows:
    cells = ""
    for c in r[1:]:
        if c == "y":
            cells += '<td><span class="yes" aria-label="enthalten">&#10003;</span></td>'
        elif c == "n":
            cells += '<td><span class="no" aria-label="nicht enthalten">&ndash;</span></td>'
        else:
            cells += f"<td>{c}</td>"
    rows_html += f"<tr><th scope='row'>{r[0]}</th>{cells}</tr>"

leistungen_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Pakete &amp; Preise</span>
    <h1>Individuelle Website f&uuml;r deinen Betrieb</h1>
    <p class="lead">Keine Vorlage, kein Baukasten: eine Website, die von Grund auf f&uuml;r deinen Betrieb gebaut wird. F&uuml;r Restaurants, Salons, Studios, Praxen, Fotografen und lokale Dienstleister in DACH.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Drei Pakete, feste Preise</h2>
    <p class="scrollhint">&larr; quer wischen f&uuml;r alle Pakete &rarr;</p>
    <div class="tablewrap">
    <table class="compare">
      <thead><tr><th>Enthalten</th><th>Basis<span>890 &euro;</span></th><th>Standard<span>1.590 &euro;</span></th><th>Premium<span>2.390 &euro;</span></th></tr></thead>
      <tbody>{rows_html}</tbody>
    </table>
    </div>
    <p class="note">Festpreise. Kein Ausweis der Umsatzsteuer gem&auml;&szlig; &sect;&nbsp;19 UStG.</p>
  </div>
</section>

<section class="section alt">
  <div class="wrap narrow">
    <h2>Welches Paket passt</h2>
    <p><strong>Basis</strong> – wenn du erst einmal &uuml;berhaupt im Netz auffindbar sein willst. Eine Seite mit allem Wichtigen. Reicht f&uuml;r viele Handwerksbetriebe und kleine Studios v&ouml;llig aus.</p>
    <p><strong>Standard</strong> – der Normalfall. Mehrere Seiten, deine Texte in Form gebracht, Bilder aufbereitet und die Grundlagen daf&uuml;r, dass Google dich bei &bdquo;deine Leistung + deine Stadt&ldquo; findet.</p>
    <p><strong>Premium</strong> – wenn die Website Arbeit abnehmen soll: Speisekarte, Kursplan oder Portfolio als echte Seite statt PDF, Reservierung oder Terminanfrage direkt eingebunden, alle Texte von mir geschrieben.</p>

    <h2>Aufpreise</h2>
    <ul class="checks">
      <li>Zus&auml;tzliche Seite 190 &euro;</li>
      <li>Weitere Korrekturrunde 90 &euro;</li>
      <li>Texte schreiben statt &uuml;berarbeiten 120 &euro; je Seite</li>
      <li>Terminbuchung anbinden 190 &euro;</li>
      <li>Logo-Wortmarke 149 &euro;</li>
      <li>Express, halbe Lieferzeit: +50 %</li>
    </ul>
    <p class="note">Braucht dein Projekt mehr als das Premium-Paket, kalkuliere ich einen Festpreis – frag einfach an.</p>

    <h2>Kein Abo, kein Shopify n&ouml;tig</h2>
    <p>Die Seite wird einmal gebaut und komplett an dich &uuml;bergeben – alle Dateien, alle Zug&auml;nge. Du zahlst keine monatliche Geb&uuml;hr an mich. Laufende Kosten entstehen nur f&uuml;r Domain und Hosting bei deinem Anbieter, &uuml;blicherweise zwischen 5 und 15 &euro; im Monat.</p>

    <h2>Relaunch einer bestehenden Seite</h2>
    <p>Dieselben Pakete, dieselben Preise. Deine Adresse bleibt, Texte und Bilder &uuml;bernehme ich, alte Links leite ich um. Schick mir die Adresse deiner jetzigen Seite, ich sage dir ehrlich, ob sich der Aufwand lohnt.</p>

    <h2>&Auml;nderungen nach dem Live-Gang</h2>
    <p>12 Monate lang sind &Auml;nderungen enthalten: Texte, Preise, &Ouml;ffnungszeiten, Bilder, Speisekarte. Schick sie mir per Mail oder Nachricht, ich setze sie in zwei bis drei Werktagen um, bis zu vier &Auml;nderungen im Monat. Neue Seiten oder neue Funktionen rechne ich nach Aufwand ab. Danach kostet eine &Auml;nderung ab 30 &euro;.</p>

    <h2>Was nicht enthalten ist</h2>
    <p>Erstellung von Impressum, Datenschutzerkl&auml;rung und AGB &middot; Fotografie und Bildlizenzen &middot; Domain- und Hostinggeb&uuml;hren &middot; laufende Betreuung nach der &Uuml;bergabe &middot; Werbung und fortlaufende Suchmaschinenoptimierung. Und keine Versprechen zu Umsatz oder Google-Platzierungen.</p>
    <p><a class="btn" href="anfrage.html">Projekt anfragen</a></p>
  </div>
</section>

{ABLAUF_BLOCK}
"""
page("leistungen.html", "Website erstellen lassen – Pakete und Preise ab 890 &euro;",
     "Drei feste Pakete f&uuml;r individuelle Websites: 890 €, 1.590 € und 2.390 €. Alle Leistungen im Vergleich, Aufpreise und Ablauf.",
     "leistungen.html", leistungen_body, rang=0.9)

# Ablauf
ablauf_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">So l&auml;uft es ab</span>
    <h1>Von der Anfrage bis zur fertigen Seite</h1>
    <p class="lead">Du musst nichts k&ouml;nnen und kaum etwas tun. Der gr&ouml;&szlig;te Teil deiner Arbeit ist das Briefing, und das dauert 15 bis 20 Minuten.</p>
  </div>
</section>
{ABLAUF_BLOCK}
<section class="section">
  <div class="wrap narrow">
    <h2>Was ich von dir brauche</h2>
    <ul class="checks">
      <li>Was dein Betrieb macht und f&uuml;r wen</li>
      <li>Kontaktdaten, &Ouml;ffnungszeiten, Anfahrt</li>
      <li>Bilder, sofern vorhanden – sonst besprechen wir das</li>
      <li>Deine Texte, falls du welche hast. Beim Premium-Paket schreibe ich sie</li>
      <li>Impressum, Datenschutzerkl&auml;rung und AGB</li>
    </ul>
    <h2>Und danach?</h2>
    <p>Nach der &Uuml;bergabe geh&ouml;rt dir alles. Du kannst die Seite selbst weiterpflegen oder mir Bescheid geben – kleine &Auml;nderungen &uuml;bernehme ich gegen Aufpreis nach Aufwand. Einen Wartungsvertrag musst du nicht abschlie&szlig;en.</p>
    <p><a class="btn" href="anfrage.html">Projekt anfragen</a></p>
  </div>
</section>
"""
page("ablauf.html", "So l&auml;uft ein Website-Projekt ab",
     "Von der Anfrage &uuml;ber Briefing und Entwurf bis zur &Uuml;bergabe – der Ablauf eines Website-Projekts bei ORD&Eacute; in f&uuml;nf Schritten.",
     "ablauf.html", ablauf_body)

# Referenzen
demos = "".join(demo_card(b) for b in BRANCHEN if b["demo"])
ref_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Beispiele</span>
    <h1>Komplette Seiten zum Anschauen</h1>
    <p class="lead">Keine Bildchen, sondern echte Websites, die du anklicken und auf dem Handy testen kannst. Alle Betriebe sind erfunden, die Seiten sind echt gebaut.</p>
  </div>
</section>
<section class="section">
  <div class="wrap"><div class="demogrid reveal-group">{demos}</div></div>
</section>
{PAKETE_KURZ}
"""
page("referenzen.html", "Beispiele – so sehen die Websites aus",
     "Live-Beispiele f&uuml;r Restaurant-, Friseur-, Fitness- und Fotografen-Websites von ORD&Eacute;. Komplett gebaut, direkt anklickbar.",
     "referenzen.html", ref_body, rang=0.8)

# Anfrage
opts = "".join(f'<option>{b["nav"]}</option>' for b in BRANCHEN)
anfrage_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Projekt anfragen</span>
    <h1>Erz&auml;hl mir kurz von deinem Betrieb</h1>
    <p class="lead">Ich melde mich innerhalb eines Werktags. Wenn es passt, baue ich dir einen echten Entwurf deiner Startseite – kostenlos und unverbindlich. Erst wenn der dir gef&auml;llt, reden wir &uuml;ber den Auftrag.</p>
  </div>
</section>
<section class="section">
  <div class="wrap narrow">
    <div class="wabox">
      <div>
        <h2 style="margin-top:0">Lieber kurz schreiben?</h2>
        <p class="note" style="margin:0">Schick mir einfach eine Nachricht per WhatsApp. Meist antworte ich noch am selben Tag.</p>
      </div>
      <a class="btn wa" href="{WA_LINK}" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.02c-.24.68-1.2 1.26-1.97 1.42-.53.11-1.21.2-3.51-.75-2.95-1.22-4.84-4.2-4.99-4.4-.14-.2-1.19-1.58-1.19-3.02s.76-2.14 1.03-2.43c.27-.29.58-.36.78-.36l.56.01c.18.01.42-.07.66.5.24.58.83 2.01.9 2.16.07.14.12.31.02.51-.1.2-.15.32-.29.49-.15.17-.31.38-.44.51-.14.14-.29.3-.13.58.17.29.75 1.23 1.6 2 1.1.98 2.03 1.28 2.32 1.42.29.15.46.12.63-.07.17-.2.72-.84.91-1.13.19-.29.39-.24.65-.14.26.09 1.68.79 1.97.94.29.14.48.22.55.34.07.12.07.69-.17 1.37z"/></svg>WhatsApp &ouml;ffnen</a>
    </div>
    <p class="oder"><span>oder per Formular</span></p>
    <p class="formfehler" id="formFehler" hidden>Da ist etwas schiefgegangen &mdash; bitte pr&uuml;f kurz deine E-Mail-Adresse und den H&auml;kchen-Hinweis, oder schreib mir direkt an <a href="mailto:{MAIL}">{MAIL}</a>.</p>
    <form class="form" action="kontakt.php" method="POST">
      <div class="falle" aria-hidden="true"><label>Bitte dieses Feld leer lassen<input type="text" name="website_url" tabindex="-1" autocomplete="off"></label></div>
      <input type="hidden" name="gestartet" value="">
      <label>Name<input type="text" name="name" required></label>
      <label>Betrieb<input type="text" name="betrieb"></label>
      <label>E-Mail<input type="email" name="email" required></label>
      <label>Telefon, optional<input type="tel" name="telefon"></label>
      <label>Branche<select name="branche">{opts}<option>Andere Branche</option></select></label>
      <label>Hast du schon eine Website? Dann hier die Adresse<input type="text" name="bestehende_seite" placeholder="z.&nbsp;B. www.mein-betrieb.de"></label>
      <label>Wunschpaket<select name="paket"><option>Basis – 890 &euro;</option><option>Standard – 1.590 &euro;</option><option>Premium – 2.390 &euro;</option><option>Wei&szlig; ich noch nicht</option></select></label>
      <label>Worum geht es?<textarea name="nachricht" rows="6" placeholder="Was macht dein Betrieb, was soll die Website k&ouml;nnen, gibt es schon eine Seite?" required></textarea></label>
      <label class="check"><input type="checkbox" name="datenschutz" required> Ich habe die <a href="datenschutz.html">Datenschutzerkl&auml;rung</a> gelesen und bin mit der Verarbeitung meiner Angaben zur Bearbeitung der Anfrage einverstanden.</label>
      <p class="klein-hinweis">Die Anfrage ist unverbindlich und noch kein Auftrag. Verbraucher haben nach Vertragsschluss ein <a href="widerruf.html">14-t&auml;giges Widerrufsrecht</a>.</p>
      <button class="btn big" type="submit">Kostenlosen Entwurf anfordern</button>
    </form>
    <p class="note">Lieber per Mail? <a href="mailto:{MAIL}">{MAIL}</a> &middot; Telefon: <a href="tel:{TEL_LINK}">{TEL_ANZEIGE}</a></p>
  </div>
</section>
"""
danke_body = f"""
<section class="pagehead"><div class="wrap">
<h1>Danke &mdash; deine Anfrage ist da</h1>
<p class="lead">Ich melde mich innerhalb eines Werktags bei dir, meist schneller.</p>
</div></section>
<section class="section"><div class="wrap narrow">
<p>Solltest du nichts h&ouml;ren, schau bitte kurz in deinen Spam-Ordner oder schreib mir direkt:</p>
<p><a class="btn wa" href="{WA_LINK}" rel="noopener">Per WhatsApp schreiben</a></p>
<p class="note">Oder per Mail an <a href="mailto:{MAIL}">{MAIL}</a> &middot; Telefon <a href="tel:{TEL_LINK}">{TEL_ANZEIGE}</a></p>
<p><a href="index.html">&larr; Zur&uuml;ck zur Startseite</a></p>
</div></section>
"""
page("danke.html", "Danke f&uuml;r deine Anfrage",
     "Deine Anfrage bei ORD&Eacute; ist eingegangen. Ich melde mich innerhalb eines Werktags.",
     "", danke_body, rang=0.1)

page("anfrage.html", "Projekt anfragen",
     "Unverbindlich anfragen: Ich melde mich innerhalb eines Werktags mit einer ehrlichen Einsch&auml;tzung und dem Festpreis f&uuml;r deine Website.",
     "anfrage.html", anfrage_body, rang=0.8)

# ---------------------------------------------------------------- Ueber mich
ueber_body = """
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">&Uuml;ber ORD&Eacute;</span>
    <h1>Wer hinter ORD&Eacute; steckt</h1>
    <p class="lead">Kein Callcenter, keine Agentur mit f&uuml;nf Ansprechpartnern. Du redest immer mit derselben Person.</p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>Hallo, ich bin Artur</h2>
    <p>Ich baue Websites f&uuml;r kleine Betriebe: Restaurants, Salons, Studios, Praxen, Fotografen und Handwerk. Angefangen habe ich mit meinem eigenen Onlineshop &ndash; da habe ich gelernt, wie viel Unterschied eine Seite macht, die man versteht und auf dem Handy bedienen kann.</p>
    <p class="incl"><strong>Noch auszuf&uuml;llen:</strong> Hier fehlen zwei bis drei S&auml;tze von dir &mdash; warum du das machst und was dich antreibt. Ruhig pers&ouml;nlich, das liest man gern. Danach diesen Hinweis l&ouml;schen.</p>

    <h2>Wie ich arbeite</h2>
    <ul class="checks">
      <li>Du bekommst einen Entwurf, bevor du dich entscheidest</li>
      <li>Festpreis, bevor die Arbeit anf&auml;ngt &ndash; keine Nachforderung</li>
      <li>Ich sage auch ab, wenn ich merke, dass mein Angebot nicht zu dir passt</li>
      <li>Keine Fachbegriffe, wenn es auch anders geht</li>
    </ul>

    <h2>Warum kein gro&szlig;es Team</h2>
    <p>Weil klein sein hier ein Vorteil ist. Du erkl&auml;rst dein Anliegen einmal, nicht dreimal. Und wenn du in einem halben Jahr etwas ge&auml;ndert haben willst, schreibst du derselben Person, die die Seite gebaut hat.</p>
    <p>Daf&uuml;r nehme ich nur eine begrenzte Zahl an Projekten gleichzeitig an. Wenn es gerade voll ist, sage ich dir das ehrlich, statt dich hinzuhalten.</p>

    <h2>Womit ich baue</h2>
    <p>Kein WordPress, kein Baukasten. Deine Seite wird fest gebaut: schnell, sicher und ohne Updates, die jemand einspielen muss. Was das f&uuml;r dich bedeutet, steht bei den <a href="leistungen.html">Leistungen</a>.</p>

    <p><a class="btn" href="anfrage.html">Kostenlosen Entwurf anfordern</a> <a class="btn ghost" href="referenzen.html">Beispiele ansehen</a></p>
  </div>
</section>
"""
page("ueber-mich.html", "&Uuml;ber ORD&Eacute; &ndash; wer die Websites baut",
     "Wer hinter ORD&Eacute; steckt und wie ich arbeite: ein Entwurf vor der Entscheidung, Festpreis vorab und eine feste Ansprechperson.",
     "", ueber_body,
     schema=schema_brotkrumen(("Start", "index.html"), ("&Uuml;ber ORD&Eacute;", "ueber-mich.html")),
     rang=0.7)


# ---------------------------------------------------------------- Ratgeber: Was kostet eine Website
KOSTEN_FAQ = [
  ("Was kostet eine Website f&uuml;r einen kleinen Betrieb?",
   "In Deutschland liegen professionell gebaute Websites f&uuml;r kleine Betriebe &uuml;blicherweise zwischen 800 und 3.000 Euro. Baukastenseiten gibt es ab etwa 150 Euro, gro&szlig;e Agenturprojekte beginnen oft erst bei 5.000 Euro."),
  ("Was kostet eine Website monatlich?",
   "F&uuml;r Domain und Hosting zahlst du &uuml;blicherweise 5 bis 15 Euro im Monat. Dazu kommen je nach Anbieter Wartungsvertr&auml;ge, die es bei fest gebauten Seiten aber nicht braucht."),
  ("Warum sind die Preise so unterschiedlich?",
   "Weil sehr Unterschiedliches darunter f&auml;llt: eine gekaufte Vorlage mit getauschten Farben, eine individuell gebaute Seite oder ein Projekt mit Shop und Anbindungen. Entscheidend ist, wie viel Arbeit in Aufbau, Texten und Bildern steckt."),
  ("Was ist teurer, einmalig zahlen oder ein Abo?",
   "Auf zwei bis drei Jahre gerechnet ist ein Abo meist teurer. Bei 49 Euro im Monat zahlst du in drei Jahren rund 1.760 Euro und die Seite geh&ouml;rt dir am Ende trotzdem nicht."),
  ("Lohnt sich eine Website f&uuml;r einen kleinen Betrieb &uuml;berhaupt?",
   "Wenn Kunden dich vorher online suchen, ja. Das trifft auf Gastronomie, Friseure, Praxen und Handwerk fast immer zu. Wenn du ausschlie&szlig;lich &uuml;ber Empfehlungen arbeitest und ausgelastet bist, eher nicht."),
]

kosten_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Ratgeber</span>
    <h1>Was kostet eine Website?</h1>
    <p class="lead">Ehrliche Einordnung statt &bdquo;ab 9,90 Euro&ldquo;. Was die Spannen bedeuten, was dahintersteckt und was davon du wirklich brauchst.</p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>Die &uuml;blichen Preisklassen</h2>
    <p>Wenn du nach Preisen suchst, findest du alles zwischen 9 Euro und 15.000 Euro. Das liegt daran, dass ganz verschiedene Dinge gemeint sind. Grob lassen sie sich so einteilen:</p>

    <div class="tablewrap">
    <table class="compare">
      <thead><tr><th>Was du bekommst</th><th>Preis<span>einmalig</span></th><th>Laufend<span>pro Monat</span></th></tr></thead>
      <tbody>
        <tr><th scope="row">Baukasten, selbst gemacht</th><td>0 &euro;</td><td>10&ndash;30 &euro;</td></tr>
        <tr><th scope="row">Gekaufte Vorlage, eingerichtet</th><td>150&ndash;600 &euro;</td><td>10&ndash;30 &euro;</td></tr>
        <tr><th scope="row">Individuell gebaut, kleiner Anbieter</th><td>800&ndash;3.000 &euro;</td><td>5&ndash;15 &euro;</td></tr>
        <tr><th scope="row">Agentur mit Team</th><td>ab 5.000 &euro;</td><td>ab 50 &euro;</td></tr>
        <tr><th scope="row">Abo-Modell &bdquo;Website mieten&ldquo;</th><td>0&ndash;500 &euro;</td><td>39&ndash;99 &euro;</td></tr>
      </tbody>
    </table>
    </div>
    <p class="note">Richtwerte f&uuml;r Deutschland, Stand 2026. Was du am Ende zahlst, h&auml;ngt vom Umfang ab.</p>

    <h2>Der Haken beim Abo</h2>
    <p>Abo-Angebote sehen g&uuml;nstig aus, weil der Einstieg wenig kostet. Rechne es aber auf drei Jahre: 49 Euro im Monat sind rund 1.760 Euro. Daf&uuml;r bek&auml;mst du an anderer Stelle eine individuell gebaute Seite, die dir dann auch geh&ouml;rt.</p>
    <p>Wichtiger als der Preis ist die Frage: Was passiert, wenn du k&uuml;ndigst? Bei vielen Abo-Anbietern ist die Seite dann weg, samt Texten und Bildern.</p>

    <h2>Wovon der Preis wirklich abh&auml;ngt</h2>
    <ul class="checks">
      <li><strong>Anzahl der Seiten.</strong> Eine Seite ist deutlich weniger Arbeit als sieben.</li>
      <li><strong>Texte.</strong> Ob du sie lieferst oder jemand sie schreibt, macht den gr&ouml;&szlig;ten Unterschied.</li>
      <li><strong>Bilder.</strong> Eigene Fotos sparen Geld, Bildbearbeitung kostet Zeit.</li>
      <li><strong>Funktionen.</strong> Terminbuchung, Reservierung oder Shop sind Aufwand, eine Kontaktseite nicht.</li>
      <li><strong>Wie oft nachgebessert wird.</strong> Deshalb sind Korrekturrunden meist begrenzt.</li>
    </ul>

    <h2>Was du nicht bezahlen solltest</h2>
    <p>Versprechen zu Platz eins bei Google. Das kann niemand garantieren, auch nicht gegen Aufpreis. Seri&ouml;se Anbieter sagen dir, dass sie die Grundlagen sauber setzen, mehr nicht.</p>
    <p>Und Wartungsvertr&auml;ge f&uuml;r Seiten, die keine Wartung brauchen. Bei WordPress sind Updates n&ouml;tig, bei fest gebauten Seiten nicht.</p>

    <h2>Unsere Preise</h2>
    <p>Damit du eine konkrete Zahl hast: Bei ORD&Eacute; kostet eine Seite <strong>890 Euro</strong>, bis zu vier Seiten <strong>1.590 Euro</strong> und bis zu sieben Seiten <strong>2.390 Euro</strong>. Einmalig, mit 12 Monaten &Auml;nderungen inklusive und ohne Abo. Die Aufschl&uuml;sselung steht bei den <a href="leistungen.html">Leistungen</a>.</p>

    <h2>H&auml;ufige Fragen</h2>
    {faq([(f, a) for f, a in KOSTEN_FAQ])}

    <p style="margin-top:2em"><a class="btn" href="anfrage.html">Kostenlosen Entwurf anfordern</a></p>
  </div>
</section>
"""
page("was-kostet-eine-website.html", "Was kostet eine Website? Preise 2026 im &Uuml;berblick",
     "Was eine Website f&uuml;r einen kleinen Betrieb kostet: Preisklassen von Baukasten bis Agentur, versteckte Kosten bei Abo-Modellen und wovon der Preis wirklich abh&auml;ngt.",
     "", kosten_body,
     schema=schema_faq(KOSTEN_FAQ) + schema_brotkrumen(("Start", "index.html"), ("Was kostet eine Website", "was-kostet-eine-website.html")),
     rang=0.8)


# ---------------------------------------------------------------- Stadtseiten
STAEDTE = [
    {"slug": "webdesign-landsberg", "stadt": "Landsberg am Lech",
     "um": "Kaufering, Penzing, Igling, Sch&ouml;ffelding und dem gesamten Landkreis",
     "text": "Landsberg ist meine Heimatstadt. Hier kenne ich die Gegend, die Betriebe und die Wege &ndash; wenn es sein muss, komme ich pers&ouml;nlich vorbei."},
    {"slug": "webdesign-augsburg", "stadt": "Augsburg",
     "um": "Friedberg, K&ouml;nigsbrunn, Gersthofen und Neus&auml;&szlig;",
     "text": "Augsburg ist gro&szlig; genug f&uuml;r viel Wettbewerb und klein genug, dass Kunden ihre Betriebe noch pers&ouml;nlich aussuchen. Genau daf&uuml;r baue ich Seiten."},
    {"slug": "webdesign-muenchen", "stadt": "M&uuml;nchen",
     "um": "F&uuml;rstenfeldbruck, Germering, Starnberg und dem gesamten Umland",
     "text": "In M&uuml;nchen zahlen viele Betriebe Agenturpreise f&uuml;r Seiten, die sie so nicht brauchen. Bei mir bekommst du dieselbe Qualit&auml;t zum Festpreis."},
]

for st in STAEDTE:
    stadt_body = f"""
<section class="pagehead">
  <div class="wrap">
    <span class="kicker">Webdesign &middot; {st['stadt']}</span>
    <h1>Website erstellen lassen in {st['stadt']}</h1>
    <p class="lead">Individuell gebaute Websites f&uuml;r Betriebe in {st['stadt']} und Umgebung. Festpreis ab 890&nbsp;&euro;, kein Abo, 12 Monate &Auml;nderungen inklusive.</p>
    <p><a class="btn" href="anfrage.html">Kostenlosen Entwurf anfordern</a> <a class="btn ghost" href="referenzen.html">Beispiele ansehen</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>F&uuml;r Betriebe in {st['stadt']} und Umgebung</h2>
    <p>{st['text']}</p>
    <p>Ich arbeite f&uuml;r Betriebe in {st['stadt']} sowie in {st['um']}. Die Zusammenarbeit l&auml;uft meist online &ndash; du schickst mir Texte und Bilder, ich baue die Seite und du bekommst einen Link zum Anschauen. Wenn dir ein pers&ouml;nliches Treffen lieber ist, l&auml;sst sich das in der Regel einrichten.</p>

    <h2>Welche Betriebe</h2>
    <p>Restaurants und Caf&eacute;s, Friseure und Kosmetikstudios, Fitness- und Yogastudios, Arzt- und Therapiepraxen, Fotografen sowie Handwerk und lokale Dienstleister. Was auf die jeweilige Seite geh&ouml;rt, steht auf den <a href="branchen.html">Branchenseiten</a>.</p>

    {branch_links()}

    <h2>Was du bekommst</h2>
    <ul class="checks">
      <li>Einen kostenlosen Entwurf deiner Startseite, bevor du dich entscheidest</li>
      <li>Eine Seite, die auf dem Handy genauso gut aussieht wie am Rechner</li>
      <li>Die Grundlagen daf&uuml;r, dass Google dich bei &bdquo;deine Leistung + {st['stadt']}&ldquo; findet</li>
      <li>12 Monate &Auml;nderungen inklusive &ndash; du schickst sie mir, ich setze sie um</li>
      <li>Vollst&auml;ndige &Uuml;bergabe: alle Dateien und Zug&auml;nge geh&ouml;ren dir</li>
    </ul>

    <h2>Was es kostet</h2>
    <p><strong>890&nbsp;&euro;, 1.590&nbsp;&euro; oder 2.390&nbsp;&euro;</strong> &ndash; je nach Anzahl der Seiten. Einmalig, ohne Abo. Wie sich das zusammensetzt, steht bei den <a href="leistungen.html">Leistungen</a>, und warum Preise so weit auseinandergehen, erkl&auml;re ich im Ratgeber <a href="was-kostet-eine-website.html">Was kostet eine Website?</a></p>

    <p><a class="btn" href="anfrage.html">Projekt anfragen</a></p>
  </div>
</section>
"""
    page(st["slug"] + ".html",
         f"Webdesign {st['stadt']} &ndash; Website erstellen lassen ab 890 &euro;",
         f"Individuell gebaute Websites f&uuml;r Betriebe in {st['stadt']} und Umgebung. Festpreis ab 890 Euro, kein Abo, kostenloser Entwurf vorab.",
         "", stadt_body,
         schema=schema_brotkrumen(("Start", "index.html"), (f"Webdesign {st['stadt']}", st["slug"] + ".html")),
         rang=0.8)


# ---------------------------------------------------------------- Rechtliches
IMPRESSUM = f"""
<section class="pagehead"><div class="wrap"><h1>Impressum</h1>
<p class="lead">Angaben gem&auml;&szlig; &sect;&nbsp;5 DDG</p></div></section>
<section class="section"><div class="wrap narrow">
<h2>Anbieter</h2>
<p>Artur Missal<br>
Ahornallee 4d<br>
86899 Landsberg am Lech<br>
Deutschland</p>

<h2>Kontakt</h2>
<p>Telefon: {TEL_ANZEIGE}<br>
E-Mail: <a href="mailto:hello@ordeshop.net">hello@ordeshop.net</a></p>

<h2>Umsatzsteuer</h2>
<p>Als Kleinunternehmer im Sinne von &sect;&nbsp;19 UStG wird keine Umsatzsteuer berechnet und daher keine Umsatzsteuer-Identifikationsnummer gef&uuml;hrt.</p>

<h2>Verantwortlich f&uuml;r den Inhalt</h2>
<p>Artur Missal, Anschrift wie oben.</p>

<h2>Streitbeilegung</h2>
<p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen (&sect; 36 VSBG).</p>

<h2>Bildnachweis</h2>
<p>Die auf den Beispielseiten gezeigten Betriebe sind frei erfunden. Die Bilder wurden mit KI erzeugt.</p>
</div></section>
"""

RECHT_OFFEN = """
<section class="pagehead"><div class="wrap"><h1>{h}</h1></div></section>
<section class="section"><div class="wrap narrow">
<p class="incl"><strong>Diese Seite ist noch leer.</strong> {hinweis}</p>
<p>Bis dahin erreichst du mich unter <a href="mailto:hello@ordeshop.net">hello@ordeshop.net</a>.</p>
</div></section>
"""

page("impressum.html", "Impressum",
     "Impressum und Anbieterkennzeichnung von ORD&Eacute;.", "", IMPRESSUM)

# ---------------------------------------------------------------
# Datenschutzerklaerung
#
# HOSTER traegt den Namen des Hosting-Anbieters. Solange dort der
# Platzhalter steht, ist die Erklaerung unvollstaendig: der Hoster
# ist Empfaenger der Daten und muss nach Art. 13 DSGVO genannt werden.
# ---------------------------------------------------------------
HOSTER = ("Hostinger International Ltd., 61 Lordou Vironos Street, "
          "6023 Larnaca, Zypern")

DATENSCHUTZ = f"""
<section class="pagehead"><div class="wrap">
<h1>Datenschutzerkl&auml;rung</h1>
<p class="lead">Wie diese Website mit personenbezogenen Daten umgeht.</p>
</div></section>
<section class="section"><div class="wrap narrow">

<h2>1. Verantwortlicher</h2>
<p>Verantwortlich f&uuml;r die Datenverarbeitung auf dieser Website ist:</p>
<p>Artur Missal<br>
Ahornallee 4d<br>
86899 Landsberg am Lech<br>
Deutschland</p>
<p>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a><br>
Telefon: <a href="tel:{TEL_LINK}">{TEL_ANZEIGE}</a></p>
<p>Ein Datenschutzbeauftragter ist nicht bestellt, da die gesetzlichen Voraussetzungen daf&uuml;r nicht vorliegen.</p>

<h2>2. Kurz gefasst</h2>
<p>Diese Website ist eine einfache, fest gebaute Seite. Sie setzt <strong>keine Cookies</strong>, bindet <strong>keine Analyse- oder Werbewerkzeuge</strong> ein und l&auml;dt <strong>keine Inhalte von fremden Servern</strong> nach. Daten entstehen nur dort, wo Sie selbst Kontakt aufnehmen &mdash; und in den technischen Protokollen des Servers.</p>

<h2>3. Aufruf der Website und Server-Protokolle</h2>
<p>Beim Aufruf dieser Website &uuml;bertr&auml;gt Ihr Browser automatisch Daten an den Server. Diese werden vor&uuml;bergehend in einer Protokolldatei gespeichert:</p>
<ul>
<li>IP-Adresse des anfragenden Ger&auml;ts</li>
<li>Datum und Uhrzeit des Zugriffs</li>
<li>Name und URL der abgerufenen Datei</li>
<li>&uuml;bertragene Datenmenge</li>
<li>Meldung, ob der Abruf erfolgreich war</li>
<li>Browsertyp, Browserversion und Betriebssystem</li>
<li>die zuvor besuchte Seite, sofern &uuml;bermittelt</li>
</ul>
<p><strong>Zweck:</strong> Auslieferung der Website, Sicherstellung der Stabilit&auml;t und Sicherheit des Servers sowie Aufkl&auml;rung von Missbrauch.</p>
<p><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO. Das berechtigte Interesse besteht darin, die Website technisch fehlerfrei und sicher bereitzustellen.</p>
<p><strong>Speicherdauer:</strong> Die Protokolle werden nach sp&auml;testens sieben Tagen gel&ouml;scht, sofern sie nicht zur Aufkl&auml;rung eines konkreten Vorfalls l&auml;nger ben&ouml;tigt werden.</p>
<p><strong>Hosting:</strong> Die Website wird bei {HOSTER} gehostet. Der Anbieter verarbeitet die genannten Daten in unserem Auftrag. Es besteht ein Vertrag &uuml;ber die Auftragsverarbeitung nach Art. 28 DSGVO.</p>

<h2>4. Kontaktformular</h2>
<p>&Uuml;ber das Formular auf der Seite <a href="anfrage.html">Anfrage</a> k&ouml;nnen Sie uns eine Nachricht senden. Dabei werden die von Ihnen eingegebenen Angaben &uuml;bermittelt: Name, Betrieb, E-Mail-Adresse, Telefonnummer, Branche, eine bereits bestehende Website-Adresse, das gew&uuml;nschte Paket sowie Ihre Nachricht.</p>
<p><strong>Zweck:</strong> Bearbeitung Ihrer Anfrage und Beantwortung.</p>
<p><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. b DSGVO, soweit die Anfrage auf den Abschluss eines Vertrags gerichtet ist. Im &Uuml;brigen Art. 6 Abs. 1 lit. f DSGVO aufgrund unseres berechtigten Interesses an der Beantwortung von Anfragen. Soweit Sie beim Absenden zus&auml;tzlich Ihre Einwilligung erkl&auml;ren, beruht die Verarbeitung auch auf Art. 6 Abs. 1 lit. a DSGVO; diese Einwilligung k&ouml;nnen Sie jederzeit f&uuml;r die Zukunft widerrufen.</p>
<p><strong>Pflichtangaben:</strong> Erforderlich sind Name, E-Mail-Adresse und Ihre Nachricht. Alle weiteren Angaben sind freiwillig und dienen nur dazu, Ihnen ein passendes Angebot machen zu k&ouml;nnen.</p>
<p><strong>Speicherdauer:</strong> Wir speichern Ihre Anfrage, bis sie abschlie&szlig;end bearbeitet ist. Kommt ein Vertrag zustande, gelten die gesetzlichen Aufbewahrungsfristen, insbesondere aus Handels- und Steuerrecht.</p>

<h2>5. Kontakt per E-Mail und Telefon</h2>
<p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten wir Ihre Angaben ausschlie&szlig;lich zur Bearbeitung Ihres Anliegens. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b beziehungsweise lit. f DSGVO. Es gelten dieselben Speicherfristen wie unter Punkt 4.</p>

<h2>6. Kontakt &uuml;ber WhatsApp</h2>
<p>Auf dieser Website finden Sie einen Link, &uuml;ber den Sie uns per WhatsApp schreiben k&ouml;nnen. Der Link selbst &uuml;bertr&auml;gt noch keine Daten an WhatsApp; eine Verbindung entsteht erst, wenn Sie ihn anklicken.</p>
<p>Nutzen Sie diesen Weg, werden Ihre Nachricht und Ihre Rufnummer &uuml;ber die Server von WhatsApp Ireland Limited, Merrion Road, Dublin 4, Irland verarbeitet. Dabei k&ouml;nnen Daten auch an Server des Mutterkonzerns Meta in den USA &uuml;bermittelt werden. Auf Art und Umfang dieser Verarbeitung haben wir keinen Einfluss. Rechtsgrundlage f&uuml;r die Verarbeitung Ihrer Nachricht auf unserer Seite ist Art. 6 Abs. 1 lit. b beziehungsweise lit. f DSGVO.</p>
<p>Wenn Sie das vermeiden m&ouml;chten, nutzen Sie bitte das Kontaktformular, die E-Mail-Adresse oder das Telefon.</p>

<h2>7. Schriftarten</h2>
<p>Die verwendeten Schriftarten liegen auf unserem eigenen Server und werden von dort geladen. Es wird <strong>keine Verbindung zu Google Fonts</strong> oder einem anderen externen Anbieter aufgebaut. Ihre IP-Adresse wird dadurch nicht an Dritte &uuml;bertragen.</p>

<h2>8. Keine Cookies, keine Analyse, keine Werbung</h2>
<p>Diese Website setzt keine Cookies und verwendet keine vergleichbaren Techniken, die Informationen auf Ihrem Ger&auml;t speichern oder auslesen. Es kommen keine Analyse-Werkzeuge wie Google Analytics, keine Werbenetzwerke und keine Besucherz&auml;hler zum Einsatz. Ein Einwilligungsbanner ist deshalb nicht erforderlich.</p>
<p>Die Website speichert lediglich w&auml;hrend Ihres Besuchs im Browser, ob die Startanimation bereits gezeigt wurde. Diese Information verl&auml;sst Ihr Ger&auml;t nicht und wird beim Schlie&szlig;en des Browsers gel&ouml;scht.</p>

<h2>9. Weitergabe an Dritte</h2>
<p>Ihre Daten werden nicht verkauft und nicht zu Werbezwecken weitergegeben. Eine &Uuml;bermittlung erfolgt nur</p>
<ul>
<li>an den unter Punkt 3 genannten Hosting-Anbieter als Auftragsverarbeiter,</li>
<li>an WhatsApp, wenn Sie diesen Kontaktweg selbst w&auml;hlen (Punkt 6),</li>
<li>an unser Steuerb&uuml;ro und Beh&ouml;rden, soweit wir gesetzlich dazu verpflichtet sind.</li>
</ul>

<h2>10. Ihre Rechte</h2>
<p>Sie haben jederzeit das Recht</p>
<ul>
<li>auf Auskunft &uuml;ber die zu Ihnen gespeicherten Daten (Art. 15 DSGVO),</li>
<li>auf Berichtigung unrichtiger Daten (Art. 16 DSGVO),</li>
<li>auf L&ouml;schung (Art. 17 DSGVO),</li>
<li>auf Einschr&auml;nkung der Verarbeitung (Art. 18 DSGVO),</li>
<li>auf Daten&uuml;bertragbarkeit (Art. 20 DSGVO),</li>
<li>auf Widerspruch gegen Verarbeitungen, die auf Art. 6 Abs. 1 lit. f DSGVO beruhen (Art. 21 DSGVO).</li>
</ul>
<p>Haben Sie in eine Verarbeitung eingewilligt, k&ouml;nnen Sie diese Einwilligung jederzeit mit Wirkung f&uuml;r die Zukunft widerrufen.</p>
<p>F&uuml;r alle diese Anliegen gen&uuml;gt eine formlose Nachricht an <a href="mailto:{MAIL}">{MAIL}</a>.</p>

<h2>11. Beschwerderecht</h2>
<p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbeh&ouml;rde zu beschweren. Zust&auml;ndig ist:</p>
<p>Bayerisches Landesamt f&uuml;r Datenschutzaufsicht<br>
Promenade 27<br>
91522 Ansbach</p>

<h2>12. Keine automatisierte Entscheidungsfindung</h2>
<p>Eine automatisierte Entscheidungsfindung einschlie&szlig;lich Profiling nach Art. 22 DSGVO findet nicht statt.</p>

<h2>13. Stand</h2>
<p>Diese Erkl&auml;rung gilt in der hier ver&ouml;ffentlichten Fassung. &Auml;ndert sich die Website technisch, wird sie angepasst.</p>

</div></section>
"""

page("datenschutz.html", "Datenschutzerkl&auml;rung",
     "Datenschutzerkl&auml;rung von ORD&Eacute;.", "", DATENSCHUTZ)

# ---------------------------------------------------------------
# AGB
#
# Der Text steht online, ist aber juristisch NOCH NICHT GEPRUEFT.
# Die offenen Punkte stehen in AGB-ENTWURF.md. Auf False setzen,
# wenn die Seite bis zur IHK-Pruefung wieder verschwinden soll.
# ---------------------------------------------------------------
AGB_ONLINE = True

AGB = """
<section class="pagehead"><div class="wrap">
<h1>Allgemeine Gesch&auml;ftsbedingungen</h1>
<p class="lead">Stand: {stand}</p>
</div></section>
<section class="section"><div class="wrap narrow">

<h2>&sect; 1 Anbieter und Geltungsbereich</h2>
<p>Diese Allgemeinen Gesch&auml;ftsbedingungen gelten f&uuml;r alle Vertr&auml;ge zwischen Artur Missal, Ahornallee 4d, 86899 Landsberg am Lech, Deutschland (nachfolgend &bdquo;ORD&Eacute;&ldquo;) und dem Auftraggeber &uuml;ber die Erstellung von Websites.</p>
<p>Abweichende Bedingungen des Auftraggebers werden nicht Vertragsbestandteil, auch wenn ORD&Eacute; ihnen nicht ausdr&uuml;cklich widerspricht.</p>

<h2>&sect; 2 Leistungsgegenstand</h2>
<p>(1) ORD&Eacute; erstellt f&uuml;r den Auftraggeber eine individuell gestaltete Website. Der Leistungsumfang ergibt sich aus dem gew&auml;hlten Paket und dem schriftlichen Angebot.</p>
<p>(2) Die Erstellung der Website ist eine Werkleistung im Sinne des &sect; 631 BGB.</p>
<p>(3) Die Betreuung nach &sect; 11 ist im Preis enthalten.</p>
<p>(4) ORD&Eacute; sagt keine bestimmten Ums&auml;tze, Besucherzahlen, Anfragen oder Platzierungen in Suchmaschinen zu. Solche Ergebnisse h&auml;ngen von Umst&auml;nden ab, die ORD&Eacute; nicht beeinflussen kann.</p>

<h2>&sect; 3 Ziell&auml;nder</h2>
<p>ORD&Eacute; schlie&szlig;t Vertr&auml;ge ausschlie&szlig;lich mit Auftraggebern mit Sitz oder Wohnsitz in Deutschland, &Ouml;sterreich oder der Schweiz.</p>

<h2>&sect; 4 Angebot, Vertragsschluss und Zahlung</h2>
<p>(1) Die Darstellung der Pakete auf der Website von ORD&Eacute; ist kein bindendes Angebot, sondern eine Aufforderung zur Anfrage.</p>
<p>(2) Nach der Anfrage erstellt ORD&Eacute; ein Angebot in Textform. Der Vertrag kommt zustande, wenn der Auftraggeber dieses Angebot in Textform annimmt.</p>
<p>(3) 50 Prozent des vereinbarten Preises sind mit Vertragsschluss als Anzahlung f&auml;llig. Die restlichen 50 Prozent sind mit der Abnahme nach &sect; 9 f&auml;llig.</p>
<p>(4) Rechnungen sind ohne Abzug innerhalb von 14 Tagen ab Zugang zahlbar.</p>
<p>(5) ORD&Eacute; ist Kleinunternehmer im Sinne des &sect; 19 UStG. Es wird keine Umsatzsteuer ausgewiesen.</p>
<p>(6) ORD&Eacute; beginnt mit der Arbeit, sobald die Anzahlung eingegangen ist und das Briefing nach &sect; 6 vollst&auml;ndig vorliegt.</p>

<h2>&sect; 5 Hosting und Domain</h2>
<p>(1) Hosting und Domain sind nicht im Preis enthalten. Der Auftraggeber schlie&szlig;t diese Vertr&auml;ge im eigenen Namen und auf eigene Rechnung ab.</p>
<p>(2) ORD&Eacute; unterst&uuml;tzt bei der Auswahl und richtet die Website auf dem gew&auml;hlten Hosting ein.</p>
<p>(3) F&uuml;r Verf&uuml;gbarkeit, Ausf&auml;lle, Sicherheit und Datensicherung des Hostings ist der jeweilige Anbieter verantwortlich, nicht ORD&Eacute;.</p>

<h2>&sect; 6 Mitwirkung des Auftraggebers</h2>
<p>(1) Der Auftraggeber stellt ORD&Eacute; alle f&uuml;r die Erstellung erforderlichen Angaben und Unterlagen zur Verf&uuml;gung, insbesondere das ausgef&uuml;llte Briefing, Texte, Bilder, Logo und Kontaktdaten.</p>
<p>(2) Die vereinbarte Lieferzeit beginnt, sobald das vollst&auml;ndige Briefing und die Anzahlung vorliegen.</p>
<p>(3) Verz&ouml;gert sich die Mitwirkung des Auftraggebers, verschiebt sich die Lieferzeit entsprechend.</p>
<p>(4) Reagiert der Auftraggeber trotz zweimaliger Aufforderung in Textform l&auml;nger als 30 Tage nicht auf R&uuml;ckfragen, die f&uuml;r die Fertigstellung erforderlich sind, kann ORD&Eacute; den bis dahin erreichten Stand zur Abnahme stellen.</p>

<h2>&sect; 7 Inhalte des Auftraggebers</h2>
<p>(1) Der Auftraggeber sichert zu, an allen von ihm gelieferten Texten, Bildern, Logos, Marken und sonstigen Inhalten die erforderlichen Rechte zu besitzen.</p>
<p>(2) Verletzt ein vom Auftraggeber geliefertes Element Rechte Dritter, stellt der Auftraggeber ORD&Eacute; von den daraus entstehenden Anspr&uuml;chen frei. Das gilt nicht, soweit der Auftraggeber die Rechtsverletzung nicht zu vertreten hat.</p>

<h2>&sect; 8 Rechtstexte</h2>
<p>(1) Impressum, Datenschutzerkl&auml;rung, AGB und &mdash; soweit erforderlich &mdash; Widerrufsbelehrung des Auftraggebers stellt der Auftraggeber selbst.</p>
<p>(2) ORD&Eacute; bindet diese Texte unver&auml;ndert technisch ein. Eine inhaltliche Pr&uuml;fung findet nicht statt.</p>
<p>(3) ORD&Eacute; erbringt keine Rechtsberatung und keine Rechtsdienstleistung im Sinne des Rechtsdienstleistungsgesetzes.</p>

<h2>&sect; 9 Abnahme und &Uuml;bergabe</h2>
<p>(1) Nach Fertigstellung stellt ORD&Eacute; dem Auftraggeber die Website &uuml;ber einen Vorschau-Link zur Verf&uuml;gung.</p>
<p>(2) Die Zahl der enthaltenen Korrekturrunden ergibt sich aus dem gew&auml;hlten Paket. Jede weitere Korrekturrunde wird gesondert beauftragt und mit 90 Euro berechnet.</p>
<p>(3) Der Auftraggeber nimmt die Website ab, wenn sie vertragsgem&auml;&szlig; erstellt ist. ORD&Eacute; setzt hierf&uuml;r eine Frist von 14 Tagen. Verweigert der Auftraggeber die Abnahme innerhalb dieser Frist nicht unter Angabe mindestens eines Mangels, gilt die Website als abgenommen (&sect; 640 Abs. 2 BGB). Ist der Auftraggeber Verbraucher, weist ORD&Eacute; ihn mit der Fristsetzung ausdr&uuml;cklich auf diese Folge hin.</p>
<p>(4) Nach der Abnahme und vollst&auml;ndiger Zahlung &uuml;bergibt ORD&Eacute; dem Auftraggeber s&auml;mtliche Dateien der Website sowie die zugeh&ouml;rigen Zugangsdaten.</p>

<h2>&sect; 10 Nutzungsrechte</h2>
<p>(1) Mit vollst&auml;ndiger Zahlung r&auml;umt ORD&Eacute; dem Auftraggeber das zeitlich, r&auml;umlich und inhaltlich unbeschr&auml;nkte Recht ein, die erstellte Website zu nutzen, zu ver&auml;ndern und weiterzuentwickeln.</p>
<p>(2) Ausgenommen sind allgemeine Gestaltungs- und Programmbausteine, die ORD&Eacute; unabh&auml;ngig von diesem Auftrag entwickelt hat, insbesondere Layout-Komponenten, Skripte und Code-Bausteine. Diese verbleiben bei ORD&Eacute; und d&uuml;rfen in anderen Projekten weiterverwendet werden. Der Auftraggeber erh&auml;lt daran ein einfaches, zeitlich unbeschr&auml;nktes Nutzungsrecht im Rahmen seiner Website.</p>
<p>(3) Bis zur vollst&auml;ndigen Zahlung bleiben alle Nutzungsrechte bei ORD&Eacute;.</p>
<p>(4) ORD&Eacute; darf die erstellte Website unter Nennung des Auftraggebers als Referenz benennen und abbilden. Der Auftraggeber kann dem jederzeit in Textform widersprechen.</p>

<h2>&sect; 11 Betreuung</h2>
<p>(1) F&uuml;r zw&ouml;lf Monate ab Abnahme sind kleine Inhalts&auml;nderungen im Preis enthalten. Dazu geh&ouml;ren insbesondere &Auml;nderungen an Texten, der Austausch von Bildern sowie die Aktualisierung von &Ouml;ffnungszeiten, Preisen, Speisekarten, Kontaktdaten und Team-Angaben.</p>
<p>(2) Nicht enthalten sind insbesondere neue Unterseiten, neue Funktionen, eine Umgestaltung des Layouts, die Anbindung weiterer Systeme, der Umzug auf ein anderes Hosting sowie die Wiederherstellung nach Eingriffen Dritter.</p>
<p>(3) Enthalten sind bis zu vier &Auml;nderungen je Kalendermonat. Nicht genutzte &Auml;nderungen werden nicht auf den Folgemonat &uuml;bertragen.</p>
<p>(4) &Auml;nderungsw&uuml;nsche richtet der Auftraggeber in Textform an ORD&Eacute;. Sie werden in der Regel innerhalb von zwei bis drei Werktagen umgesetzt.</p>
<p>(5) Leistungen au&szlig;erhalb von Absatz 1 werden nach Aufwand abgerechnet und vor Beginn als Angebot in Textform mitgeteilt.</p>
<p>(6) Nach Ablauf der zw&ouml;lf Monate k&ouml;nnen &Auml;nderungen weiterhin beauftragt werden. Eine &Auml;nderung kostet ab 30 Euro; ma&szlig;geblich ist das vorab mitgeteilte Angebot.</p>

<h2>&sect; 12 Haftung</h2>
<p>(1) ORD&Eacute; haftet unbeschr&auml;nkt f&uuml;r Vorsatz und grobe Fahrl&auml;ssigkeit sowie f&uuml;r Sch&auml;den aus der Verletzung des Lebens, des K&ouml;rpers oder der Gesundheit.</p>
<p>(2) Bei leichter Fahrl&auml;ssigkeit haftet ORD&Eacute; nur bei der Verletzung einer wesentlichen Vertragspflicht, also einer Pflicht, deren Erf&uuml;llung die ordnungsgem&auml;&szlig;e Durchf&uuml;hrung des Vertrags &uuml;berhaupt erst erm&ouml;glicht und auf deren Einhaltung der Auftraggeber regelm&auml;&szlig;ig vertrauen darf. In diesem Fall ist die Haftung auf den vertragstypischen, vorhersehbaren Schaden begrenzt.</p>
<p>(3) Die Haftung nach dem Produkthaftungsgesetz bleibt unber&uuml;hrt. Gesetzliche Verbraucherrechte bleiben ebenfalls unber&uuml;hrt.</p>

<h2>&sect; 13 Widerrufsrecht</h2>
<p>Ist der Auftraggeber Verbraucher im Sinne des &sect; 13 BGB, steht ihm ein Widerrufsrecht nach der <a href="widerruf.html">Widerrufsbelehrung</a> zu. Auftr&auml;ge, die der Auftraggeber in Aus&uuml;bung seiner gewerblichen oder selbst&auml;ndigen beruflichen T&auml;tigkeit erteilt, unterliegen keinem Widerrufsrecht.</p>

<h2>&sect; 14 Schlussbestimmungen</h2>
<p>(1) Es gilt das Recht der Bundesrepublik Deutschland. Ist der Auftraggeber Verbraucher, wird ihm dadurch nicht der Schutz zwingender Vorschriften des Staates entzogen, in dem er seinen gew&ouml;hnlichen Aufenthalt hat.</p>
<p>(2) ORD&Eacute; ist nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen (&sect; 36 VSBG).</p>
<p>(3) &Auml;nderungen und Erg&auml;nzungen dieses Vertrags bed&uuml;rfen der Textform.</p>
<p>(4) Sollte eine Bestimmung dieser Bedingungen unwirksam sein, bleibt die Wirksamkeit der &uuml;brigen Bestimmungen unber&uuml;hrt.</p>

</div></section>
"""

page("agb.html", "AGB",
     "Allgemeine Gesch&auml;ftsbedingungen von ORD&Eacute;.", "",
     AGB.replace("{stand}", "29. September 2026") if AGB_ONLINE else
     RECHT_OFFEN.format(h="Allgemeine Gesch&auml;ftsbedingungen",
        hinweis="Der Text liegt als Entwurf vor und wird gerade gepr&uuml;ft. Er geht online, sobald die Pr&uuml;fung abgeschlossen ist."))

WIDERRUF = """
<section class="pagehead"><div class="wrap"><h1>Widerrufsbelehrung</h1></div></section>
<section class="section"><div class="wrap narrow">

<h2>Widerrufsrecht</h2>
<p>Sie haben das Recht, binnen vierzehn Tagen ohne Angabe von Gr&uuml;nden diesen Vertrag zu widerrufen. Die Widerrufsfrist betr&auml;gt vierzehn Tage ab dem Tag des Vertragsschlusses.</p>

<p>Um Ihr Widerrufsrecht auszu&uuml;ben, m&uuml;ssen Sie uns</p>

<p>Artur Missal<br>
Ahornallee 4d<br>
86899 Landsberg am Lech<br>
Deutschland<br>
<a href="mailto:hello@ordeshop.net">hello@ordeshop.net</a></p>

<p>mittels einer eindeutigen Erkl&auml;rung (z.&nbsp;B. ein mit der Post versandter Brief oder eine E-Mail) &uuml;ber Ihren Entschluss, diesen Vertrag zu widerrufen, informieren. Sie k&ouml;nnen daf&uuml;r das unten stehende Muster-Widerrufsformular verwenden, das jedoch nicht vorgeschrieben ist.</p>

<p>Zur Wahrung der Widerrufsfrist reicht es aus, dass Sie die Mitteilung &uuml;ber die Aus&uuml;bung des Widerrufsrechts vor Ablauf der Widerrufsfrist absenden.</p>

<h2>Folgen des Widerrufs</h2>
<p>Wenn Sie diesen Vertrag widerrufen, haben wir Ihnen alle Zahlungen, die wir von Ihnen erhalten haben, unverz&uuml;glich und sp&auml;testens binnen vierzehn Tagen ab dem Tag zur&uuml;ckzuzahlen, an dem die Mitteilung &uuml;ber Ihren Widerruf bei uns eingegangen ist. F&uuml;r diese R&uuml;ckzahlung verwenden wir dasselbe Zahlungsmittel, das Sie bei der urspr&uuml;nglichen Transaktion eingesetzt haben, es sei denn, mit Ihnen wurde ausdr&uuml;cklich etwas anderes vereinbart; in keinem Fall werden Ihnen wegen dieser R&uuml;ckzahlung Entgelte berechnet.</p>

<p>Haben Sie verlangt, dass die Dienstleistung w&auml;hrend der Widerrufsfrist beginnen soll, so haben Sie uns einen angemessenen Betrag zu zahlen, der dem Anteil der bis zu dem Zeitpunkt, zu dem Sie uns von der Aus&uuml;bung des Widerrufsrechts hinsichtlich dieses Vertrags unterrichten, bereits erbrachten Dienstleistungen im Vergleich zum Gesamtumfang der im Vertrag vorgesehenen Dienstleistungen entspricht.</p>

<h2>Vorzeitiges Erl&ouml;schen des Widerrufsrechts</h2>
<p>Ihr Widerrufsrecht erlischt bei einem Vertrag &uuml;ber die Erbringung von Dienstleistungen, wenn wir die Dienstleistung vollst&auml;ndig erbracht haben und mit der Ausf&uuml;hrung erst begonnen haben, nachdem Sie dazu Ihre ausdr&uuml;ckliche Zustimmung gegeben haben und gleichzeitig Ihre Kenntnis davon best&auml;tigt haben, dass Sie Ihr Widerrufsrecht bei vollst&auml;ndiger Vertragserf&uuml;llung durch uns verlieren.</p>

<h2>Kein Widerrufsrecht f&uuml;r Unternehmer</h2>
<p>Das Widerrufsrecht besteht nur f&uuml;r Verbraucher im Sinne des &sect;&nbsp;13 BGB. Bestellen Sie im Rahmen Ihrer gewerblichen oder selbst&auml;ndigen beruflichen T&auml;tigkeit, besteht kein gesetzliches Widerrufsrecht.</p>

<h2>Muster-Widerrufsformular</h2>
<p>Wenn Sie den Vertrag widerrufen wollen, f&uuml;llen Sie bitte dieses Formular aus und senden Sie es zur&uuml;ck.</p>

<div class="muster">
<p>An: Artur Missal, Ahornallee 4d, 86899 Landsberg am Lech, Deutschland, hello@ordeshop.net</p>

<p>Hiermit widerrufe(n) ich/wir den von mir/uns abgeschlossenen Vertrag &uuml;ber die Erbringung der folgenden Dienstleistung:<br>
<span class="linie"></span></p>

<p>Bestellt am: <span class="linie kurz"></span></p>

<p>Name des/der Verbraucher(s):<br><span class="linie"></span></p>

<p>Anschrift des/der Verbraucher(s):<br><span class="linie"></span></p>

<p>Datum: <span class="linie kurz"></span></p>

<p>Unterschrift des/der Verbraucher(s) (nur bei Mitteilung auf Papier):<br><span class="linie"></span></p>
</div>

</div></section>
"""

page("widerruf.html", "Widerrufsbelehrung",
     "Widerrufsbelehrung und Muster-Widerrufsformular von ORD&Eacute;.", "", WIDERRUF)

# ---------------------------------------------------------------- Sitemap und robots
import datetime
heute = datetime.date.today().isoformat()

# Rechtsseiten braucht Google nicht weit oben
NIEDRIG = {"impressum.html", "datenschutz.html", "agb.html", "widerruf.html"}

zeilen = []
for datei, rang in SEITEN:
    if datei in NIEDRIG:
        rang = 0.2
    adresse = "https://ordeshop.net/" + ("" if datei == "index.html" else datei)
    zeilen.append(
        "  <url>\n"
        "    <loc>%s</loc>\n"
        "    <lastmod>%s</lastmod>\n"
        "    <priority>%.1f</priority>\n"
        "  </url>" % (adresse, heute, rang))

sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(zeilen) + "\n</urlset>\n")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

# ---------------------------------------------------------------
# kontakt.php  -  nimmt das Anfrageformular entgegen und schickt es
# als Mail weiter. Laeuft auf jedem Hoster mit PHP, also auch bei
# Hostinger. Es wird nichts auf dem Server gespeichert.
# ---------------------------------------------------------------
KONTAKT_PHP = r"""<?php
declare(strict_types=1);

$EMPFAENGER = 'hello@ordeshop.net';
$ABSENDER    = 'formular@ordeshop.net';   // Postfach beim Hoster anlegen
$ZIEL_OK     = 'danke.html';
$ZIEL_FEHLER = 'anfrage.html?fehler=1';

function weiter(string $ziel): void {
    header('Location: ' . $ziel, true, 303);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    weiter($ZIEL_FEHLER);
}

// Honigtopf: echte Menschen lassen dieses Feld leer
if (($_POST['website_url'] ?? '') !== '') {
    weiter($ZIEL_OK);   // Bot bekommt die Danke-Seite, die Mail geht nicht raus
}

function feld(string $name, int $max = 500): string {
    $wert = trim((string)($_POST[$name] ?? ''));
    $wert = str_replace(["\r", "\n", "\0"], ' ', $wert);
    return mb_substr($wert, 0, $max);
}

$name    = feld('name', 120);
$email   = feld('email', 180);
$betrieb = feld('betrieb', 120);
$telefon = feld('telefon', 60);
$branche = feld('branche', 80);
$seite   = feld('bestehende_seite', 200);
$paket   = feld('paket', 80);
$ok      = isset($_POST['datenschutz']);

$nachricht = trim((string)($_POST['nachricht'] ?? ''));
$nachricht = str_replace("\0", '', $nachricht);
$nachricht = mb_substr($nachricht, 0, 5000);

if ($name === '' || $nachricht === '' || !$ok
    || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    weiter($ZIEL_FEHLER);
}

$betreff = 'Anfrage von ' . $name . ($betrieb !== '' ? ' (' . $betrieb . ')' : '');

$text = "Neue Anfrage ueber ordeshop.net\n\n"
      . "Name:        $name\n"
      . "Betrieb:     $betrieb\n"
      . "E-Mail:      $email\n"
      . "Telefon:     $telefon\n"
      . "Branche:     $branche\n"
      . "Bisher:      $seite\n"
      . "Wunschpaket: $paket\n\n"
      . "Nachricht:\n$nachricht\n\n"
      . "---\n"
      . 'Gesendet: ' . date('d.m.Y H:i') . "\n";

$kopf = [
    'From: ORDE Formular <' . $ABSENDER . '>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'Content-Type: text/plain; charset=UTF-8',
    'MIME-Version: 1.0',
    'X-Mailer: PHP/' . phpversion(),
];

$betreff_kodiert = '=?UTF-8?B?' . base64_encode($betreff) . '?=';

if (@mail($EMPFAENGER, $betreff_kodiert, $text, implode("\r\n", $kopf))) {
    weiter($ZIEL_OK);
}
weiter($ZIEL_FEHLER);
"""
with open(os.path.join(OUT, "kontakt.php"), "w", encoding="utf-8") as f:
    f.write(KONTAKT_PHP)

robots = """User-agent: *
Allow: /

# Beispielseiten sind Demos, keine eigenstaendigen Inhalte
Disallow: /demos/

Sitemap: https://ordeshop.net/sitemap.xml
"""
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)

print("Seiten gebaut:", sorted(os.listdir(OUT)))
print("sitemap.xml mit %d Adressen, robots.txt geschrieben" % len(SEITEN))
