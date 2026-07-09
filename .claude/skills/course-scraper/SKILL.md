---
name: course-scraper
description: Build a new course/CRICOS scraper for an education provider in this repo. Use when asked to "add a scraper", "scrape courses for <institution>", "continue for <institution>", or implement a new provider under its own folder. Produces the standard xlsx (driver + enriched record), <slug>_courses_update.sql, and a scrapers.json entry.
---

# Course scraper builder

Standard workflow for adding a per-institution course scraper to this repo. Every
scraper follows the same shape: **xlsx driver → scrape → SQL `UPDATE` statements +
enriched xlsx**. Only the *extraction* logic changes per site (each uses a different
page builder). Default fetch/parse stack is **Scrapling** (plain HTTP, no browser).

## 0. Before writing code — explore first

1. **Find the provider code + URL** in `unimplemented_institutions.txt` (grep the name).
   The `cricos_provider_code` (e.g. `03844J`) goes in the `provider_institution` UPDATE.
2. **Fetch the homepage / a `/courses` page** with `curl -sL -A "Mozilla/5.0" <url>` and
   list course links. Confirm each real course page has a **CRICOS course code**
   (category/landing pages don't) — only those become rows.
3. **Identify the page builder** (drives the extraction approach):
   - WPBakery/Divi → `.wpb_text_column` columns (RSB)
   - Bricks → `.brxe-accordion-nested`, `accordion-title-wrapper` + sibling `accordion-content-wrapper` (Leaders)
   - SP Page Builder (Joomla) → `sppb-addon-header` rows, bucket by heading (AIHE)
   - Elementor accordion → `<details>/<summary>` (VIE)
   - Elementor free-form → heading-bucketing over `.elementor-widget-*`, tabs via `role=tabpanel` (AIBI)
4. **Locate each field on the page**: CRICOS, duration, tuition fee(s), enrolment/material
   fee, intake dates, course description sections, entry requirements. Note where they live
   — they are NOT always on the course page (see gotchas).

## 1. Files to produce (per institution folder `<Institution Name>/`)

| File | Purpose |
|------|---------|
| `<slug>.xlsx` | Driver **and** enriched record. Input cols: `cricos, title, url`. Scraper rewrites it with all scraped fields on each run. |
| `<slug>.py` | The scraper (Scrapling). |
| `<slug>_courses_update.sql` | Output: 1 provider UPDATE + N course UPDATEs. |

Then **register in `scrapers.json`** (append an object) and **delete temp `_*.html` files**.

```json
{ "id": "kebab-name", "name": "Full Name", "scraper": "Dir/slug.py",
  "sql": "Dir/slug_courses_update.sql", "snapshot": "Dir/snapshot.json", "dir": "Dir" }
```

## 2. SQL output shape (exact column names)

```sql
-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, March, ...',        -- union of intake months, calendar order
    updated_at = NOW()
WHERE cricos_provider_code = '<PROVIDER_CODE>';

UPDATE courses SET
    course_description = '<h4>Section</h4>...',  -- sanitised HTML, ' escaped to ''
    course_duration_per_week = 78,               -- NUMBER of weeks (unquoted), or NULL
    offshore_tuition_fee = 65000,                -- INTERNATIONAL, numeric or NULL
    onshore_tuition_fee = 34270,                 -- DOMESTIC, numeric or NULL
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4>...',
    apply_form = '<url>',
    updated_at = NOW()
WHERE cricos_course_code = '<CRICOS>';
```

If a course has no reliable CRICOS, emit a comment instead of a broken UPDATE:
`-- ⚠️ Skipped (no/unreliable CRICOS course code): <title> | <url>` and leave its
xlsx `cricos` blank so the user can fill it and re-run.

## 3. Conventions & gotchas (learned the hard way)

- **Fees: `offshore` = INTERNATIONAL (higher), `onshore` = DOMESTIC (lower).** Verified
  across ACU/WSU. Store **total course fee**. If the site quotes *per year* or *per study
  period*, multiply out by duration (per-year × years; per-study-period × SP count where
  SP count = total credit points ÷ points-per-subject ÷ subjects-per-SP).
- **Fees may live on a central page**, not the course page (AIBI `/fees-and-payments/`,
  tabs Domestic/International). Match rows to courses by a normalised title.
- **Intake dates may hide in a PDF academic calendar** (Leaders) — see the
  `intake-date-source` memory. Derive months from "Term/Semester Commences" events.
  For the provider record, use the **union** of months across all courses, calendar order.
- **CRICOS label varies**: `CRICOS Course Code:` vs `CRICOS Code:` — regex must allow both:
  `CRICOS (?:Course )?Code:\s*([0-9A-Z]{5,8})`.
- **Data-quality traps**: sites copy-paste headers, so two courses can show the *same*
  CRICOS (AIBI Grad Dip IT reused Grad Dip Business's code). Trust the **xlsx cricos as
  authoritative** for such institutions; don't blindly override from the page. Flag & ask.
- **pandas reads blank cells as `NaN`** → normalise `str(v).strip().lower() in ("nan",...)`
  to `""`. Users pasting codes sometimes include stray `|`/newlines — sanitise with
  `re.search(r'[0-9A-Z]{5,8}', cell)`.
- **SQL-escape** single quotes (`'` → `''`) in every text field via `clean_html`.
- **Sanitise HTML**: page builders nest content in many empty `<div>`s that render as
  a messy block in the DB. **Flatten to minimal semantic HTML** (see `sanitise()` in
  `template_scraper.py`): unwrap wrapper `<div>`/`<span>`, turn text-only `<div>`→`<p>`,
  drop unknown tags & empty elements, keep only `p/ul/ol/li/strong/em/a/br/h5/table`,
  keep `href`. Wrap each section under `<h4>Section</h4>`.
- **Excel caps cells at 32,767 chars** — truncate long description/entry HTML to ~32,000.
- **Windows**: `python` resolves to the project `venv`; reconfigure stdout/stderr to UTF-8
  at the top of every scraper.

## 4. Stack: Scrapling (default)

Plain HTTP, no browser, synchronous. Reserve Playwright/`DynamicFetcher`/`StealthyFetcher`
only for genuinely JS-rendered or Cloudflare-protected sites. See the `scraping-stack` memory.

```python
from scrapling.fetchers import Fetcher
page = Fetcher.get(url, stealthy_headers=True)   # 200 without a browser for these sites
full_text = re.sub(r"\s+", " ", page.get_all_text())
# elements: .css(sel) / .xpath(sel, adaptive=True) / el.children / el.attrib / el.html_content / el.get_all_text()
```

Use `adaptive=True` on the selectors that anchor sections (headings/accordion titles) so the
scraper self-heals when the site is redesigned.

A copy-paste starting point lives next to this file: **`template_scraper.py`**.
Run: `python "<Institution>/<slug>.py"` (headless HTTP; no env vars needed).

## 5. Definition of done — checklist

- [ ] Every real course scraped; count of `UPDATE courses SET` == expected.
- [ ] `offshore` (international) **and** `onshore` (domestic) fees populated (or NULL with reason).
- [ ] `course_duration_per_week`, `enrolment_fee`, `materials_fee`, `apply_form` set.
- [ ] `course_description` + `entry_requirements` non-empty, clean HTML, correct course.
- [ ] Provider `intake_date` = union of course intakes; `cricos_provider_code` correct.
- [ ] Courses with no/duplicate CRICOS flagged as `-- ⚠️ Skipped`, xlsx cricos left blank.
- [ ] xlsx rewritten with the full enriched record (driver cols preserved).
- [ ] `scrapers.json` entry added; temp `_*.html`/PDF files deleted.
- [ ] Spot-check one description’s `<h4>` headers and head/tail text for leakage.
