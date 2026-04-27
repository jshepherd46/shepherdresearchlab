---
layout: default
title: "3D Optical Scans"
description: "3D optical scanning for full-body shape, automatic circumference and length measurements, and progress tracking at the Body Composition Lab."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

# 3D Optical Scan

<nav style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.25rem 0 1.5rem;">
<a href="{{ site.baseurl }}/services/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">← All services</a>
<a href="{{ site.baseurl }}/pricing/#3d-optical" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">Pricing →</a>
<a href="{{ site.baseurl }}/make-an-appointment/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">Make an appointment →</a>
</nav>

![3D optical scan]({{ site.baseurl }}/wp-content/uploads/2020/01/3do_1920x900-1-1024x480.png)

Contactless, radiation-free 3D body imaging — automated circumferences, DXA-equivalent body composition, and validated metabolic risk measures from a single scan.

</div>
</section>

<section class="section section--alt">
<div class="container" markdown="1" style="max-width: 820px;">

## What is 3D optical scanning?

Three-dimensional optical (3DO) scanning is a contactless, radiation-free imaging technology that captures the complete exterior geometry of the body in seconds. Structured-light sensors or depth cameras record millions of surface points and assemble them into a dense 3D mesh — typically **60,000 vertices** — that accurately represents your body's shape from head to toe. From that mesh, software extracts automated circumference and length measurements, estimates body composition, and generates a visual model you can compare across visits to track change over time.

Unlike any other body-composition method, 3DO captures not just a number but the full **geometry** of your body. That geometry carries surprisingly deep information about what is happening inside: the distribution and volume of fat, the size of muscle compartments, metabolic risk, and functional capacity can all be read from the surface contours with validated algorithms. The Shepherd Lab pioneered this approach in a research program spanning more than a decade, producing a series of published algorithms that translate 3D body shape into the same output as a DXA scan — including regional fat and lean masses, fat mass index, and visceral fat estimates — without any radiation. The lab's open-access shape-model tool is described at [/shapeup/3do-bodycomp-analyzer/]({{ site.baseurl }}/shapeup/3do-bodycomp-analyzer/).

### What 3DO measures

**Automated body circumferences and lengths.**
The 3D mesh produces precise automated measurements of waist, hip, chest, neck, mid-arm, thigh, calf, and full-body heights and lengths. These replace error-prone tape measurements with repeatable, operator-independent values. Waist and hip circumferences from 3DO agree closely with tape-measured criterion values, and full-body circumference profiles can be extracted at any anatomical height. This measurement alone is a significant advance over manual anthropometry for epidemiological studies, fitness tracking, and garment fitting.
*Ng BK, Hinton BJ, Fan B, Kanaya AM, Shepherd JA. Clinical anthropometrics and body composition from 3D whole-body surface scans. Eur J Clin Nutr. 2016;70:1265–1270.*

**Total body fat % and Fat Mass Index (FMI).**
Using a statistical shape model trained on paired 3DO and DXA data from the Shape Up! Adults study, body-shape principal components predict total fat mass with **R² as high as 0.95** and root-mean-squared error below 2.5 kg — statistically indistinguishable from DXA. These predictions are available from the research-grade scanning systems using the lab's custom device-agnostic algorithm.
*Tian IY, Wong MC, Kennedy S, Kelly NN, Liu YE, Garber AK, Heymsfield SB, Curless B, Shepherd JA. A device-agnostic shape model for automated body composition estimates from 3D optical scans. Med Phys. 2022;49:6395–6409.*

**Regional body composition: trunk, arms, and legs.**
The shape model predicts regional fat and lean mass by anatomical compartment — trunk fat and fat-free mass, arm lean mass, and leg lean mass — with **R² values of 0.79–0.94**. Regional composition is the most clinically informative level of body-composition analysis, associating with cardiovascular disease, metabolic syndrome, and functional decline; 3DO provides it without any radiation.
*Ng BK, Sommer MJ, Wong MC, et al. Detailed 3-dimensional body shape features predict body composition, blood metabolites, and functional strength: the Shape Up! studies. Am J Clin Nutr. 2019;110:1316–1326.*

