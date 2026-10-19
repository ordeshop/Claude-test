// Renders the film page with Playwright.
//   node render.js stills 0,1.6,2.5        -> out/still-<t>.png
//   node render.js video [fps] [sub]       -> out/frames piped to ffmpeg -> out/orde-flyover.mp4
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');

const BASE = process.env.FILM_URL || 'http://localhost:8766/film/index.html';
const OUT = path.join(__dirname, 'out');
const mode = process.argv[2] || 'stills';
const QS = process.env.FILM_QS || '';

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--enable-gpu'] });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1152 }, deviceScaleFactor: 1 });
  page.on('console', m => console.log('[page]', m.text()));
  await page.goto(BASE + (QS ? '?' + QS : ''));
  await page.waitForFunction(() => window.READY || window.INIT_ERROR, null, { timeout: 120000 });
  const err = await page.evaluate(() => window.INIT_ERROR);
  if (err) { console.error(err); process.exit(1); }
  const stage = await page.$('#stage');

  if (mode === 'stills') {
    const times = (process.argv[3] || '0,1.6,2.5,5,6.5,9.3,11').split(',').map(Number);
    const sub = +(process.argv[4] || 16);
    for (const t of times) {
      const t0 = Date.now();
      const st = await page.evaluate(([t, s]) => window.seek(t, s), [t, sub]);
      const file = path.join(OUT, `still-${t.toFixed(2)}.png`);
      await stage.screenshot({ path: file });
      console.log(`t=${t} ${st} ${(Date.now() - t0)}ms -> ${file}`);
    }
  } else {
    const fps = +(process.argv[3] || 60), sub = +(process.argv[4] || 16);
    const name = process.argv[5] || `orde-flyover-${fps}fps.mp4`;
    const frames = Math.round(14.5 * fps);
    const audio = path.join(__dirname, 'assets', 'track_14s5.wav');
    const args = ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-'];
    if (fs.existsSync(audio) && !process.env.NO_AUDIO) args.push('-i', audio, '-c:a', 'aac', '-b:a', '256k', '-shortest');
    args.push('-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', path.join(OUT, name));
    const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'inherit', 'inherit'] });
    const t0 = Date.now();
    for (let f = 0; f < frames; f++) {
      const t = f / fps;
      await page.evaluate(([t, s]) => window.seek(t, s), [t, sub]);
      const buf = await stage.screenshot({ type: 'png' });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 30 === 0) {
        const el = (Date.now() - t0) / 1000;
        console.log(`frame ${f}/${frames} t=${t.toFixed(2)} ${el.toFixed(0)}s elapsed, eta ${(el / (f + 1) * (frames - f - 1) / 60).toFixed(1)} min`);
      }
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    console.log('done', path.join(OUT, name));
  }
  await browser.close();
})();
