---
layout: default
title: "Shape Up! — Mesh Preparation"
description: "Step-by-step guide for preparing a 3D scan mesh for upload to the 3DO Body Composition Analyzer."
---

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

# Mesh preparation

<nav style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.25rem 0 1.5rem;">
<a href="{{ site.baseurl }}/shapeup/3do-bodycomp-analyzer/" style="padding: 0.35rem 0.8rem; border: 1px solid var(--gray-300); border-radius: 100px; font-size: 0.85rem; text-decoration: none; color: var(--gray-700); font-weight: 600;">← 3DO Body Composition Analyzer</a>
</nav>

How to prepare a 3D-scan mesh for upload to the 3DO Body Composition Analyzer.

</div>
</section>

<section class="section section--alt">
<div class="container" markdown="1" style="max-width: 820px;">

## File requirements

- **Units.** Metric (meters)
- **Format.** PLY with **ASCII** encoding (not binary)
- **Orientation.** The mesh must be standing with the feet on the ZX plane and the origin centered between the feet. The head must be oriented in the +Y direction.

To verify orientation in MeshLab, display the bounding box and XYZ world axes from the toolbar and toggle "On" for Measure Info in the right panel.

</div>
</section>

<section class="section">
<div class="container" markdown="1" style="max-width: 820px;">

## Sample reference meshes

Two correctly-prepared example files are available — useful as positioning references and for testing the analyzer pipeline.

| Sample | Weight (kg) | Height (m) | Age | Download |
|---|---|---|---|---|
| Male | 106.6 | 1.84 | 62 | [MALE_example3Dmesh_initial_ascii_n_scaled.ply ↗](https://shapeup.shepherdresearchlab.org/wp-content/uploads/2022/04/MALE_example3Dmesh_initial_ascii_n_scaled.ply) |
| Female | 98.6 | 1.61 | 44 | [FEMALE_example3Dmesh_initial_ascii_n_scaled.ply ↗](https://shapeup.shepherdresearchlab.org/wp-content/uploads/2022/04/FEMALE_example3Dmesh_initial_ascii_n_scaled.ply) |

<p style="font-size: 0.85rem; color: var(--gray-700); margin-top: 1rem;">Sample-mesh files are large (~60 MB each) and are temporarily linked from the legacy WP host while we transition to a permanent storage location. If the links go stale, contact the lab.</p>

</div>
</section>

<section class="section section--alt">
<div class="container" markdown="1" style="max-width: 820px;">

## Step-by-step in MeshLab

1. **Open the scan** in mesh-viewing software like [MeshLab ↗](https://www.meshlab.net/#download).

2. **Scale to metric units.** *Filters → Mesh Layer → Matrix: Set from translation/rotation/scale.*

3. **Correct translation and rotation.** The body should orient superiorly along +Y. The head should point toward +Y; the mesh should face down +Z.

4. **Bake the transformation** by freezing the current matrix.

5. **Export as PLY** with ASCII encoding (not binary).

</div>
</section>
