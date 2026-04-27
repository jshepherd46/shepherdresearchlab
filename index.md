---
layout: default
description: "Shepherd Research Lab at the University of Hawaiʻi Cancer Center — innovation in computational imaging, breast cancer risk, body composition, and AI-assisted diagnosis."
og_image: /assets/images/hero-bg.jpg
---

<!-- HERO -->
<section class="hero">
<div class="hero__bg" aria-hidden="true"></div>
<div class="container">
<div class="hero__content">
<div class="hero__workshop-badge">
University of Hawaiʻi Cancer Center
</div>
<h1>Bridging computational imaging and <span>cancer research</span></h1>
<p class="hero__desc">The Shepherd Research Lab develops quantitative imaging, body-composition, and AI-assisted methods for earlier cancer detection and better metabolic-risk prediction — grounded in real studies, serving the community.</p>
<div class="hero__actions">
<a href="{{ site.baseurl }}/research/" class="btn btn-primary">Our Research</a>
<a href="{{ site.baseurl }}/join-a-study/" class="btn btn-outline">Join A Study</a>
<a href="{{ site.baseurl }}/publications/" class="btn btn-outline">Publications</a>
</div>
</div>
</div>
</section>

<!-- ALOHA / INTRO -->
<section class="section">
<div class="container" markdown="1" style="max-width: 760px;">

## Aloha

At SRL, we are a group of research scientists innovating the ways we detect cancer and metabolic risk. Along with how this benefits all areas of health, we are especially proud of the benefits our studies can bring to our local community on Oʻahu.

