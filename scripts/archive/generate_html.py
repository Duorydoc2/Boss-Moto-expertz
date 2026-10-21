import os
import glob
html = '<html><body><h1>Logos</h1>\n'
files = glob.glob(r'C:\Users\moham\.gemini\antigravity-ide\brain\521f531e-9d43-447b-8c37-ec4c9e6f60f3\.user_uploaded\*.*')
for f in files:
    name = os.path.basename(f)
    path = f.replace('\\', '/')
    html += f"<div><h3>{name}</h3><img src='file:///{path}' style='max-width:300px; max-height:200px; border:1px solid #ccc;' /></div><hr/>\n"
html += '</body></html>'
with open('show_logos.html', 'w', encoding='utf-8') as f:
    f.write(html)
