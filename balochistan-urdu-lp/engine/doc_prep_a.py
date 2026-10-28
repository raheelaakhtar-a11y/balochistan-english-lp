"""Level 3 Advanced, Urdu, Day 1 (28 Oct planner): Prep Pack (print-safe, no Rumi logo)."""
from common_a import *

TOTAL = 7
EXTRA_CSS = """
.card{border:.35mm dashed #8D99A8;padding:2.4mm;display:flex}
.card .in{flex:1;border:1.2mm solid var(--c);border-radius:4mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:1.6mm 2mm 2.2mm;background:#fff}
.cardgrid{position:absolute;left:10mm;right:10mm;top:21mm;height:259mm;display:grid;overflow:hidden}
.cs table.t td{line-height:1.45;padding:0 1.4mm}.slim{height:15mm}.slim h1{font-size:13pt}
:root{--grey:#1D2025;--teal:#064B38}
.small{color:#1D2025}
.en{color:#064B38;font-weight:700}
.box h2 .en{color:#1D2025;border-color:#1D2025}
.foot{color:#1D2025}
"""

EN = {"تیاری کا پیکٹ": "Preparation pack", "جملہ بدلنے کا چارٹ": "Sentence-change chart", "استاد کی رہنما شیٹ": "Teacher call sheet", "کلاس ٹریکر": "Class tally sheet"}


def bar(title, sub):
    return bar2(title, EN[title], sub)


def F(n):
    return foot(FOOT_PREP, n, TOTAL)


