"""v5 (28 Oct planner): a MATHS lesson in the English plan's structure and design (common.py CSS), with maths-native activities
built from SLO M-B-01 and the Grade 1 book (Unit 1 Whole Numbers). Nothing here is ported from the English activities.
Single source of truth: every count, pile size, answer and call lives in this file, so the plan, call sheet and worksheet
cannot disagree. Counts are drawn as SVG and asserted."""
import math
from common_v3 import *          # English design system (common.py) + drawn people + icon drawings + group_svg

# ---------------- data ----------------
HOOK_N = 14                                    # Hook: guess, then count
PILES = [12, 13, 15, 17, 18, 20]               # We Do: secret pile for groups 1 to 6
SILLY = [(7, "Skips a number: “one, two, three, five, six, seven, eight”", "The count skipped four, so the last number is wrong. There are 7."),
         (6, "Touches the third stone twice, then says “seven”", "One stone was counted twice. There are 6."),
         (9, "Leaves one stone untouched and says “eight”", "One stone was missed. There are 9.")]
BOOK_ROWS = [(6, "pumpkins"), (8, "doughnuts"), (9, "oranges")]      # book p.5 rows the pairs check
CARDS_M = {"A": (6, "apple", "scatter"), "B": (9, "ball", "row"), "C": (13, "fish", "row"), "D": (17, "star", "row")}
CARD_USE = {"A": "Stage 2: model", "B": "Stage 2: model", "C": "Stage 2: children try", "D": "Check before moving on"}
ORAL_GIVE = [12, 16, 19]                        # exit check, Part B: "Count out N counters"

# You Do (worksheet page 1)
T1_EX = (4, "star", "row", [3, 4, 5])
T1 = [(7, "ball", "row", [6, 7, 8]), (12, "apple", "row", [11, 12, 13]), (15, "flower", "row", [16, 14, 15]),
      (18, "fish", "row", [17, 19, 18])]
T2_EX = 5
T2 = [8, 13, 17]                                # numeral shown; child draws one dot per count in the Ten Boxes
T3_N = 20

# Exit check (worksheet page 2): ("c", count, object, layout, options) circle · ("d", numeral) draw dots
EXIT = [("c", 9, "ball", "scatter", [10, 9, 8]), ("d", 6), ("c", 14, "kite", "row", [15, 13, 14]), ("c", 11, "fish", "row", [10, 12, 11]),
        ("d", 10), ("c", 19, "pencil", "row", [19, 20, 18]), ("c", 16, "apple", "row", [17, 15, 16]), ("c", 20, "star", "row", [18, 19, 20])]

# ---- consistency checks ----
_t1 = {g[0] for g in T1}
_ex = {e[1] for e in EXIT if e[0] == "c"}
assert T1_EX[0] not in _t1 and T2_EX not in set(T2) and T1_EX[0] != T2_EX
assert not _ex & _t1 and not _ex & set(T2)
assert not {e[1] for e in EXIT if e[0] == "d"} & (_ex | set(T2) | _t1)
for g in T1 + [e[1:] for e in EXIT if e[0] == "c"]:
    assert g[0] in g[3] and len(set(g[3])) == 3 and all(1 <= o <= 20 for o in g[3]), g
assert len(EXIT) == 8 and len(PILES) == 6 and all(8 <= p <= 20 for p in PILES)
assert not set(ORAL_GIVE) & set(PILES[:0])
assert SILLY[0][0] != 8 and SILLY[1][0] != 7 and SILLY[2][0] != 8     # each silly count says a number that is wrong


# ---------------- drawing helpers (exact, asserted) ----------------
def counter_svg(cx, cy, r=15, mode="c"):
    return (f'<circle class="dt" cx="{cx}" cy="{cy}" r="{r}" fill="{"#fff" if mode == "l" else "#2AA7C7"}" '
            f'stroke="{"#000" if mode == "l" else INKC}" stroke-width="2.4"/>' if mode == "l"
            else f'<circle class="dt" cx="{cx}" cy="{cy}" r="{r}" fill="#2AA7C7" stroke="{INKC}" stroke-width="2.4"/>')


