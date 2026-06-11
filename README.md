# ByronStatics Retro Audio Showcase

A static product showcase site for ByronStatics retro audio products, deployed to **byron-statics.com** via GitHub Pages.

## Products Featured

| Model | Type | Colors |
|-------|------|--------|
| **KBB-228** | Spherical CD Boombox (UFO-style) | Black, Silver, Wood |
| **KBB-250** | Top-loading CD Boombox (Compact) | Black |
| **KCS-315** | Portable Cassette Player + AM/FM Recorder | Black, Teal, Pink |
| **PCD-220** | Portable CD Player (Discman-style) | Pink, Teal, Clear |
| **AM66** | Vintage AM/FM Radio (Rotary) | Black, Cream |

## Tech Stack

- **HTML5** + **Tailwind CSS** (CDN, no build step)
- **Vanilla JS** (no framework)
- **Google Fonts** (Inter + Playfair Display)
- **Zero dependencies** — drop into any static host

## File Structure

```
byronstatics-showcase/
├── index.html              # Homepage with 6-product grid
├── about.html              # Brand story
├── contact.html            # Contact info
├── products/
│   ├── kbb-228.html
│   ├── kbb-250.html
│   ├── kcs-315.html
│   ├── pcd-220.html
│   └── am66.html
├── assets/
│   ├── images/
│   │   ├── kbb-228/
│   │   ├── kbb-250/
│   │   ├── kcs-315/
│   │   ├── pcd-220/
│   │   ├── am66/
│   │   └── walmart_kbb-228_black.jpg
│   ├── css/
│   └── js/
├── CNAME                   # Custom domain (byron-statics.com)
├── .gitignore
└── README.md
```

## Local Preview

Open `index.html` directly in a browser, or:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deployment to GitHub Pages

```bash
# 1. Create new repo on GitHub (personal account): byronstatics-showcase
# 2. Add remote and push
cd byronstatics-showcase
git init
git add .
git commit -m "Initial ByronStatics showcase site"
git branch -M main
git remote add origin https://github.com/<USERNAME>/byronstatics-showcase.git
git push -u origin main

# 3. Enable GitHub Pages
#    Repo → Settings → Pages
#    Source: main / (root)
#    Custom domain: byron-statics.com
#    Enforce HTTPS: ✓
```

## Custom Domain Setup (byron-statics.com)

Add these DNS records at your domain registrar (e.g. Namecheap, Cloudflare):

| Type | Host | Value |
|------|------|-------|
| CNAME | www | `<USERNAME>.github.io` |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

The `CNAME` file in the repo root tells GitHub Pages which custom domain to use.

## Image Asset Attribution

All product images are original assets from the ByronStatics brand owner.
Walmart marketplace listings referenced for spec verification (Black 4.1-4.5/5 ratings).

## License

© 2026 ByronStatics. All rights reserved.
