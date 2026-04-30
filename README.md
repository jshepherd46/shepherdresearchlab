# Shepherd Research Lab — Site Repo

Static Jekyll site for [shepherdresearchlab.org](https://shepherdresearchlab.org), hosted on GitHub Pages.

This repo houses two independent concerns that share the same home:
- **Website** (Jekyll) — source of the public site. Everything described below.
- **Publications pipeline** (Python) — monthly OpenAlex → Claude classify → YAML → HTML/RIS/BibTeX. See `AGENT.md` and `scripts/`.

The two don't interfere: Jekyll's `exclude:` in `_config.yml` keeps the pipeline's files out of the site build, and the pipeline writes its rendered HTML into `publications/` for Jekyll to serve normally.

## Migration status

Migration from WordPress is essentially complete. Remaining work is DNS cutover and a couple of asset/hosting decisions.

- ✅ **Scaffold** — Jekyll config, layouts, includes, stylesheet (UH Mānoa green)
- ✅ **Main-site content** — homepage, about, team, research, contact, join-a-study, studies, etc.
- ✅ **Publications pipeline** — wired into `/publications/`; per-tag filtered pages live at `/publications/<tag>/`
- ✅ **Blog** (Phase 5) — migrated from `blog.shepherdresearchlab.org` to `_posts/` → `/news/`
- ✅ **Body Composition Lab** (Phase 6) — `bcl.` / `bcepem.` → `/services/`, `/dxa-scan/`, `/bodpod/`, `/3d-optical-scans/`, `/bioelectrical-impedance-analysis/`, `/muscle-dynamometer/`, `/metabolic-assessment/` (orphan), `/pricing/`, `/health-safety/`, `/make-an-appointment/` (Koalendar embed), `/services/contact/`
- ✅ **AI Precision Health Institute** (Phase 7) — `aiphi.` → `/aiphi/` branded sub-section
- ✅ **HIPIMR** (Phase 8) — `hipimr.` → `/hipimr/` branded sub-section
- ✅ **Shape Up! Studies** (Phase 9) — `shapeup.` → `/shapeup/` branded sub-section
- 🟡 **Forms** — Mixed status:
  - **Mailchimp newsletter** is paused (the existing IBDW Mailchimp account is over its 2,000-contact free-tier limit, sending disabled until the list is cleaned up). Footer form still uses placeholder values.
  - **Formspree forms** (`/contact/`, `/join-a-study/`, `/shapeup/3do-bodycomp-analyzer/`) still use `YOUR_FORMSPREE_*` placeholders.
  - **AI PHI affinity-meeting registration** *is* live via Zoom recurring-meeting registration — a single URL covers the entire monthly series.
- 🟡 **3DO Body Composition Analyzer** — `/shapeup/3do-bodycomp-analyzer/` shows abstract + access-request form; the live interactive tool needs a new host (HuggingFace Space, Streamlit, internal UH server, …)
- 🟡 **Oversize sample mesh PLYs** — two ~60 MB reference files at `/shapeup/mesh-preparation/` still link to the legacy WP host; need git-lfs / external storage before WP shutdown
- ⬜ **DNS cutover** — `shepherdresearchlab.org` still points at the WordPress host; once cut over, all four WP subdomains can be retired

## Content conventions

- **URL preservation.** We match WordPress URLs where feasible. Keeping permalinks stable means existing external links (papers, partner sites, search engines) still resolve after DNS cutover.
- **Branded sub-sections.** AI PHI, HIPIMR, Shape Up!, and the BCL each retain their identity as named sub-orgs under `/aiphi/`, `/hipimr/`, `/shapeup/`, and `/services/` (BCL). News and publications are shared with the main SRL feeds — filter via tag (e.g. `/publications/ai/`, `/publications/hipimr/`, `/publications/shape-up/`, `/news/aiphi/`).
- **Recruitment is unified.** All studies are listed on `/join-a-study/` (driven by `_data/studies.yml`) with explicit Enrolling / Reopening soon / Closed status badges, active studies first. Per-study contact info is shown on each card; clicking **Learn More** scrolls to the page-bottom form and pre-fills the textarea with the study name.
- **Images live at `wp-content/uploads/YYYY/MM/`** at the repo root, mirroring WordPress's original image URLs. Reference from Markdown as `{{ site.baseurl }}/wp-content/uploads/…`.
- **Content extraction.** The old WordPress site was built with Elementor (a visual page builder), which produces nested widget markup that doesn't convert cleanly to Markdown by scraping. Pages were extracted via AI-assisted fetch and written as simple Markdown inside HTML section wrappers. See `index.html` for the pattern — each section is `<section class="section">…<div class="container" markdown="1">…Markdown…</div></section>`, alternating with `.section--alt` for visual separation.

## How to update content

### Homepage
Edit `index.md` (root).

### Inner pages
Each lives at its own path (e.g. `about/index.md`, `services/index.md`). Pages use `_layouts/default.html`. Posts use `_layouts/post.html` automatically (configured under `defaults:` in `_config.yml`).

### Sub-organization portals
- AI PHI: `aiphi/`
- HIPIMR: `hipimr/`
- Shape Up!: `shapeup/`
- BCL services: `services/` plus the modality pages at root (`/dxa-scan/` etc.)

### Team, studies, publications
Data-driven — edit YAML files in `_data/`:
- `team.yml` — drives `/about/our-team/` and (by canonical-photo convention) the headshots used on AI PHI / HIPIMR / services pages.
- `studies.yml` — drives `/join-a-study/`. Set `status: enrolling | reopening | closed` to change a study's badge and sort position; use `note:` for nuance like "expected to reopen 2026."
- `publications.yaml` — owned by the Python pipeline; do not hand-edit (see `AGENT.md`).

### News posts
Add a Markdown file to `_posts/` named `YYYY-MM-DD-slug.md`. The default layout + permalink (`/news/:slug/`) come from `_config.yml`. Add `tags: [aiphi]` (or another tag) to surface the post in a tagged subfeed (see below).

### Tagged subfeeds (news + publications)
Branded sub-orgs get filtered subfeeds without separate post stores:
- **Publications subfeeds** at `/publications/<tag>/` are auto-generated by the pipeline.
- **News subfeeds** at `/news/<tag>/` are hand-written. `/news/aiphi/index.md` is the existing example; copy its Liquid `where_exp` filter and change the tag string to spin up a new subfeed (e.g. `/news/hipimr/`).

### Navigation
Edit the `nav:` list in `_config.yml`.

### Publications
The Python pipeline owns `_data/publications.yaml`. Don't hand-edit unless tombstoning a misattribution. See `AGENT.md` for the workflow.

## Site management and contribution workflow

The site is the lab's public face, so changes should go through review before they ship. The default flow for everyone — researchers, students, and admins alike — is **branch → pull request → admin review → merge**. Direct commits to `main` should be reserved for very small fixes by admins (typo, broken link, etc.).

### Who's who

- **Site administrators** — currently **John Shepherd** and **Thomas Wolfgruber**. They have write access to `main` and approve merges. Day-to-day editorial decisions (what content goes up, what gets corrected) flow through them.
- **Contributors** — anyone in the research group with a GitHub account who wants to update content or fix something. Contributors get write access to branches but not direct write to `main`.
- **Publications pipeline** — automated, runs monthly via GitHub Actions and opens its own PR (`📚 New publications — tags need review`). Reviewing those tag-classification PRs is also an admin job. See `AGENT.md`.

### Contribution flow (researchers + students)

1. **Open an issue first** (optional but recommended for non-trivial changes) so the change is visible to the group and won't conflict with someone else's edits.

2. **Create a branch** off `main`. Pick a short, descriptive name:
   - News post: `news/google-workshop-recap`
   - Study update: `studies/tanita-eligibility-fix`
   - AI PHI page edit: `aiphi/add-june-speaker`
   - Bug fix: `fix/broken-link-services-page`

3. **Make your edits.** Most content lives in obvious places — see [How to update content](#how-to-update-content) above. Common edits:
   - News post → `_posts/YYYY-MM-DD-slug.md`
   - Study card → `_data/studies.yml`
   - Team member → `_data/team.yml`
   - Page copy → the page's `index.md` (e.g., `aiphi/index.md`, `services/index.md`)

4. **Preview locally** before opening the PR (`bundle exec jekyll serve`, then visit `http://localhost:4000/shepherdresearchlab/`). GitHub Pages does **not** build feature branches automatically, so the PR diff is what reviewers see.

5. **Open a pull request** against `main`. Write a one-line summary of the change. Tag a site administrator (`@jshepherd46`, `@thomas-wolfgruber` — or whoever the admin GitHub handles are) for review.

6. **Wait for review.** An administrator either approves and merges, or requests changes. Once merged, GitHub Pages rebuilds within about 30 seconds and the change goes live.

### For administrators: enforcing this with branch protection

The workflow above is conventional but only **enforced** if branch protection is configured. To require PR + review on every change to `main`:

1. Repo → **Settings → Branches → Branch protection rules → Add rule** (or "Add classic branch protection rule")
2. Pattern: `main`
3. Enable:
   - **Require a pull request before merging**
   - **Require approvals: 1**
   - **Dismiss stale pull request approvals when new commits are pushed** (recommended)
   - **Do not allow bypassing the above settings** (recommended; otherwise admins can override)

Without these rules, anyone with write access can still push directly. The rules are what make the workflow mandatory.

### Optional: a `CODEOWNERS` file for automatic reviewer assignment

If you want a specific person (or people) automatically requested for review based on which paths change, add `.github/CODEOWNERS`. Example:

```
# Default reviewer for everything
*                              @jshepherd46

# Publications pipeline changes
scripts/                       @jshepherd46
_data/publications.yaml        @jshepherd46
.github/workflows/             @jshepherd46

# Studies recruitment data
_data/studies.yml              @jshepherd46 @thomas-wolfgruber
```

Pair this with the branch-protection rule **Require review from Code Owners** to enforce.

## Local development

```bash
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/shepherdresearchlab/
```

## Services wired into the site

- **Newsletter** — Mailchimp embed (paused; the IBDW Mailchimp account that owns the audience is over its 2,000-contact free-tier limit and needs list cleanup before sending resumes)
- **Contact form** — Formspree (placeholder)
- **Join A Study form** — Formspree (placeholder; pre-fills via the `Learn More` buttons on each study card)
- **3DO Analyzer access request** — Formspree (placeholder)
- **Appointment booking** — [Koalendar](https://koalendar.com/) iframe at `/make-an-appointment/` (live; embed `koalendar.com/e/dxa-bodpod`)
- **AI PHI affinity-meeting registration** — Zoom recurring-meeting registration (live; single URL `https://hawaii.zoom.us/meeting/register/IXHDo0CjTPaKD12Om3ALMg` covers the whole monthly series, with Zoom emailing the join link and reminders to each registrant)

API keys / form IDs live in the embed snippets; subscribers and submissions live in the respective services, never in this repo.

## Accessibility

Targeting WCAG 2.2 AA. Currently in place:

- Skip-to-content link as the first focusable element on every page.
- `<main id="main-content" tabindex="-1">` landmark wraps page content (in `_layouts/default.html`).
- Mobile nav toggle wired up via `assets/js/main.js` (vanilla JS, no framework — the project's only JS file). Closes on Esc and on link click; updates `aria-expanded`.
- Visible 2px focus outline on form fields (~12.6:1 contrast against white).
- `scroll-padding-top: 90px` on `<html>` so anchor jumps don't hide focused content under the 80px sticky header (WCAG 2.4.11, new in 2.2).
- `<html lang="en">`, semantic landmarks, `aria-label` on logo + nav, `aria-current="page"` on the active nav item, meaningful alt text or empty alt for decorative images.

Known gaps (low priority, do not block AA):

- Hawaiian inline words (`makawalu`, `keiki`, `kakaʻako`) lack `<span lang="haw">` markup (WCAG 3.1.2 AA).
- No `prefers-reduced-motion` rules (currently no animations to gate, but worth adding before any are introduced).

Run Lighthouse → Accessibility on changed pages to catch regressions.

## Deployment

Push to `main` → GitHub Pages builds automatically.

Currently served at: `https://shepherd-lab.github.io/shepherdresearchlab/` (after the org transfer from `jshepherd46` to `shepherd-lab`).

To cut over the custom domain (Cloudflare + GitHub Pages):
1. Add a `CNAME` file to this repo containing: `shepherdresearchlab.org`
2. In GitHub repo Settings → Pages → Custom domain: enter `shepherdresearchlab.org`
3. In Cloudflare DNS for `shepherdresearchlab.org`, add A records for apex → GitHub Pages IPs (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`) and CNAME `www` → `shepherd-lab.github.io`. SSL/TLS mode: Full. Proxy: DNS-only (gray cloud) until the Let's Encrypt cert provisions, then optionally enable proxy.
4. Switch nameservers at the registrar to the two Cloudflare nameservers shown in the Cloudflare dashboard.
5. Once the GitHub Pages DNS check turns green: enable **Enforce HTTPS**, then change `_config.yml` to `url: "https://shepherdresearchlab.org"` and `baseurl: ""`.
6. Set up 301 redirects in Cloudflare for the legacy subdomains (`bcl.`, `bcepem.`, `aiphi.`, `hipimr.`, `shapeup.`, `blog.`) so external links land on the new apex paths.
