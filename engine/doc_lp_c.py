"""Level 2 Intermediate, English, Day 1 (final planner): Lesson Plan only. Approved format (no Rumi logo) + LP RULES."""
from common_c import *

TOTAL = 5
F = lambda n: foot(FOOT_LP, n, TOTAL, mark=None)

EXTRA_CSS = FONT_CSS + """
.stp{display:flex;flex-direction:column;gap:2mm}
.stp .s{display:flex;gap:3mm;align-items:flex-start;font-size:10.4pt;line-height:1.3}
.stp .s>div{flex:1}
.n2{width:6.6mm;height:6.6mm;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:900;font-size:10.5pt;display:inline-flex;align-items:center;justify-content:center;flex:none;margin-top:.2mm}
table.ans{border-collapse:collapse;width:100%;font-size:10pt}
table.ans th{background:var(--navy);color:#fff;font-size:8.5pt;padding:1.6mm 2.4mm;text-align:left}
table.ans td{border-bottom:.3mm solid #C9D3E0;padding:1.5mm 2.4mm;vertical-align:middle}
.wc{display:inline-flex;align-items:center;font-family:Andika,sans-serif;font-weight:700;color:#001F3F;background:#fff;border:.4mm solid #C7D4EC;border-radius:2mm;padding:.6mm 2.2mm;font-size:11pt;margin:0 1mm 1mm 0}
.pt{display:inline-flex;align-items:center;justify-content:center;min-width:9mm;height:6.4mm;border-radius:1.8mm;color:#fff;font-family:Andika,sans-serif;font-weight:700;font-size:10.5pt;margin-right:1.6mm}
"""


def bar(title, sub, mins):
    return (f'<div class="bar"><div class="day">DAY<b>1</b></div><h1>{title}<small>{sub}</small></h1>'
            f'<div class="pill">{mins}</div></div>')


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{i+1}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


def ptag(p):
    return f'<span class="pt" style="background:{PATTERN_COL[p]}">{p}</span>'


def wchip(w):
    return f'<span class="wc">{w}</span>'


