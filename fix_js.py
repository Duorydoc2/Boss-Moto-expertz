with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

bad_str = 'btn.innerHTML = <span class="theme-dot" style="background:;"></span> ;'
good_str = 'btn.innerHTML = <span class="theme-dot" style="background:;"></span> ;'

if bad_str in js:
    js = js.replace(bad_str, good_str)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
