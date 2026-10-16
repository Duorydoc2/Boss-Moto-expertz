import os
import glob
import re

svgs = {
    'calendar': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
    
    'phone': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>',
    
    'map_pin': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
    
    'message': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>',
    
    'instagram': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>',
    
    'youtube': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>',
    
    'clock': '<svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-0.125em; margin-right:4px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
}

def replace_contextual(text):
    # 1. Nav CTA Book Service
    text = re.sub(r'📝(\s*Book Service)', svgs['calendar'] + r'\1', text)
    text = re.sub(r'📝(\s*BOOK NOW)', svgs['calendar'] + r'\1', text)
    
    # 2. Contact Phone buttons
    text = re.sub(r'📝(\s*\+91\s*63)', svgs['phone'] + r'\1', text)
    text = re.sub(r'📝(\s*Call:?\s*\+91)', svgs['phone'] + r'\1', text)
    text = re.sub(r'📞(\s*Contact\s*\+91)', svgs['phone'] + r'\1', text)
    text = re.sub(r'📞(\s*Call\s*\+91)', svgs['phone'] + r'\1', text)
    
    # 3. Instagram icons
    text = re.sub(r'📸(\s*<\/a>)', svgs['instagram'] + r'\1', text)
    
    # 4. Footer items
    # Map pin
    text = re.sub(r'<span class="icon">📝<\/span>(<a href="https:\/\/maps)', '<span class="icon">' + svgs['map_pin'] + r'</span>\1', text)
    # Phone
    text = re.sub(r'<span class="icon">📝<\/span>(<a href="tel:)', '<span class="icon">' + svgs['phone'] + r'</span>\1', text)
    # WhatsApp
    text = re.sub(r'<span class="icon">💬<\/span>(<a href="https:\/\/wa.me)', '<span class="icon">' + svgs['message'] + r'</span>\1', text)
    # Clock
    text = re.sub(r'<span class="icon">📝<\/span>(<span>Mon)', '<span class="icon">' + svgs['clock'] + r'</span>\1', text)
    
    # 5. Contact info cards
    # "Work" -> Map Pin
    text = re.sub(r'<div class="icon-wrap">📝<\/div>(\s*<div class="info-text">\s*<h4>Work)', '<div class="icon-wrap">' + svgs['map_pin'] + r'</div>\1', text)
    # "Call Us" -> Phone
    text = re.sub(r'<div class="icon-wrap">📝<\/div>(\s*<div class="info-text">\s*<h4>Call Us)', '<div class="icon-wrap">' + svgs['phone'] + r'</div>\1', text)
    # "WhatsApp" -> Message
    text = re.sub(r'<div class="icon-wrap">💬<\/div>(\s*<div class="info-text">\s*<h4>WhatsApp)', '<div class="icon-wrap">' + svgs['message'] + r'</div>\1', text)
    # "Instagram" -> Instagram
    text = re.sub(r'<div class="icon-wrap">📝<\/div>(\s*<div class="info-text">\s*<h4>Instagram)', '<div class="icon-wrap">' + svgs['instagram'] + r'</div>\1', text)
    # "YouTube" -> YouTube
    text = re.sub(r'<div class="icon-wrap">▶️<\/div>(\s*<div class="info-text">\s*<h4>YouTube)', '<div class="icon-wrap">' + svgs['youtube'] + r'</div>\1', text)
    
    # 6. Any stray Instagram links that still use 📝
    text = re.sub(r'>📝(<\/a>)', '>' + svgs['instagram'] + r'\1', text) # Danger if 📝 is used for something else inside <a>, but mostly Instagram here.
    
    return text

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = replace_contextual(content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated emojis to SVGs in {file}")
