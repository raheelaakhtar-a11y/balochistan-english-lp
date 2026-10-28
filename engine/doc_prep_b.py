"""Level 1 Beginner, English, Day 1 (final planner): Prep Pack (no Rumi logo)."""
from common_b import *

TOTAL = 6
EXTRA_CSS = FONT_CSS + """
.card{border:.35mm dashed #8D99A8;padding:3.5mm;display:flex}
.card .in{flex:1;border:1.4mm solid var(--c);border-radius:5mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:3mm 3mm 5mm;background:#fff}
.card .cl{font-family:Andika,sans-serif;font-weight:700;font-size:70pt;line-height:1;color:var(--c)}
.card .cp{width:62mm}
.card .cw{font-family:Andika,sans-serif;font-weight:700;font-size:28pt;color:var(--navy);line-height:1}
.cardgrid{position:absolute;left:10mm;right:10mm;top:21mm;bottom:14mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:minmax(0,1fr) minmax(0,1fr)}
.slim{height:15mm}.slim h1{font-size:13pt}
table.t{border-collapse:collapse;width:100%}
table.t td,table.t th{border:.3mm solid #B9C2CE;padding:0 1.6mm;text-align:center}
table.t th{background:var(--navy);color:#fff;font-size:8pt;font-weight:700;height:10mm}
"""


def bar(title, sub):
    return f'<div class="bar"><div class="day">DAY<b>1</b></div><h1>{title}<small>{sub}</small></h1></div>'


def F(n):
    return foot(FOOT_PREP, n, TOTAL, mark=None)


def p1():
    inside = [("Letter Chart", "page 2", "Stick on the wall at children's eye level"),
              ("Teacher Call Sheet", "page 3", "How to say each sound, every call list, all answer keys"),
              ("4 Picture-Letter Cards", "page 4", "Print on thick paper, one side. Cut on the dashed lines"),
              ("Desk Letter Strips", "page 5", "Print one strip for each child. Cut on the dashed lines"),
              ("Class Tally Sheet", f"page {TOTAL}", "Record each child's status: On track, Practise or Re-teach")]
    rows = "".join(f'<tr><td style="text-align:left;font-weight:800;padding:2mm 3mm">{a}</td><td style="width:26mm"><b>{b}</b></td><td style="text-align:left;padding:2mm 3mm">{c}</td></tr>' for a, b, c in inside)
    return f"""<section class="page">{bar("Preparation Pack", "Everything to print, cut and gather before class")}
<div class="content">
 <div class="box gold" style="display:flex;gap:4mm;align-items:center"><div style="flex:1"><div style="font-size:8.5pt;font-weight:800;letter-spacing:.05em">LEVEL 1 BEGINNER · ENGLISH · DAY 1</div>
  <div style="font-size:17pt;font-weight:900;line-height:1.15">Meet A, B, C and D</div><div style="font-size:10pt">Get ready in about 20 minutes. Keep this pack with your Lesson Plan.</div></div>
  <div style="width:30mm;border-radius:4mm;overflow:hidden;background:#fff">{scene("teacher_point")}</div></div>

 <div style="font-size:9.5pt;font-weight:800;color:var(--navy);margin:1mm 0 1.4mm">WHAT IS IN THIS PACK</div>
 <table class="t" style="margin-bottom:3.4mm;font-size:9.4pt">{rows}</table>

 <div class="row">
  <div class="box mint"><h2>Print and cut</h2>
   <div style="font-size:9.6pt;line-height:1.5">☐ Letter Chart (page 2): 1 copy<br>☐ Picture-Letter Cards (page 4): 1 set<br>☐ <b>Desk Letter Strip: 1 for each child</b><br>☐ Teacher Call Sheet (page 3): 1 copy<br>☐ <b>Student Worksheet: 1 for each child</b>, both sides<br>☐ Class Tally Sheet (page {TOTAL}): 1 copy</div></div>
  <div class="box sky"><h2>Gather</h2>
   <div style="font-size:9.6pt;line-height:1.5">☐ Chalk and a duster<br>☐ A slate or notebook page for each child<br>☐ A pencil for each child<br>☐ Pieces of paper to cover letters (4)<br>☐ Tape or sticky tack for the chart</div></div>
 </div>

 <div class="box cream"><h2>Five minutes before the children arrive</h2>
  <ol style="font-size:9.6pt;line-height:1.45">
   <li>Fix the <b>Letter Chart</b> on the wall at eye level.</li>
   <li>Write <b>A, B, C, D</b> big on the board (capitals). Cover each letter with a piece of paper, for the Hook.</li>
   <li>Put the 4 Picture-Letter Cards in order, A, B, C, D, with A on top.</li>
   <li>Stack the Desk Letter Strips and the worksheets where you can reach them.</li>
   <li>Read the Call Sheet once. Practise the four sounds: /a/, /b/, /k/, /d/. Say them short, with no extra "uh".</li></ol></div>

 <div class="box grey" style="margin-bottom:0"><b>Printing tip:</b> If you cannot print the cards or strips, draw each letter pair and its picture by hand on paper. Children need to see the letters clearly. A simple drawing is enough.</div>
</div>{F(1)}</section>"""


