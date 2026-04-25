---
layout: default
title: "News"
description: "News, awards, conference reports, and Q&A pieces from the Shepherd Research Lab."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 760px;">

# News

Lab news, awards, conference reports, and Q&A pieces. Listed newest first.

{% for post in site.posts %}
<article style="padding: 1.5rem 0; border-bottom: 1px solid var(--gray-300);">
<p style="color: var(--gray-500); font-size: 0.85rem; margin-bottom: 0.35rem; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600;">{{ post.date | date: "%B %-d, %Y" }}</p>
<h2 style="margin-bottom: 0.5rem; font-size: 1.35rem;"><a href="{{ post.url | relative_url }}" style="color: inherit; text-decoration: none;">{{ post.title }}</a></h2>
{% if post.excerpt %}<div style="color: var(--gray-700);">{{ post.excerpt | strip_html | truncate: 240 }}</div>{% endif %}
<p style="margin-top: 0.75rem;"><a href="{{ post.url | relative_url }}" style="color: var(--primary); font-weight: 600; text-decoration: none;">Read more →</a></p>
</article>
{% endfor %}

{% if site.posts.size == 0 %}
*No posts yet.*
{% endif %}

</div>
</section>
