---
name: awesome-claude-design
description: "DESIGN.md files sorted by aesthetic family (editorial, terminal, warm, data-dense, cinematic, playful, glass, brutalist, indie) plus brand remixes, prompt packs (brand-to-DESIGN.md, live-site audit, 3-designer debate, remix two brands, family picker, break the default AI look), workflow recipes and an anti-slop checklist. Use when choosing a visual direction for a website, landing page, demo or ad, when a design looks generic/AI-made, when auditing a live site, or when extracting a design system from a customer's existing website. Source: rohitg00/awesome-claude-design (MIT)."
license: MIT
metadata:
  source: "https://github.com/rohitg00/awesome-claude-design"
  imported: "2026-10-25"
---

# awesome-claude-design — Aesthetic Families, Remixes & Anti-Slop Prompts

Companion to `awesome-design-md` (84 brand DESIGN.md files). That skill is sorted
by **brand**; this one is sorted by **visual character**, adds **remixes** of two
brands, and ships **prompt packs** and **recipes** for the design process itself.

These are inspired interpretations for design reference, not official brand
assets. Never reproduce logos, trademarks or copyrighted imagery — use the tokens
(color, type, spacing, component rules) to build an original UI.

## What is in this folder

| Path | Content |
|---|---|
| `design-md/<family>/<brand>.md` | 30 DESIGN.md files in 9 families: `editorial`, `terminal`, `warm`, `data-dense`, `cinematic`, `playful`, `glass`, `brutalist`, `indie` |
| `design-md/remix/*.md` | 8 two-brand remixes (e.g. `stripe-x-a24`, `linear-x-claude`, `notion-x-duolingo`, `granola-x-criterion`) |
| `prompts/*.md` | 6 prompt packs, each with full prompt, example run, quality checks |
| `recipes/*.md` | 13 step-by-step workflows (landing page in 20 min, brand extraction, web capture → prototype, wireframe → hi-fi, …) |
| `case-studies/*.md` | 3 real-world write-ups |
| `references/families.md` | Family overview with swatches, typefaces and reference sites |
| `references/picker-and-anti-slop.md` | 3-question family picker + the anti-slop rules and "AI default fingerprints" table |
| `previews/*.jpg` | Static homepage screenshots, one per family (see `previews/ATTRIBUTION.md`) |

## How to use

1. **Pick a direction.** Run the 3 questions in `references/picker-and-anti-slop.md`
   (read-heavy vs scan-heavy → who is the user → does it need courage). Or use
   `prompts/family-picker.md`.
2. **Read one or two DESIGN.md files** from that family. For a custom feel, read a
   remix or combine two with `prompts/remix-two-brands.md` (explicit token
   arbitration: which brand wins color, which wins type, which wins spacing).
3. **Before generating, apply the anti-slop rules** from
   `references/picker-and-anti-slop.md` / `prompts/break-default-aesthetic.md`:
   no default teal accent, no animated "live" dot, containers nest max 2 levels,
   no three-column feature grid as section 2, one icon family or none, explicit
   font stack with weight + tracking, accent left-rule only with a semantic role.
4. **Build**, then **critique** with `prompts/3-designer-debate.md` or
   `prompts/audit-live-site.md` and fix the punch list.

## Prompt packs (`prompts/`)

| Pack | Use it for |
|---|---|
| `brand-to-design-md` | URL → full DESIGN.md with 9 sections (extract a customer's existing look) |
| `audit-live-site` | URL → scored audit (hierarchy, spacing, a11y, AI-slop) + punch list |
| `3-designer-debate` | Three-voice critique with synthesis + minority reports |
| `remix-two-brands` | Merge two DESIGN.md files coherently |
| `family-picker` | 3 questions → family + 2 reference files |
| `break-default-aesthetic` | Neutralize the generic AI look in one paste |

## ORDÉ-Einsatz (so nutzen wir das)

- **Kundenwebsites / kostenlose Entwürfe:** Immer zuerst dem verbindlichen Ablauf in
  `Business-Handbuch/ABLAUF-KUNDENAUFTRAG.md` und dem Skill `kundenauftrag` folgen.
  Diese Skill liefert nur die *Stilrichtung*: Familie wählen → 1–2 DESIGN.md lesen →
  mit Kundenfarben/-logo zu einem eigenen System mischen.
- **Relaunch:** `prompts/brand-to-design-md.md` auf die alte Kundenseite anwenden,
  damit der Wiedererkennungswert bleibt, und `prompts/audit-live-site.md` als
  Grundlage für die Verkaufsargumente (Punch-List) in der Akquise-Mail.
- **Lokale Betriebe:** Café/Restaurant/Friseur → meist `warm` oder `indie`;
  Fitness/Handwerk → `cinematic` oder `brutalist`; Premium-Dienstleister → `editorial`
  oder `glass`. Nie 1:1 eine Marke kopieren.
- **Senmi:** `warm`/`indie` passt zur ruhigen Matcha-Optik; Farben an Matcha-Grün anpassen.
- **Ads/Videos:** dieselben Tokens (Farben, Schrift) im Skill `motion-studio` verwenden,
  damit Website und Ad einheitlich wirken.

Combine with `awesome-design-md` (brand catalog), `design-taste-frontend`,
`high-end-visual-design`, `impeccable` and `ui-ux-pro-max` for implementation quality.

## Attribution

Content from [rohitg00/awesome-claude-design](https://github.com/rohitg00/awesome-claude-design),
MIT License — see `AWESOME-CLAUDE-DESIGN-LICENSE`. Preview screenshots: see
`previews/ATTRIBUTION.md`; trademarks remain with their owners.
