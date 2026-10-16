import os
import re

html_path = r"c:\Users\moham\Boss\gallery.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# New Filter Bar
new_filters = '''      <div class="gallery-filter-bar" role="group" aria-label="Gallery Filter">
        <button class="filter-btn active" data-filter="all" id="filterAll">📸 All Photos</button>
        <button class="filter-btn" data-filter="awards" id="filterAwards">🏆 Awards & Trophies</button>
        <button class="filter-btn" data-filter="action" id="filterAction">⚡ Action Shots</button>
        <button class="filter-btn" data-filter="team" id="filterTeam">👥 The Team</button>
      </div>'''

# Replace old filter bar
filter_start = content.find('<div class="gallery-filter-bar"')
filter_end = content.find('</div>', filter_start) + 6
content = content[:filter_start] + new_filters + content[filter_end:]

# New Masonry Grid Items
items = [
    {'src': 'assets/gallery/gallery_action_1.png', 'cat': 'action', 'title': 'Action Shot 1', 'tag': 'Action'},
    {'src': 'assets/gallery/gallery_action_2.png', 'cat': 'action', 'title': 'Action Shot 2', 'tag': 'Action'},
    {'src': 'assets/gallery/gallery_team_1.jpg', 'cat': 'team', 'title': 'The Team', 'tag': 'Team'},
    {'src': 'assets/gallery/trophy_1.jpg', 'cat': 'awards', 'title': 'Trophy 1', 'tag': 'Awards'},
    {'src': 'assets/gallery/trophy_2.jpg', 'cat': 'awards', 'title': 'Trophy 2', 'tag': 'Awards'},
    {'src': 'assets/gallery/trophy_3.jpg', 'cat': 'awards', 'title': 'Trophy 3', 'tag': 'Awards'}
]

items_html = '\n'
for i, item in enumerate(items):
    delay = '' if i == 0 else f' reveal-delay-{(i%5)}'
    items_html += f'''
        <div class="masonry-item reveal{delay}" data-category="{item['cat']}" tabindex="0" role="button" aria-label="View: {item['title']}">
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
grid_start = content.find('<div class="masonry-grid" id="masonryGrid"')
grid_content_start = content.find('>', grid_start) + 1
# Assuming the grid ends before <div id="lightbox" or </section>
grid_end = content.find('</section>', grid_content_start)
# We need to find the closing div of the grid. It should be the last </div> before </section> in that block.
# Alternatively, just regex from <div class="masonry-grid"...> to </div>\n\n  </section>
match = re.search(r'(<div class="masonry-grid"[^>]*>).*?(</section>)', content, re.DOTALL)
if match:
    # Wait, there's a closing div for the container maybe?
    # Let's be precise. The grid closes with </div>, then the container closes with </div>, then </section> closes.
    # So replacing from grid_content_start to the last </div></div> before </section>
    
    # A safer way: Find `<div class="masonry-grid"` and find the matching closing tag.
    pass

# Let's just use string replacement on the whole section to be safe
section_start = content.find('<!-- Masonry Grid -->')
section_end = content.find('</section>', section_start)

new_grid_section = '<!-- Masonry Grid -->\n      <div class="masonry-grid" id="masonryGrid" aria-label="Gallery images">' + items_html + '      </div>\n    </div>\n  '

content = content[:section_start] + new_grid_section + content[section_end:]

# Update showing count text
content = re.sub(r'<p class="gallery-count"[^>]*>.*?</p>', '<p class="gallery-count" aria-live="polite">Showing all 6 photos</p>', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery replaced with the 6 specific photos.")
