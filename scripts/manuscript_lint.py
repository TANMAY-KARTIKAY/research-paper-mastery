#!/usr/bin/env python3
"""
manuscript_lint.py - quick mechanical diagnostics for a research manuscript.

Usage:
    python manuscript_lint.py manuscript.md|.txt|.docx [--json]

These are HEURISTICS to direct attention, not verdicts. A long sentence can be
fine; a passive verb can be correct in Methods. Judge each flag in context.
"""
import argparse
import json
import re
import sys
from collections import Counter

HEADING_RE = re.compile(
    r"^\s*(?:#{1,6}\s*)?(?:\d+\.?\s+)?"
    r"(abstract|introduction|background|related work|literature review|methods?|"
    r"materials and methods|methodology|results?|results and discussion|findings|"
    r"discussion|conclusions?|limitations|acknowledg(?:e)?ments?|references|"
    r"data availability|supplementary)\s*:?\s*$",
    re.IGNORECASE,
)

HEDGES = [
    "may", "might", "could", "possibly", "perhaps", "seems", "appears",
    "suggests", "somewhat", "relatively", "probably", "potentially",
]
OVERCLAIMS = [
    "prove", "proves", "proven", "proved", "clearly shows", "clearly demonstrates",
    "undoubtedly", "obviously", "revolutionary", "groundbreaking", "unprecedented",
    "paradigm shift", "always", "never", "conclusively", "definitively",
]
INTENSIFIERS = ["very", "extremely", "highly", "quite", "really", "remarkably", "importantly"]
WORDY = {
    r"\bin order to\b": "to",
    r"\bdue to the fact that\b": "because",
    r"\bit is worth noting that\b": "(delete)",
    r"\bit should be noted that\b": "(delete)",
    r"\bit is interesting to note that\b": "(delete)",
    r"\ba number of\b": "several / the number",
    r"\bhas the ability to\b": "can",
    r"\bin the case of\b": "in / for",
    r"\bwith respect to\b": "about / for",
    r"\bthe fact that\b": "that (or rephrase)",
    r"\butili[sz]e[sd]?\b": "use",
    r"\bfacilitate[sd]?\b": "help",
}
CAUSAL = [
    "causes", "caused", "leads to", "led to", "results in", "resulted in",
    "effect of", "impact of", "drives", "driven by",
]
ABBREV_STOP = {
    "DNA", "RNA", "USA", "UK", "EU", "UN", "PDF", "URL", "HTML", "CSV", "AI",
    "IEEE", "ACM", "SI", "ID", "OK", "TV", "US", "PCR", "MRI", "CT", "GDP",
    "SD", "SEM", "CI", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
}
PASSIVE_RE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(\w+(?:ed|en))\b", re.IGNORECASE
)
NOMINAL_RE = re.compile(
    r"\b(?:perform(?:ed)?|conduct(?:ed)?|carr(?:y|ied)(?: out)?|make|made|give|gave|"
    r"provide[ds]?)\s+(?:an?|the)\s+\w*(?:ation|ment|ysis|ance|ence|ing)\b",
    re.IGNORECASE,
)
CITE_RE = re.compile(
    r"\[\d+(?:[,\u2013\-\s]*\d+)*\]|"            # [1], [1,2], [1-3]
    r"\([A-Z][A-Za-z\-']+(?: et al\.?)?(?:,|\s)\s*\(?\d{4}[a-z]?\)?"  # (Smith 2020), (Smith et al., 2020)
    r"|\b[A-Z][A-Za-z\-']+ et al\.?\s*\(\d{4}[a-z]?\)"                # Smith et al. (2020)
)
PVAL_RE = re.compile(r"\bp\s*[<=>\u2264\u2265]\s*0?\.\d+", re.IGNORECASE)
EFFECT_RE = re.compile(
    r"\b(95\s?%\s?CI|confidence interval|credible interval|effect size|cohen'?s d|"
    r"odds ratio|hazard ratio|risk ratio|\bOR\b|\bHR\b|\bRR\b|mean difference|r\s*=|"
    r"eta|R2|R\^2|beta)\b",
    re.IGNORECASE,
)
SIGNIF_WORD_RE = re.compile(r"\bsignificant(?:ly)?\b", re.IGNORECASE)
FIG_REF_RE = re.compile(r"\b(?:Fig(?:ure)?s?\.?|Table)\s*S?\d+", re.IGNORECASE)


