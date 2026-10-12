# 03. Methods, Statistics, and Rigor

## Contents
1. Principles of a defensible design
2. Reporting guidelines (EQUATOR)
3. Sampling, power, and sample size
4. Statistical practice that survives review
5. Causal versus associational claims
6. Multiplicity, researcher degrees of freedom, and pre-registration
7. Missing data, outliers, and robustness
8. Machine learning and computational rigor
9. Qualitative and mixed-methods rigor
10. Reproducibility and open practices
11. Likely methodological objections and pre-emptions

## 1. Principles of a defensible design

- **Match the design to the question.** A causal question needs a causal design (randomization, natural experiment, strong quasi-experimental identification); a descriptive question needs representative sampling; a prediction question needs held-out validation.
- **Controls and comparators are not optional.** Every claim of "better" or "effect" needs a fair comparator, tuned with the same care as your method.
- **Define variables, outcomes, and analysis before seeing results** wherever possible; label anything decided afterwards as exploratory.
- **Think about threats to validity**: confounding, selection bias, measurement error, attrition, contamination, demand effects, regression to the mean, history and maturation, leakage between training and test data.
- **Replicate yourself** before submission where feasible: rerun the pipeline from raw data to final figures, ideally on a clean machine or by a colleague.

## 2. Reporting guidelines (EQUATOR Network hosts them all)

Following the right checklist is often a submission requirement and is a strong credibility signal. Submit the completed checklist if the journal asks.

| Study type | Guideline |
|---|---|
| Randomized trials | CONSORT (and extensions); protocols: SPIRIT |
| Observational studies (cohort, case-control, cross-sectional) | STROBE |
| Systematic reviews and meta-analyses | PRISMA 2020 (scoping reviews: PRISMA-ScR); observational meta-analyses: MOOSE |
| Diagnostic accuracy | STARD |
| Prediction models | TRIPOD (and TRIPOD+AI) |
| Animal research | ARRIVE 2.0 |
| Case reports | CARE |
| Qualitative research | COREQ (interviews, focus groups), SRQR (general qualitative) |
| Economic evaluations | CHEERS |
| Quality improvement | SQUIRE |
| Machine learning in conferences | The venue's reproducibility checklist |

Register trials and systematic reviews prospectively (ClinicalTrials.gov, ISRCTN, PROSPERO, or equivalents). Many journals will not consider unregistered trials.

## 3. Sampling, power, and sample size

- Justify sample size with an **a priori power analysis** (state alpha, power, assumed effect size and its source) or, for fixed or opportunistic samples, a **sensitivity analysis** showing what effect size the study could detect.
- Conventional targets are 80 or 90 percent power at alpha 0.05, but choose the effect size from prior literature or a smallest effect size of interest, **not from the sample you happen to have**.
- Underpowered studies produce unreliable, inflated effects (Type M error) and sign errors (Type S error). Say so in limitations if power is modest.
- Describe how participants or units were **selected, recruited, and excluded**, with a flow diagram where appropriate. Report response rates and attrition.
- Beware **pseudoreplication**: the unit of analysis must match the unit of randomization or independent sampling. Use mixed-effects or cluster-robust methods for nested or repeated data.

## 4. Statistical practice that survives review

- **Report effect sizes with confidence or credible intervals**, not only p-values. State direction and magnitude in practical terms.
- Report **exact p-values** (e.g., p = 0.032; use p < 0.001 only for very small values) and avoid "trend toward significance".
- Do not dichotomize continuous variables without reason. Do not conclude "no effect" from non-significance; use **equivalence testing (TOST)** or interval-based reasoning.
- **Check assumptions** (distribution, variance homogeneity, independence, linearity) and say how. Choose robust or non-parametric alternatives when violated.
- Choose **appropriate models** for the data: count data, proportions, survival, hierarchical, longitudinal, compositional, time series with autocorrelation.
- **Do not confuse statistical with practical significance.** Large samples make trivial effects significant.
- Be consistent about **one- versus two-sided tests**, justify any one-sided test in advance.
- **Bayesian analyses:** justify priors, run sensitivity analyses to prior choice, report posterior summaries and diagnostics.
- Include **uncertainty in figures** (error bars defined as SD, SEM, or CI; prefer showing individual data points).
- Say which software and packages were used, with versions, and share code when possible.
- If a statistician co-author or consultant was involved, say so; if not, get a statistical review before submission when the analysis is non-trivial.

## 5. Causal versus associational claims

- Use **causal language only if the design earns it.** In observational data say "associated with", and state the assumptions needed for a causal reading.
- When making causal claims from observational data, be explicit about identification strategy (instrumental variables, difference-in-differences, regression discontinuity, matching, synthetic control, DAG-based adjustment), **its assumptions, and tests of those assumptions** (parallel trends, balance, instrument relevance and exclusion, sensitivity to unmeasured confounding such as E-values).
- Watch for **confounding, collider bias, mediator adjustment, reverse causation, Simpson's paradox, survivorship bias, and immortal time bias**.
- Use a **DAG** to justify covariate selection instead of "controlling for everything".
- Mechanism claims need mechanism evidence (manipulation, mediation with caveats, converging lines of evidence).

## 6. Multiplicity, researcher degrees of freedom, and pre-registration

