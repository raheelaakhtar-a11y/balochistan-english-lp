---
name: balochistan-maths-lp
description: "Build Balochistan Winter Programme (TaRL, single-level) Maths lesson plans as A4 PDFs from the 33-day planner: Lesson Plan, Prep Pack, Student Worksheet, via deterministic HTML to headless-Edge PDF. Level 1 (Beginner) Day 1, SLO M-B-01 Count objects up to 20, is built and reusable as the template. Every counted group is drawn as SVG with an asserted count, so a picture can never disagree with its number. Use for \"make Day N Maths LP\", \"Beginner Maths Day N\", \"rebuild the maths LPs on the new planner\", \"the picture does not match the text\", \"fill the blank space on page 1\". NOT English (balochistan-english-lp), NOT multi-level Quetta WSP (multilevel-lp-design), NOT grade-based corpora (curriculum-baked-lesson-plans), NOT scoring (wsp-lp-reviewer)."
metadata:
  disclosure: auto
  surface: home
  last_verified: 2026-10-28
---

# Balochistan Winter Programme: Maths lesson plans

One day, one level = one `common_*.py` data file (the single source of truth) + one `doc_*.py` per document.
Nothing is drawn by hand and no count is typed twice: change the data, rebuild, look at the PNGs.

Sibling of `balochistan-english-lp`. Same page design and 60-minute shape, **different lesson**: a Maths plan is built from the
Maths SLO and the Grade 1 book, never by porting English activities. Not multi-level. Earlier Quetta WSP / 40-minute / G1-5 work
is void. Urdu uses its own chat.

## When to use / not use

| Ask | Use |
|---|---|
| "Make Beginner Maths Day N", "rebuild on the new planner", "the picture says apples, the text says stones" | this skill |
| English LP | `balochistan-english-lp` |
| Quetta multi-level WSP page design | `multilevel-lp-design` |
| Score an LP | `wsp-lp-reviewer` |

## Inputs (ask, never assume)

1. The **current Maths planner PDF**: `TaRL_Math_SLOs_and_33Day_Planner_28Oct.pdf` is the latest seen. The user pastes the newest; a newer one replaces it. Before building, **diff the day's SLO code, sentence, support SLOs, "Difficulty" line and "Builds on" column** and tell the user what moved. The planner changed twice during Day 1 and each change reshaped the lesson.
2. The book: `Maths books\math_1 (1).pdf` (Grade 1, scanned, no text layer; **printed page = pdf page minus 4**). Read pages as images. See [reference/planner-and-book.md](reference/planner-and-book.md) for what each page offers.
3. The user's format reference if they give one (English approved set: Lesson Plan v3, Prep Pack v2, Worksheet v2).

If the planner marks a day as Practise-and-check, the lesson changes shape (no teach-and-model first). Read the day's row before designing.

## Shape of a lesson (every day)

60 minutes, fixed: **5 warm-up + 5 hook + 20 I Do + 12 We Do + 8 You Do + 10 exit check**. The minutes appear **once**, in the coloured 60-minute bar on page 1.
Five A4 pages: 1 roadmap and outcomes, 2 warm-up and hook, 3 I Do, 4 We Do, 5 Your Turn answers, exit check, score and decide, key facts, at home.
Page-by-page content and the activities used for Day 1 are in [reference/lesson-design.md](reference/lesson-design.md).

Three documents per day, all fed by one data block:

| Document | Pages | Source | Build key |
|---|---|---|---|
| Lesson Plan | 5 | `doc_lp_m8.py` | `lp` |
| Prep Pack (number chart, call sheet, picture cards, Ten Box mats, tally) | 7 | `doc_prep_m6.py` | `prep` |
| Student Worksheet (count and circle, draw dots, dot-to-dot, exit check) | 2 | `doc_ws_m6.py` (+ `doc_ws.py` CSS) | `ws` |

Engine import chain: `common.py` (design system, icons, `group_svg`) → `common_v3.py` → `common_m.py` / `common_m5.py` (maths data and Ten Box / tick / dot-to-dot helpers) → `common_m6.py` (stone icon, stone Ten Boxes) → `doc_*`. `common_v3.py` only supplies the re-exports now; its drawn-people helper is retired.

## Build

Needs Python 3.8+, `pillow`, `pymupdf`, Microsoft Edge (or set `EDGE_PATH`).

```powershell
cd skills\balochistan-maths-lp\engine
$env:PYTHONIOENCODING = "utf-8"
python -W ignore build.py lp        # lp, prep, ws; no argument builds all three
```

Expect `lp: pdf=True pages=5 overflow=OK`, `prep ... pages=7`, `ws ... pages=2`.

- **Run from PowerShell.** A bash-launched Edge silently fails to write the PDF.
- Output (`*.html`, `*.pdf`, `png/<stem>_pN.png`) is gitignored.
- **Never overwrite the user's files.** Copy each PDF to the user's Desktop day folder as the next `_vN`, e.g. `Desktop\Level 1 Maths Day 1\L1 Maths Day 1 - 1 Lesson Plan_v9.pdf`. Prep Pack is `- 2 Prep Pack`, Worksheet `- 3 Student Worksheet`. Check the folder for the highest existing `_vN` first.
- The overflow check sees only document-level overflow. It misses clipping inside zoom wrappers. **Always look at every page PNG** (copy PNGs to a Desktop folder: the user cannot see the scratchpad). Preview first, save PDFs when the user says so.
- If the user says "Lesson Plan only", do not build or deliver the Prep Pack and Worksheet. Say they are unchanged.

## Make a new day

