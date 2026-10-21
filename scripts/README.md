# Boss Moto Expertz – Utility & Migration Scripts Archive

This directory contains historical one-off automation and migration scripts that were previously executed to perform batch content updates, cache-busting, asset management, and styling migrations across the website.

> **Note for Developers & Editors:**  
> These scripts are preserved for historical audit and reference only. The website is a 100% static client-side web application hosted on Vercel and does **not** require running any of these scripts during normal development, editing, or deployment.

---

### Archive Contents Summary

| Category | Scripts | Purpose |
|---|---|---|
| **Cache Busting** | `cache_bust.py`, `cache_v*.py`, `purge_cache_all.py`, `fix_cache.py` | Query-string cache busters for stylesheet & script versions. |
| **Asset Downloaders** | `download_logos.js`, `download_logos.py`, `fix_missing_logos.py` | Initial brand logo retrieval helpers. |
| **Page Updates** | `update_careers*.py`, `update_gallery*.py`, `update_service_images.py`, `rewrite_inv.py` | Batch HTML/content updates across inner pages. |
| **Theme / Design** | `set_black_silver.py`, `set_pure_black.py`, `set_sterling_chrome.py`, `add_tiranga_theme.py` | One-time CSS variable adjustments during theme iteration. |
| **Content Replacements** | `replace_emojis.py`, `replace_premium_emojis.py`, `update_more_emojis.py` | Clean unicode replacements for UI bullet points & headers. |

All scripts are archived under `scripts/archive/`.