def p2():
    rows = ""
    for l in LETTERS:
        rows += (f'<div style="border:.5mm solid {TILE[l]};border-radius:5mm;padding:3mm 6mm;display:flex;align-items:center;gap:8mm;background:#fff">'
                 f'<div class="lt" style="width:64mm;height:44mm;font-size:84pt;font-weight:700;background:{TILE[l]};color:#fff;border-radius:5mm;display:flex;align-items:center;justify-content:center;line-height:1">{l}{l.lower()}</div>'
                 f'<div style="width:44mm;flex:none">{bpic(l)}</div>'
                 f'<div><div class="wd" style="font-size:36pt;font-weight:700;line-height:1">{WORD[l]}</div>'
                 f'<div style="font-size:11pt;color:var(--grey);margin-top:2mm">name: {l} · sound: /{SOUND[l]}/</div></div></div>')
    return f"""<section class="page">{bar("Letter Chart", "Today's four letters, their pictures and sounds")}
<div style="position:absolute;left:10mm;right:10mm;top:31mm;bottom:20mm;display:grid;grid-template-rows:repeat(4,minmax(0,1fr));gap:3mm">{rows}</div>
<div class="small" style="position:absolute;left:10mm;right:10mm;bottom:15mm;text-align:center">Stick on the wall at eye level. Point to a letter with a pointer, not with a finger over the letter.</div>
{F(2)}</section>"""


def p3():
    tr = "".join(f'<tr><td style="width:24mm"><span class="lt" style="display:inline-flex;width:17mm;height:9mm;font-size:15pt;font-weight:700;background:{TILE[l]};color:#fff;border-radius:2mm;align-items:center;justify-content:center">{l}{l.lower()}</span></td>'
                 f'<td style="text-align:left;font-weight:800">{l} (say "{NAME_SAY[l]}")</td><td style="text-align:left;font-weight:800">/{SOUND[l]}/</td><td style="text-align:left">{WORD[l]}</td><td style="text-align:left;font-size:8.4pt">{SOUND_HINT[l]}</td></tr>' for l in LETTERS)
    t3 = "".join(f'<tr><td style="text-align:left">{p}</td><td style="width:14mm"><b>{T3_KEY[p]}</b></td></tr>' for p in T3_PICS)
    ex = ""
    for i, it in enumerate(EXIT):
        opts = " &nbsp; ".join(it["options"]) if it["options"] else "(child writes)"
        ex += f'<tr><td style="width:6mm"><b>{i+1}</b></td><td style="text-align:left;width:22mm">{it["kind"]}</td><td style="text-align:left">{it["say"]}</td><td style="width:26mm">{opts}</td><td style="width:14mm"><b>{it["answer"]}</b></td></tr>'
    return f"""<section class="page">{bar("Teacher Call Sheet", "Keep this next to you during the lesson")}
<div class="content" style="top:29mm">
 <table class="t" style="font-size:9.4pt;margin-bottom:3mm"><tr><th>Letter</th><th style="text-align:left">Name</th><th style="text-align:left">Sound</th><th style="text-align:left">Picture word</th><th style="text-align:left">How to say the sound</th></tr>{tr}</table>
 <div class="row" style="gap:3mm">
  <div class="box sky" style="margin-bottom:2.4mm"><h2 style="font-size:10pt">We Do: Show me, names (in order)</h2>{" · ".join(f"<b>{t}</b>" for t, _ in SHOW_NAMES)}
   <h2 style="font-size:10pt;margin-top:2mm">Show me, sounds (in order)</h2>{" · ".join(f"<b>/{s}/</b>" for s, _ in SHOW_SOUNDS)}</div>
  <div class="box cream" style="margin-bottom:2.4mm"><h2 style="font-size:10pt">We Do: Write it (say in this order)</h2>{" · ".join(f"<b>{t}</b>" for t, _ in WRITE_CALLS)}
   <div class="small" style="margin-top:1mm">Chant order for names and sounds: A B C D, then C A D B.</div></div>
 </div>
 <div class="row" style="gap:3mm">
  <div class="box mint" style="margin-bottom:2.4mm"><h2 style="font-size:10pt">You Do answers (worksheet page 1)</h2>
   <div style="font-size:9pt;line-height:1.5"><b>1 Trace and copy:</b> A a · B b · C c · D d<br><b>2 Match big and small:</b> {" · ".join(f"{c} to {T2_KEY[c]}" for c in T2_CAPS)}<br><b>3 Picture to first letter:</b></div>
   <table class="t" style="font-size:9pt;margin-top:1mm">{t3}</table></div>
  <div class="box mint" style="margin-bottom:2.4mm"><h2 style="font-size:10pt">Part B: say it aloud</h2>
   <div style="font-size:9pt;line-height:1.5">Hear <b>4 or 5 children</b>, a different group each day. Point to one of <b>{" · ".join(PART_B)}</b> on the chart.<br>1. Ask the <b>name</b>. 2. Then ask the <b>sound</b>. Never in one question.</div>
   <h2 style="font-size:10pt;margin-top:2mm">Tracker (Part A score)</h2><div style="font-size:9pt;line-height:1.45"><b>On track:</b> 4 or 5 · <b>Practise:</b> 3 · <b>Re-teach:</b> 2 or fewer</div></div>
 </div>
 <div class="box mint" style="margin-bottom:0"><h2 style="font-size:10pt">Exit check, Part A: say each item two times</h2>
  <table class="t" style="font-size:9pt"><tr><th></th><th style="text-align:left">Kind</th><th style="text-align:left">Say</th><th>Options</th><th>Answer</th></tr>{ex}</table></div>
</div>{F(3)}</section>"""