# ---------------- PAGE 1 ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d == 1:
            st = "background:#F5B301;color:#001F3F;font-weight:900;outline:.5mm solid #001F3F"
        elif d <= 4:
            st = "background:#FBE08A;color:#001F3F"
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
    def crow(p, ws):
        return (f'<div style="display:flex;align-items:center;gap:1mm;padding:.5mm 0;border-bottom:.3mm dashed #D5DDEA">{ptag(p)}'
                f'<span style="flex:1">{"".join(wchip(w) for w in ws)}</span></div>')
    chart = (f'<div style="display:flex;gap:5mm"><div style="flex:1">{"".join(crow(p, ws) for p, ws in GROUPS[:4])}</div>'
             f'<div style="flex:1">{"".join(crow(p, ws) for p, ws in GROUPS[4:])}</div></div>')
    return f"""<section class="page">
<div style="background:var(--navy);height:50mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:900;line-height:.92"><div style="font-size:56pt;letter-spacing:-.02em">DAY 1</div><div style="font-size:22pt;color:#fff">OF 33</div></div>
 <div style="flex:1;padding-left:4mm;border-left:.5mm solid #2B4A6B">
  <div style="font-size:15pt;font-weight:800;line-height:1.15">Intermediate · English</div>
  <div style="font-size:9.5pt;color:#C9D6E6;margin-top:1.5mm">Balochistan Winter Programme · Teaching at the Right Level</div>
  <div style="margin-top:2.6mm;display:flex;gap:2mm"><span class="pill" style="font-size:9pt;padding:1.4mm 3.6mm">60 minutes</span><span class="pill" style="font-size:9pt;padding:1.4mm 3.6mm;background:var(--gold);color:var(--navy)">Teach and model</span></div>
 </div>
 <div style="width:36mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("pair_book")}</div>
</div>
<div class="content" style="top:55mm">
 <div style="display:flex;gap:.8mm;margin-bottom:1mm">{ribbon}</div>
 <div class="small" style="margin-bottom:3mm">The 33 days. Days 1 to 4 (gold) teach reading with E-I-01, Days 5 to 30 move on to the other outcomes, Days 31 to 33 (green) are final consolidation.</div>

 <div class="box sky"><h2>The learning outcome</h2>
   <p style="margin-bottom:1mm"><span class="chip">E-I-01</span> <b>Read 3–5 letter words and short phrases fluently</b></p>
   <p class="small" style="margin:0">Core SLO, Days 1 to 4. Also today: <b>E-I-06</b> Read words with common blends and digraphs. Builds on E-B-07.</p>
 </div>
 <div class="box teal"><h2>Today's Goal</h2><div style="font-size:13pt;font-weight:800;line-height:1.2">Read words with cl, bl, dr, br, ch, sh, th and ph, and read short phrases.</div></div>

 <div class="box cream" style="margin-bottom:2.4mm"><h2>Today's words <span class="t">14 taught · 3 new in We Do</span></h2>
  <div style="font-size:9.2pt;margin-bottom:1mm">Print this chart on a large sheet or copy it onto the board before class. It is the <b>Word Chart</b> children use all lesson.</div>
  <div style="background:#fff;border-radius:3mm;padding:1.4mm 3mm;border:.3mm solid #C7D4EC">{chart}</div>
  <div class="small" style="margin-top:1.2mm"><b>Phrases:</b> black drum · brick shop · clap clap clap. &nbsp;<b>Quick Words</b> for the warm-up: {" · ".join(QUICK)}.
   <b>[PENDING: swap in the 33-Day Map phrases if it lists them.]</b></div></div>

 <div style="margin-bottom:3mm"><div style="font-size:9.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">THE 60 MINUTES</div>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden">{tbar}</div>
  <div class="small" style="margin-top:1mm">The last 10 minutes are the exit check, as on every day of the programme.</div></div>

 <div class="box grey"><h2>Your documents</h2>
  <ol style="padding-left:4.5mm;margin:0"><li><b>Lesson Plan</b> (this one): every word, the board layout and the exit-check answers</li><li><b>Prep Pack</b> and <b>Student Worksheet</b> come as separate documents</li></ol></div>

 <div class="box mint" style="margin-bottom:0"><h2>To prepare (about 15 minutes)</h2>
  <div style="columns:2;column-gap:6mm;font-size:9.4pt">
   <div>☐ Word Chart on the wall (above)</div>
   <div>☐ Chalk, duster, board</div>
   <div>☐ A slate or notebook page and pencil for each child</div>
   <div>☐ Your class list, for the exit-check tracker</div>
  </div></div>
</div>
{F(1)}</section>"""


