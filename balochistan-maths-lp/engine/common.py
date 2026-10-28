"""Shared data + design system for the Level 1 Maths Day 1 documents (Lesson Plan, Prep Pack, Worksheet).
Single source of truth: every count, call list and answer key lives here so the three PDFs cannot disagree.
Every counted group is drawn as SVG by group_svg(), which asserts the number of drawn objects, so a picture
and its number can never differ."""
import math, os, random

WORK = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(WORK, "img")

NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
       "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
TILE = ["#2AA7C7", "#F08A3C", "#4DB857", "#E85C9B"]          # same four colours as the English pilot


def pl(obj):
    """Plural of an object name for printed text (fish stays fish)."""
    return obj if obj == "fish" else obj + "s"


def tile_colour(n):
    """Number chart: one colour per row of five (1-5, 6-10, 11-15, 16-20)."""
    return TILE[(n - 1) // 5]


# ---------------- activity data (used by LP, Call Sheet and Worksheet) ----------------
# I Do: five steps through counting. (count, object, layout, short title)
STEPS = [(5, "apple", "row", "Count to 5"), (9, "ball", "scatter", "Count to 9"), (10, "star", "frame", "Count to 10"),
         (15, "flower", "frame", "Count to 15"), (20, "cup", "frame", "Count to 20")]
SHOW_ME = [6, 10, 12, 9, 15, 20, 11, 17]                    # We Do, "Show me!" call list (8)

# You Do, worksheet page 1
WS_EXAMPLE = (5, "cup", "row")                              # printed solved example: NOT one of the questions
T1 = [(12, "ball", "row"), (8, "apple", "row"), (19, "star", "row"), (15, "flower", "row")]   # task 1 groups, top to bottom
T1_RIGHT = [19, 15, 12, 8]                                  # numbers on the right, shuffled (no straight-across answers)
T2 = [(7, "fish", "row", [6, 7, 8]), (14, "kite", "row", [15, 13, 14]), (11, "pencil", "row", [10, 12, 11]),
      (18, "cup", "row", [17, 18, 19]), (16, "apple", "row", [16, 17, 15])]     # (count, object, layout, three numbers)
T3 = [(10, "apple", 6), (16, "star", 10)]                   # (objects drawn, object, colour this many)

# Exit check, worksheet page 2: (count, object, layout, three numbers). Different numbers from tasks 1 and 2.
EXIT = [(4, "flower", "row", [3, 4, 5]), (9, "ball", "scatter", [10, 9, 8]), (13, "fish", "scatter", [12, 14, 13]),
        (6, "kite", "row", [7, 5, 6]), (17, "pencil", "row", [16, 17, 18]), (10, "star", "frame", [9, 11, 10]),
        (20, "apple", "row", [19, 20, 18]), (3, "cup", "row", [4, 3, 2])]
ORAL = ["I", "J", "K", "L"]                                 # exit check, Part B: any three cards

# Count Cards (Prep Pack): letter -> (count, object, layout, use)
CARDS = {
    "A": (5, "apple", "row", "teach"), "B": (9, "ball", "scatter", "teach"), "C": (10, "star", "frame_v", "teach"),
    "D": (15, "flower", "frame_v", "teach"), "E": (20, "cup", "frame_v", "teach"),
    "F": (8, "pencil", "row", "check"), "G": (16, "fish", "scatter", "check"), "H": (19, "kite", "row", "check"),
    "I": (11, "ball", "scatter", "oral"), "J": (12, "apple", "row", "oral"), "K": (14, "flower", "scatter", "oral"),
    "L": (18, "star", "scatter", "oral"),
}
CHECK_CARDS = ["F", "G", "H"]

# ---- consistency checks ----
assert [s[0] for s in STEPS] == [CARDS[k][0] for k in "ABCDE"]
assert WS_EXAMPLE[0] not in {g[0] for g in T1} | {g[0] for g in T2} | {t[0] for t in T3} | {t[2] for t in T3}
assert sorted(T1_RIGHT) == sorted(g[0] for g in T1) and all(g[0] != r for g, r in zip(T1, T1_RIGHT))
for n, _, _, opts in T2 + EXIT:
    assert n in opts and len(set(opts)) == 3 and all(1 <= o <= 20 for o in opts), (n, opts)
assert not {e[0] for e in EXIT} & ({g[0] for g in T1} | {g[0] for g in T2})
assert all(t[2] < t[0] for t in T3)
assert all(1 <= CARDS[k][0] <= 20 for k in CARDS)
assert not {CARDS[k][0] for k in ORAL} & {e[0] for e in EXIT}      # oral cards test counts not on the written check
assert len(EXIT) == 8

# ---------------- object drawings (40 x 40 units, outlined) ----------------
INK = "#14304F"


def _star(cx, cy, ro, ri):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = ro if i % 2 == 0 else ri
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return " ".join(pts)


def icon(obj, mode="c"):
    """One object as an SVG fragment in a 40x40 box. mode 'c' = colour, 'l' = line (white fill, for B&W printing)."""
    w = lambda c: "#FFFFFF" if mode == "l" else c
    sk = f'stroke="{INK if mode == "c" else "#000"}" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"'
    if obj == "apple":
        return (f'<path d="M20 12 C10 8 4 16 6 26 C8 35 14 38 20 35 C26 38 32 35 34 26 C36 16 30 8 20 12 Z" fill="{w("#E0352B")}" {sk}/>'
                f'<path d="M20 12 C20 8 21 5 24 3" fill="none" {sk}/>'
                f'<path d="M22 9 C26 4 31 5 32 7 C29 11 24 11 22 9Z" fill="{w("#4DB857")}" {sk}/>')
    if obj == "ball":
        return (f'<circle cx="20" cy="20" r="16" fill="{w("#F7C531")}" {sk}/>'
                f'<path d="M5 16 C14 23 26 23 35 16" fill="none" {sk}/><path d="M20 4 C13 12 13 28 20 36" fill="none" {sk}/>')
    if obj == "star":
        return f'<polygon points="{_star(20, 21, 18, 8)}" fill="{w("#F5B301")}" {sk}/>'
    if obj == "flower":
        petals = "".join(f'<circle cx="{20 + 9 * math.cos(math.radians(a)):.1f}" cy="{20 + 9 * math.sin(math.radians(a)):.1f}" r="6.5" fill="{w("#EE6FA6")}" {sk}/>'
                         for a in (-90, -18, 54, 126, 198))
        return petals + f'<circle cx="20" cy="20" r="5.2" fill="{w("#F7C531")}" {sk}/>'
    if obj == "cup":
        return (f'<path d="M6 12 L32 12 C32 27 27 33 19 33 C11 33 6 27 6 12Z" fill="{w("#3F8FD6")}" {sk}/>'
                f'<path d="M32 15 C40 15 40 25 30 25" fill="none" {sk}/><path d="M8 37 L30 37" fill="none" {sk}/>')
    if obj == "pencil":
        return (f'<g transform="rotate(-45 20 20)"><rect x="1" y="14.5" width="7" height="11" rx="1.5" fill="{w("#F29AB5")}" {sk}/>'
                f'<rect x="8" y="14.5" width="21" height="11" fill="{w("#F7C531")}" {sk}/>'
                f'<polygon points="29,14.5 39,20 29,25.5" fill="{w("#F3D2AE")}" {sk}/></g>')
    if obj == "kite":
        return (f'<polygon points="20,2 33,16 20,31 7,16" fill="{w("#E0352B")}" {sk}/>'
                f'<path d="M20 2 L20 31 M7 16 L33 16" fill="none" {sk}/><path d="M20 31 C14 33 26 36 20 39" fill="none" {sk}/>')
    if obj == "fish":
        return (f'<ellipse cx="17" cy="20" rx="13" ry="9.5" fill="{w("#F08A3C")}" {sk}/>'
                f'<polygon points="29,20 39,12 39,28" fill="{w("#F08A3C")}" {sk}/><circle cx="11" cy="18" r="1.8" fill="{INK if mode == "c" else "#000"}"/>')
    raise ValueError(obj)


CELL = 44           # centre-to-centre spacing in units (icon is 40)


def group_svg(n, obj, layout="row", w_mm=60, mode="c", seed=1, per_row=None, cell_mm=None, max_h_mm=None, aspect=1.5):
    """Draw exactly n objects. layout: 'row' (rows of per_row), 'frame' (Ten Boxes, top row first), 'scatter'.
    Returns an inline <svg> that is w_mm wide (or sized so one object cell is cell_mm); height follows the drawing."""
    ics = []
    extra = ""
    if layout == "row":
        pr = per_row or (n if n <= 10 else (n + 1) // 2)
        cols = min(n, pr)
        rows = math.ceil(n / pr)
        W, Hh = cols * CELL, rows * CELL
        for i in range(n):
            ics.append(((i % pr) * CELL + CELL / 2, (i // pr) * CELL + CELL / 2))
    elif layout in ("frame", "frame_v"):
        nframes = math.ceil(n / 10)
        gap = 8
        vert = layout == "frame_v"
        W = 5 * CELL if vert else nframes * 5 * CELL + (nframes - 1) * gap
        Hh = nframes * 2 * CELL + (nframes - 1) * gap if vert else 2 * CELL
        for f in range(nframes):
            x0 = 0 if vert else f * (5 * CELL + gap)
            y0 = f * (2 * CELL + gap) if vert else 0
            extra += (f'<rect x="{x0 + 1}" y="{y0 + 1}" width="{5 * CELL - 2}" height="{2 * CELL - 2}" rx="4" fill="#FFFFFF" fill-opacity=".0" '
                      f'stroke="{INK if mode == "c" else "#000"}" stroke-width="2.4"/>')
            for c in range(1, 5):
                extra += f'<line x1="{x0 + c * CELL}" y1="{y0 + 1}" x2="{x0 + c * CELL}" y2="{y0 + 2 * CELL - 1}" stroke="#9AA6B5" stroke-width="1.4"/>'
            extra += f'<line x1="{x0 + 1}" y1="{y0 + CELL}" x2="{x0 + 5 * CELL - 1}" y2="{y0 + CELL}" stroke="#9AA6B5" stroke-width="1.4"/>'
        for i in range(n):
            f, k = divmod(i, 10)
            ics.append((((k % 5) * CELL + CELL / 2) if vert else (f * (5 * CELL + gap) + (k % 5) * CELL + CELL / 2),
                        ((f * (2 * CELL + gap)) if vert else 0) + (k // 5) * CELL + CELL / 2))
    elif layout == "scatter":
        cols = max(3, math.ceil(math.sqrt(n * aspect)))
        rows = max(2, math.ceil(n * 1.15 / cols))
        S = CELL + 10
        W, Hh = cols * S, rows * S
        rng = random.Random(seed * 1000 + n)
        cells = rng.sample(range(cols * rows), n)
        for c in sorted(cells):
            ics.append(((c % cols) * S + S / 2 + rng.uniform(-6, 6), (c // cols) * S + S / 2 + rng.uniform(-6, 6)))
    else:
        raise ValueError(layout)
    if cell_mm or max_h_mm:
        sc = min(cell_mm / CELL if cell_mm else 1e9, max_h_mm / Hh if max_h_mm else 1e9)
        w_mm = round(W * sc, 2)
    body = "".join(f'<g class="ic" transform="translate({x - 20:.1f} {y - 20:.1f})">{icon(obj, mode)}</g>' for x, y in ics)
    svg = (f'<svg viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">{extra}{body}</svg>')
    assert svg.count('class="ic"') == n, (n, obj, layout)
    return svg


def tin_svg(w_mm=26):
    """Small tin cup with three stones, for the Hook."""
    return (f'<svg viewBox="0 0 80 70" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">'
            f'<path d="M14 24 L66 24 L60 62 C60 65 58 66 55 66 L25 66 C22 66 20 65 20 62 Z" fill="#B8C2CF" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<ellipse cx="40" cy="24" rx="26" ry="6" fill="#DDE3EB" stroke="{INK}" stroke-width="2.4"/>'
            f'<circle cx="28" cy="12" r="6" fill="#9AA6B5" stroke="{INK}" stroke-width="2.2"/><circle cx="42" cy="8" r="6" fill="#B5BEC9" stroke="{INK}" stroke-width="2.2"/>'
            f'<circle cx="54" cy="14" r="6" fill="#8D99A8" stroke="{INK}" stroke-width="2.2"/></svg>')


def scene(name, cls="scene"):
    f = os.path.join(IMG, f"scene_{name}.jpg")
    if os.path.exists(f):
        return f'<img class="{cls}" src="img/scene_{name}.jpg" alt="">'
    return ""


CSS = r"""
@font-face{font-family:"Nunito";src:url("fonts/Nunito.ttf");font-weight:200 1000}
@font-face{font-family:"Inter";src:url("fonts/Inter.ttf");font-weight:100 900}
:root{--navy:#001F3F;--gold:#F5B301;--paper:#FAF7F2;--ink:#1D2025;--mint:#E3F4EC;--teal:#0B8F6A;--sky:#E8EEF8;
--cream:#FFF6DC;--line:#D7DCE3;--grey:#5B6572;--c1:#2AA7C7;--c2:#F08A3C;--c3:#4DB857;--c4:#E85C9B}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;font-family:Inter,"Segoe UI",Arial,sans-serif;color:var(--ink);
-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:10pt;line-height:1.38}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.bar{height:25mm;background:var(--navy);color:#fff;display:flex;align-items:center;padding:0 10mm;gap:5mm}
.bar .day{background:var(--gold);color:var(--navy);font-weight:900;border-radius:50%;width:15mm;height:15mm;display:flex;
flex-direction:column;align-items:center;justify-content:center;line-height:1;font-size:6.5pt;letter-spacing:.04em}
.bar .day b{font-size:17pt;display:block;letter-spacing:0}
.bar h1{margin:0;font-size:17pt;font-weight:800;line-height:1.1;flex:1}
.bar h1 small{display:block;font-size:8.5pt;font-weight:500;color:#C9D6E6;margin-top:1mm;letter-spacing:.02em}
.pill{background:#0B8F6A;color:#fff;border-radius:99px;padding:2.2mm 4.5mm;font-weight:800;font-size:11pt;white-space:nowrap}
.content{position:absolute;left:10mm;right:10mm;top:30mm;bottom:15mm;overflow:hidden}
.foot{position:absolute;left:10mm;right:10mm;bottom:5mm;height:7mm;display:flex;align-items:center;justify-content:space-between;
font-size:7.5pt;color:var(--grey);border-top:.3mm solid var(--line);padding-top:1.5mm}
.box{border-radius:3.5mm;padding:3.4mm 4.2mm;margin-bottom:3mm;border:.4mm solid transparent}
.box h2{margin:0 0 1.6mm;font-size:11.5pt;font-weight:800;color:var(--navy);display:flex;align-items:center;gap:2.5mm}
.box h2 .t{font-size:8.5pt;background:var(--navy);color:#fff;border-radius:99px;padding:.6mm 2.6mm;font-weight:700;white-space:nowrap}
.box p{margin:0 0 1.4mm}
.box ul,.box ol{margin:0;padding-left:5mm}
.box li{margin-bottom:1mm}
.mint{background:var(--mint);border-color:#B9E2CF}
.sky{background:var(--sky);border-color:#C7D4EC}
.cream{background:var(--cream);border-color:#F2D98B}
.gold{background:var(--gold);color:var(--navy)}
.teal{background:var(--teal);color:#fff}.teal h2{color:#fff}
.navy{background:var(--navy);color:#fff}.navy h2{color:var(--gold)}
.grey{background:#F1F3F6;border-color:#DDE2E8}
.say{background:#fff;border:.4mm dashed #8CA3C4;border-radius:3mm;padding:2.2mm 3.4mm;margin:1.4mm 0;font-style:italic;color:#14304F}
.say:before{content:"Say: ";font-style:normal;font-weight:800;color:var(--teal)}
.do{font-weight:700}
.cfu{background:var(--teal);color:#fff;border-radius:3mm;padding:2.4mm 4mm;margin-bottom:3mm}
.cfu b{color:var(--gold)}
.row{display:flex;gap:3mm}.row>*{flex:1;min-width:0}
.chip{display:inline-block;background:var(--navy);color:#fff;border-radius:2mm;padding:.5mm 2.2mm;font-weight:800;font-size:9pt}
.small{font-size:8.5pt;color:var(--grey)}
.num{width:8mm;height:8mm;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:900;font-size:13pt;
display:inline-flex;align-items:center;justify-content:center;flex:none}
.k{font-family:Nunito,Inter,sans-serif;font-weight:900}
.lt{font-family:Nunito,sans-serif;font-weight:900;color:#fff;border-radius:2.2mm;text-align:center;line-height:1;
display:flex;align-items:center;justify-content:center}
.scene{width:100%;height:auto;display:block}
.board{background:#27403A;border:2mm solid #B07A3A;border-radius:2.5mm;color:#F4F7F2;padding:3mm 4mm;margin-bottom:3mm}
.board h3{margin:0 0 1.6mm;color:#FFD966;font-size:10pt;font-weight:800;letter-spacing:.02em}
.board .chalk{font-family:Nunito,sans-serif;font-weight:800}
"""

LEVEL = "Level 1 Beginner · Maths"
FOOT_LP = f"{LEVEL} · Day 1 of 33 · Lesson Plan"


def head_html(title):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}</style></head><body>')


OVERFLOW_JS = """<script>
window.addEventListener('load',function(){var bad=[];
document.querySelectorAll('.page').forEach(function(p,i){
 p.querySelectorAll('.content,.chk').forEach(function(c){
  if(c.scrollHeight>c.clientHeight+1){bad.push('page'+(i+1)+':'+c.className+':'+(c.scrollHeight-c.clientHeight)+'px');}
  });});
 var m=document.createElement('meta');m.name='ovf';m.content=bad.length?bad.join(' | '):'OK';document.head.appendChild(m);});
</script></body></html>"""


def foot(label, n, total):
    return f'<div class="foot"><span>{label}</span><span>Page {n} of {total}</span></div>'
