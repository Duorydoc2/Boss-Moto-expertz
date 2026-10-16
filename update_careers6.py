with open('careers.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read()

nl = '\r\n' if '\r\n' in html else '\n'

html = html.replace('                <option value="Junior Mechanic Apprentice">Junior Mechanic Apprentice</option>' + nl, '')

old_exp_block = (
    '                <option value="0-1 Years">0 - 1 Years (Fresher)</option>' + nl +
    '                <option value="1-3 Years">1 - 3 Years</option>' + nl +
    '                <option value="3-5 Years">3 - 5 Years</option>' + nl +
    '                <option value="5+ Years">5+ Years (Master)</option>'
)

new_exp_block = (
    '                <option value="Intern / Trainee (0 Exp)">Intern / Trainee (0 Years Exp)</option>' + nl +
    '                <option value="0-1 Years (Fresher)">0 - 1 Years (Fresher / Trainee)</option>' + nl +
    '                <option value="1-3 Years (Junior Technician)">1 - 3 Years (Junior Technician)</option>' + nl +
    '                <option value="3-5 Years (Mid-Level)">3 - 5 Years (Mid-Level)</option>' + nl +
    '                <option value="4+ Years (Senior Technician)">4+ Years (Senior Technician)</option>'
)

html = html.replace(old_exp_block, new_exp_block)

with open('careers.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