**Fat-Free Mass / Lean Mass Index (FFMI) and Appendicular Lean Mass.**
Lean mass and fat-free mass predicted from body shape, normalized to height squared. Appendicular lean mass from 3DO (arms + legs) tracks the same sarcopenia-relevant quantity measured by DXA, and responds sensitively to muscle gain or loss across intervention studies — **R² of 0.70–0.73** against DXA-measured change.
*Wong MC, Bennett JP, Leong LT, Tian IY, et al. Monitoring body composition change for intervention studies with advancing 3D optical imaging technology in comparison to DXA. Am J Clin Nutr. 2023;117:802–813.*

**Visceral Adipose Tissue (VAT) estimate.**
Body shape carries a moderate but significant signal for visceral fat. The Shepherd Lab's algorithms predict VAT from 3DO with **R² of 0.75**, validated against DXA. While the precision of VAT estimation is lower from 3DO than from DXA, this radiation-free, non-invasive estimate brings visceral-fat screening into settings where DXA is unavailable.
*Ng BK, Hinton BJ, Fan B, Kanaya AM, Shepherd JA. Eur J Clin Nutr. 2016;70:1265–1270.*

**Trunk-to-Leg Volume Ratio and Shape Principal Components.**
The shape of the body encodes metabolic-risk information that scalar measurements like BMI and waist circumference miss. The trunk-to-leg volume ratio — which the Shepherd Lab identified as a predictive metric for diabetes and all-cause mortality — is extracted directly from the 3D mesh. More broadly, the full set of shape principal components from a 3DO scan **improved metabolic-syndrome classification by 29% over BMI** in a diverse multiethnic sample, capturing information hidden in the geometry of the body.
*Wilson JP, Kanaya AM, Fan B, Shepherd JA. Ratio of trunk to leg volume as a new body shape metric for diabetes and mortality. PLoS One. 2013;8:e68716.*
*Bennett JP, Liu YE, Quon BK, et al. Three-dimensional optical body shape and features improve prediction of metabolic disease risk in a diverse sample of adults. Obesity. 2022;30:1589–1598.*

**Pseudo-DXA: generative deep-learning reconstruction.**
In a 2024 advance from the Shepherd Lab, a deep-learning model was trained to **generate an analyzable DXA scan from a 3DO input**. The resulting pseudo-DXA images were processed by standard clinical DXA software and yielded whole-body and regional fat, lean, and bone-mass estimates — demonstrating that exterior body shape contains enough information to synthesize DXA-equivalent data without any radiation exposure.
*Leong LT, et al. Generative deep learning furthers the understanding of local distributions of fat and muscle on body shape and health using 3D surface scans. Commun Med. 2024;4:13.*

</div>
</section>

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

## Scanning systems at the BCL

The BCL operates two tiers of 3DO scanning capability — one optimized for community use and one for research and clinical precision.

### Community assessment: Styku

The **Styku** is a consumer-grade turntable system that produces an immediate, visually intuitive report. You stand on a rotating platform for approximately **35 seconds** while a depth sensor captures your full-body silhouette. The Styku report provides automated body circumferences (waist, hip, chest, thigh, and more), estimated body-fat percentage and fat mass, a 3D avatar you can visualize and compare across visits, and a health-risk summary based on waist-to-height ratio and other shape metrics. The Styku is an ideal starting point for individuals who want to track the visible effects of a dietary or fitness intervention without the cost or complexity of a full DXA evaluation.

### Research fleet: five research-grade scanners with custom algorithms

