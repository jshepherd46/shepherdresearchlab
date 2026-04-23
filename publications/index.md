---
layout: default
title: "Publications"
description: "Peer-reviewed publications from the Shepherd Research Lab — rendered from the monthly OpenAlex pipeline output."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 900px;">

# Publications

{% assign filtered = site.data.publications | where_exp: "p", "p.exclude != true" %}

Browse by topic: [AI for Health]({{ site.baseurl }}/publications/ai/) · [Body Composition]({{ site.baseurl }}/publications/body-composition/) · [Cancer]({{ site.baseurl }}/publications/cancer/)

{% include publications-list.html entries=filtered show_downloads=true empty_message="The full publications list is regenerated each month from our automated pipeline — OpenAlex discovery, Claude-assisted classification, and exports to RIS and BibTeX — and will appear here once the first pipeline run completes." %}

</div>
</section>
