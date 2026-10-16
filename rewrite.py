import sys

with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '        <!-- RIGHT: Booking Form -->'
end_str = '        <!-- /Right -->'

new_content = '''        <!-- RIGHT: Available Services -->
        <div style="width: 100%;">
          <div class="booking-form-container reveal reveal-delay-2" style="padding: 2.5rem;">
            <h2 style="font-family: var(--font-heading); color: var(--white); font-size: 1.8rem; margin-bottom: 1rem;">Available Services</h2>
            <p style="color: var(--silver-dim); margin-bottom: 2rem; font-size: 1.05rem;">We offer a comprehensive range of motorcycle maintenance and performance services.</p>
            
            <div class="service-select-grid" style="pointer-events: none; margin-bottom: 2.5rem;">
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">🔧</div>
                <div class="sc-label">General Service</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">🔩</div>
                <div class="sc-label">Engine Repair</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">🛑</div>
                <div class="sc-label">Brake Service</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">🌀</div>
                <div class="sc-label">Suspension Work</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">💻</div>
                <div class="sc-label">ECU Tuning</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">🎨</div>
                <div class="sc-label">Custom Mod</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">🖌️</div>
                <div class="sc-label">Bike Painting</div>
              </div>
              <div class="service-select-card" style="border-color: var(--glass-border); cursor: default;">
                <div class="sc-icon">✨</div>
                <div class="sc-label">Detailing & Wash</div>
              </div>
            </div>

            <div style="background: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249,115,22,0.4); border-radius: 12px; padding: 2.5rem; text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.2);">
              <h3 style="color: var(--orange); font-family: var(--font-heading); font-size: 1.6rem; margin-bottom: 1rem;">Ready to Book?</h3>
              <p style="color: var(--silver); margin-bottom: 2rem; font-size: 1.1rem; max-width: 500px; margin-left: auto; margin-right: auto;">To book any of the above services, please contact our team directly. We'll set up your appointment instantly!</p>
              
              <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="tel:+916379929963" class="btn btn-primary" style="font-size: 1.15rem; padding: 1rem 2rem;">
                  📞 Call +91 63 799 299 63
                </a>
                <a href="https://wa.me/916379929963" target="_blank" rel="noopener" class="btn btn-outline" style="font-size: 1.15rem; padding: 1rem 2rem;">
                  💬 WhatsApp Us
                </a>
              </div>
            </div>
          </div>
        </div>
        <!-- /Right -->'''

start_idx = html.find(start_str)
end_idx = html.find(end_str) + len(end_str)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_content + html[end_idx:]

js_start = html.find('  <script>')
js_end = html.find('</body>')

if js_start != -1 and js_end != -1:
    html = html[:js_start] + '</body>' + html[js_end + 7:]

with open('booking.html', 'w', encoding='utf-8') as f:
    f.write(html)
