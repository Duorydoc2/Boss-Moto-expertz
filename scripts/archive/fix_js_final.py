with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for l in lines:
    if 'btn.innerHTML =' in l:
        new_lines.append('      btn.innerHTML = `<span class="theme-dot" style="background:${t.dot};"></span> ${t.label}`;\n')
    else:
        new_lines.append(l)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
