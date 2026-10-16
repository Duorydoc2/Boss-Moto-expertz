import os
import shutil
import glob
import re

# Source directory containing generated images
src_dir = r"C:\Users\moham\.gemini\antigravity-ide\brain\20f2a4a0-62e6-442d-a13c-c93e82b1b4b2"

# Destination directory
dest_dir = r"c:\Users\moham\Boss\assets\services"
os.makedirs(dest_dir, exist_ok=True)

# Map prefix to destination filename
image_map = {
    'general_service': 'general_service.jpg',
    'engine_repair': 'engine_repair.jpg',
    'ecu_tuning': 'ecu_tuning.jpg',
    'custom_build': 'custom_build.jpg',
    'bike_painting': 'bike_painting.jpg',
    'brake_suspension': 'brake_suspension.jpg'
}

# Copy and rename images
for prefix, new_name in image_map.items():
    files = glob.glob(os.path.join(src_dir, f"{prefix}_*.jpg"))
    if files:
        # take the most recently generated one if multiple
        latest_file = max(files, key=os.path.getctime)
        dest_path = os.path.join(dest_dir, new_name)
        shutil.copy2(latest_file, dest_path)
        print(f"Copied {os.path.basename(latest_file)} to {dest_path}")

# Update index.html
html_path = r"c:\Users\moham\Boss\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace specifically using the alt text as context to avoid duplicates replacing incorrectly
replacements = [
    (r'<img src="[^"]*" alt="General Bike Service"', r'<img src="assets/services/general_service.jpg" alt="General Bike Service"'),
    (r'<img src="[^"]*" alt="Engine Repair"', r'<img src="assets/services/engine_repair.jpg" alt="Engine Repair"'),
    (r'<img src="[^"]*" alt="ECU Tuning"', r'<img src="assets/services/ecu_tuning.jpg" alt="ECU Tuning"'),
    (r'<img src="[^"]*" alt="Custom Modification"', r'<img src="assets/services/custom_build.jpg" alt="Custom Modification"'),
    (r'<img src="[^"]*" alt="Bike Painting"', r'<img src="assets/services/bike_painting.jpg" alt="Bike Painting"'),
    (r'<img src="[^"]*" alt="Brake & Suspension Work"', r'<img src="assets/services/brake_suspension.jpg" alt="Brake & Suspension Work"')
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
