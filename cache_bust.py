with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="css/style.css"', 'href="css/style.css?v=v2"')
html = html.replace('href="css/style.css?v=1.1"', 'href="css/style.css?v=v2"')
html = html.replace('src="js/main.js"', 'src="js/main.js?v=v2"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
