"""Level 2 Intermediate, Urdu, Day 1 (final planner): Prep Pack (print-safe, no Rumi logo)."""
from common_i import *

TOTAL = 6
EXTRA_CSS = """
.wd{display:inline-block;background:#fff;border:.4mm solid #9AA6B5;border-radius:2mm;padding:0 2.4mm;margin:.4mm .6mm;font-weight:700;font-size:11pt;line-height:1.7;color:#001F3F}
.card{border:.35mm dashed #8D99A8;padding:2.4mm;display:flex}
.card .in{flex:1;border:1.2mm solid var(--c);border-radius:4mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:1.6mm 2mm 2.2mm;background:#fff}
.cardgrid{position:absolute;left:10mm;right:10mm;top:21mm;height:259mm;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(4,64.5mm);overflow:hidden}
.cardgrid .card{height:64.5mm;min-height:0;overflow:hidden}
.cs table.t td{line-height:1.45;padding:0 1.4mm}.cs .wd{line-height:1.5;padding:0 1.6mm}.slim{height:15mm}.slim h1{font-size:13pt}
:root{--grey:#1D2025;--teal:#064B38}
.small{color:#1D2025}
.en{color:#064B38;font-weight:700}
.box h2 .en{color:#1D2025;border-color:#1D2025}
.foot{color:#1D2025}
"""

EN = {"تیاری کا پیکٹ": "Preparation pack", "نشانیوں کا چارٹ": "Marks chart", "استاد کی رہنما شیٹ": "Teacher call sheet", "ڈیسک پٹیاں": "Desk strips", "کلاس ٹریکر": "Class tally sheet"}


def bar(title, sub):
    return bar2(title, EN[title], sub)


def F(n):
    return foot(FOOT_PREP, n, TOTAL)


def p1():
    inside = [("نشانیوں کا چارٹ", "صفحہ ۲", "بچوں کی آنکھ کی سطح پر دیوار پر لگائیں"),
              ("استاد کی رہنما شیٹ", "صفحہ ۳", "الفاظ کے ٹکڑے، تمام فہرستیں اور تمام جوابات"),
              ("تصویر والے لفظی کارڈ (۱۲)", "صفحہ ۴", "موٹے کاغذ پر ایک طرف پرنٹ کریں۔ نقطہ دار لکیروں پر کاٹیں"),
              ("ڈیسک پٹیاں", "صفحہ ۵", "ہر بچے کے لیے ایک پٹی پرنٹ کریں۔ نقطہ دار لکیروں پر کاٹیں"),
              ("کلاس ٹریکر", f"صفحہ {ur(TOTAL)}", "ہر بچے کی حالت لکھیں: ٹھیک چل رہا ہے، مشق چاہیے یا دوبارہ پڑھائیں")]
    rows = "".join(f'<tr><td style="text-align:right;font-weight:700;padding:.4mm 3mm">{a}</td><td style="width:22mm"><b>{b}</b></td><td style="text-align:right;padding:.4mm 3mm">{c}</td></tr>' for a, b, c in inside)
    return f"""<section class="page">{bar("تیاری کا پیکٹ", "کلاس سے پہلے پرنٹ کرنے، کاٹنے اور جمع کرنے کی ہر چیز")}
<div class="content">
 <div class="box gold" style="display:flex;gap:4mm;align-items:center"><div style="flex:1"><div style="font-size:9pt;font-weight:700;line-height:1.7">لیول ۲ درمیانہ · اردو · دن ۱</div>
  <div style="font-size:16pt;font-weight:700;line-height:1.7">زبر · زیر · پیش · جزم</div><div style="font-size:10pt;line-height:1.8">تیاری میں تقریباً ۲۰ منٹ لگیں گے۔ یہ پیکٹ لیسن پلان کے ساتھ رکھیں۔</div></div>
  <div style="width:30mm;border-radius:4mm;overflow:hidden;background:#fff">{scene("teacher_point")}</div></div>

 <div style="font-size:9.5pt;font-weight:700;color:var(--navy);margin:1mm 0 .4mm;line-height:1.8">اس پیکٹ میں کیا ہے</div>
 <table class="t" style="margin-bottom:3.4mm;font-size:9.4pt">{rows}</table>

 <div class="row">
  <div class="box mint"><h2><span class="en">Print and cut</span>پرنٹ کریں اور کاٹیں</h2>
   <div style="font-size:9.8pt;line-height:1.9">☐ نشانیوں کا چارٹ (صفحہ ۲): ۱ کاپی<br>☐ لفظی کارڈ (صفحہ ۴): ۱ سیٹ، ۱۲ کارڈ<br>☐ <b>ڈیسک پٹی: ہر بچے کے لیے ۱</b><br>☐ استاد کی رہنما شیٹ (صفحہ ۳): ۱ کاپی<br>☐ <b>ورک شیٹ: ہر بچے کے لیے ۱</b>، دونوں طرف<br>☐ کلاس ٹریکر (صفحہ {ur(TOTAL)}): ۱ کاپی</div></div>
  <div class="box sky"><h2><span class="en">Gather</span>جمع کریں</h2>
   <div style="font-size:9.8pt;line-height:1.9">☐ چاک اور ڈسٹر<br>☐ ہر بچے کے لیے کاپی کا صفحہ<br>☐ ہر بچے کے لیے پنسل<br>☐ چارٹ لگانے کے لیے ٹیپ</div></div>
 </div>

 <div class="box cream"><h2><span class="en">Five minutes before class</span>بچوں کے آنے سے ۵ منٹ پہلے</h2>
  <ol style="font-size:9.8pt;line-height:1.85">
   <li><b>نشانیوں کا چارٹ</b> آنکھ کی سطح پر دیوار پر لگائیں۔</li>
   <li>بورڈ پر بڑا <b>{BASE}</b> لکھیں۔ نشانیاں کلاس میں بچوں کے سامنے لگائیں گے۔</li>
   <li>بارہ لفظی کارڈ ترتیب سے رکھیں: پہلے زبر، پھر زیر، پھر پیش، پھر جزم والے۔</li>
   <li>ڈیسک پٹیاں اور ورک شیٹیں ایسی جگہ رکھیں جہاں ہاتھ پہنچے۔</li>
   <li>رہنما شیٹ ایک بار پڑھیں۔ بارہ الفاظ ٹکڑوں میں بولنے کی مشق کریں۔ جزم والے حرف پر آواز نہ لگائیں۔</li></ol></div>

 <div class="box grey" style="margin-bottom:0"><b>پرنٹنگ کا مشورہ:</b> اگر کارڈ یا پٹیاں پرنٹ نہ ہو سکیں تو ہر لفظ اور اس کی تصویر ہاتھ سے کاغذ پر بنا لیں۔ نشانیاں صاف اور بڑی لکھیں تاکہ بچوں کو نظر آئیں۔</div>
</div>{F(1)}</section>"""


