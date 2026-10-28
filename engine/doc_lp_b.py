"""Level 1 Beginner, English, Day 1 (final planner): Lesson Plan. Approved format (no Rumi logo) + LP RULES."""
from common_b import *

TOTAL = 5
F = lambda n: foot(FOOT_LP, n, TOTAL, mark=None)

EXTRA_CSS = FONT_CSS + """
.stp{display:flex;flex-direction:column;gap:2mm}
.stp .s{display:flex;gap:3mm;align-items:flex-start;font-size:10.4pt;line-height:1.3}
.stp .s>div{flex:1}
.n2{width:6.6mm;height:6.6mm;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:900;font-size:10.5pt;display:inline-flex;align-items:center;justify-content:center;flex:none;margin-top:.2mm}
table.ans{border-collapse:collapse;width:100%;font-size:10pt}
table.ans th{background:var(--navy);color:#fff;font-size:8.5pt;padding:1.6mm 2.4mm;text-align:left}
table.ans td{border-bottom:.3mm solid #C9D3E0;padding:1.7mm 2.4mm;vertical-align:middle}
"""


def bar(title, sub, mins):
    return (f'<div class="bar"><div class="day">DAY<b>1</b></div><h1>{title}<small>{sub}</small></h1>'
            f'<div class="pill">{mins}</div></div>')


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{i+1}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


def chip_letters(items, size=7.4, fs=12):
    return " ".join(f'<span class="lt" style="display:inline-flex;width:{size}mm;height:{size}mm;font-size:{fs}pt;font-weight:700;background:{TILE[l.upper()]};color:#fff;margin-right:.8mm">{t}</span>' for t, l in items)


