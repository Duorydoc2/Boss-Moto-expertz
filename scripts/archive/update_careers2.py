with open('careers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update filter buttons
html = html.replace(
    '<button type="button" class="pill-btn" data-filter="tech">Mechanics & Tech</button>',
    '<button type="button" class="pill-btn" data-filter="tech">Senior & Junior Tech</button>\n          <button type="button" class="pill-btn" data-filter="intern">Intern / Trainee</button>'
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
job1_end = '</article>'
first_article_end = html.find(job1_end)
if first_article_end != -1:
    junior_card = '''\n\n        <!-- Job 1b: Junior Technician -->
        <article class="job-card glass-card reveal reveal-delay-1" data-category="tech">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge" style="background:rgba(250,114,50,0.15);color:var(--orange);border-color:rgba(250,114,50,0.3);">Junior Role</span>
              <h3>Junior Motorcycle Technician</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 1-3 Years Exp</span>
            <span>💰 Salary + Skill Incentives</span>
            <span>🛠️ General Maintenance & Repair</span>
          </div>
          <p class="job-desc">Perform periodic bike services, oil changes, brake overhaul, clutch cable adjustments, suspension oiling, and routine workshop repairs under senior guidance.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Junior Technician (General Service & Repair)">Apply For Role</button>
          </div>
        </article>'''
    
    insert_pos = first_article_end + len(job1_end)
    html = html[:insert_pos] + junior_card + html[insert_pos:]

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
    '<article class="job-card glass-card reveal reveal-delay-3" data-category="tech">\n          <div class="job-header">\n            <div class="job-title-wrap">\n              <span class="job-badge" style="background:rgba(0,210,132,0.15);color:#00d084;border-color:rgba(0,210,132,0.3);">Trainee / Fresher</span>',
    '<article class="job-card glass-card reveal reveal-delay-3" data-category="intern">\n          <div class="job-header">\n            <div class="job-title-wrap">\n              <span class="job-badge" style="background:rgba(0,210,132,0.15);color:#00d084;border-color:rgba(0,210,132,0.3);">Internship / Training</span>'
)

# 5. Update Applicant Role Select Dropdown
old_role_opt = '<option value="Master Superbike Technician">Master Superbike Technician</option>'
new_role_opts = '''<option value="Senior Technician (Superbike & Multi-Brand)">Senior Technician (Superbike & Multi-Brand)</option>
                <option value="Junior Technician (General Service & Repair)">Junior Technician (General Service & Repair)</option>
                <option value="Intern / Trainee Technician">Intern / Trainee Technician</option>'''

html = html.replace(old_role_opt, new_role_opts)
html = html.replace('<option value="Junior Mechanic Apprentice">Junior Mechanic Apprentice</option>', '')

# 6. Update Applicant Experience Select Dropdown
old_exp_opt = '<option value="0-1 Years">0 - 1 Years (Fresher)</option>'
new_exp_opts = '''<option value="Intern / Trainee (0 Exp)">Intern / Trainee (0 Years Exp)</option>
                <option value="0-1 Years (Fresher)">0 - 1 Years (Fresher / Trainee)</option>
                <option value="1-3 Years (Junior Technician)">1 - 3 Years (Junior Technician)</option>
                <option value="3-5 Years (Mid-Level)">3 - 5 Years (Mid-Level)</option>
                <option value="4+ Years (Senior Technician)">4+ Years (Senior Technician)</option>'''

html = html.replace(old_exp_opt, new_exp_opts)
html = html.replace('<option value="1-3 Years">1 - 3 Years</option>\n                <option value="3-5 Years">3 - 5 Years</option>\n                <option value="5+ Years">5+ Years (Master)</option>', '')

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(html)
