import os
import shutil
import glob
import re

# Source directory containing generated images
src_dir = r"C:\Users\moham\.gemini\antigravity-ide\brain\20f2a4a0-62e6-442d-a13c-c93e82b1b4b2"

# Destination directory
dest_dir = r"c:\Users\moham\Boss\assets\gallery"
os.makedirs(dest_dir, exist_ok=True)

# Map prefix to destination filename
image_map = {
    're_bobber': 're_bobber.jpg',
    'ktm_track': 'ktm_track.jpg',
    'rx100_retro': 'rx100_retro.jpg',
    'himalayan_adv': 'himalayan_adv.jpg'
}

# Copy and rename images
for prefix, new_name in image_map.items():
    files = glob.glob(os.path.join(src_dir, f"{prefix}_*.jpg"))
    if files:
        latest_file = max(files, key=os.path.getctime)
        dest_path = os.path.join(dest_dir, new_name)
        shutil.copy2(latest_file, dest_path)
        print(f"Copied {os.path.basename(latest_file)} to {dest_path}")

# Update index.html
html_path = r"c:\Users\moham\Boss\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace specifically using the alt text
replacements = [
    (r'<img src="[^"]*" alt="Modified Royal Enfield Bobber"', r'<img src="assets/gallery/re_bobber.jpg" alt="Modified Royal Enfield Bobber"'),
    (r'<img src="[^"]*" alt="KTM Custom Streetfighter"', r'<img src="assets/gallery/ktm_track.jpg" alt="KTM Custom Streetfighter"'),
    (r'<img src="[^"]*" alt="Classic Cafe Racer"', r'<img src="assets/gallery/rx100_retro.jpg" alt="Classic Cafe Racer"'),
    (r'<img src="[^"]*" alt="Adventure Touring Setup"', r'<img src="assets/gallery/himalayan_adv.jpg" alt="Adventure Touring Setup"')
]

new_html = html
for old_pattern, new_replacement in replacements:
    new_html = re.sub(old_pattern, new_replacement, new_html)

if new_html != html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated index.html successfully.")
else:
    print("No changes made to index.html.")
