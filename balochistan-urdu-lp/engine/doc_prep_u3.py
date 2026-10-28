"""Level 1 Beginner, Urdu, Day 1 (final planner): Prep Pack (no Rumi logo)."""
from common_u2 import *
tile = ptile   # print-safe: dark letter on a pale tint, readable in plain black and white

TOTAL = 6
EXTRA_CSS = """
.card{border:.35mm dashed #8D99A8;padding:3.5mm;display:flex}
.card .in{flex:1;border:1.4mm solid var(--c);border-radius:5mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:2mm 3mm 3mm;background:#fff}
.cardgrid{position:absolute;left:10mm;right:10mm;top:21mm;height:258mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,86mm);overflow:hidden}
.cardgrid .card{height:86mm;min-height:0;overflow:hidden}
.slim{height:15mm}.slim h1{font-size:13pt}
"""


EN = {"تیاری کا پیکٹ": "Preparation pack", "حروف کا چارٹ": "Letter chart", "استاد کی رہنما شیٹ": "Teacher call sheet", "ڈیسک پٹیاں": "Desk letter strips", "کلاس ٹریکر": "Class tally sheet"}


def bar(title, sub):
    return bar2(title, EN[title], sub)


def F(n):
    return foot(FOOT_PREP, n, TOTAL)


def sounds(seq, sep=" · "):
    return sep.join(f'<b class="sn">{SOUND[l]}</b>' for l in seq)


def p1():
    inside = [("حروف کا چارٹ", "صفحہ ۲", "بچوں کی آنکھ کی سطح پر دیوار پر لگائیں"),
              ("استاد کی رہنما شیٹ", "صفحہ ۳", "ہر آواز کیسے بولیں، تمام فہرستیں اور تمام جوابات"),
              ("تصویر والے حرفی کارڈ (۵)", "صفحہ ۴", "موٹے کاغذ پر ایک طرف پرنٹ کریں۔ نقطہ دار لکیروں پر کاٹیں"),
              ("ڈیسک پٹیاں", "صفحہ ۵", "ہر بچے کے لیے ایک پٹی پرنٹ کریں۔ نقطہ دار لکیروں پر کاٹیں"),
              ("کلاس ٹریکر", f"صفحہ {ur(TOTAL)}", "ہر بچے کی حالت لکھیں: ٹھیک چل رہا ہے، مشق چاہیے یا دوبارہ پڑھائیں")]
    rows = "".join(f'<tr><td style="text-align:right;font-weight:700;padding:.4mm 3mm">{a}</td><td style="width:22mm"><b>{b}</b></td><td style="text-align:right;padding:.4mm 3mm">{c}</td></tr>' for a, b, c in inside)
    return f"""<section class="page">{bar("تیاری کا پیکٹ", "کلاس سے پہلے پرنٹ کرنے، کاٹنے اور جمع کرنے کی ہر چیز")}
<div class="content">
 <div class="box gold" style="display:flex;gap:4mm;align-items:center"><div style="flex:1"><div style="font-size:9pt;font-weight:700;line-height:1.7">لیول ۱ بنیادی · اردو · دن ۱</div>
  <div style="font-size:16pt;font-weight:700;line-height:1.7">نئے حروف: {" · ".join(LETTERS)}</div><div style="font-size:10pt;line-height:1.8">تیاری میں تقریباً ۲۰ منٹ لگیں گے۔ یہ پیکٹ لیسن پلان کے ساتھ رکھیں۔</div></div>
  <div style="width:30mm;border-radius:4mm;overflow:hidden;background:#fff">{scene("teacher_point")}</div></div>

 <div style="font-size:9.5pt;font-weight:700;color:var(--navy);margin:1mm 0 .4mm;line-height:1.8">اس پیکٹ میں کیا ہے</div>
 <table class="t" style="margin-bottom:3.4mm;font-size:9.4pt">{rows}</table>

 <div class="row">
  <div class="box mint"><h2><span class="en">Print and cut</span>پرنٹ کریں اور کاٹیں</h2>
   <div style="font-size:9.8pt;line-height:1.9">☐ حروف کا چارٹ (صفحہ ۲): ۱ کاپی<br>☐ حرفی کارڈ (صفحہ ۴): ۱ سیٹ<br>☐ <b>ڈیسک پٹی: ہر بچے کے لیے ۱</b><br>☐ استاد کی رہنما شیٹ (صفحہ ۳): ۱ کاپی<br>☐ <b>ورک شیٹ: ہر بچے کے لیے ۱</b>، دونوں طرف<br>☐ کلاس ٹریکر (صفحہ {ur(TOTAL)}): ۱ کاپی</div></div>
  <div class="box sky"><h2><span class="en">Gather</span>جمع کریں</h2>
   <div style="font-size:9.8pt;line-height:1.9">☐ چاک اور ڈسٹر<br>☐ ہر بچے کے لیے کاپی کا صفحہ<br>☐ ہر بچے کے لیے پنسل<br>☐ حروف ڈھانپنے کے لیے کاغذ کے ۵ ٹکڑے<br>☐ چارٹ لگانے کے لیے ٹیپ</div></div>
 </div>

 <div class="box cream"><h2><span class="en">Five minutes before class</span>بچوں کے آنے سے ۵ منٹ پہلے</h2>
  <ol style="font-size:9.8pt;line-height:1.85">
   <li><b>حروف کا چارٹ</b> آنکھ کی سطح پر دیوار پر لگائیں۔</li>
   <li>بورڈ پر <b>{" ، ".join(LETTERS)}</b> بڑے لکھیں۔ دلچسپی کے لیے ہر حرف کو کاغذ سے ڈھانپ دیں۔</li>
   <li>پانچ حرفی کارڈ ترتیب سے رکھیں: ا، ب، پ، ت، ٹ، اوپر ا۔</li>
   <li>ڈیسک پٹیاں اور ورک شیٹیں ایسی جگہ رکھیں جہاں ہاتھ پہنچے۔</li>
   <li>رہنما شیٹ ایک بار پڑھیں۔ پانچوں آوازیں بولنے کی مشق کریں: {sounds(LETTERS)}۔ ہر آواز چھوٹی ہو، آخر میں کوئی آواز نہ لگائیں۔</li></ol></div>

 <div class="box grey" style="margin-bottom:0"><b>پرنٹنگ کا مشورہ:</b> اگر کارڈ یا پٹیاں پرنٹ نہ ہو سکیں تو ہر حرف اور اس کی تصویر ہاتھ سے کاغذ پر بنا لیں۔ بچوں کو حروف صاف نظر آنے چاہییں۔ سادہ ڈرائنگ کافی ہے۔</div>
</div>{F(1)}</section>"""


