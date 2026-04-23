---
layout: default
title: "Publications — Body Composition"
description: "Shepherd Research Lab publications on body composition — DXA, 3D optical scanning, bioimpedance, metabolic-risk modeling."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 900px;">

# Body Composition — Publications

Papers tagged `body-composition` — quantifying fat, lean, and bone tissue and relating body shape to disease risk.

See also: [all publications]({{ site.baseurl }}/publications/) · [Body Composition research page]({{ site.baseurl }}/research/body-composition/)

{% assign filtered = site.data.publications | where_exp: "p", "p.exclude != true" %}
{% assign filtered = filtered | where_exp: "p", "p.tags contains 'body-composition'" %}

{% include publications-list.html entries=filtered %}

</div>
</section>
