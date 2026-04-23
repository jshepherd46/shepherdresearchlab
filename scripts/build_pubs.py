#!/usr/bin/env python3
"""
build_pubs.py — Generate RIS and BibTeX exports from _data/publications.yaml.

HTML rendering is handled by Jekyll/Liquid in `publications/index.md`, which
reads `site.data.publications` directly. This script only produces the
EndNote/Zotero (RIS) and LaTeX (BibTeX) export files, committed alongside
the data file so users can download them.

Usage:
  python3 scripts/build_pubs.py           # regenerate publications/publications.{ris,bib}
  python3 scripts/build_pubs.py --tag X   # list papers with a given tag (no write)
"""

import yaml
import os
import sys

PUBLICATIONS_FILE = "_data/publications.yaml"
OUTPUT_DIR = "publications"   # Jekyll source path — files served verbatim


def load_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def generate_ris(publications):
    """Generate RIS format for EndNote/Zotero/Mendeley import."""
    lines = []

    for pub in publications:
        if pub.get("exclude"):
            continue  # tombstoned entries — skip

        pub_type = "JOUR"
        journal = pub.get("journal", "")
        if any(word in journal.lower() for word in ["conference", "proceedings", "workshop", "symposium"]):
            pub_type = "CONF"
        elif not journal:
            pub_type = "GEN"

        lines.append(f"TY  - {pub_type}")
        lines.append(f"TI  - {pub.get('title', '')}")

        authors_str = pub.get("authors", "")
        if authors_str:
            for author in authors_str.split(","):
                author = author.strip()
                if author:
                    lines.append(f"AU  - {author}")

        if pub.get("year"):
            lines.append(f"PY  - {pub['year']}")
        if journal:
            lines.append(f"JO  - {journal}")
        if pub.get("volume"):
            lines.append(f"VL  - {pub['volume']}")
        if pub.get("pages"):
            pages = pub["pages"].replace("–", "-").replace("—", "-")
            if "-" in pages:
                sp, ep = pages.split("-", 1)
                lines.append(f"SP  - {sp.strip()}")
                lines.append(f"EP  - {ep.strip()}")
            else:
                lines.append(f"SP  - {pages}")

        doi = pub.get("doi", "")
        if doi:
            doi_clean = doi.replace("https://doi.org/", "").replace("http://dx.doi.org/", "")
            lines.append(f"DO  - {doi_clean}")
            lines.append(f"UR  - https://doi.org/{doi_clean}")

        if pub.get("abstract"):
            lines.append(f"AB  - {pub['abstract']}")

        for tag in pub.get("tags", []):
            lines.append(f"KW  - {tag}")

        lines.append("ER  - ")
        lines.append("")

    return "\n".join(lines)


def generate_bibtex(publications):
    """Generate BibTeX format."""
    entries = []

    for pub in publications:
        if pub.get("exclude"):
            continue

        key = pub.get("key", "unknown")
        year = pub.get("year", "")
        journal = pub.get("journal", "")

        if any(word in journal.lower() for word in ["conference", "proceedings", "workshop"]):
            entry_type = "inproceedings"
        elif journal:
            entry_type = "article"
        else:
            entry_type = "misc"

        fields = []
        fields.append(f'  title = {{{pub.get("title", "")}}}')
        fields.append(f'  author = {{{pub.get("authors", "")}}}')
        if year:
            fields.append(f'  year = {{{year}}}')
        if journal:
            if entry_type == "article":
                fields.append(f'  journal = {{{journal}}}')
            else:
                fields.append(f'  booktitle = {{{journal}}}')
        if pub.get("volume"):
            fields.append(f'  volume = {{{pub["volume"]}}}')
        if pub.get("pages"):
            fields.append(f'  pages = {{{pub["pages"]}}}')
        doi = pub.get("doi", "")
        if doi:
            doi_clean = doi.replace("https://doi.org/", "")
            fields.append(f'  doi = {{{doi_clean}}}')

        fields_str = ",\n".join(fields)
        entries.append(f"@{entry_type}{{{key},\n{fields_str}\n}}")

    return "\n\n".join(entries)


def main():
    # --tag lookup (no-write; prints papers matching)
    if "--tag" in sys.argv:
        idx = sys.argv.index("--tag")
        tag_filter = sys.argv[idx + 1]
        publications = load_yaml(PUBLICATIONS_FILE)
        filtered = [p for p in publications if tag_filter in p.get("tags", []) and not p.get("exclude")]
        print(f"Tag '{tag_filter}': {len(filtered)} papers")
        for p in filtered:
            print(f"  [{p.get('year','')}] {p['title'][:70]}")
        return

    publications = load_yaml(PUBLICATIONS_FILE)
    active = [p for p in publications if not p.get("exclude")]
    print(f"Loaded {len(publications)} publications ({len(active)} active, {len(publications) - len(active)} excluded).")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    ris_path = os.path.join(OUTPUT_DIR, "publications.ris")
    with open(ris_path, "w", encoding="utf-8") as f:
        f.write(generate_ris(publications))
    print(f"RIS export: {ris_path}")

    bib_path = os.path.join(OUTPUT_DIR, "publications.bib")
    with open(bib_path, "w", encoding="utf-8") as f:
        f.write(generate_bibtex(publications))
    print(f"BibTeX export: {bib_path}")

    print("\nBuild complete. Jekyll renders the HTML page from _data/publications.yaml.")


if __name__ == "__main__":
    main()
