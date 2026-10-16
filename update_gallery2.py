import os, glob, shutil, re

uploads = r'C:\Users\moham\.gemini\antigravity-ide\brain\521f531e-9d43-447b-8c37-ec4c9e6f60f3\.user_uploaded\*.*'
files = glob.glob(uploads)
files.sort(key=os.path.getmtime, reverse=True)

# The files to copy
action_2_src = files[0] # media_1788329774820.png (Dirt bike)
team_1_src = files[1]   # media_1788329762865.jpg (Portrait)
action_1_src = files[2] # media_1788329318642.png (Umbrella)

gallery_dir = r'c:\Users\moham\Boss\assets\gallery'

# Copy the 3 new images
shutil.copy(action_2_src, os.path.join(gallery_dir, 'gallery_action_2.png'))
shutil.copy(team_1_src, os.path.join(gallery_dir, 'gallery_team_1.jpg'))
shutil.copy(action_1_src, os.path.join(gallery_dir, 'gallery_action_1.png'))

# The final list of images and their metadata
gallery_items = [
    {'src': 'assets/gallery/trophy_1.jpg', 'cat': 'awards', 'tag': 'Awards', 'title': 'Boss Moto Trophy'},
    {'src': 'assets/gallery/trophy_2.jpg', 'cat': 'awards', 'tag': 'Awards', 'title': 'Boss Moto Award'},
    {'src': 'assets/gallery/trophy_3.jpg', 'cat': 'awards', 'tag': 'Awards', 'title': 'Championship Trophies'},
    {'src': 'assets/gallery/gallery_team_1.jpg', 'cat': 'team', 'tag': 'Team', 'title': 'Boss Moto Team'},
    {'src': 'assets/gallery/gallery_action_1.png', 'cat': 'action', 'tag': 'Action', 'title': 'Track Day Prep'},
    {'src': 'assets/gallery/gallery_action_2.png', 'cat': 'action', 'tag': 'Action', 'title': 'Dirt Track Racing'},
]

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix line endings
content = content.replace('\r\r\n', '\n').replace('\r\n', '\n')

# 1. Update Filters to include Team and Action
filter_start_str = '<div class="gallery-filter-bar"'
filter_start = content.find(filter_start_str)
filter_end = content.find('</div>', filter_start) + 6

new_filters = '''<div class="gallery-filter-bar" role="group" aria-label="Gallery Filter">
        <button class="filter-btn active" data-filter="all" id="filterAll">🏍️ All Media</button>
        <button class="filter-btn" data-filter="awards" id="filterAwards">🏆 Awards</button>
        <button class="filter-btn" data-filter="team" id="filterTeam">👥 Team</button>
        <button class="filter-btn" data-filter="action" id="filterAction">🏁 Track Action</button>
        <button class="filter-btn" data-filter="custom" id="filterCustom">🎨 Custom Mods</button>
        <button class="filter-btn" data-filter="service" id="filterService">🔧 Service Work</button>
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
    for i, item in enumerate(gallery_items):
        delay = '' if i == 0 else f' reveal-delay-{i%5}'
        items_html += f'''        <div class="masonry-item reveal{delay}" data-category="{item['cat']}" tabindex="0" role="button" aria-label="View: {item['title']}">
          <img src="{item['src']}?v=2" alt="{item['title']}" loading="lazy" />
          <div class="zoom-icon" aria-hidden="true">↗</div>
          <div class="masonry-overlay">
            <div class="masonry-info">
              <span class="tag">{item['tag']}</span>
              <h3 class="h4" style="color: #fff; margin-top: 0.5rem;">{item['title']}</h3>
            </div>
          </div>
        </div>\n'''
    
    items_html += '      </div>\n      '
    
    content = content[:gs] + items_html + content[ge:]
    
    # 3. Update Gallery Count
    content = re.sub(r'Showing \d+ items', f'Showing {len(gallery_items)} items', content)
    
    with open('gallery.html', 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("Gallery successfully updated!")
else:
    print(f"Error: Could not find grid tags. gs={gs}, ge={ge}")