# ---------------- PAGE 2 ----------------
def page2():
    hook_rows = "".join(f'<div style="display:flex;gap:2mm;align-items:center;margin-bottom:.8mm"><b class="k" style="width:15mm;font-size:11pt">{w}</b>'
                        f'<span style="font-size:9.6pt">{" ".join("/" + s + "/" for s in sy.split())}</span></div>' for w, sy in HOOK)
    return f"""<section class="page">
{bar("Start the Lesson", "Warm-up and Hook", "10 min")}
<div class="content">
<div style="zoom:1.2;display:flex;flex-direction:column;justify-content:space-between;height:210.0mm;overflow:hidden"><style>.zz>*{{flex:none}}</style>
 <div class="box grey"><h2>Warm-up: Read the Quick Words <span class="t">5 min</span></h2>
  <div style="float:right;width:25mm;margin:0 0 1mm 3mm;border-radius:3mm;overflow:hidden">{scene("teacher_point")}</div>
  <ol>
   <li><span class="do">Greet the class (1 min).</span>
    <div class="say">Good morning, everyone. Today we read longer words.</div></li>
   <li><span class="do">Read together (3 min).</span> Write the six Quick Words on the board: <b class="k">{" &nbsp; ".join(QUICK)}</b>. Point to each word. The class reads it. Then point in a mixed order: <b class="k">top, cat, bed, sun, hen, pot</b>.</li>
   <li><span class="do">Read alone (1 min).</span> Point to a word. One child reads it. Do this with 4 or 5 different children.</li>
  </ol></div>

 <div class="box sky"><h2>Hook: The Slow Robot <span class="t">5 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.5"><ol>
   <li><span class="do">Set the scene (1 min).</span>
    <div class="say">I am a slow robot. I say a word one sound at a time. You say the whole word.</div></li>
   <li><span class="do">Robot words (3 min).</span> Say the sounds, with a small stop between them. The class says the word. Children stand at their desks. For <b>clap</b>, the class claps once.</li>
   <li><span class="do">Show the word (1 min).</span> Write <b class="k">clap</b> on the board.
    <div class="say">Today we read words like this on paper. Look at the first two letters: c and l.</div></li></ol></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.4mm">ROBOT SAYS, IN ORDER</div>{hook_rows}
    <div class="small" style="margin:1mm 0 1mm">sh is one sound, /sh/.</div><div style="width:24mm;margin:0 auto">{wpic("clap")}</div></div>
  </div></div>

 <div class="board"><h3>WRITE ON THE BOARD</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.2"><div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Blends: two letters, each keeps its own sound</div>
    <div class="chalk" style="font-size:17pt;line-height:1.25">cl &nbsp; bl<br>dr &nbsp; br</div></div>
   <div style="flex:1.2;border-left:.4mm dashed #7E9A8F;border-right:.4mm dashed #7E9A8F;padding:0 4mm">
    <div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Digraphs: two letters, ONE sound</div>
    <div class="chalk" style="font-size:17pt;line-height:1.25">ch &nbsp; sh<br>th &nbsp; ph</div></div>
   <div style="flex:1.1;font-size:9.4pt;line-height:1.55"><div style="font-size:8.5pt;color:#BFD0C8;margin-bottom:1mm">Our four steps</div>
    <b style="color:#FFD966">1</b> Look at the letters<br><b style="color:#FFD966">2</b> Say each sound<br><b style="color:#FFD966">3</b> Join the sounds<br><b style="color:#FFD966">4</b> Read the word</div>
  </div></div>
</div></div>
{F(2)}</section>"""


# ---------------- PAGE 3 ----------------
def set_row(i, name, pat, mins, words, note):
    cards = ""
    for w, p in words:
        pic = wpic(w, "pic")
        pic = f'<span style="width:8.4mm;height:8.4mm;flex:none;display:inline-block">{pic}</span>' if pic else '<span style="width:8.4mm;height:8.4mm;flex:none;display:inline-block"></span>'
        cards += (f'<div style="display:flex;align-items:center;gap:2mm;margin-bottom:.6mm">{pic}{ptag(p)}<b class="wd" style="width:15mm;font-size:13pt">{w}</b>'
                  f'<span style="flex:1;white-space:nowrap">{boxes(w, 6.2, 11.5)}</span><span class="small" style="width:25mm;text-align:right;white-space:nowrap">{slash(w)}</span></div>')
    return (f'<div style="display:flex;gap:3mm;align-items:flex-start;border:.4mm solid var(--line);border-radius:3mm;padding:1.8mm 3mm;margin-bottom:1.5mm;background:#fff">'
            f'<div style="width:22mm;flex:none;text-align:center"><span class="num" style="width:7mm;height:7mm;font-size:11pt">{i}</span>'
            f'<div style="font-weight:800;font-size:8.6pt;margin-top:.5mm;line-height:1.15">{pat}</div><div class="small">{mins} min</div></div>'
            f'<div style="flex:1.45">{cards}</div>'
            f'<div style="flex:.8;font-size:8.6pt;line-height:1.28;background:#F6F9FD;border-radius:2.4mm;padding:1.6mm 2.4mm">{note}</div></div>')


