import os
import shutil
import glob
import re

# Source directory containing generated images
src_dir = r"C:\Users\moham\.gemini\antigravity-ide\brain\20f2a4a0-62e6-442d-a13c-c93e82b1b4b2"

# Destination directory
gallery_dir = r"c:\Users\moham\Boss\assets\gallery"
os.makedirs(gallery_dir, exist_ok=True)

# Map prefix to destination filename
image_map = {
    'scrambler': 'scrambler.jpg',
    'exhaust': 'exhaust.jpg',
    'tank_paint': 'tank_paint.jpg',
    'led_light': 'led_light.jpg',
    'air_intake': 'air_intake.jpg'
}

# Copy and rename images
for prefix, new_name in image_map.items():
    files = glob.glob(os.path.join(src_dir, f"{prefix}_*.jpg"))
    if files:
        latest_file = max(files, key=os.path.getctime)
        dest_path = os.path.join(gallery_dir, new_name)
        shutil.copy2(latest_file, dest_path)
        print(f"Copied {os.path.basename(latest_file)} to {dest_path}")

# Update gallery.html
html_path = r"c:\Users\moham\Boss\gallery.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace specifically using the alt text
replacements = [
    (r'<img src="[^"]*" alt="Custom Royal Enfield Bobber Build"', r'<img src="assets/gallery/re_bobber.jpg" alt="Custom Royal Enfield Bobber Build"'),
    (r'<img src="[^"]*" alt="KTM Duke Street Fighter Custom Build"', r'<img src="assets/gallery/ktm_track.jpg" alt="KTM Duke Street Fighter Custom Build"'),
    (r'<img src="[^"]*" alt="Classic Cafe Racer Custom Paint"', r'<img src="assets/gallery/rx100_retro.jpg" alt="Classic Cafe Racer Custom Paint"'),
    (r'<img src="[^"]*" alt="Adventure Touring Motorcycle Setup"', r'<img src="assets/gallery/himalayan_adv.jpg" alt="Adventure Touring Motorcycle Setup"'),
    (r'<img src="[^"]*" alt="Off-Road Scrambler Motorcycle Build"', r'<img src="assets/gallery/scrambler.jpg" alt="Off-Road Scrambler Motorcycle Build"'),
    (r'<img src="[^"]*" alt="Motorcycle Engine Overhaul"', r'<img src="assets/services/engine_repair.jpg" alt="Motorcycle Engine Overhaul"'),
    (r'<img src="[^"]*" alt="ECU Tuning Performance Work"', r'<img src="assets/services/ecu_tuning.jpg" alt="ECU Tuning Performance Work"'),
    (r'<img src="[^"]*" alt="Custom Motorcycle Paint Job"', r'<img src="assets/services/bike_painting.jpg" alt="Custom Motorcycle Paint Job"'),
    (r'<img src="[^"]*" alt="Brake System Service and Repair"', r'<img src="assets/services/brake_suspension.jpg" alt="Brake System Service and Repair"'),
    (r'<img src="[^"]*" alt="Performance Exhaust Upgrade"', r'<img src="assets/gallery/exhaust.jpg" alt="Performance Exhaust Upgrade"'),
    (r'<img src="[^"]*" alt="Two-Tone Custom Tank Paint"', r'<img src="assets/gallery/tank_paint.jpg" alt="Two-Tone Custom Tank Paint"'),
    (r'<img src="[^"]*" alt="LED Lighting Upgrade on Motorcycle"', r'<img src="assets/gallery/led_light.jpg" alt="LED Lighting Upgrade on Motorcycle"'),
    (r'<img src="[^"]*" alt="Suspension Overhaul Fork Seals"', r'<img src="assets/services/brake_suspension.jpg" alt="Suspension Overhaul Fork Seals"'),
    (r'<img src="[^"]*" alt="Royal Enfield Classic Cafe Racer Conversion"', r'<img src="assets/services/custom_build.jpg" alt="Royal Enfield Classic Cafe Racer Conversion"'),
    (r'<img src="[^"]*" alt="High Flow Air Intake Performance Upgrade"', r'<img src="assets/gallery/air_intake.jpg" alt="High Flow Air Intake Performance Upgrade"')
]

new_html = html
for old_pattern, new_replacement in replacements:
    new_html = re.sub(old_pattern, new_replacement, new_html)

if new_html != html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated gallery.html successfully.")
else:
    print("No changes made to gallery.html.")
