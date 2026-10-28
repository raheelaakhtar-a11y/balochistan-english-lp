"""Prep Pack v4, Level 1 Maths Day 1. English prep-pack structure and design (checklist, big chart, Teacher Call Sheet,
cut-out cards, Class Tally Sheet), with maths materials: Number Chart 1 to 20, Ten Box Mats, 4 Picture Cards, pile sizes,
silly counts and answer keys, all from common_m.py."""
from common_m6 import *

FOOT = f"{LEVEL} · Day 1 of 33 · Prep Pack"
CARD_KEYS = list(CARDS_M)                               # A to D
MAT_PAGES = 2                                           # 4 mats per page, 8 mats (6 groups + 2 spare)
TOTAL = 3 + 1 + MAT_PAGES + 1
EXTRA_CSS = """
.cardf{border:.35mm dashed #8D99A8;padding:3.5mm;display:flex}
.cardf .in{flex:1;border:1.4mm solid var(--c);border-radius:5mm;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:3mm;background:#fff;position:relative}
.cardf .id{position:absolute;left:3mm;top:3mm;background:var(--c);color:#fff;font-family:Nunito,sans-serif;font-weight:900;font-size:14pt;border-radius:2mm;width:9mm;height:9mm;display:flex;align-items:center;justify-content:center}
.cardgrid{position:absolute;left:10mm;right:10mm;top:31mm;bottom:14mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr}
table.t{border-collapse:collapse;width:100%}
table.t td,table.t th{border:.3mm solid #B9C2CE;padding:0 1.6mm;text-align:center}
table.t th{background:var(--navy);color:#fff;font-size:8pt;font-weight:700;height:9mm}
.chart{position:absolute;left:10mm;right:10mm;top:31mm;bottom:22mm;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(4,1fr);gap:2.6mm}
.chart .lt{font-size:50pt;border-radius:4mm;width:auto;height:auto;flex-direction:column}
.mat{border:.35mm dashed #8D99A8;padding:3.5mm;display:flex}
.mat .in{flex:1;border:1.2mm solid var(--c);border-radius:5mm;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3mm;padding:3mm;background:#fff;position:relative}
"""


def bar(title, sub, right=""):
    return f'<div class="bar"><div class="day">DAY<b>1</b></div><h1>{title}<small>{sub}</small></h1>{right}</div>'


def F(n):
    return foot(FOOT, n, TOTAL)


def p1():
    inside = [("Number Chart 1 to 20", "page 2", "Stick on the wall, or copy onto the board"),
              ("Teacher Call Sheet", "page 3", "How to say each number, pile sizes, silly counts, the answer keys"),
              ("4 Picture Cards (A to D)", "page 4", "Print on thick paper, one side. Cut on the dashed lines"),
              ("Ten Box Mats (8)", f"pages 5 to {4 + MAT_PAGES}", "One mat per group, used to lay out and count each pile. Print on thick paper and cut. 2 are spare"),
              ("Class Tally Sheet", f"page {TOTAL}", "Record each child's exit check score")]
    rows = "".join(f'<tr><td style="text-align:left;font-weight:800;padding:2mm 3mm">{a}</td><td style="width:30mm"><b>{b}</b></td><td style="text-align:left;padding:2mm 3mm">{c}</td></tr>' for a, b, c in inside)
    return f"""<section class="page">{bar("Preparation Pack", "Everything to print, cut and gather before class")}
<div class="content">
 <div class="box gold" style="display:flex;gap:4mm;align-items:center"><div style="flex:1"><div style="font-size:8.5pt;font-weight:800;letter-spacing:.05em">LEVEL 1 BEGINNER · MATHS · DAY 1</div>
  <div style="font-size:17pt;font-weight:900;line-height:1.15">Count Objects up to 20</div><div style="font-size:10pt">Get ready in about 25 minutes. Keep this pack with your Lesson Plan.</div></div>
  <div style="width:30mm;border-radius:4mm;overflow:hidden;background:#fff">{scene("teacher_point")}</div></div>

 <div style="font-size:9.5pt;font-weight:800;color:var(--navy);margin:1mm 0 1.4mm">WHAT IS IN THIS PACK</div>
 <table class="t" style="margin-bottom:3.4mm;font-size:9.4pt">{rows}</table>

 <div class="row">
  <div class="box mint"><h2>Print and cut</h2>
   <div style="font-size:9.6pt;line-height:1.5">☐ Number Chart (page 2): 1 copy<br>☐ Picture Cards (page 4): 1 set<br>☐ Teacher Call Sheet (page 3): 1 copy<br>☐ Ten Box Mats: 6 needed, 8 on the pages<br>☐ <b>Student Worksheet: 1 per child</b>, printed on both sides<br>☐ Class Tally Sheet (page {TOTAL}): 1 copy</div></div>
  <div class="box sky"><h2>Gather</h2>
   <div style="font-size:9.6pt;line-height:1.5">☐ <b>About 100 small stones, caps or seeds</b><br>☐ <b>6 cups or small bags</b>, one per group<br>☐ Chalk in two colours, and a duster<br>☐ Pencils and crayons for the children<br>☐ Your student book, open at page 2</div></div>
 </div>

 <div class="box cream"><h2>Make the piles (10 minutes, before class)</h2>
  <ol style="font-size:9.6pt;line-height:1.45">
   <li>Count out <b>6 piles</b>: {", ".join(str(p) for p in PILES)} stones. Count each pile twice. Put each pile in its own cup.</li>
   <li>Write the group number on the outside of each cup (1 to 6). The pile sizes are on the Call Sheet. <b>Do not write the number of stones on the cup.</b></li>
   <li>Keep a spare handful of <b>{HOOK_N} stones</b> in your bag for the Hook.</li>
   <li>Put the Number Chart where every group can reach it, at children's eye level. No chart? Copy 1 to 20 on the board in four rows of five.</li>
   <li>Stack the worksheets on a desk. Check you can reach every child's desk.</li></ol></div>

 <div class="box grey" style="margin-bottom:0"><b>Printing tip:</b> If you cannot print the Ten Box Mats, draw them on the floor in chalk or on a sheet of paper: two rows of five boxes, once for each ten. Draw the Picture Cards by hand if needed, and count what you draw before class.</div>
</div>{F(1)}</section>"""