For research and clinical studies, the BCL operates a fleet of **five research-grade 3DO scanning systems** from multiple manufacturers, including both turntable and scan-booth designs. These systems produce high-resolution point clouds processed by the Shepherd Lab's device-agnostic shape model, which standardizes output across scanner manufacturers and produces DXA-equivalent body-composition estimates for all the measures described above. The lab's custom algorithms are built on principal-component analysis of paired 3DO–DXA datasets from more than 1,000 adults in the Shape Up! Adults study (NIH/NIDDK R01 DK109008) and have been validated across six independent intervention studies. Researchers can submit raw mesh files for analysis using the public web tool at the [Shape Up! site]({{ site.baseurl }}/shapeup/3do-bodycomp-analyzer/).

Having multiple scanner platforms with a unified algorithm is a deliberate design choice: it lets multi-site studies, remote data collection, or technology-constrained settings contribute 3DO data that feeds into the same body-composition model regardless of which scanner was used.
*Tian IY, Wong MC, Kennedy S, Kelly NN, Liu YE, Garber AK, Heymsfield SB, Curless B, Shepherd JA. Med Phys. 2022;49:6395–6409.*

## Pediatric 3DO — scanning children from birth to 5 years

Standard 3DO systems require a cooperative standing subject, which excludes infants and young children entirely. The Shepherd Lab developed a custom pediatric scanning solution for the **Shape Up! Keiki** study (NIH/NICHD R01 HD103885), a 360-participant observational study of children from birth to five years in Hawaiʻi and the Pacific.

The system scans children while they lie in a clear enclosure, allowing the 3DO sensors to capture the full body surface even during normal infant movement. Specialized pediatric mesh templates and age-appropriate body-composition models were developed to handle the rapidly changing body geometry from newborn through preschool age. The scan is completely contactless, takes seconds, and requires no sedation or restraint.

This capability fills a major gap in childhood body-composition research. BMI z-score is currently the only adiposity measure routinely used in pediatric studies and clinical practice for young children, but it cannot capture regional fat distribution or its metabolic consequences. The Shepherd Lab's pediatric 3DO approach enables radiation-free measurement of total and regional body composition in children across the full early-childhood window, in a diverse multiethnic Pacific population that is underrepresented in existing reference standards.
*Tian IY, Wong MC, Nguyen WM, Kennedy S, McCarthy C, Kelly NN, Liu YE, Garber AK, Heymsfield SB, Curless B, Shepherd JA. Automated body composition estimation from device-agnostic 3D optical scans in pediatric populations. Clin Nutr. 2023;42:1619–1630.*

</div>
</section>

<section class="section section--alt">
<div class="container" markdown="1" style="max-width: 820px;">

## How should I prepare for a 3D optical scan?

For the most accurate representation of your body shape, wear form-fitting apparel like single-layer compression shorts without padding, and (for women) a sports bra.

## What can I expect during the scan?

You will stand on a turntable that rotates 360° while an optical sensor records circumferential data. Afterward, you will receive a detailed report.

</div>
</section>

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

## Sample report

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
<a href="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_01-scaled.jpg"><img src="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_01-scaled.jpg" alt="3D scan report page 1" style="width: 100%; height: auto;"></a>
<a href="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_02-scaled.jpg"><img src="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_02-scaled.jpg" alt="3D scan report page 2" style="width: 100%; height: auto;"></a>
<a href="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_08-scaled.jpg"><img src="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_08-scaled.jpg" alt="3D scan report page 8" style="width: 100%; height: auto;"></a>
<a href="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_11-scaled.jpg"><img src="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_11-scaled.jpg" alt="3D scan report page 11" style="width: 100%; height: auto;"></a>
<a href="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_12-scaled.jpg"><img src="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_12-scaled.jpg" alt="3D scan report page 12" style="width: 100%; height: auto;"></a>
<a href="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_13-scaled.jpg"><img src="{{ site.baseurl }}/wp-content/uploads/2023/09/Styku_Report_Page_13-scaled.jpg" alt="3D scan report page 13" style="width: 100%; height: auto;"></a>
</div>

</div>
</section>
