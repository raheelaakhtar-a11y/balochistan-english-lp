"""Lesson Plan v8 (no repeated minute breakdown)
based on v7 (goal moved up under the learning outcome; no "by the end" or "counting only" boxes) (pictures match the text; illustrated characters) (28 Oct planner: M-B-01 on Days 1 and 2), Level 1 Maths Day 1 (M-B-01 Count objects up to 20 and say how many).
English plan structure and design (5 pages, 60 min = 5+5+20+12+8+10, no Rumi logo, no Key Words / Coming Up / Coaching Corner),
with a maths lesson inside: fingers and counting, guess then count, real objects then pictures then the Ten Box,
Silly Counter, count and swap piles, check the book, dot-to-dot, count out N."""
from common_m6 import *

TOTAL = 5
F = lambda n: foot(FOOT_LP, n, TOTAL)
SLO = "Count objects up to 20 and say how many"

EXTRA_CSS = """
.stp{display:flex;flex-direction:column;gap:2mm}
.stp .s{display:flex;gap:3mm;align-items:flex-start;font-size:10.4pt;line-height:1.3}
.stp .s>div{flex:1}
.n2{width:6.6mm;height:6.6mm;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:900;font-size:10.5pt;display:inline-flex;align-items:center;justify-content:center;flex:none;margin-top:.2mm}
table.ans{border-collapse:collapse;width:100%;font-size:9.6pt}
table.ans th{background:var(--navy);color:#fff;font-size:8.5pt;padding:1.6mm 2.4mm;text-align:left}
table.ans td{border-bottom:.3mm solid #C9D3E0;padding:1.8mm 2.4mm;vertical-align:middle}
.bub{position:relative;background:#fff;border:.5mm solid var(--navy);border-radius:4mm;padding:2mm 3mm;font-weight:600;font-size:9.2pt;line-height:1.3;color:var(--navy)}
.bub:after{content:"";position:absolute;bottom:-2.8mm;left:8mm;width:4mm;height:4mm;background:#fff;border-right:.5mm solid var(--navy);border-bottom:.5mm solid var(--navy);transform:rotate(45deg)}
"""


def bar(title, sub, mins):
    return (f'<div class="bar"><div class="day">DAY<b>1</b></div><h1>{title}<small>{sub}</small></h1>'
            f'<div class="pill">{mins}</div></div>')


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{i+1}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


