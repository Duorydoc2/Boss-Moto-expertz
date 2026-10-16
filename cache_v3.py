with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="css/style.css?v=v2"', 'href="css/style.css?v=v3"')
html = html.replace('src="js/main.js?v=v2"', 'src="js/main.js?v=v3"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