def page3():
    rows = "".join(set_row(i + 1, s[0] + ": " + s[1], s[1], s[2], s[3], s[4]) for i, s in enumerate(SETS))
    blocks = [("Look", "Point to the word. Name the pair: the blend or the digraph.", "Cover the rest of the word if it helps."),
              ("Say each sound", "Touch each box as you say its sound. Children say it after you.", "Children touch the boxes in the air."),
              ("Join the sounds", "Say the sounds again, faster, and slide them into one word.", "Children join with you, then alone."),
              ("Read the word", "Say the word. Children read it two times.", "Then point to the word and the class reads it.")]
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:2mm 2.6mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm;margin-bottom:1mm"><span class="n2">{i+1}</span><b style="font-size:10pt">{t}</b></div><div style="font-size:8.8pt;line-height:1.28">{d}</div></div>' for i, (t, d, _) in enumerate(blocks))
    return f"""<section class="page">
{bar("Teach New Words", "I Do: four sets, four steps for every word", "20 min")}
<div class="content">
 <div class="box sky" style="padding:2.6mm 4mm"><h2 style="margin-bottom:1.2mm">Every word has the same 4 steps <span class="t">same wording every time</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small" style="margin-top:1mm">Write each word on the board, one at a time. Draw a box under each sound, as shown below. A digraph (ch, sh, th) or ck shares one box: it is one sound.</div></div>
 {rows}
 <div class="row" style="margin-top:2mm">
  <div class="box mint" style="margin-bottom:0"><h2 style="margin-bottom:1mm">Worked example: clap</h2>
   <div style="font-size:8.9pt;line-height:1.3">
    <div class="say" style="margin:.8mm 0">Look. The word is clap. The first two letters are c and l. They are a blend: each keeps its own sound.</div>
    <div class="say" style="margin:.8mm 0">Say the sounds: /k/ /l/ /a/ /p/. Now join them: clap. Read it with me: clap.</div></div></div>
  <div class="box cream" style="margin-bottom:0"><h2 style="margin-bottom:1mm">Watch for</h2>
   <ul style="font-size:8.7pt;line-height:1.28;padding-left:4mm">
    <li>Keep blend sounds close: /k/ /l/, never "kuh-luh". Say /b/ /r/, not "buh-ruh".</li>
    <li>c says /k/ in clap, clip. ck says /k/ in black, brick.</li>
    <li>ch, sh, th and ph are two letters, ONE sound. Never say "c and h together". ph says /f/.</li>
    <li>In phone the o says its name and the e is silent. Say the whole word and do not teach more.</li>
    </ul></div>
 </div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4 ----------------
def page4():
    cold = "".join(f'<div style="display:flex;align-items:center;gap:2mm;margin-bottom:.8mm"><b class="k" style="width:14mm;font-size:11.5pt">{w}</b>{boxes(w, 5.6, 10.5)}</div>' for w in COLD)
    return f"""<section class="page">
{bar("Let's Practise Together", "We Do: the whole class, standing at desks", "12 min")}
<div class="content">
<div style="zoom:1.12;display:flex;flex-direction:column;justify-content:space-between;height:225.0mm;overflow:hidden"><style>.zz>*{{flex:none}}</style>
 <div class="box mint"><h2>1. Read the Word Chart <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.6">{steps(["Children stand at their desks. Point to the Word Chart.",
          "Point to the words in the order shown. The class reads each word.",
          "Point to a word and wait. Say <i>\"Read it with me.\"</i> Then the class reads it. A wrong word? Say the sounds with the class, then join them."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.4mm">READ IN THIS ORDER</div>
    <div class="k" style="font-size:11pt;font-weight:700;line-height:1.5">{" · ".join(WE_DO_ORDER)}</div></div></div></div>

 <div class="box sky"><h2>2. Three new words <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.5">{steps(["Write the first new word on the board. Draw a box under each sound.",
          "Say <i>\"Look at the letters.\"</i> The class names the blend or digraph. Then the class says each sound with you.",
          "The class joins the sounds and reads the word. Do the same for the other two words.",
          "Ask: <i>\"Which letters make one sound?\"</i> Children point to the pair on the board."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.4mm">NEW WORDS, IN ORDER</div>{cold}
    <div class="small" style="margin-top:1mm">These use only the patterns you taught. ck says /k/.</div></div></div></div>

 <div class="box cream"><h2>3. Read the phrases <span class="t">4 min</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["Write the three phrases on the board. Point to each word as you read the phrase, once, slowly.",
          "The class reads the phrase with you. Then the class reads it again without you.",
          "Pairs turn to each other and read the phrase to each other. Walk around and listen."])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2.4mm 3mm;align-self:flex-start"><div style="font-size:8.5pt;font-weight:800;color:var(--navy);margin-bottom:1.2mm">PHRASES</div>
    <div class="k" style="font-size:12pt;font-weight:700;line-height:1.6">{"<br>".join(PHRASES)}</div>
    <div class="small" style="margin-top:1mm">For clap clap clap, the class claps three times.</div></div>
   <div style="width:27mm;flex:none;align-self:flex-start;border-radius:3mm;overflow:hidden">{scene("pair_book")}</div></div></div>

 <div class="row" style="">
  <div class="cfu" style="flex:1.1"><b>CHECK BEFORE MOVING ON</b><br>Point to 2 words from the chart. Hear 4 or 5 children: each reads one word alone.
   <br><b>Most right?</b> Go on. <b>Most wrong?</b> Do step 1 again for 2 minutes, sounds first.</div>
  <div class="box gold" style="flex:1;margin-bottom:3mm"><h2 style="color:var(--navy)">While you walk around</h2>
   <ul style="font-size:9.4pt"><li>Do they say both sounds in a blend?</li><li>Do they read ch, sh, th, ph as one sound?</li><li>Different children each time: hear 4 or 5, not everyone.</li></ul></div>
 </div>