def p2():
    rows = ""
    for l in LETTERS:
        rows += (f'<div style="border:.5mm solid {TILE[l]};border-radius:5mm;padding:2mm 6mm;display:flex;align-items:center;gap:8mm;background:#fff">'
                 f'<div style="flex:none">{tile(l, 40, 36, 46)}</div>'
                 f'<div style="width:30mm;flex:none">{pic(l)}</div>'
                 f'<div><div style="font-size:30pt;font-weight:700;line-height:1.5">{WORD[l]}</div>'
                 f'<div style="font-size:15pt;color:var(--grey);line-height:1.8">آواز: <b class="sn" style="color:var(--navy);font-size:20pt">{SOUND[l]}</b></div></div></div>')
    return f"""<section class="page">{bar("حروف کا چارٹ", "آج کے پانچ حروف، ان کی تصویریں اور آوازیں")}
<div style="position:absolute;left:10mm;right:10mm;top:31mm;bottom:22mm;display:grid;grid-template-rows:repeat(5,minmax(0,1fr));gap:2.4mm">{rows}</div>
<div class="small" style="position:absolute;left:10mm;right:10mm;bottom:14mm;text-align:center">بچوں کی آنکھ کی سطح پر دیوار پر لگائیں۔ حرف کی طرف اشارہ چھڑی سے کریں، انگلی حرف کے اوپر نہ رکھیں۔</div>
{F(2)}</section>"""


