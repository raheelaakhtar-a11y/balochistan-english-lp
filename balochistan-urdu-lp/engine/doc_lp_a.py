"""Level 3 Advanced, Urdu, Day 1 (28 Oct planner): Lesson Plan. Same approved format as the Beginner and Intermediate Day 1 LPs."""
from common_a import *

TOTAL = 5
F = lambda n: foot(FOOT_LP, n, TOTAL)
CSS3 = r""".enh{font-family:Poppins,Arial,sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;font-size:12.5pt;font-weight:700;color:#001F3F;line-height:1.6}
:root{--grey:#1D2025;--teal:#064B38}
.small{color:#1D2025}
.en{color:#064B38;font-weight:700}
.box h2 .en{color:#1D2025;border-color:#1D2025}
.foot{color:#1D2025}
.bub0:after{display:none}.bub0{margin:.6mm 0}
.p1 .box{padding:4mm 6mm;font-size:12pt;line-height:2.05}.p1 .box h2{font-size:14.5pt;margin-bottom:2mm}
.p1 .small{font-size:10pt}.p1 .chip{font-size:10pt}
.p2 .box{padding:3mm 6mm;margin-bottom:3.4mm;font-size:12pt;line-height:2.1}.p2 .box h2{font-size:14.5pt;margin-bottom:2mm}
.p2 .bub{font-size:13pt}.p2 .small{font-size:10pt}.p2 .board{padding:2.6mm 6mm}
.p4 .box{margin-bottom:5mm}
.fc{flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:2.6mm;padding:.8mm 1.6mm;text-align:center;min-width:0}
.fc .pw{width:17mm;margin:0 auto}
"""


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{ur(i+1)}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


def talk(img, html, w=22):
    return f'<div class="talk"><div class="who" style="width:{w}mm">{scene(img)}</div><div class="bub">{html}</div></div>'


def say(html, size=None):
    st = f' style="font-size:{size}pt;line-height:1.8"' if size else ""
    return f'<div class="bub bub0"{st}><b class="t">کہیں:</b> {html}</div>'