- Every extra outcome, subgroup, model specification, or stopping rule inflates false positives ("the garden of forking paths").
- **Correct for multiple comparisons** where there is a family of tests (Bonferroni or Holm for family-wise control; Benjamini-Hochberg for false discovery rate) or define one primary outcome and label others secondary or exploratory.
- **Pre-register** hypotheses, design, and analysis plan (OSF, AsPredicted, ClinicalTrials.gov, or a Registered Report at a participating journal). Deviations from the plan are reported and explained.
- Do not HARK (hypothesize after results are known). It is fine to explore, but label it as exploration and treat results as hypothesis-generating.
- Disclose **all** conditions, outcomes, exclusions, and stopping rules, not only the ones that worked.
- Interim analyses and optional stopping require proper methods (sequential designs) and disclosure.

## 7. Missing data, outliers, and robustness

- Characterize **missingness** (missing completely at random, at random, not at random). Complete-case analysis is justified only under limited conditions. Prefer multiple imputation or likelihood-based methods and compare with sensitivity analyses.
- Define **outlier rules in advance**. Report results with and without exclusions.
- Include **robustness checks**: alternative specifications, subsamples, variable definitions, estimators, tuning choices. Put extended ones in the supplement but state the headline conclusion about robustness in the main text.
- Do **negative controls** or **placebo tests** when possible to show that the method does not find effects where none should exist.
- Report **heterogeneity** (subgroup or moderator effects) with proper interaction tests, not by comparing p-values across subgroups.

## 8. Machine learning and computational rigor

- Prevent **data leakage**: split by the correct unit (patient, subject, time, group), fit preprocessing on training data only, and never tune on the test set.
- Compare with **strong, properly tuned baselines** and simple models; state compute budgets and hyperparameter search effort for all methods equally.
- Report **variance across seeds, folds, or runs** (mean and standard deviation or CI); one run is an anecdote. Use significance tests or interval overlap sparingly and honestly.
- Include **ablation studies** for each claimed component, and error analysis showing failure cases.
- Evaluate on **multiple datasets** or settings and out-of-distribution or shifted data where generalization is claimed. Beware benchmark contamination and overfitting to public leaderboards.
- Document **data provenance, licenses, preprocessing, and compute**. Release code, configs, and weights when allowed, with a README that reproduces the headline numbers.
- Discuss **societal impact, bias, and misuse** where the venue requires it or the topic warrants it. Use model and dataset documentation (model cards, datasheets).
- For clinical prediction, calibrate and validate externally, and follow TRIPOD.

## 9. Qualitative and mixed-methods rigor

- State the **methodological tradition** (grounded theory, phenomenology, ethnography, thematic analysis, case study, discourse analysis) and why it fits the question.
- Evidence of **trustworthiness** (Lincoln and Guba: credibility, transferability, dependability, confirmability): prolonged engagement, triangulation, member checking where appropriate, negative case analysis, audit trail, thick description.
- Describe **sampling logic** (purposive, theoretical, snowball), the basis for stopping (information power or saturation, argued not just asserted), and participant characteristics.
- Practice **reflexivity**: state the researcher's position and how it may shape data collection and interpretation.
- Show **how themes were derived**: coding process, number of coders, resolution of disagreement, and supporting quotations (representative, not cherry-picked, with participant identifiers that preserve anonymity).
- In mixed methods, explain **integration** (convergent, explanatory sequential, exploratory sequential), not just two studies side by side.
- Follow COREQ or SRQR and secure ethics approval and informed consent appropriate to the data.

## 10. Reproducibility and open practices

- Share **data** in a trusted repository (Zenodo, Dryad, Figshare, OSF, or a field-specific one such as GenBank, GEO, ICPSR, Harvard Dataverse) with a DOI and a clear license, following **FAIR** principles (findable, accessible, interoperable, reusable). If data cannot be public (privacy, legal), describe access conditions and share synthetic or minimal data where possible.
- Share **code** (GitHub archived to Zenodo for a DOI) with environment files, dependency versions, and a README. Containerize if feasible.
- Provide a **data dictionary** and codebook.
- Share **materials** (questionnaires, stimuli, protocols, reagents with identifiers such as RRIDs).
- Say what is shared in a **Data and code availability statement**; reviewers and funders increasingly check it.
- Never claim data are "available on request" if you cannot actually provide them; many journals treat that as inadequate.

## 11. Likely methodological objections and pre-emptions

Prepare answers (in the manuscript, not only in a rebuttal) to:

| Reviewer objection | Pre-emption |
|---|---|
| "Sample too small or unrepresentative" | Power or sensitivity analysis; sample description; scope of generalization stated |
| "Confounding or reverse causation" | Design features, adjustment rationale (DAG), sensitivity analysis, careful language |
| "Alternative explanation" | Name it, test or rule it out, or concede and scale the claim |
| "Multiple testing / forking paths" | Pre-registration, primary outcome, correction, exploratory label |
| "Measure not valid or reliable" | Validation evidence, reliability coefficients, convergent checks |
| "Baselines weak or unfair" | Strong, equally tuned baselines, shared compute budget |
| "Results not robust" | Robustness section, alternative specifications, ablations |
| "Not reproducible" | Code, data, versions, detailed protocol |
| "Overgeneralized conclusions" | Explicit scope; limits and external validity paragraph |
| "Ethics or consent unclear" | Approval number, consent procedure, data protection stated |
