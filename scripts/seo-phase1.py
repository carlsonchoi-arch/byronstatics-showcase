#!/usr/bin/env python3
"""
SEO Phase 1 head injection for byron-statics.com
- Replaces existing <title> and meta description with optimized versions
- Adds canonical, OG, Twitter Card, JSON-LD schema
- Adds theme color, GSC slot, and tracking slot
"""
import re
from pathlib import Path

ROOT = Path("/Users/brian/.hermes/work/byronstatics-showcase")

# ============================================================
# Per-page SEO config
# ============================================================
PAGES = {
    "index.html": {
        "path": "/",
        "title": "ByronStatics — Retro Boomboxes, CD Players & Cassette Recorders | 70s/80s Audio",
        "desc": "Shop retro-styled boomboxes, portable CD players, cassette recorders, and AM/FM radios. By ByronStatics — far out sound from the sunshine era, available now on Walmart.",
        "og_type": "website",
        "schema": "home",
    },
    "about.html": {
        "path": "/about.html",
        "title": "About ByronStatics — The Story Behind Far Out Retro Audio",
        "desc": "ByronStatics is a Vaughn Marketing Inc. brand dedicated to bringing the iconic sound of 70s & 80s audio back to life. Learn about our retro audio philosophy.",
        "og_type": "website",
        "schema": "about",
    },
    "contact.html": {
        "path": "/contact.html",
        "title": "Contact ByronStatics — Say Hi to Our Retro Audio Crew",
        "desc": "Get in touch with ByronStatics for product questions, wholesale inquiries, or just to say hi. We respond to every message.",
        "og_type": "website",
        "schema": "contact",
    },
    "products/kbb-228.html": {
        "path": "/products/kbb-228.html",
        "title": "KBB-228 Spherical CD Boombox — UFO-Style Retro CD Player | ByronStatics",
        "desc": "ByronStatics KBB-228 spherical UFO-style CD boombox. Top-loading CD, AM/FM stereo, 6 brass control buttons, central LCD display, dual speakers. Shop the iconic round boombox.",
        "og_type": "product",
        "schema": "product",
    },
    "products/kbb-250.html": {
        "path": "/products/kbb-250.html",
        "title": "KBB-250 CD Boombox — Top-Load AM/FM Stereo | ByronStatics",
        "desc": "ByronStatics KBB-250 retro CD boombox. Top-loading CD, AM/FM stereo, dual 1W speakers, AC/DC power, 6 C-battery option. Classic 80s boombox style.",
        "og_type": "product",
        "schema": "product",
    },
    "products/kcs-315.html": {
        "path": "/products/kcs-315.html",
        "title": "KCS-315 Portable Cassette Player & Recorder — AM/FM | ByronStatics",
        "desc": "ByronStatics KCS-315 portable AM/FM cassette recorder. VAS (Voice Activation System), built-in mic, 2x AA or Micro USB power, 3 colors. Walkman-style retro.",
        "og_type": "product",
        "schema": "product",
    },
    "products/pcd-220.html": {
        "path": "/products/pcd-220.html",
        "title": "PCD-220 Portable CD Player — 60s Anti-Skip, 5 EQ | ByronStatics",
        "desc": "ByronStatics PCD-220 Discman-style portable CD player. 60-second anti-skip, 5 EQ presets, 3 colorways (Pink, Blue, Clear), earbuds included, 2x AA or USB power.",
        "og_type": "product",
        "schema": "product",
    },
    "products/am66.html": {
        "path": "/products/am66.html",
        "title": "AM66 AM/FM Radio — Vintage Rotary Dial, USB-C | ByronStatics",
        "desc": "ByronStatics AM66 vintage AM/FM radio. Rotary controls, telescopic antenna, 4W output, USB-C charging, available in Black and Cream. Classic 70s portable radio style.",
        "og_type": "product",
        "schema": "product",
    },
}

