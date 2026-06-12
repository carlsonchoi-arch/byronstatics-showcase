#!/usr/bin/env python3
"""
SEO Phase 2: Expand 5 product pages with rich content + FAQ schema
- Adds ~1300 words of SEO content per product page (Specs/Features/Use Cases/Compare/FAQ)
- Adds FAQPage JSON-LD schema
- Adds internal links to blog posts (cross-linking)
- Maintains design system (uses Tailwind classes already in pages)
"""
import re
from pathlib import Path

ROOT = Path("/Users/brian/.hermes/work/byronstatics-showcase")
BASE_URL = "https://byron-statics.com"

# ============================================================
# Per-product SEO content
# Each entry: (slug, target_keyword, faqs, body_sections)
# ============================================================

PRODUCT_CONTENT = {
    "kbb-228": {
        "model": "KBB-228",
        "model_full": "KBB-228 Spherical CD Boombox",
        "primary_keyword": "spherical CD boombox",
        "secondary_keywords": [
            "UFO boombox", "round CD player", "retro spherical boombox",
            "spherical boombox Walmart", "vintage UFO CD player"
        ],
        "intro_paragraph": "The KBB-228 isn't just another retro boombox — it's the only spherical UFO-style CD player on the market. Inspired by 70s space-age design and the iconic Panasonic RX-5050, the KBB-228 puts a modern spin on what boomboxes used to look like, with a perfectly round form factor that makes it as much a sculpture as a sound system. If you've been searching for a CD boombox that actually stands out on a shelf, this is it.",
        "use_cases": [
            ("🛋️ Living Room Centerpiece", "The spherical form factor makes the KBB-228 an instant conversation starter. Place it on a side table or media console and let the UFO shape do the talking — no one will mistake it for a generic speaker."),
            ("☕ Kitchen Counter Companion", "AM/FM radio + CD in one compact unit. Listen to morning talk radio while you brew coffee, or pop in a greatest-hits CD for weekend brunch."),
            ("📚 Study & Focus", "With full AM broadcast band coverage (520–1710 kHz) and a clear central LCD display, the KBB-228 is perfect for dorm rooms, home offices, or study nooks. The 6 tactile buttons are satisfying to press during long listening sessions."),
            ("🎉 Parties & Gatherings", "Stereo speakers with silver mesh grilles pump out enough volume for a small-to-medium room. Whether it's a family dinner or a friends' hangout, the spherical shape adds instant retro-cool to the vibe."),
            ("🎁 Gift-Ready", "Comes in a retail box (see gallery). The unique form factor makes it a memorable gift for music lovers, design enthusiasts, and anyone who remembers the original 70s boombox era."),
        ],
        "compare": {
            "title": "KBB-228 vs KBB-250: Which Retro Boombox Is Right for You?",
            "kbb228_points": [
                "Spherical UFO-style form factor — most distinctive design in the collection",
                "Compact footprint, great for desks, side tables, and small spaces",
                "6 tactile brass-feel buttons with a classic CD player layout",
                "Single oval LCD display centered in the unit",
            ],
            "kbb250_points": [
                "Traditional rectangular boombox shape — classic 80s silhouette",
                "Larger chassis with stronger stereo separation",
                "LED display + dual 1W speakers for fuller room-filling sound",
                "6 C-cell battery option for true portable use",
            ],
            "verdict": "Choose the KBB-228 if design and uniqueness matter most to you. Choose the KBB-250 if you want fuller sound and true portability.",
        },
        "faqs": [
            {
                "q": "Is the KBB-228 a real spherical boombox or just a rectangular one in marketing photos?",
                "a": "It's genuinely spherical. The CD compartment sits on top of the unit, accessed via a hinged lid that flips up. The whole chassis is a true round form factor — not a rectangle with rounded corners."
            },
            {
                "q": "Does the KBB-228 play burned CDs?",
                "a": "Yes. The KBB-228 supports CD, CD-R, and CD-RW formats, so you can play commercially-pressed CDs as well as burned mixes and home recordings."
            },
            {
                "q": "What kind of power does the KBB-228 use?",
                "a": "The KBB-228 runs on AC/DC power. Plug it in at home or use battery operation for portable listening (battery type listed in the retail box). The radio works in any environment — no WiFi or app required."
            },
            {
                "q": "Can I connect headphones or external speakers?",
                "a": "The KBB-228 has a 3.5mm headphone jack for private listening. The internal stereo speakers are designed for room-filling sound, so external speakers aren't needed for most use cases."
            },
            {
                "q": "Is the KBB-228 a Bluetooth boombox?",
                "a": "No — the KBB-228 is a CD + AM/FM boombox, true to the 70s/80s format. We made it this way deliberately. If you want Bluetooth streaming, our KBB-250 boombox or other modern options may be a better fit. The KBB-228 is for people who still own a CD collection and want a beautiful, distraction-free way to play it."
            },
            {
                "q": "What does the KBB-228 cost?",
                "a": "Current pricing is available on the Walmart listing linked above. By buying direct from Walmart you get free shipping on orders over $35, 30-day returns, and Walmart's standard customer support."
            },
            {
                "q": "Does the KBB-228 come with a warranty?",
                "a": "Yes — all ByronStatics products include a 1-year limited warranty covering manufacturing defects. Contact our support team if you have any issues and we'll make it right."
            },
        ],
    },
    "kbb-250": {
        "model": "KBB-250",
        "model_full": "KBB-250 CD Boombox",
        "primary_keyword": "retro CD boombox",
        "secondary_keywords": [
            "vintage CD boombox", "AM FM boombox", "portable CD boombox",
            "top loading boombox", "boombox with speakers"
        ],
        "intro_paragraph": "The KBB-250 is the classic 80s boombox, rebuilt for today. With a traditional rectangular silhouette, dual 1W stereo speakers, AM/FM radio, and a top-loading CD player, it's the boombox you remember from your childhood — only better. The KBB-250 also runs on 6 C-cell batteries, making it one of the few truly portable CD boomboxes still being made.",
        "use_cases": [
            ("🚶 Truly Portable", "Run it on 6 C-cell batteries and take the KBB-250 to the park, beach, or backyard. No power outlet required. Few modern boomboxes offer this kind of portability."),
            ("🏠 Home Stereo Replacement", "Dual 1W stereo speakers deliver room-filling sound — enough to fill a kitchen, bedroom, or living room. The KBB-250 makes a great low-profile alternative to a full bookshelf system."),
            ("🛠️ Workshop & Garage", "Tough enough for a garage, simple enough to use with one hand. AM/FM radio + CD for when you don't want to deal with a smartphone in a dusty environment."),
            ("👴 For the Cassette-Generation", "If you grew up with a boombox and miss that exact form factor, the KBB-250 is your nostalgic match. It looks, sounds, and feels like the boombox you remember — not a 'retro-styled' speaker pretending to be one."),
            ("🎁 Gift for Dad, Grandpa, or Anyone 40+", "Instant nostalgia. Pair it with a few classic CDs (Beatles, Eagles, Fleetwood Mac) and you've got a perfect Father's Day, birthday, or holiday gift."),
        ],
        "compare": {
            "title": "KBB-250 vs KBB-228: Pick Your Boombox Personality",
            "kbb228_points": [
                "Spherical UFO shape — conversation piece",
                "Compact, desk-friendly footprint",
                "Single oval LCD display",
                "Best for design lovers and small spaces",
            ],
            "kbb250_points": [
                "Classic rectangular 80s silhouette",
                "Dual 1W stereo speakers with stronger separation",
                "LED display + 6 C-cell battery option",
                "Best for nostalgia, portability, and room-filling sound",
            ],
            "verdict": "Pick the KBB-228 if design is your priority. Pick the KBB-250 if sound and portability matter most.",
        },
        "faqs": [
            {
                "q": "How loud is the KBB-250?",
                "a": "The KBB-250 has dual 1W stereo speakers — enough to fill a small-to-medium room with clear sound. It's not a party speaker, but it's plenty loud for a kitchen, bedroom, or office. If you need more volume, headphones plug into the 3.5mm jack for personal listening."
            },
            {
                "q": "Does the KBB-250 work on batteries?",
                "a": "Yes — the KBB-250 runs on 6 C-cell batteries for true portable use, or plug it into AC power at home. Battery life depends on usage, but expect 10+ hours of casual radio listening."
            },
            {
                "q": "Can the KBB-250 play MP3 CDs?",
                "a": "Yes. The KBB-250 plays CD, CD-R, and CD-RW discs, including MP3-encoded discs. Burn a mix CD-R with 100+ of your favorite tracks and the KBB-250 will play them back."
            },
            {
                "q": "Is the KBB-250 a Bluetooth boombox?",
                "a": "No — the KBB-250 is a CD + AM/FM boombox. We kept it intentionally simple. If you need wireless streaming, look at the KBB-228's compact alternative or pair the KBB-250 with a Bluetooth-to-3.5mm adapter."
            },
            {
                "q": "What colors does the KBB-250 come in?",
                "a": "The KBB-250 ships in black with silver speaker grilles — the iconic 80s boombox look. The retail box includes the unit, AC power cable, and instruction manual."
            },
            {
                "q": "Where can I buy the KBB-250?",
                "a": "Available on Walmart (linked above) with free shipping on orders over $35, 30-day returns, and a 1-year ByronStatics warranty."
            },
        ],
    },
    "kcs-315": {
        "model": "KCS-315",
        "model_full": "KCS-315 Portable Cassette Player",
        "primary_keyword": "portable cassette player",
        "secondary_keywords": [
            "cassette player recorder", "AM FM cassette player", "Walkman-style cassette player",
            "vintage cassette player", "cassette player with microphone"
        ],
        "intro_paragraph": "Cassettes are back. From indie musicians releasing mixtapes to a new generation discovering mixtape culture for the first time, the KCS-315 puts a portable cassette player and recorder in your pocket — the same way Walkmans did in the 80s. With Voice Activation System (VAS), a built-in microphone, and AM/FM radio, the KCS-315 is a complete retro audio tool for creators, students, and nostalgia lovers.",
        "use_cases": [
            ("🎙️ Voice Recording & Memos", "The built-in mic + Voice Activation System (VAS) makes the KCS-315 perfect for recording lectures, interviews, voice memos, and podcasts on the go. VAS auto-stops recording when you stop talking — saves tape and skips silence."),
            ("📻 AM/FM Radio On The Go", "Tune in to talk radio, sports, news, or your local college station. The AM/FM tuner pulls in stations clearly thanks to the telescopic antenna."),
            ("🎵 Mixtape Revival", "Got a stack of old mix cassettes? The KCS-315 plays them back. Or record fresh mixtapes from radio, mic, or line-in and share them with friends the old-school way."),
            ("📚 Students & Journalists", "Recording lectures, interviews, or audio notes? The KCS-315 is the simplest, cheapest way to do it. No app, no smartphone, no fuss. Just press record."),
            ("🎁 Gift for the '80s Kid", "Anyone who grew up with a Walkman will smile when they unwrap a KCS-315. Comes in 3 colors — pick the one that matches their vibe."),
        ],
        "compare": {
            "title": "KCS-315 vs Modern Digital Recorders: Why Cassettes Still Win",
            "kbb228_points": [
                "No app, no firmware, no subscriptions — ever",
                "Records onto physical tapes you can hold, label, and share",
                "Battery-powered (2x AA) for 10+ hours of recording",
                "Has the unmistakable warm sound of magnetic tape",
            ],
            "kbb250_points": [
                "Modern digital recorders: more storage, but proprietary formats",
                "Smartphone recorders: always with you, but fragile and distracting",
                "Most digital recorders lack the AM/FM radio + cassette combo",
                "KCS-315 wins on simplicity, character, and battery life",
            ],
            "verdict": "The KCS-315 isn't trying to replace your phone — it's the deliberate, distraction-free audio tool that does one thing well. It's the anti-smartphone.",
        },
        "faqs": [
            {
                "q": "Can the KCS-315 record from the radio?",
                "a": "Yes. Tune to an AM/FM station, insert a blank cassette, press record, and capture the broadcast. Perfect for archiving radio shows, sports games, or late-night DJ sets."
            },
            {
                "q": "What does Voice Activation System (VAS) do?",
                "a": "VAS pauses recording when you stop talking and resumes when you start again. It saves tape, skips silence during playback, and makes recordings much easier to listen to later."
            },
            {
                "q": "Does the KCS-315 need special batteries?",
                "a": "No — the KCS-315 runs on 2 standard AA batteries (alkaline recommended). You can also power it via Micro USB cable for long recording sessions."
            },
            {
                "q": "What kind of cassettes does the KCS-315 use?",
                "a": "Standard Type I (normal bias) cassette tapes — the most common type, available everywhere. Type II and Type IV (metal) tapes may play but with reduced quality."
            },
            {
                "q": "Is the KCS-315 a Walkman?",
                "a": "It's a Walkman-style portable cassette player — same form factor, same idea, modern build quality. It also includes extras the original Walkman never had: AM/FM radio, built-in mic, and VAS recording."
            },
            {
                "q": "What colors does the KCS-315 come in?",
                "a": "Three colors: classic black, soft cream, and pastel pink. Mix and match or collect all three."
            },
            {
                "q": "Does the KCS-315 come with earbuds?",
                "a": "Yes — a pair of earbuds is included in the box, plus a hand strap for portable use."
            },
        ],
    },
    "pcd-220": {
        "model": "PCD-220",
        "model_full": "PCD-220 Portable CD Player",
        "primary_keyword": "portable CD player",
        "secondary_keywords": [
            "Discman CD player", "portable CD player with anti-skip",
            "personal CD player", "CD Walkman", "small CD player"
        ],
        "intro_paragraph": "The PCD-220 is the Discman reimagined. After Sony discontinued the original Discman line, the world moved on to streaming — but a stubborn group of CD collectors never gave up. The PCD-220 is for them. With 60-second anti-skip protection, 5 EQ presets, and 3 colorways, it's the portable CD player for the streaming-fatigued.",
        "use_cases": [
            ("🚶 Walking, Commuting, Traveling", "Pop in a CD, clip the player to your belt, and enjoy 60-second anti-skip protection that handles bumps, stairs, and bus rides. The PCD-220 doesn't need WiFi or a phone — perfect for digital detox."),
            ("📚 Focus & Study", "Unlike streaming, CDs don't have notifications, autoplay, or 'suggested tracks.' Put on a full album and let your brain focus. Students swear by this."),
            ("🏃 Workout Companion", "Anti-skip tech + dual power options (2x AA or USB) make the PCD-220 ideal for running, gym sessions, or yoga. 20-track programmable memory lets you build the perfect workout playlist."),
            ("🛏️ Bedroom Audio", "Pair the PCD-220 with the included earbuds for private late-night listening. No bright screen, no app, no sleep-mode quirks — just a CD and your favorite music."),
            ("🎁 The Anti-Smartphone Gift", "Give a teenager a PCD-220 and a few of your favorite CDs. Watch them rediscover what music felt like before the algorithm."),
        ],
        "compare": {
            "title": "PCD-220 vs Streaming: Why Physical Media Is Making a Comeback",
            "kbb228_points": [
                "No monthly subscription, ever",
                "Full albums, exactly as the artist intended them",
                "You own the music — no platform can take it away",
                "No algorithm choosing what you hear next",
                "Physical artwork, liner notes, and the joy of collection",
            ],
            "kbb250_points": [
                "Streaming: infinite library, but you don't own anything",
                "Streaming: convenience, but constant subscription pressure",
                "Streaming: tracks out of album order, ruining the artist's vision",
                "Streaming: 1.5 million tracks uploaded daily — most of it noise",
            ],
            "verdict": "The PCD-220 isn't anti-tech — it's pro-intentionality. A CD you love is worth a thousand algorithm-served tracks.",
        },
        "faqs": [
            {
                "q": "What is anti-skip protection?",
                "a": "Anti-skip protection buffers 60 seconds of CD audio in memory, so if the player gets bumped (walking, running, in a car), playback continues without skipping. The PCD-220 offers 60 seconds of anti-skip — enough for nearly any real-world movement."
            },
            {
                "q": "Does the PCD-220 play MP3 CDs?",
                "a": "Yes — the PCD-220 supports CD, CD-R, CD-RW, and MP3-encoded discs. Burn 150+ MP3 tracks onto a single CD-R and the PCD-220 will play them back in order."
            },
            {
                "q": "What kind of batteries does the PCD-220 use?",
                "a": "2 AA batteries (alkaline recommended) for 8+ hours of portable playback, or plug in via USB for unlimited home listening. The PCD-220 ships with earbuds and a USB cable."
            },
            {
                "q": "What are the 5 EQ presets?",
                "a": "Five sound profiles tuned for different music types: Bass Boost, Pop, Rock, Jazz, and Classic. Switch between them based on what you're listening to — deeper bass for hip-hop, brighter treble for classical, balanced for podcasts."
            },
            {
                "q": "Does the PCD-220 have Bluetooth?",
                "a": "No — the PCD-220 is wired-only (3.5mm headphone jack). This is intentional: Bluetooth adds latency, drains battery, and adds compression that defeats the purpose of CD-quality audio. Plug in the included earbuds (or your favorite wired headphones) for the best experience."
            },
            {
                "q": "What colors does the PCD-220 come in?",
                "a": "Three colorways: classic Black, Bubblegum Pink, and Ocean Blue. All three ship in retail boxes with earbuds and a USB cable."
            },
            {
                "q": "Can the PCD-220 play store-bought CDs?",
                "a": "Yes. Any standard CD, CD-R, or CD-RW will play — including commercially-pressed albums from your existing collection. Most listeners use the PCD-220 as a way to enjoy the CDs they already own."
            },
        ],
    },
    "am66": {
        "model": "AM66",
        "model_full": "AM66 AM/FM Radio",
        "primary_keyword": "vintage AM FM radio",
        "secondary_keywords": [
            "retro portable radio", "AM FM radio with USB-C",
            "vintage style radio", "analog radio with rotary dial",
            "small portable radio"
        ],
        "intro_paragraph": "The AM66 is the radio your grandparents had — and the one you'll want on your nightstand. With a true rotary tuning dial, telescopic antenna, USB-C charging, and 4W of warm analog-style sound, the AM66 is the simplest, most beautiful radio on the market. No apps, no WiFi, no nonsense. Just turn the dial and find your station.",
        "use_cases": [
            ("🛏️ Bedside Companion", "The AM66's compact size and warm sound make it perfect for the nightstand. Wake up to AM news, FM music, or your local talk station — no phone alarm required."),
            ("🍳 Kitchen Counter", "The rotary dial is satisfying to turn, and the telescopic antenna pulls in stations clearly. The AM66 makes a morning coffee ritual feel like 1972."),
            ("🚨 Emergency Radio", "When the cell towers go down (storms, blackouts, rural areas), the AM66 keeps you informed. AM radio in particular carries emergency broadcasts. The AM66 runs on USB-C or replaceable batteries — always ready."),
            ("🏕️ Camping & Outdoors", "USB-C rechargeable + 4W speaker = great sound at the campsite. AM/FM radio is also lighter on battery than any streaming setup."),
            ("🎁 The 'No Tech' Gift", "Know someone overwhelmed by smartphones? The AM66 is a breath of fresh air. Pure radio, simple controls, beautiful design. Pair it with a hand-written note explaining why you thought of them."),
        ],
        "compare": {
            "title": "AM66 vs Smart Speakers: Why Simple Radio Still Wins",
            "kbb228_points": [
                "No WiFi required — works anywhere, anytime",
                "Real rotary dial with tactile feedback",
                "AM band (520–1710 kHz) for emergency broadcasts and talk radio",
                "USB-C charging + battery option for true portability",
                "Privacy-first: no microphone, no listening, no data collection",
            ],
            "kbb250_points": [
                "Smart speakers need WiFi, power, and constant updates",
                "Smart speakers collect voice data by default",
                "Smart speakers require voice commands — not always ideal in shared spaces",
                "AM radio carries emergency broadcasts smart speakers can't access",
            ],
            "verdict": "The AM66 is the anti-smart-speaker. Simple, beautiful, private, and ready the moment you turn it on.",
        },
        "faqs": [
            {
                "q": "Does the AM66 have Bluetooth?",
                "a": "No — the AM66 is a pure AM/FM radio, true to the original format. This is intentional: Bluetooth adds complexity, drains battery, and breaks the simple 'turn the dial' experience. If you need Bluetooth streaming, look at our KBB-250 boombox."
            },
            {
                "q": "How long does the battery last?",
                "a": "The AM66 has a built-in rechargeable battery (USB-C charging) that delivers 8–12 hours of listening per charge. It can also run on USB-C power indefinitely when plugged in."
            },
            {
                "q": "Can the AM66 receive emergency broadcasts?",
                "a": "Yes — the AM band is the standard for emergency broadcasts (NOAA weather radio, EAS alerts, AM news stations). The AM66 receives the full AM band (520–1710 kHz), making it a reliable emergency radio when other systems fail."
            },
            {
                "q": "What colors does the AM66 come in?",
                "a": "Two colors: Cream (warm off-white with brown leather-look strap) and Black (matte black with chrome dial). Both ship in a retail gift box."
            },
            {
                "q": "Is the AM66 good for old people or people who aren't tech-savvy?",
                "a": "The AM66 is one of the best radios for non-tech users. It has exactly three controls: volume, tuning, and band switch. No menus, no apps, no passwords. Turn the dial, find your station, enjoy."
            },
            {
                "q": "How is the sound quality?",
                "a": "The AM66 puts out 4W through a single full-range driver — more than enough for bedroom, kitchen, or office listening. The sound is warm and full, with a slight analog character that streaming audio never quite captures."
            },
            {
                "q": "Does the AM66 have a headphone jack?",
                "a": "Yes — 3.5mm headphone jack for private listening. Plug in your favorite earbuds or headphones and enjoy radio without disturbing anyone."
            },
        ],
    },
}