# ---------------- PAGE 1 ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d <= 3:
            st = "background:#FBE08A;color:#001F3F" if d > 1 else "background:#F5B301;color:#001F3F;font-weight:700;outline:.5mm solid #001F3F"
        elif d >= 31:
            st = "background:#BDE5D2;color:#064B38"
        else:
            st = "background:#E6E9EE;color:#3A4A63"
        ribbon += f'<span style="flex:1;height:8.5mm;border-radius:1.2mm;display:flex;align-items:center;justify-content:center;font-size:7.4pt;line-height:1;{st}">{ur(d)}</span>'
    bits = [("آغاز", 5, "#6C7A8D"), ("دلچسپی", 5, "#0B8F6A"), ("میں کر کے دکھاؤں", 20, "#F5B301"), ("ہم سب مل کر", 12, "#F08A3C"),
            ("اکیلے", 8, "#2AA7C7"), ("خروجی جانچ", 10, "#001F3F")]
    assert [m for _, m, _ in bits] == [MINUTES[k] for k in ("warmup", "hook", "i_do", "we_do", "you_do", "exit")]
    tbar = "".join(f'<div style="flex:{m};background:{c};color:{"#001F3F" if c in ("#F5B301","#F08A3C","#2AA7C7") else "#fff"};'
                   f'padding:2mm 1mm;font-size:9.5pt;font-weight:700;text-align:center;line-height:1.8">{n}<br><span style="font-weight:400">{ur(m)} منٹ</span></div>'
                   for n, m, c in bits)
    tiles = "".join(f'<div style="text-align:center"><div>{ftile(f, 20, 16, 14)}</div><div style="font-size:10pt;font-weight:700;line-height:1.5">{FLABEL[f].split()[0]}</div></div>' for f in FORMS)
    return f"""<section class="page p1">
<div style="background:var(--navy);height:44mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:700;line-height:1.3;text-align:center"><div style="font-size:15pt;color:#fff">دن</div><div style="font-size:50pt;line-height:1.25">۱</div><div style="font-size:15pt;color:#fff">از ۳۳</div></div>
 <div style="flex:1;padding-inline-start:5mm;border-inline-start:.5mm solid #2B4A6B">
  <span class="en" style="color:var(--gold)">Day 1 of 33 · Teach and model</span>
  <div style="font-size:16pt;font-weight:700;line-height:1.7">لیول ۳ ایڈوانس · اردو</div>
  <div style="font-size:9.5pt;color:#C9D6E6;line-height:1.7">بلوچستان ونٹر پروگرام · درست سطح پر تدریس</div>
  <div style="margin-top:1.4mm;display:flex;gap:2mm"><span class="pill" style="font-size:9.5pt">۶۰ منٹ</span><span class="pill" style="font-size:9.5pt;background:var(--gold);color:var(--navy)">جملوں میں ملاپ</span></div>
 </div>
 <div style="width:36mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("pair_book")}</div>
</div>
<div class="content" style="top:47mm">
 <div style="display:flex;gap:.8mm;margin-bottom:.4mm">{ribbon}</div>
 <div class="small" style="margin-bottom:2mm">۳۳ دن۔ دن ۱ تا ۳ (سنہری): جملوں میں ایک اور کئی، لڑکا اور لڑکی کا ملاپ۔ دن ۴ سے مخالف اور ہم معنی الفاظ۔ دن ۳۱ تا ۳۳ (سبز): آخری دہرائی۔</div>

 <div class="box gold" style="display:flex;gap:4mm;align-items:center;padding:4mm 6mm;margin-bottom:5mm">
  <div style="display:flex;gap:2.4mm">{tiles}</div>
  <div><span class="en" style="color:var(--navy)">Today's four forms</span>
  <div style="font-size:14pt;font-weight:700;line-height:1.8">ایک جملہ، چار شکلیں</div></div>
 </div>

 <div class="box sky" style="margin-bottom:5mm"><h2><span class="en">Learning outcomes</span>آج کے سیکھنے کے مقاصد</h2>
  <p style="margin-bottom:.4mm"><span class="chip">U-A-08</span> <b>جملے میں ایک یا کئی، لڑکا یا لڑکی کے مطابق درست لفظ استعمال کرنا</b></p>
  <p style="margin-bottom:.4mm"><span class="chip">U-A-10</span> <b>جملے میں نام، کیسا اور کام والے لفظ پہچاننا</b></p>
  <p class="small" style="margin:0">دن ۱ تا ۳۔ اس سے پہلے: <span class="chip">U-I-11</span> مذکر اور مونث کی درست شکل بھرنا۔</p>
 </div>

 <div class="box" style="margin-bottom:5mm;background:#E3F4EC;border:.7mm solid #0B8F6A;color:#001F3F"><h2 style="color:#001F3F"><span class="en">Today's goal</span>آج کا ہدف</h2><div style="font-size:15pt;font-weight:700;line-height:2;color:#001F3F">جملے میں نام بدلیں تو باقی سب لفظ ساتھ بدلیں اور درست جملہ بولیں۔</div></div>

 <div style="margin-bottom:5mm"><span class="en" style="margin-inline-end:3mm">The 60 minutes</span><span style="font-size:9.5pt;font-weight:700;color:var(--navy)">وقت کی تقسیم (۶۰ منٹ)</span>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden;margin-top:.6mm">{tbar}</div></div>

 <div class="box mint" style="margin-bottom:0"><h2><span class="en">To prepare</span>تیاری (تقریباً ۲۰ منٹ)</h2>
  <div style="columns:2;column-gap:6mm;font-size:11.5pt;line-height:2.1">
   <div>☐ جملہ بدلنے کا چارٹ دیوار پر لگائیں</div><div>☐ آٹھ تصویر والے کارڈ کاٹیں</div>
   <div>☐ بارہ لفظی کارڈ کاٹیں</div><div>☐ ہر جوڑی کے لیے ایک ڈیسک پٹی کاٹیں</div>
   <div>☐ ورک شیٹ: ہر بچے کے لیے ایک، ۳ صفحے</div><div>☐ استاد کی رہنما شیٹ اپنے پاس رکھیں</div>
   <div>☐ چاک اور ڈسٹر</div><div>☐ ہر بچے کے لیے کاپی اور پنسل</div>
  </div></div>
</div>
{F(1)}</section>"""