def p1():
    inside = [("جملہ بدلنے کا چارٹ", "صفحہ ۲", "بچوں کی آنکھ کی سطح پر دیوار پر لگائیں"),
              ("استاد کی رہنما شیٹ", "صفحہ ۳", "تمام فہرستیں اور تمام جوابات"),
              ("تصویر والے کارڈ (۸)", "صفحہ ۴", "موٹے کاغذ پر ایک طرف پرنٹ کریں۔ نقطہ دار لکیروں پر کاٹیں"),
              ("لفظی کارڈ (۱۲)", "صفحہ ۵", "بورڈ پر لگانے کے لیے۔ نقطہ دار لکیروں پر کاٹیں"),
              ("ڈیسک پٹیاں", "صفحہ ۶", "ہر جوڑی کے لیے ایک پٹی پرنٹ کریں۔ نقطہ دار لکیروں پر کاٹیں"),
              ("کلاس ٹریکر", f"صفحہ {ur(TOTAL)}", "ہر بچے کی حالت لکھیں: ٹھیک چل رہا ہے، مشق چاہیے یا دوبارہ پڑھائیں")]
    rows = "".join(f'<tr><td style="text-align:right;font-weight:700;padding:.4mm 3mm">{a}</td><td style="width:22mm"><b>{b}</b></td><td style="text-align:right;padding:.4mm 3mm">{c}</td></tr>' for a, b, c in inside)
    return f"""<section class="page">{bar("تیاری کا پیکٹ", "کلاس سے پہلے پرنٹ کرنے، کاٹنے اور جمع کرنے کی ہر چیز")}
<div class="content">
 <div class="box gold" style="display:flex;gap:4mm;align-items:center"><div style="flex:1"><div style="font-size:9pt;font-weight:700;line-height:1.7">لیول ۳ ایڈوانس · اردو · دن ۱</div>
  <div style="font-size:16pt;font-weight:700;line-height:2.1">ایک · کئی · لڑکا · لڑکی</div><div style="font-size:10pt;line-height:1.8">تیاری میں تقریباً ۲۰ منٹ لگیں گے۔ یہ پیکٹ لیسن پلان کے ساتھ رکھیں۔</div></div>
  <div style="width:30mm;border-radius:4mm;overflow:hidden;background:#fff">{scene("teacher_point")}</div></div>

 <div style="font-size:9.5pt;font-weight:700;color:var(--navy);margin:1mm 0 .4mm;line-height:1.8">اس پیکٹ میں کیا ہے</div>
 <table class="t" style="margin-bottom:3.4mm;font-size:9.4pt">{rows}</table>

 <div class="row">
  <div class="box mint"><h2><span class="en">Print and cut</span>پرنٹ کریں اور کاٹیں</h2>
   <div style="font-size:9.8pt;line-height:1.9">☐ چارٹ (صفحہ ۲): ۱ کاپی<br>☐ تصویر والے کارڈ (صفحہ ۴): ۱ سیٹ<br>☐ لفظی کارڈ (صفحہ ۵): ۱ سیٹ<br>☐ <b>ڈیسک پٹی: ہر جوڑی کے لیے ۱</b><br>☐ <b>ورک شیٹ: ہر بچے کے لیے ۱</b> (صفحہ ۳ ایک طرف پرنٹ کریں)<br>☐ استاد کی رہنما شیٹ (صفحہ ۳): ۱ کاپی<br>☐ کلاس ٹریکر (صفحہ {ur(TOTAL)}): ۱ کاپی</div></div>
  <div class="box sky"><h2><span class="en">Gather</span>جمع کریں</h2>
   <div style="font-size:9.8pt;line-height:1.9">☐ چاک اور ڈسٹر<br>☐ ہر بچے کے لیے کاپی کا صفحہ<br>☐ ہر بچے کے لیے پنسل<br>☐ چارٹ اور کارڈ لگانے کے لیے ٹیپ<br>☐ ورک شیٹ صفحہ ۳ کے لیے قینچی اور پیپر کلپ</div></div>
 </div>

 <div class="box cream"><h2><span class="en">Five minutes before class</span>بچوں کے آنے سے ۵ منٹ پہلے</h2>
  <ol style="font-size:9.8pt;line-height:1.85">
   <li><b>جملہ بدلنے کا چارٹ</b> آنکھ کی سطح پر دیوار پر لگائیں۔</li>
   <li>بارہ لفظی کارڈ بورڈ کے پاس رکھیں۔ اس ترتیب میں: چھوٹا، لڑکا، پڑھتا، ہے، پھر باقی کارڈ۔</li>
   <li>آٹھ تصویر والے کارڈ ترتیب سے رکھیں: پہلے ایک لڑکا اور ایک کتا، پھر کئی لڑکے اور کئی کتے، پھر لڑکی اور بلی۔</li>
   <li>ڈیسک پٹیاں اور ورک شیٹیں ایسی جگہ رکھیں جہاں ہاتھ پہنچے۔</li>
   <li>رہنما شیٹ ایک بار پڑھیں۔ ہر جملے کے سب لفظ بدلنے کی مشق کریں۔</li></ol></div>

 <div class="box grey" style="margin-bottom:0"><b>پرنٹنگ کا مشورہ:</b> اگر کارڈ یا پٹیاں پرنٹ نہ ہو سکیں تو لفظ اور تصویر ہاتھ سے کاغذ پر بنا لیں۔ ہر قسم کے لفظ کا ڈبہ الگ طرح کا بنائیں: نام (ٹھوس لکیر)، کیسا (ٹوٹی لکیر)، کام (نقطوں والی لکیر)۔</div>
</div>{F(1)}</section>"""


def p2():
    rows = ""
    for f in FORMS:
        side = "".join(f'<div style="text-align:center;flex:1"><div style="width:18mm;margin:0 auto">{apic(s, f)}</div><div style="line-height:1.55;margin-top:.6mm">{chips(set_words(s, f), 12.5)}</div></div>' for s in ("A", "B"))
        rows += (f'<div style="border:.5mm solid {FCOL[f]};border-radius:5mm;padding:2mm 6mm;display:flex;align-items:center;gap:5mm;background:#fff">'
                 f'<div style="flex:none">{ftile(f, 30, 24, 20)}</div>'
                 f'<div style="width:46mm;flex:none"><div style="font-size:22pt;font-weight:700;line-height:1.5">{FLABEL[f]}</div>'
                 f'<div style="font-size:10pt;line-height:1.7">{FRULE[f]}</div></div>'
                 f'<div style="flex:1;display:flex;gap:4mm">{side}</div></div>')
    return f"""<section class="page">{bar("جملہ بدلنے کا چارٹ", "ایک جملہ، چار شکلیں")}
<div style="position:absolute;left:10mm;right:10mm;top:31mm;bottom:30mm;display:grid;grid-template-rows:repeat(4,minmax(0,1fr));gap:2.4mm">{rows}</div>
<div style="position:absolute;left:10mm;right:10mm;bottom:15mm;display:flex;gap:6mm;justify-content:center;align-items:center">
 <span class="small" style="font-weight:700">لفظ کی قسم:</span><span class="cw rn" style="font-size:11pt">لڑکا<i>نام (اسم)</i></span><span class="cw ra" style="font-size:11pt">چھوٹا<i>کیسا (صفت)</i></span><span class="cw rv" style="font-size:11pt">پڑھتا<i>کام (فعل)</i></span><span class="cw rh" style="font-size:11pt">ہے<i>ملانے کا لفظ</i></span></div>
{F(2)}</section>"""


