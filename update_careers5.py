with open('careers.html', 'r', encoding='utf-8', newline='') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'data-role="Senior Technician (Superbike & Multi-Brand)">Apply For Role</button>' in line:
        pass
    if line.strip() == '</article>' and len(new_lines) > 10 and 'Senior Technician' in ''.join(new_lines[-15:]):
        junior_card = '''
        <!-- Job 1b: Junior Technician -->
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
            <span>🛠️ Maintenance & Repair</span>
          </div>
          <p class="job-desc">Perform periodic bike services, oil changes, brake overhaul, clutch cable adjustments, suspension oiling, and routine workshop repairs under senior guidance.</p>
          <div class="job-actions">
            <button class="btn btn-outline btn-sm apply-btn" data-role="Junior Technician (General Service & Repair)">Apply For Role</button>
          </div>
        </article>
'''
        new_lines.append(junior_card)

with open('careers.html', 'w', encoding='utf-8', newline='') as f:
    f.writelines(new_lines)
