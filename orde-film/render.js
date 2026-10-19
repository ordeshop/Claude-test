// Renders the film page with Playwright.
//   node render.js stills 0,1.6,2.5 [sub]            -> out/still-<t>.png
//   node render.js frames <fps> <sub> <dir> [workers] -> out/<dir>/NNNNN.png (parallel browsers)
//   node render.js encode <fps> <dir> <name.mp4>       -> out/<name.mp4>, with the track if present
const { chromium } = require('playwright');
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), path = require('path');

const BASE = process.env.FILM_URL || 'http://localhost:8767/film/index.html';
const OUT = path.join(__dirname, 'out');
const DURATION = 14.5;
const [mode, ...args] = process.argv.slice(2);

async function openFilm() {
  const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--enable-gpu'] });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1152 }, deviceScaleFactor: 1 });
  page.on('console', m => { if (!/GPU stall|GL Driver/.test(m.text())) console.log('[page]', m.text()); });
  await page.goto(BASE + (process.env.FILM_QS ? '?' + process.env.FILM_QS : ''));
  await page.waitForFunction(() => window.READY || window.INIT_ERROR, null, { timeout: 120000 });
  const err = await page.evaluate(() => window.INIT_ERROR);
  if (err) throw new Error(err);
  return { browser, page, stage: await page.$('#stage') };
}

async function stills() {
  const times = (args[0] || '0,1.6,2.5,5,6.5,9.3,11').split(',').map(Number);
  const sub = +(args[1] || 16);
  const { browser, page, stage } = await openFilm();
  for (const t of times) {
    const t0 = Date.now();
    const st = await page.evaluate(([t, s]) => window.seek(t, s), [t, sub]);
    const file = path.join(OUT, `still-${t.toFixed(2)}.png`);
    await stage.screenshot({ path: file });
    console.log(`t=${t} ${st} ${Date.now() - t0}ms -> ${file}`);
  }
  await browser.close();
}

// One worker renders every k-th frame, skipping frames already on disk.
async function worker(fps, sub, dir, k, of) {
  const frames = Math.round(DURATION * fps);
  const { browser, page, stage } = await openFilm();
  const t0 = Date.now(); let done = 0;
  for (let f = k; f < frames; f += of) {
    const file = path.join(dir, String(f).padStart(5, '0') + '.png');
    if (fs.existsSync(file)) continue;
    await page.evaluate(([t, s]) => window.seek(t, s), [f / fps, sub]);
    await stage.screenshot({ path: file + '.tmp', type: 'png' });
    fs.renameSync(file + '.tmp', file);
    if (++done % 20 === 0) console.log(`[w${k}] frame ${f}/${frames} ${((Date.now() - t0) / done / 1000).toFixed(1)}s/frame`);
  }
  await browser.close();
}

async function frames() {
  const fps = +args[0], sub = +args[1], dir = path.join(OUT, args[2]), workers = +(args[3] || 1);
  fs.mkdirSync(dir, { recursive: true });
  if (process.env.WORKER) return worker(fps, sub, dir, +process.env.WORKER_K, workers);
  const kids = [...Array(workers).keys()].map(k => new Promise(res => {
    const c = spawn(process.execPath, [__filename, 'frames', ...args], { env: { ...process.env, WORKER: '1', WORKER_K: String(k) }, stdio: 'inherit' });
    c.on('close', res);
  }));
  await Promise.all(kids);
  const n = fs.readdirSync(dir).filter(f => f.endsWith('.png')).length;
  console.log(`rendered ${n}/${Math.round(DURATION * fps)} frames into ${dir}`);
}

function encode() {
  const fps = +args[0], dir = path.join(OUT, args[1]), name = args[2];
  const audio = path.join(__dirname, 'assets', 'track_14s5.wav');
  const a = ['-y', '-v', 'error', '-framerate', String(fps), '-i', path.join(dir, '%05d.png')];
  if (fs.existsSync(audio) && !process.env.NO_AUDIO) a.push('-i', audio, '-c:a', 'aac', '-b:a', '256k', '-shortest');
  a.push('-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', path.join(OUT, name));
  const r = spawnSync('ffmpeg', a, { stdio: 'inherit' });
  if (r.status) process.exit(r.status);
  console.log('wrote', path.join(OUT, name));
}

fs.mkdirSync(OUT, { recursive: true });
Promise.resolve().then(() => ({ stills, frames, encode })[mode]()).catch(e => { console.error(e); process.exit(1); });