# ---------------- PAGE 1: roadmap ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d == 1:
            st = "background:#F5B301;color:#001F3F;font-weight:900;outline:.5mm solid #001F3F"
        elif d <= 2:
            st = "background:#FBE08A;color:#001F3F"
        elif d >= 31:
            st = "background:#BDE5D2;color:#064B38"
        else:
            st = "background:#E6E9EE;color:#7A8594"
        ribbon += f'<span style="flex:1;height:7mm;border-radius:1.2mm;display:flex;align-items:center;justify-content:center;font-size:6.2pt;{st}">{d}</span>'
    bits = [("Warm-up", 5, "#6C7A8D"), ("Hook", 5, "#0B8F6A"), ("I Do: teach", 20, "#F5B301"), ("We Do: practise together", 12, "#F08A3C"),
            ("You Do", 8, "#2AA7C7"), ("Exit check", 10, "#001F3F")]
    assert sum(b[1] for b in bits) == 60
    tbar = "".join(f'<div style="flex:{m};background:{c};color:{"#001F3F" if c in ("#F5B301","#F08A3C","#2AA7C7") else "#fff"};'
                   f'padding:1.6mm 1.2mm;font-size:7.4pt;font-weight:800;text-align:center;line-height:1.15">{n}<br><span style="font-weight:600">{m} min</span></div>'
                   for n, m, c in bits)
    return f"""<section class="page">
<div style="background:var(--navy);height:46mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:900;line-height:.92"><div style="font-size:56pt;letter-spacing:-.02em">DAY 1</div><div style="font-size:22pt;color:#fff">OF 33</div></div>
 <div style="flex:1;padding-left:4mm;border-left:.5mm solid #2B4A6B">
  <div style="font-size:15pt;font-weight:800;line-height:1.15">Level 1 Beginner · Maths</div>
  <div style="font-size:9.5pt;color:#C9D6E6;margin-top:1.5mm">Balochistan Winter Programme · Teaching at the Right Level</div>
  <div style="margin-top:2.6mm;display:flex;gap:2mm"><span class="pill" style="font-size:9pt;padding:1.4mm 3.6mm">60 minutes</span><span class="pill" style="font-size:9pt;padding:1.4mm 3.6mm;background:var(--gold);color:var(--navy)">Teach and model</span></div>
 </div>
 <div style="width:30mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("kids_wave")}</div>
</div>
<style>.p1b .box{{margin-bottom:var(--g);padding-top:var(--pd);padding-bottom:var(--pd)}}</style>
<div class="content p1b" style="top:51mm;zoom:1.07;--g:3.6mm;--pd:3.5mm">
 <div style="display:flex;gap:.8mm;margin-bottom:.8mm">{ribbon}</div>
 <div class="small" style="margin-bottom:2mm">The 33 days. Days 1 and 2 (gold) teach counting objects. Days 31 to 33 (green) are final consolidation.</div>

 <div class="box gold" style="display:flex;gap:4mm;align-items:center">
  <div class="lt k" style="width:20mm;height:17mm;font-size:23pt;background:var(--navy);color:var(--gold)">1-20</div>
  <div><div style="font-size:8.5pt;font-weight:800;letter-spacing:.05em">TODAY</div>
  <div style="font-size:20pt;font-weight:900;line-height:1.1">Count Objects up to 20</div>
  <div style="font-size:10pt;font-weight:600">Touch each one, say a number, and say how many</div></div>
 </div>

 <div class="box sky"><h2>The learning outcome</h2>
  <p><span class="chip">M-B-01</span> <b>{SLO}</b></p>
  <p class="small" style="margin:0">Core SLO. Taught on Days 1 and 2: today is Teach and model, Day 2 is Practise and check. Builds on the entry skill (placement level).</p>
 </div>

 <div class="box teal"><h2>Today's Goal</h2><div style="font-size:13pt;font-weight:800;line-height:1.2">Count up to 20 objects and say how many there are.</div></div>

 <div style="margin-bottom:2.4mm"><div style="font-size:9.5pt;font-weight:800;color:var(--navy);margin-bottom:1mm">THE 60 MINUTES</div>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden">{tbar}</div>
  <div class="small" style="margin-top:1mm">The last 10 minutes are the exit check, as on every day of the programme.</div></div>

 <div class="row">
  <div class="box grey"><h2>Student book</h2>
   <p style="margin:0"><b>Unit 1, Whole Numbers</b><br><b>Pages 2 to 3:</b> fingers and objects, 1 to 9<br><b>Page 5:</b> Counting<br><b>Page 14:</b> Number ten · <b>Page 18:</b> Numbers 11 to 20<br><span class="small">The book shows objects only up to 9. For 10 to 20, use the Ten Box and Picture Cards.</span></p></div>
  <div class="box grey"><h2>Your three documents</h2>
   <ol style="padding-left:4.5mm"><li><b>Lesson Plan</b> (this one)</li><li><b>Prep Pack</b>: cut and print before class</li><li><b>Student Worksheet</b>: 1 per child, both sides</li></ol></div>
 </div>

 <div class="box mint" style="margin-bottom:0"><h2>To prepare (about 25 minutes)</h2>
  <div style="columns:2;column-gap:6mm;font-size:9pt;line-height:1.4">
   <div>☐ Number Chart 1 to 20 on the wall</div>
   <div>☐ Cut out the 4 Picture Cards (A to D)</div>
   <div>☐ Cut out the Ten Box Mats: 1 per group</div>
   <div>☐ Make <b>6 piles</b> of small stones, caps or seeds (sizes on the Call Sheet) and put each in a cup</div>
   <div>☐ A spare handful: 14 stones for the Hook</div>
   <div>☐ Teacher Call Sheet next to you</div>
   <div>☐ Worksheet: 1 per child, both sides</div>
   <div>☐ Chalk, duster, pencils, crayons. Class Tally Sheet ready</div>
  </div></div>
</div>
{F(1)}</section>"""