def p2():
    rows = ""
    for m in MARKS:
        words = "".join(f'<div style="text-align:center"><div style="width:20mm;margin:0 auto">{wpic(k)}</div><div style="font-size:16pt;font-weight:700;line-height:1.5">{wd(k)}</div></div>' for k in BLOCK_WORDS[m])
        rows += (f'<div style="border:.5mm solid {MCOL[m]};border-radius:5mm;padding:2mm 6mm;display:flex;align-items:center;gap:6mm;background:#fff">'
                 f'<div style="flex:none">{mtile(m, 34, 32, 40)}</div>'
                 f'<div style="width:44mm;flex:none"><div style="font-size:26pt;font-weight:700;line-height:1.5">{MNAME[m]}</div>'
                 f'<div style="font-size:11pt;line-height:1.7">{MWHERE[m]}</div>'
                 f'<div style="font-size:12pt;line-height:1.7;margin-top:.6mm">{"  ".join(MEX[m])}</div></div>'
                 f'<div style="flex:1;display:flex;gap:4mm;justify-content:space-around">{words}</div></div>')
    return f"""<section class="page">{bar("نشانیوں کا چارٹ", "ایک حرف، چار نشانیاں، چار آوازیں")}
<div style="position:absolute;left:10mm;right:10mm;top:31mm;bottom:22mm;display:grid;grid-template-rows:repeat(4,minmax(0,1fr));gap:2.4mm">{rows}</div>
<div class="small" style="position:absolute;left:10mm;right:10mm;bottom:14mm;text-align:center">بچوں کی آنکھ کی سطح پر دیوار پر لگائیں۔ نشانی کی طرف اشارہ چھڑی سے کریں، انگلی نشانی کے اوپر نہ رکھیں۔</div>
{F(2)}</section>"""


