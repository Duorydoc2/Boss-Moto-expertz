import os

# 1. Append theme classes to css/style.css
theme_css = '''

/* ============================================================
   ULTRA-PREMIUM THEME OVERRIDES & SWITCHER STYLES
   ============================================================ */

/* Theme 1: Cyberpunk Carbon & Liquid Gold */
body.theme-gold {
  --black: #0B0E14;
  --black-soft: #121722;
  --black-card: #182030;
  --black-surface: #222C40;
  --white: #F8FAFC;
  --white-dim: #E2E8F0;
  --silver: #CBD5E1;
  --silver-dim: #64748B;
  --accent: #F59E0B;
  --accent-dim: #FBBF24;
  --accent-glow: rgba(245, 158, 11, 0.35);
  --orange: #F59E0B;
  --orange-glow: rgba(245, 158, 11, 0.35);
  --grad-orange: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
  --navy: #121722;
  --deep-blue: #0B0E14;
  --glass-bg: rgba(24, 32, 48, 0.88);
  --glass-border: rgba(245, 158, 11, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(245, 158, 11, 0.22) 0%, transparent 45%), linear-gradient(135deg, #0B0E14 0%, #182030 100%);
  --grad-accent: linear-gradient(135deg, #F59E0B 0%, #B45309 100%);
  --grad-card: linear-gradient(145deg, #182030 0%, #121722 100%);
  --grad-section: linear-gradient(180deg, #0B0E14 0%, #121722 100%);
}

/* Theme 2: Titanium Stealth & Racing Crimson */
body.theme-crimson {
  --black: #0F1015;
  --black-soft: #181A22;
  --black-card: #202430;
  --black-surface: #2A2F40;
  --white: #FAFAFA;
  --white-dim: #E4E4E7;
  --silver: #A1A1AA;
  --silver-dim: #52525B;
  --accent: #EF4444;
  --accent-dim: #F87171;
  --accent-glow: rgba(239, 68, 68, 0.35);
  --orange: #EF4444;
  --orange-glow: rgba(239, 68, 68, 0.35);
  --grad-orange: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
  --navy: #181A22;
  --deep-blue: #0F1015;
  --glass-bg: rgba(32, 36, 48, 0.88);
  --glass-border: rgba(239, 68, 68, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(239, 68, 68, 0.22) 0%, transparent 45%), linear-gradient(135deg, #0F1015 0%, #202430 100%);
  --grad-accent: linear-gradient(135deg, #EF4444 0%, #991B1B 100%);
  --grad-card: linear-gradient(145deg, #202430 0%, #181A22 100%);
  --grad-section: linear-gradient(180deg, #0F1015 0%, #181A22 100%);
}

/* Theme 3: Midnight Obsidian & Cyber Cyan */
body.theme-cyan {
  --black: #040810;
  --black-soft: #091222;
  --black-card: #0E1B33;
  --black-surface: #152749;
  --white: #F0FDF4;
  --white-dim: #CFFAFE;
  --silver: #7DD3FC;
  --silver-dim: #38BDF8;
  --accent: #06B6D4;
  --accent-dim: #22D3EE;
  --accent-glow: rgba(6, 182, 212, 0.35);
  --orange: #06B6D4;
  --orange-glow: rgba(6, 182, 212, 0.35);
  --grad-orange: linear-gradient(135deg, #06B6D4 0%, #10B981 100%);
  --navy: #091222;
  --deep-blue: #040810;
  --glass-bg: rgba(14, 27, 51, 0.88);
  --glass-border: rgba(6, 182, 212, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(6, 182, 212, 0.25) 0%, transparent 45%), linear-gradient(135deg, #040810 0%, #0E1B33 100%);
  --grad-accent: linear-gradient(135deg, #06B6D4 0%, #059669 100%);
  --grad-card: linear-gradient(145deg, #0E1B33 0%, #091222 100%);
  --grad-section: linear-gradient(180deg, #040810 0%, #091222 100%);
}

/* Theme 4: Satin Onyx & Apex Copper */
body.theme-copper {
  --black: #0E0E10;
  --black-soft: #16161A;
  --black-card: #1E1E24;
  --black-surface: #2A2A33;
  --white: #FFFBEB;
  --white-dim: #FDE68A;
  --silver: #D4D4D8;
  --silver-dim: #71717A;
  --accent: #E57C23;
  --accent-dim: #F89B29;
  --accent-glow: rgba(229, 124, 35, 0.35);
  --orange: #E57C23;
  --orange-glow: rgba(229, 124, 35, 0.35);
  --grad-orange: linear-gradient(135deg, #E57C23 0%, #C2410C 100%);
  --navy: #16161A;
  --deep-blue: #0E0E10;
  --glass-bg: rgba(30, 30, 36, 0.88);
  --glass-border: rgba(229, 124, 35, 0.35);
  --grad-hero: radial-gradient(circle at 80% 20%, rgba(229, 124, 35, 0.22) 0%, transparent 45%), linear-gradient(135deg, #0E0E10 0%, #1E1E24 100%);
  --grad-accent: linear-gradient(135deg, #E57C23 0%, #9A3412 100%);
  --grad-card: linear-gradient(145deg, #1E1E24 0%, #16161A 100%);
  --grad-section: linear-gradient(180deg, #0E0E10 0%, #16161A 100%);
}

/* Theme Switcher Widget Styling */
.theme-switcher-bar {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 99999;
  background: rgba(10, 15, 25, 0.92);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 50px;
  padding: 8px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 0, 0, 0.4);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.theme-switcher-title {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #F8FAFC;
  display: flex;
  align-items: center;
  gap: 6px;
  padding-right: 6px;
  border-right: 1px solid rgba(255, 255, 255, 0.15);
}

.theme-opt-btn {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 30px;
  padding: 6px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #CBD5E1;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.25s ease;
}

.theme-opt-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #FFFFFF;
  transform: translateY(-2px);
}

.theme-opt-btn.active {
  background: rgba(255, 255, 255, 0.2);
  border-color: #FFFFFF;
  color: #FFFFFF;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.theme-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
  border: 1px solid rgba(255,255,255,0.4);
}

@media (max-width: 768px) {
  .theme-switcher-bar {
    bottom: 12px;
    padding: 6px 10px;
    gap: 6px;
    max-width: 95vw;
    overflow-x: auto;
  }
  .theme-switcher-title {
    display: none;
  }
  .theme-opt-btn {
    padding: 4px 10px;
    font-size: 0.75rem;
  }
}
'''