# ---------------- PAGE 2 ----------------
def page2():
    ws = " ، ".join(f"<b>{w}</b>" for w, _ in WARM)
    gest = " · ".join(f"<b>{ROLE[r]}</b> ({ROLE_FORMAL[r]}): {GESTURE[r]}" for r in ("n", "a", "v"))
    h = [hook_pair(i) for i in range(3)]
    board_sents = "<br>".join(f"<b style='color:#FFD966'>{FLABEL[f].split()[0]}</b> &nbsp;{set_sent('A', f)}" for f in FORMS)
    return f"""<section class="page p2">
{bar2("کلاس کا آغاز", "Start the lesson", "آغاز اور دلچسپی", "۱۰ منٹ")}
<div class="content">
 <div class="box grey"><h2><span class="en">Warm-up</span>آغاز: نام، کیسا، کام <span class="t">۵ منٹ</span></h2>
  <div style="margin-bottom:1.2mm"><span class="do">۱۔ بچوں کو سلام کریں (۱ منٹ)۔</span>
   {talk("teacher_point", "السلام علیکم بچو! آج ہم جملے کے لفظوں کو ایک دوسرے کے ساتھ ملانا سیکھیں گے۔", 20)}</div>
  <div><span class="do">۲۔ لفظ سنیں، اشارہ کریں (۴ منٹ)۔</span> پہلے تین اشارے بتائیں: {gest}۔ پھر ایک ایک لفظ بولیں اور بچے اشارہ کریں: {ws}۔</div></div>

 <div class="box sky"><h2><span class="en">Hook</span>دلچسپی: ایک سے کئی <span class="t">۵ منٹ</span></h2>
  <ol>
   <li><span class="do">منظر بنائیں (۱ منٹ)۔</span> ایک لڑکے کی تصویر دکھائیں۔
    {say("چھوٹا لڑکا پڑھتا ہے۔ اب تین لڑکے آ گئے! جملہ کیسے بدلے گا؟")}</li>
   <li><span class="do">جادو بدلاؤ (۲ منٹ)۔</span> تین لڑکوں کی تصویر دکھائیں اور جملہ بولیں: <b>{set_sent("A", "mp")}</b> پوچھیں: کتنے لفظ بدلے؟ جواب: چاروں! آخری آواز سنیں: ے ے ے ہیں۔</li>
   <li><span class="do">تم بتاؤ (۲ منٹ)۔</span> جملہ بولیں، بچے بدل کر بولیں۔
    {say("اب آپ بدلیں!")}<b>{h[0][0]}</b> ← {h[0][1]}<br><b>{h[1][0]}</b> ← {h[1][1]}<br><b>{h[2][0]}</b> ← {h[2][1]}</li>
  </ol></div>

 <div class="board"><h3>Write on the board &nbsp;·&nbsp; بورڈ پر لکھیں</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.5"><div style="font-size:8.8pt;color:#fff;line-height:1.8">ایک جملہ، چار شکلیں</div>
    <div style="font-size:14pt;line-height:1.95">{board_sents}</div></div>
   <div style="flex:1;border-inline:.4mm dashed #7E9A8F;padding:0 4mm">
    <div style="font-size:8.8pt;color:#fff;line-height:1.8">تین قسم کے لفظ</div>
    <div style="font-size:12pt;line-height:1.95">{"<br>".join(f"<b style='color:#FFD966'>{ROLE[r]}</b> &nbsp;({ROLE_FORMAL[r]})" for r in ("n", "a", "v"))}</div></div>
   <div style="flex:.9;font-size:10.2pt;line-height:1.85"><div style="font-size:8.8pt;color:#fff">ہمارے چار کام</div>
    <b style="color:#FFD966">۱</b> جملہ بولیں<br><b style="color:#FFD966">۲</b> لفظ پہچانیں<br><b style="color:#FFD966">۳</b> ملاپ دیکھیں<br><b style="color:#FFD966">۴</b> دوسرا جملہ</div>
  </div></div>
</div>
{F(2)}</section>"""


