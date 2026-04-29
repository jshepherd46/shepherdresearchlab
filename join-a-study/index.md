---
layout: default
title: "Join A Study"
description: "Participate in a Shepherd Research Lab study on body composition, health measurement, or cancer risk."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

# Join A Study

The Shepherd Research Lab invites participants to join research studies focused on body composition, health-measurement technologies, and related health outcomes. Studies that are **currently enrolling** appear first below; closed studies are kept on the page for reference.

For general inquiries, call **808-440-5234** or email [bodycompstudies@cc.hawaii.edu](mailto:bodycompstudies@cc.hawaii.edu). Each study below also has its own contact details.

</div>
</section>

<section class="section section--alt">
<div class="container">

{% assign sorted_statuses = "enrolling,reopening,closed" | split: "," %}
<div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
{% for status in sorted_statuses %}
{% assign filtered = site.data.studies | where: "status", status %}
{% for s in filtered %}

<article class="feature-card" style="display: flex; flex-direction: column; gap: 1rem; padding: 2rem;{% if s.status == 'closed' %} opacity: 0.7;{% endif %}">

<div>
{% if s.status == 'enrolling' %}
<span style="display: inline-block; padding: 0.3rem 0.85rem; border-radius: 100px; background: rgba(2, 71, 49, 0.12); color: var(--primary); font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">Enrolling</span>
{% elsif s.status == 'reopening' %}
<span style="display: inline-block; padding: 0.3rem 0.85rem; border-radius: 100px; background: rgba(217, 119, 6, 0.14); color: #b45309; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">Reopening soon</span>
{% else %}
<span style="display: inline-block; padding: 0.3rem 0.85rem; border-radius: 100px; background: rgba(107, 114, 128, 0.14); color: #4b5563; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">Closed</span>
{% endif %}
</div>

<h2 style="margin: 0; font-size: 1.35rem; line-height: 1.3;">{{ s.name }}</h2>

{% if s.note %}
<p style="margin: 0; color: var(--gray-700); font-size: 0.9rem; font-style: italic;">{{ s.note }}</p>
{% endif %}

<p style="margin: 0; color: var(--gray-700);">{{ s.description }}</p>

<dl style="margin: 0; display: grid; grid-template-columns: max-content 1fr; gap: 0.4rem 1rem; font-size: 0.9rem; color: var(--gray-700);">
<dt style="font-weight: 600; color: var(--gray-900);">Eligibility</dt><dd style="margin: 0;">{{ s.eligibility }}</dd>
<dt style="font-weight: 600; color: var(--gray-900);">Commitment</dt><dd style="margin: 0;">{{ s.commitment }}</dd>
<dt style="font-weight: 600; color: var(--gray-900);">Compensation</dt><dd style="margin: 0;">{{ s.compensation }}</dd>
</dl>

<div style="border-top: 1px solid var(--gray-300); padding-top: 1rem; font-size: 0.85rem; color: var(--gray-700);">
<strong>Phone:</strong> 808-440-5234<br>
<strong>Email:</strong> <a href="mailto:{{ s.email }}">{{ s.email }}</a>
</div>

<div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: auto;">
{% if s.status != 'closed' %}
<a href="mailto:{{ s.email }}?subject=Interest in {{ s.name }}" class="btn btn-primary">Email the team</a>
{% endif %}
{% if s.detail_page %}
<a href="{{ site.baseurl }}{{ s.detail_page }}" class="btn btn-outline-primary">Study details →</a>
{% endif %}
</div>

</article>

{% endfor %}
{% endfor %}
</div>

</div>
</section>

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

## Not sure which study? Want to be notified?

Fill in the form below or email the lab directly — we'll route your interest to the right study coordinator and add you to the future-studies notification list if you'd like.

<div class="contact-grid" markdown="1" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem; margin-top: 2rem;">
<div markdown="1">

**Studies inquiries**  
[bodycompstudies@cc.hawaii.edu](mailto:bodycompstudies@cc.hawaii.edu)  
808-440-5234

**Lab**  
Body Composition Lab  
701 Ilalo Street  
Honolulu, HI 96813

</div>
<div>
<!-- TODO (Phase 3): replace YOUR_FORMSPREE_STUDIES_ID with the real form ID from formspree.io -->
<!-- All submissions route to bodycompstudies@cc.hawaii.edu (configured in Formspree). -->
<form action="https://formspree.io/f/YOUR_FORMSPREE_STUDIES_ID" method="POST" style="display: flex; flex-direction: column; gap: 1rem;">
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Your name
<input type="text" name="name" required style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit;">
</label>
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Email address
<input type="email" name="email" required style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit;">
</label>
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Which study interests you?
<select name="study" style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit;">
<option>I'm not sure yet — please contact me</option>
{% for s in site.data.studies %}<option>{{ s.short_name }}{% if s.status == 'closed' %} (closed){% endif %}</option>
{% endfor %}<option>Future studies — just add me to the list</option>
</select>
</label>
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Anything you'd like us to know
<textarea name="message" rows="4" style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit; resize: vertical;"></textarea>
</label>
<button type="submit" class="btn btn-primary" style="align-self: flex-start;">Submit</button>
</form>
</div>
</div>

</div>
</section>
