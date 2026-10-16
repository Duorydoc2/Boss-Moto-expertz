import os

with open('investors.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read()

target = '        <a href="#inquiry" class="btn btn-primary">📝 Partner Inquiry</a>'

html = html.replace(target, '')

# Also remove the empty line left behind if possible, but let's just use string replace.
html = html.replace('\n\n        <a href="#highlights"', '\n        <a href="#highlights"')
html = html.replace('\r\n\r\n        <a href="#highlights"', '\r\n        <a href="#highlights"')

with open('investors.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