def p2():
    tiles = "".join(f'<div class="lt" style="background:{tile_colour(n)}"><span>{n}</span><span style="font-family:Inter,sans-serif;font-weight:700;font-size:13pt;margin-top:1.5mm">{NUM[n]}</span></div>' for n in range(1, 21))
    return f"""<section class="page">{bar("Number Chart", "1 to 20, in rows of five")}
<div class="chart">{tiles}</div>
<div class="small" style="position:absolute;left:10mm;right:10mm;bottom:16mm;text-align:center">Stick on the wall at eye level. Point to a number with a pointer, never with a finger over the number.</div>
{F(2)}</section>"""


def p3():
    def tbl(rng):
        r = "".join(f'<tr><td style="width:15mm"><span class="lt k" style="display:inline-flex;width:11mm;height:8mm;font-size:13pt;background:{tile_colour(n)}">{n}</span></td>'
                    f'<td style="text-align:left;font-weight:800;font-size:10.5pt">{NUM[n]}</td></tr>' for n in rng)
        return f'<table class="t" style="font-size:9pt"><tr><th>Number</th><th style="text-align:left">Say it as</th></tr>{r}</table>'

    piles = "".join(f'<tr><td style="width:18mm"><b>Group {i+1}</b></td><td style="width:9mm"><b>{p}</b></td><td style="text-align:left">{NUM[p]} stones</td></tr>' for i, p in enumerate(PILES))
    silly = "".join(f'<tr><td style="width:9mm"><b>{n}</b></td><td style="text-align:left;font-size:7.8pt;line-height:1.2">{what}</td></tr>' for n, what, _ in SILLY)
    cards = "".join(f'<tr><td style="width:14mm"><b>Card {k}</b></td><td style="width:9mm"><b>{c[0]}</b></td><td style="text-align:left">{NUM[c[0]]} {pl(c[1])}</td><td style="text-align:left;color:var(--grey)">{CARD_USE[k]}</td></tr>' for k, c in CARDS_M.items())
    t1 = "".join(f'<tr><td style="width:6mm"><b>{i+1}</b></td><td style="text-align:left">{r[0]} {pl(r[1])}</td><td style="width:20mm"><b>circle {r[0]}</b></td></tr>' for i, r in enumerate(T1))
    ex = ""
    for i, e in enumerate(EXIT):
        if e[0] == "c":
            ex += f'<tr><td style="width:6mm"><b>{i+1}</b></td><td style="text-align:left">{e[1]} {pl(e[2])}</td><td style="width:20mm"><b>circle {e[1]}</b></td></tr>'
        else:
            ex += f'<tr><td style="width:6mm"><b>{i+1}</b></td><td style="text-align:left">numeral {e[1]}</td><td style="width:20mm"><b>draw {e[1]} dots</b></td></tr>'
    return f"""<section class="page">{bar("Teacher Call Sheet", "Keep this next to you during the lesson")}
<div class="content" style="top:29mm">
 <div style="font-size:9.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">HOW TO SAY EACH NUMBER <span class="small" style="font-weight:500">(say the end of the "teen" numbers clearly: thirteen, not thirty)</span></div>
 <div class="row" style="gap:4mm;margin-bottom:2.6mm">{tbl(range(1, 11))}{tbl(range(11, 21))}</div>
 <div class="row" style="gap:3mm">
  <div class="box sky" style="margin-bottom:2.2mm"><h2 style="font-size:10pt">We Do 2: pile sizes</h2><table class="t" style="font-size:8.6pt">{piles}</table><div class="small" style="margin-top:1mm">Hook: {HOOK_N} stones. Exit check, Part B: say "Count out {ORAL_GIVE[0]}" (or {ORAL_GIVE[1]} or {ORAL_GIVE[2]}).</div></div>
  <div class="box cream" style="margin-bottom:2.2mm"><h2 style="font-size:10pt">We Do 1: silly counts (stones)</h2><table class="t" style="font-size:8.6pt">{silly}</table><div class="small" style="margin-top:1mm">Say the mistake, then the class shouts Stop.</div></div>
 </div>
 <div class="box mint" style="margin-bottom:2.2mm"><h2 style="font-size:10pt">Picture Cards</h2><table class="t" style="font-size:8.4pt;line-height:1.2">{cards}</table></div>
 <div class="row" style="gap:3mm">
  <div class="box mint" style="margin-bottom:0"><h2 style="font-size:10pt">You Do answers</h2>
   <div style="font-size:8.4pt;line-height:1.35"><b>Task 1</b> circle:</div><table class="t" style="font-size:8.4pt">{t1}</table>
   <div class="small" style="margin-top:1mm"><b>Task 2:</b> draw {", ".join(str(n) for n in T2)} dots, top row first. <b>Task 3:</b> join 1 to 20: a star.</div></div>
  <div class="box mint" style="margin-bottom:0"><h2 style="font-size:10pt">Exit check, Part A: answers</h2><table class="t" style="font-size:8.4pt">{ex}</table>
   <div class="small" style="margin-top:1mm"><b>7 or 8</b>: ready · <b>5 or 6</b>: nearly there · <b>4 or fewer</b>: needs help</div></div>
 </div>
</div>{F(3)}</section>"""


