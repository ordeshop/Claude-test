# ORDÉ Claude Code Skills

A collection of **34 Claude Code skills** bundled as a one-install plugin.

## What's inside

- **Design systems** — `awesome-design-md` (74 brand `DESIGN.md` files: Stripe, Linear, Notion, Apple, …)
- **Anti-slop frontend** (from tasteskill) — `design-taste-frontend`, `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `gpt-taste`, `stitch-design-taste`, `redesign-existing-projects`, `image-to-code`, `full-output-enforcement`, `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`
- **UI/UX intelligence** — `ui-ux-pro-max`, `ui-styling`, `uupm-design`, `design-system`, `brand`, `banner-design`, `slides`
- **Engineering workflow** (Superpowers) — `brainstorming`, `test-driven-development`, `systematic-debugging`, `writing-plans`, `executing-plans`, `requesting-code-review`, `receiving-code-review`, and more

## Install everything at once (recommended) — as a plugin

In Claude Code:

```
/plugin marketplace add ordeshop/Claude-test
/plugin install orde-skillpack@orde-skills
```

That's it — after installing once, all 34 skills are available in **every** project.
Type `/` to see them, or just describe your task (e.g. "build a landing page in Stripe style")
and Claude picks the right skill automatically.

## Alternative — install skills globally via script

If you prefer plain skills under `~/.claude/skills/` instead of a plugin:

```bash
git clone https://github.com/ordeshop/Claude-test.git
cd Claude-test
./install.sh          # --list to preview, --force to overwrite
```

## Repository layout

```
.claude/skills/                 # skills for use when working in THIS repo + used by install.sh
.claude-plugin/marketplace.json # marketplace manifest (for /plugin marketplace add)
plugins/orde-skillpack/         # the bundled plugin (all 34 skills)
install.sh                      # installs all skills into ~/.claude/skills
```

## Licenses

Bundled third-party skills keep their original MIT licenses — see the
`*-LICENSE` files in `.claude/skills/` and `plugins/orde-skillpack/`.
Sources: [awesome-design-md](https://github.com/VoltAgent/awesome-design-md),
[tasteskill](https://github.com/tasteskill/tasteskill), Superpowers, UI/UX Pro Max.