</div></div>
{F(4)}</section>"""


# ---------------- PAGE 5 ----------------
def page5():
    board_items = ('<table style="border-collapse:collapse;width:100%;font-size:9.4pt">'
                   '<tr class="small" style="color:#5B6B80"><td></td><td>you say</td><td>write on the board</td><td>answer</td></tr>'
                   + "".join(f'<tr><td style="width:5mm"><b>{i+1}</b></td><td style="width:15mm"><b>{w}</b></td>'
                             f'<td style="white-space:nowrap">' + " &nbsp;".join(f"{ch}) {o}" for ch, o in zip("abc", opts)) + '</td>'
                             f'<td style="text-align:center"><b style="background:#F5B301;border-radius:50%;width:5.6mm;height:5.6mm;display:inline-flex;align-items:center;justify-content:center">{a}</b></td></tr>'
                             for i, (w, opts, a) in enumerate(EXIT)) + '</table>')
    sort = "".join(f'<tr><td style="width:12mm;padding:0"><span style="display:inline-flex;align-items:center;justify-content:center;min-width:8mm;height:4.8mm;border-radius:1.4mm;color:#fff;font-weight:700;font-size:9pt;background:{PATTERN_COL[p]}">{p}</span></td><td class="k">{" &nbsp; ".join(SORT_KEY[p])}</td></tr>' for p in SORT_ORDER)
    pb = "".join(f'<div style="margin-bottom:.6mm"><b>Child {i+1}:</b> <span class="k">{" · ".join(r)}</span></div>' for i, r in enumerate(PART_B))
    return f"""<section class="page">
{bar("Your Turn and Exit Check", "You Do (8 min), then the Exit Check (10 min)", "18 min")}
<div class="content" style="bottom:70mm"><div style="zoom:1.05;display:flex;flex-direction:column;justify-content:space-between;height:187.62mm;overflow:hidden">
 <div class="box mint" style="padding-bottom:2mm"><h2 style="margin-bottom:.6mm">Your Turn <span class="t">8 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.35;font-size:9.4pt">
    <p style="margin:0 0 1mm"><b>1. Read to a partner (4 min).</b> Pairs sit together and face the Word Chart. One child points to a word and reads it. The partner listens and checks the word on the chart. Then swap. Read down each pattern in turn.</p>
    <p style="margin:0"><b>2. Sort and copy (4 min).</b> Children write the eight headings <span class="k">cl bl dr br ch sh th ph</span> in their notebook and copy each of the 14 taught words under the right heading. They check their work against the Word Chart.</p>
    <div class="small" style="margin-top:1.2mm">Do the first heading together, as an example. Children need no teacher: the Word Chart shows the answers.</div></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:2mm 3mm"><div class="small" style="font-weight:800;color:var(--navy);margin-bottom:.8mm">SORT: ANSWERS</div>
    <table style="border-collapse:collapse;font-size:9.2pt;width:100%;line-height:1.15">{sort}</table></div>
  </div></div>

 <div class="box sky"><h2>Exit Check <span class="t">10 min</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:.9;font-size:9.4pt">
    <p><b>Part A: Listen and pick (6 min).</b> Write the six rows on the board (see the box). Children number 1 to 6 on a slate or notebook page. Say each word two times. Children read the three words and write the letter of the right one. Wait about 30 seconds.</p>
    <div class="say">Number one. Find the word clip. Write its letter.</div>
    <p style="margin-top:1.4mm"><b>Part B: Read it aloud (4 min).</b> Hear <b>4 or 5 children</b>, a different group each day. Point to three words on the Word Chart. The child reads them. Ask one child to read <span class="k">black drum</span>.</p>
    <div style="background:#fff;border-radius:2.4mm;padding:1.4mm 2.6mm;font-size:8.8pt;line-height:1.3"><div class="small" style="font-weight:800;color:var(--navy)">PART B: WORDS FOR EACH CHILD</div>{pb}</div></div>
   <div style="flex:1.15;background:#fff;border-radius:3mm;padding:2.2mm 3mm"><div class="small" style="font-weight:800;color:var(--navy);margin-bottom:1.2mm">PART A: BOARD AND ANSWERS</div>
    <div class="k">{board_items}</div></div>
  </div>