# ---------------- PAGE 2: warm-up, hook, goal, board ----------------
def page2():
    chalk_rows = "<br>".join(" ".join(str(i) for i in range(s, s + 5)) for s in (1, 6, 11, 16))
    return f"""<section class="page">
{bar("Start the Lesson", "Warm-up and Hook", "10 min")}
<div class="content" style="zoom:1.1">
 <div class="box grey"><h2>Warm-up: Fingers and Counting <span class="t">5 min</span></h2>
  <ol>
   <li><span class="do">Count on fingers (2 min).</span> Hold up your book open at page 2, where hands show the numbers. Count 1 to 10 with the class, one finger for each number. Then call 3, 7, 5 and 10: children show each number on their fingers.
    <div class="say">Good morning, everyone. Let us count on our fingers. One finger for each number.</div></li>
   <li><span class="do">Count as far as you can (3 min).</span> Ask three or four children, one at a time, to count out loud as far as they can. Write the last number each child reaches on the board. Do not correct anyone yet. Quietly notice who skips a number, says one twice, or stops early: you will use this when you make groups.
    <div class="say">Thank you. Today we count all the way to twenty.</div></li>
  </ol></div>

 <div class="box sky"><h2>Hook: Guess, Then Count <span class="t">5 min</span></h2>
  <div style="display:flex;gap:4mm;align-items:center;margin:1mm 0 2.4mm;padding:2mm 4mm;background:#fff;border-radius:3mm;border:.3mm solid #C7D4EC">
   <div style="width:46mm;flex:none">{group_svg(HOOK_N, "stone", "row", w_mm=44, per_row=7)}</div>
   <div style="flex:1;font-size:9.6pt;line-height:1.4"><b>Stones in two rows on your desk.</b><br>Use {HOOK_N} real stones, in rows of seven. The picture shows how it should look.<br><span class="small">Teacher only: do not tell the children the number.</span></div>
  </div>
  <ol>
   <li><span class="do">Show the pile (1 min).</span> Lay the {HOOK_N} stones in two rows of seven where everyone can see.
    <div class="say">Are there more than ten stones, or fewer than ten? Hands up for more. Hands up for fewer.</div></li>
   <li><span class="do">Guess (1 min).</span> Take three guesses and write them on the board. Do not say who is closest.</li>
   <li><span class="do">Count to check (3 min).</span> Count the stones aloud, touching and moving each stone once, into a new line. Stop at the last stone.
    <div class="say">The last number is {HOOK_N}. A guess can be near. Counting tells us exactly how many.</div></li>
  </ol></div>

 <div class="board"><h3>WRITE ON THE BOARD</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.1"><div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Numbers, in rows of five</div>
    <div class="chalk" style="font-size:12pt;line-height:1.4;letter-spacing:.06em">{chalk_rows}</div></div>
   <div style="flex:1.3;border-left:.4mm dashed #7E9A8F;border-right:.4mm dashed #7E9A8F;padding:0 4mm;text-align:center">
    <div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1.4mm">A Ten Box (draw it big)</div>
    <div style="background:#fff;border-radius:2mm;padding:1.4mm;width:46mm;margin:0 auto">{boxes_svg(1, 0, 43)}</div>
    <div class="chalk" style="font-size:9pt;margin-top:1.4mm;line-height:1.35">2 rows of 5.<br>A full Ten Box holds 10.</div></div>
   <div style="flex:1.1;font-size:9.4pt;line-height:1.55"><div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Our counting rule</div>
    <b style="color:#FFD966">Touch</b> each one once.<br><b style="color:#FFD966">Say</b> one number.<br><b style="color:#FFD966">Move</b> it aside.<br>The <b style="color:#FFD966">last</b> number tells how many.</div>
  </div></div>
</div>
{F(2)}</section>"""


