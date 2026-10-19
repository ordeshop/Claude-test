// Prints the camera path and where key things land on screen, and checks
// that the glide never slows or reverses and the zoom never turns inward.
const T = require('./film/timeline.js');
const layout = require('./film/capture/layout.json');
const tl = T.make(layout);
const piece = id => layout.pieces.find(p => p.id === id);
console.log('cruise px/s', tl.cruise.toFixed(1), 'D_over', tl.D_OVER.toFixed(0));
let prev = null, bad = [];
for (let t = 0; t <= 14.5 + 1e-9; t += 1 / 60) {
  const c = tl.camera(t);
  if (prev && t < 8.2) {
    const v = (c.ly - prev.ly) * 60;
    if (t > 0.05 && v < -1e-6) bad.push(`ly reverses at ${t.toFixed(3)}`);
    if (c.D < prev.D - 1e-6) bad.push(`zoom-in at ${t.toFixed(3)}`);
  }
  prev = c;
}
console.log(bad.length ? bad.slice(0, 10).join('\n') : 'flight: glide monotonic, no zoom-in');
for (const t of [0, 0.6, 1.25, 1.35, 1.6, 2.5, 3, 5, 5.4, 6.5, 7.3, 8.0, 8.3, 8.475, 8.65, 9.25, 9.3, 9.47, 9.7, 9.97, 11, 14.5]) {
  const c = tl.camera(t);
  const f = (p) => { const q = tl.project(c, p); return `${q.x.toFixed(0)},${q.y.toFixed(0)}@${q.depth.toFixed(0)}`; };
  let s = `t=${t.toFixed(2)} ${c.stage.padEnd(8)} ly=${c.ly.toFixed(0).padStart(5)} D=${c.D.toFixed(0).padStart(5)} tilt=${(c.tilt*180/Math.PI).toFixed(1).padStart(4)} spd=${(tl.speed(t)).toFixed(2)}`;
  s += ` | pageTop ${f([720, 0, 0])} pageBot ${f([720, tl.H, 0])}`;
  console.log(s);
}
const at = (t, label, p) => { const c = tl.camera(t); const q = tl.project(c, p); console.log(`  ${label} @${t}: ${q.x.toFixed(0)},${q.y.toFixed(0)} depth ${q.depth.toFixed(0)} coc ${(q.depth < c.focus ? 75 * (c.focus - q.depth) / q.depth : 6 * (q.depth - c.focus) / q.depth).toFixed(1)}`); };
for (const t of [0, 0.6, 1.0, 1.35, 1.8, 2.4]) for (const tile of tl.tiles(t)) at(t, `${tile.id} size ${tile.size.toFixed(0)}`, tile.c);
for (const t of [4.9, 5.2, 5.4, 5.6, 5.8, 6.0, 6.3]) for (const tile of tl.tiles(t).filter(x => x.id === 'tile-4')) at(t, tile.id, tile.c);
for (const id of ['demo-chip-3', 'demo-chip-5', 'demo-chip-0', 'demo-chip-2']) { const p = piece(id); const s = tl.pieceState(p, 2.5); at(2.5, `${id} z=${s.z.toFixed(0)}`, [p.x + p.w / 2 + s.dx, p.y + p.h / 2, s.z]); }
const h2 = 1087; console.log('  section-2 title crosses centre at', tl.crossTime(h2).toFixed(2));
console.log('  testimonial crosses centre at', tl.crossTime(piece('testimonial-0').y + 144).toFixed(2));
console.log('  "Noch unsicher?" crosses at', tl.crossTime(7602).toFixed(2), ' footer logo', tl.crossTime(7998).toFixed(2));
