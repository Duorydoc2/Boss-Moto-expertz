with open('careers.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read()

nl = '\r\n' if '\r\n' in html else '\n'

# Insert Junior Technician card after Job 1
target_job1_end = '          <div class="job-actions">' + nl + '            <button class="btn btn-outline btn-sm apply-btn" data-role="Senior Technician (Superbike & Multi-Brand)">Apply For Role</button>' + nl + '          </div>' + nl + '        </article>'

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

if target_job1_end in html:
    html = html.replace(target_job1_end, target_job1_end + junior_card)

# Clean up dropdown option
html = html.replace('                <option value="Junior Mechanic Apprentice">Junior Mechanic Apprentice</option>' + nl, '')

# Update Experience Dropdown
old_exp = (
    '                <option value="0-1 Years">0 - 1 Years (Fresher)</option>' + nl +
    '                <option value="1-3 Years">1 - 3 Years</option>' + nl +
    '                <option value="3-5 Years">3 - 5 Years</option>' + nl +
    '                <option value="5+ Years">5+ Years (Master)</option>'
)

new_exp = (
    '                <option value="Intern / Trainee (0 Exp)">Intern / Trainee (0 Years Exp)</option>' + nl +
    '                <option value="0-1 Years (Fresher)">0 - 1 Years (Fresher / Trainee)</option>' + nl +
    '                <option value="1-3 Years (Junior Technician)">1 - 3 Years (Junior Technician)</option>' + nl +
    '                <option value="3-5 Years (Mid-Level)">3 - 5 Years (Mid-Level)</option>' + nl +
    '                <option value="4+ Years (Senior Technician)">4+ Years (Senior Technician)</option>'
)

if old_exp in html:
    html = html.replace(old_exp, new_exp)

with open('careers.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
