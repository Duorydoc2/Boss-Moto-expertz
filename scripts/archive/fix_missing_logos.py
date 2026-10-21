import os
import glob
import shutil
import re

# Upload directory
uploads_dir = r'C:\Users\moham\.gemini\antigravity-ide\brain\20f2a4a0-62e6-442d-a13c-c93e82b1b4b2\.user_uploaded'

# Destination directory
brands_dir = r'c:\Users\moham\Boss\assets\brands'

# Get latest two pngs
files = glob.glob(os.path.join(uploads_dir, '*.png'))
files.sort(key=os.path.getmtime)

# Assuming the last 2 files uploaded are hero and kawasaki in order.
# The user uploaded Hero first, then Kawasaki.
# So files[-2] is Hero, files[-1] is Kawasaki.
hero_src = files[-2]
kawasaki_src = files[-1]

hero_dst = os.path.join(brands_dir, 'hero.png')
kawasaki_dst = os.path.join(brands_dir, 'kawasaki.png')

shutil.copy2(hero_src, hero_dst)
shutil.copy2(kawasaki_src, kawasaki_dst)
print(f"Copied {hero_src} to {hero_dst}")
print(f"Copied {kawasaki_src} to {kawasaki_dst}")

# Update brands.html
html_path = r'c:\Users\moham\Boss\brands.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .svg with .png for hero and kawasaki
content = content.replace('assets/brands/hero.svg', 'assets/brands/hero.png')
content = content.replace('assets/brands/kawasaki.svg', 'assets/brands/kawasaki.png')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated brands.html successfully.")
