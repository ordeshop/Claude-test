# Praxis Lindenhof — Hero (Demo)

Fullscreen cinematic hero section for a **fictional** German dental practice,
built as a design showcase. React + Vite + TypeScript + Tailwind CSS +
Lucide icons. The entire user-facing copy is in German; code and comments
are English.

> **Demo only.** No real patient data, no real contact details. The phone
> number, email and address are placeholders, and the appointment form does
> not submit anywhere — it shows an inline confirmation and resets.

## Run

```bash
npm install
npm run dev      # http://localhost:5173
npm run build    # production build to /dist
```

## What's inside

- Four stacked, autoplaying background videos with a 1s opacity crossfade
  and a text switcher (Empfang · Präzision · Behandlung · Ihr Team).
- Auto-advance every 8s, paused once the visitor picks a scene, and disabled
  under `prefers-reduced-motion`.
- A breathing readability scrim, `.liquid-glass` frosted panels, and a dark
  brand-colour mode that engages over the moody "Behandlung" clip.
- Responsive nav (desktop pill / mobile overlay menu), German aria-labels,
  `lang="de"`, and focus-visible rings.

## Media (generated with Kling)

The four clips and their poster stills were generated with Kling in a
documentary style (no faces, teeth or hands in frame) so the footage does
not read as an AI render. Swap them for real footage when available.

> ⚠️ **The Kling URLs in `src/App.tsx` are temporary and expire ~24h after
> generation.** For a persistent demo, download the eight assets, drop them
> in `public/media/`, and point the `VIDEO_URL_*` / `POSTER_URL_*` constants
> at the local paths.

## Legal note

A production German site would legally require **Impressum** and
**Datenschutz** pages. They are rendered here as `href="#"` placeholders
only — no legal text is included (see the comment in `src/App.tsx`).