# ---------------- PAGE 3: teach and model (I Do) ----------------
def stage_row(i, title, mins, body, pic):
    return (f'<div style="display:flex;gap:3mm;align-items:center;border:.4mm solid var(--line);border-radius:3mm;padding:1.8mm 3mm;margin-bottom:1.6mm;background:#fff">'
            f'<div style="width:21mm;flex:none;text-align:center"><span class="num" style="width:7mm;height:7mm;font-size:11pt">{i}</span><div style="font-weight:800;font-size:8.6pt;margin-top:.5mm;line-height:1.15">{title}</div><div class="small">{mins} min</div></div>'
            f'<div style="width:62mm;flex:none;display:flex;justify-content:center;align-items:center">{pic}</div>'
            f'<div style="flex:1;font-size:8.7pt;line-height:1.28">{body}</div></div>')


def page3():
    spread = (f'<div style="display:flex;gap:2.4mm;align-items:center"><div style="text-align:center">{group_svg(6, "stone", "row", w_mm=25, per_row=3)}<div class="small" style="font-weight:800">6</div></div>'
              f'<div class="k" style="font-size:12pt">=</div><div style="text-align:center">{group_svg(6, "stone", "scatter", w_mm=25, seed=2)}<div class="small" style="font-weight:800">6</div></div></div>')
    ticks = (f'<div style="display:flex;gap:3mm;align-items:center">{ticked_svg(6, "apple", 3, 24)}<div class="k" style="font-size:12pt">and</div>{ticked_svg(9, "ball", 5, 30)}</div>')
    nine = (f'<div style="display:flex;gap:1.4mm;align-items:center"><div style="width:25mm">{boxes_svg(1, 9, 25)}</div><div class="k" style="font-size:10pt">+</div>'
            f'<div style="width:5.6mm">{group_svg(1, "stone", "row", w_mm=5.6)}</div><div class="k" style="font-size:10pt">=</div><div style="width:21mm">{boxes_svg(1, 10, 21)}</div></div>')
    past = f'<div style="display:flex;flex-direction:column;align-items:center;gap:1mm"><div style="width:58mm">{boxes_svg(2, 14, 58)}</div><div class="small" style="font-weight:800">full box + 4 more = 14</div></div>'
    r1 = stage_row(1, "Real things", 5,
                   "<b>Model (2 min):</b> count 6 stones. Touch one, say its number, move it aside. At the end, point to the last stone: “six”. Then spread the 6 stones a new way and ask: “How many now?” (Still six.) Do the same with 9.<br>"
                   "<b>Together (1.5):</b> count 9 with the class. <b>Try (1.5):</b> each group counts 6, then 9, from its pile.", spread)
    r2 = stage_row(2, "Pictures", 5,
                   "<b>Model (2 min):</b> hold up <b>Card A</b> (6 apples) and <b>Card B</b> (9 balls). Touch each picture and say its number. Draw a tick on the board for each one counted, so none is missed or counted twice.<br>"
                   "<b>Together (1.5):</b> count Card B again. <b>Try (1.5):</b> show <b>Card C</b> (13 fish). Children count in the air with a finger, then say how many.", ticks)
    r3 = stage_row(3, "Make ten", 5,
                   "<b>Model (2 min):</b> book <b>page 14</b>: 9 candies and 1 more is 10. On the board, put 9 stones in a Ten Box. One space is empty. Add 1 stone: the box is full. “A full Ten Box is ten.”<br>"
                   "<b>Together (1.5):</b> count the full box. <b>Try (1.5):</b> each group fills its Ten Box Mat with 10.", nine)
    r4 = stage_row(4, "Past ten", 5,
                   "<b>Model (2 min):</b> a full box and 4 more. Say <b>ten</b> for the full box, then keep going: eleven, twelve, thirteen, fourteen. Show the numerals 11 to 20 in the book, <b>page 18</b>, and read them aloud.<br>"
                   "<b>Together (1.5):</b> count 1 to 20 on the Number Chart. <b>Try (1.5):</b> groups make 14 on their mats.", past)
    beats = [("Model", "2 min", "I count and you watch. Touch, say, move. Point to the last one."),
             ("Together", "1.5 min", "We count together, two times. Then ask: “How many?”"),
             ("Try", "1.5 min", "Children count in their groups with their own stones. Then say how many.")]
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:2mm 2.6mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm;margin-bottom:1mm"><span class="n2">{i+1}</span><b style="font-size:10.5pt">{t}</b><span class="small" style="margin-left:auto;white-space:nowrap">{m}</span></div><div style="font-size:9pt;line-height:1.3">{d}</div></div>' for i, (t, m, d) in enumerate(beats))
    for r in (r1, r3, r4):          # these stages say "stones": no apples or balls may be drawn in them
        assert "#E0352B" not in r and "#F7C531" not in r, "picture does not match the word 'stones'"
        assert "#B8B1A5" in r or "#A9A398" in r or "#C4BDB0" in r or "#B0AA9F" in r, "no stones drawn"
    return f"""<section class="page">
{bar("Teach and Model", "I Do: real things, pictures, then the Ten Box", "20 min")}
<div class="content" style="zoom:1.1">
 <div class="box sky" style="padding:2.6mm 4mm"><h2 style="margin-bottom:1.2mm">Every stage has the same 3 beats <span class="t">5 min</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small" style="margin-top:1mm">Four stages, 5 minutes each. Start with real stones, then pictures, then numbers.</div></div>
 {r1}{r2}{r3}{r4}
 <div class="row" style="margin-top:2.4mm">
  <div class="box mint" style="margin-bottom:0"><h2 style="margin-bottom:1mm">Say it the same way every time</h2>
   <div style="font-size:9pt;line-height:1.34">
    <div class="say" style="margin:.8mm 0">I touch one stone and say “one”. I move it aside. I touch the next stone and say “two”.</div>
    <div class="say" style="margin:.8mm 0">The last number I said is six. So there are six stones.</div></div></div>
  <div class="box cream" style="margin-bottom:0"><h2 style="margin-bottom:1mm">Watch for these mistakes</h2>
   <ul style="font-size:8.7pt;line-height:1.3;padding-left:4mm">
    <li><b>Counting one twice, or missing one.</b> Move each object aside.</li>
    <li><b>Saying numbers faster than touching.</b> One touch, one number.</li>
    <li><b>Counting again when asked "How many?"</b> Ask: "What was the last number?"</li>
    <li><b>13 and 30, 14 and 40.</b> Say the end of "teen" clearly.</li></ul></div>
 </div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4: we do ----------------
def page4():
    silly = "".join(f'<tr><td style="width:30mm"><div style="display:flex;align-items:center;gap:1.6mm"><b style="width:3.6mm">{n}</b>{group_svg(n, "stone", "row", w_mm=22 if n < 8 else 23, per_row=5)}</div></td><td>{what}</td><td>{fix}</td></tr>' for n, what, fix in SILLY)
    piles = " ".join(f'<span class="chip" style="margin:0 .6mm .6mm 0">G{i+1}: {p}</span>' for i, p in enumerate(PILES))
    rows = " · ".join(f'<b>{n}</b> {o}' for n, o in BOOK_ROWS)
    return f"""<section class="page">
{bar("Let's Practise Together", "We Do: a silly counter, then groups, then the book", "12 min")}
<div class="content" style="zoom:.97">
 <div class="box mint"><h2>1. Silly Counter <span class="t">3 min</span></h2>
  <div style="display:flex;gap:3mm;align-items:flex-end">
   <div style="flex:1.5">{steps(["Tell the class: “I will count some stones. I might make a mistake. Shout <b>Stop</b> if you hear or see one.”",
          "Lay each set of stones in a row. Count one set at a time, making the mistake in the table. Let the class shout <b>Stop</b>.",
          "Ask: “What went wrong?” Then a child counts the stones the right way."])}</div>
   <div style="width:44mm;flex:none;padding-bottom:3mm"><div class="bub">“1, 2, 3, 5, 6 ... eight!”</div></div>
   <div style="width:30mm;flex:none">{scene("teacher_oops")}</div>
  </div>
  <table class="ans" style="margin-top:2mm;font-size:8.8pt"><tr><th>Stones</th><th>What the silly counter does</th><th>The mistake</th></tr>{silly}</table></div>

 <div class="box sky"><h2>2. Count and Swap <span class="t">5 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.45">{steps(["Children sit in <b>6 groups</b>. Give each group its <b>pile in a cup</b> and its Ten Box Mat. Do not tell them the number.",
          "Each group puts one stone in each box of its mat, top row first, then counts the stones together, touching each one. One child <b>touches the number on the Number Chart</b>.",
          "Groups <b>swap cups</b>, fill the mat again and count. Same number? Great. Different? Count once more, together, slowly."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.4mm">PILE SIZES (do not read aloud)</div>{piles}<div class="small" style="margin-top:1mm">A pile counted twice must give the same number.</div></div>
  </div></div>

 <div class="box cream"><h2>3. Check the Book <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm;align-items:center">
   <div style="flex:1.6">{steps(["Children sit in pairs. Open the book at <b>page 5</b>. Each row has a number and some pictures.",
          "<b>Partner A</b> touches and counts the pictures in a row. <b>Partner B</b> watches for mistakes. Then swap rows.",
          "Ask: “Is the book right?” Check the rows with " + rows + "."])}</div>
   <div style="flex:1;max-width:58mm;background:#fff;border-radius:3mm;padding:2mm 3mm;display:flex;gap:2mm;align-items:flex-end"><div style="width:26mm;flex:none">{scene("pair_book")}</div><div style="font-size:9pt;font-weight:700;padding-bottom:4mm;line-height:1.2">The book says 6. Do I count 6?</div></div>
  </div></div>

 <div class="row">
  <div class="cfu" style="flex:1.1"><b>CHECK BEFORE MOVING ON</b><br>Hold up <b>Card D</b> (17 stars). Ask 3 different children to count it aloud, touching each star in the air.
   <br><b>Most right?</b> Go on. <b>Most wrong?</b> Do Silly Counter again for 2 minutes.</div>
  <div class="box gold" style="flex:1;margin-bottom:3mm"><h2 style="color:var(--navy)">While you walk around</h2>
   <ul style="font-size:9.2pt"><li>Does each child touch <b>one object for each number</b>?</li><li>Does the same pile give the same number twice?</li><li>Give quiet children the smaller piles first.</li></ul></div>
 </div>