# ---------------- PAGE 3 ----------------
ENDING = {"ms": "ا ا ا", "mp": "ے ے ے", "fs": "ی ی ی", "fp": "ی ی ی"}


def form_row(i, f):
    cards = "".join(f'<div class="fc" style="display:flex;align-items:center;gap:2mm;padding:.8mm 2mm"><div style="width:14mm;flex:none">{apic(s, f)}</div><div style="flex:1;line-height:1.5;text-align:center">{chips(words(SETS[s]["adj"], SETS[s]["noun"][f[0]], SETS[s]["verb"], f), 9.6)}</div></div>' for s in ("A", "B"))
    return (f'<div style="border:.4mm solid var(--line);border-radius:3mm;padding:.8mm 2.4mm 1.2mm;margin-bottom:1.6mm;background:#fff">'
            f'<div style="display:flex;gap:2.6mm;align-items:center;margin-bottom:.8mm">'
            f'<div style="width:12mm;flex:none;text-align:center"><span class="num" style="width:6.4mm;height:6.4mm;font-size:10pt">{ur(i)}</span>'
            f'<div class="small" style="line-height:1.5">۵ منٹ</div></div>'
            f'<div style="flex:none;text-align:center">{ftile(f, 24, 13, 15)}</div>'
            f'<div style="flex:1;min-width:0;font-size:9.4pt;line-height:1.7"><div style="font-size:13pt;font-weight:700;line-height:1.5">{FLABEL[f]} <span class="small" style="font-weight:400">({FTERM[f]})</span></div>'
            f'<div>{FRULE[f]} <b>آخری آواز:</b> <b style="font-size:12pt">{ENDING[f]}</b></div></div></div>'
            f'<div style="display:flex;gap:2.4mm">{cards}</div></div>')