def read_text(path):
    if path.lower().endswith(".docx"):
        try:
            import docx  # python-docx
        except ImportError:
            sys.exit("Reading .docx needs python-docx: pip install python-docx --break-system-packages")
        d = docx.Document(path)
        return "\n".join(p.text for p in d.paragraphs)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def split_sections(text):
    sections, current, buf = {}, "Front matter", []
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            sections[current] = "\n".join(buf)
            current, buf = m.group(1).title(), []
        else:
            buf.append(line)
    sections[current] = "\n".join(buf)
    return {k: v for k, v in sections.items() if v.strip()}


def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+(?:\.\d+)?", s)


def sentences(s):
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\b(et al|e\.g|i\.e|Fig|Figs|vs|cf|approx|Eq|Dr|Prof)\.", r"\1<dot>", s)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\[\(])", s)
    return [p.replace("<dot>", ".").strip() for p in parts if len(p.split()) >= 3]


def count_terms(text, terms):
    low = text.lower()
    out = {}
    for t in terms:
        n = len(re.findall(r"\b" + re.escape(t) + r"\b", low))
        if n:
            out[t] = n
    return out


def find_undefined_abbrevs(text):
    defined = set(re.findall(r"\(([A-Z][A-Za-z]{1,7}s?)\)", text))
    defined |= {d.rstrip("s") for d in defined}
    counts = Counter(re.findall(r"\b[A-Z]{2,7}s?\b", text))
    flagged = []
    for abbr, n in counts.items():
        base = abbr.rstrip("s") if abbr.endswith("s") and len(abbr) > 2 else abbr
        if base in ABBREV_STOP or abbr in ABBREV_STOP:
            continue
        if base in defined or abbr in defined:
            continue
        flagged.append((abbr, n))
    return sorted(flagged, key=lambda x: -x[1])[:15]


def analyze(text):
    r = {}
    all_words = words(text)
    sents = sentences(text)
    r["total_words"] = len(all_words)
    r["sentence_count"] = len(sents)

    secs = split_sections(text)
    r["section_words"] = {k: len(words(v)) for k, v in secs.items()}

    lens = [len(words(s)) for s in sents] or [0]
    r["avg_sentence_length"] = round(sum(lens) / len(lens), 1)
    r["long_sentences"] = [
        {"words": len(words(s)), "preview": s[:110] + ("..." if len(s) > 110 else "")}
        for s in sents if len(words(s)) > 40
    ][:8]

    passives = PASSIVE_RE.findall(text)
    r["passive_hints"] = len(passives)
    r["passive_rate_per_100_sentences"] = round(100 * len(passives) / max(len(sents), 1), 1)
    r["nominalization_hints"] = [m.group(0) for m in NOMINAL_RE.finditer(text)][:10]

    r["hedges"] = count_terms(text, HEDGES)
    r["overclaims"] = count_terms(text, OVERCLAIMS)
    r["intensifiers"] = count_terms(text, INTENSIFIERS)
    def _label(pat):
        lab = pat.replace(r"\b", "").replace("\\", "")
        return {"utili[sz]e[sd]?": "utilize/utilise", "facilitate[sd]?": "facilitate"}.get(lab, lab)

    r["wordy_phrases"] = {
        _label(pat): {"count": len(re.findall(pat, text, re.I)), "try": fix}
        for pat, fix in WORDY.items() if re.search(pat, text, re.I)
    }
    r["causal_language"] = count_terms(text, CAUSAL)

    cites = CITE_RE.findall(text)
    r["citation_markers"] = len(cites)
    r["citations_per_1000_words"] = round(1000 * len(cites) / max(len(all_words), 1), 1)

    pvals = PVAL_RE.findall(text)
    effects = EFFECT_RE.findall(text)
    sig = SIGNIF_WORD_RE.findall(text)
    r["stats"] = {
        "p_values": len(pvals),
        "effect_size_or_interval_mentions": len(effects),
        "'significant' mentions": len(sig),
    }
    flags = []
    if len(pvals) >= 3 and len(effects) == 0:
        flags.append("p-values reported but no effect sizes or intervals detected")
    if len(sig) >= 5 and len(pvals) == 0:
        flags.append("'significant(ly)' used often with no p-values; quantify or choose another word")
    r["stats"]["flags"] = flags

    r["undefined_abbreviations_candidates"] = find_undefined_abbrevs(text)

    starters = Counter(
        " ".join(s.split()[:2]).lower() for s in sents if len(s.split()) > 4
    )
    r["repeated_sentence_openers"] = [(k, v) for k, v in starters.most_common(6) if v >= 4]

    r["figure_table_mentions"] = len(FIG_REF_RE.findall(text))

    # Section proportion warnings
    warn = []
    sw = {k.lower(): v for k, v in r["section_words"].items()}
    meth = sum(v for k, v in sw.items() if "method" in k or "material" in k)
    res = sum(v for k, v in sw.items() if k.startswith("result") or k == "findings")
    disc = sum(v for k, v in sw.items() if "discussion" in k)
    intro = sum(v for k, v in sw.items() if k in ("introduction", "background"))
    if intro > 1500:
        warn.append(f"Introduction is {intro} words; consider trimming to the gap and contribution.")
    if meth and res and meth > 2.5 * res:
        warn.append("Methods are much longer than Results; move detail to supplement?")
    if disc and res and disc > 2 * res:
        warn.append("Discussion is much longer than Results; check for restating or overreach.")
    if "limitations" not in sw and disc and "limitation" not in text.lower():
        warn.append("No limitations discussion detected.")
    abstract = sw.get("abstract", 0)
    if abstract and (abstract > 350):
        warn.append(f"Abstract is {abstract} words; many journals cap near 150-300.")
    r["structure_warnings"] = warn
    return r