def p3():
    tr = "".join(f'<tr><td style="width:16mm">{tile(l, 11, 10, 12)}</td>'
                 f'<td style="text-align:center;font-weight:700"><span class="sn" style="font-size:14pt">{SOUND[l]}</span></td><td style="text-align:right;font-weight:700">{WORD[l]}</td><td style="text-align:right;font-size:8.6pt">{HOW[l]}</td></tr>' for l in LETTERS)
    t2 = " &nbsp; ".join(f'{WORD[l]} ← <b style="font-size:12pt">{l}</b>' for l in T2_PICS)
    ex = ""
    for i, it in enumerate(EXIT):
        opts = " &nbsp; ".join(it["options"]) if it["options"] else "(بچہ لکھے)"
        say = (f'نمبر {NUM_WORD[i]}۔ جو حرف <b class="sn">{SOUND[it["sound"]]}</b> کہتا ہے، اس کے گرد دائرہ لگائیں۔' if it["options"]
              else f'نمبر {NUM_WORD[i]}۔ جو حرف <b class="sn">{SOUND[it["sound"]]}</b> کہتا ہے، اسے لکھیں۔')
        ex += (f'<tr><td style="width:6mm"><b>{ur(i+1)}</b></td><td style="text-align:right;width:24mm">{it["kind"]}</td><td style="text-align:right">{say}</td>'
               f'<td style="width:26mm;font-size:12pt">{opts}</td><td style="width:14mm"><b style="font-size:13pt">{it["answer"]}</b></td></tr>')
    t3 = "<br>".join(f'<b style="font-size:12pt">{tg}:</b> ' + "، ".join(ur(i + 1) for i, o in enumerate(opts) if o == tg) for tg, opts in T3_ROWS)
    return f"""<section class="page">{bar("استاد کی رہنما شیٹ", "سبق کے دوران اسے اپنے پاس رکھیں")}
<div class="content" style="top:29mm">
 <table class="t" style="font-size:9.4pt;margin-bottom:3mm"><tr><th>حرف</th><th>آواز</th><th style="text-align:right">تصویر والا لفظ</th><th style="text-align:right">آواز کیسے بولیں</th></tr>{tr}</table>
 <div class="row" style="gap:3mm">
  <div class="box sky" style="margin-bottom:2.4mm"><h2 style="font-size:10.5pt"><span class="en">We do · Show me</span>ہم سب مل کر: مجھے دکھاؤ (اسی ترتیب میں)</h2>{sounds(SHOW_ME)}
   <div class="small">ہر آواز دو بار بولیں۔ ملتی آوازیں (ب، پ اور ت، ٹ) ساتھ ساتھ نہیں آتیں۔</div></div>
  <div class="box cream" style="margin-bottom:2.4mm"><h2 style="font-size:10.5pt"><span class="en">We do · Write it</span>ہم سب مل کر: لکھیں (اسی ترتیب میں)</h2>{sounds(WRITE_CALLS)}
   <div class="small">آواز بولنے کا ترتیب وار راؤنڈ: {sounds(CHANT_ORDER, " ")}، پھر {sounds(CHANT_MIXED, " ")}۔</div></div>
 </div>
 <div class="row" style="gap:3mm">
  <div class="box mint" style="margin-bottom:2.4mm"><h2 style="font-size:10.5pt"><span class="en">Answers</span>اکیلے: جوابات (ورک شیٹ صفحہ ۱)</h2>
   <div style="font-size:9.4pt;line-height:1.85"><b>۱ ٹریس اور نقل:</b> {" · ".join(T1_LETTERS)}<br><b>۲ تصویر سے پہلا حرف:</b></div>
   <div style="font-size:9.4pt;line-height:1.85">{t2}</div>
   <div style="font-size:9.4pt;line-height:1.85"><b>۳ وہی حرف (دائیں سے گنیں):</b><br>{t3}</div></div>
  <div class="box mint" style="margin-bottom:2.4mm"><h2 style="font-size:10.5pt"><span class="en">Part B</span>حصہ ب: بول کر سنائیں</h2>
   <div style="font-size:9.4pt;line-height:1.85">۴ یا ۵ بچوں سے سنیں، ہر دن مختلف گروپ۔ چارٹ پر اس ترتیب میں اشارہ کریں: {" · ".join(PART_B)}۔ بچہ اس کی <b>آواز</b> بتائے۔ آواز اور نام ایک سوال میں نہ ملائیں۔</div>
   <h2 style="font-size:10.5pt;margin-top:1mm"><span class="en">Tracker</span>ٹریکر (حصہ الف کا اسکور)</h2><div style="font-size:9.4pt;line-height:1.85"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ · <b>مشق چاہیے:</b> ۳ · <b>دوبارہ پڑھائیں:</b> ۲ یا کم</div></div>
 </div>
 <div class="box mint" style="margin-bottom:0"><h2 style="font-size:10.5pt"><span class="en">Exit check · Part A</span>خروجی جانچ، حصہ الف: ہر آئٹم دو بار بولیں</h2>
  <table class="t" style="font-size:9.4pt"><tr><th></th><th style="text-align:right">قسم</th><th style="text-align:right">کیا کہیں</th><th>اختیارات</th><th>جواب</th></tr>{ex}</table></div>
</div>{F(3)}</section>"""