# ---------------- PAGE 1 ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d == 1:
            st = "background:#F5B301;color:#001F3F;font-weight:900;outline:.5mm solid #001F3F"
        elif d <= 7:
            st = "background:#FBE08A;color:#001F3F"
        elif d <= 9:
            st = "background:#E9EEF6;color:#3A4A63"
        elif d >= 31:
            st = "background:#BDE5D2;color:#064B38"
        else:
            st = "background:#E6E9EE;color:#7A8594"
        ribbon += f'<span style="flex:1;height:7mm;border-radius:1.2mm;display:flex;align-items:center;justify-content:center;font-size:6.2pt;{st}">{d}</span>'
    bits = [("Warm-up", 5, "#6C7A8D"), ("Hook", 5, "#0B8F6A"), ("I Do: teach", 20, "#F5B301"), ("We Do: practise together", 12, "#F08A3C"),
            ("You Do", 8, "#2AA7C7"), ("Exit check", 10, "#001F3F")]
    tbar = "".join(f'<div style="flex:{m};background:{c};color:{"#001F3F" if c in ("#F5B301","#F08A3C","#2AA7C7") else "#fff"};'
                   f'padding:1.6mm 1.2mm;font-size:7.4pt;font-weight:800;text-align:center;line-height:1.15">{n}<br><span style="font-weight:600">{m} min</span></div>'
                   for n, m, c in bits)
    return f"""<section class="page">
<div style="background:var(--navy);height:50mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:900;line-height:.92"><div style="font-size:56pt;letter-spacing:-.02em">DAY 1</div><div style="font-size:22pt;color:#fff">OF 33</div></div>
 <div style="flex:1;padding-left:4mm;border-left:.5mm solid #2B4A6B">
  <div style="font-size:15pt;font-weight:800;line-height:1.15">Level 1 Beginner · English</div>
  <div style="font-size:9.5pt;color:#C9D6E6;margin-top:1.5mm">Balochistan Winter Programme · Teaching at the Right Level</div>
  <div style="margin-top:2.6mm;display:flex;gap:2mm"><span class="pill" style="font-size:9pt;padding:1.4mm 3.6mm">60 minutes</span><span class="pill" style="font-size:9pt;padding:1.4mm 3.6mm;background:var(--gold);color:var(--navy)">Teach new letters</span></div>
 </div>
 <div style="width:36mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("kids_wave")}</div>
</div>
<div class="content" style="top:55mm">
 <div style="display:flex;gap:.8mm;margin-bottom:1mm">{ribbon}</div>
 <div class="small" style="margin-bottom:3mm">The 33 days. Days 1 to 7 (gold) teach new letters, Days 8 and 9 are catch-up, Days 31 to 33 (green) are final consolidation.</div>

 <div class="box gold" style="display:flex;gap:4mm;align-items:center">
  <div style="display:flex;gap:1.4mm">{"".join(tile(l, 13, 16, 20) for l in LETTERS)}</div>
  <div><div style="font-size:8.5pt;font-weight:800;letter-spacing:.05em">TODAY'S LETTERS</div>
  <div style="font-size:19pt;font-weight:900;line-height:1.1">Meet A, B, C and D</div>
  <div style="font-size:10pt;font-weight:600">Name, sound and writing: capital and small</div></div>
 </div>

 <div class="box sky"><h2>The learning outcomes</h2>
   <p style="margin-bottom:1mm"><span class="chip">E-B-01</span> <b>Recognise and name the 26 letters (capital and small)</b></p>
   <p style="margin-bottom:1mm"><span class="chip">E-B-02</span> <b>Say the sound of each letter and the first sound of a spoken word</b></p>
   <p style="margin-bottom:1mm"><span class="chip">E-B-03</span> <b>Write a letter when it is read aloud</b></p>
   <p class="small" style="margin:0">Core SLOs, taught on Days 1 to 9. Also today: <b>E-B-04</b> Copy and trace letters with correct formation (left to right).</p>
 </div>
 <div class="box teal"><h2>Today's Goal</h2><div style="font-size:13pt;font-weight:800;line-height:1.2">Say the name and the sound of A, B, C and D, and write each letter.</div></div>

 <div class="box cream" style="margin-bottom:2.4mm"><h2>Four letters only today</h2>
  <p style="margin:0">Teach <b>A, B, C, D</b> and no more (4 new letters a day at most). Picture words: <b>ant, bed, cat, dog</b>. Children say only these letters, sounds and words today.</p></div>

 <div style="margin-bottom:3mm"><div style="font-size:9.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">THE 60 MINUTES</div>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden">{tbar}</div>
  <div class="small" style="margin-top:1mm">The last 10 minutes are the exit check, as on every day of the programme.</div></div>

 <div class="row">
  <div class="box grey"><h2>Student book</h2>
   <p style="margin:0"><b>Unit 1, Time to Recall</b><br>Page 2: cat and bed pictures<br><b>Page 3: alphabet card, first row (Aa Bb Cc Dd)</b><br>Page 6: trace and copy letters</p></div>
  <div class="box grey"><h2>Your three documents</h2>
   <ol style="padding-left:4.5mm"><li><b>Lesson Plan</b> (this one)</li><li><b>Prep Pack</b>: cut and print before class</li><li><b>Student Worksheet</b>: 1 per child, both sides</li></ol></div>
 </div>

 <div class="box mint" style="margin-bottom:0"><h2>To prepare (about 20 minutes)</h2>
  <div style="columns:2;column-gap:6mm;font-size:9.4pt">
   <div>☐ Letter Chart on the wall</div>
   <div>☐ Cut out the 4 Picture-Letter Cards</div>
   <div>☐ Cut out one Desk Letter Strip for each child</div>
   <div>☐ Teacher Call Sheet next to you</div>
   <div>☐ Student Worksheet: one per child, both sides</div>
   <div>☐ Chalk, duster, and a slate and pencil for each child</div>
  </div></div>
</div>
{F(1)}</section>"""


