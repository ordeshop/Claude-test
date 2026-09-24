---
name: ugc-ad-scripts
description: >-
  Writes full shot-by-shot UGC ad scripts for short-form video (TikTok-first),
  built to be generated as realistic AI video in Kling. Supports two formats and
  picks or asks based on what the user wants: (1) TALKING-HEAD — a creator/AI-avatar
  speaking to camera with a scroll-stopping hook, spoken lines, and captions; and
  (2) FACELESS SATISFYING / ASMR — hands-and-product close-ups, on-screen text, and
  ASMR sound, in the vein of "Amazon finds" demos and ASMR restocking/refilling
  accounts. From just a product name or link it infers the audience and angle,
  writes the hook, and outputs a scene-by-scene script where every shot has a
  Kling-ready prompt tuned to look like real phone footage, not glossy AI. Use
  whenever someone wants a UGC ad, a TikTok ad script, a talking-head or
  faceless/satisfying/ASMR/restock/"Amazon finds" product video, an AI UGC ad, or a
  Kling video script — even if they just say "make me an ad for [product]."
---

# UGC Ad Scripts (talking-head + faceless, Kling-ready)

## What this skill produces

A complete, shot-by-shot **UGC ad script for TikTok**, written so each shot generates
cleanly in **Kling** and stitches into one ad that looks like a real person filmed it on
their phone — not like AI. UGC ads win because they feel like a friend's recommendation.
The whole job is to protect that handheld, human, unpolished feeling while hitting a tight
conversion structure.

The skill produces one of **two formats**. Deliver the shot-by-shot structure in the
matching **Output template** below — never loose copy; the value is the scene breakdown
someone can paste into Kling shot by shot.

## Step 0 — Choose the format

Two formats, because the same person will want different things on different days:

- **Talking-head** — a creator or **AI avatar** talks to camera. Persuasion rides on a
  spoken hook, short conversational lines, and captions. Great for story/testimonial angles,
  apps/software, anything that needs explaining. Use this when the user has (or wants to use)
  a face/avatar.
- **Faceless — satisfying / ASMR** — no face, no monologue. Hands-and-product close-ups,
  on-screen text, and ASMR/satisfying sound, à la "Amazon finds" demos and ASMR restocking
  accounts. Persuasion rides on a visual hook, oddly-satisfying footage, and sound. Great for
  gadgets, home, beauty, consumables, restock/refill moments.

How to pick:

1. **If the user says** (talking head, faceless, ASMR, restock, "with my avatar," "no face,"
   etc.), follow it.
2. **If they don't say**, infer from the product and pick a sensible default — but say which you
   chose and offer the other in one line, e.g. "Went faceless/ASMR since it's a refillable
   product; say the word if you'd rather a talking-head version with your avatar." If it's a
   real toss-up, ask one quick question before writing.

Everything below is shared until it splits into **Format A (talking-head)** and
**Format B (faceless)**.

## Step 1 — Understand the product (start from almost nothing)

The user will usually give **just a product name or a link**. Don't interrogate them.

- If a URL or product tools are available, look at the page: what it is, who it's for, the main
  benefit, price, what it looks like, any proof (reviews, before/after, stats).
- Infer the **target viewer**, their **top pain/desire**, the **one benefit** to lead with, and a
  believable **creator persona** (talking-head) or the **single most satisfying visual moment** of
  the product (faceless — that moment is your hook).
- Pick **one** angle. One ad = one idea. Only ask a question if there's a real fork you can't guess.
  When you infer, add a short **Assumptions** line up top so the user can redirect.

## Step 2 — The hook (80% of the job)

~71% of viewers decide within 3 seconds. Always give **three hook options** on different
approaches so the user can test — same body, different openings. The hook is delivered
differently per format:

- **Talking-head**: a spoken hook (10–14 words) shown as on-screen text too. Formulas: pattern
  interrupt, curiosity gap, problem-solution, POV/contrarian, confession (great for apps), story.
- **Faceless**: a *visual* hook + short text (5–8 words). Approaches: reveal-first (open on the
  most satisfying end state), "for those who…/POV:", or curiosity/"watch till the end."

Pair verbal/text with a strong visual either way. See `references/hooks.md` for both sets with examples.

## Step 3 — Structure

Target **~21–34s** for talking-head, **~15–30s** for faceless (restock can loop a bit longer). Keep
it tight; under ~10s rarely sells, over ~45s tanks completion.