def card(l):
    return (f'<div class="card" style="--c:{TILE[l]}"><div class="in"><div style="flex:none">{tile(l, 40, 26, 33)}</div>'
            f'<div style="width:29mm">{pic(l)}</div><div><div style="text-align:center;font-size:20pt;font-weight:700;line-height:1.5">{WORD[l]}</div>'
            f'<div style="text-align:center;font-size:11pt;color:var(--grey);line-height:1.6;margin-top:1.6mm">آواز <b class="sn" style="font-size:14pt;color:var(--navy)">{SOUND[l]}</b></div></div></div></div>')


def p4():
    note = ('<div class="card" style="--c:#8D99A8"><div class="in" style="border:0;justify-content:center;text-align:center;color:var(--grey);font-size:10pt;line-height:1.9">'
            'کارڈ موٹے کاغذ پر ایک طرف پرنٹ کریں۔<br>نقطہ دار لکیروں پر کاٹیں۔<br>ترتیب: ا، ب، پ، ت، ٹ (اوپر ا)۔<br><br>ملتی آوازوں والے کارڈ (ب، پ اور ت، ٹ) ایک ساتھ نہ دکھائیں۔</div></div>')
    return (f'<section class="page"><div class="bar slim"><div class="day" style="width:10mm;height:10mm;font-size:5.5pt"><b style="font-size:11pt">۱</b></div>'
            f'<h1><span class="en">Picture-letter cards</span>تصویر والے حرفی کارڈ<small>ا · ب · پ · ت · ٹ، نقطہ دار لکیروں پر کاٹیں</small></h1></div>'
            f'<div class="cardgrid">{"".join(card(l) for l in LETTERS)}{note}</div>{F(4)}</section>')


def p5():
    def strip():
        cells = "".join(f'<div style="flex:1;border:.5mm solid {TILE[l]};border-radius:3mm;display:flex;align-items:center;gap:2mm;padding:.6mm 1.6mm;background:#fff">'
                        f'<div style="flex:none">{tile(l, 15, 13, 15)}</div>'
                        f'<div style="width:11mm;flex:none">{pic(l)}</div><span style="font-size:8.6pt;font-weight:700;line-height:1.5">{WORD[l]}</span></div>' for l in LETTERS)
        return f'<div style="border-bottom:.35mm dashed #8D99A8;padding:2mm 0;display:flex;gap:2mm;align-items:center;height:100%">{cells}</div>'
    return (f'<section class="page">{bar("ڈیسک پٹیاں", "ہر بچے کے لیے ایک پٹی کاٹیں۔ بچے اس سے اپنا کام خود جانچتے ہیں")}'
            f'<div style="position:absolute;left:10mm;right:10mm;top:30mm;bottom:14mm;display:grid;grid-template-rows:repeat(8,minmax(0,1fr))">{"".join(strip() for _ in range(8))}</div>{F(5)}</section>')


def tally():
    rows = "".join(f'<tr style="height:7.3mm"><td style="width:8mm;color:var(--grey);font-size:8pt">{ur(i)}</td><td></td>' + "<td></td>" * 5 + '<td></td><td></td><td></td></tr>' for i in range(1, 31))
    return f"""<section class="page">{bar("کلاس ٹریکر", "خروجی جانچ، دن ۱ · لیول ۱ اردو")}
<div class="content" style="top:29mm">
 <div style="display:flex;gap:6mm;font-size:9.5pt;margin-bottom:.4mm"><div>استاد: ______________________</div><div>کلاس: ________________</div><div>تاریخ: ______________</div></div>
 <div class="small" style="margin-bottom:1.4mm">حصہ الف: ہر درست آئٹم (۱ تا ۵) پر ٹک لگائیں اور اسکور لکھیں۔ حالت: ٹ (ٹھیک چل رہا ہے، ۴ یا ۵)، م (مشق چاہیے، ۳)، د (دوبارہ پڑھائیں، ۲ یا کم)۔ حصہ ب: جب بچے سے آواز سن لیں تو ٹک لگائیں۔</div>
 <table class="t" style="font-size:8.8pt"><tr><th>نمبر</th><th style="width:50mm;text-align:right">بچے کا نام</th>{"".join(f"<th>{ur(i)}</th>" for i in range(1, 6))}<th>اسکور<br>/ ۵</th><th>حالت<br>ٹ / م / د</th><th>حصہ ب</th></tr>{rows}</table>
</div>{F(TOTAL)}</section>"""


def build():
    html = head_html2("Level 1 Urdu Day 1 - Prep Pack v2").replace("</style>", EXTRA_CSS + "</style>") + p1() + p2() + p3() + p4() + p5() + tally() + OVERFLOW_JS
    out = os.path.join(WORK, "prepu3.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
