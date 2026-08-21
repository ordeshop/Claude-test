# ORDÉ Design — Claude Code Skills

**34 Claude Code skills** bundled as one installable plugin: `orde-design`.

## What's inside

- **Design systems** — `awesome-design-md` (74 brand `DESIGN.md` files: Stripe, Linear, Notion, Apple, …)
- **Anti-slop frontend** (from tasteskill) — `design-taste-frontend`, `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `gpt-taste`, `stitch-design-taste`, `redesign-existing-projects`, `image-to-code`, `full-output-enforcement`, `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`
- **UI/UX intelligence** — `ui-ux-pro-max`, `ui-styling`, `uupm-design`, `design-system`, `brand`, `banner-design`, `slides`
- **Engineering workflow** (Superpowers) — `brainstorming`, `test-driven-development`, `systematic-debugging`, `writing-plans`, `executing-plans`, `requesting-code-review`, `receiving-code-review`, and more

## Install (recommended) — as a plugin

In Claude Code:

```
/plugin marketplace add ordeshop/Claude-test
/plugin install orde-design@orde-skills
```

Install once — all 34 skills are then available in **every** project. Type `/`
to list them, or just describe your task ("build a landing page in Stripe style")
and Claude picks the right skill automatically.

## Alternative — install skills globally via script

```bash
git clone https://github.com/ordeshop/Claude-test.git
cd Claude-test
./install.sh          # --list to preview, --force to overwrite
```

Installs every skill into `~/.claude/skills/`.

## Repository layout

```
.claude-plugin/marketplace.json     # marketplace manifest (/plugin marketplace add)
plugins/orde-design/                # the plugin — single source of truth
  ├─ .claude-plugin/plugin.json
  └─ skills/                        # all 34 skills
install.sh                          # optional: install skills into ~/.claude/skills
```

## Licenses

Bundled third-party skills keep their original MIT licenses — see the
`*-LICENSE` files in `plugins/orde-design/`.
Sources: [awesome-design-md](https://github.com/VoltAgent/awesome-design-md),
[tasteskill](https://github.com/tasteskill/tasteskill), Superpowers, UI/UX Pro Max.
