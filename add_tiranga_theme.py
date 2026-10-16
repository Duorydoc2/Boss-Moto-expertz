import os

with open(r'css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update :root with Indian Tricolor Design Tokens
root_start = ':root {'
root_end = '}'
start_idx = css.find(root_start)
end_idx = css.find(root_end, start_idx)

tiranga_root = ''':root {
  /* ──────────────────────────────────────────────────────────
     STEALTH OBSIDIAN BLACK & STERLING PLATINUM CHROME DESIGN
     WITH SUBTLE INDIAN TRICOLOR (TIRANGA) ACCENTS 🇮🇳
     ────────────────────────────────────────────────────────── */
  --black: #050507;             /* Ultra Deep Obsidian Black */
  --black-soft: #0C0C10;        /* Secondary Dark Background */
  --black-card: #121218;        /* Dark Metallic Card Surface */
  --black-surface: #1B1B24;     /* Elevated Interactive Surface */
  
  --white: #FFFFFF;             /* Pure High-Contrast White */
  --white-dim: #F1F5F9;         /* Sterling Platinum White */
  --silver: #E2E8F0;            /* Liquid Metallic Platinum */
  --silver-dim: #94A3B8;        /* Muted Sterling Silver */
  
  --accent: #FFFFFF;            /* Pure Sterling Platinum White Accent */
  --accent-dim: #E2E8F0;        /* Soft Platinum Chrome Glow */
  --accent-glow: rgba(255, 255, 255, 0.35);
  
  --silver-accent: #FFFFFF;     /* Pure Platinum Silver Highlight */
  --silver-glow: rgba(255, 255, 255, 0.3);

  /* Indian Tricolor Tokens */
  --saffron: #FF9933;           /* India Saffron */
  --saffron-glow: rgba(255, 153, 51, 0.35);
  --india-white: #FFFFFF;
  --india-green: #138808;        /* India Emerald Green */
  --india-green-glow: rgba(19, 136, 8, 0.35);
  --chakra-blue: #002244;
  
  --grad-tiranga: linear-gradient(90deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
  --grad-tiranga-subtle: linear-gradient(90deg, rgba(255, 153, 51, 0.22) 0%, rgba(255, 255, 255, 0.12) 50%, rgba(19, 136, 8, 0.22) 100%);

  --teal-muted: #1E293B;
  --teal-deep: #0C0C10;
  --teal-dark: #050507;

  /* Legacy & HTML Aliases */
  --navy: #0C0C10;
  --deep-blue: #050507;
  --orange: #FF9933;
  --orange-glow: rgba(255, 153, 51, 0.35);
  --grad-orange: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%);

  /* Glassmorphism & Metallic Borders */
  --glass-bg: rgba(18, 18, 24, 0.88);
  --glass-border: rgba(255, 255, 255, 0.2);
  --glass-blur: blur(24px);

  /* Typography */
  --font-brand: 'Orbitron', sans-serif;
  --font-heading: 'Rajdhani', sans-serif;
  --font-body: 'Inter', sans-serif;

  /* Spacing */
  --section-py: 6rem;
  --container-max: 1280px;

  /* Transitions & Smooth Motion */
  --t-fast: 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --t-mid: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  --t-slow: 0.7s cubic-bezier(0.16, 1, 0.3, 1);

  /* Gradients */
  --grad-hero: radial-gradient(circle at 75% 25%, rgba(255, 153, 51, 0.12) 0%, transparent 45%), radial-gradient(circle at 25% 75%, rgba(19, 136, 8, 0.12) 0%, transparent 45%), linear-gradient(135deg, #030304 0%, #0C0C10 100%);
  --grad-accent: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%);
  --grad-silver: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
  --grad-card: linear-gradient(145deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.01) 100%), linear-gradient(145deg, #121218 0%, #0C0C10 100%);
  --grad-section: linear-gradient(180deg, #050507 0%, #0C0C10 100%);
}'''

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + tiranga_root + css[end_idx + len(root_end):]

# 2. Append Subtle Tiranga Navbar Stripe & Section Divider Styling
tiranga_css = '''

/* ─── SUBTLE INDIAN TRICOLOR (TIRANGA) DESIGN ELEMENTS 🇮🇳 ─── */
.navbar::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--grad-tiranga);
  z-index: 1002;
  box-shadow: 0 0 10px rgba(255, 153, 51, 0.4), 0 0 10px rgba(19, 136, 8, 0.4);
}

.section-divider {
  height: 1px !important;
  background: linear-gradient(90deg, transparent 0%, rgba(255, 153, 51, 0.45) 25%, rgba(255, 255, 255, 0.7) 50%, rgba(19, 136, 8, 0.45) 75%, transparent 100%) !important;
  margin: 0 auto !important;
  border: none !important;
}

.section-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 1.1rem;
  background: var(--grad-tiranga-subtle) !important;
  border: 1px solid rgba(255, 153, 51, 0.35) !important;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #FFFFFF !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
}

.btn-primary::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2.5px;
  background: var(--grad-tiranga);
  opacity: 0.85;
}

.btn-primary:hover {
  box-shadow: 0 10px 30px rgba(255, 153, 51, 0.22), 0 0 20px rgba(19, 136, 8, 0.22) !important;
}

.footer-bottom {
  position: relative;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-bottom::before {
  content: '';
  position: absolute;
  top: -1px;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 2px;
  background: var(--grad-tiranga);
}
'''

css += tiranga_css

with open(r'css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with subtle Tiranga elements.")
