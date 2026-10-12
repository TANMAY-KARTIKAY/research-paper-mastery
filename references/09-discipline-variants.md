# 09. Discipline Variants

Conventions differ sharply by field. Always verify against the specific venue's guidelines and a few recent papers. This file gives the defaults a veteran would expect.

## Contents
1. Biomedical and clinical research
2. Life sciences and basic science (letters-style journals)
3. Physical sciences and chemistry
4. Engineering and applied sciences
5. Computer science and machine learning (conference culture)
6. Mathematics and theoretical work
7. Social sciences and psychology
8. Economics and quantitative policy research
9. Humanities and interpretive scholarship
10. Qualitative and mixed-methods articles
11. Review articles (narrative, systematic, meta-analysis)
12. Short formats: letters, case reports, brief reports
13. Data, software, and methods papers
14. Theses and dissertation chapters turned into articles

## 1. Biomedical and clinical research

- **Structure:** IMRaD, usually structured abstract (Background, Methods, Results, Conclusions), strict word limits.
- **Reporting:** follow CONSORT, STROBE, PRISMA, STARD, TRIPOD, CARE, etc. and submit checklists. Register trials prospectively. State ethics approval and consent.
- **Emphasis:** clinical relevance, effect sizes with confidence intervals, absolute as well as relative risks, number needed to treat where relevant, patient-important outcomes, harms and adverse events, generalizability, and conflicts of interest.
- **Language:** avoid causal claims from observational data; distinguish statistical from clinical significance; use person-first, non-stigmatizing language.
- **Process:** ICMJE recommendations; data sharing statements; trial protocols and statistical analysis plans may be requested. Embargo and press rules can apply.
- **Common failures:** unregistered or retrospectively registered trials, switched outcomes, underpowered studies, inadequate follow-up, selective reporting, spin in conclusions.

## 2. Life sciences and basic science

- **Impact-focused journals** (broad-audience) want a conceptual advance, mechanism, and strong, multi-pronged evidence; typically fewer words, many supplementary experiments, and **significance statements**.
- Use **orthogonal approaches** (genetic, biochemical, imaging, computational) to support a mechanism. Include controls, replicates (biological versus technical clearly distinguished), and blinded analysis where possible.
- Provide **reagent identifiers** (RRIDs), cell line authentication, mycoplasma testing, antibody validation, and strain details.
- Deposit **sequence and omics data** in public repositories (GEO, SRA, PDB, ProteomeXchange, GenBank) with accession numbers.
- Pay attention to **blot and image integrity**, full uncropped gels in the supplement, and statistics appropriate to n (avoid tiny n with parametric tests without justification).

## 3. Physical sciences and chemistry

- Emphasis on **measurement uncertainty, calibration, and reproducibility**, characterization of new compounds (NMR, MS, elemental analysis, crystallography with deposited CIF), and comparisons with theory.
- Provide **computational details** (functionals, basis sets, convergence criteria, code versions) and deposit input and output files or datasets.
- Physics papers (including arXiv-first cultures such as high-energy and condensed matter) often post preprints at submission; collaborations may have long author lists and internal review.
- Use **SI units**, proper significant figures, error propagation, and clearly labeled axes with units.

## 4. Engineering and applied sciences

- Show **problem relevance, design requirements, method, validation, and performance versus state of the art** with appropriate benchmarks and standards.
- Include **experimental setup details, uncertainty analysis, and repeatability**, and discuss limitations, scalability, cost, safety, and deployment.
- **Validation** (against analytical solutions, experiments, or independent datasets) is central for simulation and modeling work. Verify and validate separately.
- Patents and **intellectual property** timing: file before public disclosure where relevant.
- Both conferences and journals matter; many fields publish a conference paper first and then an extended journal version (with a substantial new contribution, usually 30 percent or more, and disclosure).

## 5. Computer science and machine learning

