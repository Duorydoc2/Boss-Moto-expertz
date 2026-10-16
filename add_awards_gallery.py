import os
import glob
import shutil
import re

# Correct path for current session uploads
uploads_dir = r'C:\Users\moham\.gemini\antigravity-ide\brain\20f2a4a0-62e6-442d-a13c-c93e82b1b4b2\.user_uploaded'
files = glob.glob(os.path.join(uploads_dir, '*.png'))
files.sort(key=os.path.getmtime)

# We want the 4 pngs
recent_photos = files[-4:]

gallery_dir = r'c:\Users\moham\Boss\assets\gallery'
os.makedirs(gallery_dir, exist_ok=True)

new_images = []
for i, f in enumerate(recent_photos):
    filename = f'award_img_{i+1}.png'
    dst = os.path.join(gallery_dir, filename)
    shutil.copy(f, dst)
    new_images.append(f'assets/gallery/{filename}')
    print(f"Copied {f} to {dst}")

with open(r'c:\Users\moham\Boss\gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add 'Awards' filter button if not exists
filter_bar_end = content.find('</div>', content.find('<div class="gallery-filter-bar"'))
if filter_bar_end != -1 and 'data-filter="awards"' not in content:
    awards_btn = '        <button class="filter-btn" data-filter="awards" id="filterAwards">🏆 Awards</button>\n'
    content = content[:filter_bar_end] + awards_btn + content[filter_bar_end:]

# 2. Add the 4 new masonry items at the top of the grid
grid_start = content.find('<div class="masonry-grid" id="masonryGrid" aria-label="Gallery images">')
if grid_start != -1:
    insert_pos = content.find('>', grid_start) + 1
    
    items_html = '\n'
    for i, img in enumerate(new_images):
        delay = '' if i == 0 else f' reveal-delay-{i}'
        items_html += f'''
        <div class="masonry-item reveal{delay}" data-category="awards" tabindex="0" role="button" aria-label="View: Boss Moto Award {i+1}">
          <img src="{img}?v=1" alt="Boss Moto Award {i+1}" loading="lazy" />
          <div class="zoom-icon" aria-hidden="true">↗</div>
          <div class="masonry-overlay">
            <div class="masonry-info">
              <span class="tag">Awards & Achievements</span>
              <h4>Boss Moto History</h4>
              <p>Recognized for excellence.</p>
            </div>
          </div>
        </div>
'''
    content = content[:insert_pos] + items_html + content[insert_pos:]

# 3. Update the showing count script to include 'awards' properly (it already handles 'all' dynamically but let's make sure)
# The JS in the file does: const match = cat === 'all' || item.dataset.category === cat; visible++;
# So we just write the file back.

with open(r'c:\Users\moham\Boss\gallery.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery successfully updated with your attached photos!")