def page3():
    rows = "".join(form_row(i + 1, f) for i, f in enumerate(FORMS))
    blocks = [("جملہ بولیں", "۱ منٹ", "تصویر دکھائیں۔ جملہ آہستہ بولیں۔ بچے دہرائیں۔"),
              ("لفظ کی قسم", "۱ منٹ", "نام، کیسا اور کام والے لفظ پر اشارہ کریں۔"),
              ("ملاپ دیکھیں", "۲ منٹ", "سب لفظوں کی آخری آواز سنائیں اور ہے یا ہیں بتائیں۔"),
              ("دوسرا جملہ", "۱ منٹ", "جانور والی تصویر اور جملہ۔ وہی ملاپ دیکھیں۔")]
    assert sum(int(t.split()[0].translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))) for _, t, _ in blocks) == 5
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:.8mm 2.4mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm"><span class="n2" style="width:6mm;height:6mm;font-size:9.5pt">{ur(i+1)}</span><b style="font-size:10pt">{t}</b><span class="small" style="margin-inline-start:auto">{mn}</span></div><div style="font-size:8.8pt;line-height:1.75">{d}</div></div>' for i, (t, mn, d) in enumerate(blocks))
    ex = set_words("A", "fp")
    return f"""<section class="page">
{bar2("میں کر کے دکھاؤں", "I do · teach the four forms", "چار شکلیں، ہر شکل کے لیے چار کام", "۲۰ منٹ")}
<div class="content">
 <div class="box sky" style="padding:1.6mm 4mm"><h2 style="margin-bottom:.4mm"><span class="en">Four actions</span>ہر شکل کے لیے یہی ۴ کام <span class="t">ہر شکل ۵ منٹ</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small">ایک لڑکا سے شروع کریں۔ پھر کئی لڑکے، ایک لڑکی، کئی لڑکیاں۔ ہر لفظ کے نیچے لکھا نام، کیسا یا کام بچوں کو لفظ کی قسم یاد دلاتا ہے۔</div></div>
 {rows}
 <div class="box mint" style="margin:1.6mm 0 0"><h2 style="margin-bottom:.4mm"><span class="en">Worked example · Watch for</span>مثال: {set_sent("A", "fp")[:-1]} اور خیال رکھیں</h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.45">{talk("teacher_point", f'<b class="t">کہیں:</b> یہاں کئی لڑکیاں ہیں۔ لڑکی ← لڑکیاں۔ کیسا؟ {ex[0]}۔ کام؟ {ex[2]}۔ کئی ہیں، اس لیے آخر میں ہیں۔ پورا جملہ: {set_sent("A", "fp")}', 20)}</div>
   <div style="flex:1"><ul style="font-size:8.9pt;line-height:1.75;margin:0">
    <li>کئی لڑکیاں ہوں تو «{ex[0]}» اور «{ex[2]}» نہیں بدلتے۔ صرف نام اور ہیں بدلتے ہیں۔</li>
    <li>لڑکی کے ساتھ «پڑھتا» نہیں آتا۔ لڑکا ← پڑھتا، لڑکی ← پڑھتی۔</li>
    <li>آخری آواز ملائیں: ا ا ا، ے ے ے، ی ی ی۔</li></ul></div>
  </div></div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4 ----------------
def page4():
    a, n, v = WE1_FRAME
    base = "<b>" + sent(a, n, v, "ms")[:-1] + "</b>"
    nouns = " · ".join(f"<b>{we1_noun(f)}</b>" for f in WE1_CALLS)
    wrong = "<br>".join(f"{ur(i+1)}۔ <b>{w}</b>" for i, (w, _) in enumerate(WE3))
    return f"""<section class="page p4">
{bar2("ہم سب مل کر", "We do · practise together", "پوری کلاس جملے بدلتی ہے", "۱۲ منٹ")}
<div class="content">
 <div class="box mint"><h2><span class="enh">1 · Change the name card</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["بورڈ پر چار لفظی کارڈ رکھیں اور پوری کلاس پڑھے: " + base,
          "<b>نام</b> والا کارڈ بدلیں، جیسے «لڑکیاں»۔ باقی کارڈ نہ بدلیں۔",
          "بچے سوچیں: کون سے لفظ بدلیں گے؟ پھر پورا جملہ بولیں۔ ہر بار جواب رہنما شیٹ سے جانچیں۔"])}</div>
   <div style="flex:1.1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">نام کارڈ، اسی ترتیب میں</div>
    <div style="font-size:12.5pt;line-height:1.9">{nouns}</div></div></div></div>

 <div class="box sky"><h2><span class="enh">2 · Match with a partner</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["بچے جوڑی میں بیٹھیں۔ ڈیسک پٹی دونوں کے بیچ رکھیں۔",
          "ایک بچہ پٹی کی ایک تصویر پر انگلی رکھے۔ دوسرا جملہ بولے۔",
          "پہلا بچہ پٹی پر لکھا جملہ پڑھ کر جانچے۔ پھر باری بدلیں۔"])}
    <div style="margin-top:1.4mm">{talk("teacher_point", '<b class="t">کہیں:</b> ساتھی کو تصویر دکھائیں اور جملہ سنیں!', 18)}</div></div>
   <div style="flex:1.1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">پٹی پر آٹھ تصویریں</div>
    <div style="line-height:1.9;font-size:11pt">{" · ".join(f"<b>{FLABEL[f]}</b>" for f in FORMS)}<br><span class="small">ہر شکل کی دو تصویریں: بچے اور جانور۔</span></div></div>
  </div></div>

 <div class="box cream"><h2><span class="enh">3 · Fix the sentence</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["بورڈ پر ایک غلط جملہ لکھیں اور پڑھیں۔",
          "بچے «غلط!» کہیں اور بتائیں کون سا لفظ غلط ہے۔",
          "بچے درست لفظ بتائیں۔ پھر پورا درست جملہ ایک ساتھ پڑھیں۔"])}
    <div style="margin-top:1.4mm">{say("غلط! کون سا لفظ بدلنا ہے؟")}</div></div>
   <div style="flex:1.1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">چار غلط جملے</div>
    <div style="font-size:11.5pt;line-height:1.95">{wrong}</div></div></div></div>

 <div class="box" style="position:absolute;left:0;right:0;bottom:0;margin:0;background:#fff;border:.7mm solid #001F3F"><div style="display:flex;gap:5mm">
  <div style="flex:1.1"><h2><span class="en">Check before moving on</span>آگے بڑھنے سے پہلے جانچ</h2><div style="line-height:1.85">۴ یا ۵ بچوں سے سنیں: آپ نام کارڈ بدلیں، بچہ پورا جملہ درست بولے۔<br><b style="color:#001F3F;text-decoration:underline">زیادہ تر درست؟</b> آگے بڑھیں۔ <b style="color:#001F3F;text-decoration:underline">زیادہ تر غلط؟</b> ۲ منٹ آخری آواز کا ملاپ دوبارہ کریں۔</div></div>
  <div style="flex:1;border-inline-start:.4mm solid #001F3F;padding-inline-start:5mm"><h2><span class="en">While you walk around</span>کلاس میں گھومتے ہوئے</h2><ul style="line-height:1.85;margin:0"><li>آخری آوازیں آپس میں ملتی ہیں؟</li><li>«ہے» اور «ہیں» صحیح ہیں؟</li><li>کئی لڑکیاں کے ساتھ «پڑھتی» ہے؟</li><li>ہر بار مختلف بچے سنیں: ۴ یا ۵، سب نہیں۔</li></ul></div>
 </div></div>