with open(r'css\style.css', 'a', encoding='utf-8') as f:
    f.write(theme_css)

# 2. Append Theme Switcher Script to js/main.js
switcher_js = '''

/* ─── LIVE THEME SWITCHER WIDGET ──────────────────────────── */
(function () {
  const themes = [
    { id: 'default', label: 'Sunset Teal', dot: '#FA7232' },
    { id: 'gold', label: 'Liquid Gold', dot: '#F59E0B' },
    { id: 'crimson', label: 'Racing Crimson', dot: '#EF4444' },
    { id: 'cyan', label: 'Cyber Cyan', dot: '#06B6D4' },
    { id: 'copper', label: 'Apex Copper', dot: '#E57C23' }
  ];

  // Load saved theme
  const savedTheme = localStorage.getItem('boss_moto_theme') || 'default';
  if (savedTheme !== 'default') {
    document.body.classList.add('theme-' + savedTheme);
  }

  // Inject floating switcher widget
  document.addEventListener('DOMContentLoaded', () => {
    const bar = document.createElement('div');
    bar.className = 'theme-switcher-bar';
    bar.innerHTML = '<span class="theme-switcher-title">🎨 Preview Theme:</span>';

    themes.forEach(t => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'theme-opt-btn' + ((savedTheme === t.id) ? ' active' : '');
      btn.innerHTML = <span class="theme-dot" style="background:;"></span> ;
      btn.onclick = () => {
        // Remove all theme classes
        document.body.classList.remove('theme-gold', 'theme-crimson', 'theme-cyan', 'theme-copper');
        if (t.id !== 'default') {
          document.body.classList.add('theme-' + t.id);
        }
        localStorage.setItem('boss_moto_theme', t.id);

        document.querySelectorAll('.theme-opt-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      };
      bar.appendChild(btn);
    });

    document.body.appendChild(bar);
  });
})();
'''

with open(r'js\main.js', 'a', encoding='utf-8') as f:
    f.write(switcher_js)
