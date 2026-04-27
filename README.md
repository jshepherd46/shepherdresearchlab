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
- 🟡 **Forms** — Mailchimp + Formspree placeholders still need real account / form IDs (search for `YOUR_FORMSPREE_*` and the Mailchimp embed snippet)
- 🟡 **3DO Body Composition Analyzer** — `/shapeup/3do-bodycomp-analyzer/` shows abstract + access-request form; the live interactive tool needs a new host (HuggingFace Space, Streamlit, internal UH server, …)
- 🟡 **Oversize sample mesh PLYs** — two ~60 MB reference files at `/shapeup/mesh-preparation/` still link to the legacy WP host; need git-lfs / external storage before WP shutdown
- ⬜ **DNS cutover** — `shepherdresearchlab.org` still points at the WordPress host; once cut over, all four WP subdomains can be retired

## Content conventions

- **URL preservation.** We match WordPress URLs where feasible. Keeping permalinks stable means existing external links (papers, partner sites, search engines) still resolve after DNS cutover.
- **Branded sub-sections.** AI PHI, HIPIMR, Shape Up!, and the BCL each retain their identity as named sub-orgs under `/aiphi/`, `/hipimr/`, `/shapeup/`, and `/services/` (BCL). News and publications are shared with the main SRL feeds — filter via tag (e.g. `/publications/ai/`, `/publications/hipimr/`, `/publications/shape-up/`).
- **Recruitment is unified.** Open studies live on `/join-a-study/` (currently Shape Up! Keiki, Samsung 2026, Makawalu, Tanita), not on per-study sub-pages.
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

### Team, sponsors, etc.
Data-driven — edit YAML files in `_data/` (`team.yml`, `publications.yaml`).

### News posts
Add a Markdown file to `_posts/` named `YYYY-MM-DD-slug.md`. The default layout + permalink (`/news/:slug/`) come from `_config.yml`.

### Navigation
Edit the `nav:` list in `_config.yml`.

### Publications
The Python pipeline owns `_data/publications.yaml`. Don't hand-edit unless tombstoning a misattribution. See `AGENT.md` for the workflow.

## Local development

```bash
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/shepherdresearchlab/
```

## Services wired into the site

- **Newsletter** — Mailchimp embed (placeholder until a real account ID is wired)
- **Contact form** — Formspree (placeholder)
- **Join A Study form** — Formspree (placeholder)
- **3DO Analyzer access request** — Formspree (placeholder)
- **Appointment booking** — [Koalendar](https://koalendar.com/) iframe at `/make-an-appointment/` (live; embed `koalendar.com/e/dxa-bodpod`)

API keys / form IDs live in the embed snippets; subscribers and submissions live in the respective services, never in this repo.

## Deployment

Push to `main` → GitHub Pages builds automatically.

Currently served at: `https://jshepherd46.github.io/shepherdresearchlab/`

To cut over the custom domain:
1. Add a `CNAME` file to this repo containing: `shepherdresearchlab.org`
2. In GitHub repo Settings → Pages → Custom domain: enter `shepherdresearchlab.org`
3. Update DNS at the registrar: CNAME `www` → `jshepherd46.github.io`; A records for apex → GitHub Pages IPs (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`)
4. Set up 301 redirects on the legacy WP host(s) so external links to the four subdomains (`bcl.`, `aiphi.`, `hipimr.`, `shapeup.`) land on the new apex paths before the WP install is retired. A scheduled audit agent will sweep the BCL subdomain on 2026-06-08 to flag missing redirects.
