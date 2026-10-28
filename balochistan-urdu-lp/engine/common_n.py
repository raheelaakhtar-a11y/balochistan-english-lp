"""Level 1 Beginner, URDU, Day 1 (28 Oct planner): Teach new letters ا ب پ ت ٹ ث (sound, picture word, write in isolated form).
SLOs: U-B-01 (recognise the letters), U-B-02 (sound + first sound of a spoken word), U-B-03 (write a letter when read aloud),
support U-B-04 (copy and trace, right to left). Letters are taught BY SOUND (planner difficulty note), never by letter name.
One source of truth for the Lesson Plan, Prep Pack and Worksheet: every call list and answer key lives here.
Picture words come from the Balochistan Grade 1 Urdu book, Lesson 1, printed p.1: انار ، بٹن ، پری ، توا ، ٹرک."""
import os

WORK = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(WORK, "img")


def ur(n):
    return str(n).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))


LETTERS = ["ا", "ب", "پ", "ت", "ٹ", "ث"]                 # alphabet order
WORD = {"ا": "انار", "ب": "بٹن", "پ": "پری", "ت": "توا", "ٹ": "ٹرک", "ث": "ثمر"}
PIC = {"ا": "u1_anar", "ب": "u1_button", "پ": "u1_pari", "ت": "u1_tawa", "ٹ": "u1_truck", "ث": "u2_samar"}
SOUND = {"ا": "اَ", "ب": "بْ", "پ": "پْ", "ت": "تْ", "ٹ": "ٹْ", "ث": "ثْ"}   # the short sound, no vowel after it
HOW = {"ا": "منہ کھول کر چھوٹی سی آواز، جیسے انار کا پہلا حصہ",
       "ب": "ہونٹ ملا کر چھوٹی آواز: بْ (“با” نہیں)",
       "پ": "ہونٹ ملا کر ہوا کے ساتھ: پْ (“پا” نہیں)",
       "ت": "زبان دانتوں کے پیچھے: تْ (“تا” نہیں)",
       "ٹ": "زبان کی نوک اوپر مڑی ہوئی: ٹْ (“ٹا” نہیں)",
       "ث": "دانتوں کے درمیان سے ہوا، سانپ کی سی آواز: ثْ (“ثا” نہیں)"}
LOOK = {"ا": "ا ایک سیدھی لکیر ہے۔ اسے اوپر سے نیچے لکھیں۔",
        "ب": "ب کے نیچے ایک نقطہ ہے۔",
        "پ": "پ کے نیچے تین نقطے ہیں۔",
        "ت": "ت کے اوپر دو نقطے ہیں۔",
        "ٹ": "ٹ کے اوپر چھوٹی ط کی نشانی ہے۔",
        "ث": "ث کے اوپر تین نقطے ہیں۔"}
TILE = {"ا": "#2AA7C7", "ب": "#F08A3C", "پ": "#4DB857", "ت": "#E85C9B", "ٹ": "#7B61C9", "ث": "#C28A00"}

# similar-sounding pairs are never asked next to each other, and never offered together in one exit item
SIMILAR = [{"ب", "پ"}, {"ت", "ٹ"}]

# We Do (all call lists are SOUNDS, said short)
CHANT_ORDER = ["ا", "ب", "پ", "ت", "ٹ", "ث"]
CHANT_MIXED = ["ب", "ث", "ا", "ت", "پ", "ٹ"]
SHOW_ME = ["ٹ", "ا", "ب", "ث", "ت", "پ"]
WRITE_CALLS = ["ا", "ت", "ث", "ب", "ٹ", "پ"]

# You Do, worksheet page 1
T1_LETTERS = LETTERS                                  # trace and copy
T2_PICS = ["پ", "ث", "ا", "ٹ", "ت", "ب"]                   # picture shown for each of these letters, in this order (right column)
T2_LETTERS = LETTERS                                  # left column, in this order
T3_ROWS = [("ب", ["ا", "ب", "ث", "ب", "پ"]), ("ث", ["ت", "ث", "ٹ", "ا", "ث"]), ("ٹ", ["ٹ", "پ", "ا", "ث", "ٹ"]),
           ("پ", ["ا", "پ", "ب", "پ", "ٹ"]), ("ت", ["ث", "ت", "ت", "ب", "ٹ"]), ("ا", ["ا", "ث", "ا", "ب", "ٹ"])]   # (target, five options)

# Exit check: 5 single-answer items, sounds only (the planner teaches sounds, not names)
EXIT = [dict(kind="سن کر گھیرنا", sound="ب", options=["ا", "ت", "ب"], answer="ب"),
        dict(kind="سن کر گھیرنا", sound="ث", options=["ث", "ا", "پ"], answer="ث"),
        dict(kind="سن کر گھیرنا", sound="ٹ", options=["ب", "ٹ", "ث"], answer="ٹ"),
        dict(kind="سن کر گھیرنا", sound="ا", options=["پ", "ث", "ا"], answer="ا"),
        dict(kind="لکھنا", sound="ت", options=None, answer="ت")]