def print_report(r):
    p = print
    p("=" * 64)
    p("MANUSCRIPT LINT REPORT (heuristics - judge each flag in context)")
    p("=" * 64)
    p(f"Words: {r['total_words']}   Sentences: {r['sentence_count']}   "
      f"Avg sentence length: {r['avg_sentence_length']} words")
    p("\n-- Section word counts --")
    for k, v in r["section_words"].items():
        p(f"  {k:<28}{v}")
    if r["structure_warnings"]:
        p("\n-- Structure warnings --")
        for w in r["structure_warnings"]:
            p("  * " + w)

    p("\n-- Sentence length (flag > 40 words) --")
    if r["long_sentences"]:
        for s in r["long_sentences"]:
            p(f"  [{s['words']}w] {s['preview']}")
    else:
        p("  none")

    p("\n-- Voice and wordiness --")
    p(f"  Passive-voice hints: {r['passive_hints']} "
      f"({r['passive_rate_per_100_sentences']} per 100 sentences)")
    if r["nominalization_hints"]:
        p("  Nominalizations (try a direct verb): " + "; ".join(r["nominalization_hints"]))
    if r["wordy_phrases"]:
        for k, v in r["wordy_phrases"].items():
            p(f"  '{k}' x{v['count']} -> {v['try']}")

    p("\n-- Claim calibration --")
    p(f"  Hedges: {r['hedges'] or 'none'}")
    p(f"  Overclaim words: {r['overclaims'] or 'none'}")
    p(f"  Intensifiers: {r['intensifiers'] or 'none'}")
    if r["causal_language"]:
        p(f"  Causal language (confirm the design supports it): {r['causal_language']}")

    p("\n-- Evidence and citations --")
    p(f"  Citation markers: {r['citation_markers']} "
      f"({r['citations_per_1000_words']} per 1000 words)")
    p(f"  Stats: {r['stats']}")
    p(f"  Figure/table mentions: {r['figure_table_mentions']}")

    if r["undefined_abbreviations_candidates"]:
        p("\n-- Abbreviations possibly never defined (check) --")
        p("  " + ", ".join(f"{a}({n})" for a, n in r["undefined_abbreviations_candidates"]))
    if r["repeated_sentence_openers"]:
        p("\n-- Repeated sentence openers --")
        p("  " + ", ".join(f"'{k}' x{v}" for k, v in r["repeated_sentence_openers"]))
    p("\nReminder: also run the consistency pass (numbers, terms) by hand against tables/figures.")


def main():
    ap = argparse.ArgumentParser(description="Heuristic manuscript diagnostics")
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    a = ap.parse_args()
    report = analyze(read_text(a.path))
    if a.json:
        print(json.dumps(report, indent=2, default=list))
    else:
        print_report(report)


if __name__ == "__main__":
    main()
