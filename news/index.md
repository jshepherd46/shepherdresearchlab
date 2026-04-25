---
layout: default
title: "News"
description: "News, awards, conference reports, and Q&A pieces from the Shepherd Research Lab."
---

<section class="section">
<div class="container" style="max-width: 960px;">

<h1>News</h1>
<p style="color: var(--gray-500); margin-top: -0.75rem; margin-bottom: 2.5rem;">Lab news, awards, conference reports, and Q&amp;A pieces. Listed newest first.</p>

<div style="display: flex; flex-direction: column; gap: 2rem;">

{% for post in site.posts %}
<a href="{{ post.url | relative_url }}" class="news-card" style="display: grid; grid-template-columns: minmax(0, 240px) 1fr; gap: 2rem; padding: 0; background: white; border: 1px solid var(--gray-300); border-radius: var(--radius-lg); overflow: hidden; text-decoration: none; color: inherit; transition: var(--transition);">
{% if post.thumbnail %}
<img src="{{ site.baseurl }}{{ post.thumbnail }}" alt="" style="width: 100%; height: 100%; min-height: 160px; aspect-ratio: 4/3; object-fit: cover;">
{% else %}
<div style="background: var(--primary-light); min-height: 160px;"></div>
{% endif %}
<div style="padding: 1.5rem 1.75rem 1.5rem 0;">
<p style="font-size: 0.75rem; color: var(--gray-500); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; margin-bottom: 0.5rem;">{{ post.date | date: "%B %-d, %Y" }}</p>
<h2 style="font-size: 1.25rem; margin-bottom: 0.6rem; line-height: 1.3;">{{ post.title }}</h2>
<p style="color: var(--gray-700); margin-bottom: 0.75rem;">{{ post.excerpt | strip_html | truncate: 220 }}</p>
<span style="color: var(--primary); font-weight: 600; font-size: 0.9rem;">Read more →</span>
</div>
</a>
{% endfor %}

{% if site.posts.size == 0 %}
<p><em>No posts yet.</em></p>
{% endif %}

</div>
</div>
</section>