PART_B = ["ب", "ٹ", "ث", "ا", "پ", "ت"]
NUM_WORD = ["ایک", "دو", "تین", "چار", "پانچ"]
PASS_NOTE_UNUSED = "پاس مارک ۵ میں سے ۴ ہے (۲۱ اکتوبر کی ایکسل شیٹ سے)۔ یہ نئی PDF میں نہیں ہے [زیرِ تصدیق]۔"


def _similar_adjacent(seq):
    return any({a, b} in SIMILAR for a, b in zip(seq, seq[1:]))


# ---- checks (the three PDFs cannot disagree) ----
assert sorted(CHANT_MIXED) == sorted(LETTERS) and sorted(SHOW_ME) == sorted(LETTERS) and sorted(WRITE_CALLS) == sorted(LETTERS)
for seq in (CHANT_ORDER[:2], CHANT_MIXED, SHOW_ME, WRITE_CALLS, PART_B):
    assert not _similar_adjacent(seq), seq
assert sorted(T2_PICS) == sorted(LETTERS) and all(T2_PICS[i] != T2_LETTERS[i] for i in range(6)), "no straight-across picture answers"
for tgt, opts in T3_ROWS:
    assert tgt in opts and len(opts) == 5 and len(T3_ROWS) == 6
for it in EXIT:
    if it["options"]:
        assert it["answer"] in it["options"] and len(set(it["options"])) == 3
        assert not any(s <= set(it["options"]) for s in SIMILAR), "similar-sounding letters offered together"
pos = [it["options"].index(it["answer"]) for it in EXIT if it["options"]]
assert len(set(pos)) > 1, "answer is always in the same place"
assert set(LETTERS) == set(WORD) == set(PIC) == set(SOUND) == set(TILE)


def pic(letter, cls="pic"):
    word = WORD[letter]
    f = os.path.join(IMG, f"{PIC[letter]}.jpg")
    if os.path.exists(f):
        return f'<img class="{cls}" src="img/{PIC[letter]}.jpg" alt="{word}">'
    return f'<div class="{cls} pending"><span>{word}</span></div>'


def scene(name, cls="scene"):
    f = os.path.join(IMG, f"scene_{name}.jpg")
    return f'<img class="{cls}" src="img/scene_{name}.jpg" alt="">' if os.path.exists(f) else ""


def tile(letter, w=14, h=11, fs=22):
    return (f'<span class="lt" style="width:{w}mm;height:{h}mm;font-size:{fs}pt;background:{TILE[letter]};color:#fff;'
            f'border-radius:2.2mm;display:inline-flex;align-items:flex-start;justify-content:center;line-height:1.3;padding-top:{max(.6, fs*.03):.1f}mm">{letter}</span>')


def snd(letter, size="inherit"):
    return f'<span class="sn" style="font-size:{size}">{SOUND[letter]}</span>'


