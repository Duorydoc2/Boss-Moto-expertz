import os

# 1. Clean js/main.js: Remove all theme switcher code and force-clear localStorage
with open(r'js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Force clear local storage theme at top of js/main.js
clear_code = '''/* Clear any legacy theme override */
try {
  localStorage.removeItem('boss_moto_theme');
  document.body.className = document.body.className.replace(/theme-[^\s]+/g, '').trim();
} catch (e) {}

'''

# Remove theme switcher widget block from end of main.js if present
idx = js.find('/* ─── LIVE THEME SWITCHER WIDGET')
if idx != -1:
    js = js[:idx]

js = clear_code + js

with open(r'js\main.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Re-architect css/style.css for Black & Platinum Silver Theme + Rich Effects
with open(r'css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old theme overrides from end of style.css if present
idx_css = css.find('/* ====================================================\n   ULTRA-PREMIUM THEME OVERRIDES')
if idx_css == -1:
    idx_css = css.find('/* ====================================================\r\n   ULTRA-PREMIUM THEME OVERRIDES')
if idx_css == -1:
    idx_css = css.find('body.theme-gold')

if idx_css != -1:
    css = css[:idx_css]

# Replace :root definition in css/style.css with Sterling Black & Platinum Silver System
root_start = ':root {'
root_end = '}'
start_idx = css.find(root_start)
end_idx = css.find(root_end, start_idx)

black_silver_root = ''':root {
  /* ──────────────────────────────────────────────────────────
     STEALTH OBSIDIAN BLACK & STERLING PLATINUM SILVER THEME
     ────────────────────────────────────────────────────────── */
  --black: #050507;             /* Ultra Deep Obsidian Black */
  --black-soft: #0C0C10;        /* Secondary Dark Background */
  --black-card: #121218;        /* Dark Metallic Card Surface */
  --black-surface: #1B1B24;     /* Elevated Interactive Surface */
  
  --white: #FFFFFF;             /* Pure High-Contrast White */
  --white-dim: #F1F5F9;         /* Sterling Platinum White */
  --silver: #CBD5E1;            /* Liquid Metallic Silver */
  --silver-dim: #64748B;        /* Muted Silver Label / Subtitle */
  
  --accent: #FA7232;            /* Vivid Hyper-Orange Metallic Accent */
  --accent-dim: #FF8A50;        /* Warm Amber-Orange Glow */
  --accent-glow: rgba(250, 114, 50, 0.4);
  
  --silver-accent: #E2E8F0;     /* Sterling Silver Highlight */
  --silver-glow: rgba(226, 232, 240, 0.25);
  
  --teal-muted: #1E293B;
  --teal-deep: #0C0C10;
  --teal-dark: #050507;

  /* Legacy & HTML Aliases */
  --navy: #0C0C10;
  --deep-blue: #050507;
  --orange: #FA7232;
  --orange-glow: rgba(250, 114, 50, 0.4);
  --grad-orange: linear-gradient(135deg, #FA7232 0%, #D94600 100%);

  /* Glassmorphism & Metallic Borders */
  --glass-bg: rgba(18, 18, 24, 0.85);
  --glass-border: rgba(255, 255, 255, 0.16);
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
  --grad-hero: radial-gradient(circle at 75% 25%, rgba(250, 114, 50, 0.18) 0%, transparent 45%), radial-gradient(circle at 20% 80%, rgba(226, 232, 240, 0.08) 0%, transparent 40%), linear-gradient(135deg, #030304 0%, #0C0C10 100%);
  --grad-accent: linear-gradient(135deg, #FA7232 0%, #C43E00 100%);
  --grad-silver: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
  --grad-card: linear-gradient(145deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.01) 100%), linear-gradient(145deg, #121218 0%, #0C0C10 100%);
  --grad-section: linear-gradient(180deg, #050507 0%, #0C0C10 100%);
}'''

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + black_silver_root + css[end_idx + len(root_end):]

# Add Enhanced Glass Card Effects & Tab Hover Animations
extra_effects = '''

/* ─── ENHANCED BLACK & STERLING SILVER CARD & TAB EFFECTS ─── */
.glass-card, .service-card, .job-card, .stat-card, .vm-card, .bento-card {
  position: relative;
  background: var(--grad-card) !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
  overflow: hidden;
}

.glass-card::before, .service-card::before, .job-card::before, .bento-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.08), transparent);
  transition: left 0.7s ease;
  pointer-events: none;
}

.glass-card:hover::before, .service-card:hover::before, .job-card:hover::before, .bento-card:hover::before {
  left: 140%;
}

.glass-card:hover, .service-card:hover, .job-card:hover, .stat-card:hover, .vm-card:hover, .bento-card:hover {
  transform: translateY(-6px) scale(1.01) !important;
  border-color: rgba(255, 255, 255, 0.35) !important;
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.9), 0 0 25px rgba(255, 255, 255, 0.1) !important;
}

/* Enhanced Tab / Pill Buttons */
.pill-btn {
  background: rgba(255, 255, 255, 0.04) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  color: var(--silver) !important;
  font-weight: 600 !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4) !important;
}

.pill-btn:hover {
  background: rgba(255, 255, 255, 0.12) !important;
  color: #FFFFFF !important;
  border-color: rgba(255, 255, 255, 0.4) !important;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6), 0 0 15px rgba(255, 255, 255, 0.15) !important;
}

.pill-btn.active {
  background: linear-gradient(135deg, #FA7232 0%, #D94600 100%) !important;
  border-color: #FA7232 !important;
  color: #FFFFFF !important;
  box-shadow: 0 8px 24px rgba(250, 114, 50, 0.4) !important;
}
'''

css += extra_effects

with open(r'css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)
