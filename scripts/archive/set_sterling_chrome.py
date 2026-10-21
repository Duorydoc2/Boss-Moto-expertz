import os

with open(r'css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace :root in css/style.css with Pure Sterling Platinum & Liquid Chrome System
root_start = ':root {'
root_end = '}'
start_idx = css.find(root_start)
end_idx = css.find(root_end, start_idx)

sterling_chrome_root = ''':root {
  /* ──────────────────────────────────────────────────────────
     STEALTH OBSIDIAN BLACK & STERLING PLATINUM CHROME DESIGN
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
  
  --teal-muted: #1E293B;
  --teal-deep: #0C0C10;
  --teal-dark: #050507;

  /* Legacy & HTML Aliases */
  --navy: #0C0C10;
  --deep-blue: #050507;
  --orange: #FFFFFF;
  --orange-glow: rgba(255, 255, 255, 0.35);
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
  --grad-hero: radial-gradient(circle at 75% 25%, rgba(255, 255, 255, 0.15) 0%, transparent 45%), radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.05) 0%, transparent 40%), linear-gradient(135deg, #030304 0%, #0C0C10 100%);
  --grad-accent: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%);
  --grad-silver: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
  --grad-card: linear-gradient(145deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.01) 100%), linear-gradient(145deg, #121218 0%, #0C0C10 100%);
  --grad-section: linear-gradient(180deg, #050507 0%, #0C0C10 100%);
}'''

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + sterling_chrome_root + css[end_idx + len(root_end):]

# Update primary and active buttons for high contrast sterling platinum black style
old_btn_primary = '''.btn-primary {
  background: var(--accent);
  color: #FFFFFF;
  border: 1.5px solid var(--accent);
}

.btn-primary:hover {
  background: var(--accent-dim);
  border-color: var(--accent-dim);
  color: #FFFFFF;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--accent-glow);
}'''

new_btn_primary = '''.btn-primary {
  background: linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 100%);
  color: #050507;
  border: 1.5px solid #FFFFFF;
  font-weight: 800;
  box-shadow: 0 4px 20px rgba(255, 255, 255, 0.25);
}

.btn-primary:hover {
  background: #FFFFFF;
  border-color: #FFFFFF;
  color: #000000;
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(255, 255, 255, 0.45);
}'''

if old_btn_primary in css:
    css = css.replace(old_btn_primary, new_btn_primary)

# Update active pill buttons
old_pill_active = '''.pill-btn.active {
  background: linear-gradient(135deg, #FA7232 0%, #D94600 100%) !important;
  border-color: #FA7232 !important;
  color: #FFFFFF !important;
  box-shadow: 0 8px 24px rgba(250, 114, 50, 0.4) !important;
}'''

new_pill_active = '''.pill-btn.active {
  background: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%) !important;
  border-color: #FFFFFF !important;
  color: #050507 !important;
  font-weight: 700 !important;
  box-shadow: 0 8px 24px rgba(255, 255, 255, 0.35) !important;
}'''

if old_pill_active in css:
    css = css.replace(old_pill_active, new_pill_active)

with open(r'css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)