- **Conferences are primary venues** (e.g., NeurIPS, ICML, ICLR, CVPR, ACL via ACL Rolling Review, EMNLP, KDD, SIGMOD, STOC/FOCS, CHI, and many others). Journals (JMLR, TPAMI, TOIS, CACM etc.) are also valued; norms differ by subfield.
- **Format:** strict page limits, anonymized (double-blind) submissions, a related work section, experiments and ablations, an appendix for extras; **camera-ready** versions after acceptance.
- **What reviewers want:** a clear problem and contribution list; strong, fairly tuned baselines; ablations; multiple datasets or tasks; variance across seeds; error and failure analysis; compute and hyperparameter reporting; limitations; and societal impact or ethics statements as required.
- **Reproducibility checklists** are mandatory at many venues. Release code, data, and models (anonymously during review via anonymized repositories if needed).
- **Rebuttal phase:** you get a short window (often a few days) to respond to reviewers; be concise, add key experiments if possible, and address score-driving concerns first. The area chair or meta-reviewer decides.
- **Strategy:** write a **teaser figure** on page 1; state contributions as a short bulleted list; ensure the **abstract and introduction** carry the claim; manage the deadline cycle; make the paper skimmable in 3 minutes; use arXiv preprints following the venue's anonymity policy.
- Beware: overclaiming generality from a few benchmarks, weak or untuned baselines, data leakage and contamination, cherry-picked qualitative examples, undisclosed compute advantages, and missing negative results.
- **Theory CS:** author lists are often alphabetical; results are theorem-centered with proofs, often with full proofs in the appendix and sketches in the main text.

## 6. Mathematics and theoretical work

- **Structure:** introduction stating main results and context, preliminaries and notation, theorems with proofs (lemmas, propositions, corollaries), examples and counterexamples, remarks, open problems.
- **State the main theorem precisely** in the introduction, with intuition and why it is interesting and how it relates to known results. Provide **proof strategy overviews** for long proofs.
- Make proofs **correct, complete, and checkable**; define all notation; avoid hidden assumptions; show necessity or tightness where possible, and counterexamples when assumptions are dropped.
- Authors typically listed **alphabetically**. Journals are slow; arXiv postings are standard. Refereeing may take many months.
- Use LaTeX with consistent macros; follow MSC classification codes; check references carefully (MathSciNet, zbMATH).

## 7. Social sciences and psychology

- **Structure:** IMRaD (APA style in psychology), with clearly stated hypotheses, theory, and measures.
- **Open science:** pre-registration, registered reports, open materials and data, and transparency statements (e.g., the 21-word solution or similar) are increasingly expected; report all conditions and measures.
- **Rigor:** adequate power, validated and reliable measures (report reliability coefficients), appropriate handling of nested data (mixed models), effect sizes with CIs, attention to demand characteristics, manipulation checks, and generalizability (WEIRD samples caution).
- **Replication and robustness** matter. Discuss construct validity, internal validity, external validity, and ecological validity.
- **Ethical care** with human participants, deception, and debriefing; report IRB approval.
- **Theory contribution** is central in many top journals: what does the paper change about how we understand a phenomenon?

## 8. Economics and quantitative policy research

- **Structure:** introduction (research question, contribution relative to specific literature, summary of methods and findings, magnitude of results), conceptual framework or model, data, empirical strategy, results, robustness, conclusion. The **introduction is the paper** for many readers, so write it carefully (first page conveys the question, identification strategy, and result).
- **Identification** is the crux: explain the source of exogenous variation, assumptions, and threats; show falsification tests, event-study plots (pre-trends), and sensitivity analyses.
- Working papers (NBER, SSRN, RePEc, institutional series) circulate years before publication; seminar feedback is part of the process. Long review cycles are common.
- Authors often **alphabetical** in economics. Provide replication packages (data, code), which many journals require.
- Be careful with external validity and general equilibrium effects; discuss mechanisms and magnitudes in interpretable units (percent, dollars).

