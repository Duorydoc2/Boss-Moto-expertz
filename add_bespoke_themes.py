import os

new_themes_css = '''

/* ============================================================
   NEW BESPOKE LUXURY THEMES
   ============================================================ */

/* Theme 1: BRABUS Hyperion Void (Black, Platinum & Electric Violet) */
body.theme-hyperion {
  --black: #060709;
  --black-soft: #0D0F17;
  --black-card: #131724;
  --black-surface: #1C2236;
  --white: #F8FAFC;
  --white-dim: #E2E8F0;
  --silver: #CBD5E1;
  --silver-dim: #64748B;
  --accent: #8B5CF6;
  --accent-dim: #A855F7;
  --accent-glow: rgba(139, 92, 246, 0.4);
  --orange: #8B5CF6;
  --orange-glow: rgba(139, 92, 246, 0.4);
  --grad-orange: linear-gradient(135deg, #8B5CF6 0%, #D946EF 100%);
  --navy: #0D0F17;
  --deep-blue: #060709;
  --glass-bg: rgba(19, 23, 36, 0.9);
  --glass-border: rgba(139, 92, 246, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(139, 92, 246, 0.25) 0%, transparent 50%), linear-gradient(135deg, #060709 0%, #131724 100%);
  --grad-accent: linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%);
  --grad-card: linear-gradient(145deg, #131724 0%, #0D0F17 100%);
  --grad-section: linear-gradient(180deg, #060709 0%, #0D0F17 100%);
}

/* Theme 2: Mansory Stealth Emerald */
body.theme-emerald {
  --black: #040806;
  --black-soft: #09140F;
  --black-card: #0F2018;
  --black-surface: #183025;
  --white: #F0FDF4;
  --white-dim: #DCFCE7;
  --silver: #86EFAC;
  --silver-dim: #34D399;
  --accent: #10B981;
  --accent-dim: #34D399;
  --accent-glow: rgba(16, 185, 129, 0.4);
  --orange: #10B981;
  --orange-glow: rgba(16, 185, 129, 0.4);
  --grad-orange: linear-gradient(135deg, #10B981 0%, #059669 100%);
  --navy: #09140F;
  --deep-blue: #040806;
  --glass-bg: rgba(15, 32, 24, 0.9);
  --glass-border: rgba(16, 185, 129, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.25) 0%, transparent 50%), linear-gradient(135deg, #040806 0%, #0F2018 100%);
  --grad-accent: linear-gradient(135deg, #10B981 0%, #047857 100%);
  --grad-card: linear-gradient(145deg, #0F2018 0%, #09140F 100%);
  --grad-section: linear-gradient(180deg, #040806 0%, #09140F 100%);
}

/* Theme 3: Akrapovič Titanium Quartz */
body.theme-titanium {
  --black: #090C15;
  --black-soft: #111728;
  --black-card: #18223B;
  --black-surface: #222F50;
  --white: #F8FAFC;
  --white-dim: #E2E8F0;
  --silver: #94A3B8;
  --silver-dim: #475569;
  --accent: #F97316;
  --accent-dim: #FB923C;
  --accent-glow: rgba(249, 115, 22, 0.4);
  --orange: #F97316;
  --orange-glow: rgba(249, 115, 22, 0.4);
  --grad-orange: linear-gradient(135deg, #F97316 0%, #0284C7 100%);
  --navy: #111728;
  --deep-blue: #090C15;
  --glass-bg: rgba(24, 34, 59, 0.9);
  --glass-border: rgba(249, 115, 22, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(249, 115, 22, 0.25) 0%, transparent 50%), linear-gradient(135deg, #090C15 0%, #18223B 100%);
  --grad-accent: linear-gradient(135deg, #F97316 0%, #C2410C 100%);
  --grad-card: linear-gradient(145deg, #18223B 0%, #111728 100%);
  --grad-section: linear-gradient(180deg, #090C15 0%, #111728 100%);
}

/* Theme 4: Monaco 24K Gold & Carbon */
body.theme-monaco {
  --black: #0A0A0C;
  --black-soft: #141418;
  --black-card: #1D1D24;
  --black-surface: #272730;
  --white: #FFFBEB;
  --white-dim: #FDE68A;
  --silver: #E4E4E7;
  --silver-dim: #71717A;
  --accent: #D97706;
  --accent-dim: #F59E0B;
  --accent-glow: rgba(217, 119, 6, 0.4);
  --orange: #D97706;
  --orange-glow: rgba(217, 119, 6, 0.4);
  --grad-orange: linear-gradient(135deg, #D97706 0%, #B45309 100%);
  --navy: #141418;
  --deep-blue: #0A0A0C;
  --glass-bg: rgba(29, 29, 36, 0.9);
  --glass-border: rgba(217, 119, 6, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(217, 119, 6, 0.25) 0%, transparent 50%), linear-gradient(135deg, #0A0A0C 0%, #1D1D24 100%);
  --grad-accent: linear-gradient(135deg, #D97706 0%, #78350F 100%);
  --grad-card: linear-gradient(145deg, #1D1D24 0%, #141418 100%);
  --grad-section: linear-gradient(180deg, #0A0A0C 0%, #141418 100%);
}
'''

with open(r'css\style.css', 'a', encoding='utf-8') as f:
    f.write(new_themes_css)

# Update js/main.js to include these 4 new bespoke options
with open(r'js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_themes_list = '''  const themes = [
    { id: 'default', label: 'Sunset Teal', dot: '#FA7232' },
    { id: 'gold', label: 'Liquid Gold', dot: '#F59E0B' },
    { id: 'crimson', label: 'Racing Crimson', dot: '#EF4444' },
    { id: 'cyan', label: 'Cyber Cyan', dot: '#06B6D4' },
    { id: 'copper', label: 'Apex Copper', dot: '#E57C23' }
  ];'''

new_themes_list = '''  const themes = [
    { id: 'hyperion', label: '🔮 BRABUS Hyperion', dot: '#8B5CF6' },
    { id: 'emerald', label: '🟢 Mansory Emerald', dot: '#10B981' },
    { id: 'titanium', label: '🔥 Akrapovič Titanium', dot: '#F97316' },
    { id: 'monaco', label: '👑 Monaco 24K Gold', dot: '#D97706' },
    { id: 'default', label: 'Original Teal', dot: '#FA7232' }
  ];'''

old_remove = "document.body.classList.remove('theme-gold', 'theme-crimson', 'theme-cyan', 'theme-copper');"
new_remove = "document.body.classList.remove('theme-gold', 'theme-crimson', 'theme-cyan', 'theme-copper', 'theme-hyperion', 'theme-emerald', 'theme-titanium', 'theme-monaco');"

if old_themes_list in js:
    js = js.replace(old_themes_list, new_themes_list)

if old_remove in js:
    js = js.replace(old_remove, new_remove)

with open(r'js\main.js', 'w', encoding='utf-8') as f:
    f.write(js)
