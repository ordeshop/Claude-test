---
name: remotion-video
description: "Build videos programmatically with Remotion (React-based video framework). Use when the user wants to create, animate, or render video with code — data-driven product clips, social/marketing videos, animated explainers, title cards, or embedding a video player in a React app. Covers project setup, Compositions, frame-based animation (useCurrentFrame, interpolate, spring), sequencing, audio, images/video, data via props, the Studio preview, and CLI rendering to MP4."
license: MIT
metadata:
  about: "Original helper skill for using Remotion. Not affiliated with Remotion; Remotion itself is source-available under its own license — see the Licensing note."
---

# Remotion — Programmatic Video with React

Remotion renders video by drawing a React component **once per frame**. You
describe what the screen looks like at frame `f`; Remotion steps `f` from `0` to
`durationInFrames - 1` and encodes the frames into a video file. Everything is
plain React + CSS (and any web tech: SVG, Canvas, WebGL, Three.js).

## When to use this skill

- Creating a video from code: marketing/social clips, animated explainers,
  title/lower-thirds, data-driven product videos (one template, many inputs).
- Animating UI/text/images on a timeline and rendering to MP4/WebM/GIF.
- Embedding an interactive preview in a React app via `@remotion/player`.

Not for: editing existing footage frame-by-frame by hand, or non-video work.

## Setup

Scaffold a new project (recommended):

```bash
npm create video@latest        # interactive; pick a template (e.g. "Blank")
cd my-video
npm run dev                     # opens Remotion Studio (live preview)
```

Add to an existing React project:

```bash
npm i remotion @remotion/cli
```

Core files:
- `src/index.ts` → `registerRoot(Root)` — the entry point.
- `src/Root.tsx` → declares one or more `<Composition>`s (id, component, size, fps, duration, default props).
- Your composition components → the actual React that gets drawn each frame.

```tsx
// src/Root.tsx
import { Composition } from "remotion";
import { Hello } from "./Hello";

export const Root = () => (
  <Composition
    id="Hello"
    component={Hello}
    durationInFrames={150}   // 5s at 30fps
    fps={30}
    width={1080}
    height={1920}            // 9:16 for social; use 1920x1080 for landscape
    defaultProps={{ name: "ORDÉ" }}
  />
);
```

## Core concepts

**Frame + config** — every animation reads the current frame:

```tsx
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

export const Hello: React.FC<{ name: string }> = ({ name }) => {
  const frame = useCurrentFrame();
  const { fps, width, height, durationInFrames } = useVideoConfig();

  // linear fade-in over the first 30 frames, then hold
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // physical, springy entrance
  const scale = spring({ frame, fps, config: { damping: 12 } });

  return (
    <AbsoluteFill style={{ background: "#0d0d0d", justifyContent: "center", alignItems: "center" }}>
      <h1 style={{ color: "white", fontSize: 96, opacity, transform: `scale(${scale})` }}>
        {name}
      </h1>
    </AbsoluteFill>
  );
};
```

- `interpolate(input, inputRange, outputRange, options)` — map frames → any value. Always `clamp` unless you want extrapolation.
- `spring({ frame, fps, config })` — natural motion; returns ~0→1.
- `useVideoConfig()` — `fps`, `width`, `height`, `durationInFrames`.

**Layout & timeline:**
- `<AbsoluteFill>` — a full-frame absolutely-positioned div; stack them for layers.
- `<Sequence from={30} durationInFrames={60}>…</Sequence>` — time-shift children; inside, `useCurrentFrame()` restarts at 0.
- `<Series>` / `<Series.Sequence>` — play blocks back-to-back without computing offsets by hand.

**Assets & media:**
- `staticFile("logo.png")` — reference files in the `public/` folder.
- `<Img>`, `<OffthreadVideo>` (preferred for rendering) / `<Video>`, `<Audio src={staticFile("music.mp3")} volume={0.6} />`.
- Fonts: `@remotion/google-fonts` or `@remotion/fonts` for local fonts — load before rendering text.

## Data-driven videos (one template, many outputs)

Type your props with Zod so the Studio shows an editable form and renders accept `--props`:

```tsx
import { z } from "zod";
export const schema = z.object({ name: z.string(), color: z.string() });
// <Composition ... schema={schema} defaultProps={{ name: "ORDÉ", color: "#e11" }} />
```

Use `calculateMetadata` on the `<Composition>` to derive duration/size from the
props (e.g. length from a script or audio file) at render time.

## Preview & render

```bash
npx remotion studio                       # live editor/preview (v4+)
npx remotion render Hello out/video.mp4    # render a composition to MP4
npx remotion render Hello out/v.mp4 --props='{"name":"Ada"}'
npx remotion render Hello out/v.webm --codec=vp8   # WebM; --codec=gif for GIF
npx remotion still Hello out/thumb.png --frame=30  # single-frame PNG
```

Render at scale programmatically with `@remotion/renderer` (Node), or on
Remotion Lambda for parallel cloud rendering of many variants.

## Embed a player in a React app

```tsx
import { Player } from "@remotion/player";
<Player component={Hello} durationInFrames={150} fps={30} compositionWidth={1080}
        compositionHeight={1920} inputProps={{ name: "ORDÉ" }} controls />
```

## Practical tips

- Design in the target resolution and `fps` from the start; 30fps is a good default.
- Keep motion purposeful: ease in/out with `interpolate`'s easing or `spring`; avoid one duration for everything.
- Prefer `<OffthreadVideo>` over `<Video>` when rendering embedded video for reliability.
- Everything is deterministic per frame — never rely on `Date.now()`/`Math.random()` without seeding, or frames won't match.
- Pair with the `awesome-design-md` and design skills here to give the video a real brand look (palette, type, motion).

## Licensing note (read before shipping)

Remotion is **source-available under its own license**, not MIT: free for
individuals, non-profits, and small for-profit companies (roughly ≤3 employees),
but larger for-profit organizations need a paid company license. This skill is
original helper documentation (MIT) and bundles none of Remotion's code — but
whoever actually uses Remotion must confirm their own eligibility at
https://remotion.dev and https://remotion.pro. Do not copy or relicense
Remotion's source to build a competing product.
