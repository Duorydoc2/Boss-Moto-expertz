import os

with open('careers.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read()

# Replace filter pills
old_pills = '''        <div class="pill-group" id="careerFilterGroup" style="margin:0;">
          <button type="button" class="pill-btn active" data-filter="all">All Roles</button>
          <button type="button" class="pill-btn" data-filter="tech">Mechanics & Tech</button>
          <button type="button" class="pill-btn" data-filter="ecu">ECU & Electrical</button>
          <button type="button" class="pill-btn" data-filter="service">Service & Ops</button>
          <button type="button" class="pill-btn" data-filter="custom">Paint & Modification</button>
        </div>'''

new_pills = '''        <div class="pill-group" id="careerFilterGroup" style="margin:0;">
          <button type="button" class="pill-btn active" data-filter="all">All Roles</button>
          <button type="button" class="pill-btn" data-filter="tech">Senior & Junior Tech</button>
          <button type="button" class="pill-btn" data-filter="intern">Intern / Trainee</button>
          <button type="button" class="pill-btn" data-filter="ecu">ECU & Electrical</button>
          <button type="button" class="pill-btn" data-filter="service">Service & Ops</button>
          <button type="button" class="pill-btn" data-filter="custom">Paint & Modification</button>
        </div>'''

if old_pills in html:
    html = html.replace(old_pills, new_pills)
else:
    # newline variant
    old_pills_rn = old_pills.replace('\n', '\r\n')
    new_pills_rn = new_pills.replace('\n', '\r\n')
    html = html.replace(old_pills_rn, new_pills_rn)

# Replace jobs grid
old_jobs_start = '      <div class="career-jobs-grid" id="jobsGrid">'
old_jobs_end = '      </div>\n    </div>\n  </section>'

jobs_start_idx = html.find(old_jobs_start)
jobs_end_idx = html.find(old_jobs_end, jobs_start_idx)

if jobs_start_idx == -1:
    old_jobs_end_rn = old_jobs_end.replace('\n', '\r\n')
    jobs_end_idx = html.find(old_jobs_end_rn, jobs_start_idx)
    end_len = len(old_jobs_end_rn)
else:
    end_len = len(old_jobs_end)

new_jobs_grid = '''      <div class="career-jobs-grid" id="jobsGrid">
        <!-- Job 1: Senior Technician -->
        <article class="job-card glass-card reveal" data-category="tech">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge" style="background:rgba(250,114,50,0.2);color:var(--orange);border-color:rgba(250,114,50,0.4);">Senior Role</span>
              <h3>Senior Superbike & Multi-Brand Technician</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 4+ Years Exp</span>
            <span>💰 High Pay + Incentives</span>
            <span>🔧 Superbike & Engine Overhauls</span>
          </div>
          <p class="job-desc">Lead complex engine diagnostics, cylinder head servicing, valve clearances, dyno tuning support, and precision repairs on high-cc motorcycles.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Senior Technician (Superbike & Multi-Brand)">Apply For Role</button>
          </div>
        </article>

        <!-- Job 2: Junior Technician -->
        <article class="job-card glass-card reveal reveal-delay-1" data-category="tech">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge">Full Time</span>
              <h3>Junior Motorcycle Technician</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 1-3 Years Exp</span>
            <span>💰 Salary + Skill Incentives</span>
            <span>🛠️ Maintenance & Repair</span>
          </div>
          <p class="job-desc">Perform periodic bike services, oil changes, brake overhaul, clutch cable adjustments, suspension oiling, and routine workshop repairs under senior guidance.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Junior Technician (General Service & Repair)">Apply For Role</button>
          </div>
        </article>

        <!-- Job 3: Intern / Trainee -->
        <article class="job-card glass-card reveal reveal-delay-2" data-category="intern">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge" style="background:rgba(0,210,132,0.15);color:#00d084;border-color:rgba(0,210,132,0.3);">Trainee / Intern</span>
              <h3>Intern / Trainee Mechanic</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 0-1 Yr / Freshers</span>
            <span>💰 Stipend + Training</span>
            <span>🎓 Hands-on Mentorship</span>
          </div>
          <p class="job-desc">Kickstart your career with 1-on-1 mentorship under Master Technicians. Learn diagnostic tools, basic servicing, chain lubing, and workshop protocols.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Intern / Trainee Technician">Apply For Role</button>
          </div>
        </article>

        <!-- Job 4: ECU Specialist -->
        <article class="job-card glass-card reveal reveal-delay-1" data-category="ecu">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge">Full Time</span>
              <h3>ECU Tuning & Electrical Specialist</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 3+ Years Exp</span>
            <span>💰 Premium Package</span>
            <span>💻 Dyno / ECU Remap</span>
          </div>
          <p class="job-desc">Execute ECU flashing, dyno runs, custom fuel map tuning, wire harness troubleshooting, and digital cluster installations.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="ECU Tuning & Electrical Specialist">Apply For Role</button>
          </div>
        </article>

        <!-- Job 5: Service Advisor -->
        <article class="job-card glass-card reveal reveal-delay-2" data-category="service">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge">Full Time</span>
              <h3>Service Advisor & Customer Experience Lead</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 2+ Years Exp</span>
            <span>💰 Salary + Monthly Bonus</span>
            <span>📝 Customer Relations</span>
          </div>
          <p class="job-desc">Greet riders, generate detailed digital job cards, guide customers on service packages, manage delivery schedules, and ensure 100% satisfaction.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Service Advisor & Customer Experience Lead">Apply For Role</button>
          </div>
        </article>

        <!-- Job 6: Custom Paint & Build -->
        <article class="job-card glass-card reveal reveal-delay-1" data-category="custom">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge">Full Time</span>
              <h3>Custom Build & Paint Master</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 3+ Years Exp</span>
            <span>💰 Performance Bonus</span>
            <span>🎨 Paint & Fabrication</span>
          </div>
          <p class="job-desc">Perform custom bodywork modifications, airbrush detailing, powder coating, matte/gloss ceramic painting, and cafe racer/scrambler transformations.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Custom Build & Paint Master">Apply For Role</button>
          </div>
        </article>

        <!-- Job 7: Spare Parts Manager -->
        <article class="job-card glass-card reveal reveal-delay-2" data-category="service">
          <div class="job-header">
            <div class="job-title-wrap">
              <span class="job-badge">Full Time</span>
              <h3>Spare Parts & Inventory Manager</h3>
            </div>
            <div class="job-location">📝 Coimbatore Hub</div>
          </div>
          <div class="job-meta">
            <span>⏱️ 2+ Years Exp</span>
            <span>💰 Standard Package</span>
            <span>📝 OEM Parts & Logistics</span>
          </div>
          <p class="job-desc">Manage genuine OEM spare parts inventory, vendor procurement, stock auditing, and quick dispatch for workshop bay requirements.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Spare Parts & Inventory Manager">Apply For Role</button>
          </div>
        </article>
      </div>
    </div>
  </section>'''

if jobs_start_idx != -1 and jobs_end_idx != -1:
    html = html[:jobs_start_idx] + new_jobs_grid + html[jobs_end_idx + end_len:]

# Replace Select Role Dropdown
old_role_select = '''              <select id="applicantRole" class="form-control" required style="background:var(--navy-light);color:var(--white);">
                <option value="">-- Select Job Role --</option>
                <option value="Master Superbike Technician">Master Superbike Technician</option>
                <option value="ECU Tuning & Electrical Specialist">ECU Tuning & Electrical Specialist</option>
                <option value="Service Advisor & Customer Experience Lead">Service Advisor & Customer Experience Lead</option>
                <option value="Custom Build & Paint Master">Custom Build & Paint Master</option>
                <option value="Spare Parts & Inventory Manager">Spare Parts & Inventory Manager</option>
                <option value="Junior Mechanic Apprentice">Junior Mechanic Apprentice</option>
                <option value="General Open Application">Other / Open Application</option>
              </select>'''

new_role_select = '''              <select id="applicantRole" class="form-control" required style="background:var(--navy-light);color:var(--white);">
                <option value="">-- Select Job Role --</option>
                <option value="Senior Technician (Superbike & Multi-Brand)">Senior Technician (Superbike & Multi-Brand)</option>
                <option value="Junior Technician (General Service & Repair)">Junior Technician (General Service & Repair)</option>
                <option value="Intern / Trainee Technician">Intern / Trainee Technician</option>
                <option value="ECU Tuning & Electrical Specialist">ECU Tuning & Electrical Specialist</option>
                <option value="Service Advisor & Customer Experience Lead">Service Advisor & Customer Experience Lead</option>
                <option value="Custom Build & Paint Master">Custom Build & Paint Master</option>
                <option value="Spare Parts & Inventory Manager">Spare Parts & Inventory Manager</option>
                <option value="General Open Application">Other / Open Application</option>
              </select>'''

if old_role_select in html:
    html = html.replace(old_role_select, new_role_select)
else:
    old_role_select_rn = old_role_select.replace('\n', '\r\n')
    new_role_select_rn = new_role_select.replace('\n', '\r\n')
    html = html.replace(old_role_select_rn, new_role_select_rn)

# Replace Experience Select Dropdown
old_exp_select = '''              <select id="applicantExp" class="form-control" style="background:var(--navy-light);color:var(--white);">
                <option value="0-1 Years">0 - 1 Years (Fresher)</option>
                <option value="1-3 Years">1 - 3 Years</option>
                <option value="3-5 Years">3 - 5 Years</option>
                <option value="5+ Years">5+ Years (Master)</option>
              </select>'''

new_exp_select = '''              <select id="applicantExp" class="form-control" style="background:var(--navy-light);color:var(--white);">
                <option value="Intern / Trainee (0 Exp)">Intern / Trainee (0 Years Exp)</option>
                <option value="0-1 Years (Fresher)">0 - 1 Years (Fresher / Trainee)</option>
                <option value="1-3 Years (Junior Technician)">1 - 3 Years (Junior Technician)</option>
                <option value="3-5 Years (Mid-Level)">3 - 5 Years (Mid-Level)</option>
                <option value="4+ Years (Senior Technician)">4+ Years (Senior Technician)</option>
              </select>'''

if old_exp_select in html:
    html = html.replace(old_exp_select, new_exp_select)
else:
    old_exp_select_rn = old_exp_select.replace('\n', '\r\n')
    new_exp_select_rn = new_exp_select.replace('\n', '\r\n')
    html = html.replace(old_exp_select_rn, new_exp_select_rn)

with open('careers.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