# Product-specific schema (rich data for Google)
PRODUCT_SCHEMA = {
    "products/kbb-228.html": {
        "name": "ByronStatics KBB-228 Spherical CD Boombox",
        "image": "kbb-228-front-control-panel-hero.jpg",
        "sku": "KBB-228",
        "mpn": "BS-KBB228",
        "desc": "Spherical UFO-style CD boombox with top-loading CD, AM/FM stereo, 6 brass control buttons, central LCD display, dual speakers, AC/DC power.",
        "rating": "4.1",
        "review_count": "92",
    },
    "products/kbb-250.html": {
        "name": "ByronStatics KBB-250 CD Boombox",
        "image": "kbb-250-front-hero-shot-powered-on.jpg",
        "sku": "KBB-250",
        "mpn": "BS-KBB250",
        "desc": "Top-loading CD boombox with AM/FM stereo, dual 1W speakers, AC/DC power, 6 C-cell battery option.",
        "rating": "4.2",
        "review_count": "325",
    },
    "products/kcs-315.html": {
        "name": "ByronStatics KCS-315 Portable Cassette Player",
        "image": "kcs-315-front-hero-view.jpg",
        "sku": "KCS-315",
        "mpn": "BS-KCS315",
        "desc": "Portable AM/FM cassette recorder with VAS, built-in mic, 2x AA or Micro USB power, 3 colors.",
        "rating": "4.0",
        "review_count": "192",
    },
    "products/pcd-220.html": {
        "name": "ByronStatics PCD-220 Portable CD Player",
        "image": "pcd220-pink-closed-hero.jpg",
        "sku": "PCD-220",
        "mpn": "BS-PCD220",
        "desc": "Discman-style portable CD player with 60-second anti-skip, 5 EQ presets, 3 colorways, earbuds included.",
        "rating": "4.1",
        "review_count": "425",
    },
    "products/am66.html": {
        "name": "ByronStatics AM66 AM/FM Radio",
        "image": "am66-cream-front-3q-dial.jpg",
        "sku": "AM66",
        "mpn": "BS-AM66",
        "desc": "Vintage AM/FM radio with rotary controls, telescopic antenna, 4W output, USB-C charging, 2 colors.",
        "rating": "4.5",
        "review_count": "121",
    },
}

BASE_URL = "https://byron-statics.com"
BRAND_NAME = "ByronStatics"
BRAND_OWNER = "Vaughn Marketing Inc."
SITE_NAME = f"{BRAND_NAME} — Far Out Audio"
DEFAULT_OG_IMAGE = f"{BASE_URL}/assets/images/kbb-228/kbb-228-front-hero.jpg"
SITE_DESCRIPTION = "Far out retro audio from the 70s & 80s — boomboxes, CD players, cassette recorders, and AM/FM radios. By ByronStatics."

# ============================================================
# Tracking IDs — set these once you have them
# ============================================================
# GA4 placeholder: replace G-XXXXXXXXXX with your actual Measurement ID
GA4_ID = None  # e.g., "G-ABC123DEF4"
# Plausible (privacy-friendly alternative)
PLAUSIBLE_DOMAIN = "byron-statics.com"  # set to None to disable
# Google Search Console verification
GSC_VERIFICATION = None  # e.g., "abc123def456..."


def build_tracking_snippet() -> str:
    """Build GA4 / Plausible / GSC verification code."""
    parts = []
    if GSC_VERIFICATION:
        parts.append(f'  <meta name="google-site-verification" content="{GSC_VERIFICATION}">')
    if GA4_ID:
        parts.append(f"""  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>""")
    if PLAUSIBLE_DOMAIN:
        parts.append(f"""  <!-- Plausible Analytics -->
  <script defer data-domain="{PLAUSIBLE_DOMAIN}" src="https://plausible.io/js/script.js"></script>""")
    return "\n".join(parts)