def p3():
    mt = "".join(f'<tr><td style="width:18mm">{mtile(m, 12, 11, 14)}</td><td style="text-align:center;font-weight:700">{MNAME[m]}</td>'
                 f'<td style="text-align:right;font-size:8.8pt">{MWHERE[m]}</td><td style="text-align:right;font-size:8.8pt">{MHOW[m]}</td></tr>' for m in MARKS)
    wt = "".join(f'<tr><td style="font-weight:700;font-size:12pt;text-align:right">{wd(k)}</td><td style="text-align:right">{parts_html(k)}</td><td>{MNAME[W[k][3]]}</td></tr>' for k in W)
    ex = ""
    for i, it in enumerate(EXIT):
        ex += (f'<tr><td style="width:6mm"><b>{ur(i+1)}</b></td><td style="text-align:right;font-weight:700;font-size:11pt">{it["text"]}</td>'
               f'<td style="width:22mm">تصویر {ur(it["options"].index(it["answer"]) + 1)}</td><td style="width:20mm"><b>{wd(it["answer"]) if it["answer"] in W else it["answer"]}</b></td></tr>')
    t1 = " &nbsp; ".join(f'{wd(k)} ← {ur(T1_PICS.index(k) + 1)}' for k in T1)
    t3 = " &nbsp; ".join(f'{wd(k)}: <b>{l}{MSYM[m]}</b>' for k, l, m in T3)
    pb = "<br>".join(f'<b>کارڈ {ur(i+1)}:</b> {" ، ".join(wd(k) for k in card)}' for i, card in enumerate(PART_B))
    return f"""<section class="page">{bar("استاد کی رہنما شیٹ", "سبق کے دوران اسے اپنے پاس رکھیں")}
<div class="content cs" style="top:29mm">
 <table class="t" style="font-size:9.2pt;margin-bottom:2.4mm"><tr><th>نشانی</th><th>نام</th><th style="text-align:right">جگہ</th><th style="text-align:right">آواز کیسے بولیں</th></tr>{mt}</table>
 <div class="row" style="gap:3mm">
  <div style="flex:1.1"><table class="t" style="font-size:9pt;margin-bottom:2.4mm"><tr><th style="text-align:right">لفظ</th><th style="text-align:right">ٹکڑے (آواز آواز کر کے)</th><th>نشانی</th></tr>{wt}</table></div>
  <div style="flex:1">
   <div class="box sky" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">We do · Read together</span>ایک ساتھ پڑھیں (اسی ترتیب میں)</h2><div style="line-height:1.8">{wchips(CHORUS)}</div></div>
   <div class="box cream" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Partner read</span>جوڑی میں</h2><div style="line-height:1.8">{wchips(PAIR_READ)}</div></div>
   <div class="box mint" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Phrases</span>جملے</h2><div style="font-size:11pt;line-height:1.85;font-weight:700">{"<br>".join(PHRASES)}</div></div>
  </div>
 </div>
 <div class="box mint" style="margin-bottom:2mm;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Answers · worksheet page 1</span>اکیلے: جوابات</h2>
  <div style="font-size:9.2pt;line-height:1.85"><b>۱ لفظ سے تصویر (نمبر اوپر سے):</b> {t1}<br><b>۳ پہلے حرف کی آواز:</b> {t3}</div></div>
 <div class="row" style="gap:3mm">
  <div class="box mint" style="margin-bottom:0;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Exit check · Part A</span>حصہ الف: جوابات (ورک شیٹ صفحہ ۲)</h2>
   <table class="t" style="font-size:9pt"><tr><th></th><th style="text-align:right">بچہ پڑھے</th><th>تصویر</th><th>جواب</th></tr>{ex}</table></div>
  <div class="box mint" style="margin-bottom:0;padding:1mm 3mm"><h2 style="font-size:10pt"><span class="en">Part B</span>حصہ ب: بول کر سنائیں</h2>
   <div style="font-size:9.2pt;line-height:1.85">۴ یا ۵ بچوں سے ایک ایک کارڈ پڑھوائیں، ہر دن مختلف بچے۔ نشانی صحیح پڑھی گئی ہو تو ٹک لگائیں۔<br>{pb}</div>
   <h2 style="font-size:10pt;margin-top:1mm"><span class="en">Tracker</span>ٹریکر (حصہ الف کا اسکور)</h2><div style="font-size:9.2pt;line-height:1.85"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ · <b>مشق چاہیے:</b> ۳ · <b>دوبارہ پڑھائیں:</b> ۲ یا کم</div></div>
 </div>
</div>{F(3)}</section>"""