def p3():
    lines = [("ms", "چھوٹا لڑکا پڑھتا ہے۔")]
    we1 = "".join(f'<tr><td style="width:6mm"><b>{ur(i+1)}</b></td><td style="font-weight:700;font-size:11.5pt">{we1_noun(f)}</td><td style="text-align:right;font-weight:700;font-size:11pt">{we1_sentence(f)}</td></tr>' for i, f in enumerate(WE1_CALLS))
    we3 = "".join(f'<tr><td style="width:6mm"><b>{ur(i+1)}</b></td><td style="text-align:right">{w}</td><td style="text-align:right;font-weight:700">{r}</td></tr>' for i, (w, r) in enumerate(WE3))
    t1 = " &nbsp; ".join(f'{set_sent(*it)[:-1]} ← {ur(T1_PICS.index(it) + 1)}' for it in T1_ITEMS)
    t2 = " &nbsp; ".join(f"{ur(i+1)}: <b>{t['answer']}</b>" for i, t in enumerate(T2))
    t3 = " &nbsp; ".join(f"{ur(i+1)}۔ دائرہ: <b>{words(*a)[1]}</b> · لکیر: <b>{words(*a)[0]}</b> · ڈبہ: <b>{words(*a)[2]}</b>" for i, a in enumerate(T3))
    ex = "".join(f'<tr><td style="width:6mm"><b>{ur(i+1)}</b></td><td style="text-align:right;font-weight:700;font-size:10.5pt">{it["answer"]}</td><td style="width:22mm">{["پہلا", "دوسرا", "تیسرا"][it["pos"]]} جملہ</td></tr>' for i, it in enumerate(EXIT))
    pb = "".join(f'<tr><td><b>{ur(i+1)}</b></td><td style="text-align:right;line-height:1.75">' + "<br>".join(f'{sent(a, n, v, f0)[:-1]} ← <b>{sent(a, n, v, f1)[:-1]}</b>' for a, n, v, f0, f1 in card) + "</td></tr>" for i, card in enumerate(PART_B))
    return f"""<section class="page">{bar("استاد کی رہنما شیٹ", "سبق کے دوران اسے اپنے پاس رکھیں")}
<div class="content cs" style="top:29mm">
 <div class="box gold" style="margin-bottom:2.4mm;padding:.6mm 4mm;font-size:10pt;line-height:1.75"><b>آخری آواز اور آخر کا لفظ:</b><br>{" &nbsp;|&nbsp; ".join(f"<span style='white-space:nowrap'>{FLABEL[f]}: <b>{ENDING_TXT[f]}</b> اور <b>{HELP[f]}</b></span>" for f in FORMS)}</div>
 <div class="row" style="gap:3mm">
  <div class="box sky" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">We do 1 · Change the name card</span>نام کارڈ بدلیں (چھوٹا · لڑکا · پڑھتا · ہے)</h2>
   <table class="t" style="font-size:9pt"><tr><th></th><th>نیا نام کارڈ</th><th style="text-align:right">درست جملہ</th></tr>{we1}</table></div>
  <div class="box cream" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">We do 3 · Fix the sentence</span>غلط جملہ ٹھیک کریں</h2>
   <table class="t" style="font-size:9pt"><tr><th></th><th style="text-align:right">غلط جملہ</th><th style="text-align:right">درست جملہ</th></tr>{we3}</table></div>
 </div>
 <div class="box mint" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Answers · worksheet page 1</span>اکیلے: جوابات</h2>
  <div style="font-size:9.2pt;line-height:1.85"><b>۱ جملہ سے تصویر (نمبر اوپر سے):</b> {t1}<br><b>۲ درست لفظ:</b> {t2}<br><b>۳ لفظ کی قسم:</b> {t3}</div></div>
 <div class="row" style="gap:3mm">
  <div class="box mint" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Exit check · Part A</span>حصہ الف: جوابات (ورک شیٹ صفحہ ۲)</h2>
   <table class="t" style="font-size:9pt"><tr><th></th><th style="text-align:right">درست جملہ</th><th>جگہ</th></tr>{ex}</table></div>
  <div class="box cream" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Tracker</span>ٹریکر (حصہ الف کا اسکور)</h2>
   <div style="font-size:9.6pt;line-height:1.95"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ درست<br><b>مشق چاہیے:</b> ۳ درست<br><b>دوبارہ پڑھائیں:</b> ۲ یا کم درست<br><span class="small">ہر بچے کی حالت کلاس ٹریکر (صفحہ ۷) پر لکھیں۔ نمبر بلند آواز میں نہ بتائیں۔</span></div></div>
 </div>
 <div class="box mint" style="margin-bottom:0;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Part B</span>حصہ ب: بدل کر بولیں (۴ منٹ)</h2>
  <div style="font-size:9pt;line-height:1.8;margin-bottom:.8mm">۴ یا ۵ بچوں سے ایک ایک کارڈ کروائیں، ہر دن مختلف بچے۔ آپ پہلا جملہ بولیں، بچہ ایک سے کئی یا کئی سے ایک بدل کر بولے۔ سب لفظ درست ہوں تو ٹک لگائیں۔</div>
  <table class="t" style="font-size:9pt"><tr><th style="width:14mm">کارڈ</th><th style="text-align:right">آپ بولیں ← بچہ بولے</th></tr>{pb}</table></div>
</div>{F(3)}</section>"""


