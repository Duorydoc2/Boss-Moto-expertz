with open('careers.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read()

# Normalize newline for matching if needed
nl = '\r\n' if '\r\n' in html else '\n'

# 1. Update filter pills
html = html.replace(
    'data-filter="tech">Mechanics & Tech</button>',
    'data-filter="tech">Senior & Junior Tech</button>' + nl + '          <button type="button" class="pill-btn" data-filter="intern">Intern / Trainee</button>'
)

# 2. Update Job 1 to Senior Technician
html = html.replace(
    '<h3>Master Superbike Technician</h3>',
    '<h3>Senior Superbike & Multi-Brand Technician</h3>'
)
html = html.replace(
    'data-role="Master Superbike Technician"',
    'data-role="Senior Technician (Superbike & Multi-Brand)"'
)
html = html.replace(
    '<span>⏱️ 5+ Years Exp</span>',
    '<span>⏱️ 4+ Years Exp (Senior)</span>'
)

# 3. Add Junior Technician job card after Job 1
job1_target = 'data-role="Senior Technician (Superbike & Multi-Brand)">Apply For Role</button>' + nl + '          </div>' + nl + '        </article>'

junior_card = (
    nl + nl +
    '        <!-- Job 1b: Junior Technician -->' + nl +
    '        <article class="job-card glass-card reveal reveal-delay-1" data-category="tech">' + nl +
    '          <div class="job-header">' + nl +
    '            <div class="job-title-wrap">' + nl +
    '              <span class="job-badge" style="background:rgba(250,114,50,0.15);color:var(--orange);border-color:rgba(250,114,50,0.3);">Junior Role</span>' + nl +
    '              <h3>Junior Motorcycle Technician</h3>' + nl +
    '            </div>' + nl +
    '            <div class="job-location">📝 Coimbatore Hub</div>' + nl +
    '          </div>' + nl +
    '          <div class="job-meta">' + nl +
    '            <span>⏱️ 1-3 Years Exp</span>' + nl +
    '            <span>💰 Salary + Skill Incentives</span>' + nl +
    '            <span>🛠️ Maintenance & Repair</span>' + nl +
    '          </div>' + nl +
    '          <p class="job-desc">Perform periodic bike services, oil changes, brake overhaul, clutch cable adjustments, suspension oiling, and routine workshop repairs under senior guidance.</p>' + nl +
    '          <div class="job-actions">' + nl +
    '            <button class="btn btn-outline btn-sm apply-btn" data-role="Junior Technician (General Service & Repair)">Apply For Role</button>' + nl +
    '          </div>' + nl +
    '        </article>'
)

if job1_target in html:
    html = html.replace(job1_target, job1_target + junior_card)

# 4. Update Apprentice card to Intern / Trainee Technician
html = html.replace(
    '<h3>Junior Mechanic Apprentice</h3>',
    '<h3>Intern / Trainee Technician</h3>'
)
html = html.replace(
    'data-role="Junior Mechanic Apprentice"',
    'data-role="Intern / Trainee Technician"'
)
html = html.replace(
    '<article class="job-card glass-card reveal reveal-delay-3" data-category="tech">',
    '<article class="job-card glass-card reveal reveal-delay-3" data-category="intern">'
)
html = html.replace(
    '<span class="job-badge" style="background:rgba(0,210,132,0.15);color:#00d084;border-color:rgba(0,210,132,0.3);">Trainee / Fresher</span>',
    '<span class="job-badge" style="background:rgba(0,210,132,0.15);color:#00d084;border-color:rgba(0,210,132,0.3);">Internship / Training</span>'
)

# 5. Update Applicant Role Select Dropdown
old_role_opt = '<option value="Master Superbike Technician">Master Superbike Technician</option>'
new_role_opts = (
    '<option value="Senior Technician (Superbike & Multi-Brand)">Senior Technician (Superbike & Multi-Brand)</option>' + nl +
    '                <option value="Junior Technician (General Service & Repair)">Junior Technician (General Service & Repair)</option>' + nl +
    '                <option value="Intern / Trainee Technician">Intern / Trainee Technician</option>'
)

html = html.replace(old_role_opt, new_role_opts)
html = html.replace('                <option value="Junior Mechanic Apprentice">Junior Mechanic Apprentice</option>' + nl, '')

# 6. Update Applicant Experience Select Dropdown
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
