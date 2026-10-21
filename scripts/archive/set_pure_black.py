import os

with open(r'css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace :root definition in css/style.css
root_start = ':root {'
root_end = '}'
start_idx = css.find(root_start)
end_idx = css.find(root_end, start_idx)

new_root = ''':root {
  /* ── Stealth Pure Black & Monochromatic Platinum Theme ── */
  --black: #000000;             /* Pure Pitch Black */
  --black-soft: #08080A;        /* Deep Charcoal Secondary */
  --black-card: #111115;        /* Dark Glass Card */
  --black-surface: #1A1A22;     /* Elevated Dark Surface */
  
  --white: #FFFFFF;             /* Crisp Pure White Text */
  --white-dim: #E5E5E5;         /* Soft Off-White */
  --silver: #A3A3A3;            /* Neutral Muted Silver */
  --silver-dim: #404040;        /* Subdued Borders */
  
  --accent: #FA7232;            /* Vibrant Electric Orange Accent */
  --accent-dim: #FF8A50;        /* Soft Amber Orange Glow */
  --accent-glow: rgba(250, 114, 50, 0.35);
  
  --teal-muted: #262626;
  --teal-deep: #08080A;
  --teal-dark: #000000;

  /* Legacy & HTML aliases */
  --navy: #08080A;
  --deep-blue: #000000;
  --orange: #FA7232;
  --orange-glow: rgba(250, 114, 50, 0.35);
  --grad-orange: linear-gradient(135deg, #FA7232 0%, #E05314 100%);

  /* Glass Effects */
  --glass-bg: rgba(17, 17, 21, 0.88);
  --glass-border: rgba(255, 255, 255, 0.12);
  --glass-blur: blur(20px);

  /* Typography */
  --font-brand: 'Orbitron', sans-serif;
  --font-heading: 'Rajdhani', sans-serif;
  --font-body: 'Inter', sans-serif;

  /* Spacing */
  --section-py: 6rem;
  --container-max: 1280px;

  /* Transitions */
  --t-fast: 0.2s ease;
  --t-mid: 0.4s ease;
  --t-slow: 0.7s cubic-bezier(0.22, 1, 0.36, 1);

  /* Atmospheric Gradients */
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(250, 114, 50, 0.16) 0%, transparent 50%), linear-gradient(135deg, #000000 0%, #0B0B0E 100%);
  --grad-accent: linear-gradient(135deg, #FA7232 0%, #C4410A 100%);
  --grad-card: linear-gradient(145deg, #111115 0%, #08080A 100%);
  --grad-section: linear-gradient(180deg, #000000 0%, #08080A 100%);
}'''

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + new_root + css[end_idx + len(root_end):]

with open(r'css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update js/main.js to clear any old localStorage theme override
with open(r'js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Clear saved theme in js/main.js
js = js.replace("localStorage.getItem('boss_moto_theme')", "null")

with open(r'js\main.js', 'w', encoding='utf-8') as f:
    f.write(js)