**Talking-head arc:** Hook (0–3s) → Problem (3–8s, name the pain in the viewer's words) →
Solution/Demo (8–20s, show it working) → Proof (one credibility beat) → CTA (soft, specific, spoken +
on-screen). Spoken sentences **10–12 words max**, conversational ("I tried this and honestly…").

**Faceless arc:** Hook (satisfying tease) → Setup/"before" (the empty/messy/problem state) →
Demo/Restock (the main event: smooth satisfying product use, most of the runtime) → Payoff/Reveal
(the after) → CTA (on-screen text: "linked below"). Text stays minimal; restocks can be near-wordless.

## Step 3.5 — The conversion layer (what actually makes it sell)

A pretty video that doesn't sell is a failure. UGC ads convert on a direct-response spine —
**Hook → Problem → Solution → Value prop → Social proof → Offer CTA** — and the goal of this ad is
to get the viewer to **tap through to the store**. Bake these in regardless of format:

1. **Sell one promise, lead with the transformation.** Benefit/outcome first ("dinner solved for
   $9 a plate"), not a feature list. One product, one promise.
2. **Be specific — specificity is credibility.** Real numbers, dollar amounts, and timeframes beat
   vague claims every time. "$400/month on takeout → cut in half" outperforms "saves you money."
3. **Include a social-proof beat.** One credibility moment: a genuine-feeling result, a "10k+ sold /
   sold out twice" line, or a review quote shown as on-screen text (green-screen a review behind a
   talking head; flash a text testimonial in a faceless demo). Proof is what converts the skeptic.
4. **Handle the #1 objection in one beat.** Name the likely hesitation (price, "does it actually
   work," effort, "will it look AI/cheap") and defuse it — a quick demo, a guarantee, a before/after.
5. **Make the CTA an offer with a reason to act now.** Specific + incentivized beats "check it out."
   Use the real offer: "tap the link and use [CODE] for 20% off your first order," "free shipping
   today," "link in bio — this drop sells out." One CTA, one destination (the store). Talking-head:
   say it *and* show it on screen; faceless: on-screen text.
6. **Match the funnel if the user says so.** Cold/awareness → relatable problem hook, softer CTA
   ("see why everyone's switching"). Warm/retargeting → lead with the offer + urgency.

**Keep it honest.** Invent nothing. Don't fabricate statistics, fake reviews, or false scarcity —
it's both wrong and it tanks trust (and ad-platform approval). If you don't know the real number,
frame proof as first-person experience ("first month I saved…") and mark offer/proof placeholders
like **[insert your real discount code]** or **[your real review quote]** for the user to fill in.

## Step 4 — Break into Kling shots (≤5s each)

Both formats: slice into shots of **≤5 seconds** — Kling looks most real at ≤5s and generates in
5s/10s clips. A 20–30s ad is ~5–6 shots. Reuse the same reference description across shots for
continuity (same creator, or same hands + product + setting).

**Hard rule: no shot over 5 seconds.** If a beat needs more time (a longer demo, a big claim, a
restock), split it into two shots of ≤5s each rather than writing one 7–8s shot — the extra cut
also adds pace, which helps retention. Every timecode range you write must be ≤5s.

**Shared realism anchors** — each fights a specific AI tell; put them in every motion prompt:

- **Handheld/phone framing + slight drift** (talking-head: selfie framing; faceless: macro close-up).
  Static perfect framing reads as CGI.
- **A named light source + direction** — "soft window light from camera-left." Soft daylight reads
  real and gives the clean aesthetic; invented studio lighting is the #1 tell.
- **One micro-action** — talking-head: a glance/fidget/laugh; faceless: the specific satisfying motion.
- **One environmental imperfection** — clutter, a wrinkle, a crumb, a water droplet, a crooked label.
  Spotless = synthetic; keep it aesthetic but real.
- **Natural, slightly desaturated palette** — muted, not glossy/oversaturated.
- **≤5s** and the subject described **identically** across shots.

Negative prompts (attach every shot):

```
Talking-head: plastic skin, waxy skin, oversaturated, overly smooth, digital sharpness, cgi look,
airbrushed, perfect symmetry, warped hands, extra fingers, floating objects, stiff motion, studio lighting

Faceless (hands/product): warped hands, extra fingers, fused fingers, mangled fingers, plastic skin,
oversaturated, overly smooth, digital sharpness, cgi look, floating objects, morphing product,
warped text on packaging, stiff motion, studio lighting
```

---

## Format A — Talking-head (creator / AI avatar)

Per shot, write: **Spoken line**, **On-screen caption**, **Kling motion prompt**, **Realism cues**.
Mark each shot **talking-head** or **B-roll**.

**Dialogue handling.** Newer Kling versions generate native lip-synced dialogue from a line + a voice;
older ones don't. Write so it works either way: give the exact spoken line per shot (usable as lip-sync
input) AND collect all lines into one clean **voiceover read** at the end for VO-over-silent-B-roll.

### Output template — Talking-head

