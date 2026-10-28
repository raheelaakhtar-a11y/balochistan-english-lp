---
name: balochistan-english-lp
description: "Build Balochistan Winter Programme (TaRL, single-level) English lesson plans as A4 PDFs from the 33-day planner — Lesson Plan, Prep Pack, Student Worksheet — via deterministic HTML to headless-Edge PDF. Day 1 Beginner (letters A B C D) and Day 1 Intermediate (blends and digraphs) are built and reusable as templates. Use for \"make Day N English LP\", \"Beginner/Intermediate Day N\", \"rebuild the LPs on the new planner\", \"fill the blank space on page 4\". NOT multi-level Quetta WSP (multilevel-lp-design), NOT grade-based corpora (curriculum-baked-lesson-plans), NOT scoring (wsp-lp-reviewer)."
metadata:
  disclosure: auto
  surface: home
  last_verified: 2026-10-28
---

# Balochistan Winter Programme: English lesson plans

One day, one level = one `common_*.py` data file (the single source of truth) + one `doc_*.py` per document.
Nothing is drawn by hand: change the data, rebuild, look at the PNGs.

Not multi-level. Earlier Quetta WSP / 40-minute / G1-5 work is void. Urdu and Maths use their own chats.

## Inputs (ask, never assume)

1. The **current planner PDF** (the user pastes the newest one; the 28 Oct `TaRL_English_SLOs_and_33Day_Planner_28Oct.pdf` is the latest seen). A newer planner replaces it: diff the day's SLOs first and tell the user what moved.
2. `LP RULES — WSP lesson plans.docx` (Downloads): approved words only, hear 4 to 5 children not everyone, tracker On track / Practise / Re-teach, no pass-mark line (use `[PENDING: ...]`, never guess), no running or trick games.
3. Books if the day cites them: `english_1.pdf` (printed page = pdf page minus 6), `english_2.pdf`.

## Shape of a lesson (every day)

60 minutes; the last 10 are the exit check. Five A4 pages: 1 roadmap and outcomes, 2 start/I Do, 3 We Do, 4 You Do and check, 5 exit check with footer band. Details and the page-by-page layout decisions are in [reference/layout-rules.md](reference/layout-rules.md).

## Build

Needs Python 3.8+, `pillow`, `pymupdf`, Microsoft Edge (or set `EDGE_PATH`).

```powershell
cd skills\balochistan-english-lp\engine
python -W ignore build.py lpb          # lpb Beginner LP, prepb Prep Pack, wsb Worksheet, lpc Intermediate LP
```

- **Run from PowerShell.** A bash-launched build silently fails to write the PDF.
- Set `PYTHONIOENCODING=utf-8`.
- Output (`<name>.pdf`, `png/<name>_pN.png`) is gitignored. Copy PDFs to the user's Desktop as the next `_vN`; **never overwrite** an earlier version.
- The overflow check only sees document-level overflow. It misses clipping inside zoom wrappers, so **always look at the PNGs** (copy them to a Desktop folder, because the user cannot see the scratchpad). Preview first, save PDFs when the user says so.

## Make a new day or level

1. Copy `common_b.py` (letters) or `common_c.py` (words) to `common_<x>.py`, replace the data, keep the `assert` block: it enforces approved-words-only, no straight-across answers, `b`/`d` never adjacent, and planner-forbidden patterns.
2. Copy the matching `doc_lp_*.py`, point it at the new data, add a key in the `mods` map in `build.py`.
3. Pictures: only text-free object pictures via `kie-ai-imagegen` (`nano-banana-pro`, saved to `img/` as `b1_<word>.jpg` / `c1_<word>.jpg`). Letters and words are live text, never AI-drawn. Kie error 433 = daily cap: stop, never retry in a loop. Missing pictures render as labelled dashed placeholders.
4. Build, view PNGs on every page, then save.

## Gotchas

- f-strings in `doc_*.py`: inline `<style>` needs doubled braces `{{ }}`.
- Fill-the-page: wrap a page's blocks in `<div style="zoom:Z;display:flex;flex-direction:column;justify-content:space-between;height:{content_mm/Z}mm;overflow:hidden">`. Raise Z until text clips or an answer cell wraps in the PNG, then step back (Beginner: p2 1.2, p4 1.08, p5 1.2; Intermediate: p2 1.2, p4 1.12, p5 1.05).
- Fonts: Andika (single-storey a) for beginner readers. Brand: navy #001F3F, gold #F5B301. No Rumi logo, no em dashes. English-medium, no Roman-Urdu glosses.
- Branding: Rumi vs Taleemabad per the router rules; never mix.

## Status (2026-10-28)

| Piece | State |
|---|---|
| Beginner Day 1 LP (A B C D) | v6 saved, 28 Oct planner, page-5 footer band |
| Beginner Day 1 Prep Pack / Worksheet | built on 27 Oct planner (Prep v3, WS v2); not re-checked against 28 Oct |
| Intermediate Day 1 LP (E-I-01 + E-I-06) | v7 saved; footer-band version built, unsaved |
| Open | Intermediate has no `st` words (newly allowed); phrases are ours (`[PENDING]` swap to 33-Day Map phrases); tracker thresholds are ours; Beginner p5 has ~25 mm gap between Your Turn and Exit Check |
