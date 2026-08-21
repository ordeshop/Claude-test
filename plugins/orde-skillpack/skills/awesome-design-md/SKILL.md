---
name: awesome-design-md
description: "Brand-inspired design systems as plain-text DESIGN.md files for building consistent UIs. Use when a user asks to build, style, or theme UI in the look-and-feel of a known brand (e.g. Stripe, Linear, Vercel, Notion, Apple, Airbnb, Figma, Spotify, Tesla) or wants a reference design system to follow. Bundles 74 DESIGN.md files capturing color palettes, typography, components, layout, elevation, and guardrails. Source: VoltAgent/awesome-design-md (MIT)."
license: MIT
metadata:
  source: "https://github.com/VoltAgent/awesome-design-md"
  brands: 74
---

# awesome-design-md — Brand Design Systems

A curated collection of **DESIGN.md** files, one per brand. A `DESIGN.md` is a
plain-text design-system document (a format popularized by Google Stitch) that
an AI agent reads to generate visually consistent UI. Each file captures a
brand's visual theme, color palette, typography scale, component styling,
layout principles, elevation/depth, responsive behavior, and design guardrails.

These are **inspired interpretations** for design reference, not official brand
assets. Do not reproduce a company's logo, protected trademarks, or copyrighted
imagery — use the tokens (color, type, spacing, component style) to guide an
original UI.

## When to use

Use this skill when the task is to **build, style, restyle, or theme a UI** and
either:

- the user names a brand whose feel they want ("make it look like Stripe",
  "Linear-style dashboard", "Notion vibes"), **or**
- the user wants a ready-made, coherent design system to follow instead of
  inventing tokens from scratch.

Skip it for backend logic, non-visual work, or when the user has their own
design system already.

## How to use

1. **Pick the brand.** Match the user's request to a slug in
   `references/catalog.md` (74 brands, each with a one-line description).
2. **Read the design system.** Open `design-md/<slug>/DESIGN.md` from this
   skill's directory. It contains YAML frontmatter (name, description, colors,
   typography) followed by prose sections on components, layout, depth, and
   guardrails.
3. **Apply the tokens.** Use the palette, type scale, radii, spacing, and
   component rules when generating or editing the UI. Prefer semantic tokens
   over raw hex where the target project supports them.
4. **Respect the guardrails.** Each DESIGN.md lists do/don't rules — follow
   them so the result reads as intentional rather than a loose imitation.

Combine with `ui-ux-pro-max` / `ui-styling` for accessibility, responsive, and
implementation quality once the visual language is chosen.

## Finding a brand

```bash
# list all available brands
ls .claude/skills/awesome-design-md/design-md

# search the catalog for a keyword (fintech, dark, editorial, ...)
grep -i "fintech" .claude/skills/awesome-design-md/references/catalog.md
```

The full slug list is in `references/catalog.md`. Brands span AI platforms,
developer tools, fintech, e-commerce, automotive, and media.

## Attribution

Content from [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md),
MIT License — see `AWESOME-DESIGN-MD-LICENSE`. Live previews and downloads:
https://getdesign.md
