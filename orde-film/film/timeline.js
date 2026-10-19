// Camera path and per-piece animation for the Ordé fly-over.
// Pure functions of time. Loaded by the film page and by the Node checks.
(function (root) {
  const F = 1880, W = 1440, HS = 1152;           // focal length and frame
  const DEG = Math.PI / 180;
  const TILT0 = 56 * DEG;
  const PIN_Y = HS - 42;                          // page bottom edge line during the rise
  const CARD_W = 1018, CARD_TOP = 283, HERO_BOTTOM = 903;

  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  const ss = (a, b, x) => { x = clamp((x - a) / (b - a), 0, 1); return x * x * (3 - 2 * x); };
  const mix = (a, b, u) => a + (b - a) * u;

  function make(layout) {
    const H = layout.height;
    const LY0 = 420;                               // top half of the hero, phone in focus
    const D_OVER = F * H / (PIN_Y - 42);           // whole page fills 42..1110

    // Speed down the page, as a share of cruise.
    function speed(t) {
      if (t < 0.6) return 0.5 * ss(0, 0.6, t);
      if (t < 1.25) return 0.5;
      if (t < 1.6) return 0.5 + 0.5 * ss(1.25, 1.6, t);
      if (t < 7.3) return 1.0;
      return 1.0 - 0.88 * ss(7.3, 8.3, t);
    }
    // Integrate it once into a table.
    const DT = 1 / 2000, N = Math.ceil(14.6 / DT);
    const S = new Float64Array(N + 1);
    for (let i = 0; i < N; i++) S[i + 1] = S[i] + DT * 0.5 * (speed(i * DT) + speed((i + 1) * DT));
    const Sat = t => { const x = clamp(t / DT, 0, N - 1e-9), i = Math.floor(x); return mix(S[i], S[i + 1], x - i); };

    // Rise: log-distance speed is a smooth trapezoid.
    const riseV = t => ss(7.75, 8.35, t) * (1 - ss(8.95, 9.25, t));
    const RV = new Float64Array(N + 1);
    for (let i = 0; i < N; i++) RV[i + 1] = RV[i] + DT * 0.5 * (riseV(i * DT) + riseV((i + 1) * DT));
    const RVat = t => { const x = clamp(t / DT, 0, N - 1e-9), i = Math.floor(x); return mix(RV[i], RV[i + 1], x - i); };
    const RV_TOT = RVat(9.25);

    const D_FLIGHT_START = 1480, D_FLIGHT_END = 1760;  // wider than 1360 so the hero headline fits
    function distance(t) {
      if (t <= 7.75) { const u = t / 7.75; return mix(D_FLIGHT_START, D_FLIGHT_END, 1 - (1 - u) * (1 - u)); }
      if (t <= 9.25) return Math.exp(mix(Math.log(D_FLIGHT_END), Math.log(D_OVER), RVat(t) / RV_TOT));
      return null; // later stages are driven by scale
    }
    const tilt = t => TILT0 * (1 - ss(8.15, 8.95, t));
    const pinLook = (D, th) => H - (PIN_Y - HS / 2) * D / (F * Math.cos(th) + (PIN_Y - HS / 2) * Math.sin(th));

    // Pick the cruise speed so the glide meets the pinned camera mid-handover.
    const TM = 8.475;
    const cruise = (pinLook(distance(TM), tilt(TM)) - LY0) / Sat(TM);
    const glide = t => LY0 + cruise * Sat(t);

    // Overhead creep and dive, in log scale.
    const K_OVER = F / D_OVER;
    const creep = u => 1 + 0.035 * u * u;
    const K_C = K_OVER * creep(1);
    const K_F = CARD_W / W;
    const M0 = (0.035 * 2 / creep(1)) / 0.22 * 0.5;  // d ln k / du at dive start (u over 0.5 s)
    function hermite(p0, p1, m0, m1, s) {
      const s2 = s * s, s3 = s2 * s;
      return (2 * s3 - 3 * s2 + 1) * p0 + (s3 - 2 * s2 + s) * m0 + (-2 * s3 + 3 * s2) * p1 + (s3 - s2) * m1;
    }
    const TOP_C = HS / 2 - K_C * H / 2;
    const LY_F = (HS / 2 - CARD_TOP) / K_F;

    // Full camera state at time t.
    function camera(t) {
      let D, th, ly, stage, maskBottom = H, belowFade = 0, radius = 24;
      if (t < 9.25) {
        D = distance(t); th = tilt(t);
        if (t < 8.3) ly = glide(t);
        else if (t < 8.65) ly = mix(glide(t), pinLook(D, th), ss(8.3, 8.65, t));
        else ly = pinLook(D, th);
        stage = t < 7.75 ? 'flight' : 'rise';
      } else if (t < 9.47) {
        const u = (t - 9.25) / 0.22;
        D = D_OVER / creep(u); th = 0; ly = H / 2; stage = 'overhead';
      } else if (t < 9.97) {
        const u = (t - 9.47) / 0.5;
        const k = Math.exp(hermite(Math.log(K_C), Math.log(K_F), M0, 0, u));
        const top = mix(TOP_C, CARD_TOP, ss(0.3, 1.0, u));
        D = F / k; th = 0; ly = (HS / 2 - top) / k; stage = 'dive';
        belowFade = ss(0.0, 0.75, u);
        maskBottom = mix(H, HERO_BOTTOM, ss(0.55, 0.95, u));
        radius = mix(24, 38 / K_F, ss(0.2, 1.0, u));
      } else {
        const k = K_F * (1 + 0.02 * ss(9.97, 14.5, t));
        D = F / k; th = 0; ly = LY_F; stage = 'card';
        belowFade = 1; maskBottom = HERO_BOTTOM; radius = 38 / K_F;
      }
      // flight looks a touch left of centre so the hero headline is not cut; eases back during the rise
      const lx = W / 2 - 60 * (1 - ss(7.9, 8.9, t));
      const L = [lx, ly, 0];
      const sn = Math.sin(th), cs = Math.cos(th);
      const pos = [L[0], L[1] + D * sn, D * cs];
      return { t, D, tilt: th, ly, L, pos, focus: D, stage, maskBottom, belowFade, radius,
        fwd: [0, -sn, -cs], up: [0, -cs, sn], right: [1, 0, 0] };
    }

    function project(cam, p) {
      const d = [p[0] - cam.pos[0], p[1] - cam.pos[1], p[2] - cam.pos[2]];
      const z = d[0] * cam.fwd[0] + d[1] * cam.fwd[1] + d[2] * cam.fwd[2];
      const x = d[0];
      const y = d[1] * cam.up[1] + d[2] * cam.up[2];
      return { x: W / 2 + F * x / z, y: HS / 2 - F * y / z, depth: z };
    }
    function unproject(cam, sx, sy, depth) {
      const x = (sx - W / 2) * depth / F, y = (HS / 2 - sy) * depth / F;
      return [0, 1, 2].map(i => cam.pos[i] + cam.fwd[i] * depth + cam.right[i] * x + cam.up[i] * y);
    }

    // Time at which the glide puts a page y in the middle of the frame.
    function crossTime(y) {
      let a = 0, b = 8.3;
      for (let i = 0; i < 50; i++) { const m = (a + b) / 2; glide(m) < y ? a = m : b = m; }
      return a;
    }

    // ---- pieces --------------------------------------------------------
    const CARD_FLOAT = { 'branch-card': 18, 'step-card': 20, 'price-card': 22, 'process-card': 18, 'final-button': 16 };
    function pieceState(p, t) {
      const cy = p.y + p.h / 2;
      const tc = crossTime(cy);
      const settle = (a, b) => 1 - ss(a, b, t);
      let z = 0, angle = 0, thick = 0, dx = 0;
      switch (p.kind) {
        case 'hero-phone': z = 6 + 24 * ss(0.0, 1.2, t); break;
        case 'hero-button': z = 4 + 18 * ss(0.15, 0.9, t); break;
        case 'hero-chip': {
          const e = ss(0.1 + 0.08 * p.index, 1.35, t) * settle(4.0, 5.0);
          z = [64, 72, 80][p.index] * e + 2; angle = 30 * DEG * e; break;
        }
        case 'demo-photo': {
          const row = p.index < 3 ? 0 : 1, col = p.index % 3;
          const e = (row ? ss(1.75, 2.7, t) : ss(1.35, 2.2, t)) * settle(tc + 2.6, tc + 3.6);
          z = ([112, 126, 104][col] + row * 6) * e; angle = 46 * DEG * e; break;
        }
        case 'demo-chip': {
          if (p.index === 3 || p.index === 5) {
            const e = ss(1.55, 2.5, t) * settle(tc + 2.4, tc + 3.4);
            z = 200 * e; angle = 54 * DEG * e; dx = (p.index === 3 ? -240 : 240) * e;
          }
          break;
        }
        case 'testimonial': {
          const e = ss(tc - 0.75, tc + 0.1, t) * settle(tc + 2.2, tc + 3.2);
          z = mix(22, 112, e); angle = 30 * DEG * e; thick = 56 * e; break;
        }
        default:
          z = (CARD_FLOAT[p.kind] || 0) + (p.index % 3) * 3;
      }
      // Pieces below the hero fade out with the page during the dive.
      const fade = cy > HERO_BOTTOM ? camera(t).belowFade : 0;
      return { z, angle, thick, fade, dx };
    }

    // ---- logo tiles (3D, flight only) ------------------------------------
    const TILE_START = [0, 1, 2, 3].map(i => [690 + 16 + i * 44, 640, 0]);
    const TILE_HANG = [
      [10, 250, 150, 150],
      [110, 70, 196, 124],
      [1340, 90, 176, 136],
      [1440, 280, 140, 168],
    ];
    let PASSER = null;
    function tiles(t) {
      const out = [];
      for (let i = 0; i < 4; i++) {
        const e = ss(0.1 + 0.07 * i, 1.35, t);
        const trail = 300 * ss(1.2, 2.4, t);
        const h = TILE_HANG[i], s0 = TILE_START[i];
        out.push({
          id: 'tile-' + i,
          c: [mix(s0[0], h[0], e), mix(s0[1], h[1], e) + trail, mix(0, h[2], e)],
          size: mix(32, h[3], e), angle: 52 * DEG * e,
          fade: ss(2.6, 3.1, t),
        });
      }
      // One tile drifts past the left edge, close and blurred, at 5.4 s.
      if (!PASSER) {
        const cam = camera(5.4);
        PASSER = unproject(cam, 20, 640, 640);
      }
      if (t > 4.2 && t < 6.6) {
        const drift = (t - 5.4) * -420;  // slides out past the left edge
        out.push({ id: 'tile-4', c: [PASSER[0] + drift, PASSER[1], PASSER[2]], size: 190, angle: 56 * DEG,
          fade: ss(6.0, 6.5, t) });
      }
      return out;
    }

    return { F, W, HS, H, cruise, D_OVER, K_F, LY0, speed, glide, distance, tilt, camera, project, unproject,
      crossTime, pieceState, tiles, HERO_BOTTOM, CARD_TOP };
  }

  const api = { make, ss, mix, clamp };
  if (typeof module !== 'undefined') module.exports = api; else root.Timeline = api;
})(typeof window !== 'undefined' ? window : globalThis);