1. Read the day's planner row (SLO code and sentence, "Difficulty", "Builds on", day type). **Quote the SLO code and sentence verbatim** on page 1.
2. Copy `common_m5.py` to `common_<x>.py` and replace the data: hook count, piles, cards, worksheet items, exit items. **Keep every `assert`**. They enforce: no number reused between worked example, You Do and exit check; three answer options containing the right one; numbers within 1 to 20 (or the day's range); scatter layouts only for 9 or fewer objects (planner: "in rows or small groups"). Add new asserts for the new day's Difficulty line.
3. Copy `doc_lp_m8.py`, `doc_prep_m6.py`, `doc_ws_m6.py`, point them at the new data module, add keys to `MODS` in `build.py`.
4. Redesign the **activities** from the SLO and the book. The page design carries over; the activities do not. Do not reuse Day 1's stone-counting lesson for, say, comparing numbers.
5. Pictures: counted groups are SVG (`group_svg`, `boxes_svg`, `ticked_svg`, `dotdot_svg`); only text-free scene illustrations come from Kie (see below). Add an icon for any new object (see the next section).
6. Build, look at every PNG, then save as the next `_vN`.

## A picture must show exactly what the text names

The user rejected a version that said "stones" while apples were drawn. Rules now enforced:

- Text says "stones" → the picture draws pebbles (`stone` icon in `common_m6.py`, four shapes, four greys). `common.icon` and `common_m.icon` are monkeypatched so every helper draws through it.
- `doc_lp_m8.py` asserts the stone stages contain no apple (`#E0352B`) or ball (`#F7C531`) colours and do contain a stone grey. Copy this pattern for any new object: **assert the object's colour is present and the other objects' colours are absent in that stage.**
- A stage that really is about apples, balls or fish (Stage 2 picture cards) names them in the text: "(6 apples)", "(9 balls)", "(13 fish)".
- Never let Kie draw a counted group (it miscounts). Scenes show no more than 4 countable objects.

## Scene pictures (Kie)

`engine/kie_gen.py` makes text-free flat-vector scenes with `nano-banana-pro`: `teacher_point`, `teacher_oops`, `pair_book` (plus `kids_wave`, copied from the English set). Same style sentence as English so the subjects match.

```powershell
$env:AGENT_SKILLS_REPO = "C:\path\to\agent-skills-taleemabad"   # holds .env with KIE_API_KEY and skills\kie-ai-imagegen\scripts\kie_throttle.py
python kie_gen.py balance
python kie_gen.py run scene_teacher_point        # or: run all
```

- `KIE_API_KEY` missing: say so and point to KEYS.md; never probe for it.
- **Error 433 = daily cap: stop. Never loop or retry.** Reuse the existing scenes, build with placeholders, tell the user, and retry on a later day (the cap blocked 19 to 20 Oct and had reset by 28 Oct).
- Raw PNGs go to `engine/img/raw/`; `build.py` converts them to `engine/img/*.jpg` (max 760 px).
- Drawn-SVG people were rejected as "bad pictures"; people are Kie illustrations only.

## Page-fill and zoom (when a change leaves blank space)

The user's standing preference: if a change leaves a gap, **rebalance the page; never fill it by repeating information** (a duplicated 60-minute grid was rejected: "why have you repeated the 60 min breakdown, remove that").

Levers, in order: box spacing / padding variables, then the page's zoom wrapper, then a slightly larger illustration. Day 1 values in `doc_lp_m8.py`:

| Page | Setting |
|---|---|
| 1 | content `top:51mm; zoom:1.07; --g:3.6mm; --pd:3.5mm` via a `.p1b` style block |
| 2 | zoom 1.1 (1.11 overflows) |
| 3 | zoom 1.1 |
| 4 | zoom .97 |
| 5 | as built |

Zoom reflow is non-linear: probe values, rebuild, look. Inline `<style>` in an f-string needs doubled braces `{{ }}` or the build fails with `NameError: name 'margin' is not defined`.

## Content rules (all from the user)

- English medium. No Roman-Urdu glosses. No Rumi logo, no Rumi WhatsApp number. No em dashes.
- Learning outcome box (sky) full width on page 1; **Today's Goal (teal) directly after it**. No "By the end of today, children can". No "Counting only today".
- Spell-check every printed word. All answers come from the one data block.
- Design: the English plan design (navy bar, gold DAY badge, mint/sky/cream boxes, Nunito + Inter). Not a replica of the Pindi sample maths LP, and not the Taleemabad-brand look unless asked. Never mix Rumi and Taleemabad palettes.
- A rejected design means **ask before rebuilding** (the user dislikes copies of the sample).
- Pass mark: no pass-mark line unless the planner gives one; use `[PENDING: ...]`, never guess.

## Gotchas

- Edge default path `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`; set `EDGE_PATH` otherwise.
- CSS: `--grey` is a background colour here; text that must be readable uses `--mid`.
- Plurals: use `pl()` (`fish` stays `fish`); never append "s" by hand.
- Documents must import `common_m6` so the stone patch is applied before any group is drawn.
- The Day 1 ribbon shows Days 1 to 2 (gold) and 31 to 33 (green): update it from the planner, never copy.

## Status (2026-10-28)

| Piece | State |
|---|---|
| Beginner Day 1 Lesson Plan (M-B-01) | v8 saved: goal under outcome, minutes shown once, page 1 rebalanced |
| Beginner Day 1 Prep Pack / Worksheet | v6 saved, current; not re-issued since the v7/v8 Lesson Plan edits (data unchanged) |
| Beginner Days 2 to 33 | not built. Day 2 is M-B-01 Practise and check (no new SLO) |
| Open | pass-mark line `[PENDING]`; "Ten Box" (ten-frame) wording to confirm with the programme team; the book shows objects only to 9 (the plan says so) |

More history and decisions already made with the user: [reference/rules-and-history.md](reference/rules-and-history.md).
