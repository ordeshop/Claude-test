# Superpowers Skills (project-installed)

This directory contains the [Superpowers](https://github.com/obra/superpowers)
skill library by Jesse Vincent, copied into this repo as **project-level**
Claude Code skills.

## What's here

- `skills/` — 14 Superpowers skills (brainstorming, writing/executing plans,
  test-driven-development, systematic-debugging, code-review, subagent-driven
  development, git worktrees, verification, and more).
- `hooks/session-start` + `hooks/run-hook.cmd` — the SessionStart hook that
  injects the `using-superpowers` skill at the start of each session.
- `settings.json` — wires the SessionStart hook into Claude Code.

## How it activates

Claude Code auto-discovers any `.claude/skills/*/SKILL.md`, so the skills
trigger automatically based on their descriptions. The SessionStart hook
additionally injects the `using-superpowers` primer at startup, so the skills
are used proactively rather than only on demand.

## Updating

Re-copy from the upstream repo:

```bash
git clone --depth 1 https://github.com/obra/superpowers /tmp/superpowers
cp -r /tmp/superpowers/skills/. .claude/skills/
cp /tmp/superpowers/hooks/session-start /tmp/superpowers/hooks/run-hook.cmd .claude/hooks/
```

## Alternative: install as a plugin instead

If you'd rather not vendor the files, install Superpowers as a plugin in your
Claude Code CLI:

```
/plugin install superpowers@claude-plugins-official
```

## Bundled skill packages

- **Superpowers** (`obra/superpowers`, MIT): brainstorming, writing/executing
  plans, TDD, debugging, code-review, and more.
- **UI/UX Pro Max** (`nextlevelbuilder/ui-ux-pro-max-skill`, MIT): `ui-ux-pro-max`,
  `uupm-design`, `ui-styling`, `design-system`, `brand`, `banner-design`, `slides`.
  Note: this package's `design` skill was renamed to **`uupm-design`** to avoid
  colliding with Claude Code's built-in `design` (canvas) skill.

## License

Superpowers is MIT-licensed. See `skills/SUPERPOWERS-LICENSE`.
Copyright (c) 2025 Jesse Vincent.