# ---------------- PAGE 2 ----------------
def page2():
    paper = ''.join(f'<span class="lt" style="display:inline-flex;width:13mm;height:13mm;font-size:22pt;font-weight:700;background:{TILE[l]};color:#fff;margin-right:2mm">{l}</span>' for l in LETTERS)
    return f"""<section class="page">
{bar("Start the Lesson", "Warm-up and Hook", "10 min")}
<div class="content">
<div style="zoom:1.2;display:flex;flex-direction:column;justify-content:space-between;height:210.0mm;overflow:hidden"><style>.zz>*{{flex:none}}</style>
 <div class="box grey"><h2>Warm-up: Say the Picture Words <span class="t">5 min</span></h2>
  <ol>
   <li><span class="do">Greet the class (1 min).</span>
    <div class="say">Good morning, everyone. Today we meet four new letters.</div></li>
   <li><span class="do">Say the four words (4 min).</span> Point to each picture on the Letter Chart: <b>ant</b>, <b>bed</b>, <b>cat</b>, <b>dog</b>. Say the word. Children say it after you, two times. Then say a word at random and children show you its picture on the chart.</li>
  </ol></div>

 <div class="box sky"><h2>Hook: Four Letter Friends <span class="t">5 min</span></h2>
  <div style="margin:1mm 0 2.6mm;padding:2.4mm 3.4mm;background:#fff;border-radius:3mm;border:.3mm solid #C7D4EC;display:flex;align-items:center;gap:3mm">{paper}<div class="small" style="flex:1">Before class, write A, B, C, D big on the board and cover each one with a piece of paper.</div></div>
  <ol>
   <li><span class="do">Set the scene (1 min).</span>
    <div class="say">Four new friends have come to school today. They are letters. Let us meet them.</div></li>
   <li><span class="do">Meet the friends (2 min).</span> Take the paper off one letter. Say its name. Children say the name after you and wave to the letter. Do A, then B, then C, then D.</li>
   <li><span class="do">Which letter is hiding? (2 min).</span> Cover one letter again.
    <div class="say">Which letter is hiding?</div>Children say the name. Take the paper off to check. Do this three times.</li>
  </ol></div>


 <div class="board"><h3>WRITE ON THE BOARD</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.3"><div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Today's letters: capital and small</div>
    <div class="chalk" style="font-size:20pt;line-height:1.15;letter-spacing:.04em">A a &nbsp; B b<br>C c &nbsp; D d</div></div>
   <div style="flex:1.1;border-left:.4mm dashed #7E9A8F;border-right:.4mm dashed #7E9A8F;padding:0 4mm">
    <div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Picture words</div>
    <div class="chalk" style="font-size:12pt;line-height:1.4">A ant<br>B bed<br>C cat<br>D dog</div></div>
   <div style="flex:1.1;font-size:9.4pt;line-height:1.55"><div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Our four actions</div>
    <b style="color:#FFD966">1</b> Say the name<br><b style="color:#FFD966">2</b> Say the sound<br><b style="color:#FFD966">3</b> Trace it<br><b style="color:#FFD966">4</b> Write it</div>
  </div></div>
</div></div>
{F(2)}</section>"""


# ---------------- PAGE 3 ----------------
def letter_row(i, l):
    return (f'<div style="display:flex;gap:3mm;align-items:center;border:.4mm solid var(--line);border-radius:3mm;padding:1.6mm 3mm;margin-bottom:1.4mm;background:#fff">'
            f'<div style="width:21mm;flex:none;text-align:center"><span class="num" style="width:7mm;height:7mm;font-size:11pt">{i}</span>'
            f'<div style="font-weight:800;font-size:8.6pt;margin-top:.5mm;line-height:1.1">Letter {l}</div><div class="small">5 min</div></div>'
            f'<div style="flex:none">{tile(l, 24, 17, 30)}</div>'
            f'<div style="width:17mm;flex:none">{bpic(l)}</div>'
            f'<div style="flex:1;font-size:9.6pt;line-height:1.35"><div class="wd" style="font-size:15pt;font-weight:700;line-height:1">{WORD[l]}</div>'
            f'<div><b>Name:</b> {l} (say "{NAME_SAY[l]}")</div><div><b>Sound:</b> /{SOUND[l]}/ <span class="small">{SOUND_HINT[l]}</span></div></div></div>')


