"""Level 1 Beginner, Urdu, Day 1 (final planner): Lesson Plan v2.
v2 = English section tags, stroke-order diagrams, larger speech lines in bubbles with characters, fewer boxes, one consistent minutes check."""
from common_u2 import *

TOTAL = 5
F = lambda n: foot(FOOT_LP, n, TOTAL)


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{ur(i+1)}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


def sounds(seq, sep=" · "):
    return sep.join(f'<b class="sn">{SOUND[l]}</b>' for l in seq)


def talk(img, html, w=22):
    return f'<div class="talk"><div class="who" style="width:{w}mm">{scene(img)}</div><div class="bub">{html}</div></div>'


# ---------------- PAGE 1 ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d == 1:
            st = "background:#F5B301;color:#001F3F;font-weight:700;outline:.5mm solid #001F3F"
        elif d <= 7:
            st = "background:#FBE08A;color:#001F3F"
        elif d <= 9:
            st = "background:#E9EEF6;color:#3A4A63"
        elif d >= 31:
            st = "background:#BDE5D2;color:#064B38"
        else:
            st = "background:#E6E9EE;color:#7A8594"
        ribbon += f'<span style="flex:1;height:7mm;border-radius:1.2mm;display:flex;align-items:center;justify-content:center;font-size:6.6pt;line-height:1;{st}">{ur(d)}</span>'
    bits = [("آغاز", 5, "#6C7A8D"), ("دلچسپی", 5, "#0B8F6A"), ("میں کر کے دکھاؤں", 20, "#F5B301"), ("ہم سب مل کر", 12, "#F08A3C"),
            ("اکیلے", 8, "#2AA7C7"), ("خروجی جانچ", 10, "#001F3F")]
    assert [m for _, m, _ in bits] == [MINUTES[k] for k in ("warmup", "hook", "i_do", "we_do", "you_do", "exit")]
    tbar = "".join(f'<div style="flex:{m};background:{c};color:{"#001F3F" if c in ("#F5B301","#F08A3C","#2AA7C7") else "#fff"};'
                   f'padding:.6mm 1mm;font-size:8pt;font-weight:700;text-align:center;line-height:1.6">{n}<br><span style="font-weight:400">{ur(m)} منٹ</span></div>'
                   for n, m, c in bits)
    return f"""<section class="page">
<div style="background:var(--navy);height:44mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:700;line-height:1.3;text-align:center"><div style="font-size:15pt;color:#fff">دن</div><div style="font-size:50pt;line-height:1.25">۱</div><div style="font-size:15pt;color:#fff">از ۳۳</div></div>
 <div style="flex:1;padding-inline-start:5mm;border-inline-start:.5mm solid #2B4A6B">
  <span class="en" style="color:var(--gold)">Day 1 of 33 · Teach new letters</span>
  <div style="font-size:16pt;font-weight:700;line-height:1.7">لیول ۱ بنیادی · اردو</div>
  <div style="font-size:9.5pt;color:#C9D6E6;line-height:1.7">بلوچستان ونٹر پروگرام · درست سطح پر تدریس</div>
  <div style="margin-top:1.4mm;display:flex;gap:2mm"><span class="pill" style="font-size:9.5pt">۶۰ منٹ</span><span class="pill" style="font-size:9.5pt;background:var(--gold);color:var(--navy)">نئے حروف سکھائیں</span></div>
 </div>
 <div style="width:36mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("kids_wave")}</div>
</div>
<div class="content" style="top:47mm">
 <div style="display:flex;gap:.8mm;margin-bottom:.4mm">{ribbon}</div>
 <div class="small" style="margin-bottom:2mm">۳۳ دن۔ دن ۱ تا ۷ (سنہری) میں نئے حروف، دن ۸ اور ۹ میں دہرائی، دن ۳۱ تا ۳۳ (سبز) میں آخری دہرائی۔</div>

 <div class="box gold" style="display:flex;gap:4mm;align-items:center;padding:2.4mm 4.2mm">
  <div style="display:flex;gap:1.4mm">{"".join(tile(l, 14, 17, 22) for l in LETTERS)}</div>
  <div><span class="en" style="color:var(--navy)">Today's letters</span>
  <div style="font-size:16pt;font-weight:700;line-height:1.5">{" · ".join(LETTERS)}</div>
  <div style="font-size:10pt;line-height:1.5">آواز، تصویر والا لفظ اور لکھنا</div></div>
 </div>

 <div class="row">
  <div class="box sky"><h2><span class="en">Learning outcomes</span>آج کے سیکھنے کے مقاصد</h2>
   <p style="margin-bottom:.4mm"><span class="chip">U-B-01</span> <b>اردو حروف تہجی کے حروف کو پہچاننا اور ان کا نام لینا</b></p>
   <p style="margin-bottom:.4mm"><span class="chip">U-B-02</span> <b>حرف کی آواز اور بولے گئے لفظ کی پہلی آواز بتانا</b></p>
   <p style="margin-bottom:.4mm"><span class="chip">U-B-03</span> <b>حرف بولا جائے تو اسے لکھنا</b></p>
   <p class="small" style="margin:0">دن ۱ تا ۹۔ ساتھ میں: <span class="chip">U-B-04</span> دائیں سے بائیں ٹریس اور نقل کرنا۔</p>
  </div>
  <div class="box mint"><h2><span class="en">By the end of today</span>بچے یہ کر سکیں گے</h2>
   <ul><li>ا، ب، پ، ت، ٹ کو دیکھ کر پہچانیں</li><li>ہر حرف کی آواز اور اس کا تصویر والا لفظ بتائیں</li><li>آواز سن کر وہ حرف لکھیں</li><li>پانچوں حروف کو ٹریس کریں اور نقل کریں</li></ul>
  </div>
 </div>

 <div class="box cream" style="margin-bottom:2.4mm"><h2><span class="en">Five letters only</span>آج صرف پانچ حروف</h2>
  <p style="margin:0">صرف <b>{" ، ".join(LETTERS)}</b> پڑھائیں۔ تصویر والے الفاظ: <b>{" ، ".join(WORD[l] for l in LETTERS)}</b>۔ حروف آواز سے پڑھائے جاتے ہیں۔ ب اور پ، ت اور ٹ کی آوازیں ملتی ہیں: انہیں ایک ساتھ نہ پوچھیں۔</p></div>

 <div style="margin-bottom:2.4mm"><span class="en" style="margin-inline-end:3mm">The 60 minutes</span><span style="font-size:9.5pt;font-weight:700;color:var(--navy)">وقت کی تقسیم (۶۰ منٹ)</span>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden;margin-top:.6mm">{tbar}</div></div>

 <div class="box grey" style="margin-bottom:2.4mm"><h2><span class="en">Book and documents</span>کتاب اور دستاویز</h2>
  <div style="display:flex;gap:6mm"><div style="flex:1"><b>اردو جماعت اول</b> (بلوچستان ٹیکسٹ بک بورڈ)، <b>سبق ۱، صفحہ ۱</b>: آج صرف ا، ب، پ، ت، ٹ۔ آ کو آج چھوڑ دیں۔</div>
  <div style="flex:1"><b>تین دستاویز:</b> ۱ لیسن پلان (یہی) · ۲ تیاری کا پیکٹ · ۳ طالب علم کی ورک شیٹ</div></div></div>

 <div class="box mint" style="margin-bottom:0"><h2><span class="en">To prepare</span>تیاری (تقریباً ۲۰ منٹ)</h2>
  <div style="columns:2;column-gap:6mm;font-size:9.8pt;line-height:1.85">
   <div>☐ حروف کا چارٹ دیوار پر لگائیں</div><div>☐ پانچ تصویر والے حرفی کارڈ کاٹیں</div>
   <div>☐ ہر بچے کے لیے ایک ڈیسک پٹی کاٹیں</div><div>☐ استاد کی رہنما شیٹ اپنے پاس رکھیں</div>
   <div>☐ ورک شیٹ: ہر بچے کے لیے ایک، دونوں طرف</div><div>☐ چاک، ڈسٹر، ہر بچے کے لیے تختی اور پنسل</div>
  </div></div>
</div>
{F(1)}</section>"""