The lab is led by **[Dr. John A. Shepherd](https://www.uhcancercenter.org/shepherd-john)** at the University of Hawaiʻi Cancer Center, with studies spanning breast cancer detection through breast density, metabolic risk prediction through body-composition analysis, and deep learning for AI-assisted diagnosis.

</div>
</section>

<!-- RESEARCH AREAS -->
<section class="section section--alt">
<div class="container">
<div style="text-align:center; max-width: 640px; margin: 0 auto 3rem;">
<h2 style="margin-bottom: 0.75rem;">Research Areas</h2>
<p style="color: var(--gray-500);">Three linked research threads. Imaging grounds the methods, body analysis bridges the biology, and AI lifts the diagnostics.</p>
</div>
<div class="features-grid">
<a href="{{ site.baseurl }}/research/cancer/" class="feature-card" style="text-decoration:none; color:inherit;">
<div class="feature-card__icon">
<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
</div>
<h3>Cancer</h3>
<p>Breast cancer detection and risk assessment through quantitative imaging and breast density analysis.</p>
</a>
<a href="{{ site.baseurl }}/research/body-composition/" class="feature-card" style="text-decoration:none; color:inherit;">
<div class="feature-card__icon">
<svg viewBox="0 0 24 24"><circle cx="12" cy="5" r="3"/><path d="M12 8v6M8 14h8M9 14l-2 8M15 14l2 8"/></svg>
</div>
<h3>Body Composition</h3>
<p>3D body scans and body-composition analysis to predict metabolic health status and chronic disease risk.</p>
</a>
<a href="{{ site.baseurl }}/research/ai/" class="feature-card" style="text-decoration:none; color:inherit;">
<div class="feature-card__icon">
<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h.01M15 9h.01M9 15h6"/></svg>
</div>
<h3>AI for Health</h3>
<p>Deep learning for AI-assisted diagnosis, tissue classification, and novel biomarker discovery.</p>
</a>
</div>
</div>
</section>

<!-- VISIT THE LAB (Body Composition Lab CTA) -->
<section class="section">
<div class="container">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; align-items: center;">
<img src="{{ site.baseurl }}/wp-content/uploads/2020/01/dxa_1920x900-1024x480.png" alt="A participant lying on a DXA scanner table during a body-composition scan at the Body Composition Lab" style="width: 100%; border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
<div markdown="1">

<div style="font-size: 0.8rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Visit the Lab</div>

## Body Composition Lab

The lab operates the **Body Composition Lab (BCEPEM)** — a core facility at the UH Cancer Center offering DXA, Bod Pod, 3D optical scans, BIA, and muscle dynamometry to researchers and the community.

[Make an appointment]({{ site.baseurl }}/make-an-appointment/){: .btn .btn-primary style="margin-top: 0.5rem;"}
[Services &amp; pricing]({{ site.baseurl }}/services/){: .btn .btn-outline-primary style="margin-top: 0.5rem;"}

</div>
</div>
</div>
</section>

<!-- LATEST NEWS -->
<section class="section section--alt">
<div class="container">
<div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;">
<h2 style="margin: 0;">Latest News</h2>
<a href="{{ site.baseurl }}/news/" style="color: var(--primary); font-weight: 600; text-decoration: none;">All news →</a>
</div>
<div class="features-grid">
{% assign latest_posts = site.posts | slice: 0, 3 %}
{% for post in latest_posts %}
<a href="{{ post.url | relative_url }}" class="feature-card" style="padding: 0; overflow: hidden; text-decoration: none; color: inherit;">
{% if post.thumbnail %}
<img src="{{ site.baseurl }}{{ post.thumbnail }}" alt="" style="width: 100%; aspect-ratio: 16/9; object-fit: cover;">
{% endif %}
<div style="padding: 1.25rem 1.5rem;">
<p style="font-size: 0.75rem; color: var(--gray-500); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; margin-bottom: 0.5rem;">{{ post.date | date: "%b %-d, %Y" }}</p>
<h3 style="font-size: 1rem; margin-bottom: 0.5rem;">{{ post.title }}</h3>
<p style="font-size: 0.9rem; color: var(--gray-700);">{{ post.excerpt | strip_html | truncate: 140 }}</p>
</div>
</a>
{% endfor %}
</div>
</div>
</section>

<!-- FEATURED RESEARCH -->
<section class="section">
<div class="container">
<div style="text-align:center; margin-bottom: 2.5rem;">
<div style="font-size: 0.8rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Featured Research</div>
<h2>Three-Compartment Breast Lesion Detection</h2>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; align-items: center;">
<img src="{{ site.baseurl }}/wp-content/uploads/2022/03/Leong_commmed_fig2.png" alt="ROC curves showing improved cancer detection performance when adding 3CB compositional information to CAD" style="width:100%; border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
<div markdown="1">

Leong LT, Malkov S, Drukker K, Niell BL, Sadowski P, Wolfgruber T, et al. *Dual-energy three-compartment breast imaging for compositional biomarkers to improve detection of malignant lesions.* **Communications Medicine.** 2021;1(1):29.

Adding three-compartment breast (3CB) features to computer-aided detection yields an area under the ROC curve of **0.81** — compared to **0.69** for CAD alone. The integrated discrimination improvement demonstrates substantial benefit from adding 3CB features.

[Read the paper ↗](https://www.nature.com/articles/s43856-021-00024-0){: .btn .btn-outline-primary style="margin-top: 0.5rem;"}

</div>
</div>
</div>
</section>

<!-- LATEST PUBLICATIONS (dynamic — top 3 by year) -->
<section class="section section--alt">
<div class="container">
<div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;">
<h2 style="margin: 0;">Latest Publications</h2>
<a href="{{ site.baseurl }}/publications/" style="color: var(--primary); font-weight: 600; text-decoration: none;">All publications →</a>
</div>
{% assign active_pubs = site.data.publications | where_exp: "p", "p.exclude != true" %}
{% assign latest_pubs = active_pubs | sort: "year" | reverse | slice: 0, 3 %}
<div class="features-grid">
{% for pub in latest_pubs %}
<article class="feature-card" style="display: flex; flex-direction: column; gap: 0.75rem;">
<div style="font-size: 0.75rem; font-weight: 700; color: var(--primary); letter-spacing: 0.05em;">{{ pub.year }}</div>
<div style="font-weight: 600; font-size: 1rem; line-height: 1.35;">{{ pub.title }}</div>
<div style="font-size: 0.85rem; color: var(--gray-700);">{% assign authors = pub.authors | split: ", " %}{% for a in authors limit: 5 %}{% if a contains "Shepherd" %}<strong>{{ a }}</strong>{% else %}{{ a }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}{% if authors.size > 5 %}, et al.{% endif %}</div>
{% if pub.journal %}<div style="font-size: 0.85rem; color: var(--gray-500);"><em>{% if pub.journal_display %}{{ pub.journal_display }}{% else %}{{ pub.journal }}{% endif %}</em></div>{% endif %}
{% if pub.doi %}<div style="margin-top: auto;"><a href="https://doi.org/{{ pub.doi | remove: 'https://doi.org/' }}" target="_blank" rel="noopener" style="font-size: 0.85rem; color: var(--primary); font-weight: 600; text-decoration: none;">DOI →</a></div>{% endif %}
</article>
{% endfor %}
</div>
</div>
</section>