def build_og_twitter(page_cfg: dict) -> str:
    """Build Open Graph + Twitter Card meta tags."""
    url = BASE_URL + page_cfg["path"]
    og_image = DEFAULT_OG_IMAGE
    if page_cfg["schema"] == "product" and page_cfg["path"].startswith("/products/"):
        prod = page_cfg["path"].replace("/products/", "").replace(".html", "")
        ps = PRODUCT_SCHEMA.get(f"products/{prod}.html", {})
        if ps:
            og_image = f"{BASE_URL}/assets/images/{prod}/{ps['image']}"
    tags = [
        f'  <meta property="og:type" content="{page_cfg["og_type"]}">',
        f'  <meta property="og:site_name" content="{SITE_NAME}">',
        f'  <meta property="og:title" content="{page_cfg["title"]}">',
        f'  <meta property="og:description" content="{page_cfg["desc"]}">',
        f'  <meta property="og:url" content="{url}">',
        f'  <meta property="og:image" content="{og_image}">',
        f'  <meta property="og:image:width" content="1200">',
        f'  <meta property="og:image:height" content="630">',
        f'  <meta property="og:image:alt" content="{page_cfg["title"]}">',
        f'  <meta property="og:locale" content="en_US">',
        f'  <meta name="twitter:card" content="summary_large_image">',
        f'  <meta name="twitter:title" content="{page_cfg["title"]}">',
        f'  <meta name="twitter:description" content="{page_cfg["desc"]}">',
        f'  <meta name="twitter:image" content="{og_image}">',
        f'  <meta name="twitter:image:alt" content="{page_cfg["title"]}">',
    ]
    return "\n".join(tags)


def build_schema(page_cfg: dict) -> str:
    """Build JSON-LD structured data per page type."""
    url = BASE_URL + page_cfg["path"]
    if page_cfg["schema"] == "home":
        return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "{BASE_URL}/#organization",
      "name": "{BRAND_NAME}",
      "alternateName": "Byron Statics",
      "url": "{BASE_URL}",
      "logo": "{BASE_URL}/assets/images/byronstatics-correct-logo-reference.jpg",
      "description": "{SITE_DESCRIPTION}",
      "brand": {{
        "@type": "Brand",
        "name": "{BRAND_NAME}"
      }},
      "parentOrganization": {{
        "@type": "Organization",
        "name": "{BRAND_OWNER}"
      }},
      "sameAs": [
        "https://www.walmart.com/seller/103033976"
      ]
    }},
    {{
      "@type": "WebSite",
      "@id": "{BASE_URL}/#website",
      "url": "{BASE_URL}",
      "name": "{SITE_NAME}",
      "description": "{SITE_DESCRIPTION}",
      "publisher": {{"@id": "{BASE_URL}/#organization"}},
      "inLanguage": "en-US"
    }}
  ]
}}
</script>"""
    if page_cfg["schema"] == "about":
        return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About {BRAND_NAME}",
  "url": "{url}",
  "description": "{page_cfg["desc"]}",
  "isPartOf": {{"@id": "{BASE_URL}/#website"}},
  "about": {{"@id": "{BASE_URL}/#organization"}},
  "inLanguage": "en-US"
}}
</script>"""
    if page_cfg["schema"] == "contact":
        return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact {BRAND_NAME}",
  "url": "{url}",
  "description": "{page_cfg["desc"]}",
  "isPartOf": {{"@id": "{BASE_URL}/#website"}},
  "about": {{"@id": "{BASE_URL}/#organization"}},
  "inLanguage": "en-US"
}}
</script>"""
    if page_cfg["schema"] == "product":
        path = f"products/{page_cfg['path'].split('/')[-1]}"
        p = PRODUCT_SCHEMA.get(path, {})
        if not p:
            return ""
        og_image = f"{BASE_URL}/assets/images/{path.replace('products/', '').replace('.html', '')}/{p['image']}"
        return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{p['name']}",
  "image": [
    "{og_image}"
  ],
  "description": "{p['desc']}",
  "sku": "{p['sku']}",
  "mpn": "{p['mpn']}",
  "brand": {{
    "@type": "Brand",
    "name": "{BRAND_NAME}"
  }},
  "manufacturer": {{
    "@type": "Organization",
    "name": "{BRAND_OWNER}"
  }},
  "offers": {{
    "@type": "Offer",
    "url": "{url}",
    "priceCurrency": "USD",
    "priceValidUntil": "2027-12-31",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {{
      "@type": "Organization",
      "name": "Walmart"
    }}
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "{p['rating']}",
    "reviewCount": "{p['review_count']}",
    "bestRating": "5",
    "worstRating": "1"
  }}
}}
</script>"""
    return ""