# ---------------- PAGE 2 ----------------
def page2():
    paper = "".join(tile(l, 13, 15, 20) + '<span style="width:2mm;display:inline-block"></span>' for l in LETTERS)
    return f"""<section class="page">
{bar2("کلاس کا آغاز", "Start the lesson", "آغاز اور دلچسپی", "۱۰ منٹ")}
<div class="content">
 <div class="box grey"><h2><span class="en">Warm-up</span>آغاز: تصویر والے الفاظ بولیں <span class="t">۵ منٹ</span></h2>
  <div style="margin-bottom:1.2mm"><span class="do">۱۔ بچوں کو سلام کریں (۱ منٹ)۔</span>
   {talk("teacher_point", "السلام علیکم بچو! آج ہم پانچ نئے حروف سے ملیں گے۔", 20)}</div>
  <div><span class="do">۲۔ پانچ الفاظ بولیں (۴ منٹ)۔</span> حروف کے چارٹ پر ہر تصویر کی طرف اشارہ کریں: <b>انار، بٹن، پری، توا، ٹرک</b>۔ لفظ بولیں۔ بچے دو بار دہرائیں۔ پھر کوئی لفظ بولیں اور بچے چارٹ پر اس کی تصویر دکھائیں۔</div></div>

 <div class="box sky"><h2><span class="en">Hook</span>دلچسپی: پانچ حرفی دوست <span class="t">۵ منٹ</span></h2>
  <div style="margin:.4mm 0 1.6mm;padding:1.4mm 3.4mm;background:#fff;border-radius:3mm;border:.3mm solid #C7D4EC;display:flex;align-items:center;gap:3mm"><div style="display:flex">{paper}</div><div class="small" style="flex:1">کلاس سے پہلے ا، ب، پ، ت، ٹ بورڈ پر بڑے لکھیں اور ہر حرف کو کاغذ سے ڈھانپ دیں۔</div></div>
  <ol>
   <li><span class="do">منظر بنائیں (۱ منٹ)۔</span>
    <div class="say">پانچ نئے دوست آج ہمارے سکول آئے ہیں۔ یہ حروف ہیں۔ آئیں، ان سے ملیں۔</div></li>
   <li><span class="do">دوستوں سے ملیں (۲ منٹ)۔</span> ایک حرف سے کاغذ ہٹائیں۔ اس کی آواز بولیں۔ بچے آپ کے بعد وہی آواز بولیں اور حرف کو ہاتھ ہلائیں۔ پہلے ا، پھر ب، پ، ت، ٹ۔</li>
   <li><span class="do">کون سا حرف چھپا ہے؟ (۲ منٹ)۔</span> ایک حرف کو دوبارہ ڈھانپیں۔
    <div class="say">کون سا حرف چھپا ہے؟</div>بچے اس کی آواز بتائیں۔ کاغذ ہٹا کر دیکھیں۔ تین بار کھیلیں: ا، پھر ٹ، پھر ب۔</li>
  </ol></div>

 <div class="box teal"><h2><span class="en">Today's goal</span>آج کا ہدف</h2><div style="font-size:12.5pt;font-weight:700;line-height:1.9">ا، ب، پ، ت اور ٹ کی آواز بولیں، ان کے تصویر والے لفظ بتائیں اور ہر حرف لکھیں۔</div></div>

 <div class="board"><h3>Write on the board &nbsp;·&nbsp; بورڈ پر لکھیں</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.2"><div style="font-size:8.8pt;color:#BFD0C8;line-height:1.8">آج کے حروف</div>
    <div style="font-size:30pt;line-height:1.5;letter-spacing:0;word-spacing:.35em">{" ".join(LETTERS)}</div></div>
   <div style="flex:1;border-inline:.4mm dashed #7E9A8F;padding:0 4mm">
    <div style="font-size:8.8pt;color:#BFD0C8;line-height:1.8">تصویر والے الفاظ</div>
    <div style="font-size:13pt;line-height:1.85">{"<br>".join(f"{l} &nbsp;{WORD[l]}" for l in LETTERS)}</div></div>
   <div style="flex:1;font-size:10.2pt;line-height:1.85"><div style="font-size:8.8pt;color:#BFD0C8">ہمارے چار کام</div>
    <b style="color:#FFD966">۱</b> آواز بولیں<br><b style="color:#FFD966">۲</b> تصویر کا لفظ بولیں<br><b style="color:#FFD966">۳</b> ٹریس کریں<br><b style="color:#FFD966">۴</b> لکھیں</div>
  </div></div>
</div>
{F(2)}</section>"""


