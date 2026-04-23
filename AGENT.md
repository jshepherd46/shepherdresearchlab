# AGENT.md — SRL Publications System
## Operating Manual for the Claude Code Webmaster Agent

This file tells you everything you need to know to manage the SRL publications pipeline.
Read this before taking any action on this repository.

---

## What This Repo Does

This repository manages publications for the Shepherd Research Lab website.
It is the canonical source of truth for all publications displayed at shepherdresearchlab.org.

**The pipeline:**
1. `_data/publications.yaml` — master library of all publications with tags (Jekyll auto-loads as `site.data.publications`)
2. `tags.yaml` — the classification taxonomy (study tags, research areas, modalities, cohorts)
3. `scripts/scraper.py` — finds new papers on OpenAlex (author A5069392685 / ORCID 0000-0003-2280-2541)
4. `scripts/classify.py` — uses Claude API to propose tags for new papers
5. `scripts/merge.py` — merges approved papers into `_data/publications.yaml`
6. `scripts/build_pubs.py` — generates RIS and BibTeX exports from the library. HTML rendering of the `/publications/` page is handled by Jekyll/Liquid directly from the data file (see `publications/index.md`).

---

## Tasks You Can Do Autonomously

### Add a new publication manually
1. Open `_data/publications.yaml`
2. Add the entry following the existing schema (key, title, authors, year, journal, doi, tags)
3. Use `tags.yaml` as the tag reference — only use tags that exist there
4. Run `python3 scripts/build_pubs.py` to regenerate `publications/publications.ris` and `.bib`
5. Commit `_data/publications.yaml` + `publications/publications.ris` + `publications/publications.bib` together — the site rebuilds automatically via GitHub Pages

### Run the discovery pipeline (local)
```bash
python3 scripts/scraper.py          # find new papers (OpenAlex)
python3 scripts/classify.py         # auto-tag them (claude-sonnet-4-6)
# Review classified_papers.yaml
python3 scripts/merge.py --auto     # merge if auto-approved
python3 scripts/build_pubs.py       # rebuild site
```

### Scheduled / CI flow
Discovery runs automatically on the **1st of each month at 8am UTC** via
`.github/workflows/publications.yml`, and can be triggered manually from the
Actions tab. The workflow runs `scraper → classify → merge --auto` in the
runner, then opens a PR titled "📚 New publications — tags need review"
containing the resulting `_data/publications.yaml` diff. Review the tags in the
PR (edit inline if needed); merging triggers the site-build job.

### Check papers for a specific tag
```bash
python3 scripts/build_pubs.py --tag hipimr
python3 scripts/build_pubs.py --tag body-composition
```
(Prints matching papers; does not write files.)

### Regenerate RIS/BibTeX exports
```bash
python3 scripts/build_pubs.py
```
Writes `publications/publications.ris` and `publications/publications.bib`. The Jekyll site picks them up on the next build; commit them alongside any `_data/publications.yaml` changes so the download links stay in sync.

---

## Tasks That Require John's Approval (via Slack)

- Adding a new tag to `tags.yaml`
- Removing or renaming an existing tag
- Changing the tags on existing publications
- Removing a publication from the library
- Any changes to the build scripts themselves

**When in doubt, ask.**

---

## Tag Rules

- A paper must have at least ONE research area tag (`breast-density`, `body-composition`, etc.)
- Study tags (`hipimr`, `shape-up`, etc.) should only be applied when the paper explicitly
  uses data from or was produced by that study
- Multiple tags are encouraged — err toward more tags rather than fewer
- Never invent tags not in `tags.yaml` — add them to the taxonomy first

---

## Data Schema for _data/publications.yaml

```yaml
- key: lastname-year-shortword        # unique identifier, lowercase-hyphenated
  title: "Full paper title"
  authors: "Last F, Last F, ..."      # comma-separated, standard bibliographic format
  year: 2024                          # integer
  journal: "Journal Name"             # or conference name
  volume: "7"                         # string or empty
  pages: "298"                        # or "1-12" format
  doi: "10.1038/s41746-024-01289-0"   # without https://doi.org/ prefix
  abstract: "First 500 chars..."      # optional, truncate long abstracts
  openalex_id: "W4412712238"          # OpenAlex work ID (without https://openalex.org/ prefix)
  source_url: "https://..."           # landing page URL from OpenAlex, if available
  tags:
    - body-composition
    - dxa
    - shape-up
  added: "2025-04-21"                 # ISO date when added to library
  notes: ""                           # optional internal notes
```

---

## What NOT to Do

- Do not delete `publications_backup_*.yaml` files (kept in repo root, gitignored) for 30 days
- Do not modify `_data/publications.yaml` without running `build_pubs.py` afterward to keep the RIS/BibTeX exports in sync
- Do not push directly to main if you have unreviewed papers — open a PR instead
- Do not change the RIS or BibTeX output files directly — they are generated artifacts (regenerate with `build_pubs.py`)
- Do not add `<!-- exclude -->` style comments — use the `exclude: true` YAML field for tombstoned/misattributed entries (the Liquid template and Python exports both honor it)

---

## Environment Variables Required

- `ANTHROPIC_API_KEY` — for classify.py (set in GitHub Actions secrets)
- `GITHUB_TOKEN` — auto-provided by GitHub Actions

---

## Contact

This system is managed for John Shepherd (johnshep@hawaii.edu)
University of Hawaiʻi Cancer Center