```
# UGC Ad Script — [Product]
Platform: TikTok · Format: Talking-head (avatar) · Length: ~[X]s · Angle: [one line] · Persona: [who]
Assumptions: [what you inferred]

## Creator & setting — Kling reference image
Reference-image prompt: [person, age/vibe, wardrobe, real setting, named lighting, phone-selfie framing, natural imperfections]
Negative prompt: [talking-head block]

## Hook options (test all three)
A. "[hook]" — formula: [name] · visual: [what we see]
B. / C. [...]

## Shot-by-shot
### Shot 1 — Hook · 0:00–0:04 · [talking-head | B-roll]
- Spoken: "[line]"
- On-screen caption: "[text]"
- Kling motion prompt: [action + camera + named light + micro-action + imperfection + muted color]
- Realism cues: [drift; the micro-action; the imperfection]
### Shot 2 — Problem · … → Shot 3 Solution · Shot 4 Proof (a real result / review) · Shot 5 CTA (offer + urgency: "[CODE] for X% off," spoken + on-screen)

## Clean voiceover read (all lines, for VO or lip-sync)
[all spoken lines as one natural read]

## TikTok caption + hashtags
[caption] [3–5 hashtags]

## Production notes
- Generate each shot as a ≤5s Kling clip; reuse the reference frame for a consistent creator/avatar.
- [screen-record real app UI for demo beats; which shots are talking-head vs B-roll]
```

---

## Format B — Faceless (satisfying / ASMR)

No face, no monologue. Two sub-styles (see `references/styles.md`): **satisfying product demo**
("Amazon finds") and **ASMR restock/refill**. Default to whichever fits; you can blend.

Per shot, write: **On-screen text**, **Kling motion prompt** (macro hands + product, one satisfying
action), **Sound / ASMR** (the exact sound, or the trending-audio beat — never blank; sound defines
this genre), **Realism cues**.

**Hands & small objects — make-or-break.** Faceless demos die on warped hands, Kling's #1 failure mode.
Keep hand actions simple, one or two hands, avoid intricate finger work, and **flag any shot where the
product is small or held close** as a candidate for real footage. Kling warps label text too — don't
linger on readable packaging. No voiceover by default; offer an optional VO line only if the product
truly needs a word of explanation.

### Output template — Faceless

```
# UGC Ad Script — [Product]
Platform: TikTok · Format: Faceless [satisfying demo | ASMR restock | blend] · Length: ~[X]s · Angle: [one line]
Assumptions: [what you inferred]

## Setting & hands — Kling reference image
Reference-image prompt: [macro scene: simple hands, the product, the real surface/setting, named soft light, phone-macro framing, natural imperfections]
Negative prompt: [faceless block]

## Hook options (test all three)
A. Text: "[hook]" — approach: [reveal-first | "for those who" | curiosity] · Visual: [what we open on]
B. / C. [...]

## Shot-by-shot
### Shot 1 — Hook · 0:00–0:04
- On-screen text: "[text]"
- Kling motion prompt: [macro hands + product action + camera + named light + satisfying motion + imperfection + muted color]
- Sound / ASMR: [the sound / trending-audio beat]
- Realism cues: [macro drift; simple real-hand action; the imperfection; the light]
### Shot 2 — Setup/"before" · … → Shot 3 Demo/Restock · Shot 4 Payoff (+ a proof text overlay: "sold out twice" / a ⭐️ review) · Shot 5 CTA (on-screen offer: "[CODE] for X% off — linked 👇")

## Sound design summary
[pure ASMR capture vs trending audio; the signature sounds to nail]

## Text overlay script (all captions in order)
[every on-screen caption in sequence]

## Optional voiceover (only if needed)
[one or two short lines — or "not needed for this one"]

## TikTok caption + hashtags
[caption] [3–5 hashtags]

## Production notes
- Generate each shot as a ≤5s Kling clip; reuse the reference frame so hands/product/setting stay consistent.
- [flag small-object/held shots to film for real; note any screen-record beats]
```

---

## Quick checklist (run before delivering)

**Sells (both formats):** leads with the benefit/transformation · at least one specific number,
price, or timeframe · a social-proof beat · the top objection defused in one beat · a single
offer-driven CTA to the store ("tap the link + [CODE] for X off"), not "check it out" · no fabricated
stats/reviews/urgency (placeholders marked for real numbers).

**Looks real (both formats):** every shot ≤5s · handheld/phone framing + drift · named light source +
direction · one micro-action · one aesthetic imperfection · muted palette · negative prompt attached ·
subject described consistently.

- **Talking-head also**: 3 hooks on different formulas · spoken line + caption per shot · CTA spoken +
  on-screen · a consolidated clean VO read · assumptions stated.
- **Faceless also**: faceless (hands + product only, no monologue) · a defined sound/ASMR per shot ·
  simple hand actions (small/held objects flagged for real footage) · no lingering on readable label text ·
  text-overlay script consolidated · assumptions stated.

## Reference files

- `references/styles.md` — the faceless sub-styles (demo vs restock) in depth, plus talking-head persona tips.
- `references/hooks.md` — spoken hook formulas AND faceless visual/text hooks, with examples.
- `references/example-script.md` — one worked example of each format to match the bar.

Read these for more variety or a concrete quality target.
