---
layout: default
title: "Publications — Cancer"
description: "Shepherd Research Lab publications on cancer — breast density, cancer screening, and risk modeling."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 900px;">

# Cancer — Publications

Papers tagged with any of `breast-density`, `cancer-screening`, or `risk-modeling` — the three research-area tags collectively representing the lab's cancer work.

See also: [all publications]({{ site.baseurl }}/publications/) · [Cancer research page]({{ site.baseurl }}/research/cancer/)

{%- comment -%}
No single "cancer" tag exists in tags.yaml; cancer research surfaces under
three tags. A single where_exp with `or` automatically dedupes (each entry
is tested once and included at most once).
{%- endcomment -%}

{% assign active = site.data.publications | where_exp: "p", "p.exclude != true" %}
{% assign filtered = active | where_exp: "p", "p.tags contains 'breast-density' or p.tags contains 'cancer-screening' or p.tags contains 'risk-modeling'" %}

{% include publications-list.html entries=filtered %}

</div>
</section>
