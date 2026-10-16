with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'btn.innerHTML =' in line and 'theme-dot' in line:
        new_lines.append('      btn.innerHTML = <span class=\"theme-dot\" style=\"background:;\"></span> ;\n')
    else:
        new_lines.append(line)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
