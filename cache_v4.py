with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="css/style.css?v=v3"', 'href="css/style.css?v=v4"')
html = html.replace('src="js/main.js?v=v3"', 'src="js/main.js?v=v4"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