CSS = r"""
@font-face{font-family:"NNU";src:url("fonts/NotoNastaliqUrdu.ttf");font-weight:400 700}
:root{--navy:#001F3F;--gold:#F5B301;--paper:#FAF7F2;--ink:#1D2025;--mint:#E3F4EC;--teal:#0B8F6A;--sky:#E8EEF8;
--cream:#FFF6DC;--line:#D7DCE3;--grey:#5B6572}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;font-family:NNU,"Noto Nastaliq Urdu",serif;color:var(--ink);direction:rtl;
-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:10.6pt;line-height:1.95;word-spacing:.12em;letter-spacing:0}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.bar{height:25mm;background:var(--navy);color:#fff;display:flex;align-items:center;padding:0 10mm;gap:5mm}
.bar .day{background:var(--gold);color:var(--navy);font-weight:700;border-radius:50%;width:15mm;height:15mm;display:flex;
flex-direction:column;align-items:center;justify-content:center;line-height:1.05;font-size:8pt}
.bar .day b{font-size:17pt;display:block;line-height:1.1}
.bar h1{margin:0;font-size:17pt;font-weight:700;line-height:1.5;flex:1}
.bar h1 small{display:block;font-size:9pt;font-weight:400;color:#C9D6E6;line-height:1.6}
.pill{background:#0B8F6A;color:#fff;border-radius:99px;padding:.4mm 4.5mm;font-weight:700;font-size:11pt;white-space:nowrap;line-height:2}
.content{position:absolute;left:10mm;right:10mm;top:30mm;bottom:15mm;overflow:hidden}
.foot{position:absolute;left:10mm;right:10mm;bottom:4mm;height:8mm;display:flex;align-items:center;justify-content:space-between;
font-size:8pt;color:var(--grey);border-top:.3mm solid var(--line);line-height:1.6}
.box{border-radius:3.5mm;padding:2mm 4.2mm;margin-bottom:3mm;border:.4mm solid transparent}
.box h2{margin:0 0 .6mm;font-size:12pt;font-weight:700;color:var(--navy);display:flex;align-items:center;gap:2.5mm;line-height:1.8}
.box h2 .t{font-size:8.6pt;background:var(--navy);color:#fff;border-radius:99px;padding:0 2.8mm;font-weight:700;white-space:nowrap;line-height:1.9}
.box p{margin:0 0 1mm}
.box ul,.box ol{margin:0;padding-inline-start:5.5mm}
.box li{margin-bottom:.4mm}
.mint{background:var(--mint);border-color:#B9E2CF}
.sky{background:var(--sky);border-color:#C7D4EC}
.cream{background:var(--cream);border-color:#F2D98B}
.gold{background:var(--gold);color:var(--navy)}
.teal{background:var(--teal);color:#fff}.teal h2{color:#fff}
.navy{background:var(--navy);color:#fff}.navy h2{color:var(--gold)}
.grey{background:#F1F3F6;border-color:#DDE2E8}
.say{background:#fff;border:.4mm dashed #8CA3C4;border-radius:3mm;padding:.2mm 3.4mm;margin:1mm 0;color:#14304F}
.say:before{content:"کہیں: ";font-weight:700;color:var(--teal)}
.do{font-weight:700}
.cfu{background:var(--teal);color:#fff;border-radius:3mm;padding:1.6mm 4mm;margin-bottom:3mm}
.cfu b{color:var(--gold)}
.row{display:flex;gap:3mm}.row>*{flex:1;min-width:0}
.chip{display:inline-block;background:var(--navy);color:#fff;border-radius:2mm;padding:0 2.2mm;font-weight:700;font-size:9pt;font-family:Arial,sans-serif;direction:ltr;line-height:1.7}
.small{font-size:8.8pt;color:var(--grey);line-height:1.8}
.num,.n2{width:7mm;height:7mm;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:700;font-size:10.5pt;
display:inline-flex;align-items:center;justify-content:center;flex:none;line-height:1}
.lt{font-weight:400;color:#fff;border-radius:2.2mm;text-align:center;line-height:1;display:flex;align-items:center;justify-content:center}
.sn{font-weight:700}
.pic{width:100%;height:auto;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:3mm;display:block}
.pic.pending{border:.4mm dashed #9AA6B5;display:flex;align-items:center;justify-content:center;color:#7A8594;font-size:9pt}
.scene{width:100%;height:auto;display:block}
.board{background:#27403A;border:2mm solid #B07A3A;border-radius:2.5mm;color:#F4F7F2;padding:2mm 4mm;margin-bottom:3mm}
.board h3{margin:0 0 .6mm;color:#FFD966;font-size:10.5pt;font-weight:700;line-height:1.8}
.stp{display:flex;flex-direction:column;gap:.6mm}
.stp .s{display:flex;gap:3mm;align-items:flex-start;line-height:1.85}
.stp .s>div{flex:1}
table.ans,table.t{border-collapse:collapse;width:100%}
table.ans th,table.t th{background:var(--navy);color:#fff;font-size:8.8pt;padding:0 2.4mm;text-align:right;font-weight:700;line-height:2}
table.ans td,table.t td{border-bottom:.3mm solid #C9D3E0;padding:.4mm 2.4mm;vertical-align:middle;line-height:1.9}
table.t td,table.t th{border:.3mm solid #B9C2CE;text-align:center}
"""

FOOT_LP = "لیول ۱ بنیادی · اردو · دن ۱ از ۳۳ · لیسن پلان"
FOOT_PREP = "لیول ۱ بنیادی · اردو · دن ۱ از ۳۳ · تیاری کا پیکٹ"
FOOT_WS = "لیول ۱ بنیادی · اردو · دن ۱ · طالب علم کی ورک شیٹ"


def head_html(title):
    return (f'<!doctype html><html lang="ur" dir="rtl"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}</style></head><body>')


OVERFLOW_JS = """<script>
window.addEventListener('load',function(){var bad=[];
document.querySelectorAll('.page').forEach(function(p,i){
 p.querySelectorAll('.content,.chk').forEach(function(c){
  if(c.scrollHeight>c.clientHeight+1){bad.push('page'+(i+1)+':'+c.className+':'+(c.scrollHeight-c.clientHeight)+'px');}
  });});
 document.title='OVF:'+(bad.length?bad.join(' | '):'OK');});
</script></body></html>"""


def foot(label, n, total):
    return f'<div class="foot"><span>{label}</span><span>صفحہ {ur(n)} از {ur(total)}</span></div>'
