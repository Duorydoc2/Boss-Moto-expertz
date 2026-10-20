/* Force clear cache and legacy theme switcher */
(function() {
  try {
    localStorage.clear();
    sessionStorage.clear();
    if (document.body) {
      document.body.className = document.body.className.replace(/theme-[^\s]+/g, '').trim();
    }
    const oldBar = document.querySelector('.theme-switcher-bar');
    if (oldBar) oldBar.remove();
  } catch (e) {}
})();

/* Clear any legacy theme override */
try {
  localStorage.removeItem('boss_moto_theme');
  document.body.className = document.body.className.replace(/theme-[^\s]+/g, '').trim();
} catch (e) {}

/* ============================================================

   BOSS MOTO EXPERTZ – JavaScript

   ============================================================ */



/* ─── Navbar Scroll ─────────────────────────────────────── */

(function () {

  const navbar = document.querySelector('.navbar');

  if (navbar) {

    window.addEventListener('scroll', () => {

      navbar.classList.toggle('scrolled', window.scrollY > 50);

    });

  }

})();



/* ─── Mobile Menu ────────────────────────────────────────── */

(function () {

  const toggle = document.getElementById('navToggle');

  const mobileMenu = document.getElementById('mobileMenu');

  const mobileLinks = document.querySelectorAll('#mobileMenu .nav-link, #mobileMenu .btn');



  if (!toggle || !mobileMenu) return;



  toggle.addEventListener('click', () => {

    toggle.classList.toggle('open');

    mobileMenu.classList.toggle('open');

    document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';

  });



  mobileLinks.forEach(link => {

    link.addEventListener('click', () => {

      toggle.classList.remove('open');

      mobileMenu.classList.remove('open');

      document.body.style.overflow = '';

    });

  });

})();



/* ─── Active Nav Link ────────────────────────────────────── */

(function () {

  const current = location.pathname.split('/').pop() || 'index.html';

  document.querySelectorAll('.nav-link').forEach(link => {

    const href = link.getAttribute('href');

    if (href === current || (current === '' && href === 'index.html')) {

      link.classList.add('active');

    }

  });

})();



/* ─── Hero BG Parallax / Load ────────────────────────────── */

(function () {

  const heroBg = document.querySelector('.hero-bg');

  if (heroBg) {

    setTimeout(() => heroBg.classList.add('loaded'), 100);

    window.addEventListener('scroll', () => {

      const scrolled = window.scrollY;

      heroBg.style.transform = `translateY(${scrolled * 0.3}px) scale(1)`;

    });

  }

})();



/* ─── Scroll Reveal ──────────────────────────────────────── */

(function () {

  const reveals = document.querySelectorAll('.reveal');

  if (!reveals.length) return;



  const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

      if (entry.isIntersecting) {

        entry.target.classList.add('visible');

        observer.unobserve(entry.target);

      }

    });

  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });



  reveals.forEach(el => observer.observe(el));

})();



/* ─── Counter Animation ──────────────────────────────────── */

(function () {

  const counters = document.querySelectorAll('[data-count]');

  if (!counters.length) return;



  const animate = (el, target, suffix) => {

    let current = 0;

    const step = target / 60;

    const timer = setInterval(() => {

      current += step;

      if (current >= target) { current = target; clearInterval(timer); }

      el.textContent = Math.floor(current) + suffix;

    }, 25);

  };



  const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

      if (entry.isIntersecting) {

        const el = entry.target;

        const target = parseInt(el.dataset.count);

        const suffix = el.dataset.suffix || '';

        animate(el, target, suffix);

        observer.unobserve(el);

      }

    });

  }, { threshold: 0.5 });



  counters.forEach(el => observer.observe(el));

})();



/* ─── Gallery Filter ─────────────────────────────────────── */

(function () {

  const filters = document.querySelectorAll('.filter-btn');

  const items = document.querySelectorAll('.masonry-item');

  if (!filters.length) return;



  filters.forEach(btn => {

    btn.addEventListener('click', () => {

      filters.forEach(b => b.classList.remove('active'));

      btn.classList.add('active');

      const cat = btn.dataset.filter;



      items.forEach(item => {

        const match = cat === 'all' || item.dataset.category === cat;

        item.style.display = match ? 'block' : 'none';

      });

    });

  });

})();