</div>
{F(4)}</section>"""


# ---------------- PAGE 5: your turn (answers only) + exit check ----------------
def page5():
    t1 = " &nbsp; ".join(f'<b class="k" style="font-size:11.5pt">{g[0]}</b>' for g in T1)
    t2 = " &nbsp; ".join(f'<span class="small" style="color:var(--ink)">{i+1}:</span> <b class="k" style="font-size:11.5pt">{n} dots</b>' for i, n in enumerate(T2))
    key = ""
    for i, e in enumerate(EXIT):
        if e[0] == "c":
            _, n, o, l, opts = e
            opt = "".join(f'<span class="k" style="width:6.6mm;height:6.6mm;display:inline-flex;align-items:center;justify-content:center;font-size:10pt;border:.3mm solid #9AA6B5;border-radius:50%;margin-right:.6mm;{"background:#F5B301;" if x == n else ""}">{x}</span>' for x in opts)
            key += f'<div style="display:flex;align-items:center;gap:1.6mm;margin-bottom:.9mm"><b style="width:3.6mm">{i+1}</b>{opt}<span class="small">{NUM[n]} ({pl(o)})</span></div>'
        else:
            key += f'<div style="display:flex;align-items:center;gap:1.6mm;margin-bottom:.9mm"><b style="width:3.6mm">{i+1}</b><span class="small" style="color:var(--ink)">draw <b>{e[1]}</b> dots in the Ten Box</span></div>'
    give = ", ".join(str(n) for n in ORAL_GIVE)
    return f"""<section class="page">
{bar("Your Turn and Exit Check", "You Do (8 min), then the Exit Check (10 min)", "18 min")}
<div class="content">
 <div class="box mint" style="padding-bottom:2mm"><h2>Your Turn <span class="t">8 min</span> <span class="small" style="font-weight:600;margin-left:auto">Student Worksheet, page 1. Read each task twice.</span></h2>
  <table class="ans"><tr><th style="width:30mm">Task</th><th style="width:17mm">Worksheet</th><th style="width:14mm">Time</th><th>Answers</th></tr>
   <tr><td><b>1</b> Count and circle how many</td><td>page 1</td><td>3 min</td><td>Top to bottom: {t1}</td></tr>
   <tr><td><b>2</b> Draw the dots</td><td>page 1</td><td>3 min</td><td>{t2}<div class="small" style="margin-top:.6mm">One dot in each box, top row first. Check by counting the dots.</div></td></tr>
   <tr><td><b>3</b> Join the dots</td><td>page 1</td><td>2 min</td><td style="display:flex;gap:4mm;align-items:center"><div style="width:26mm;flex:none">{dotdot_svg(26, solved=True)}</div><span style="font-size:9pt">Join 1 to 20 in order. A ten-pointed star appears. Stop at 8 minutes, finished or not.</span></td></tr>
  </table></div>

 <div class="box sky"><h2>Exit Check <span class="t">10 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.15;font-size:9.4pt">
    <p><b>Part A: count and show (6 min).</b> Give out <b>page 2 of the Student Worksheet</b>. Children write their names.</p>
    <div class="say">Count each picture and circle how many. Where you see a number and a Ten Box, draw that many dots.</div>
    <p style="margin-top:1.4mm">Say it twice. Children work alone, at their own speed. Stop at 6 minutes.</p>
    <p><b>Part B: count out (4 min).</b> While the others check their sheets, call up the children who looked unsure, one at a time. Say: <i>"Count out {ORAL_GIVE[0]} stones."</i> (or {ORAL_GIVE[1]} or {ORAL_GIVE[2]}). The child counts out stones from a cup, touching each, and says how many.</p></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.2mm 3mm"><div class="small" style="font-weight:800;color:var(--navy);margin-bottom:1.2mm">PART A: ANSWERS</div>{key}</div>
  </div></div>

 <div class="row">
  <div class="box mint"><h2>Score and decide</h2>
   <div style="font-size:9.2pt;line-height:1.35"><b>7 or 8 right:</b> ready. Day 2 goes as planned.<br><b>5 or 6 right:</b> nearly there. On Day 2, give these children two extra turns with Count and Swap.<br><b>4 or fewer:</b> needs help. On Day 2, seat them near you and start with piles of 10 or fewer.
   <div class="small" style="margin-top:1mm">Write each score on the Class Tally Sheet. Never read scores out loud.</div></div></div>
  <div class="navy box"><h2>Key facts to remember</h2>
   <div style="font-size:9.6pt;line-height:1.45">✓ Touch each object <b>once</b>.<br>✓ Say <b>one number</b> for each object.<br>✓ The <b>last number</b> tells how many.<br>✓ A full Ten Box is <b>10</b>.</div>
   <div class="small" style="color:#C9D6E6;margin-top:1.6mm">Say these lines with the class before they leave.</div></div>
 </div>

 <div class="box grey" style="margin-bottom:0"><b>At home (optional):</b> Count things at home, up to 20: spoons, steps, stones. Count them twice. Is the number the same?</div>
</div>
{F(5)}</section>"""


def build():
    html = (head_html("Level 1 Maths Day 1 - Lesson Plan v8").replace("</style>", EXTRA_CSS + "</style>")
            + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS)
    assert html.count("Stones in two rows") == 1 and "#F7C531" not in page2(), "Hook picture must show stones"
    out = os.path.join(WORK, "lp8.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
