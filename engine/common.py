"""Shared data + design system for the Level 1 English Day 1 documents (LP, Prep Pack, Worksheet).
Single source of truth: every letter, call list and answer key lives here so the three PDFs cannot disagree."""
import os

WORK = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(WORK, "img")

LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
WORDS = dict(A="apple", B="ball", C="cat", D="duck", E="egg", F="fish", G="goat", H="hen", I="ice cream",
             J="jug", K="kite", L="lion", M="mango", N="net", O="orange", P="pen", Q="quilt", R="rabbit",
             S="sun", T="teapot", U="umbrella", V="van", W="watch", X="xylophone", Y="yo-yo", Z="zebra")
# How to SAY each letter name (British/Pakistani English: Z = zed)
NAMES = dict(A="ay", B="bee", C="see", D="dee", E="ee", F="ef", G="jee", H="aitch", I="eye", J="jay", K="kay",
             L="el", M="em", N="en", O="oh", P="pee", Q="kyoo", R="ar", S="ess", T="tee", U="yoo", V="vee",
             W="double-yoo", X="ex", Y="why", Z="zed")
CHUNKS = [("A to E", "ABCDE"), ("F to J", "FGHIJ"), ("K to O", "KLMNO"), ("P to T", "PQRST"), ("U to Z", "UVWXYZ")]
# Tile colours follow the student book's alphabet card (4 colours cycling across a 4-column grid)
TILE = ["#2AA7C7", "#F08A3C", "#4DB857", "#E85C9B"]


def tile_colour(letter):
    return TILE[LETTERS.index(letter) % 4]


# ---- activity data (used by LP, Call Sheet and Worksheet) ----
SHOW_ME = list("GMATRZKESW")                       # We Do, "Show me!" call list (10)
MATCH_CAPS = list("DGMRTW")                        # worksheet task 1, left column
MATCH_SMALLS = list("tmwdrg")                      # right column, shuffled
MATCH_KEY = {c: c.lower() for c in MATCH_CAPS}
CIRCLE_ROWS = [("KMS", "M"), ("htz", "t"), ("BFQ", "F"), ("wgr", "g"), ("YAJ", "J")]   # task 2: (options, call)
GRID = ["SnsKo", "mSwsT", "zsASh", "PesdS", "uSVgs"]   # task 3: colour every S and s
GRID_TARGET = sum(ch in "Ss" for row in GRID for ch in row)
EXIT_ROWS = [("BHX", "H"), ("aeu", "e"), ("PRT", "R"), ("kvy", "k"), ("MNW", "W"), ("fjs", "j"), ("SYZ", "Z"), ("pmo", "p")]
ORAL_CARDS = list("DGSAMR")                        # exit check part B, any three per child

assert GRID_TARGET == 10
for opts, call in CIRCLE_ROWS + EXIT_ROWS:
    assert call in opts and len(set(opts)) == 3, (opts, call)
for c, s in zip(MATCH_CAPS, MATCH_SMALLS):
    pass
assert sorted(MATCH_SMALLS) == sorted(c.lower() for c in MATCH_CAPS)
assert all(MATCH_CAPS[i].lower() != MATCH_SMALLS[i] for i in range(6))   # no accidental straight-across answers


def pic(letter, cls="pic"):
    """Picture tile for a letter's keyword. Falls back to a labelled dashed box until the picture exists."""
    f = os.path.join(IMG, f"obj_{letter}.jpg")
    word = WORDS[letter]
    if os.path.exists(f):
        return f'<img class="{cls}" src="img/obj_{letter}.jpg" alt="{word}">'
    return f'<div class="{cls} pending"><span>{word}</span></div>'


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
.foot img{height:4.2mm;width:auto;margin-right:2mm;vertical-align:middle}
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
.tiles{display:flex;gap:2mm;flex-wrap:wrap}
.lt{font-family:Nunito,sans-serif;font-weight:900;color:#fff;border-radius:2.2mm;text-align:center;line-height:1;
display:flex;align-items:center;justify-content:center}
.pic{width:100%;height:auto;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:3mm;display:block}
.pic.pending{border:.4mm dashed #9AA6B5;display:flex;align-items:center;justify-content:center;color:#7A8594;font-size:8pt;text-align:center}
.scene{width:100%;height:auto;display:block}
.board{background:#27403A;border:2mm solid #B07A3A;border-radius:2.5mm;color:#F4F7F2;padding:3mm 4mm;margin-bottom:3mm}
.board h3{margin:0 0 1.6mm;color:#FFD966;font-size:10pt;font-weight:800;letter-spacing:.02em}
.board .chalk{font-family:Nunito,sans-serif;font-weight:800}
.coach{background:var(--c2);color:#fff;border-radius:1.8mm;width:15mm;height:11mm;display:flex;align-items:center;justify-content:center;
font-family:Nunito,sans-serif;font-weight:900;font-size:14pt;position:relative}
.wheels{display:flex;gap:6mm;margin-top:.5mm}
"""

FOOT_LP = "Level 1 Beginner · English · Day 1 of 33 · Lesson Plan"


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


def foot(label, n, total, mark="rumi-mark-navy-transparent.png"):
    img = f'<img src="{mark}" alt="Rumi">' if mark else ""
    return (f'<div class="foot"><span>{img}{label}</span><span>Page {n} of {total}</span></div>')