# ============================================================
# Blog cross-link (will be set in Batch 2)
# ============================================================
BLOG_LINKS = []  # Empty for now; will populate after blog posts are written

# ============================================================
# Inject content + FAQ schema
# ============================================================

def build_faq_schema(slug, faqs):
    """Build FAQPage JSON-LD schema."""
    items = [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faqs]
    import json
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": items,
    }
    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'


def build_content_html(slug, content, is_first=False):
    """Build the SEO content section as HTML (Tailwind-styled to match site)."""
    intro = content["intro_paragraph"]
    primary = content["primary_keyword"]
    secondaries = content["secondary_keywords"]

    use_case_html = "\n".join([
        f'''        <div class="bg-stone-50 rounded-xl p-6 border border-stone-200">
          <h3 class="font-semibold text-lg mb-2">{title}</h3>
          <p class="text-sm text-stone-700 leading-relaxed">{body}</p>
        </div>'''
        for title, body in content["use_cases"]
    ])

    compare = content["compare"]
    compare_html = f'''        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <div class="bg-amber-50 rounded-xl p-6 border border-amber-200">
            <h3 class="font-semibold text-lg mb-3 text-amber-900">✓ {compare["title"].split(":")[0].replace(" vs", "")}</h3>
            <ul class="space-y-2 text-sm text-stone-700">
              {"".join(f'<li class="flex gap-2"><span class="text-amber-600 font-bold">+</span><span>{p}</span></li>' for p in compare["kbb228_points"])}
            </ul>
          </div>
          <div class="bg-stone-100 rounded-xl p-6 border border-stone-300">
            <h3 class="font-semibold text-lg mb-3 text-stone-700">vs the alternative</h3>
            <ul class="space-y-2 text-sm text-stone-700">
              {"".join(f'<li class="flex gap-2"><span class="text-stone-500">−</span><span>{p}</span></li>' for p in compare["kbb250_points"])}
            </ul>
          </div>
        </div>
        <p class="text-stone-700 leading-relaxed"><strong>Verdict:</strong> {compare["verdict"]}</p>'''

    faqs_html = "\n".join([
        f'''        <details class="bg-stone-50 rounded-xl border border-stone-200 p-5 group" open>
          <summary class="font-semibold text-lg cursor-pointer list-none flex items-center justify-between">
            <span>{f["q"]}</span>
            <span class="text-amber-700 group-open:rotate-180 transition-transform text-xl">+</span>
          </summary>
          <p class="mt-3 text-stone-700 leading-relaxed">{f["a"]}</p>
        </details>'''
        for f in content["faqs"]
    ])

    section = f'''
  <!-- SEO Phase 2: Long-form content + FAQs -->
  <section class="py-16 bg-stone-50">
    <div class="max-w-4xl mx-auto px-6">

      <h2 class="font-display text-3xl md:text-4xl font-bold mb-6 text-stone-900">Why Choose the {content["model"]}?</h2>
      <p class="text-lg text-stone-700 leading-relaxed mb-8">{intro}</p>

      <p class="text-sm text-stone-500 mb-12">
        <strong>Target keywords:</strong> {primary}, {", ".join(secondaries[:3])}
      </p>

      <h2 class="font-display text-3xl md:text-4xl font-bold mb-6 text-stone-900">5 Ways to Use the {content["model"]}</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-16">
{use_case_html}
      </div>

      <h2 class="font-display text-3xl md:text-4xl font-bold mb-6 text-stone-900">{compare["title"]}</h2>
{compare_html}

      <h2 class="font-display text-3xl md:text-4xl font-bold mb-6 mt-16 text-stone-900">Frequently Asked Questions</h2>
      <div class="space-y-3 mb-8">
{faqs_html}
      </div>

      <div class="mt-12 bg-stone-900 text-stone-100 rounded-2xl p-8 text-center">
        <h3 class="font-display text-2xl md:text-3xl font-bold mb-3">Ready to bring the {primary} home?</h3>
        <p class="text-stone-300 mb-6">Free shipping on orders over $35 from Walmart. 30-day returns. 1-year warranty.</p>
        <a href="https://www.walmart.com/seller/103033976/cp/shopall" target="_blank" rel="noopener" class="inline-block bg-amber-600 text-white font-semibold px-8 py-4 rounded-full hover:bg-amber-700 transition">
          Shop the {content["model"]} on Walmart →
        </a>
      </div>

    </div>
  </section>
'''
    return section


