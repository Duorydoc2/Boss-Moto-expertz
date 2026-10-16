import os
import glob

# 1. Update all HTML files with ?v=100 cache-buster query params
html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace style.css references
    import re
    content = re.sub(r'css/style\.css(\?v=[^"\'\s>]+)?', 'css/style.css?v=100', content)
    content = re.sub(r'js/main\.js(\?v=[^"\'\s>]+)?', 'js/main.js?v=100', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files with ?v=100 cache buster tags.")

# 2. Update js/main.js to forcefully purge theme switcher widget & clear cache
with open(r'js\main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Force clear local storage and purge theme switcher bar
purge_code = '''/* Force clear cache and legacy theme switcher */
(function() {
  try {
    localStorage.clear();
    sessionStorage.clear();
    if (document.body) {
      document.body.className = document.body.className.replace(/theme-[^\s]+/g, '').trim();
    }
    const oldBar = document.querySelector('.theme-switcher-bar');
    if (oldBar) oldBar.remove();
  } catch (e) {}
})();

'''

# Remove any remaining theme switcher widget block from main.js
switcher_idx = js.find('/* ─── LIVE THEME SWITCHER WIDGET')
if switcher_idx != -1:
    js = js[:switcher_idx]

# Check if purge_code already at top
if 'Force clear cache' not in js:
    js = purge_code + js

with open(r'js\main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated js/main.js cleanly.")
