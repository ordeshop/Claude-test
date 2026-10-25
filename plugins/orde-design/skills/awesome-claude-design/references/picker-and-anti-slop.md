## Picker: What Should I Use

Three questions. Pick a family.

1. **Is your product read-heavy or scan-heavy?**
   - Read-heavy → [Editorial Minimalism](#1-editorial-minimalism) or [Warm Editorial](#3-warm-editorial)
   - Scan-heavy → [Data-Dense Pro](#4-data-dense-pro) or [Terminal-Core](#2-terminal-core)

2. **Who's the user?**
   - Developer → [Terminal-Core](#2-terminal-core) or [Data-Dense Pro](#4-data-dense-pro)
   - Designer / creator → [Cinematic Dark](#5-cinematic-dark) or [Playful Color](#6-playful-color)
   - Consumer → [Glass / Soft-Futurism](#7-glass--soft-futurism) or [Playful Color](#6-playful-color)
   - Prosumer → [Warm Editorial](#3-warm-editorial)

3. **Does the brand need to feel like it took courage?**
   - Yes → [Neon Brutalist](#8-neon-brutalist) or [Cult / Indie Picks](#9-cult--indie-picks-non-fortune-500)
   - No → Stay in families 1-7

## Prompts & Cookbooks

### Official (Anthropic)

- [Anthropic Prompt Library](https://docs.anthropic.com/en/resources/prompt-library/library) — 40+ prompts including **Brand builder**, **Website wizard**, **Prose polisher**
- [claude-cookbooks / prompting_for_frontend_aesthetics.ipynb](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) — official anti-slop notebook
- [System prompts release notes](https://docs.anthropic.com/en/release-notes/system-prompts)

### Community gists & prompt repos

- [**superdesigndev/superdesign**](https://github.com/superdesigndev/superdesign) <img src="https://img.shields.io/github/stars/superdesigndev/superdesign?style=flat-square&logo=github&label=" height="16"> — open-source design agent in the IDE by [@jasonzhou1993](https://x.com/jasonzhou1993) and [@jackjack_eth](https://x.com/jackjack_eth). Parallel Claude Code agents, infinite canvas UX. [Show HN](https://news.ycombinator.com/item?id=44376003)
- [**jonthebeef/superdesign-mcp-claude-code**](https://github.com/jonthebeef/superdesign-mcp-claude-code) <img src="https://img.shields.io/github/stars/jonthebeef/superdesign-mcp-claude-code?style=flat-square&logo=github&label=" height="16"> — MCP server wiring SuperDesign into Claude Code, no API key
- [**Owl-Listener/designer-skills**](https://github.com/Owl-Listener/designer-skills) <img src="https://img.shields.io/github/stars/Owl-Listener/designer-skills?style=flat-square&logo=github&label=" height="16"> — Designer Skills Collection by MC Dean. MIT
- [**Owl-Listener/designpowers**](https://github.com/Owl-Listener/designpowers) <img src="https://img.shields.io/github/stars/Owl-Listener/designpowers?style=flat-square&logo=github&label=" height="16"> — specialist design agents, Direct + Auto modes. MIT
- [**saifyxpro/ui-ux-design-pro-skill**](https://github.com/saifyxpro/ui-ux-design-pro-skill) <img src="https://img.shields.io/github/stars/saifyxpro/ui-ux-design-pro-skill?style=flat-square&logo=github&label=" height="16"> — styles, palettes, fonts, reasoning rules, platform templates
- [**nextlevelbuilder/ui-ux-pro-max-skill**](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) <img src="https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square&logo=github&label=" height="16"> — professional UI/UX across platforms
- [**alirezarezvani/claude-skills**](https://github.com/alirezarezvani/claude-skills) <img src="https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=flat-square&logo=github&label=" height="16"> — skills across engineering, marketing, product, compliance
- [**NicholasSpisak — Design with Claude Code**](https://gist.github.com/NicholasSpisak/7cb9db221b0b7c4c4aaf9ffca21a847c) — `design.md` prompt with three design-professional personas in live debate
- [**abhishekray07/claude-md-templates**](https://github.com/abhishekray07/claude-md-templates) <img src="https://img.shields.io/github/stars/abhishekray07/claude-md-templates?style=flat-square&logo=github&label=" height="16"> — CLAUDE.md + `api-design.md` rule template
- [**smartwhale8/claude-playbook**](https://github.com/smartwhale8/claude-playbook) <img src="https://img.shields.io/github/stars/smartwhale8/claude-playbook?style=flat-square&logo=github&label=" height="16"> — production `.claude/` scaffolding, GitHub template
- [**VoltAgent/awesome-agent-skills**](https://github.com/VoltAgent/awesome-agent-skills) — 1000+ skills incl. `design-md`, `enhance-prompt`, `react-components`, `shadcn-ui`
- [**daymade/claude-code-skills**](https://github.com/daymade/claude-code-skills) — production-ready Claude Code skills marketplace

### Prompt packs shipped here (`/prompts`)

Every pack includes the full prompt, an example run with expected output, quality checks, and variations.

| Pack | Purpose | File |
|---|---|---|
| `brand-to-design-md` | URL → full DESIGN.md with 9 canonical sections | [`/prompts/brand-to-design-md.md`](../prompts/brand-to-design-md.md) |
| `audit-live-site` | URL → scored audit (hierarchy, spacing, a11y, AI-slop) + punch list | [`/prompts/audit-live-site.md`](../prompts/audit-live-site.md) |
| `3-designer-debate` | Three-voice critique with synthesis + minority reports | [`/prompts/3-designer-debate.md`](../prompts/3-designer-debate.md) |
| `remix-two-brands` | Combine two DESIGN.md files with explicit token arbitration | [`/prompts/remix-two-brands.md`](../prompts/remix-two-brands.md) |
| `family-picker` | 3 questions → recommended family + 2 reference DESIGN.md files | [`/prompts/family-picker.md`](../prompts/family-picker.md) |

Index: [`/prompts/README.md`](../prompts/README.md)

## Anti-Slop Kit

Drop this fragment into Claude Design's system prompt or any Claude Code project. Sourced from Anthropic's [frontend aesthetics cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb):

```
NEVER use generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Cliched color schemes (purple gradients on white or dark backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

DO use:
- Unique fonts chosen for the brand, not defaults
- Cohesive colors and themes grounded in the product's story
- Animations for effects and micro-interactions
- Context-specific character in every component
```

Malewicz's [teardown](https://www.youtube.com/watch?v=IkspcJdeP3U) <img src="https://img.shields.io/youtube/views/IkspcJdeP3U?style=flat-square&label=views&color=191817" height="16"> opens by flagging Claude Design's own logo as "generic, color palette" — exactly the trap this prompt is built to avoid.

### Claude Design's default fingerprints (avoid)

The single biggest community complaint: every Claude Design output looks the same. Catalogued from launch-week Reddit threads, the [Sam Henri Gold blog post](https://samhenri.gold/blog/20260418-claude-design/), the [Banani review](https://www.banani.co/blog/claude-design-review), and [The Neuron Daily round-up](https://www.theneurondaily.com/p/anthropic-s-claude-design-launched-and-reddit-has-thoughts).

| Fingerprint | What it looks like | Counter-rule |
|---|---|---|
| **Teal accent everywhere** | The default `#16d5e6`-adjacent action color appears on CTA, headline accent, focus rings, and chart fill | Pick a brand-specific accent in your DESIGN.md before the first generation |
| **Blinking status dot** | Animated green/lime dot top-right of nav, signals "live"/"AI" by reflex | Reject in your prompt: "no animated status indicators" |
| **Container soup** | Pills wrapping cards wrapping cards wrapping content; padding stacking 24/24/24 | Cap nesting depth: "containers nest at most 2 levels" |
| **Default serif headline** | Tiempos- or Source-Serif-adjacent serif paired with sans body — reads like the Anthropic brand's leftovers | Specify font stack with explicit weight + tracking, not a vibe |
| **Accent bar left of every card** | 4px coloured rule on every card, regardless of semantic meaning | Reserve left-rule for one role (e.g. severity) — never as decoration |
| **Three-column feature grid in hero** | Almost every landing the model produces has the same section-2 layout | Brief: "no three-column feature grid; choose marquee, alternating-row, or single-column instead" |
| **Lucide icon stack** | Default icon set across nav, buttons, empty states | Either commit to a single icon family (Phosphor / Heroicons / custom) or ship type-only |
| **Generative hero in product palette ignored** | Image generator picks colors that "look right" but ignore the DESIGN.md tokens | Constrain the image: "regenerate hero using only `--bg`, `--accent`, `--text`" |

Use the dedicated prompt pack [`prompts/break-default-aesthetic.md`](../prompts/break-default-aesthetic.md) to neutralize these in one paste.

### How the defaults got there

Claude Design routes through Anthropic's open-source [`frontend-design` skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) — the same skill Claude Code auto-loads for UI work. The skill's defaults bias toward "production-quality first pass" which, in the absence of a DESIGN.md, lands on the same look every time.

Two related Anthropic resources worth bookmarking:

- [**frontend-aesthetics cookbook**](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) — Anthropic's own anti-slop primer; the source quoted above
- [**`skills` PR #210**](https://github.com/anthropics/skills/pull/210) — clarity revision of the frontend-design skill; 75% win rate across model tiers, biggest lift on Haiku

Anthropic acknowledges the problem in the cookbook: *"You tend to converge toward generic, 'on distribution' outputs. In frontend design, this creates what users call the 'AI slop' aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight."*