def card(k):
    m = W[k][3]
    return (f'<div class="card" style="--c:{MCOL[m]}"><div class="in"><div style="width:30mm">{wpic(k)}</div>'
            f'<div style="text-align:center;font-size:22pt;font-weight:700;line-height:1.5;color:#001F3F">{wd(k)}</div>'
            f'<div style="text-align:center;font-size:10.5pt;line-height:1.6">{parts_html(k)}</div>'
            f'<div style="font-size:8.6pt;font-weight:700;color:#1D2025;line-height:1.5">{MNAME[m]}</div></div></div>')


def p4():
    order = [k for m in MARKS for k in BLOCK_WORDS[m]]
    return (f'<section class="page"><div class="bar slim"><div class="day" style="width:10mm;height:10mm;font-size:5.5pt"><b style="font-size:11pt">۱</b></div>'
            f'<h1><span class="en">Picture-word cards</span>تصویر والے لفظی کارڈ<small>بارہ کارڈ، نقطہ دار لکیروں پر کاٹیں</small></h1></div>'
            f'<div class="cardgrid">{"".join(card(k) for k in order)}</div>{F(4)}</section>')


def p5():
    cells_keys = sorted(set(T1) | {k for k, _, _ in T3}, key=lambda k: list(W).index(k))

    def strip():
        cells = "".join(f'<div style="flex:1;border:.4mm solid {MCOL[W[k][3]]};border-radius:2.4mm;padding:.4mm 1mm;background:#fff;text-align:center;min-width:0">'
                        f'<div style="width:10.5mm;margin:0 auto">{wpic(k)}</div><div style="font-size:10pt;font-weight:700;line-height:1.5;color:#001F3F">{wd(k)}</div>'
                        f'<div style="font-size:8.6pt;line-height:1.4;color:#1D2025">{W[k][1][0]}</div></div>' for k in cells_keys)
        return f'<div style="border-bottom:.35mm dashed #8D99A8;padding:1.6mm 0;display:flex;gap:1.4mm;align-items:center;height:100%">{cells}</div>'
    return (f'<section class="page">{bar("ڈیسک پٹیاں", "ہر بچے کے لیے ایک پٹی کاٹیں۔ بچے اس سے اپنا کام خود جانچتے ہیں")}'
            f'<div style="position:absolute;left:10mm;right:10mm;top:30mm;bottom:14mm;display:grid;grid-template-rows:repeat(8,minmax(0,1fr))">{"".join(strip() for _ in range(8))}</div>{F(5)}</section>')


def tally():
    rows = "".join(f'<tr style="height:7.3mm"><td style="width:8mm;color:var(--grey);font-size:8pt">{ur(i)}</td><td></td>' + "<td></td>" * 5 + '<td></td><td></td><td></td></tr>' for i in range(1, 31))
    return f"""<section class="page">{bar("کلاس ٹریکر", "خروجی جانچ، دن ۱ · لیول ۲ اردو")}
<div class="content" style="top:29mm">
 <div style="display:flex;gap:6mm;font-size:9.5pt;margin-bottom:.4mm"><div>استاد: ______________________</div><div>کلاس: ________________</div><div>تاریخ: ______________</div></div>
 <div class="small" style="margin-bottom:1.4mm">حصہ الف: ہر درست آئٹم (۱ تا ۵) پر ٹک لگائیں اور اسکور لکھیں۔ حالت: ٹ (ٹھیک چل رہا ہے، ۴ یا ۵)، م (مشق چاہیے، ۳)، د (دوبارہ پڑھائیں، ۲ یا کم)۔ حصہ ب: جب بچے سے کارڈ سن لیں تو ٹک لگائیں۔</div>
 <table class="t" style="font-size:8.8pt"><tr><th>نمبر</th><th style="width:50mm;text-align:right">بچے کا نام</th>{"".join(f"<th>{ur(i)}</th>" for i in range(1, 6))}<th>اسکور<br>/ ۵</th><th>حالت<br>ٹ / م / د</th><th>حصہ ب</th></tr>{rows}</table>
</div>{F(TOTAL)}</section>"""


def build():
    html = head_i("Level 2 Urdu Day 1 - Prep Pack v1").replace("</style>", EXTRA_CSS + "</style>") + p1() + p2() + p3() + p4() + p5() + tally() + OVERFLOW_JS
    out = os.path.join(WORK, "prepi.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