def process_file(rel_path: str, cfg: dict) -> None:
    full = ROOT / rel_path
    html = full.read_text(encoding="utf-8")
    original_len = len(html)

    # 1. Replace <title>
    html = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", html, count=1, flags=re.S)

    # 2. Replace meta description (if exists), else add before </head>
    if re.search(r'<meta\s+name="description"\s+content="[^"]*"', html):
        html = re.sub(
            r'<meta\s+name="description"\s+content="[^"]*"',
            f'<meta name="description" content="{cfg["desc"]}"',
            html, count=1,
        )
    else:
        html = html.replace("</head>", f'  <meta name="description" content="{cfg["desc"]}">\n</head>', 1)

    # 3. Build full injection block
    canonical_url = BASE_URL + cfg["path"]
    canonical_block = f'  <link rel="canonical" href="{canonical_url}">'

    theme_block = '  <meta name="theme-color" content="#1B6B61">'
    robots_block = '  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'

    og_block = build_og_twitter(cfg)
    schema_block = build_schema(cfg)
    tracking_block = build_tracking_snippet()

    # Combine all new head content
    new_head_content = "\n".join(filter(bool, [
        "  <!-- SEO: Core -->",
        canonical_block,
        robots_block,
        theme_block,
        "",
        "  <!-- SEO: Open Graph + Twitter Card -->",
        og_block,
        "",
        "  <!-- SEO: Structured Data (JSON-LD) -->",
        schema_block,
        "",
        tracking_block,
    ]))

    # 4. Insert before </head> — remove any pre-existing SEO meta we want to overwrite
    html = re.sub(r'\s*<link\s+rel="canonical"[^>]*>\s*', '\n', html)
    html = re.sub(r'\s*<meta\s+name="robots"[^>]*>\s*', '\n', html)
    html = re.sub(r'\s*<meta\s+name="theme-color"[^>]*>\s*', '\n', html)
    html = re.sub(r'\s*<meta\s+property="og:[^"]+"[^>]*>\s*', '\n', html)
    html = re.sub(r'\s*<meta\s+name="twitter:[^"]+"[^>]*>\s*', '\n', html)
    html = re.sub(r'\s*<script\s+type="application/ld\+json">.*?</script>\s*', '\n', html, flags=re.S)

    # Insert new block before </head>
    html = html.replace("</head>", f"\n{new_head_content}\n</head>", 1)

    full.write_text(html, encoding="utf-8")
    delta = len(html) - original_len
    print(f"  ✅ {rel_path:35s}  {original_len:>6} → {len(html):>6} bytes  (+{delta})")


def main():
    print("=" * 70)
    print("SEO Phase 1: Injecting head meta + structured data into 8 pages")
    print("=" * 70)
    for rel_path, cfg in PAGES.items():
        process_file(rel_path, cfg)
    print()
    print("=" * 70)
    print(f"Tracking configured: GA4={'on' if GA4_ID else 'OFF (placeholder)'}, "
          f"Plausible={'on' if PLAUSIBLE_DOMAIN else 'off'}, "
          f"GSC={'on' if GSC_VERIFICATION else 'OFF (placeholder)'}")
    print("=" * 70)


if __name__ == "__main__":
    main()