</div>
{F(4)}</section>"""


# ---------------- PAGE 5 ----------------
def page5():
    t1 = '<div style="columns:2;column-gap:4mm;font-size:9.6pt;line-height:1.75">' + "".join(f"<div><b>{set_sent(*it)[:-1]}</b> ← {ur(T1_PICS.index(it) + 1)}</div>" for it in T1_ITEMS) + "</div>"
    t2 = " &nbsp; ".join(f"{ur(i+1)}: <b>{t['answer']}</b>" for i, t in enumerate(T2))
    t3 = "<br>".join(f"{ur(i+1)}۔ دائرہ: <b>{words(*a)[1]}</b> · لکیر: <b>{words(*a)[0]}</b> · ڈبہ: <b>{words(*a)[2]}</b>" for i, a in enumerate(T3))
    key = ""
    for i, it in enumerate(EXIT):
        key += (f'<tr><td><b>{ur(i+1)}</b></td><td><b style="font-size:11pt;line-height:1.5">{it["answer"]}</b></td><td>{["پہلا", "دوسرا", "تیسرا"][it["pos"]]} جملہ</td></tr>')
    return f"""<section class="page">
{bar2("اکیلے اور خروجی جانچ", "You do · exit check", "اکیلے (۸ منٹ)، پھر خروجی جانچ (۱۰ منٹ)", "۱۸ منٹ")}
<div class="content">
 <div class="box mint" style="padding-bottom:1.4mm"><h2 style="margin-bottom:0"><span class="en">Your turn</span>اکیلے <span class="t">۸ منٹ</span></h2>
  <p class="small" style="margin:0 0 .8mm">ورک شیٹ صفحہ ۱۔ ہر کام کی پہلی لائن سب مل کر کریں۔ بچے ڈیسک پٹی سے خود جانچیں اور ورک شیٹ جمع کروائیں۔</p>
  <table class="ans"><tr><th style="width:42mm">کام</th><th style="width:16mm">ورک شیٹ</th><th style="width:14mm">وقت</th><th>جوابات</th></tr>
   <tr><td><b>۱</b> جملہ پڑھیں اور تصویر سے ملائیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td><span class="small" style="color:var(--ink)">تصویر نمبر اوپر سے:</span><br><span style="font-size:10pt">{t1}</span></td></tr>
   <tr><td><b>۲</b> درست لفظ پر دائرہ لگائیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td>{t2}</td></tr>
   <tr><td><b>۳</b> نام، کیسا، کام پہچانیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۲ منٹ</td><td>{t3}</td></tr>
  </table></div>

 <div class="box sky" style="padding-bottom:3mm"><h2><span class="en">Exit check</span>خروجی جانچ <span class="t">۱۰ منٹ</span></h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:3mm;padding:1.4mm 4mm">
    <div style="font-weight:700;font-size:11pt;line-height:1.8"><span class="n2" style="margin-inline-end:2mm">الف</span>بچوں کا کام <span class="small">· ۶ منٹ</span></div>
    <div style="line-height:1.9"><b>ورک شیٹ صفحہ ۲:</b> “درست جملے پر دائرہ لگائیں”۔ ہر آئٹم میں تین جملے ہیں۔ بچے خاموشی سے پڑھیں اور درست جملے کے گرد دائرہ لگائیں۔</div></div>
   <div style="flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:3mm;padding:1.4mm 4mm">
    <div style="font-weight:700;font-size:11pt;line-height:1.8"><span class="n2" style="margin-inline-end:2mm">ب</span>استاد کا کام <span class="small">· ۴ منٹ</span></div>
    <div style="line-height:1.9">۴ یا ۵ بچوں کو ایک ایک کارڈ دیں۔ آپ جملہ بولیں، بچہ اسے ایک سے کئی یا کئی سے ایک بدل کر بولے۔ ہر دن مختلف بچے۔</div></div>
  </div>
  <div style="margin-top:2.4mm"><table class="ans" style="font-size:9.4pt;line-height:1.5"><tr><th style="width:9mm;padding:0 1mm">آئٹم</th><th style="padding:0 1mm">درست جملہ</th><th style="width:26mm;padding:0 1mm">جگہ</th></tr>{key}</table></div>
  <div class="small" style="margin-top:1.2mm"><b>حصہ ب:</b> تین کارڈ اور ان کے جوابات استاد کی رہنما شیٹ (صفحہ ۳) میں ہیں۔</div>
 </div>

 <div class="box grey" style="margin-bottom:1.4mm"><b><span class="en" style="margin-inline-end:3mm">At home · optional</span>گھر پر (اختیاری):</b> ورک شیٹ کا صفحہ ۳ گھر والوں کے ساتھ کھیلیں۔ اگلے دن بچوں کے بنائے جملے سنیں۔</div>

 <div class="box" style="position:absolute;left:0;right:0;bottom:0;margin:0;background:#fff;border:.7mm solid #001F3F;padding:2mm 5mm"><h2 style="margin-bottom:.6mm"><span class="en">Score and decide</span>نتیجہ دیکھ کر فیصلہ کریں</h2>
  <div style="display:flex;gap:4mm;font-size:10pt;line-height:1.8">
   <div style="flex:1"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ درست۔</div>
   <div style="flex:1.3"><b>مشق چاہیے:</b> ۳ درست۔ دن ۲ پر ان بچوں کے ساتھ جملے دوبارہ بدلیں۔</div>
   <div style="flex:1.3"><b>دوبارہ پڑھائیں:</b> ۲ یا کم درست۔ جس شکل میں غلطی ہوئی، اس کے ۴ کام چھوٹے گروپ میں دہرائیں۔</div></div>
  <div class="small">ہر بچے کی حالت کلاس ٹریکر پر لکھیں۔ نمبر بلند آواز میں نہ بتائیں۔</div></div>
</div>
{F(5)}</section>"""


def build():
    html = head_a("Level 3 Urdu Day 1 - Lesson Plan v1").replace("</style>", CSS3 + "</style>") + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS
    out = os.path.join(WORK, "lpa.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
