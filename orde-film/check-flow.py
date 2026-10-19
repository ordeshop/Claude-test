"""Optical-flow check of a rendered preview.

Measures, frame to frame during the flight, how fast the page moves through
the sharp middle band (vertical flow) and whether the picture is shrinking or
growing (horizontal scale of the flow). The glide must never dip while it
cruises, and the scale must never turn into a zoom-in.

usage: python3 check-flow.py out/preview30 30
"""
import sys, os
import numpy as np
import cv2

import json
d, fps = sys.argv[1], float(sys.argv[2])
CAMS = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else None

def to_page(cam, sx, sy):
    """Screen point (full res) -> point on the page plane, via the film's camera."""
    F = CAMS['F']; c = cam
    pos, fw, up, rt = map(np.array, (c['pos'], c['fwd'], c['up'], c['right']))
    dirs = rt[None, :] * (sx - 720)[:, None] + up[None, :] * (576 - sy)[:, None] + fw[None, :] * F
    s = -pos[2] / dirs[:, 2]
    return pos[None, :] + dirs * s[:, None]
files = sorted(f for f in os.listdir(d) if f.endswith('.png'))
flight_end = int(8.2 * fps)

def load(i):
    im = cv2.imread(os.path.join(d, files[i]), cv2.IMREAD_GRAYSCALE)
    return cv2.resize(im, (720, 576), interpolation=cv2.INTER_AREA)

rows = []
prev = load(0)
for i in range(1, min(flight_end, len(files))):
    cur = load(i)
    # track textured points (text, photos) in the sharp middle band; flat
    # backgrounds carry no motion information
    mask = np.zeros_like(prev); mask[130:380, 40:680] = 255
    pts = cv2.goodFeaturesToTrack(prev, 400, 0.01, 6, mask=mask)
    v, s = float('nan'), float('nan')
    if pts is not None and len(pts) >= 12:
        nxt, st, _ = cv2.calcOpticalFlowPyrLK(prev, cur, pts, None, winSize=(21, 21), maxLevel=3)
        ok = st.ravel() == 1
        a0, a1 = pts[ok].reshape(-1, 2), nxt[ok].reshape(-1, 2)
        if len(a0) >= 12:
            M, inl = cv2.estimateAffinePartial2D(a0, a1, method=cv2.RANSAC, ransacReprojThreshold=1.0)
            if M is not None:
                inl = inl.ravel() == 1
                if CAMS:
                    # page px the camera moved down the page: a point fixed on the page
                    # appears in frame i at the page position seen through camera i
                    p0 = to_page(CAMS['cams'][i - 1], a0[inl, 0] * 2, a0[inl, 1] * 2)
                    # read the new positions through the previous frame's camera: how far
                    # the page slid, in page px, is the glide speed down the page
                    p1 = to_page(CAMS['cams'][i - 1], a1[inl, 0] * 2, a1[inl, 1] * 2)
                    v = float(np.median(p0[:, 1] - p1[:, 1]))
                else:
                    v = float(-np.median(a1[inl, 1] - a0[inl, 1]) * 2)   # full-res px/frame, + = gliding down the page
                s = float(np.hypot(M[0, 0], M[1, 0]) - 1)            # < 0 shrinking, > 0 zooming in
    rows.append((i / fps, v, s))
    prev = cur

t = np.array([r[0] for r in rows]); v = np.array([r[1] for r in rows]); s = np.array([r[2] for r in rows])
# smooth a little: Farneback is noisy on blurred areas
k = 3
vs = np.convolve(np.nan_to_num(v, nan=np.nanmedian(v)), np.ones(k) / k, mode='same')
cruise = (t > 1.75) & (t < 7.2)
med = np.median(vs[cruise])
dips = [(round(a, 2), round(b, 1)) for a, b in zip(t[cruise], vs[cruise]) if b < 0.85 * med]
zoom_in = [(round(a, 2), round(b, 5)) for a, b in zip(t, s) if b > 0.002]
nan = int(np.isnan(v).sum())
print('frames without enough texture to track:', nan)
print(f'frames checked: {len(rows)} (0..{t[-1]:.2f}s)')
print(f'cruise glide: median {med:.1f} page px/frame ({med*fps:.0f} px/s), min {vs[cruise].min():.1f}, max {vs[cruise].max():.1f}')
print('dips below 85% of cruise:', dips if dips else 'none')
print('zoom-in frames (scale > +0.002/frame):', zoom_in if zoom_in else 'none')
for a, b, c in rows[::int(fps // 3)]:
    print(f'  t={a:5.2f}  glide {b:6.1f} px/frame  scale {c:+.4f}')