</div>

</div></div>
<style>.ftb .box{{padding:2mm 3.2mm;margin-bottom:0}}.ftb .box h2{{font-size:10pt;margin-bottom:1mm}}.ftb .row{{gap:3mm;margin-bottom:0}}</style><div class="ftb" style="position:absolute;left:10mm;right:10mm;bottom:12.5mm;zoom:.9;border-top:.5mm solid var(--gold);padding-top:2mm">
 <div class="row">
  <div class="box mint"><h2>Score and decide</h2>
   <div style="font-size:9.2pt;line-height:1.35"><b>On track:</b> 5 or 6 right in Part A. <br><b>Practise:</b> 4 right. Do Read to a partner again with these children on Day 2.<br><b>Re-teach:</b> 3 or fewer right. Repeat the 4 steps for the patterns they missed, in a small group.
   <div class="small" style="margin-top:1mm">Write each child's status on your class list. Never read scores out loud. Part B: note any child who read a pair as two sounds, for example "sh" as /s/ /h/.</div></div></div>
  <div class="navy box"><h2>Key facts to remember</h2>
   <div style="font-size:9.6pt;line-height:1.45">✓ A <b>blend</b>: two letters, each keeps its own sound.<br>✓ A <b>digraph</b>: two letters, <b>one</b> sound.<br>✓ Say the sounds, then <b>join</b> them.</div>
   <div style="display:flex;align-items:flex-end;gap:3mm;margin-top:1.6mm"><div class="small" style="color:#C9D6E6;flex:1">Say these three lines with the class before they leave.</div><div style="width:26mm;border-radius:3mm;overflow:hidden;flex:none">{scene("kids_wave")}</div></div></div>
 </div>
<div class="box grey" style="margin:2mm 0 0 0"><b>At home (optional):</b> Read the words clap, drum, ship and phone to someone at home.</div>
</div>
{F(5)}</section>"""


def build():
    html = (head_html("Intermediate English Day 1 - Lesson Plan").replace("</style>", EXTRA_CSS + "</style>")
            + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS)
    out = os.path.join(WORK, "lpc.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