def page3():
    rows = "".join(letter_row(i + 1, l) for i, l in enumerate(LETTERS))
    blocks = [("Say the name", "1 min", "Show the card. Say: capital, small, then the name. Children say the name two times."),
              ("Say the sound", "1.5 min", "Say the picture word, then the sound. Children say them after you."),
              ("Trace it", "1 min", "Trace the capital and the small letter in the air, then on the desk. Say the sound as you trace."),
              ("Write it", "1.5 min", "Write the capital and the small letter on the board. Children write them on a slate or notebook page. They check with the chart.")]
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:2mm 2.6mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm;margin-bottom:1mm"><span class="n2">{i+1}</span><b style="font-size:10pt">{t}</b><span class="small" style="margin-left:auto">{m}</span></div><div style="font-size:8.8pt;line-height:1.28">{d}</div></div>' for i, (t, m, d) in enumerate(blocks))
    return f"""<section class="page">
{bar("Teach New Letters", "I Do: four letters, four actions each", "20 min")}
<div class="content">
 <div class="box sky" style="padding:2.6mm 4mm"><h2 style="margin-bottom:1.2mm">Every letter has the same 4 actions <span class="t">5 min a letter</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small" style="margin-top:1mm">Do all 4 actions for A. Then repeat them for B, then C, then D.</div></div>
 {rows}
 <div class="row" style="margin-top:2mm">
  <div class="box mint" style="margin-bottom:0"><h2 style="margin-bottom:1mm">Worked example: letter B</h2>
   <div style="font-size:8.9pt;line-height:1.3">
    <div class="say" style="margin:.8mm 0">This is capital B. This is small b. The name is B. Say it with me: B.</div>
    <div class="say" style="margin:.8mm 0">The picture word is bed. The first sound is /b/. Say it: /b/.</div>
    Trace B in the air, then b. Then write B and b on your slate. Check with the chart: are they the same?</div></div>
  <div class="box cream" style="margin-bottom:0"><h2 style="margin-bottom:1mm">Watch for</h2>
   <ul style="font-size:8.7pt;line-height:1.28;padding-left:4mm">
    <li>Say sounds short and clean: /b/, not "buh". C says /k/, not /s/.</li>
    <li>The name and the sound are different: A is said "ay", its sound is /a/.</li>
    <li>The book shows small a with a roof. We write it without the roof. Show both: same letter.</li>
    <li>b and d are mirror images. Teach them in separate steps. Point to capital B and D first.</li></ul></div>
 </div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4 ----------------
def page4():
    return f"""<section class="page">
{bar("Let's Practise Together", "We Do: the whole class, standing at desks", "12 min")}
<div class="content">
<div style="zoom:1.08;display:flex;flex-direction:column;justify-content:space-between;height:233.33mm;overflow:hidden"><style>.zz>*{{flex:none}}</style>
 <div class="box mint"><h2>1. Name it, sound it <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.6">{steps(["Children stand at their desks. Point to a letter on the chart.",
          "Round 1, names: point to A, B, C, D. The class says each <b>name</b>. Then point in this order: C, A, D, B.",
          "Round 2, sounds: point to A, B, C, D. The class says each <b>sound</b>. Then point in the same mixed order."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.4mm">SOUNDS</div>
    <div style="font-size:9.6pt;line-height:1.45">A /a/ · B /b/ · C /k/ · D /d/</div><div class="small" style="margin-top:1mm">Names and sounds are done in separate rounds.</div></div></div></div>

 <div class="box sky"><h2>2. Show me! <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.5">{steps(["Children take their <b>Desk Letter Strip</b>.",
          "<b>Names:</b> say a letter name two times. Say: <i>\"Show me ... C!\"</i> Children touch that letter on the strip.",
          "<b>Sounds:</b> say a sound two times. Say: <i>\"Show me ... /k/!\"</i> Children touch that letter.",
          "Look at the fingers. Wrong letter? Point to the right one on the chart and say it together."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">NAMES, IN ORDER</div>{chip_letters([(t.replace("small ", ""), l) for t, l in SHOW_NAMES])}<div class="small" style="margin:1mm 0 2mm">The last two are the small letters a and c.</div>
    <div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">SOUNDS, IN ORDER</div><div style="font-size:11pt;font-weight:700">/k/ &nbsp; /b/ &nbsp; /a/ &nbsp; /d/</div></div>
  </div></div>

 <div class="box cream"><h2>3. Write it <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["Children take a slate or notebook page and a pencil.",
          "Say what to write: <i>\"Write capital A.\"</i> Children write it. Then write it on the board.",
          "Children check their letter against the board and the chart, then fix it if they need to."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">SAY, IN THIS ORDER</div><div style="font-size:9.6pt;line-height:1.5">capital A · small c · capital B · small a · capital D · small d</div></div></div></div>

 <div class="row" style="">
  <div class="cfu" style="flex:1.1"><b>CHECK BEFORE MOVING ON</b><br>Hear 4 or 5 children: each says the name of one letter you point to, then its sound.
   <br><b>Most right?</b> Go on. <b>Most wrong?</b> Do round 2 of Show me again for 2 minutes.</div>
  <div class="box gold" style="flex:1;margin-bottom:3mm"><h2 style="color:var(--navy)">While you walk around</h2>
   <ul style="font-size:9.4pt"><li>Is the finger on the right letter?</li><li>Are the sounds short and clean?</li><li>Different children each time: hear 4 or 5, not everyone.</li></ul></div>
 </div>
</div></div>
{F(4)}</section>"""


# ---------------- PAGE 5 ----------------
def page5():
    t1 = " &nbsp; ".join(f'<b class="k" style="font-size:11.5pt">{c} {s}</b>' for c, s in T1_ROWS)
    t2 = " &nbsp; ".join(f'<b class="k" style="font-size:11.5pt">{c} &rarr; {T2_KEY[c]}</b>' for c in T2_CAPS)
    t3 = " &nbsp; ".join(f'<b class="k" style="font-size:11pt">{p} &rarr; {T3_KEY[p]}</b>' for p in T3_PICS)
    key = ""
    for i, it in enumerate(EXIT):
        if it["options"]:
            opt = "".join(f'<span class="k" style="width:6.6mm;height:6.6mm;display:inline-flex;align-items:center;justify-content:center;font-size:11pt;'
                          f'border:.3mm solid #9AA6B5;border-radius:50%;margin-right:.6mm;{"background:#F5B301;" if ch == it["answer"] else ""}">{ch}</span>' for ch in it["options"])
        else:
            opt = f'<span class="small" style="color:var(--ink)">child writes</span> <b class="k" style="font-size:12pt">{it["answer"]}</b>'
        key += f'<div style="display:flex;align-items:center;gap:1.6mm;margin-bottom:.9mm"><b style="width:3.6mm">{i+1}</b>{opt}<span class="small">{it["kind"]}</span></div>'
    return f"""<section class="page">
{bar("Your Turn and Exit Check", "You Do (8 min), then the Exit Check (10 min)", "18 min")}
<div class="content" style="bottom:70mm">
<div style="zoom:1.2;display:flex;flex-direction:column;justify-content:space-between;height:164.17mm;overflow:hidden">
 <div class="box mint" style="padding-bottom:2mm"><h2 style="margin-bottom:.6mm">Your Turn <span class="t">8 min</span></h2>
  <p class="small" style="margin:0 0 1.6mm">Student Worksheet, page 1. Do the first line of each task together. Children check their own work with the Desk Letter Strip.</p>
  <table class="ans"><tr><th style="width:36mm">Task</th><th style="width:17mm">Worksheet</th><th style="width:17mm">Time</th><th>Answers</th></tr>
   <tr><td><b>1</b> Trace and copy</td><td>page 1</td><td style="white-space:nowrap">3 min</td><td>{t1}</td></tr>
   <tr><td><b>2</b> Match capital and small</td><td>page 1</td><td style="white-space:nowrap">2 min</td><td>{t2}</td></tr>
   <tr><td><b>3</b> Match picture and first letter</td><td>page 1</td><td style="white-space:nowrap">3 min</td><td>{t3}</td></tr>
  </table></div>

 <div class="box sky"><h2>Exit Check <span class="t">10 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.1;font-size:9.4pt">
    <p><b>Part A: Listen and show (6 min).</b> Give out <b>page 2 of the Student Worksheet</b>. Children write their names. Say each item two times and wait about 30 seconds.</p>
    <div class="say">Number one. Circle the letter B.</div>
    <p style="margin-top:1.4mm">Children work alone. Items 1 and 2 are names, items 3 and 4 are sounds, item 5 is writing.</p>
    <p><b>Part B: Say it aloud (4 min).</b> Hear <b>4 or 5 children</b>, a different group each day. Point to B, D, A or C on the chart. The child says the name. Then ask for the sound.</p></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.2mm 3mm"><div class="small" style="font-weight:800;color:var(--navy);margin-bottom:1.2mm">PART A: ANSWERS</div>{key}</div>
  </div></div>

</div></div>
<style>.ftb .box{{padding:2mm 3.2mm;margin-bottom:0}}.ftb .box h2{{font-size:10pt;margin-bottom:1mm}}.ftb .row{{gap:3mm;margin-bottom:0}}</style><div class="ftb" style="position:absolute;left:10mm;right:10mm;bottom:12.5mm;zoom:.9;border-top:.5mm solid var(--gold);padding-top:2mm">
 <div class="row">
  <div class="box mint"><h2>Score and decide</h2>
   <div style="font-size:9.2pt;line-height:1.35"><b>On track:</b> 4 or 5 right.<br><b>Practise:</b> 3 right. Do Show me again with these children on Day 2.<br><b>Re-teach:</b> 2 or fewer right. Repeat the 4 actions for the letters they missed, in a small group.
   <div class="small" style="margin-top:1mm">Write each child's status on the Class Tally Sheet. Never read scores out loud.</div></div></div>
  <div class="navy box"><h2>Key facts to remember</h2>
   <div style="font-size:9.6pt;line-height:1.45">✓ Every letter has a <b>name</b>.<br>✓ Every letter has a <b>sound</b>.<br>✓ Every letter has a <b>capital</b> and a <b>small</b> form.</div>
   <div class="small" style="color:#C9D6E6;margin-top:1.6mm">Say these three lines with the class before they leave.</div></div>
 </div>
<div class="box grey" style="margin:2mm 0 0 0"><b>At home (optional):</b> Say A, B, C, D and the words ant, bed, cat, dog to someone at home.</div>
</div>
{F(5)}</section>"""


def build():
    html = (head_html("Level 1 English Day 1 - Lesson Plan").replace("</style>", EXTRA_CSS + "</style>")
            + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS)
    out = os.path.join(WORK, "lpb.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