def card(k):
    n, obj, layout = CARDS_M[k]
    colour = TILE[CARD_KEYS.index(k) % 4]
    pr = (n + 1) // 2 if layout == "row" and n > 5 else None
    return (f'<div class="cardf" style="--c:{colour}"><div class="in"><div class="id">{k}</div>'
            f'<div style="width:100%;display:flex;justify-content:center">{group_svg(n, obj, layout, w_mm=80, seed=CARD_KEYS.index(k) + 4, per_row=pr)}</div></div></div>')


def card_page():
    return (f'<section class="page">{bar("Picture Cards", "Cards A to D · cut on the dashed lines")}'
            f'<div class="cardgrid">{"".join(card(k) for k in CARD_KEYS)}</div>{F(4)}</section>')


def mat():
    return (f'<div class="mat" style="--c:#2AA7C7"><div class="in"><div style="position:absolute;left:4mm;top:3mm;font-weight:900;font-size:11pt;color:var(--navy)">Ten Box Mat</div>'
            f'<div style="margin-top:6mm;width:82mm">{boxes_svg(2, 0, 82, stack=True)}</div>'
            f'<div class="small" style="text-align:center">Fill the top row first. A full box holds 10.</div></div></div>')


def mat_pages():
    out = ""
    for i in range(MAT_PAGES):
        out += (f'<section class="page">{bar(f"Ten Box Mats {i+1} of {MAT_PAGES}", "One mat for each group · cut on the dashed lines")}'
                f'<div class="cardgrid">{"".join(mat() for _ in range(4))}</div>{F(5 + i)}</section>')
    return out


def tally():
    rows = "".join(f'<tr style="height:7.3mm"><td style="width:8mm;color:var(--grey);font-size:8pt">{i}</td><td style="text-align:left"></td>' + "<td></td>" * 8 + '<td></td><td></td><td></td></tr>' for i in range(1, 31))
    return f"""<section class="page">{bar("Class Tally Sheet", "Exit check, Day 1 · Level 1 Maths")}
<div class="content" style="top:29mm">
 <div style="display:flex;gap:6mm;font-size:9.5pt;margin-bottom:2mm"><div>Teacher: ______________________</div><div>Class / group: ________________</div><div>Date: ______________</div></div>
 <div class="small" style="margin-bottom:2mm">Part A: tick each correct answer (1 to 8) and write the score. Part B: tick if the child counted out the stones correctly. Tick the last column for children who need extra help on Day 2 (score 4 or fewer).</div>
 <table class="t" style="font-size:8.5pt"><tr><th>No.</th><th style="width:48mm;text-align:left">Child's name</th>{"".join(f"<th>{i}</th>" for i in range(1, 9))}<th>Score<br>/ 8</th><th>Part B</th><th>Extra help<br>Day 2</th></tr>{rows}</table>
</div>{F(TOTAL)}</section>"""


def build():
    html = head_html("Level 1 Maths Day 1 - Prep Pack v6").replace("</style>", EXTRA_CSS + "</style>") + p1() + p2() + p3() + card_page() + mat_pages() + tally() + OVERFLOW_JS
    out = os.path.join(WORK, "prep6.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
