import os
import re

html_path = r"c:\Users\moham\Boss\gallery.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Correctly mapped and arranged items based on visual analysis of the CSS columns
items = [
    # Team / Founder
    {'src': 'assets/gallery/gallery_action_1.png', 'cat': 'team', 'title': 'Boss Moto Founder', 'tag': 'Team'},
    {'src': 'assets/gallery/gallery_team_1.jpg', 'cat': 'team', 'title': 'Track Support', 'tag': 'Team'},
    
    # Action
    {'src': 'assets/gallery/gallery_action_2.png', 'cat': 'action', 'title': 'Racing in Action', 'tag': 'Action'},
    
    # Trophies
    {'src': 'assets/gallery/trophy_2.jpg', 'cat': 'awards', 'title': 'Championship Win', 'tag': 'Awards'},
    {'src': 'assets/gallery/trophy_1.jpg', 'cat': 'awards', 'title': 'Racing Achievement', 'tag': 'Awards'},
    {'src': 'assets/gallery/trophy_3.jpg', 'cat': 'awards', 'title': 'Podium Finish', 'tag': 'Awards'}
]

items_html = '\n'
for i, item in enumerate(items):
    delay = '' if i == 0 else f' reveal-delay-{(i%5)}'
    items_html += f'''        <div class="masonry-item reveal{delay}" data-category="{item['cat']}" tabindex="0" role="button" aria-label="View: {item['title']}">
          <img src="{item['src']}" alt="{item['title']}" loading="lazy" />
          <div class="zoom-icon" aria-hidden="true">↗</div>
          <div class="masonry-overlay">
            <div class="masonry-info">
              <span class="tag">{item['tag']}</span>
              <h4>{item['title']}</h4>
            </div>
          </div>
        </div>
'''

# Find grid start and end
section_start = content.find('<!-- Masonry Grid -->')
section_end = content.find('</section>', section_start)

new_grid_section = '<!-- Masonry Grid -->\n      <div class="masonry-grid" id="masonryGrid" aria-label="Gallery images">\n' + items_html + '      </div>\n    </div>\n  '

content = content[:section_start] + new_grid_section + content[section_end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery properly arranged and labelled.")