/* ─── Lightbox ───────────────────────────────────────────── */

(function () {

  const lightbox = document.getElementById('lightbox');

  if (!lightbox) return;



  const lbImg = lightbox.querySelector('img');

  const lbClose = lightbox.querySelector('.lightbox-close');



  document.querySelectorAll('.masonry-item').forEach(item => {

    item.addEventListener('click', () => {

      const img = item.querySelector('img');

      if (img && lbImg) {

        lbImg.src = img.src;

        lightbox.classList.add('open');

        document.body.style.overflow = 'hidden';

      }

    });

  });



  const closeLightbox = () => {

    lightbox.classList.remove('open');

    document.body.style.overflow = '';

  };



  if (lbClose) lbClose.addEventListener('click', closeLightbox);

  lightbox.addEventListener('click', (e) => {

    if (e.target === lightbox) closeLightbox();

  });

  document.addEventListener('keydown', (e) => {

    if (e.key === 'Escape') closeLightbox();

  });

})();



/* ─── Booking Form ───────────────────────────────────────── */

(function () {

  const form = document.getElementById('bookingForm');

  if (!form) return;



  form.addEventListener('submit', (e) => {

    e.preventDefault();

    const btn = form.querySelector('.form-submit');

    const original = btn.textContent;

    btn.textContent = 'Sending...';

    btn.disabled = true;



    setTimeout(() => {

      form.style.display = 'none';

      const success = document.querySelector('.booking-success');

      if (success) success.style.display = 'block';

    }, 1200);

  });

})();



/* ─── Back to Top ────────────────────────────────────────── */

(function () {

  const btn = document.getElementById('backToTop');

  if (!btn) return;



  window.addEventListener('scroll', () => {

    btn.classList.toggle('visible', window.scrollY > 400);

  });



  btn.addEventListener('click', () => {

    window.scrollTo({ top: 0, behavior: 'smooth' });

  });

})();



/* ─── Smooth Hover Tilt (why-cards) ─────────────────────── */