def card(l):
    return (f'<div class="card" style="--c:{TILE[l]}"><div class="in"><div class="cl">{l}{l.lower()}</div>'
            f'<div class="cp">{bpic(l)}</div><div><div class="cw" style="text-align:center">{WORD[l]}</div>'
            f'<div style="text-align:center;font-size:9.5pt;color:var(--grey);margin-top:1mm">name {l} · sound /{SOUND[l]}/</div></div></div></div>')


def p4():
    return (f'<section class="page"><div class="bar slim"><div class="day" style="width:10mm;height:10mm;font-size:5pt"><b style="font-size:11pt">1</b></div>'
            f'<h1>Picture-Letter Cards<small>A B C D · cut on the dashed lines</small></h1></div>'
            f'<div class="cardgrid">{"".join(card(l) for l in LETTERS)}</div>{F(4)}</section>')


def p5():
    def strip():
        cells = "".join(f'<div style="flex:1;border:.5mm solid {TILE[l]};border-radius:3mm;display:flex;align-items:center;gap:2mm;padding:1mm 2mm;background:#fff">'
                        f'<span class="lt" style="width:20mm;height:15mm;font-size:24pt;font-weight:700;background:{TILE[l]};color:#fff;border-radius:2mm;display:flex;align-items:center;justify-content:center;line-height:1">{l}{l.lower()}</span>'
                        f'<div style="width:13mm;flex:none">{bpic(l)}</div><span class="wd" style="font-size:10pt;font-weight:700">{WORD[l]}</span></div>' for l in LETTERS)
        return f'<div style="border-bottom:.35mm dashed #8D99A8;padding:2.2mm 0;display:flex;gap:2mm;align-items:center;height:100%">{cells}</div>'
    return (f'<section class="page">{bar("Desk Letter Strips", "Cut one strip for each child. They use it to check their own work")}'
            f'<div style="position:absolute;left:10mm;right:10mm;top:30mm;bottom:14mm;display:grid;grid-template-rows:repeat(8,minmax(0,1fr))">{"".join(strip() for _ in range(8))}</div>{F(5)}</section>')


def tally():
    rows = "".join(f'<tr style="height:7.3mm"><td style="width:8mm;color:var(--grey);font-size:8pt">{i}</td><td style="text-align:left"></td>' + "<td></td>" * 5 + '<td></td><td></td><td></td></tr>' for i in range(1, 31))
    return f"""<section class="page">{bar("Class Tally Sheet", "Exit check, Day 1 · Level 1 English")}
<div class="content" style="top:29mm">
 <div style="display:flex;gap:6mm;font-size:9.5pt;margin-bottom:2mm"><div>Teacher: ______________________</div><div>Class: ________________</div><div>Date: ______________</div></div>
 <div class="small" style="margin-bottom:2mm">Part A: tick each correct item (1 to 5) and write the score. Status: write O (On track, 4 or 5), P (Practise, 3) or R (Re-teach, 2 or fewer). Part B: tick when you have heard the child say a name and a sound.</div>
 <table class="t" style="font-size:8.5pt"><tr><th>No.</th><th style="width:50mm;text-align:left">Child's name</th>{"".join(f"<th>{i}</th>" for i in range(1, 6))}<th>Score<br>/ 5</th><th>Status<br>O / P / R</th><th>Part B</th></tr>{rows}</table>
</div>{F(TOTAL)}</section>"""


def build():
    html = head_html("Level 1 English Day 1 - Prep Pack").replace("</style>", EXTRA_CSS + "</style>") + p1() + p2() + p3() + p4() + p5() + tally() + OVERFLOW_JS
    out = os.path.join(WORK, "prepb.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
