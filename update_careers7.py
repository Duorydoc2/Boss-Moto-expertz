with open('careers.html', 'r', encoding='utf-8', newline='') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '<option value="Junior Mechanic Apprentice">Junior Mechanic Apprentice</option>' in line:
        continue
    if '<option value="0-1 Years">0 - 1 Years (Fresher)</option>' in line:
        new_lines.append('                <option value="Intern / Trainee (0 Exp)">Intern / Trainee (0 Years Exp)</option>\n')
        new_lines.append('                <option value="0-1 Years (Fresher)">0 - 1 Years (Fresher / Trainee)</option>\n')
        continue
    if '<option value="1-3 Years">1 - 3 Years</option>' in line:
        new_lines.append('                <option value="1-3 Years (Junior Technician)">1 - 3 Years (Junior Technician)</option>\n')
        continue
    if '<option value="3-5 Years">3 - 5 Years</option>' in line:
        new_lines.append('                <option value="3-5 Years (Mid-Level)">3 - 5 Years (Mid-Level)</option>\n')
        continue
    if '<option value="5+ Years">5+ Years (Master)</option>' in line:
        new_lines.append('                <option value="4+ Years (Senior Technician)">4+ Years (Senior Technician)</option>\n')
        continue
    new_lines.append(line)

with open('careers.html', 'w', encoding='utf-8', newline='') as f:
    f.writelines(new_lines)
