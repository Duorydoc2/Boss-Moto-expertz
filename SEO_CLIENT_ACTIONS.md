# Client Action Items & Approval Guide: Boss Moto Expertz

**Target Audience:** Business Owner / Marketing Lead / Website Administrator  
**Date:** 2026-10-20  
**Project:** Boss Moto Expertz Technical SEO Rollout  

---

## 1. What You Need to Test & Approve Before Publishing

Before authorizing a deployment to production on Vercel, please review the local site running at `http://localhost:3000` (or local preview) and verify the following:

- [ ] **Workshop Hours Display:** Confirm all page footers show `Mon – Sat: 9:00 AM – 7:00 PM` and `Sunday: Based on Appointment`.
- [ ] **Contact Page Schedule:** Verify the table on [contact.html](file:///c:/Users/gurus/Boss-Moto-expertz/contact.html) displays `Based on Appointment` for Sunday and Public Holidays.
- [ ] **Team Profile Section:** Review [about.html](file:///c:/Users/gurus/Boss-Moto-expertz/about.html) to confirm team avatars show high-resolution specialist portraits with role titles (Founder & CEO, Engine Specialist, ECU & Electrical Expert, Custom Build & Paint) and that personal names have been removed.
- [ ] **Customer FAQs:** Check the interactive FAQ section near the bottom of [services.html](file:///c:/Users/gurus/Boss-Moto-expertz/services.html) and verify all answers match your workshop policies.
- [ ] **Mobile Experience:** Open the website on your smartphone and verify smooth menu navigation, button clicks, and quotation estimator functionality.

---

## 2. Immediate Client Confirmations Required

Please confirm these two specific data points so we can finalize code parameters:

1. **Exact Production Domain:**
   - *Current Code Baseline:* `https://bossmotoexpertz.com/`
   - *Question:* Is your live domain `bossmotoexpertz.com`, `bossmotoexpertz.in`, or a specific Vercel URL (e.g. `boss-moto-expertz.vercel.app`)?
   - *Action:* If different, let us know and we will update `sitemap.xml`, `robots.txt`, and canonical tags instantly before pushing.
2. **Postal Code (PIN Code):**
   - *Current Address:* `42, Amarar Jeeva Main Road, Nalvar Layout, Coimbatore, Tamil Nadu`
   - *Question:* What is the official 6-digit postal code (e.g. `641012`)? Once confirmed, we will add it to the structured data schema.

---

## 3. External Actions Requiring Client Authorization

The following tasks cannot be completed automatically inside the code and require your account access or physical business verification:

### Action 1: Google Business Profile (GBP) Ownership
- **Why it matters:** GBP is the #1 ranking factor for local searches like "bike service near me" and the Google Maps local 3-pack.
- **Steps:**
  1. Visit [google.com/business](https://www.google.com/business/) and sign in with your official business Google account.
  2. Search for `Boss Moto Expertz` or click "Add business".
  3. Enter the exact verified business name: `Boss Moto Expertz`.
  4. Select Primary Category: **Motorcycle repair shop**.
  5. Add Secondary Categories: **Motorcycle shop**, **Motorsports store**.
  6. Enter the physical address: `42, Amarar Jeeva Main Road, Nalvar Layout, Coimbatore, Tamil Nadu`. Place the map marker directly on your workshop entrance.
  7. Add verified phone: `+91 63 799 299 63`.
  8. Complete Google's verification method (video of workshop signage/tools, or phone/SMS code).

### Action 2: Google Search Console (GSC) Setup
- **Why it matters:** GSC informs Google about all your site pages, checks index status, and reports organic search queries and clicks.
- **Steps:**
  1. Go to [search.google.com/search-console](https://search.google.com/search-console).
  2. Add your property (Domain or URL Prefix).
  3. Verify ownership via DNS TXT record or HTML meta tag in Vercel.
  4. Navigate to **Sitemaps** in the left menu and submit: `sitemap.xml`.

### Action 3: Review Collection Protocol
- **Why it matters:** High-rating authentic customer reviews dramatically improve local rankings in Coimbatore.
- **Steps:**
  1. Once your GBP listing is verified, copy your short review link from the Google Business Profile dashboard.
  2. Generate a free QR code pointing to that review link.
  3. Print a clean, branded QR code standee for your billing desk: *"Loved our work? Leave Boss Moto Expertz a quick Google Review!"*
  4. Send a polite WhatsApp message with the link to clients 24 hours after bike collection.

### Action 4: Claim Local Directory Citations
- **Why it matters:** High-authority local business citations build geographic trust with search engines.
- **Steps:**
  1. **Justdial:** Claim your business listing under "Two Wheeler Repair & Services" in Coimbatore. Ensure Name, Address, and Phone match the website exactly.
  2. **Sulekha:** Create a verified listing for Boss Moto Expertz.
  3. **IndiaMART:** Create a verified listing under automotive custom fabrication & bike repair services.

---

## 4. Deployment Approval Sign-off

When you are ready to publish these changes to production:

1. Confirm the production domain.
2. Provide sign-off to push the Git commit to the repository's `main` branch.
3. Vercel will automatically trigger a clean production deployment.
