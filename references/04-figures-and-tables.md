# 04. Figures, Tables, and Supplementary Material

## Contents
1. Role of figures and tables
2. Choosing figure versus table versus text
3. Design principles for figures
4. Common chart choices and pitfalls
5. Color, accessibility, and typography
6. Captions
7. Tables
8. Image integrity and technical specs
9. Supplementary material
10. Graphical abstracts and highlights
11. Figure review checklist

## 1. Role of figures and tables

Reviewers and skimming readers look at the abstract, figures, and tables first. **The main figures should carry the paper's argument on their own.** Plan them before writing, and revise the text to match, not the reverse.

## 2. Choosing figure versus table versus text

- **Text:** one to three numbers, or a simple comparison.
- **Table:** exact values readers may look up or compare precisely; many variables with few observations; parameter estimates; study characteristics.
- **Figure:** patterns, trends, distributions, relationships, comparisons across conditions, workflows, mechanisms, spatial or temporal structure.
- If a figure could be a sentence, make it a sentence. If a table has many empty cells, rethink it.

## 3. Design principles for figures

- **One message per figure** (or per panel). State it in the caption's first sentence.
- **Maximize data-ink and show the data.** Prefer showing individual points, distributions, or raw traces over bars with only means and error bars. Dot plots, box or violin plots with points, and paired-line plots are often more honest.
- **Make comparisons easy:** put compared items adjacent, share axes, use consistent order, scales, and colors across panels and across figures.
- **Label directly** where possible instead of forcing readers to match legends. Axis labels have units. Panel letters (A, B, C) are placed consistently.
- **Design at final size.** Check that text is readable at the printed column width (commonly 6 to 8 pt minimum after scaling; check the journal's guidance).
- Remove chartjunk: heavy gridlines, 3D effects, drop shadows, redundant legends, decorative backgrounds.
- Keep **axes honest**: bar charts start at zero; avoid truncated or dual axes that mislead; use log scales deliberately and say so.
- Show **uncertainty** and define what error bars mean (SD, SEM, 95% CI, range) and the n behind them.
- Make **schematics and workflow diagrams** clean and consistent in symbols and arrow meaning; a good conceptual figure early in the paper often raises citation rates.

## 4. Common chart choices and pitfalls

| Goal | Good options | Avoid |
|---|---|---|
| Compare groups | Dot plot, box or violin with points, estimation plots | Bars with SEM only, pie charts for many categories |
| Show change over time | Line plot with uncertainty bands, slope graph | Dual y-axes, 3D lines |
| Show distribution | Histogram, density plot, ECDF | Bar chart of means |
| Show relationship | Scatter with fit and CI, hexbin for large n | Smoothed curve without data |
| Show proportions | Stacked bars with limited categories, waffle chart | Pie with more than 3 to 4 slices |
| Show many conditions | Small multiples (faceting) | One crowded panel |
| Show model performance | Curves with CIs (ROC, precision-recall, calibration) | Single point estimates without variance |
| Show spatial data | Maps with clear scale, projection, color legend | Rainbow colormaps for ordered data |

Other frequent mistakes: overplotting, inconsistent scales between related panels, unlabeled axes, legends hiding data, tiny fonts, inconsistent line styles, and chart types chosen for decoration.

## 5. Color, accessibility, and typography

- Use **colorblind-safe palettes** (e.g., Okabe-Ito for categorical; viridis or cividis for sequential data). Avoid red-green contrasts as the only distinction. Avoid rainbow ("jet") colormaps for ordered data because they distort perception.
- Do not rely on color alone: vary **marker shapes, line styles, or direct labels** so figures survive grayscale printing.
- Use **consistent color meaning** across the paper (the same condition always has the same color).
- Use a clean sans-serif font (Arial, Helvetica) matching the journal; keep font sizes consistent across figures.
- Provide **alt text** or accessible descriptions when the venue requests them.

## 6. Captions

- A caption lets a figure be understood **without reading the main text**.
- Structure: **Title sentence stating the finding or content**, then what is plotted (axes, symbols, error bars), sample sizes, statistical tests and thresholds, abbreviations defined, and any key observation to notice.
- Do not repeat the Methods; refer to it for details.
- Do not put results interpretation in the caption beyond what the viewer should see.

## 7. Tables

- Number tables and refer to every one in the text. Give each a **descriptive title** above the table.
- Align numbers by decimal point, use consistent decimal places and units, and keep **no more than needed**. Avoid vertical lines; use light horizontal rules (booktabs style).
- Order rows and columns logically (by importance, magnitude, time, or theory) and put the **comparison of interest side by side**.
- Include **n, effect sizes, intervals, and p-values** where appropriate, with clear notes defining abbreviations, tests, and symbols.
- Descriptive "Table 1" (participant or sample characteristics) is standard in many fields and should show **group-wise** descriptives when comparing groups.
- Do not duplicate a table's content in the text, and do not present a table that is also a figure.
- Long tables go in the supplement.

## 8. Image integrity and technical specs

- **No inappropriate manipulation.** Adjustments (brightness, contrast, cropping) must be uniform across the entire image, applied equally to controls, and disclosed. Do not splice or clone. Retain original uncropped images (especially blots and gels). Journals screen images with software, and manipulation is a common cause of retraction.
- Provide **scale bars** for micrographs and maps, and specify magnification.
- Use **vector formats** (PDF, SVG, EPS) for plots and diagrams, and **high-resolution raster** (TIFF or PNG) for photographs; common journal requirements are around 300 dpi for photos and higher (about 600 to 1,000 dpi) for line art, but follow the target journal's specifications exactly.
- Embed fonts, flatten transparency problems, and size figures to column widths (single versus double column).
- Obtain **permission** for any reproduced or adapted figure from other sources, and cite it. Check licenses (e.g., CC BY) before reuse.

## 9. Supplementary material

- Use for **robustness checks, extended methods, additional controls, long tables, detailed derivations, extra figures, and protocols**. Do not hide essential evidence there. The main text must stand alone.
- Number and name consistently (Fig. S1, Table S2) and reference each in the main text.
- Keep it organized: one PDF or a few labeled files, with a table of contents for long ones.
- Deposit large datasets or code in a repository and cite the DOI, rather than attaching huge files.
- Reviewers often skim supplements, so state the key takeaway of each in the main text.

## 10. Graphical abstracts and highlights

- Some journals ask for a **graphical abstract** (one clear visual summarizing the question, approach, and finding), **highlights** (three to five short bullets), or a **plain-language summary** or **significance statement**. Write these for a broad audience, avoiding jargon, and keep them consistent with the paper.
- Treat them as promotion tools: they affect attention, downloads, and press interest.

## 11. Figure review checklist

- [ ] Does each figure have a single clear message?
- [ ] Are axes labeled with units and are scales honest?
- [ ] Is every data point or group identifiable, with n stated?
- [ ] Are error bars defined?
- [ ] Is the palette colorblind-safe and grayscale-readable?
- [ ] Is text legible at final printed size?
- [ ] Is the caption self-contained?
- [ ] Is every figure referenced in order in the text?
- [ ] Are reused images permitted and credited?
- [ ] Are originals and raw data retained?
- [ ] Do numbers in figures match the text and tables?
