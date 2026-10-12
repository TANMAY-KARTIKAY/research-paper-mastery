# 02. Section-by-Section Craft

## Contents
1. The overall architecture (hourglass)
2. Title
3. Abstract
4. Keywords
5. Introduction
6. Methods
7. Results
8. Discussion
9. Conclusion
10. Acknowledgments, funding, declarations
11. Paragraph and section mechanics
12. Common failure patterns by section

## 1. The overall architecture

Most empirical papers follow **IMRaD** (Introduction, Methods, Results, and Discussion) because readers navigate by it. Think of it as an **hourglass**: broad context narrowing to a precise question (Introduction), the narrowest point being your methods and results, then widening back to implications (Discussion). Adapt headings to the venue (e.g., Methods after Discussion in some high-impact journals; Related Work and Experiments in CS; Theorem-Proof in math).

Every section answers one question for the reader:
- Introduction: *Why should I care, and what exactly did you do?*
- Methods: *Can I trust and reproduce how you did it?*
- Results: *What did you find?*
- Discussion: *What does it mean, and how sure are you?*

## 2. Title

- Specific, informative, and findable. Include the key concepts, population or system, and, where honest, the main finding.
- **Declarative titles** ("X reduces Y in Z") are engaging but must be fully supported by the evidence. **Descriptive titles** ("Effects of X on Y in Z") are safer; **question titles** work for open questions.
- Avoid: vague words ("Study of", "Investigations into", "Towards"), unexplained abbreviations, puns that block searching, overclaiming ("Proof that").
- Length: usually 10 to 20 words; respect journal limits.
- Write ten candidate titles; test them for search-engine discoverability and for whether a stranger understands the topic.

## 3. Abstract

Many editors decide from the title and abstract alone, and it is often the only part read. Write it last, then check it matches the paper.

**Structured or unstructured, use the same logic:**
1. **Context and problem** (1 to 2 sentences): why it matters.
2. **Gap or objective** (1 sentence): what was unknown or what you set out to do.
3. **Approach** (1 to 2 sentences): design, data, sample size, key methods.
4. **Key results** (2 to 3 sentences): the main findings **with numbers** (effect sizes, intervals, accuracy, n).
5. **Conclusion and implication** (1 to 2 sentences): what it means, scaled to the evidence.

Rules:
- Only include what appears in the paper. No new claims, no citations in most venues.
- Put numbers in, not "significantly improved". Say how much.
- Respect word limits (commonly 150 to 300).
- Make it self-contained: define abbreviations that are essential, or avoid them.
- Read it as a stranger. Could they decide whether to read on?

## 4. Keywords

Choose terms people actually search, including synonyms not in the title. Check the journal's controlled vocabulary (e.g., MeSH in biomedicine, ACM CCS, JEL codes, PACS/PhySH). Avoid unusual coinages.

## 5. Introduction

**Job:** convince the reader the question matters and is unresolved, and state what you did. Aim for **600 to 1,000 words** in most journals unless told otherwise; shorter in letters and conference papers.

**Structure (tested over decades):**
1. **Hook and stakes** (1 paragraph): the broad problem and why it matters, concretely.
2. **What is known** (1 to 3 paragraphs): the most relevant prior work, synthesized, not listed. Move from general to specific.
3. **The gap or tension** (1 paragraph): what is unknown, contradicted, or unsolved, and the consequence. Use "However", "Yet", or "Despite" deliberately at this pivot.
4. **Your approach and contribution** (1 paragraph): "Here we..." State the question, the approach, and the main finding or contribution. Many modern journals want the main result stated here. Do not make the reader wait.
5. **Optional roadmap**: one sentence on structure, mainly for long or theoretical papers. Skip in short papers.

**Quality checks:**
- Could a reader in an adjacent field follow the first paragraph?
- Is the gap framed as a problem someone cares about?
- Do citations support specific claims rather than decorate?
- Does the last paragraph promise exactly what the paper delivers?
- Avoid the "history of the universe" opening, and avoid opening with a dictionary definition.

## 6. Methods

**Job:** give enough detail for an expert to evaluate and reproduce. Past tense, mostly active voice where possible ("We measured..."). Passive is acceptable when the actor is irrelevant.

**Typical order:** study design, setting and participants or materials, ethical approval and consent, procedures, measures and variables, data processing, statistical or analytical methods, software and versions, data and code availability.

