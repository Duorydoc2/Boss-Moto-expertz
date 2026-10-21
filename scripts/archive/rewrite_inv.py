import sys
import re

with open('investors.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. FOFO to COCO
html = html.replace('<td>FOFO</td>', '<td>COCO (Company owned and company operated)</td>')

# 2. FRANCHISE FEES to INVESTORS FEES
html = html.replace('<td><strong>FRANCHISE FEES</strong></td>', '<td><strong>INVESTORS FEES</strong></td>')

# 3. Remove rows from INTERIOR DESIGN LAYOUT to LOCATION
start_remove = '            <tr>\n              <td><strong>INTERIOR DESIGN LAYOUT</strong></td>'
end_remove = '            <tr>\n              <td><strong>LOCATION</strong></td>\n              <td>On GarageWalle</td>\n            </tr>\n'

start_idx = html.find(start_remove)
end_idx = html.find(end_remove)

if start_idx != -1 and end_idx != -1:
    end_idx += len(end_remove)
    html = html[:start_idx] + html[end_idx:]

# 4. Replace Form
form_start = '        <form id="investorForm"'
form_end = '        </form>'
new_form = '''        <div style="text-align: center;">
          <h3 style="color: var(--orange); margin-bottom: 1.5rem; font-family: var(--font-heading);">Inquiry Types</h3>
          
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2.5rem;">
            <div style="padding: 1rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center; background: rgba(255,255,255,0.05);">
              <strong style="color: var(--white);">Equity Investment / VC</strong>
            </div>
            <div style="padding: 1rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center; background: rgba(255,255,255,0.05);">
              <strong style="color: var(--white);">Angel Investor</strong>
            </div>
            <div style="padding: 1rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center; background: rgba(255,255,255,0.05);">
              <strong style="color: var(--white);">Franchise Ownership (COCO)</strong>
            </div>
            <div style="padding: 1rem; border: 1px solid var(--glass-border); border-radius: 8px; flex: 1 1 200px; text-align: center; background: rgba(255,255,255,0.05);">
              <strong style="color: var(--white);">Strategic Partnership</strong>
            </div>
          </div>
          
          <p style="color: var(--silver-dim); margin-bottom: 1.5rem;">For any of the inquiries above, please reach out to us directly:</p>
          
          <div>
            <a href="tel:+916379929963" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.15rem;">
              📞 Contact +91 63 799 299 63
            </a>
          </div>
        </div>'''

f_start_idx = html.find(form_start)
f_end_idx = html.find(form_end)

if f_start_idx != -1 and f_end_idx != -1:
    f_end_idx += len(form_end)
    html = html[:f_start_idx] + new_form + html[f_end_idx:]

with open('investors.html', 'w', encoding='utf-8') as f:
    f.write(html)
