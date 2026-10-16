with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_code = '''  // Inject floating switcher widget
  document.addEventListener('DOMContentLoaded', () => {
    const bar = document.createElement('div');
    bar.className = 'theme-switcher-bar';
    bar.innerHTML = '<span class="theme-switcher-title">🎨 Preview Theme:</span>';

    themes.forEach(t => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'theme-opt-btn' + ((savedTheme === t.id) ? ' active' : '');
      btn.innerHTML = `<span class="theme-dot" style="background:${t.dot};"></span> ${t.label}`;
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
  });'''

new_code = '''  // Inject floating switcher widget immediately
  function initThemeSwitcher() {
    if (document.querySelector('.theme-switcher-bar')) return;
    const bar = document.createElement('div');
    bar.className = 'theme-switcher-bar';
    bar.innerHTML = '<span class="theme-switcher-title">🎨 Preview Theme:</span>';

    themes.forEach(t => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'theme-opt-btn' + ((savedTheme === t.id) ? ' active' : '');
      btn.innerHTML = `<span class="theme-dot" style="background:${t.dot};"></span> ${t.label}`;
      btn.onclick = () => {
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeSwitcher);
  } else {
    initThemeSwitcher();
  }'''

if old_code in js:
    js = js.replace(old_code, new_code)
else:
    # fallback replace
    print("Old code block not matched directly, running fallback replacement")
    js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "function initThemeSwitcher() {")
    js = js.replace("document.body.appendChild(bar);\n  });", "document.body.appendChild(bar);\n  }\n  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', initThemeSwitcher); } else { initThemeSwitcher(); }")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
