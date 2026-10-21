import os, glob, shutil, re

uploads = r'C:\Users\moham\.gemini\antigravity-ide\brain\521f531e-9d43-447b-8c37-ec4c9e6f60f3\.user_uploaded\*.*'
files = glob.glob(uploads)
files.sort(key=os.path.getmtime, reverse=True)

# The latest 4 files are the photos
recent_photos = files[:4]

gallery_dir = r'c:\Users\moham\Boss\assets\gallery'
os.makedirs(gallery_dir, exist_ok=True)

new_images = []
for i, f in enumerate(reversed(recent_photos)):
    filename = f'trophy_{i+1}.jpg'
    dst = os.path.join(gallery_dir, filename)
    shutil.copy(f, dst)
    new_images.append(f'assets/gallery/{filename}')

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix line endings
content = content.replace('\r\r\n', '\n').replace('\r\n', '\n')

# 1. Update Filters
filter_start_str = '<div class="gallery-filter-bar"'
filter_start = content.find(filter_start_str)
filter_end = content.find('</div>', filter_start) + 6

new_filters = '''<div class="gallery-filter-bar" role="group" aria-label="Gallery Filter">
        <button class="filter-btn active" data-filter="all" id="filterAll">🏍️ All Builds</button>
        <button class="filter-btn" data-filter="awards" id="filterAwards">🏆 Awards</button>
        <button class="filter-btn" data-filter="custom" id="filterCustom">🎨 Custom Mods</button>
        <button class="filter-btn" data-filter="service" id="filterService">🔧 Service Work</button>
        <button class="filter-btn" data-filter="paint" id="filterPaint">🖌️ Paint Jobs</button>
        <button class="filter-btn" data-filter="performance" id="filterPerformance">🚀 Performance</button>
      </div>'''

content = content[:filter_start] + new_filters + content[filter_end:]

# 2. Update Grid
grid_start_str = '<div class="masonry-grid" id="masonryGrid" aria-label="Gallery images">'
grid_end_str = '<!-- /masonry-grid -->'

gs = content.find(grid_start_str)
ge = content.find(grid_end_str)

if gs != -1 and ge != -1:
    gs += len(grid_start_str)
    
    items_html = '\n'
    for i, img in enumerate(new_images):
        delay = '' if i == 0 else f' reveal-delay-{i}'
        items_html += f'''        <div class="masonry-item reveal{delay}" data-category="awards" tabindex="0" role="button" aria-label="View: Award">
          <img src="{img}?v=1" alt="Trophy {i+1}" loading="lazy" />
          <div class="zoom-icon" aria-hidden="true">↗</div>
          <div class="masonry-overlay">
            <div class="masonry-info">
              <span class="tag">Awards</span>
              <h3 class="h4" style="color: #fff; margin-top: 0.5rem;">Boss Moto Trophy</h3>
            </div>
          </div>
        </div>\n'''
    
    items_html += '      </div>\n      '
    
    content = content[:gs] + items_html + content[ge:]
    
    # 3. Update Gallery Count
    content = re.sub(r'Showing all \d+ builds', f'Showing {len(new_images)} items', content)
    content = re.sub(r'Showing all builds', f'Showing {len(new_images)} items', content)
    
    with open('gallery.html', 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("Gallery successfully updated!")
else:
    print(f"Error: Could not find grid tags. gs={gs}, ge={ge}")