## 9. Humanities and interpretive scholarship

- **Argument-driven:** a clear **thesis** stated early, developed through close reading of primary sources, historiographical or theoretical positioning, and a conclusion on significance. Evidence is textual, archival, visual, or artifact-based.
- **Structure** is less formulaic than IMRaD, but should have a roadmap, a clear line of argument, and strong topic sentences. Engagement with the scholarly conversation ("intervention") in the introduction is critical.
- **Citation style:** Chicago (notes-bibliography), MLA, or field-specific; footnotes carry nuance and sources.
- Many fields value **books and edited volumes** as primary outputs; articles are often longer (6,000 to 12,000 words). Review cycles are long. Single authorship is common.
- Show **archival and source transparency**, translation practices, permissions for images and quotations, and reflexivity about positionality.
- Reviewers look for **originality of argument and sources**, command of the historiography, and quality of prose.

## 10. Qualitative and mixed-methods articles

See `03`. Add: a transparent account of the **research design logic**, **sampling**, **analysis**, **reflexivity**, and **trustworthiness**; thick description and well-chosen quotations; a clear **theoretical contribution** (many qualitative journals expect more than description); and explicit **limitations on transferability**. Use COREQ or SRQR. Respect participant confidentiality in excerpts.

## 11. Review articles

- **Narrative and conceptual reviews:** value comes from synthesis, a **new framework, taxonomy, or research agenda**, not a catalogue. State scope and search approach, evaluate evidence quality, highlight contradictions, and propose testable directions.
- **Systematic reviews and meta-analyses:** pre-registered protocol (PROSPERO or OSF), PRISMA 2020 flow diagram, documented search strategy for multiple databases, dual screening and extraction, risk-of-bias assessment, appropriate synthesis (random-effects meta-analysis, heterogeneity, prediction intervals, subgroup and meta-regression carefully), publication-bias assessment, GRADE certainty, and sensitivity analyses. Share extraction data and code.
- **Scoping reviews:** PRISMA-ScR; map the literature breadth, concepts, and gaps.
- **Umbrella reviews, living reviews, bibliometric and meta-research** have their own standards; follow their guidelines.
- Reviews get heavily cited when they are **timely, well-organized, balanced, and visual** (summary figures and tables); they are rejected when they are unfocused or biased by selective citation.

## 12. Short formats: letters, case reports, brief reports

- **Letters/Communications:** concise, high-impact results, one main claim, brief methods (with full details in supplement), tight introduction, and strong figures. Speed matters; reviewers expect completeness within the constraint.
- **Case reports (CARE):** novelty or teaching value, a clear timeline, patient consent, de-identification, discussion of literature, and a take-home lesson.
- **Brief reports and short communications:** one clear finding, limited scope, an honest acknowledgment of preliminary status.

## 13. Data, software, and methods papers

- **Data papers:** describe collection, structure, quality control, validation, access, and reuse potential; no hypothesis testing required; provide DOIs and licenses; show use cases.
- **Software or tool papers:** state the problem, design, features, benchmarks versus alternatives, availability (open source, license, documentation, tests, continuous integration), and community use. Archive releases (Zenodo) and cite software formally.
- **Methods papers:** demonstrate advantages with **head-to-head comparisons, validation on realistic data, limitations and failure modes, and practical guidance**, plus open implementation.

## 14. Theses and dissertation chapters turned into articles

- Extract **one claim per article**; thesis structure (long literature review, extensive methods) must be compressed into the target journal's format.
- Rewrite the introduction for a general audience of the journal, not for a committee.
- Cut anything not needed for the central argument; move details to supplements.
- Disclose that the content comes from a thesis if required, and check the university repository policy on prior publication.
- Co-author with the supervisor as appropriate under authorship criteria, and agree on order and contributions early.
- Consider publishing as you go (during the PhD), which spreads effort and gives early reviewer feedback.