- **Justify choices**, do not just list them. "We used X because Y" pre-empts a reviewer objection.
- Cite established methods; describe in detail only what is new or modified.
- Specify **sample size rationale** (power analysis or constraints), **inclusion/exclusion criteria**, **randomization and blinding**, **handling of missing data and outliers**, and **pre-specified versus exploratory analyses**.
- Report **software, packages, versions, hardware, random seeds** where relevant.
- Use **subheadings** so reviewers can find what they check first (sampling, statistics, ethics).
- Follow the relevant **reporting guideline** (CONSORT, PRISMA, STROBE, ARRIVE, etc.; see `03` and `09`).
- Put long protocols, reagent tables, or derivations in supplementary files with a short pointer.

## 7. Results

**Job:** report what you found, organized to answer your questions, without interpretation.

- **Order by the logic of the argument**, not the chronology of experiments. Mirror the order of questions in the Introduction and Methods.
- Open each subsection with the **question or purpose**, then the finding, then the evidence ("To test whether X, we... X was higher in A than B (mean difference 4.2, 95% CI 2.1 to 6.3; Fig. 2a)").
- Report **effect sizes with uncertainty**, exact p-values (or equivalent), sample sizes per analysis, and which test was used if not obvious.
- Point to every figure and table in the text, and **do not repeat every number** shown there; highlight the key ones.
- Report **unexpected, null, and contradicting results**, including failed controls and excluded data with reasons.
- Separate **pre-planned** from **exploratory** analyses.
- Keep interpretation minimal. A brief "this suggests" sentence is fine when it aids understanding, but save the main interpretation for the Discussion (some fields and "Results and Discussion" sections combine them).

## 8. Discussion

**Job:** turn results into understanding while staying honest. This is where many papers fail.

**Recommended structure:**
1. **Principal findings** (1 paragraph): answer the question stated in the Introduction in plain words. Do not simply repeat the Results.
2. **Interpretation and mechanism or explanation**: what do the findings mean? Offer the most plausible explanation and **at least one serious alternative**.
3. **Relation to prior work**: where you agree, disagree, and why (differences in method, population, power). Engage the strongest competing study.
4. **Implications**: theoretical, methodological, practical, or policy, scaled to the evidence.
5. **Limitations** (1 paragraph, specific): what could bias or limit generalization, and what you did to mitigate it. Say which conclusions are robust and which are tentative.
6. **Future directions** (a few sentences): concrete next studies, not generic "more research is needed".
7. Close with a **take-home sentence**.

**Quality checks:**
- Does every claim trace back to a result?
- Are causal words ("causes", "leads to") used only with causal designs?
- Did you discuss why results might be wrong or limited, before a reviewer does?
- Are you generalizing beyond the sample, setting, or time period?

## 9. Conclusion

Short (one paragraph or a few). Restate the answer, the significance, and the main caveat. No new data, no new citations, no grand claims beyond the evidence. Some journals fold this into the Discussion.

## 10. Acknowledgments, funding, and declarations

- Acknowledge non-author contributors (with permission), funders (with grant numbers), and technical help.
- Declare **conflicts of interest**, **ethics approvals**, **consent**, **data and code availability**, **author contributions (CRediT)**, and **AI-tool use** if the journal requires it.
- Missing declarations cause desk delays and can look like concealment.

## 11. Paragraph and section mechanics

- **One idea per paragraph**, announced in the **first sentence** (topic sentence) and developed or evidenced after.
- Use the **old-to-new** principle: begin sentences with familiar information and end with new information (the stress position).
- Link paragraphs with **logical transitions** (contrast, consequence, example), not filler ("Moreover" repeated).
- Keep related **sections balanced**. A 3,000-word Methods with a 400-word Results suggests a structural problem.
- Use **headings and subheadings** that state content, and in some fields findings ("Treatment X reduces Y").
- Run a **reverse outline** (one sentence per paragraph) and read the sentences in order. They should form a coherent argument.

## 12. Common failure patterns by section

| Section | Typical failure | Fix |
|---|---|---|
| Title | Vague, overclaiming, or too clever | Specific and searchable, claim matched to evidence |
| Abstract | Background-heavy, no numbers | Cut context, add results with quantities |
| Introduction | Literature dump; gap not shown; too long | Synthesize, state the consequential gap, trim |
| Methods | Missing details; unjustified choices; no sample rationale | Add reproducibility details and reasons |
| Results | Interpretation mixed in; every number repeated; no order | Structure by question; highlight key values |
| Discussion | Restates results; ignores alternatives; overclaims | Interpret, compare, concede limits, scale claims |
| Conclusion | New claims; vague "more research needed" | Concise answer, significance, one caveat |
| Whole paper | Inconsistent numbers or terminology | Consistency pass against source tables |
