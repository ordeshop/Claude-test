// Step 1: capture the landing page as a flat base (lifting pieces hidden) plus
// each lifting piece alone on transparency, and record every piece's page box.
// Usage: node capture.js <url> <outdir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const URL = process.argv[2] || 'http://localhost:8765/index.html';
const OUT = process.argv[3] || path.join(__dirname, 'film', 'capture');
const DPR = 2, PAD = 28, TILE = 4096; // tile height in device px (WebGL max 8192)

// What lifts. kind decides how the film animates it.
const LAYERS = [
  ['hero-phone',  '.hero .phone-frame'],
  ['hero-button', '.hero .hero-btns .btn.big'],
  ['hero-chip',   '.hero ul.facts li'],
  ['demo-photo',  '.demoframe .screen'],
  ['demo-chip',   '.demoframe .browserbar'],
  ['branch-card', '.branchcard'],
  ['step-card',   '.steps-section .steps li'],
  ['price-card',  '.cards .card:not(.featured)'],
  ['testimonial', '.cards .card.featured'],
  ['process-card','.steps:not(.steps-section .steps) li'],
  ['final-button','.final .btn.big'],
];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: DPR });
  await page.goto(URL, { waitUntil: 'networkidle' });

  // Scroll to the bottom once so lazy images load and reveal animations fire.
  const h0 = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y <= h0; y += 400) { await page.evaluate(y => scrollTo(0, y), y); await page.waitForTimeout(70); }
  await page.waitForTimeout(1500);
  await page.evaluate(() => scrollTo(0, 0));

  // Freeze the page: no intro overlay, no floating buttons, no transitions,
  // phone slideshow parked on its first screen.
  await page.addStyleTag({ content: `
    *,*::before,*::after{transition:none!important;animation:none!important}
    .waFloat,.toTop,a.skip{display:none!important}
    .reveal{opacity:1!important;transform:none!important}
    .site-head{position:relative!important}
    html{scroll-behavior:auto!important}` });
  await page.evaluate(() => {
    for (let i = 1; i < 99999; i++) clearInterval(i);
    window.setInterval = () => 0;  // the phone slideshow restarts itself on resize
    document.querySelectorAll('body > div').forEach(d => {
      if (getComputedStyle(d).position === 'fixed') d.remove();
    });
    const slides = document.querySelectorAll('.pslide');
    slides.forEach((s, i) => { s.loading = 'eager'; s.classList.toggle('is-active', i === 0); });
    const label = document.getElementById('phoneLabel');
    if (label && slides[0]) label.innerHTML = slides[0].getAttribute('data-label');
  });
  await page.evaluate(() => Promise.all([...document.images].map(i => i.decode().catch(() => {}))));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);

  // Mark pieces.
  const pieces = await page.evaluate(({ LAYERS, PAD }) => {
    const out = [];
    for (const [kind, sel] of LAYERS) {
      document.querySelectorAll(sel).forEach((el, i) => {
        if (el.closest('[data-layer]')) return;
        const id = `${kind}-${i}`;
        el.setAttribute('data-layer', id);
        const r = el.getBoundingClientRect();
        out.push({ id, kind, index: i, x: r.x + scrollX, y: r.y + scrollY, w: r.width, h: r.height, pad: PAD,
          radius: parseFloat(getComputedStyle(el).borderTopLeftRadius) || 0 });
      });
    }
    return out;
  }, { LAYERS, PAD });

  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  const W = 1440;

  // Base page with every piece hidden.
  await page.addStyleTag({ content: `[data-layer]{visibility:hidden!important}` });
  await page.setViewportSize({ width: W, height: H });
  await page.waitForTimeout(300);
  const tiles = [];
  for (let y = 0, i = 0; y < H * DPR; y += TILE, i++) {
    const hh = Math.min(TILE, H * DPR - y);
    const file = `page-${i}.png`;
    await page.screenshot({ path: path.join(OUT, file), clip: { x: 0, y: y / DPR, width: W, height: hh / DPR } });
    tiles.push({ file, y: y / DPR, h: hh / DPR });
  }
  // One full page at 1x for previews.
  await page.screenshot({ path: path.join(OUT, 'page-full-1x.jpg'), fullPage: true, quality: 85, type: 'jpeg', scale: 'css' });

  // Each piece alone on transparency: hide everything, reveal only the piece,
  // drop its own box-shadow (the film draws its own shadows).
  await page.addStyleTag({ content: `
    html,body{background:transparent!important}
    body *{visibility:hidden!important}
    .solo-on, .solo-on *{visibility:visible!important}
    .solo-on{box-shadow:none!important}` });
  for (const p of pieces) {
    await page.evaluate(id => {
      document.querySelectorAll('.solo-on').forEach(e => e.classList.remove('solo-on'));
      document.querySelector(`[data-layer="${id}"]`).classList.add('solo-on');
    }, p.id);
    p.file = `${p.id}.png`;
    await page.screenshot({ path: path.join(OUT, p.file), omitBackground: true,
      clip: { x: p.x - PAD, y: p.y - PAD, width: p.w + PAD * 2, height: p.h + PAD * 2 } });
  }

  fs.writeFileSync(path.join(OUT, 'layout.json'), JSON.stringify({ width: W, height: H, dpr: DPR, tiles, pieces }, null, 1));
  console.log(`page ${W}x${H}, ${tiles.length} tiles, ${pieces.length} pieces`);
  console.log(pieces.map(p => `${p.id} ${Math.round(p.x)},${Math.round(p.y)} ${Math.round(p.w)}x${Math.round(p.h)}`).join('\n'));
  await browser.close();
})();
