# ByronStatics → Vitrola Retro Design Spec

_Updated: 2026-06-10. Source: victrola.com brand DNA (Sedo-parked; spec from public knowledge of the brand) + current ByronStatics site audit._

---

## 1. The Vitrola/Victrola Design DNA

The Victrola brand (vitrola.com root, est. 1906) is THE benchmark for retro audio e-commerce. Their visual language signals "vintage hi-fi heirloom":

| Element | Vitrola | ByronStatics (current) | Delta |
|---|---|---|---|
| **Hero background** | Deep walnut wood + brass speaker grille texture | Stone-50 with dark grey gradient | Switch to deep wood + brass |
| **Primary accent** | Brass gold (`#B8893A`) + oxblood red (`#6B1F1F`) | Amber-700 only | Add oxblood as 2nd accent |
| **Body text bg** | Warm cream / parchment (`#F4EBD9`) | Stone-50 (cold grey) | Warm to parchment |
| **Section dividers** | Ornamental flourishes (✦ ❖ filigree SVG) | Plain uppercase tracking | Add filigree dividers |
| **Display font** | Cinzel / Trajan (Roman engraved) | Playfair Display (still elegant, less "heirloom") | Add Cinzel for headings |
| **Body font** | Cormorant Garamond / Lora (warm serif) | Inter (cold sans) | Switch body to Lora |
| **Hero layout** | 2-column: text left, product hero shot right with brass frame | Centered text only | Add hero product image |
| **Product cards** | Ivory bg, brass border on hover, serif title | White cards, stone-200 border, sans | Warm to ivory + brass border |
| **CTA buttons** | Brass pill / arch shape with engraved feel | Sharp rounded-md | Arch-top / pill with serif text |
| **Section labels** | Roman numerals (I. II. III.) or letters (A. B. C.) | "OUR COLLECTION" tracking caps | Use Roman numerals |
| **Tagline tone** | "Since [year] • Crafted for the Connoisseur" | "Retro Audio Collection" | Add heritage / since-cue |

---

## 2. Color Palette (Apply)

```
--bs-walnut-deep:     #1F1209   /* hero / footer bg */
--bs-walnut-mid:      #3A2418   /* secondary dark */
--bs-brass:           #B8893A   /* primary accent, CTA, borders */
--bs-brass-bright:    #D4A85A   /* hover, highlights */
--bs-oxblood:         #6B1F1F   /* secondary accent, badges */
--bs-cream:           #F4EBD9   /* main bg, replaces stone-50 */
--bs-cream-dark:      #E8DDC4   /* card bg, replaces white */
--bs-ink:             #2A1810   /* primary text (warm black, not stone-800) */
--bs-ink-soft:        #5C4A3A   /* secondary text */
```

**Tailwind extension** (add to `<script>` tailwind config):
```js
colors: {
  walnut: { deep: '#1F1209', mid: '#3A2418' },
  brass:  { DEFAULT: '#B8893A', bright: '#D4A85A' },
  oxblood: '#6B1F1F',
  cream:  { DEFAULT: '#F4EBD9', dark: '#E8DDC4' },
  ink:    { DEFAULT: '#2A1810', soft: '#5C4A3A' },
}
```

---

## 3. Typography (Apply)

**Replace font import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
```

**Usage:**
- `.font-display` → **Cinzel** (h1/h2, hero title, product names, section labels, nav logo)
- `.font-serif` → **Cormorant Garamond** (body, descriptions, large quote text)
- `.font-body` → **Lora** (small body, nav, buttons, footer)

---

## 4. Decorative Elements (Apply)

**Filigree divider SVG (inline, reusable):**
```html
<div class="flex items-center justify-center gap-4 my-12">
  <div class="h-px w-24 bg-brass"></div>
  <svg class="w-6 h-6 text-brass" viewBox="0 0 24 24" fill="currentColor">
    <path d="M12 2 L13.5 9 L21 10.5 L13.5 12 L12 19 L10.5 12 L3 10.5 L10.5 9 Z"/>
  </svg>
  <div class="h-px w-24 bg-brass"></div>
</div>
```

**Brass pill CTA:**
```html
<a href="..." class="inline-block bg-brass text-walnut-deep font-display tracking-widest text-sm px-10 py-4 rounded-full border-2 border-brass-bright hover:bg-brass-bright transition shadow-lg">
  VIEW THE COLLECTION