ENDING_TXT = {"ms": "ا ا ا", "mp": "ے ے ے", "fs": "ی ی ی", "fp": "ی ی ی"}


def pcard(s, f):
    return (f'<div class="card" style="--c:{FCOL[f]}"><div class="in"><div style="width:35mm">{apic(s, f)}</div>'
            f'<div style="text-align:center;line-height:1.7">{chips(set_words(s, f), 15, False)}</div>'
            f'<div style="font-size:9pt;font-weight:700;color:#1D2025;line-height:1.5">{FLABEL[f]}</div></div></div>')


def p4():
    order = [(s, f) for s in ("A", "B") for f in FORMS]
    return (f'<section class="page"><div class="bar slim"><div class="day" style="width:10mm;height:10mm;font-size:5.5pt"><b style="font-size:11pt">۱</b></div>'
            f'<h1><span class="en">Picture cards</span>تصویر والے کارڈ<small>آٹھ کارڈ، نقطہ دار لکیروں پر کاٹیں</small></h1></div>'
            f'<div class="cardgrid" style="grid-template-columns:repeat(2,1fr);grid-template-rows:repeat(4,64.5mm)">{"".join(pcard(s, f) for s, f in order)}</div>{F(4)}</section>')


WORDCARDS = [("چھوٹا", "a"), ("چھوٹے", "a"), ("چھوٹی", "a"), ("لڑکا", "n"), ("لڑکے", "n"), ("لڑکی", "n"), ("لڑکیاں", "n"),
             ("پڑھتا", "v"), ("پڑھتے", "v"), ("پڑھتی", "v"), ("ہے", "h"), ("ہیں", "h")]
assert [w for w, _ in WORDCARDS if _ == "a"] == list(ADJ["chota"]) and [w for w, _ in WORDCARDS if _ == "v"] == list(VERB["parhna"])


