import os

with open('investors.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read()

target = '        <a href="#inquiry" class="btn btn-primary">📝 Partner Inquiry</a>\n'

if target in html:
    html = html.replace(target, '')
else:
    # try replacing with carriage return
    target2 = '        <a href="#inquiry" class="btn btn-primary">📝 Partner Inquiry</a>\r\n'
    if target2 in html:
        html = html.replace(target2, '')

# Change the other button to btn-primary
html = html.replace('btn-outline">💡 Investment Highlights', 'btn-primary">💡 Investment Highlights')

with open('investors.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