# ---------------- PAGE 3 ----------------
def letter_row(i, l):
    return (f'<div style="display:flex;gap:3mm;align-items:center;border:.4mm solid var(--line);border-radius:3mm;padding:.6mm 3mm;margin-bottom:1.2mm;background:#fff">'
            f'<div style="width:14mm;flex:none;text-align:center"><span class="num" style="width:6.4mm;height:6.4mm;font-size:10pt">{ur(i)}</span>'
            f'<div class="small" style="line-height:1.5">۴ منٹ</div></div>'
            f'<div style="flex:none">{tile(l, 22, 21, 30)}</div>'
            f'<div style="flex:none" title="stroke order">{stroke_box(l, 40)}</div>'
            f'<div style="width:19mm;flex:none">{pic(l)}</div>'
            f'<div style="flex:1;font-size:9.6pt;line-height:1.7"><div style="font-size:14pt;font-weight:700;line-height:1.5">{WORD[l]}</div>'
            f'<div><b>آواز:</b> <b class="sn" style="font-size:12pt">{SOUND[l]}</b> <span class="small">{HOW[l]}</span></div>'
            f'<div><b>دھیان دیں:</b> {LOOK[l]}</div></div></div>')


def page3():
    rows = "".join(letter_row(i + 1, l) for i, l in enumerate(LETTERS))
    blocks = [("آواز بولیں", "۱ منٹ", "حرفی کارڈ دکھائیں اور آواز بولیں۔ بچے دو بار دہرائیں۔"),
              ("تصویر کا لفظ", "۱ منٹ", "تصویر دکھائیں اور لفظ بولیں۔ پہلی آواز پر زور دیں۔ بچے دہرائیں۔"),
              ("ٹریس کریں", "۱ منٹ", "ہوا میں، پھر میز پر انگلی سے حرف ٹریس کریں۔ ساتھ آواز بولیں۔"),
              ("لکھیں", "۱ منٹ", "بورڈ پر حرف لکھیں۔ بچے تختی یا کاپی پر لکھیں اور چارٹ سے ملائیں۔")]
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:.8mm 2.4mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm"><span class="n2" style="width:6mm;height:6mm;font-size:9.5pt">{ur(i+1)}</span><b style="font-size:10pt">{t}</b><span class="small" style="margin-inline-start:auto">{m}</span></div><div style="font-size:8.8pt;line-height:1.75">{d}</div></div>' for i, (t, m, d) in enumerate(blocks))
    return f"""<section class="page">
{bar2("میں کر کے دکھاؤں", "I do · teach new letters", "پانچ حروف، ہر حرف کے لیے چار کام", "۲۰ منٹ")}
<div class="content">
 <div class="box sky" style="padding:1.6mm 4mm"><h2 style="margin-bottom:.4mm"><span class="en">Four actions</span>ہر حرف کے لیے یہی ۴ کام <span class="t">ہر حرف ۴ منٹ</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small">ا کے لیے چاروں کام کریں۔ پھر یہی ب، پ، ت اور ٹ کے لیے دہرائیں۔ ٹریس کرتے وقت تیر کی سمت دیکھیں: <b>۱</b> حرف کا جسم، <b>۲</b> نقطے یا نشانی۔</div></div>
 {rows}
 <div class="box mint" style="margin:1.6mm 0 0"><h2 style="margin-bottom:.4mm"><span class="en">Worked example · Watch for</span>مثال: حرف ب اور خیال رکھیں</h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.25">{talk("teacher_point", '<b class="t">کہیں:</b> یہ ب ہے۔ اس کی آواز بْ ہے۔ میرے ساتھ بولیں: بْ۔<br><b class="t">کہیں:</b> تصویر بٹن ہے۔ بٹن کی پہلی آواز بْ ہے۔ بولیں: بْ۔', 20)}
    <div style="font-size:9pt;line-height:1.75;margin-top:.8mm">پھر ب کو ہوا میں ٹریس کریں، میز پر ٹریس کریں، تختی پر لکھیں اور چارٹ سے ملائیں۔</div></div>
   <div style="flex:1"><ul style="font-size:8.9pt;line-height:1.75;margin:0">
    <li>آوازیں چھوٹی اور صاف بولیں: بْ، “با” نہیں۔</li>
    <li>ب، پ، ت، ٹ کی شکل ملتی ہے۔ فرق نقطوں کا ہے۔ نقطے انگلی سے گنوائیں۔</li>
    <li>ت میں زبان دانتوں کے پیچھے، ٹ میں زبان کی نوک مڑی ہوئی۔ دونوں الگ الگ سنائیں۔</li></ul></div>
  </div></div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4 ----------------
def page4():
    return f"""<section class="page">
{bar2("ہم سب مل کر", "We do · practise together", "پوری کلاس اپنی میز کے پاس کھڑی ہو کر", "۱۲ منٹ")}
<div class="content">
 <div class="box mint"><h2><span class="en">1 · Say the sounds</span>۱۔ آواز بولیں <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.7">{steps(["بچے اپنی میز کے پاس کھڑے ہوں۔ چارٹ پر ایک حرف کی طرف اشارہ کریں۔",
          "پہلا راؤنڈ: ا، ب، پ، ت، ٹ کی طرف ترتیب سے اشارہ کریں۔ پوری کلاس <b>آواز</b> بولے۔",
          "دوسرا راؤنڈ: اسی طرح ملی جلی ترتیب میں اشارہ کریں: ب، ا، ت، پ، ٹ۔"])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">آوازیں</div>
    <div style="font-size:12pt;line-height:1.8">{sounds(CHANT_ORDER)}</div><div class="small">ہر آواز چھوٹی اور صاف، آخر میں کوئی آواز نہیں۔</div></div></div></div>

 <div class="box sky"><h2><span class="en">2 · Show me</span>۲۔ مجھے دکھاؤ <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.7">{steps(["بچے اپنی <b>ڈیسک پٹی</b> سامنے رکھیں۔",
          "ایک آواز دو بار بولیں۔ بچے پٹی پر وہ حرف چھوئیں۔",
          "بچوں کی انگلیاں دیکھیں۔ کسی نے غلط حرف چھوا؟ چارٹ پر صحیح حرف دکھائیں اور سب مل کر آواز بولیں۔"])}
    <div style="margin-top:1.4mm">{talk("teacher_point", '<b class="t">کہیں:</b> مجھے دکھاؤ ... بْ!', 18)}</div></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">آوازیں، اسی ترتیب میں</div>
    <div style="font-size:12pt;line-height:1.8">{sounds(SHOW_ME)}</div></div>
  </div></div>

 <div class="box cream"><h2><span class="en">3 · Write it</span>۳۔ لکھیں <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.7">{steps(["بچے تختی یا کاپی اور پنسل اٹھائیں۔",
          "آواز بولیں: <i>“لکھیں ... تْ۔”</i> بچے وہ حرف لکھیں۔ پھر بورڈ پر وہ حرف لکھیں۔",
          "بچے اپنا حرف بورڈ اور چارٹ سے ملائیں اور ضرورت ہو تو ٹھیک کریں۔"])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">اس ترتیب میں بولیں</div><div style="font-size:12pt;line-height:1.8">{sounds(WRITE_CALLS)}</div></div></div></div>

 <div class="box navy" style="margin-bottom:0"><div style="display:flex;gap:5mm">
  <div style="flex:1.1"><h2><span class="en">Check before moving on</span>آگے بڑھنے سے پہلے جانچ</h2><div style="line-height:1.85">۴ یا ۵ بچوں سے سنیں: آپ جس حرف کی طرف اشارہ کریں، بچہ اس کی آواز بتائے۔<br><b style="color:var(--gold)">زیادہ تر درست؟</b> آگے بڑھیں۔ <b style="color:var(--gold)">زیادہ تر غلط؟</b> ۲ منٹ “مجھے دکھاؤ” دوبارہ کریں۔</div></div>
  <div style="flex:1;border-inline-start:.4mm solid #2B4A6B;padding-inline-start:5mm"><h2><span class="en">While you walk around</span>کلاس میں گھومتے ہوئے</h2><ul style="line-height:1.85;margin:0"><li>انگلی صحیح حرف پر ہے؟</li><li>آوازیں چھوٹی اور صاف ہیں؟</li><li>حرف صحیح سمت میں لکھے جا رہے ہیں؟</li><li>ہر بار مختلف بچے سنیں: ۴ یا ۵، سب نہیں۔</li></ul></div>
 </div></div>