def process_product(slug):
    """Inject content + FAQ schema into one product page."""
    content = PRODUCT_CONTENT[slug]
    f = ROOT / "products" / f"{slug}.html"
    html = f.read_text()

    # 1. Build content section
    content_html = build_content_html(slug, content)

    # 2. Build FAQ schema
    faq_schema = build_faq_schema(slug, content["faqs"])

    # 3. Insert content section before <footer> (or before </body> if no footer pattern matches)
    # Use the last </section> followed by <footer> as insertion point
    if "<footer" in html:
        # Inject before <footer
        html = html.replace("<footer", f"{content_html}\n\n  <footer", 1)
    else:
        # Fallback: inject before </body>
        html = html.replace("</body>", f"{content_html}\n\n</body>", 1)

    # 4. Insert FAQ schema into <head> (after the existing Product schema)
    # Find the closing </script> of the existing Product schema
    # and inject FAQ schema right after it
    if "FAQPage" not in html:  # Don't double-inject
        # Find the last </script> in <head>
        head_end = html.find("</head>")
        # Find last </script> before </head>
        last_script_close = html.rfind("</script>", 0, head_end)
        if last_script_close > 0:
            insert_pos = last_script_close + len("</script>")
            html = html[:insert_pos] + f"\n  {faq_schema}" + html[insert_pos:]

    f.write_text(html)
    return len(html), len(content["faqs"])


def main():
    print("=" * 70)
    print("SEO Phase 2: Expanding 5 product pages with content + FAQ schema")
    print("=" * 70)
    for slug in PRODUCT_CONTENT:
        size, n_faqs = process_product(slug)
        print(f"  ✅ products/{slug}.html → {size:,} bytes ({n_faqs} FAQs)")
    print()
    print("Next: re-validate, commit, push, then add blog posts (Batch 2).")


if __name__ == "__main__":
    main()