(function () {

  document.querySelectorAll('.why-card, .service-card, .testimonial-card').forEach(card => {

    card.addEventListener('mousemove', (e) => {

      const rect = card.getBoundingClientRect();

      const x = e.clientX - rect.left;

      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;

      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -4;

      const rotateY = ((x - centerX) / centerX) * 4;

      card.style.transform = `perspective(600px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;

    });

    card.addEventListener('mouseleave', () => {

      card.style.transform = '';

    });

  });

})();



/* ─── 3D Hero Background Slider & Interactive Stage ────────── */

(function () {

  const slides = document.querySelectorAll('.hero-3d-slide');

  const cards = document.querySelectorAll('.hero-3d-card');

  const dots = document.querySelectorAll('.stage-indicators .dot');

  const prevBtn = document.getElementById('stagePrev');

  const nextBtn = document.getElementById('stageNext');

  const stage = document.getElementById('hero3dStage');

  

  if (!slides.length || !cards.length) return;



  let currentIndex = 0;

  let autoTimer = null;



  function setSlide(index) {

    currentIndex = (index + slides.length) % slides.length;



    slides.forEach((slide, i) => {

      slide.classList.toggle('active', i === currentIndex);

    });



    cards.forEach((card, i) => {

      card.classList.toggle('active', i === currentIndex);

    });



    dots.forEach((dot, i) => {

      dot.classList.toggle('active', i === currentIndex);

    });

  }



  function startAuto() {

    stopAuto();

    autoTimer = setInterval(() => {

      setSlide(currentIndex + 1);

    }, 4500);

  }



  function stopAuto() {

    if (autoTimer) clearInterval(autoTimer);

  }



  cards.forEach((card, i) => {

    card.addEventListener('click', () => {

      setSlide(i);

      startAuto();

    });

  });



  dots.forEach((dot, i) => {

    dot.addEventListener('click', () => {

      setSlide(i);

      startAuto();

    });

  });



  if (prevBtn) {

    prevBtn.addEventListener('click', () => {

      setSlide(currentIndex - 1);

      startAuto();

    });

  }



  if (nextBtn) {

    nextBtn.addEventListener('click', () => {

      setSlide(currentIndex + 1);

      startAuto();

    });

  }



  // 3D Parallax Mouse Tracking on Stage

  if (stage) {

    stage.addEventListener('mousemove', (e) => {

      const rect = stage.getBoundingClientRect();

      const x = e.clientX - rect.left - rect.width / 2;

      const y = e.clientY - rect.top - rect.height / 2;

      const rotY = (x / rect.width) * 15;

      const rotX = -(y / rect.height) * 15;

      const activeCard = stage.querySelector('.hero-3d-card.active');

      if (activeCard) {

        activeCard.style.transform = `rotateY(${rotY}deg) rotateX(${rotX}deg) translateZ(20px) scale(1.03)`;

      }

    });



    stage.addEventListener('mouseleave', () => {

      const activeCard = stage.querySelector('.hero-3d-card.active');

      if (activeCard) {

        activeCard.style.transform = '';

      }

    });

  }



  startAuto();

})();



/* ─── Interactive Quick Estimator ────────────────────────── */

(function () {

  const categoryBtns = document.querySelectorAll('#bikeCategoryGroup .pill-btn');

  const packageBtns = document.querySelectorAll('#servicePackageGroup .pill-btn');

  const estBikeTitle = document.getElementById('estBikeTitle');

  const estPackageTitle = document.getElementById('estPackageTitle');

  const estPriceRange = document.getElementById('estPriceRange');

  const estTime = document.getElementById('estTime');

  const estChecklist = document.getElementById('estChecklist');



  if (!categoryBtns.length || !packageBtns.length) return;



  const categoryData = {

    moped: { name: 'Moped & Light Scooter (70–110cc)', priceMult: 0.75, generalTime: 'Up to 3 Hours' },

    commuter: { name: 'Commuter Motorcycle (110–150cc)', priceMult: 1.0, generalTime: 'Up to 3 Hours' },

    performance: { name: 'Sport & Executive (150–250cc)', priceMult: 1.35, generalTime: 'Up to 3 Hours' },

    classic: { name: 'Classic & Mid-Capacity (250–500cc)', priceMult: 1.65, generalTime: '3 – 4 Hours' },

    superbike: { name: 'Superbike & Multi-Cylinder (500–1300cc+)', priceMult: 2.5, generalTime: '4 – 6 Hours' }

  };



  const packageData = {

    general: {

      name: 'Adjustment & Lubing',

      basePrice: 1499,

      maxPrice: 2499,

      baseTime: 'Up to 3 Hours',

      items: [

        '✓ Premium Oil & Filter Replacement',

        '✓ 40-Point Mechanical & Electrical Safety Audit',

        '✓ Brake Pad Inspection & Fluid Top-up',

        '✓ Drive Chain Cleaning, Tensioning & Lube',

        '✓ Complimentary Foam Wash & Polish'

      ]

    },

    engine: {

      name: 'Engine Tune-Up & Overhaul',

      basePrice: 3999,

      maxPrice: 8999,

      baseTime: '1 – 2 Days',

      items: [

        '✓ Engine Compression & Cylinder Pressure Diagnostic',

        '✓ Valve Clearance Shim Adjustment / Tappet Setting',

        '✓ Spark Plug & Carburetor/Injector Cleaning',

        '✓ Clutch Plate & Friction Disc Inspection',

        '✓ Engine Flush & High Performance Oil Refill'

      ]

    },

    ecu: {

      name: 'ECU Remapping & Dyno Tuning',

      basePrice: 5999,

      maxPrice: 12999,

      baseTime: '4 – 8 Hours',

      items: [

        '✓ Custom Fuel & Spark Ignition Map Calibration',

        '✓ Throttle Response & Speed Limiter Optimization',

        '✓ Quickshifter & Auto-Blipper Setup',

        '✓ Pre & Post Dyno Wheel Horsepower Printout',

        '✓ Air-Fuel Ratio (AFR) Sensor Calibration'

      ]

    },

    custom: {

      name: 'Full Custom Build & Paint',

      basePrice: 14999,

      maxPrice: 49999,

      baseTime: '7 – 14 Days',

      items: [

        '✓ 3D Concept Design & Chassis Frame Modification',

        '✓ Handcrafted Tank, Seat & Fender Fabrications',

        '✓ 3-Coat Metallic / Matte Custom Paint Job',

        '✓ Custom Performance Exhaust & Filter Upgrade',

        '✓ Full Vehicle Wiring & LED Lighting Conversion'

      ]

    }

  };



  let activeCategory = 'commuter';

  let activePackage = 'general';



  function updateEstimate() {

    const cat = categoryData[activeCategory];

    const pkg = packageData[activePackage];



    if (!cat || !pkg) return;



    const minP = Math.round(pkg.basePrice * cat.priceMult);

    const maxP = Math.round(pkg.maxPrice * cat.priceMult);



    if (estBikeTitle) estBikeTitle.textContent = cat.name;

    if (estPackageTitle) estPackageTitle.textContent = pkg.name;

    if (estPriceRange) estPriceRange.textContent = 'Based on vehicle condition';

    if (estTime) estTime.textContent = activePackage === 'general' ? cat.generalTime : pkg.baseTime;



    if (estChecklist) {

      estChecklist.innerHTML = pkg.items.map(item => `<li>${item}</li>`).join('');

    }

  }



  categoryBtns.forEach(btn => {

    btn.addEventListener('click', () => {

      categoryBtns.forEach(b => b.classList.remove('active'));

      btn.classList.add('active');

      activeCategory = btn.dataset.category;

      updateEstimate();

    });

  });



  packageBtns.forEach(btn => {

    btn.addEventListener('click', () => {

      packageBtns.forEach(b => b.classList.remove('active'));

      btn.classList.add('active');

      activePackage = btn.dataset.package;

      updateEstimate();

    });

  });



  updateEstimate();

})();



/* ─── Advanced Interactive Service Search Engine ────────── */

(function () {

  const searchInput = document.getElementById('serviceSearchInput');

  if (!searchInput) return;



  const searchBox = searchInput.closest('.service-search-box');

  const clearBtn = document.getElementById('searchClearBtn');

  const dropdown = document.getElementById('serviceSearchDropdown');

  const statusContainer = document.getElementById('searchResultsStatus');

  const noResultsContainer = document.getElementById('searchNoResults');

  const pillBtns = document.querySelectorAll('.search-pill-btn');

  

  const cards = Array.from(document.querySelectorAll('.service-detail-card'));

  const sections = document.querySelectorAll('.service-cat-section');



  // Build searchable index of all service cards

  const servicesIndex = cards.map((card, idx) => {

    card.id = card.id || `service-card-${idx}`;

    const title = card.querySelector('h4') ? card.querySelector('h4').textContent.trim() : '';

    const desc = card.querySelector('p') ? card.querySelector('p').textContent.trim() : '';

    const icon = card.querySelector('.icon') ? card.querySelector('.icon').textContent.trim() : '🔧';

    const price = card.querySelector('.price') ? card.querySelector('.price').textContent.trim() : '';

    const section = card.closest('.service-cat-section');

    const catName = section && section.querySelector('h2') ? section.querySelector('h2').textContent.replace(/Category \d+\s*[-:]?\s*/, '').trim() : 'Service';

    const text = (title + ' ' + desc + ' ' + catName).toLowerCase();

    

    return { element: card, section, title, desc, icon, price, catName, text };

  });



  function performSearch(queryText, showDropdown = true) {

    const query = queryText.toLowerCase().trim();



    // Toggle clear button

    if (clearBtn) {

      clearBtn.style.display = query.length > 0 ? 'flex' : 'none';

    }



    if (query === '') {

      // Reset everything

      cards.forEach(card => card.style.display = 'flex');

      sections.forEach(sec => sec.style.display = 'block');

      if (dropdown) dropdown.style.display = 'none';

      if (statusContainer) statusContainer.style.display = 'none';

      if (noResultsContainer) noResultsContainer.style.display = 'none';

      return;

    }



    let matchCount = 0;

    const matchingServices = [];



    servicesIndex.forEach(item => {

      if (item.text.includes(query)) {

        item.element.style.display = 'flex';

        matchCount++;

        matchingServices.push(item);

      } else {

        item.element.style.display = 'none';

      }

    });



    // Toggle category sections

    sections.forEach(sec => {

      const visible = sec.querySelectorAll('.service-detail-card[style*="display: flex"], .service-detail-card:not([style*="display: none"])');

      sec.style.display = visible.length > 0 ? 'block' : 'none';

    });



    // Handle Status Bar & Empty State

    if (statusContainer) {

      if (matchCount > 0) {

        statusContainer.style.display = 'flex';

        statusContainer.innerHTML = `

          <span>Showing ${matchCount} service${matchCount > 1 ? 's' : ''} matching "${queryText}"</span>

          <button type="button" class="search-pill-btn" onclick="document.getElementById('serviceSearchInput').value=''; document.getElementById('serviceSearchInput').dispatchEvent(new Event('input'));">Clear Filter ✕</button>

        `;

      } else {

        statusContainer.style.display = 'none';

      }

    }



    if (noResultsContainer) {

      if (matchCount === 0) {

        noResultsContainer.style.display = 'block';

        noResultsContainer.innerHTML = `

          <h3>🔍 No services matching "${queryText}"</h3>

          <p>Try searching for a different keyword or explore our popular categories below.</p>

          <div style="display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap;">

            <button type="button" class="btn btn-primary btn-sm" onclick="document.getElementById('serviceSearchInput').value=''; document.getElementById('serviceSearchInput').dispatchEvent(new Event('input'));">Reset All Filters</button>

            <a href="booking.html" class="btn btn-outline btn-sm">Ask Custom Quote</a>

          </div>

        `;

      } else {

        noResultsContainer.style.display = 'none';

      }

    }



    // Render Dropdown Suggestions Popup

    if (dropdown && showDropdown) {

      if (matchingServices.length > 0 && query.length > 0) {

        dropdown.style.display = 'block';

        dropdown.innerHTML = matchingServices.slice(0, 5).map(item => `

          <div class="dropdown-item" data-card-id="${item.element.id}">

            <div class="dropdown-item-left">

              <span class="dropdown-item-icon">${item.icon}</span>

              <div>

                <div class="dropdown-item-title">${item.title}</div>

                <div class="dropdown-item-cat">${item.catName}</div>

              </div>

            </div>

            <span class="dropdown-item-price">${item.price}</span>

          </div>

        `).join('');



        // Dropdown item click handler

        dropdown.querySelectorAll('.dropdown-item').forEach(itemEl => {

          itemEl.addEventListener('click', () => {

            const targetId = itemEl.dataset.cardId;

            const targetCard = document.getElementById(targetId);

            if (targetCard) {

              dropdown.style.display = 'none';

              targetCard.scrollIntoView({ behavior: 'smooth', block: 'center' });

              targetCard.classList.add('highlight-card');

              setTimeout(() => targetCard.classList.remove('highlight-card'), 2500);

            }

          });

        });

      } else {

        dropdown.style.display = 'none';

      }

    }

  }



  // Input listener

  searchInput.addEventListener('input', (e) => {

    performSearch(e.target.value, true);

  });



  // Enter key press auto-scrolls to first matching card

  searchInput.addEventListener('keydown', (e) => {

    if (e.key === 'Enter') {

      e.preventDefault();

      const firstVisible = document.querySelector('.service-detail-card[style*="display: flex"], .service-detail-card:not([style*="display: none"])');

      if (dropdown) dropdown.style.display = 'none';

      if (firstVisible) {

        firstVisible.scrollIntoView({ behavior: 'smooth', block: 'center' });

        firstVisible.classList.add('highlight-card');

        setTimeout(() => firstVisible.classList.remove('highlight-card'), 2500);

      }

    } else if (e.key === 'Escape') {

      if (dropdown) dropdown.style.display = 'none';

    }

  });



  // Clear button click handler

  if (clearBtn) {

    clearBtn.addEventListener('click', () => {

      searchInput.value = '';

      performSearch('', false);

      searchInput.focus();

    });

  }



  // Popular search pill buttons click handler

  pillBtns.forEach(pill => {

    pill.addEventListener('click', () => {

      const term = pill.dataset.search || pill.textContent.trim();

      searchInput.value = term;

      performSearch(term, true);

      searchInput.focus();

    });

  });



  // Close dropdown when clicking outside

  document.addEventListener('click', (e) => {

    if (dropdown && !searchBox.contains(e.target)) {

      dropdown.style.display = 'none';

    }

  });

})();