</div>
{F(4)}</section>"""


# ---------------- PAGE 5 ----------------
def page5():
    t1 = " ، ".join(f'<b style="font-size:13pt">{l}</b>' for l in T1_LETTERS)
    t2 = " &nbsp; ".join(f'<b>{WORD[l]} ← <span style="font-size:13pt">{l}</span></b>' for l in T2_PICS)
    t3 = "".join(f'<span style="display:inline-block;margin-inline-start:4mm"><b style="font-size:12pt">{tg}:</b> ' + "، ".join(ur(i + 1) for i, o in enumerate(opts) if o == tg) + '</span>' for tg, opts in T3_ROWS)
    key = ""
    for i, it in enumerate(EXIT):
        if it["options"]:
            opt = "".join(f'<span style="width:7mm;height:7mm;display:inline-flex;align-items:center;justify-content:center;font-size:12pt;line-height:1;'
                          f'border:.3mm solid #9AA6B5;border-radius:50%;margin-inline-start:.8mm;{"background:#F5B301;" if ch == it["answer"] else ""}">{ch}</span>' for ch in it["options"])
        else:
            opt = f'<span class="small" style="color:var(--ink)">بچہ لکھے</span> <b style="font-size:14pt">{it["answer"]}</b>'
        key += f'<div style="display:flex;align-items:center;gap:1.6mm;line-height:1.9"><b style="width:4mm">{ur(i+1)}</b>{opt}<span class="small">{SOUND[it["sound"]]}</span></div>'
    return f"""<section class="page">
{bar2("اکیلے اور خروجی جانچ", "You do · exit check", "اکیلے (۸ منٹ)، پھر خروجی جانچ (۱۰ منٹ)", "۱۸ منٹ")}
<div class="content">
 <div class="box mint" style="padding-bottom:1.4mm"><h2 style="margin-bottom:0"><span class="en">Your turn</span>اکیلے <span class="t">۸ منٹ</span></h2>
  <p class="small" style="margin:0 0 .8mm">طالب علم کی ورک شیٹ، صفحہ ۱۔ ہر کام کی پہلی لائن سب مل کر کریں۔ بچے اپنا کام ڈیسک پٹی سے خود جانچیں۔ جب مکمل ہو جائے تو ورک شیٹ جمع کروائیں۔</p>
  <table class="ans"><tr><th style="width:42mm">کام</th><th style="width:16mm">ورک شیٹ</th><th style="width:14mm">وقت</th><th>جوابات</th></tr>
   <tr><td><b>۱</b> ٹریس اور نقل</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td>{t1}</td></tr>
   <tr><td><b>۲</b> تصویر اور پہلا حرف ملائیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td>{t2}</td></tr>
   <tr><td><b>۳</b> وہی حرف گھیریں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۲ منٹ</td><td><span class="small" style="color:var(--ink)">دائیں سے گنیں:</span> {t3}</td></tr>
  </table></div>

 <div class="box sky"><h2><span class="en">Exit check</span>خروجی جانچ <span class="t">۱۰ منٹ</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.15;font-size:9.6pt">
    <p><b>حصہ الف: سنیں اور گھیریں (۶ منٹ)۔</b> <b>ورک شیٹ کا صفحہ ۲</b> دیں۔ بچے نام لکھیں۔ ہر آئٹم دو بار بولیں اور تقریباً ۳۰ سیکنڈ انتظار کریں۔</p>
    <div class="say" style="font-size:10.6pt">نمبر ایک۔ جو حرف بْ کہتا ہے، اس کے گرد دائرہ لگائیں۔</div>
    <p style="margin-top:.4mm">بچے اکیلے کام کریں۔ آئٹم ۱ تا ۴ آواز سن کر گھیرنا ہے، آئٹم ۵ لکھنا ہے۔</p>
    <p><b>حصہ ب: بول کر سنائیں (۴ منٹ)۔</b> <b>۴ یا ۵ بچوں</b> سے سنیں، ہر دن مختلف گروپ۔ چارٹ پر ب، ٹ، ا، پ یا ت کی طرف اشارہ کریں۔ بچہ اس کی آواز بتائے۔</p></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm"><div class="small" style="font-weight:700;color:var(--navy)">حصہ الف: جوابات</div>{key}</div>
  </div></div>

 <div class="row">
  <div class="box mint"><h2><span class="en">Score and decide</span>نتیجہ دیکھ کر فیصلہ کریں</h2>
   <div style="font-size:9.6pt;line-height:1.85"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ درست۔<br><b>مشق چاہیے:</b> ۳ درست۔ دن ۲ پر ان بچوں کے ساتھ “مجھے دکھاؤ” دوبارہ کریں۔<br><b>دوبارہ پڑھائیں:</b> ۲ یا کم درست۔ جو حروف غلط ہوئے، ان کے ۴ کام چھوٹے گروپ میں دہرائیں۔
   <div class="small">ہر بچے کی حالت کلاس ٹریکر پر لکھیں۔ نمبر بلند آواز میں نہ بتائیں۔</div></div></div>
  <div class="navy box"><h2><span class="en">Key facts to remember</span>یاد رکھنے کی باتیں</h2>
   <div style="font-size:10pt;line-height:1.85">✓ ہر حرف کی ایک <b>آواز</b> ہے۔<br>✓ ہر حرف کی ایک الگ <b>شکل</b> ہے۔<br>✓ حروف <b>دائیں سے بائیں</b> لکھے جاتے ہیں۔</div>
   <div class="small" style="color:#C9D6E6">جانے سے پہلے کلاس کے ساتھ یہ تین جملے دہرائیں۔</div></div>
 </div>

 <div class="box grey" style="margin-bottom:1.4mm"><b><span class="en" style="margin-inline-end:3mm">At home · optional</span>گھر پر (اختیاری):</b> گھر میں کسی کو ا، ب، پ، ت، ٹ کی آوازیں اور انار، بٹن، پری، توا، ٹرک سنائیں۔</div>
 <div class="small" style="line-height:1.7">{PASS_NOTE}</div>
</div>
{F(5)}</section>"""


def build():
    html = head_html2("Level 1 Urdu Day 1 - Lesson Plan v2") + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS
    out = os.path.join(WORK, "lpu2.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
