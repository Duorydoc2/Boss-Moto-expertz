import os
import glob

# Map of emojis to premium SVG code
svg_map = {
    '🖥️': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="premium-icon"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    '⏱️': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="premium-icon"><circle cx="12" cy="13" r="8"></circle><path d="M12 9v4l2 2"></path><line x1="10" y1="2" x2="14" y2="2"></line><line x1="12" y1="2" x2="12" y2="5"></line></svg>',
    '🛡️': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="premium-icon"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
    '📝': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="premium-icon"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>'
}

# The folder to process
folder_path = r'c:\Users\moham\Boss'

# Find all HTML files
html_files = glob.glob(os.path.join(folder_path, '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace each emoji with its SVG
    for emoji, svg in svg_map.items():
        # Using string replace to swap them out completely
        content = content.replace(emoji, svg)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced premium icons in {os.path.basename(file_path)}")
    else:
        print(f"No changes needed for {os.path.basename(file_path)}")

print("All files processed successfully.")