</a>
```

---

## 5. Section-by-Section Changes (Prioritized)

### P1 — Hero (index.html L37-49)
- [x] Replace `bg-stone-50` body → `bg-cream`
- [x] Replace `hero-bg` (grey gradient) → **walnut wood pattern**: `bg-walnut-deep` with subtle linear gradient + SVG noise overlay
- [x] Add **2-column layout**: text LEFT (40%), hero product image RIGHT (60%) — use KBB-228 球形 boombox hero shot
- [x] Add **Roman numeral eyebrow**: `I. ✦ EST. MMXXVI ✦ THE COLLECTION`
- [x] Add **filigree divider** below h1
- [x] Change CTA text to `EXPLORE THE COLLECTION` (Cinzel, brass pill)
- [x] Add **"Since 1906-inspired" tagline** small under eyebrow: `Heritage Reimagined for the Modern Listener`

### P1 — Header (index.html L23-35)
- [x] Logo: `Byron` walnut-deep + `STATICS` brass (Cinzel, all caps, tracking-widest)
- [x] Nav: Cinzel small caps, hover = brass underline (animated)
- [x] Shop CTA: brass-bordered pill, walnut text

### P1 — Product Cards (index.html L62-140)
- [x] Card bg: `bg-cream-dark` (replaces white)
- [x] Border: `border-2 border-brass/30` (replaces stone-200)
- [x] Hover: `hover:border-brass hover:shadow-2xl hover:shadow-brass/20`
- [x] Title: Cinzel 2xl
- [x] Eyebrow category: Roman numeral + small caps + brass
- [x] Price-area or "EXPLORE →" CTA: brass serif

### P2 — Brand Story Section (index.html L146-158)
- [x] Replace `bg-stone-900` → `bg-walnut-mid`
- [x] Add **large pull-quote** with Cormorant italic 4xl, large quotation marks
- [x] Add **signature line** at end: `— The ByronStatics Atelier`
- [x] Add filigree divider above + below

### P2 — Section Labels
- [x] Replace "OUR COLLECTION" → `II. THE COLLECTION` (Cinzel, brass, Roman numeral)
- [x] Add Roman numerals to all section eyebrows: `III. OUR PHILOSOPHY`, `IV. CONTACT`

### P3 — Footer
- [x] Replace `bg-stone-950` → `bg-walnut-deep`
- [x] Footer logo Cinzel, all caps
- [x] Add **double brass line** divider before copyright
- [x] Footer tagline: `CRAFTED WITH HERITAGE • KELL PRODUCE LIMITED` (or generic "Crafted with Heritage" if client-facing)

### P3 — Product Pages (kbb-228.html, etc.)
- [x] Same color/typography overhaul
- [x] Add **specs table** styled as engraved plaque (brass border, Cinzel labels)
- [x] Add **"Pair With" / "From the Collection"** cross-sell at bottom

---

## 6. Heritage / Trust Cues (Apply throughout)

- **Top bar** (above header, optional): `✦ FREE SHIPPING ON ORDERS OVER $99 ✦ 30-DAY RETURNS ✦` — brass text on walnut-deep
- **Trust strip** (below hero, before products): 4 small icons + text: "SINCE-STYLE HERITAGE" / "HAND-FINISHED" / "1-YEAR WARRANTY" / "AUTHENTIC VINTAGE SOUND"
- **Footer badge**: small Vitrola-inspired "EST. 1906" mark (replace with `EST. MMXXVI` or just remove if not authentic)

---

## 7. What NOT to copy from Vitrola

- ❌ Don't literally steal their logo, product photography, or copy
- ❌ Don't claim "est. 1906" or any false heritage
- ❌ Don't use their exact tagline
- ✅ Take the **design language** (colors, fonts, ornaments) — apply ByronStatics's own voice

---

## 8. Implementation Order

1. **Apply colors + fonts to `index.html`** ← START HERE (one file, full overhaul)
2. Generate `previews/index-v2.html` screenshot for review
3. Apply same to `about.html`, `contact.html`
4. Apply to 5 product pages
5. Add top bar + trust strip + footer polish

---

## 9. Reference Imagery (find later)

For hero product image, the spherical KBB-228 is the iconic piece — use `assets/images/kbb-228/kbb-228-front-cd-lid-open.jpg` as the hero (most photogenic).

Vitrola reference sites to scout for cross-check:
- victrola.com (Wayback Machine 2023)
- crosleyradio.com (sister brand, similar DNA)
- Roberts Radio (UK retro)