def wcard(w, r):
    lab = f"<i>{ROLE[r]}</i>" if ROLE[r] else ""
    return (f'<div class="card"><div class="in" style="--c:{ {"a": "#F08A3C", "n": "#2AA7C7", "v": "#4DB857", "h": "#9AA6B5"}[r] };justify-content:center;gap:2mm">'
            f'<div class="cw r{r}" style="font-size:34pt;border-width:1mm;padding:2mm 7mm;line-height:1.6;margin:0">{w}</div><div style="font-size:11pt;font-weight:700;color:#1D2025;line-height:1.5">{ROLE[r] or "ملانے کا لفظ"}</div></div></div>')


def p5():
    return (f'<section class="page"><div class="bar slim"><div class="day" style="width:10mm;height:10mm;font-size:5.5pt"><b style="font-size:11pt">۱</b></div>'
            f'<h1><span class="en">Word cards</span>لفظی کارڈ<small>بارہ کارڈ، بورڈ پر لگانے کے لیے، نقطہ دار لکیروں پر کاٹیں</small></h1></div>'
            f'<div class="cardgrid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(4,64.5mm)">{"".join(wcard(w, r) for w, r in WORDCARDS)}</div>{F(5)}</section>')


def p6():
    def strip():
        cells = ""
        for s in ("A", "B"):
            for f in FORMS:
                cells += (f'<div style="border:.4mm solid {FCOL[f]};border-radius:2.4mm;padding:.6mm 1mm;background:#fff;text-align:center;min-width:0">'
                          f'<div style="width:15mm;margin:0 auto">{apic(s, f)}</div><div style="font-size:9.4pt;font-weight:700;line-height:1.55;color:#001F3F">{set_sent(s, f)[:-1]}</div></div>')
        return f'<div style="border-bottom:.35mm dashed #8D99A8;padding:1.6mm 0;display:grid;grid-template-columns:repeat(4,1fr);gap:1.6mm;align-content:center;height:100%">{cells}</div>'
    return (f'<section class="page">{bar2("ڈیسک پٹیاں", "Desk strips", "ہر جوڑی کے لیے ایک پٹی کاٹیں۔ بچے اس سے اپنا کام خود جانچتے ہیں")}'
            f'<div style="position:absolute;left:10mm;right:10mm;top:30mm;bottom:14mm;display:grid;grid-template-rows:repeat(4,minmax(0,1fr))">{"".join(strip() for _ in range(4))}</div>{F(6)}</section>')


def tally():
    rows = "".join(f'<tr style="height:7.3mm"><td style="width:8mm;color:var(--grey);font-size:8pt">{ur(i)}</td><td></td>' + "<td></td>" * 5 + '<td></td><td></td><td></td></tr>' for i in range(1, 31))
    return f"""<section class="page">{bar("کلاس ٹریکر", "خروجی جانچ، دن ۱ · لیول ۳ اردو")}
<div class="content" style="top:29mm">
 <div style="display:flex;gap:6mm;font-size:9.5pt;margin-bottom:.4mm"><div>استاد: ______________________</div><div>کلاس: ________________</div><div>تاریخ: ______________</div></div>
 <div class="small" style="margin-bottom:1.4mm">حصہ الف: ہر درست آئٹم (۱ تا ۵) پر ٹک لگائیں اور اسکور لکھیں۔ حالت: ٹ (ٹھیک چل رہا ہے، ۴ یا ۵)، م (مشق چاہیے، ۳)، د (دوبارہ پڑھائیں، ۲ یا کم)۔ حصہ ب: جب بچے سے جملہ سن لیں تو ٹک لگائیں۔</div>
 <table class="t" style="font-size:8.8pt"><tr><th>نمبر</th><th style="width:50mm;text-align:right">بچے کا نام</th>{"".join(f"<th>{ur(i)}</th>" for i in range(1, 6))}<th>اسکور<br>/ ۵</th><th>حالت<br>ٹ / م / د</th><th>حصہ ب</th></tr>{rows}</table>
</div>{F(TOTAL)}</section>"""


def build():
    html = head_a("Level 3 Urdu Day 1 - Prep Pack v1").replace("</style>", EXTRA_CSS + "</style>") + p1() + p2() + p3() + p4() + p5() + p6() + tally() + OVERFLOW_JS
    out = os.path.join(WORK, "prepa.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
