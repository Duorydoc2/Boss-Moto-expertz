# Boss Moto Expertz – Web Platform Architecture & Developer Guide

Welcome to the **Boss Moto Expertz** official codebase. This document serves as the master technical handbook for developers, editors, and maintainers.

---

## 1. Project Overview

**Boss Moto Expertz** is a high-performance motorcycle and superbike performance studio based in Coimbatore, Tamil Nadu. The web application is engineered as a zero-dependency, ultra-fast, search-engine-optimized static platform with rich micro-interactions, responsive mobile drawers, real-time service searching, interactive cost estimation, and WCAG-compliant accessibility.

* **Workshop Address:** 42, Amarar Jeeva Main Road, Nalvar Layout, Coimbatore, Tamil Nadu 641006
* **Primary Telephone:** [+91 63 799 299 63](tel:+916379929963)
* **Production Deployment:** Static edge hosting on [Vercel](https://vercel.com/) via [`vercel.json`](file:///c:/Users/gurus/Boss-Moto-expertz/vercel.json)
* **Tech Stack:** Semantic HTML5, Vanilla CSS3 (Custom Properties & Design Tokens), Vanilla JavaScript (ES6+), Schema.org JSON-LD Microdata.

---

## 2. Directory Structure

```text
Boss-Moto-expertz/
├── assets/                       # Static media, images, and brand assets
│   ├── brands/                   # Manufacturer logos (Royal Enfield, KTM, Yamaha, etc.)
│   ├── gallery/                  # Showcase builds, shop photos, and staff portraits
│   ├── services/                 # Category visual backgrounds & illustrations
│   ├── logo.png                  # Master brand insignia
│   └── rx100.png                 # Featured restoration highlight graphic
│
├── css/
│   └── style.css                 # Master design system & component styles (37 sections)
│
├── js/
│   └── main.js                   # Client interactivity, search, 3D tilt, and estimators
│
├── scripts/                      # Project automation & tooling
│   ├── archive/                  # 50+ preserved migration and one-off maintenance scripts
│   └── README.md                 # Documentation of historical tooling
│
├── [Page Files]
│   ├── index.html                # Apex Studio Homepage & Quick Estimator
│   ├── about.html                # Company story, certifications, & workshop facility
│   ├── services.html             # Comprehensive 28-service directory with live search
│   ├── brands.html               # Multi-brand diagnostic & service portfolio
│   ├── gallery.html              # Custom builds showcase & lightbox modal
│   ├── booking.html              # Multi-step online appointment scheduling engine
│   ├── contact.html              # Location, interactive map, operating hours, & contact form
│   ├── careers.html              # Workshop technician job openings & application modal
│   └── investors.html            # Expansion roadmap & studio franchise telemetry
│
├── [Technical SEO & Discovery]
│   ├── robots.txt                # Crawler directives for Googlebot & search spiders
│   ├── sitemap.xml               # Canonical XML sitemap with daily/weekly changefreq
│   ├── vercel.json               # Edge security headers, caching, & clean URL routing
│   │
│   ├── SEO_AUDIT.md              # Complete technical SEO audit & health report
│   ├── SEO_CLIENT_ACTIONS.md     # Client action checklist (Google Business, DNS, GBP)
│   ├── SEO_IMPLEMENTATION_REPORT.md # On-page meta, schema, & landmark implementation details
│   ├── SEO_KEYWORD_MAP.md        # Keyword targets, monthly volume, & target URLs
│   ├── SEO_VALIDATION_CHECKLIST.md  # 15-point verification checklist for SEO compliance
│   ├── LOCAL_SEO_PLAN.md         # Hyper-local Kongu region & Coimbatore SEO blueprint
│   └── role_tabs_documentation.md # Technical documentation for Careers tab component
│
└── README.md                     # Master developer documentation (this file)
```

---

## 3. Page Catalog & Functional Breakdown

| Page File | Title | Primary Role & Components |
|---|---|---|
| [`index.html`](file:///c:/Users/gurus/Boss-Moto-expertz/index.html) | Home | Hero video/particle stage, 3D bike showcase, instant pricing calculator, telemetry cards, Bento feature grid, customer reviews. |
| [`about.html`](file:///c:/Users/gurus/Boss-Moto-expertz/about.html) | About Us | Heritage backstory, certified master technician profiles, precision workshop equipment specs, quality guarantees. |
| [`services.html`](file:///c:/Users/gurus/Boss-Moto-expertz/services.html) | Services | 28 distinct service cards categorized across 4 hubs, real-time live search engine with auto-suggest dropdown, native FAQ accordions. |
| [`brands.html`](file:///c:/Users/gurus/Boss-Moto-expertz/brands.html) | Brands We Service | Brand logos & capability matrix covering Royal Enfield, KTM, Yamaha, Kawasaki, BMW, Honda, Triumph, TVS, Bajaj, and vintage models. |
| [`gallery.html`](file:///c:/Users/gurus/Boss-Moto-expertz/gallery.html) | Showcase & Gallery | Masonry image gallery, category filter pills (Cafe Racer, Bobber, Restoration, Paintwork), full-screen lightbox viewer. |
| [`booking.html`](file:///c:/Users/gurus/Boss-Moto-expertz/booking.html) | Book Service | Multi-step booking wizard, dynamic calendar slot picker, URL query pre-fill (`?brand=tvs&model=rr310`), WhatsApp reservation dispatcher. |
| [`contact.html`](file:///c:/Users/gurus/Boss-Moto-expertz/contact.html) | Contact & Location | Google Maps embed, operating schedule (Mon-Sat 9-7, Sun by appt), emergency roadside assistance callouts, contact form. |
| [`careers.html`](file:///c:/Users/gurus/Boss-Moto-expertz/careers.html) | Careers | Job postings (Engine Builder, Superbike Tech, ECU Tuner, Painter), role description tab switcher, application intake modal. |
| [`investors.html`](file:///c:/Users/gurus/Boss-Moto-expertz/investors.html) | Investors & Franchise | Studio expansion projections, franchise investment calculator, investor prospectus inquiry form. |

---

## 4. Design System & CSS Architecture ([`css/style.css`](file:///c:/Users/gurus/Boss-Moto-expertz/css/style.css))

The stylesheet is structured into **37 dedicated sections** governed by CSS Custom Properties (`:root` tokens).

### 4.1. Core Color Tokens
```css
:root {
  /* Stealth Obsidian Black & Sterling Platinum Chrome */
  --black: #050507;             /* Ultra Deep Obsidian Black Background */
  --black-soft: #0C0C10;        /* Secondary Dark Surface */
  --black-card: #121218;        /* Dark Metallic Card Background */
  --black-surface: #1B1B24;     /* Elevated Interactive Hover Surface */

  --white: #FFFFFF;             /* Pure High-Contrast White */
  --white-dim: #F1F5F9;         /* Sterling Platinum White */
  --silver: #E2E8F0;            /* Liquid Metallic Platinum */
  --silver-dim: #94A3B8;        /* Muted Sterling Silver */

  /* Indian Tricolor (Tiranga) Accents 🇮🇳 */
  --saffron: #FF9933;           /* India Saffron Highlight */
  --saffron-glow: rgba(255, 153, 51, 0.35);
  --india-white: #FFFFFF;
  --india-green: #138808;        /* India Emerald Green */
  --india-green-glow: rgba(19, 136, 8, 0.35);
  --chakra-blue: #002244;
}
```

### 4.2. Typography
* **Branding / Numbers:** `'Orbitron', sans-serif` (`--font-brand`)
* **Headings:** `'Rajdhani', sans-serif` (`--font-heading`)
* **Body / UI Copy:** `'Inter', sans-serif` (`--font-body`)

### 4.3. Responsive Breakpoints
* **Desktop / Wide:** `1280px` max container width (`--container-max`)
* **Tablet Landscape:** `@media (max-width: 1024px)` – 2-column bento collapse
* **Tablet Portrait:** `@media (max-width: 860px)` – Single column form & telemetry stack
* **Mobile Phone:** `@media (max-width: 768px)` – Full mobile navigation drawer activation
* **Small Mobile:** `@media (max-width: 480px)` – Condensed buttons, stacked quick pills

---

## 5. JavaScript Architecture ([`js/main.js`](file:///c:/Users/gurus/Boss-Moto-expertz/js/main.js))

The core JavaScript runs natively in the browser without bundlers or compilation steps. All modules are enclosed in clean Immediately Invoked Function Expressions (IIFEs) to avoid global scope pollution:

1. **`Navbar Scroll`**: Monitors `window.scrollY > 50` to apply glassmorphic `.scrolled` state.
2. **`Mobile Menu`**: Toggles `.open` state on the hamburger button `#navToggle` and `#mobileMenu`, preventing background scroll when open.
3. **`Active Link Highlighter`**: Inspects `window.location.pathname` and adds `.active` to the matching desktop & mobile nav items.
4. **`Hero Parallax`**: Translates background canvas at `scrolled * 0.3px` for smooth depth.
5. **`Scroll Reveal`**: Uses `IntersectionObserver` (threshold `0.12`) to trigger smooth fade/slide-in on `.reveal` elements.
6. **`Counter Animation`**: Observes elements with `data-count` and animates numeric increments over 60 frames.
7. **`Gallery Filter`**: Filters `.masonry-item` elements by matching `data-category` attribute.
8. **`Lightbox Viewer`**: Fullscreen modal for viewing high-res gallery images with `Escape` key and backdrop click handlers.
9. **`Smooth 3D Hover Tilt`**: Real-time cursor tracking on `.why-card`, `.service-card`, and `.testimonial-card` calculating 3D perspective rotation (`perspective(600px)`).
10. **`3D Hero Slider`**: Multi-slide carousel with auto-rotation (4.5s), manual indicator navigation, and mouse-follow 3D stage translation.
11. **`Quick Estimator`**: Dynamic pricing model calculating estimated bill and service turnaround based on bike displacement (70cc to 1300cc+) and selected service package.
12. **`Live Service Search Engine`**: Real-time keystroke filter with autocomplete dropdown popup, keyword pill triggers, scroll-to-card, and temporary `.highlight-card` pulse effect.

---

## 6. Technical SEO & Discovery Suite

The repository is built following technical SEO and Local SEO best practices:

* **Structured Data:** Every page includes valid `MotorcycleRepairShop` Schema.org JSON-LD structured data with precise geo-coordinates (`11.0268, 76.9634`), operating hours, accepted currencies, and payment methods.
* **FAQ Schema:** [`services.html`](file:///c:/Users/gurus/Boss-Moto-expertz/services.html) includes full `FAQPage` schema matching on-page accordion questions.
* **Canonical URLs:** Strict self-referential canonical URLs (`https://bossmotoexpertz.com/...`) on all HTML pages to avoid duplicate content penalties.
* **OpenGraph & Twitter:** Complete social sharing tags with high-resolution image previews, titles, descriptions, and site names.
* **WCAG 2.1 Accessibility:** Includes hidden skip-to-content links (`<a href="#main-content" class="skip-link">`), ARIA landmark roles (`role="navigation"`, `role="main"`), and accessible labels on all toggles and buttons.

### Detailed SEO Reference Reports
* [`LOCAL_SEO_PLAN.md`](file:///c:/Users/gurus/Boss-Moto-expertz/LOCAL_SEO_PLAN.md) – Local search ranking strategy.
* [`SEO_KEYWORD_MAP.md`](file:///c:/Users/gurus/Boss-Moto-expertz/SEO_KEYWORD_MAP.md) – Keyword mapping by URL and intent.
* [`SEO_AUDIT.md`](file:///c:/Users/gurus/Boss-Moto-expertz/SEO_AUDIT.md) – Baseline technical SEO audit.
* [`SEO_CLIENT_ACTIONS.md`](file:///c:/Users/gurus/Boss-Moto-expertz/SEO_CLIENT_ACTIONS.md) – Google Business Profile and local citation guide.
* [`SEO_VALIDATION_CHECKLIST.md`](file:///c:/Users/gurus/Boss-Moto-expertz/SEO_VALIDATION_CHECKLIST.md) – Pre-launch SEO verification checklist.

---

## 7. How to Preview & Run Locally

Because the project is built with vanilla web technologies, you do **not** need `npm install` or complex build configurations.

### Option A: VS Code Live Server (Recommended)
1. Open the project folder in VS Code.
2. Right-click [`index.html`](file:///c:/Users/gurus/Boss-Moto-expertz/index.html) and select **"Open with Live Server"**.

### Option B: Python Local Server
Run in PowerShell or Command Prompt:
```powershell
python -m http.server 3000
```
Then navigate to `http://localhost:3000` in your browser.

### Option C: Node.js (via `serve` or `http-server`)
```powershell
npx serve .
```

---

## 8. Deployment & Hosting (Vercel)

The website is configured for immediate deployment on **Vercel** via [`vercel.json`](file:///c:/Users/gurus/Boss-Moto-expertz/vercel.json):
* **`cleanUrls: true`**: Automatically routes `/about` to `/about.html`, `/services` to `/services.html`, etc.
* **Security Headers**: Injects `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`, and restrictive `Permissions-Policy`.
* **Asset Caching**: Sets `Cache-Control: public, max-age=31536000, immutable` for all files in `/assets/` for maximum performance scores.

---

## 9. Developer Guidelines & Conventions

When modifying or expanding the codebase:
1. **Maintain Consistent Indentation:** Use standard 2-space indentation across all HTML, CSS, and JS files.
2. **Preserve Section Dividers:** Keep the standardized section comments (`<!-- ═══════════════════ SECTION NAME ═══════════════════ -->`) so other editors can locate components quickly.
3. **Use CSS Custom Properties:** Always refer to existing color variables (`var(--black)`, `var(--silver)`, `var(--orange)`, etc.) instead of hardcoded hex codes.
4. **Static Assets:** Store all new photos, graphics, or logos under `assets/` in their respective subdirectories (`assets/gallery/`, `assets/services/`, etc.).
5. **No Visual Breaking Changes:** Always verify changes in both desktop and mobile viewports before committing to `main`.