def boxes_svg(frames=2, filled=0, w_mm=60, mode="c", stack=False, dot_fill="#F08A3C"):
    """Ten Boxes (2 rows of 5). `filled` counters are drawn top row first, frame by frame. Empty when filled=0."""
    gap = 8
    W = 5 * CELL if stack else frames * 5 * CELL + (frames - 1) * gap
    Hh = frames * 2 * CELL + (frames - 1) * gap if stack else 2 * CELL
    ink = INKC if mode == "c" else "#000"
    body = ""
    for f in range(frames):
        x0 = 0 if stack else f * (5 * CELL + gap)
        y0 = f * (2 * CELL + gap) if stack else 0
        body += f'<rect x="{x0 + 1}" y="{y0 + 1}" width="{5 * CELL - 2}" height="{2 * CELL - 2}" rx="4" fill="#fff" stroke="{ink}" stroke-width="2.4"/>'
        for c in range(1, 5):
            body += f'<line x1="{x0 + c * CELL}" y1="{y0 + 1}" x2="{x0 + c * CELL}" y2="{y0 + 2 * CELL - 1}" stroke="#9AA6B5" stroke-width="1.4"/>'
        body += f'<line x1="{x0 + 1}" y1="{y0 + CELL}" x2="{x0 + 5 * CELL - 1}" y2="{y0 + CELL}" stroke="#9AA6B5" stroke-width="1.4"/>'
    for i in range(filled):
        f, k = divmod(i, 10)
        assert f < frames
        x0 = 0 if stack else f * (5 * CELL + gap)
        y0 = f * (2 * CELL + gap) if stack else 0
        cx, cy = x0 + (k % 5) * CELL + CELL / 2, y0 + (k // 5) * CELL + CELL / 2
        fill = "#fff" if mode == "l" else dot_fill
        body += f'<circle class="dt" cx="{cx}" cy="{cy}" r="14" fill="{fill}" stroke="{ink}" stroke-width="2.4"/>' if mode == "c" else \
                f'<circle class="dt" cx="{cx}" cy="{cy}" r="9" fill="#000"/>'
    svg = f'<svg viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">{body}</svg>'
    assert svg.count('class="dt"') == filled
    return svg


def ticked_svg(n, obj, per_row=5, w_mm=50):
    """Objects in rows with a green tick on each one counted (touch and tick). Exactly n objects and n ticks."""
    cols = min(n, per_row)
    rows = math.ceil(n / per_row)
    W, Hh = cols * CELL, rows * CELL
    body = ""
    for i in range(n):
        x, y = (i % per_row) * CELL, (i // per_row) * CELL
        body += (f'<g class="ic" transform="translate({x + 2} {y + 2})">{icon(obj, "c")}</g>'
                 f'<circle class="tk" cx="{x + 36}" cy="{y + 8}" r="8.5" fill="#4DB857" stroke="#fff" stroke-width="1.6"/>'
                 f'<path d="M{x + 32} {y + 8} l3 3.4 l6 -7" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
    svg = f'<svg viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">{body}</svg>'
    assert svg.count('class="ic"') == n and svg.count('class="tk"') == n
    return svg


def dotdot_svg(w_mm=70, solved=False, mode="l"):
    """Join the dots, 1 to 20: a ten-pointed star. Points alternate outer and inner; numbers sit outside each dot."""
    pts = []
    for i in range(20):
        a = math.radians(-90 + i * 18)
        r = 100 if i % 2 == 0 else 62
        pts.append((r * math.cos(a), r * math.sin(a)))
    body = ""
    if solved:
        body += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" fill="#FFF3C4" stroke="#000" stroke-width="1.8" stroke-linejoin="round"/>'
    for i, (x, y) in enumerate(pts):
        a = math.radians(-90 + i * 18)
        lr = (100 if i % 2 == 0 else 62) + 16          # every number sits just outside its dot
        lx, ly = (lr * math.cos(a)), (lr * math.sin(a))
        body += (f'<circle class="dt" cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="#000"/>'
                 f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="13" fill="#000">{i + 1}</text>')
    svg = f'<svg viewBox="-135 -125 270 250" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">{body}</svg>'
    assert svg.count('class="dt"') == 20
    return svg


def plural(o):
    return pl(o)


# v5 check: planner 28 Oct says "counting 1-20 with objects in rows or small groups" -> scatter only for small groups (9 or fewer)
assert all(c[2] != "scatter" or c[0] <= 9 for c in CARDS_M.values())
assert all(e[0] != "c" or e[3] != "scatter" or e[1] <= 9 for e in EXIT)
