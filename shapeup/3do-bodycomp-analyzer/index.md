---
layout: default
title: "3D Optical Body Composition Analyzer"
description: "Web-based tool implementing a peer-reviewed scanner-agnostic algorithm for automated body-composition estimates from 3DO scans."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

# 3D Optical Body Composition Analyzer

<nav style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.25rem 0 1.5rem;">
<a href="{{ site.baseurl }}/shapeup/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">← Shape Up! home</a>
<a href="{{ site.baseurl }}/shapeup/mesh-preparation/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">Mesh preparation guide →</a>
<a href="{{ site.baseurl }}/publications/optical-scan/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">Optical-scan publications →</a>
</nav>

A web-based tool implementing a peer-reviewed algorithm for automated body-composition analysis from 3D optical scans. Accepts mesh-file uploads and returns templated meshes with body-composition predictions for demonstration purposes.

<div style="padding: 1rem 1.25rem; background: var(--gray-100); border-left: 4px solid var(--gray-400); border-radius: var(--radius); margin: 1.5rem 0;">
<strong>Tool currently unavailable.</strong> The interactive analyzer is being re-hosted. Use the contact form below to request access or to be notified when the tool is back online. The reference paper and methodology are described below.
</div>

</div>
</section>

<section class="section section--alt">
<div class="container" markdown="1" style="max-width: 820px;">

## Reference publication

**Tian IY, Wong MC, Kennedy SF, Kelly NN, Liu YE, Garber AK, Heymsfield SB, Curless B, Shepherd JA.** A Device-Agnostic Shape Model for Automated Body Composition Estimates from 3D Optical Scans. *Medical Physics* 2022.

[DOI: 10.1002/mp.15843](https://doi.org/10.1002/mp.15843) · [PubMed PMID: 35837761](https://pubmed.ncbi.nlm.nih.gov/35837761/)

</div>
</section>

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

## Abstract

**Background.** Many predictors of morbidity caused by metabolic disease are associated with body shape. 3D optical (3DO) scanning captures body shape and has been shown to accurately and precisely predict body-composition variables associated with mortality risk — with advantages in safety, cost, and accessibility compared to dual-energy X-ray absorptiometry (DXA). However, standardization across manufacturers remains lacking.

**Purpose.** We introduce a scanner-agnostic algorithm that automatically fits a topologically consistent human mesh to 3DO-scanned point clouds and predicts clinically important body metrics using standardized models.

**Methods.** Training used **848 scans** across three different 3D optical systems (ages 18–89; BMI 14–52 kg/m²). The pipeline applied template-mesh registration, anatomically constrained PCA deformation, and surface-to-surface optimization. A unified PCA model generated body-composition predictions, learned from 562 withheld test scans.

**Results.** The model achieved **R² > 0.8** for most predictions (highest **0.94** for total fat / lean and trunk fat). Root-mean-squared errors stayed below 3.0 kg. Repeatability precision was 2–3× worse than DXA, except for visceral fat measurements.

**Conclusions.** The method provides an accurate, automated, and scanner-agnostic framework for standardizing 3DO scans — a radiation-free, low-cost alternative to criterion radiology imaging for body-composition analysis.

</div>
</section>

<section class="section section--alt">
<div class="container" markdown="1" style="max-width: 820px;">

## Request access / get notified

<form action="https://formspree.io/f/xdabkwzg" method="POST" style="display: flex; flex-direction: column; gap: 1rem; max-width: 480px;">
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Your name
<input type="text" name="name" required style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit;">
</label>
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Your email
<input type="email" name="email" required style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit;">
</label>
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Subject
<input type="text" name="subject" required style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit;">
</label>
<label style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 600;">Your message (optional)
<textarea name="message" rows="5" style="padding: 0.65rem 0.9rem; border: 1px solid var(--gray-300); border-radius: var(--radius); font: inherit; resize: vertical;"></textarea>
</label>
<button type="submit" class="btn btn-primary" style="align-self: flex-start;">Submit</button>
</form>

</div>
</section>
