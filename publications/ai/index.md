---
layout: default
title: "Publications — AI for Health"
description: "Shepherd Research Lab publications applying AI, machine learning, and deep learning to health — cancer detection, body composition, and medical imaging."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 900px;">

# AI for Health — Publications

Papers tagged `ai` — applications of machine learning and deep learning to health.

See also: [all publications]({{ site.baseurl }}/publications/) · [AI for Health research page]({{ site.baseurl }}/research/ai/)

{% assign filtered = site.data.publications | where_exp: "p", "p.exclude != true" %}
{% assign filtered = filtered | where_exp: "p", "p.tags contains 'ai'" %}

{% include publications-list.html entries=filtered %}

</div>
</section>
