#!/usr/bin/env bash
#
# install.sh — Install this repo's Claude Code skills globally.
#
# Copies every skill under .claude/skills/ into your personal
# ~/.claude/skills/ directory, so the skills are available in ALL projects
# where you run Claude Code locally (not just this repo).
#
# Usage:
#   ./install.sh            # install all skills (skips ones already present)
#   ./install.sh --force    # overwrite skills that are already installed
#   ./install.sh --list     # just list the skills that would be installed
#
set -euo pipefail

# Resolve the directory this script lives in, so it works from anywhere.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/.claude/skills"
DEST_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

FORCE=0
LIST_ONLY=0
for arg in "$@"; do
  case "$arg" in
    --force) FORCE=1 ;;
    --list)  LIST_ONLY=1 ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//' | head -20
      exit 0 ;;
    *) echo "Unknown option: $arg" >&2; exit 2 ;;
  esac
done

if [ ! -d "$SRC_DIR" ]; then
  echo "Error: no skills found at $SRC_DIR" >&2
  exit 1
fi

# A skill is any directory containing a SKILL.md file.
mapfile -t SKILLS < <(find "$SRC_DIR" -maxdepth 2 -name SKILL.md -printf '%h\n' | sort)

if [ "${#SKILLS[@]}" -eq 0 ]; then
  echo "No skills (SKILL.md) found under $SRC_DIR" >&2
  exit 1
fi

if [ "$LIST_ONLY" -eq 1 ]; then
  echo "Skills in this repo (${#SKILLS[@]}):"
  for s in "${SKILLS[@]}"; do echo "  - $(basename "$s")"; done
  exit 0
fi

echo "Installing ${#SKILLS[@]} skill(s) into: $DEST_DIR"
mkdir -p "$DEST_DIR"

installed=0
skipped=0
for skill in "${SKILLS[@]}"; do
  name="$(basename "$skill")"
  target="$DEST_DIR/$name"
  if [ -e "$target" ] && [ "$FORCE" -ne 1 ]; then
    echo "  skip    $name (already installed; use --force to overwrite)"
    skipped=$((skipped + 1))
    continue
  fi
  rm -rf "$target"
  cp -r "$skill" "$target"
  echo "  install $name"
  installed=$((installed + 1))
done

# Copy any bundled license files sitting alongside the skills.
find "$SRC_DIR" -maxdepth 1 -type f -name '*LICENSE*' -exec cp {} "$DEST_DIR"/ \; 2>/dev/null || true

echo ""
echo "Done. Installed: $installed, skipped: $skipped."
echo "Restart Claude Code, then type '/' to see the skills or invoke e.g. /awesome-design-md"
