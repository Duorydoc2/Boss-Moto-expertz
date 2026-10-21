import os

with open('investors.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_mode = None

for line in lines:
    stripped = line.strip()
    
    if skip_mode == 'form':
        if stripped == '</form>':
            skip_mode = None
            new_lines.append('''        <div style="text-align: center;">
          <h3 style="color: var(--orange); margin-bottom: 1.5rem; font-family: var(--font-heading);">Inquiry Types</h3>
          
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2.5rem;">
            <div class="glass-card" style="padding: 1.2rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center;">
              <strong style="color: var(--white); font-size: 1.1rem;">Equity Investment / VC</strong>
            </div>
            <div class="glass-card" style="padding: 1.2rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center;">
              <strong style="color: var(--white); font-size: 1.1rem;">Angel Investor</strong>
            </div>
            <div class="glass-card" style="padding: 1.2rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center;">
              <strong style="color: var(--white); font-size: 1.1rem;">Franchise Ownership (COCO)</strong>
            </div>
            <div class="glass-card" style="padding: 1.2rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center;">
              <strong style="color: var(--white); font-size: 1.1rem;">Strategic Partnership</strong>
            </div>
          </div>
          
          <p style="color: var(--silver-dim); margin-bottom: 1.5rem; font-size: 1.05rem;">For any of the inquiries above, please reach out to us directly:</p>
          
          <div>
            <a href="tel:+916379929963" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.15rem;">
              📞 Contact +91 63 799 299 63
            </a>
          </div>
        </div>\n''')
        continue

    if stripped == '<!-- EXPANSION ROADMAP -->':
        new_lines.append('''  <!-- COMMERCIAL DETAILS -->
  <section class="section-py" id="commercials">
    <div class="container">
      <div class="section-header text-center reveal">
        <div class="section-label">Commercials</div>
        <h2 class="section-title">Investment Details</h2>
      </div>
      <div class="commercial-table-wrapper reveal reveal-delay-1" style="max-width:800px;margin:0 auto;background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border-radius:12px;padding:2rem;">
        <table class="commercial-table" style="width:100%;border-collapse:collapse;color:var(--white);">
          <thead>
            <tr>
              <th style="padding:1.25rem;text-align:left;border-bottom:2px solid var(--accent);color:var(--silver);">MODEL NAME</th>
              <th style="padding:1.25rem;text-align:left;border-bottom:2px solid var(--accent);color:var(--silver);">GARAGE WALLE</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>INVESTORS FEES</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">5,00,000</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>ROYALTY</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">5%</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>TENURE</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">5 Years</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>MODEL TYPE</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">COCO (Company owned and company operated)</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>HIRING SUPPORT</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">Yes</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>MARKETING & SALES</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">On Partner & On GarageWalle</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>NATIONAL LEVEL MARKETING</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">Yes</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>EXCLUSIVITY</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">Yes (5 KM)</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>REFERRAL AMOUNT</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">10% on brand fees</td>
            </tr>
            <tr>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);"><strong>SOFTWARE</strong></td>
              <td style="padding:1rem;border-bottom:1px solid rgba(255,255,255,0.1);color:var(--silver);">Yes</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <div class="section-divider"></div>

''')

    if stripped.startswith('<form id="investorForm"'):
        skip_mode = 'form'
        continue

    new_lines.append(line)

with open('investors.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
