---
layout: default
title: "AI PHI — Events"
description: "AI PHI events — monthly Affinity Group meetings on AI in cancer research, plus workshops and special events."
---

{% assign now_date = site.time | date: "%Y-%m-%d" %}
{% assign upcoming_meetings = site.data.affinity_meetings | where_exp: "m", "m.date >= now_date" | sort: "date" %}
{% assign past_meetings = site.data.affinity_meetings | where_exp: "m", "m.date < now_date" | sort: "date" | reverse %}
{% assign stein_meetings = past_meetings | where_exp: "m", "m.stein_photo" %}

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

# Events

<nav style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.25rem 0 1.5rem;">
<a href="{{ site.baseurl }}/aiphi/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">← AI PHI home</a>
<a href="https://www.youtube.com/@UHCC_AIPHI" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">YouTube ↗</a>
<a href="{{ site.baseurl }}/news/aiphi/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">AI PHI news →</a>
</nav>

AI PHI runs two streams of events: a recurring monthly **Affinity Group** for AI-in-cancer-research talks, and occasional **special events** — workshops, symposia, and partner sessions. Special events are written up in our news feed; talk recaps appear there too once recordings are posted.

To suggest a speaker for the Affinity Group, contact [johnshep@hawaii.edu](mailto:johnshep@hawaii.edu).

</div>
</section>

<section class="section section--alt">
<div class="container">
<div style="text-align:center; max-width: 820px; margin: 0 auto 2.5rem;">
<div style="font-size: 0.8rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Upcoming</div>
{% if upcoming_meetings.size > 0 %}
{% assign next = upcoming_meetings[0] %}
<h2 style="margin: 0;">{{ next.date | date: "%A, %B %-d, %Y" }} — 9:00 AM HST</h2>
<p style="color: var(--gray-500); margin-top: 0.5rem; margin-bottom: 0;">Affinity Group · via Zoom</p>
{% else %}
<h2 style="margin: 0;">No meetings currently scheduled</h2>
<p style="color: var(--gray-500); margin-top: 0.5rem; margin-bottom: 0;">Check back soon — the affinity group meets the first Friday of every month.</p>
{% endif %}
</div>

{% if upcoming_meetings.size > 0 %}
{% assign next = upcoming_meetings[0] %}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 3rem; align-items: center; max-width: 1000px; margin: 0 auto;">
{% if next.image %}
<img src="{{ site.baseurl }}{{ next.image }}" alt="{{ next.speaker }}" style="width:100%; max-width: 360px; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); margin: 0 auto; display: block;">
{% endif %}
<div markdown="1">

**{{ next.speaker }}**{% if next.affiliation %} · *{{ next.affiliation }}*{% endif %}

{{ next.title }}

{% if next.abstract %}{{ next.abstract }}{% endif %}

[Register for this Event →](https://hawaii.zoom.us/meeting/register/IXHDo0CjTPaKD12Om3ALMg){: .btn .btn-primary style="margin-top: 0.5rem;"}

*Register once to attend this and any future Affinity Group meeting — Zoom emails you the join link and reminders automatically.*

</div>
</div>
{% endif %}

</div>
</section>

<section class="section">
<div class="container">
<div style="max-width: 820px; margin: 0 auto;" markdown="1">

## Affinity Group: AI in Cancer Research

A monthly group discussing current trends and applications of artificial intelligence in cancer research and clinical practice. We bring together AI researchers from computer science, engineering, nutrition, epidemiology, and radiology with clinicians and patient advocates.

**Open to all backgrounds.** Students, trainees, and faculty with any (or no) background in AI are welcome — the goal is to foster collaborative interactions to solve cancer problems.

**Cadence.** First Friday of each month, 9:00 AM Hawaiʻi time, via Zoom.

[Register for the series →](https://hawaii.zoom.us/meeting/register/IXHDo0CjTPaKD12Om3ALMg){: .btn .btn-primary}
[Watch past meetings on YouTube ↗](https://www.youtube.com/@UHCC_AIPHI){: .btn .btn-outline-primary}

</div>

{% if past_meetings.size > 0 %}
<div style="max-width: 1100px; margin: 3.5rem auto 0;">
<h3 style="text-align: center; margin-bottom: 0.5rem;">Past meetings</h3>
<p style="text-align: center; color: var(--gray-500); margin-bottom: 2rem; max-width: 640px; margin-left: auto; margin-right: auto;">Recordings of all past meetings are on the <a href="https://www.youtube.com/@UHCC_AIPHI">AI PHI YouTube channel ↗</a>.</p>

<div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
{% for m in past_meetings %}
<article class="feature-card" style="display: flex; flex-direction: column; gap: 0.4rem; padding: 1.1rem 1.25rem;">
<p style="font-size: 0.7rem; color: var(--gray-500); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin: 0;">{{ m.date | date: "%b %-d, %Y" }}</p>
<h4 style="margin: 0; font-size: 1rem; line-height: 1.3;">{{ m.speaker }}{% if m.affiliation %} · <span style="font-weight: 400; color: var(--gray-700); font-size: 0.9rem;">{{ m.affiliation }}</span>{% endif %}</h4>
<p style="margin: 0; font-size: 0.88rem; color: var(--gray-700); line-height: 1.45;">{{ m.title }}</p>
{% if m.recap_post %}
<a href="{{ site.baseurl }}{{ m.recap_post }}" style="font-size: 0.85rem; font-weight: 600; margin-top: auto;">Read recap →</a>
{% endif %}
</article>
{% endfor %}
</div>
</div>
{% endif %}

</div>
</section>

{% if stein_meetings.size > 0 %}
<section class="section section--alt">
<div class="container">

<div style="text-align:center; max-width: 720px; margin: 0 auto 2.5rem;">
<div style="font-size: 0.8rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Speaker compensation</div>
<h2>Beer steins from the speakers</h2>
<p style="color: var(--gray-700); margin: 0;">Every Affinity Group speaker receives a custom AI PHI beer stein as thanks for their contribution. The gallery below grows month by month as speakers send back photos with their stein.</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; max-width: 1100px; margin: 0 auto;">
{% for m in stein_meetings %}
<figure style="margin: 0; text-align: center;">
<img src="{{ site.baseurl }}{{ m.stein_photo }}" alt="{{ m.speaker }} with their AI PHI beer stein" style="width: 100%; aspect-ratio: 1/1; object-fit: cover; object-position: center top; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);">
<figcaption style="font-size: 0.85rem; color: var(--gray-700); margin-top: 0.6rem; font-weight: 600;">{{ m.speaker }}</figcaption>
</figure>
{% endfor %}
</div>

</div>
</section>
{% endif %}

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

## Special events

Workshops, symposia, and partner sessions are written up in our news feed alongside Affinity Group talk recaps.

[AI PHI news →]({{ site.baseurl }}/news/aiphi/){: .btn .btn-outline-primary}

</div>
</section>
