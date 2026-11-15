// Clean captures of nichecounter.fr for the promo (mobile 390x844 @3x).
// Fixed bottom nav hidden, page fully scrolled first so scroll-reveal content is painted.
// Usage: node scripts/capture.mjs   -> assets/raw/clean/*.png + clean/boxes.json
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright'); // pre-installed globally in this environment
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const OUT = path.join(ROOT, 'assets/raw/clean/');
fs.mkdirSync(OUT, { recursive: true });
const BASE = 'https://nichecounter.fr';
const BEST = '/annonce/ac95cac8-d942-46e0-bd5e-012f6491cbbe';
const boxes = {};

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, locale: 'fr-FR', isMobile: true, hasTouch: true });
const p = await ctx.newPage();

async function go(u) {
  await p.goto(BASE + u, { waitUntil: 'networkidle' });
  for (let y = 0; y < 6000; y += 250) { await p.evaluate((y) => window.scrollTo(0, y), y); await p.waitForTimeout(90); }
  await p.evaluate(() => window.scrollTo(0, 0));
  await p.waitForTimeout(900);
  // hide fixed/sticky elements anchored at the bottom (mobile tab bar)
  await p.evaluate(() => {
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if (cs.position === 'fixed' && e.getBoundingClientRect().top > 500) e.style.display = 'none';
    }
  });
  await p.waitForTimeout(300);
}
async function box(name, sel) {
  const h = p.locator(sel).first();
  const bb = await h.evaluate((e) => { const r = e.getBoundingClientRect(); return { x: r.x, y: r.y + window.scrollY, w: r.width, h: r.height }; });
  boxes[name] = bb; return bb;
}
const shot = (name, clip) => p.screenshot({ path: OUT + name + '.png', ...(clip ? { clip, fullPage: true } : {}) });

// 1. home screen (viewport), + search bar box
await go('/');
await shot('home_screen');
await box('home_search', 'input[placeholder^="Rechercher un parfum"]');
await box('home_header', 'header');

// 2. results "Renaissance", default order (Plus récent) then sorted (Prix croissant)
await go('/?q=Renaissance');
await shot('results_default');
await box('results_chip_asc', 'button:has-text("Prix croissant")');
const cards = p.locator('a[href*="/annonce/"]:visible');
const n = await cards.count();
boxes.results_default_cards = [];
for (let i = 0; i < n; i++) {
  const t = (await cards.nth(i).innerText()).replace(/\n/g, ' | ');
  const bb = await cards.nth(i).evaluate((e) => { const r = e.getBoundingClientRect(); return { x: r.x, y: r.y + window.scrollY, w: r.width, h: r.height }; });
  boxes.results_default_cards.push({ t, ...bb });
  await shot('card_default_' + i, { x: bb.x - 2, y: bb.y - 2, width: bb.w + 4, height: bb.h + 4 });
}
await go('/?q=Renaissance&tri=price-asc');
await shot('results_sorted');
await box('results_sorted_grid', 'a[href*="/annonce/"]:visible >> xpath=..');
const g = boxes.results_sorted_grid;
await shot('results_sorted_grid', { x: 0, y: g.y - 24, width: 390, height: g.h + 48 });
// chips row (selected state)
const chips = await box('chips', 'button:has-text("Plus récent") >> xpath=..');
await shot('chips_sorted', { x: 0, y: chips.y - 8, width: 390, height: chips.h + 16 });

// 3. product page of the best offer
await go(BEST);
await box('pd_brand', 'text=XERJOFF');
await box('pd_protection', 'text=Fonds bloqués >> xpath=../..');
await box('pd_seller', 'text=Flacon Club >> xpath=ancestor::div[contains(@class,"rounded")][1]');
await box('pd_price', 'text=Soit >> xpath=..');
const top = boxes.pd_brand.y - 24;
const bottom = boxes.pd_protection.y + boxes.pd_protection.h + 24;
await shot('product_strip', { x: 0, y: top, width: 390, height: bottom - top });
await shot('product_protection', { x: boxes.pd_protection.x - 6, y: boxes.pd_protection.y - 6, width: boxes.pd_protection.w + 12, height: boxes.pd_protection.h + 12 });

fs.writeFileSync(OUT + 'boxes.json', JSON.stringify(boxes, null, 1));
console.log(JSON.stringify(boxes, null, 1));
await b.close();
