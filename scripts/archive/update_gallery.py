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
    filename = f'gallery_img_{i+1}.jpg'
    dst = os.path.join(gallery_dir, filename)
    shutil.copy(f, dst)
    new_images.append(f'assets/gallery/{filename}')

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix line endings
content = content.replace('\r\r\n', '\n').replace('\r\n', '\n')

# Find the start of the first masonry-item and the end of the last one
start_idx = content.find('<div class="masonry-item')
if start_idx != -1:
    # Find the end of the gallery grid. It's closed by a div, followed by </section> usually.
    # Let's find the placeholder <img src="" alt="Gallery Image Preview" /> which is inside the lightbox
    end_idx = content.find('<div id="lightbox"', start_idx)
    if end_idx == -1:
        # fallback
        end_idx = content.find('</main>', start_idx)
    
    # We need to find the exact closing tag of the masonry-grid, which is just before lightbox
    # Let's search backwards from end_idx for the closing div
    grid_end = content.rfind('</div>', start_idx, end_idx)
    # The grid structure is:
    # <div class="masonry-grid" id="galleryGrid">
    #   <div class="masonry-item">...</div>
    # </div>
    # So the last </div> before the lightbox is the grid closing.
    grid_end = content.rfind('</div>', start_idx, content.rfind('</div>', start_idx, end_idx))

    items_html = ''
    for i, img in enumerate(new_images):
        delay = '' if i == 0 else f' reveal-delay-{(i%5)+1}'
        items_html += f'''
        <div class="masonry-item reveal{delay}" data-category="awards" tabindex="0" role="button" aria-label="View: Gallery Image {i+1}">
          <img src="{img}?v=1" alt="Gallery Image {i+1}" loading="lazy" />
          <div class="zoom-icon" aria-hidden="true">↗</div>
          <div class="masonry-overlay">
            <div class="masonry-info">
              <span class="tag">Awards & Achievements</span>
              <h3 class="h4" style="color: #fff; margin-top: 0.5rem;">Boss Moto History</h3>
            </div>
          </div>
        </div>
'''
    
    # Let's also update the filter buttons to include an 'awards' filter
    filter_html = '''
        <button class="brand-filter-btn active" data-filter="all"><span>All Builds</span></button>
        <button class="brand-filter-btn" data-filter="awards"><span>Awards</span></button>
        <button class="brand-filter-btn" data-filter="custom"><span>Custom Mods</span></button>
        <button class="brand-filter-btn" data-filter="service"><span>Service Work</span></button>
        <button class="brand-filter-btn" data-filter="paint"><span>Paint Jobs</span></button>
        <button class="brand-filter-btn" data-filter="performance"><span>Performance</span></button>
    '''
    
    # Replace old filters with new filters
    filter_start = content.find('<div class="brand-catalog-filters"')
    if filter_start != -1:
        filter_start = content.find('>', filter_start) + 1
        filter_end = content.find('</div>', filter_start)
        content = content[:filter_start] + filter_html + content[filter_end:]
    
    # Recalculate start_idx because we modified content above it
    start_idx = content.find('<div class="masonry-item')
    end_idx = content.find('<div id="lightbox"', start_idx)
    grid_end_2 = content.rfind('</div>', start_idx, end_idx)
    grid_end_1 = content.rfind('</div>', start_idx, grid_end_2)
    # Actually, instead of exact divs, just replace everything between <div class="masonry-grid" id="galleryGrid"> and </div>\n    <div id="lightbox"
    grid_start_tag = '<div class="masonry-grid" id="galleryGrid">'
    gs = content.find(grid_start_tag) + len(grid_start_tag)
    ge = content.find('</div>\n\n    <!-- Lightbox -->')
    if ge == -1:
        ge = content.find('<div id="lightbox"')
        # Backtrack past the closing </div> of the grid
        ge = content.rfind('</div>', gs, ge)
    
    content = content[:gs] + '\n' + items_html + '      ' + content[ge:]
    
    # Also update the showing text
    content = re.sub(r'Showing all \d+ builds', f'Showing {len(new_images)} items', content)

    with open('gallery.html', 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("Gallery successfully updated!")
else:
    print("Could not find masonry items.")
